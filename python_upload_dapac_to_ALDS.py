if __name__== "__main__":
import logging
import os, uuid

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

    #setx AZURE_STORAGE_CONNECTION_STRING ""  
    connect_str = os.environ.get("CONNECTIONSTRING")
    runner_file_path = os.environ.get("FILEPATH")
    container_name = os.environ.get("CONTAINER")
    
    print("Azure Blob Storage connect_str is :" + connect_str + " - for usage")
    
# Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    print("BlobServiceClient - created!")
    
# Create a unique name for the container
    #container_name = "githubactions-dacpac-from-runner" #str(uuid.uuid4())
# Create the container
#   container_client = blob_service_client.create_container(container_name)
# print("container_client - " + container_name  + " - created!")

# Create a file in the local data directory to upload and download
    local_file_name = "GITHUB_ACTIONDB_TESTING.dacpac" #str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(runner_file_path, local_file_name)

# Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name + " to blob conainer " + container_name + " .... !")

# Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

# Try to generate a delta script via sqlpackage.exe    
#    filepath = 'C:\Program Files (x86)\Microsoft SQL Server\140\DAC\bin\sqlpackage.exe /Action:Script /SourceFile:"C:\actions-runner\_work\GITHUB_ACTIONDB_TESTING\GITHUB_ACTIONDB_TESTING\bin\Release\GITHUB_ACTIONDB_TESTING.dacpac" /TargetFile:"C:\Users\ericp\Documents\SQL Server Management Studio\DAC Packages\GITHUB_ACTIONDB_TESTING.dacpac" /TargetDatabaseName:"GITHUB_ACTIONDB_TESTING" /OutputPath:"C:\Users\ericp\Documents\_WFA_Documents\Github_Actions_Work\dbscripting\delta_script.sql" /p:DropObjectsNotInSource=TRUE /p:ScriptDatabaseOptions=False /p:DoNotDropObjectTypes=Sequences;DatabaseRoles;Permissions;Credentials;ColumnEncryptionKeys;ColumnMasterKeys;Certificates;RoleMembership;SymmetricKeys;Users;Audits;CryptographicProviders;DatabaseAuditSpecifications;DatabaseScopedCredentials;Logins;ServerRoleMembership;ServerRoles /p:ExcludeObjectTypes=Aggregates;ApplicationRoles;Assemblies;AsymmetricKeys;BrokerPriorities;Certificates;ColumnEncryptionKeys;ColumnMasterKeys;Contracts;DatabaseRoles;DatabaseTriggers;Defaults;ExtendedProperties;ExternalDataSources;ExternalFileFormats;ExternalTables;Filegroups;FileTables;FullTextCatalogs;FullTextStoplists;MessageTypes;PartitionFunctions;PartitionSchemes;Permissions;Queues;RemoteServiceBindings;RoleMembership;Rules;ScalarValuedFunctions;SearchPropertyLists;SecurityPolicies;Sequences;Services;Signatures;StoredProcedures;SymmetricKeys;Synonyms;TableValuedFunctions;UserDefinedDataTypes;UserDefinedTableTypes;ClrUserDefinedTypes;Users;XmlSchemaCollections;Audits;Credentials;CryptographicProviders;DatabaseAuditSpecifications;DatabaseScopedCredentials;Endpoints;ErrorMessages;EventNotifications;EventSessions;LinkedServerLogins;LinkedServers;Logins;Routes;ServerAuditSpecifications;ServerRoleMembership;ServerRoles;ServerTriggers'
#    os.startfile(filepath)
    
except Exception as ex:
    print('Exception:')
    print(ex)
