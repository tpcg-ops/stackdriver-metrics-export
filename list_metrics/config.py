#!/usr/bin/env python

# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

PUBSUB_TOPIC = "metrics_list"
AGGREGATION_ALIGNMENT_PERIOD = "3600s"
PUBSUB_VERIFICATION_TOKEN = "9110614f-ce4a-4a80-a2c8-01f681859954"
LAST_END_TIME_FILENAME = "last_end_time.txt"
PAGE_SIZE = 500
BIGQUERY_DATASET = "metric_export"
BIGQUERY_STATS_TABLE = "sd_metrics_stats"
BIGQUERY_PARAMS_TABLE = "sd_metrics_params"
WRITE_BQ_STATS_FLAG = True
WRITE_MONITORING_STATS_FLAG = True
ALL = "*"

INCLUSIONS = {
    "include_all": "",
    "metricTypes": [
        #       { "metricType": "compute.googleapis.com/instance/cpu/utilization" },
        #       { "metricType": "compute.googleapis.com/instance/disk/write_ops_count" }
    ],
    "metricTypeGroups": [
        #        { "metricTypeGroup": "bigquery.googleapis.com" }
    ],
}

EXCLUSIONS = {
    "exclude_all": "",
    "metricKinds": [{"metricKind": "GAUGE", "valueType": "STRING"}],
    "metricTypes": [],
    "metricTypeGroups": [
        {"metricTypeGroup": "aws.googleapis.com"},
        {"metricTypeGroup": "external.googleapis.com"},
    ],
}

METRIC_TYPES = [
    {
        "name": "compute",
        "metric_type_prefix": "compute.googleapis.com/",
        "metric_type": [
            "guest/cpu/usage_time",
            "disk/async_replication/sent_bytes_count",
            "disk/regional/replica_state",
        ],
    }
]
