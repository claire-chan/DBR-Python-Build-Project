import os
import sys
import cv2
import json
from dbr import *

#you can change the following four variables' value to your own value.
license_key = "Input your own license"
#license_server = "Input the name/IP of the license server"
input_json_string = '{"ImageParameter" : { "BarcodeFormatIds" : [ "BF_ALL" ], "DeblurLevel" : 9, "Description" : "", "ExpectedBarcodesCount" : 0, "MaxAlgorithmThreadCount" : 4, "Name" : "IP_1", "Timeout" : 10000}, "Version" : "3.0"}'
append_json_string = '{"ImageParameter" : { "BarcodeFormatIds" : [ "BF_ALL" ], "DeblurLevel" : 9, "Description" : "", "ExpectedBarcodesCount" : 15, "MaxAlgorithmThreadCount" : 2, "Name" : "IP_2", "Timeout" : 20000}, "Version" : "3.0"}'
#conflict_mode should be a value which is in EnumConflictMode.
conflict_mode = EnumConflictMode.CM_OVERWRITE

reader = BarcodeReader()

reader.init_license(license_key)
#reader.init_license_from_server(license_server, license_key)
#license_content = reader.output_license_to_string()
#reader.init_license_from_license_content(license_key, license_content)

error = reader.init_runtime_settings_with_string(input_json_string)
if error[0] != EnumErrorCode.DBR_OK:
    print(error[1])

error = reader.append_template_string_to_runtime_settings(append_json_string, conflict_mode)
if error[0] != EnumErrorCode.DBR_OK:
    print(error[1])

template_names = reader.get_all_template_names()
print(template_names)

save_json_string = reader.output_settings_to_json_string()
print(save_json_string)