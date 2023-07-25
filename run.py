#!/usr/bin/env python

import typeguard
typeguard.install_import_hook(['compressors', 'data', 'experiments', 'utils'])
import main_text

if __name__ == '__main__':
    main_text.main()
