# --
# File: ./mobileiron/mobileiron_consts.py
#
# Copyright (c) Phantom Cyber Corporation, 2014-2018
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

MOBILEIRON_JSON_DEVICE_URL = "url"
MOBILEIRON_JSON_USERNAME = "username"
MOBILEIRON_JSON_PASSSWORD = "password"
MOBILEIRON_JSON_START_INDEX = "start_index"
MOBILEIRON_JSON_LIMIT = "limit"
MOBILEIRON_JSON_TOTAL_DEVICES = "total_devices"
MOBILEIRON_JSON_UUID = "uuid"
MOBILEIRON_JSON_REASON = "reason"

MOBILEIRON_ERR_INVALID_UUID = "Input device uuid not proper format"
MOBILEIRON_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
MOBILEIRON_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
MOBILEIRON_ERR_SERVER_CONNECTION = "Connection failed"
MOBILEIRON_ERR_FROM_SERVER = "API failed, Status code: {status}, Detail: {detail}"
MOBILEIRON_MSG_GET_DEVICES_TEST = "Querying devices to check credentials"
MOBILEIRON_ERR_JSON_PARSE = "Unable to parse response as JSON, response '{data}'"
MOBILEIRON_USING_BASE_URL = "Using url: {base_url}"
MOBILEIRON_ERR_INVALID_INPUT = "Invalid '{param}' input value"
