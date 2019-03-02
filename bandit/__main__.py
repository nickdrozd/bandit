#!/usr/bin/env python3
from bandit.cli import main
import yappi

yappi.set_clock_type('cpu')
yappi.start()

try:
    main.main()
except:
    print('getting stats')
    stats = yappi.get_func_stats()
    stats.save('yappi.callgrind', type='callgrind')
    print('done')
