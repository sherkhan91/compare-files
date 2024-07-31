from itertools import zip_longest


middle_permissions = [
    {
        "SubPage": {"Rule": False, "Data_New": True},
        "SubPage_searc": {"MostRecentDocs": True, "AdvancedSearch": True, "DocumentTracking": True, "ReprocessFiles": True,
                    "ResendFiles": True},
        "Edit": {"NewSearch": True, "TrackDoc": True, "ShowRecent": True},
        "Delete": {"AdvancedSearch": True, "DocumentTracking": True, "ShowRecent": True},
        "Download": {"BasicSearch": True, "TrackDoc": True, "ShowRecent": True},
        "Report": {"MySearch": False},
        "DocLog": {"AdvancedSearch": True, "DocumentTracking": True, "ShowRecent": True},
        "Resend_Reprocess_Files": {"AdvancedSearch": True, "DocumentTracking": True, "ShowRecent": True}
    },
    {},
    {"MainPage": {"Dashboard": False},
        "SubPage": {"DayToDaySupport": True, "Analytics": True,
                                                    "CustomerCare": True, "SalesExecutive": True}, "Edit": {},
        "Delete": {}, "Download": {}, "Report": {}, "Document_Trail": {},
                                        "Resend_Reprocess_Files": {}},
    {
    "MainPage": {"Partners": True},
     "Edit": {"SaleRelations": True},
     "Delete": {"TradingRelationships": True},
     "Download": {"TradingRelationships": True},
     "Report": {}, "DocumentLog": {},
     "Resend_Reprocess_Files": {}
     },
    {"MainPage": {"Analytics": True},
     "SubPage": {"TradingPartnersSummary": True, "Analytics": True, "document-summary": True, "TransactionAck": True},
     "Edit": {}, "Delete": {},
     "Download": {"Analytics": True, "document-summary": True, "TradingPartnersSummary": True, "TransactionAck": True},
     "Report": {}, "Document_Trail": {}, "Resend_Reprocess_Files": {}},
    {"MainPage": {"SLAManagement": True},
     "SubPage": {"TransactionOverdue": True, "TransactionalSLA": True},
     "Delete": {"TransactionalSLA": True},
     "Download": {},
     "Analysis": {"TransactionalSLA": True},
     "DocLog": {},
     "Resend_Reprocess_Files": {}}
]

existing_permissions = [
    {
        "MainPage": {"Data": False, "Data_New": True},
        "SubPage": {"MostRecentDocs": True, "AdvancedSearch": True, "DocumentTracking": True, "ReprocessFiles": True,
                    "ResendFiles": True},
        "Edit": {"AdvancedSearch": True, "DocumentTracking": False, "MostRecentDocs": True},
        "Delete": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True},
        "Download": {"My_AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True},
        "Report": {"MySearch": False},
        "Document_Trail": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True},
        "Resend_Reprocess_Files": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True}
    },
    {},
    {"MainPage": {"Dashboard": True},
        "SubPage": {"DayToDaySupport": True, "EDIAnalyst": True,
                                                    "CustomerServiceRepo": True, "SalesExecutive": True}, "Edit": {},
        "Delete": {}, "Download": {}, "Report": {}, "Document_Trail": {},
                                        "Resend_Reprocess_Files": {}},
    {
    "MainPage": {"TradingPartners": True},
     "Edit": {"TradingRelationships": True},
     "Delete": {"TradingRelationships": True},
     "Download": {"TradingRelationships": True},
     "Report": {}, "Document_Trail": {},
     "Resend_Reprocess_Files": {}
     },
    {"MainPage": {"Analytics": True},
     "SubPage": {"TradingPartnersSummary": True, "Analytics": True, "document-summary": True, "TransactionAck": True},
     "Edit": {}, "Delete": {},
     "Download": {"Analytics": True, "document-summary": True, "TradingPartnersSummary": True, "TransactionAck": True},
     "Report": {}, "Document_Trail": {}, "Resend_Reprocess_Files": {}},
    {"MainPage": {"SLAManagement": True},
     "SubPage": {"TransactionOverdue": True, "TransactionalSLA": True},
     "Delete": {"TransactionalSLA": True},
     "Download": {},
     "Report": {"TransactionalSLA": True},
     "Document_Trail": {},
     "Resend_Reprocess_Files": {}}
]

new_permissions = [
    {
        "MainPage": {"Data": True},
        "SubPage": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True, "ReprocessFiles": True,
                    "ResendFiles": True},
        "Edit": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True},
        "Delete": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True },
        "Download": {"AdvancedSearch": True, "DocumentTracking": True, "MostRecentDocs": True},
        "Report": {},
        "Document_Trail": {"AdvancedSearch": True, "DocumentTracking": True,"MostRecentDocs": True},
        "Resend_Reprocess_Files": {
            "AdvancedSearch": True,
            "DocumentTracking": True,
            "MostRecentDocs": True,
        }
    },
    {
        "MainPage": {
            "Alerts": True
        },
        "SubPage": {
            "Anomalies": True,
            "Errors": True,
            "Notifications": True,
            "TransactionAcknowledgement": True
        },
        "Edit": {
            "Notifications": True,
        },
        "Delete": {
            "Notifications": True,
        },
        "Download": {
            "Errors": True,
            "TransactionAcknowledgement": True
        },
        "Report": {
        },
        "Document_Trail": {
        },
        "Resend_Reprocess_Files": {
        }
    },
    {
        "MainPage": {
            "Dashboard": True
        },
        "SubPage": {
            "CustomerServiceRepo": True,
            "DayToDaySupport": True,
            "EDIAnalyst": True,
            "SalesExecutive": True
        },
        "Edit": {

        },
        "Delete": {

        },
        "Download": {

        },
        "Report": {

        },
        "Document_Trail": {
        },
        "Resend_Reprocess_Files": {

        }
    },
    {
        "MainPage": {
            "TradingPartners": True
        },
        "SubPage": {
            "TradingPartnerSetup": True,
            "TradingRelationships": True
        },
        "Edit": {
            "TradingRelationships": True
        },
        "Delete": {
            "TradingRelationships": True
        },
        "Download": {
            "TradingRelationships": True
        },
        "Report": {
        },
        "Document_Trail": {
        },
        "Resend_Reprocess_Files": {
        }
    },
    {
        "MainPage": {
            "Analytics": True
        },
        "SubPage": {
            "Analytics": True,
            "document-summary": True,
            "TradingPartnersSummary": True,
            "TransactionAck": True
        },
        "Edit": {
        },
        "Delete": {
        },
        "Download": {
            "Analytics": True,
            "document-summary": True,
            "TradingPartnersSummary": True,
            "TransactionAck": True
        },
        "Report": {
        },
        "Document_Trail": {
        },
        "Resend_Reprocess_Files": {
        }
    },
    {
        "MainPage": {
            "SLAManagement": True
        },
        "SubPage": {
            "TransactionalSLA": True,
        },
        "Edit": {
            "TransactionalSLA": True,
        },
        "Delete": {
            "TransactionalSLA": True,
        },
        "Download": {
        },
        "Report": {
            "TransactionalSLA": True,
        },
        "Document_Trail": {
        },
        "Resend_Reprocess_Files": {
        }
    },
    {
        "MainPage": {
            "Reports": True
        },
        "SubPage": {
            "ConfigureReports": True,
            "InboundActivity": True,
            "OutboundActivity": True,
            "PreconfiguredReports": True,
            "SavedReports": True,
            "ScheduleReport": True
        },
        "Edit": {
            "ConfigureReports": True,
            "ScheduleReport": True
        },
        "Delete": {
            "ConfigureReports": True,
            "ScheduleReport": True
        },
        "Download": {
            "InboundActivity": True,
            "OutboundActivity": True,
            "PreconfiguredReports": True,
            "SavedReports": True,
        },
        "Report": {
            "ConfigureReports": True,
            "PreconfiguredReports": True,
            "SavedReports": True,
            "ScheduleReport": True
        },
        "Document_Trail": {
            "InboundActivity": True,
            "OutboundActivity": True,
        },
        "Resend_Reprocess_Files": {
            "InboundActivity": True,
            "OutboundActivity": True,
        }
    }

]

updated_permissions = []

counter = 0

diff_count = len(new_permissions) - len(existing_permissions)
print("diff count", diff_count)
new_permissions_cut = new_permissions[0:(len(new_permissions)-diff_count)]
print("length og new permissions after cut", len(new_permissions_cut))
for new_permission in new_permissions_cut:
    update_permission_obj = existing_permissions[counter]
    for key, value in new_permission.items():
        print(f"HEADER KEY: {key}, HEADER VALUE: {value}")
        if update_permission_obj.get(key) is None:
            print("sorry got a new HEADER key so appending it")
            update_permission_obj[key] = value
        elif update_permission_obj.get(key) == value:
            print("do nothing for header values because both dictionaries are same.")
        else:
            print("sorry dictionary is different going inside to check")
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    print(f"NESTED KEY: {key2}, NESTED VALUE: {value2}")
                    if update_permission_obj[key].get(key2) is None:
                        print(f"this was a new key: {key2} with value: {value2}")
                        update_permission_obj[key][key2] = value2
                    elif update_permission_obj[key].get(key2) == value2:
                        print("do nothing for inner values because both are same.")
                    else:
                        print("sorry old value is different than new one so leaving as it is")

                # if nested dictionary has something which is not present in new then delete.
                for del_key in list(update_permission_obj[key].keys()):
                    print("checking del_key", del_key)
                    if del_key not in new_permission[key].keys():
                        print(f"yes deleting : {del_key}")
                        del update_permission_obj[key][del_key]

            else:
                print(f"sorry there is something wrong, I don't know what is this: {type(value)}, {value}")

    print(f"existing_permission: {existing_permissions[counter]}")
    print(f"new_permission: {new_permission}")

    keyorder = ['MainPage', 'SubPage', 'Edit', 'Delete', 'Download', 'Report', 'Document_Trail', 'Resend_Reprocess_Files']
    temp_dict = {k: update_permission_obj[k] for k in keyorder if k in update_permission_obj}
    print(f"updated_permission: {temp_dict}")
    updated_permissions.append(temp_dict)
    counter += 1

for new_permission1 in new_permissions[(len(new_permissions)-diff_count):]:
    print("new_permission1", new_permission1)
    updated_permissions.append(new_permission1)

print("updated permission list", updated_permissions)
