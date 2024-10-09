#!/usr/bin/python3
"""DASH generator for ROUTE GROUP"""

import os
import sys

from dpugen.confbase import ConfBase
from dpugen.confutils import common_main
from dpugen.confutils import create_uuid_from_string


class RouteGroup(ConfBase):

    def __init__(self, params={}):
        super().__init__(params)
        self.num_yields = 0

    def items(self):
        print('  Generating %s ...' % os.path.basename(__file__), file=sys.stderr)
        p = self.params
        ip_int = self.cooked_params

        for eni_index, eni in enumerate(range(p.ENI_START, p.ENI_START + p.ENI_COUNT * p.ENI_STEP, p.ENI_STEP)):  # Per ENI
            route_group_name = 'route-group-%d' % eni
            self.num_yields += 1
            yield {
                "DASH_ROUTE_GROUP_TABLE:%s" % route_group_name : {
                    "guid": create_uuid_from_string(route_group_name),
                    "version":"1"
                },
                "OP": "SET"
            }


if __name__ == '__main__':
    conf = RouteGroup()
    common_main(conf)
