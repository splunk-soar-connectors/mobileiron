[comment]: # "Auto-generated SOAR connector documentation"
# MobileIron

Publisher: Splunk Community  
Connector Version: 2\.0\.0  
Product Vendor: MobileIron  
Product Name: MobileIron  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.1\.0  

This app allows endpoint management on MobileIron by implementing containment and investigative actions

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a MobileIron asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**url** |  required  | string | Device URL, e\.g\. https\://mycore\.mobileiron\.com
**verify\_server\_cert** |  optional  | boolean | Verify server certificate
**username** |  optional  | string | Username
**password** |  optional  | password | Password

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity\. This action runs a quick query on the device to check the connection and credentials  
[list devices](#action-list-devices) - Get a list of active devices  
[lock device](#action-lock-device) - Lock the device  
[unlock device](#action-unlock-device) - Unlock the device  
[get system info](#action-get-system-info) - Get info about a device  

## action: 'test connectivity'
Validate the asset configuration for connectivity\. This action runs a quick query on the device to check the connection and credentials

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'list devices'
Get a list of active devices

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start\_index** |  required  | The start index of a device | numeric | 
**limit** |  required  | Total number of devices to return | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.limit | string | 
action\_result\.parameter\.start\_index | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.comment | string | 
action\_result\.data\.\*\.userFirstName | string | 
action\_result\.data\.\*\.countryCode | numeric | 
action\_result\.data\.\*\.userSource | numeric | 
action\_result\.data\.\*\.userId | numeric | 
action\_result\.data\.\*\.deviceCount | numeric | 
action\_result\.data\.\*\.homeOperator | string | 
action\_result\.data\.\*\.languageCountryId | numeric | 
action\_result\.data\.\*\.operator | string | 
action\_result\.data\.\*\.platformType | string | 
action\_result\.data\.\*\.createdAt | string | 
action\_result\.data\.\*\.principal | string | 
action\_result\.data\.\*\.countryId | numeric | 
action\_result\.data\.\*\.uuid | string |  `mobileiron device uuid` 
action\_result\.data\.\*\.languageId | numeric | 
action\_result\.data\.\*\.platform | string | 
action\_result\.data\.\*\.mdmProfileUrlId | numeric | 
action\_result\.data\.\*\.quarantinedStatus | numeric | 
action\_result\.data\.\*\.details\.\*\.entry\.\*\.value | string | 
action\_result\.data\.\*\.details\.\*\.entry\.\*\.key | string | 
action\_result\.data\.\*\.notifyUser | boolean | 
action\_result\.data\.\*\.lastConnectedAt | string | 
action\_result\.data\.\*\.registeredAt | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.operatorId | numeric | 
action\_result\.data\.\*\.currentPhoneNumber | string | 
action\_result\.data\.\*\.wipeReason | numeric | 
action\_result\.data\.\*\.countryName | string | 
action\_result\.data\.\*\.emailAddress | string | 
action\_result\.data\.\*\.userDisplayName | string | 
action\_result\.data\.\*\.employeeOwned | boolean | 
action\_result\.data\.\*\.regType | string | 
action\_result\.data\.\*\.\@id | string | 
action\_result\.data\.\*\.manufacturer | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.compliance | numeric | 
action\_result\.data\.\*\.mdmManaged | boolean | 
action\_result\.data\.\*\.clientId | numeric | 
action\_result\.data\.\*\.regCount | numeric | 
action\_result\.data\.\*\.blockReason | numeric | 
action\_result\.data\.\*\.emailDomain | string |  `domain` 
action\_result\.data\.\*\.userUUID | string |  `mobileiron user uuid` 
action\_result\.data\.\*\.userLastName | string | 
action\_result\.data\.\*\.model | string | 
action\_result\.data\.\*\.statusCode | numeric | 
action\_result\.summary\.total\_devices | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.nonGMS | boolean | 
action\_result\.data\.\*\.authOnly | boolean | 
action\_result\.data\.\*\.multiUser | boolean | 
action\_result\.data\.\*\.TLVVersion | numeric | 
action\_result\.data\.\*\.migrationStatus | string | 
action\_result\.data\.\*\.temporarySessionOnly | boolean |   

## action: 'lock device'
Lock the device

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**uuid** |  required  | Device UUID | string |  `mobileiron device uuid` 
**reason** |  optional  | Reason to lock | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.reason | string | 
action\_result\.parameter\.uuid | string |  `mobileiron device uuid` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unlock device'
Unlock the device

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**uuid** |  required  | Device UUID | string |  `mobileiron device uuid` 
**reason** |  optional  | Reason to lock | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.reason | string | 
action\_result\.parameter\.uuid | string |  `mobileiron device uuid` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get system info'
Get info about a device

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**uuid** |  required  | Device UUID | string |  `mobileiron device uuid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.uuid | string |  `mobileiron device uuid` 
action\_result\.data\.\*\.device\.comment | string | 
action\_result\.data\.\*\.device\.userFirstName | string | 
action\_result\.data\.\*\.device\.countryCode | numeric | 
action\_result\.data\.\*\.device\.userSource | numeric | 
action\_result\.data\.\*\.device\.userId | numeric | 
action\_result\.data\.\*\.device\.deviceCount | numeric | 
action\_result\.data\.\*\.device\.homeOperator | string | 
action\_result\.data\.\*\.device\.languageCountryId | numeric | 
action\_result\.data\.\*\.device\.operator | string | 
action\_result\.data\.\*\.device\.platformType | string | 
action\_result\.data\.\*\.device\.createdAt | string | 
action\_result\.data\.\*\.device\.principal | string | 
action\_result\.data\.\*\.device\.countryId | numeric | 
action\_result\.data\.\*\.device\.uuid | string |  `mobileiron device uuid` 
action\_result\.data\.\*\.device\.languageId | numeric | 
action\_result\.data\.\*\.device\.platform | string | 
action\_result\.data\.\*\.device\.mdmProfileUrlId | numeric | 
action\_result\.data\.\*\.device\.quarantinedStatus | numeric | 
action\_result\.data\.\*\.device\.details\.\*\.entry\.\*\.value | string | 
action\_result\.data\.\*\.device\.details\.\*\.entry\.\*\.key | string | 
action\_result\.data\.\*\.device\.notifyUser | boolean | 
action\_result\.data\.\*\.device\.lastConnectedAt | string | 
action\_result\.data\.\*\.device\.registeredAt | string | 
action\_result\.data\.\*\.device\.status | string | 
action\_result\.data\.\*\.device\.operatorId | numeric | 
action\_result\.data\.\*\.device\.currentPhoneNumber | string | 
action\_result\.data\.\*\.device\.wipeReason | numeric | 
action\_result\.data\.\*\.device\.countryName | string | 
action\_result\.data\.\*\.device\.emailAddress | string |  `email` 
action\_result\.data\.\*\.device\.userDisplayName | string | 
action\_result\.data\.\*\.device\.employeeOwned | boolean | 
action\_result\.data\.\*\.device\.regType | string | 
action\_result\.data\.\*\.device\.\@id | string | 
action\_result\.data\.\*\.device\.manufacturer | string | 
action\_result\.data\.\*\.device\.name | string | 
action\_result\.data\.\*\.device\.compliance | numeric | 
action\_result\.data\.\*\.device\.mdmManaged | boolean | 
action\_result\.data\.\*\.device\.clientId | numeric | 
action\_result\.data\.\*\.device\.regCount | numeric | 
action\_result\.data\.\*\.device\.blockReason | numeric | 
action\_result\.data\.\*\.device\.emailDomain | string |  `domain` 
action\_result\.data\.\*\.device\.userUUID | string |  `mobileiron user uuid` 
action\_result\.data\.\*\.device\.userLastName | string | 
action\_result\.data\.\*\.device\.model | string | 
action\_result\.data\.\*\.device\.statusCode | numeric | 
action\_result\.summary\.total\_devices | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.device\.nonGMS | boolean | 
action\_result\.data\.\*\.device\.authOnly | boolean | 
action\_result\.data\.\*\.device\.multiUser | boolean | 
action\_result\.data\.\*\.device\.TLVVersion | numeric | 
action\_result\.data\.\*\.device\.migrationStatus | string | 
action\_result\.data\.\*\.device\.temporarySessionOnly | boolean | 
action\_result\.data\.\*\.messages | string | 
action\_result\.data\.\*\.totalCount | numeric | 