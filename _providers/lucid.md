---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 120
  human_in_the_loop: 1
  name: Lucid Agentic Access
  operation_count: 220
  slug: lucid-agentic-access
  summary_line: 220 operations · 120 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: 'Lucid''s remote Model Context Protocol server. Connects AI clients (ChatGPT, Claude, Microsoft Copilot, Cursor) to Lucid documents so they can be searched, retrieved, edited, summarized and created in '
  name: Lucid MCP Server
  slug: lucid-mcp-server
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve information about the authenticated Lucid account.
  name: Lucid Accounts API
  phrasing_intents:
  - id: getAccountInformation
    intent: Get my account's details
    question: What basic information does Lucid hold about my account?
  - id: getClassifications
    intent: List my account's document classifications
    question: What data classifications are configured on my account?
  phrasing_ops: 2
  slug: lucid-accounts-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve audit log events that record user and admin activity across the Lucid account.
  name: Lucid Audit Logs API
  phrasing_intents:
  - id: getAuditLogs
    intent: Page through account audit log events
    question: What audit events have happened on our Lucid account within a date range?
  - id: queryAuditLogs
    intent: Search audit logs by user or event type
    question: Which actions did a specific user take according to the audit logs?
  phrasing_ops: 2
  slug: lucid-audit-logs-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Manage cloud infrastructure credentials, data sources, and architecture diagrams for AWS, Azure, and Google Cloud.
  name: Lucid Cloud API
  phrasing_intents:
  - id: getAwsExternalId
    intent: Get the AWS external ID for a trust relationship
    question: What external ID do I put in my AWS IAM role trust policy so Lucid Cloud can assume it?
  - id: createAwsCredential
    intent: Add an AWS credential to Lucid Cloud
    question: How do I connect my AWS account to Lucid Cloud using an IAM role ARN?
  - id: updateAwsCredential
    intent: Update an existing AWS credential
    question: Can I change the role ARN on an AWS credential I already saved in Lucid Cloud?
  - id: createAzureCredential
    intent: Add an Azure credential to Lucid Cloud
    question: How do I connect an Azure tenant to Lucid Cloud with a service principal client ID and secret?
  - id: updateAzureCredential
    intent: Update an existing Azure credential
    question: Can I rotate the client secret on an Azure credential already saved in Lucid Cloud?
  - id: createGoogleCloudCredential
    intent: Add a Google Cloud credential to Lucid Cloud
    question: How do I connect Google Cloud to Lucid using a service account key file?
  - id: updateGoogleCloudCredential
    intent: Update an existing Google Cloud credential
    question: Can I upload a new service account key for a Google Cloud credential I already created?
  - id: listCredentials
    intent: List all cloud credentials on the account
    question: Which cloud credentials are saved on my Lucid account?
  phrasing_ops: 50
  slug: lucid-cloud-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, and delete collections within a data source. A collection is a named group of data items that share a common schema (similar to a database table).
  name: Lucid Collection API
  phrasing_intents:
  - id: getTotalCollectionsCount
    intent: Count the collections I can access
    question: How many data collections do I have access to?
  - id: getAllCollections
    intent: List all data collections I can access
    question: Which data collections do I have access to in Lucid?
  - id: createCollection
    intent: Create a data collection in a data source
    question: How do I add a new collection with a schema to an existing data source?
  - id: getCollection
    intent: Get one data collection
    question: What does a specific collection look like in Lucid?
  - id: updateCollection
    intent: Rename a collection or move its data source
    question: Can I rename a collection after it's been created?
  - id: deleteCollection
    intent: Delete a collection and its items
    question: Does deleting a collection also remove its schema, items and metadata collections?
  - id: getAllMetadataCollections
    intent: List metadata collections of a collection
    question: Which metadata collections are attached to a given collection?
  - id: createMetadataCollection
    intent: Add a metadata collection to a collection
    question: How do I attach a metadata collection to an existing collection?
  phrasing_ops: 8
  slug: lucid-collection-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Read and update metadata properties on a collection, such as display name and configuration.
  name: Lucid Collection Properties API
  phrasing_intents:
  - id: getCollectionProperties
    intent: Get a collection's properties
    question: What properties are set on a data collection?
  - id: updateCollectionProperties
    intent: Add or update a collection's properties
    question: How do I set new properties on a collection?
  - id: deleteCollectionProperties
    intent: Delete properties from a collection
    question: Can I remove specific properties from a collection?
  phrasing_ops: 3
  slug: lucid-collection-properties-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: The CreateDiagram API from Lucid — 1 operation(s) for creatediagram.
  name: Lucid Create Diagram API
  phrasing_intents:
  - id: createDiagram
    intent: Create a diagram from Mermaid code
    question: Can Lucid turn Mermaid code into a diagram image?
  phrasing_ops: 1
  slug: lucid-creatediagram-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, and delete individual data items within a collection. A data item is a single record conforming to the collection's schema.
  name: Lucid Data Item API
  phrasing_intents:
  - id: getTotalDataItemsCount
    intent: Count the data items in a collection
    question: How many items does a data collection contain?
  - id: getAllDataItems
    intent: List the data items in a collection
    question: What rows are stored in my Lucid data collection?
  - id: createDataItems
    intent: Add new data items to a collection
    question: How do I insert new rows into a data collection?
  - id: updateDataItems
    intent: Update many data items in a collection at once
    question: How can I edit the field values of many collection items in one request?
  - id: deleteDataItems
    intent: Delete several data items from a collection
    question: Can I remove a batch of specific items from a collection in one call?
  - id: getDataItem
    intent: Retrieve a single data item
    question: What values does one particular item in a collection hold?
  - id: getDataItemsByKey
    intent: Find data items by their key field values
    question: How do I look up collection items whose key fields equal certain values?
  - id: updateDataItem
    intent: Update one data item's values
    question: How do I change the values of one specific item in a collection?
  phrasing_ops: 11
  slug: lucid-data-item-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Manage access grants on data sets to control which users or applications can read or write data.
  name: Lucid Data Set Grant API
  phrasing_intents:
  - id: getDataSetGrant
    intent: Get one data set grant
    question: What access does a particular data set grant give?
  - id: deleteDataSetGrant
    intent: Revoke a data set grant
    question: Can I revoke someone's grant to a data set?
  - id: getAllDataSetGrants
    intent: List all grants on a data set
    question: Who has been granted access to a given data set?
  - id: createDataSetGrant
    intent: Grant access to a data set
    question: How do I share a data set with another user or team?
  phrasing_ops: 4
  slug: lucid-data-set-grant-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Read and update metadata properties on a data set, such as display name and configuration.
  name: Lucid Data Set Properties API
  phrasing_intents:
  - id: getDataSetProperties
    intent: Get a data set's properties
    question: What properties are configured on a data set?
  - id: updateDataSetProperties
    intent: Add or update a data set's properties
    question: How do I set new properties on a data set?
  - id: deleteDataSetProperties
    intent: Delete properties from a data set
    question: Can I remove selected properties from a data set?
  phrasing_ops: 3
  slug: lucid-data-set-properties-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, and delete data sources within a data set. A data source represents an external system whose data is synced into Lucid.
  name: Lucid Data Source API
  phrasing_intents:
  - id: getDataSourceCount
    intent: Count my data sources
    question: How many data sources can I access?
  - id: getAllDataSources
    intent: List my data sources
    question: Which data sources do I have access to in Lucid?
  - id: createDataSource
    intent: Create a data source
    question: How do I create a new data source to link data into diagrams?
  - id: getDataSource
    intent: Get a data source
    question: What details does a single data source have?
  - id: updateDataSource
    intent: Rename a data source or change its adapter
    question: How do I rename a data source?
  - id: deleteDataSource
    intent: Delete a data source and everything in it
    question: Does deleting a data source also remove its collections and items?
  - id: createDataSourceFromCSV
    intent: Create a data source from a CSV file
    question: Can I upload a CSV to make a brand-new data source?
  - id: updateDataSourceFromCSV
    intent: Replace a data source's data from a CSV
    question: How do I refresh an existing data source with a new CSV file?
  phrasing_ops: 8
  slug: lucid-data-source-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, import, copy, retrieve, update, search, export, and trash documents across the Lucid Suite, and access their contents.
  name: Lucid Document Access API
  phrasing_intents:
  - id: SearchAccountDocuments
    intent: Search all documents across the account as admin
    question: How can an admin find every document on our Enterprise Shield account?
  - id: createDocument
    intent: Create a new Lucidchart or Lucidspark document
    question: How do I create a blank Lucidchart diagram from code?
  - id: createDocumentWithStandardImport
    intent: Create a document from a Standard Import zip
    question: Can I upload a Lucid Standard Import .zip file to make a new document?
  - id: importDocument
    intent: Import an external file as a document
    question: How do I import a draw.io file into Lucidchart?
  - id: copyDocument
    intent: Copy an existing document
    question: Can I duplicate one of my documents under a new name?
  - id: getOrExportDocument
    intent: Get document details or export it as an image
    question: How do I export a Lucid document page as a PNG?
  - id: updateDocument
    intent: Rename, move or reclassify a document
    question: How do I rename a document or move it to another folder?
  - id: trashDocument
    intent: Move a document to the trash
    question: Can I trash a document I own?
  phrasing_ops: 10
  slug: lucid-document-access-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve comment threads on a document, list comments within a thread, and post new comments to an existing thread.
  name: Lucid Document Comments API
  phrasing_intents:
  - id: listDocumentThreads
    intent: List comment threads on a document
    question: Which comment threads are open or closed on a Lucid document?
  - id: listDocumentThreadComments
    intent: Read the comments in a thread
    question: What comments have people left in a specific thread?
  - id: postDocumentThreadComment
    intent: Reply to a comment thread
    question: How do I add a reply to an existing comment thread on a document?
  phrasing_ops: 3
  slug: lucid-document-comments-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Generate session tokens and render the embedded viewer iframe used to display Lucid documents in external applications.
  name: Lucid Document Embedding API
  phrasing_intents:
  - id: documentEmbeds
    intent: Load an embedded document viewer in an iframe
    question: How do I show a Lucid document picker or viewer inside an iframe?
  - id: documentEmbedsToken
    intent: Generate a short-lived embed session token
    question: Can I get a temporary token so my site can display embedded documents?
  phrasing_ops: 2
  slug: lucid-document-embedding-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Generate tokens and render an embedded document picker that lets users select Lucid documents from within your application.
  name: Lucid Document Picker API
  phrasing_intents:
  - id: generateDocumentPickerToken
    intent: Generate a token for the embedded document picker
    question: How do I get a token to embed the Lucid document picker in my app?
  - id: embeddedDocumentPicker
    intent: Show the embedded document picker
    question: What does the embedded document picker iframe let users do?
  phrasing_ops: 2
  slug: lucid-document-picker-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Manage user and team collaborator access on individual documents, including granting, updating, and revoking collaboration roles.
  name: Lucid Documents Collaboration API
  phrasing_intents:
  - id: getDocumentUserCollaborators
    intent: Check one user's access to a document
    question: What role does a specific person have on a Lucid document?
  - id: putDocumentUserCollaborators
    intent: Share a document with a user or change their role
    question: How do I share a document with one person?
  - id: deleteDocumentUserCollaborators
    intent: Remove a user's access to a document
    question: Can I unshare a document from a particular user?
  - id: listDocumentUserCollaborators
    intent: List the people a document is shared with
    question: Who are all the collaborators on a document?
  - id: getDocumentTeamCollaborator
    intent: Check a team's access to a document
    question: What access does a team have on a given document?
  - id: putDocumentTeamCollaborator
    intent: Share a document with a team or change its role
    question: How do I add a team as a collaborator on a document?
  - id: deleteDocumentTeamCollaborator
    intent: Remove a team from a document
    question: Can I take a team off a document's collaborators?
  phrasing_ops: 7
  slug: lucid-documents-collaboration-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, and delete share links for documents to control external access.
  name: Lucid Documents Sharing API
  phrasing_intents:
  - id: getDocumentShareLink
    intent: Get a document share link
    question: What settings does an existing share link on a document have?
  - id: updateDocumentShareLink
    intent: Change a document share link's settings
    question: Can I change the role granted by an existing share link?
  - id: deleteDocumentShareLink
    intent: Delete a document share link
    question: How do I disable a share link on a document?
  - id: createDocumentShareLink
    intent: Create a share link for a document
    question: How do I generate a share link for a Lucid document?
  phrasing_ops: 4
  slug: lucid-documents-sharing-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, delete, and change the version of embed instances on a document.
  name: Lucid Embedding Utils API
  phrasing_intents:
  - id: getEmbedInformation
    intent: Get a document embed's details
    question: What metadata can I get about an existing document embed?
  - id: deleteEmbed
    intent: Delete a document embed
    question: Can I remove an embed so it stops loading in the viewer?
  - id: getEmbedDocument
    intent: Get the document behind an embed
    question: Which document is shown by a given embed?
  - id: createEmbed
    intent: Create an embed for a document
    question: How do I create an embed so a document can be shown in my app?
  - id: changeEmbedVersion
    intent: Switch an embed's version type
    question: Can I freeze an existing embed to a snapshot of the document?
  phrasing_ops: 5
  slug: lucid-embedding-utils-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, search, trash, and restore folders. Includes listing folder contents and root folder navigation.
  name: Lucid Folders API
  phrasing_intents:
  - id: getFolder
    intent: Get a folder's details
    question: What information can I get about a single Lucid folder?
  - id: updateFolder
    intent: Rename or move a folder
    question: How do I rename a folder?
  - id: createFolder
    intent: Create a new folder
    question: Can I create a folder or team folder from code?
  - id: trashFolder
    intent: Move a folder and its contents to the trash
    question: Does trashing a folder also trash everything in it?
  - id: restoreFolder
    intent: Restore a trashed folder
    question: Can I bring back a folder I trashed?
  - id: searchFolders
    intent: Search folders I can access
    question: How do I find folders by keyword?
  - id: listFolderContents
    intent: List what is inside a folder
    question: What documents and subfolders are inside a given folder?
  - id: listRootFolderContents
    intent: List the contents of my root folder
    question: What's at the top level of my Lucid documents?
  phrasing_ops: 9
  slug: lucid-folders-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Manage user, group, and team collaborator access on folders, including granting, updating, and revoking collaboration roles.
  name: Lucid Folders Collaboration API
  phrasing_intents:
  - id: getFolderUserCollaborators
    intent: Check one user's direct access to a folder
    question: What role does a specific person have directly on a Lucid folder?
  - id: putFolderUserCollaborator
    intent: Share a folder with a user or change their role
    question: How do I give a person access to a folder?
  - id: deleteFolderUserCollaborator
    intent: Remove a user's direct access to a folder
    question: Can I unshare a folder from one person?
  - id: listFolderUserCollaborators
    intent: List users with direct access to a folder
    question: Who has been shared directly on a folder?
  - id: getFolderGroupCollaborator
    intent: Check a group's direct access to a folder
    question: What role does a particular group have on a folder?
  - id: updateFolderGroupCollaborator
    intent: Share a folder with a group or change its role
    question: How do I grant a whole group access to a folder?
  - id: deleteFolderGroupCollaborator
    intent: Remove a group's direct access to a folder
    question: Can I take a group off a folder's sharing list?
  - id: listFolderGroupCollaborators
    intent: List groups with direct access to a folder
    question: Which groups are shared directly on a folder?
  phrasing_ops: 11
  slug: lucid-folders-collaboration-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, and delete share links for folders to control external access.
  name: Lucid Folders Sharing API
  phrasing_intents:
  - id: getFolderShareLink
    intent: Get a folder share link's settings
    question: What role and security settings does a folder share link have?
  - id: updateFolderShareLink
    intent: Change a folder share link's settings
    question: Can I change the role granted by an existing folder share link?
  - id: deleteFolderShareLink
    intent: Delete a folder share link
    question: How do I stop a folder share link from working?
  - id: createFolderShareLink
    intent: Create a share link for a folder
    question: How do I generate a shareable link to a Lucid folder?
  phrasing_ops: 4
  slug: lucid-folders-sharing-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Endpoints that deal with org groups or teams (dependent on which bearer token is used).
  name: Lucid Groups API
  phrasing_intents:
  - id: getGroup
    intent: Get a group or team via SCIM
    question: How do I read one org group or team through SCIM?
  - id: modifyGroupPut
    intent: Replace a group or team via SCIM
    question: Can I overwrite a group's name and member list with a SCIM PUT?
  - id: modifyGroupPatch
    intent: Patch a group or team via SCIM
    question: How do I add or remove a single member of a group with a SCIM PATCH?
  - id: deleteGroup
    intent: Delete a group or archive a team via SCIM
    question: What happens to a team when I delete it through SCIM?
  - id: getAllGroups
    intent: List groups and teams via SCIM
    question: Which org groups and teams exist on the account according to SCIM?
  - id: createGroup
    intent: Create a group or team via SCIM
    question: How do I provision a new org group from my identity provider?
  phrasing_ops: 6
  slug: lucid-groups-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create and manage legal holds on a Lucid account. Legal holds prevent documents from being permanently deleted for users placed on hold.
  name: Lucid Legal Holds API
  phrasing_intents:
  - id: createLegalHold
    intent: Create a legal hold
    question: How do I put a legal hold in place on an Enterprise Shield account?
  - id: getLegalHolds
    intent: List the account's legal holds
    question: Which legal holds are configured on our Lucid account?
  - id: addLegalHoldUsers
    intent: Add users to a legal hold
    question: Can I add custodians to a legal hold that hasn't started yet?
  - id: removeLegalHoldUsers
    intent: Remove users from a legal hold
    question: Can I take a user off a legal hold before it begins?
  - id: editLegalHold
    intent: Edit a legal hold's details or dates
    question: Can I extend the end time of an existing legal hold?
  - id: releaseLegalHold
    intent: Release a legal hold
    question: How do I lift a legal hold once the matter is closed?
  - id: getLegalHoldUsers
    intent: List users on a legal hold
    question: Which users are custodians under a given legal hold?
  - id: getLegalHoldDocuments
    intent: List documents preserved by a legal hold
    question: Which documents are being preserved under a legal hold?
  phrasing_ops: 8
  slug: lucid-legal-holds-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: View and manage product licenses assigned to users within a subscription.
  name: Lucid Licenses API
  phrasing_intents:
  - id: listSubscriptionLicenses
    intent: List licenses on a subscription
    question: Which licenses belong to one of our Lucid subscriptions?
  - id: listUserLicenses
    intent: List a user's licenses
    question: What licenses has a specific user been granted?
  - id: grantUserLicense
    intent: Grant a user a license from a subscription
    question: How do I give a user a license from a subscription?
  phrasing_ops: 3
  slug: lucid-licenses-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, refresh, introspect, and revoke OAuth 2.0 access tokens used to authenticate API requests on behalf of a user.
  name: Lucid OAuth 2.0 Tokens API
  phrasing_intents:
  - id: createOrRefreshAccessToken
    intent: Get or refresh an OAuth access token
    question: How do I exchange an authorization code for a Lucid access token?
  - id: introspectAccessToken
    intent: Check whether an OAuth token is active
    question: Is a given OAuth token still active, and what scopes does it carry?
  - id: revokeAccessToken
    intent: Revoke an OAuth token and its grant
    question: How do I revoke a user's OAuth token when they disconnect my app?
  phrasing_ops: 3
  slug: lucid-oauth-2-0-tokens-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve current rate limit thresholds and quotas for the authenticated user.
  name: Lucid Rate Limits API
  phrasing_intents:
  - id: getRateLimits
    intent: Check my current API rate limits
    question: What are my current Lucid API rate limits?
  phrasing_ops: 1
  slug: lucid-rate-limits-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create and manage shared document repositories. Control repository membership by adding and removing users and groups.
  name: Lucid Repositories API
  phrasing_intents:
  - id: listRepositories
    intent: List repositories I can view
    question: Which Lucid repositories do I have permission to view?
  - id: createRepository
    intent: Create a new repository
    question: How do I create a new repository and assign its initial users?
  - id: getRepository
    intent: Get details of one repository
    question: What basic information can I see about a single repository?
  - id: listRepositoryUsers
    intent: List users with roles on a repository
    question: Who are the individual user collaborators on a repository and what roles do they hold?
  - id: addRepositoryUsers
    intent: Add users or change their repository roles
    question: How do I add people to a repository or change the role an existing user has?
  - id: removeRepositoryUsers
    intent: Remove users from a repository
    question: Can I take individual users off a repository?
  - id: listRepositoryGroups
    intent: List groups with access to a repository
    question: Which groups have member access to a repository?
  - id: addRepositoryGroups
    intent: Give groups member access to a repository
    question: How do I give a whole group member access to a repository?
  phrasing_ops: 9
  slug: lucid-repositories-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Define and retrieve the schema for a collection, specifying the fields, types, and constraints for its data items.
  name: Lucid Schema API
  phrasing_intents:
  - id: getFieldDefinition
    intent: Get one field definition in a collection schema
    question: What type and settings does a single field in a collection's schema have?
  - id: updateFieldDefinition
    intent: Update one field definition
    question: Can I change the type or label of a single schema field?
  - id: deleteFieldDefinition
    intent: Delete one field from a collection schema
    question: What happens to item values when I delete a single field from a schema?
  - id: getAllFieldDefinitions
    intent: Get a collection's full schema
    question: What fields make up a collection's schema?
  - id: updateFieldDefinitions
    intent: Update many field definitions at once
    question: Can I update several schema fields in a single request?
  - id: deleteFieldDefinitions
    intent: Delete several fields from a schema
    question: Can I remove multiple fields from a collection schema in one request?
  phrasing_ops: 6
  slug: lucid-schema-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Endpoints that deal with lucid resource schemas.
  name: Lucid Schemas API
  phrasing_intents:
  - id: getSchema
    intent: Get one SCIM resource schema
    question: What attributes does a particular SCIM resource schema define?
  - id: getAllSchemas
    intent: List all SCIM resource schemas
    question: Which SCIM resource schemas does Lucid support?
  phrasing_ops: 2
  slug: lucid-schemas-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve the SCIM service provider configuration, describing supported operations, authentication schemes, and bulk/filter capabilities.
  name: Lucid Service Provider Config API
  phrasing_intents:
  - id: getServiceProviderConfig
    intent: Get Lucid's SCIM service provider config
    question: Which SCIM features, such as patch, filter or bulk, does Lucid support?
  phrasing_ops: 1
  slug: lucid-service-provider-config-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: The Sharing API from Lucid — 1 operation(s) for sharing.
  name: Lucid Sharing API
  phrasing_intents:
  - id: acceptShareLink
    intent: Accept a share link for a document or folder
    question: How do I accept a Lucid share link on behalf of a user?
  phrasing_ops: 1
  slug: lucid-sharing-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: List and retrieve product subscriptions on the account.
  name: Lucid Subscriptions API
  phrasing_intents:
  - id: listSubscriptions
    intent: List subscriptions on the account
    question: Which Lucid subscriptions does my account have?
  - id: getSubscription
    intent: Get details of one subscription
    question: What are the details of a specific subscription on our account?
  phrasing_ops: 2
  slug: lucid-subscriptions-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Create, retrieve, update, archive, and restore teams. Manage team membership by adding and removing users.
  name: Lucid Teams API
  phrasing_intents:
  - id: listTeams
    intent: List teams I can access
    question: Which Lucid teams do I have access to?
  - id: createTeam
    intent: Create a team with members
    question: How do I create a new team with a set of members?
  - id: getTeam
    intent: Get a team's details
    question: What are the details of a specific team?
  - id: updateTeam
    intent: Rename a team
    question: How do I rename an existing team?
  - id: listUsersOnTeam
    intent: List members of a team
    question: Who is on a given team?
  - id: addUsersToTeam
    intent: Add users to a team
    question: How do I add people to a team with a role?
  - id: removeUsersFromTeam
    intent: Remove users from a team
    question: Can I take members off a team?
  - id: archiveTeam
    intent: Archive a team
    question: How do I make a team inactive?
  phrasing_ops: 9
  slug: lucid-teams-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Transfer ownership of a user's documents, folders, custom shape libraries, and Lucidscale objects to another user within the same account.
  name: Lucid Transfer Content API
  phrasing_intents:
  - id: transferUserContent
    intent: Transfer a user's content to another user
    question: How do I hand over a departing employee's documents and folders to someone else?
  phrasing_ops: 1
  slug: lucid-transfer-content-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve metadata for Lucid document links to power rich previews, and serve direct iframe embeds for Lucid documents in external applications.
  name: Lucid Unfurling API
  phrasing_intents:
  - id: describeLink
    intent: Get preview metadata for a Lucid document link
    question: How do I unfurl a Lucid document URL into a rich link preview?
  - id: directEmbed
    intent: Embed a document directly by its ID
    question: Can I show a document in an iframe using just its ID and my client ID?
  phrasing_ops: 2
  slug: lucid-unfurling-api
- baseURL: https://api.lucid.co
  baseurl_source: declared
  description: Retrieve, create, and search for users within the authenticated account. Includes user profile access.
  name: Lucid Users API
  phrasing_intents:
  - id: getUser
    intent: Get a user on my account
    question: What details can I see about a specific user on my Lucid account?
  - id: listUsers
    intent: List all users on my account
    question: Who are all the users on my Lucid account?
  - id: createUser
    intent: Add a new user to my account
    question: How do I add a new person to our Enterprise account with their name and email?
  - id: userEmailSearch
    intent: Find users by email address
    question: Which users on my account match these email addresses?
  - id: getUserProfile
    intent: Get my own user profile
    question: Who am I signed in as in Lucid?
  - id: getUsersById
    intent: Get a user via SCIM provisioning
    question: How do I fetch a single user record through SCIM?
  - id: modifyUserPut
    intent: Replace a user's attributes via SCIM
    question: How do I deactivate a user through SCIM by replacing their record?
  - id: modifyUserPatch
    intent: Patch a user's attributes via SCIM
    question: Can I change just a few attributes of a user with a SCIM PATCH?
  phrasing_ops: 11
  slug: lucid-users-api
- baseURL: https://mcp.lucid.app/mcp
  baseurl_source: declared
  description: Create, retrieve, update, and delete data sets. A data set is a top-level container that groups related data sources and their collections.
  name: Lucid Dataset API
  phrasing_intents:
  - id: getDataSetCount
    intent: Count the data sets I can access
    question: How many data sets do I have access to?
  - id: getAllDataSets
    intent: List all data sets I can access
    question: Which data sets do I have access to in Lucid?
  - id: createDataSet
    intent: Create a data set
    question: How do I create a new data set to group data sources?
  - id: getDataSet
    intent: Get one data set
    question: What does a specific data set contain?
  - id: updateDataSetName
    intent: Rename a data set
    question: Can I rename an existing data set?
  - id: deleteDataSet
    intent: Delete a data set
    question: Does deleting a data set also delete the data sources inside it?
  phrasing_ops: 6
  slug: lucid-dataset-api
artifact_total: 58
collections:
- collection_type: open
  name: Lucid Data API
  slug: open-lucid-data-api
- collection_type: open
  name: Lucid REST API
  slug: open-lucid-rest-api
- collection_type: open
  name: Lucid SCIM API
  slug: open-lucid-scim-api
common:
- group: commercial
  href: https://artifacts.apis.io/lucid/plans/lucid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lucid-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://lucid.co/solutions/engineering
- group: company
  title: ''
  type: BlogRSS
  url: https://lucid.co/legal-rss.xml
- group: other
  href: https://artifacts.apis.io/lucid/capabilities/lucid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lucid-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lucid/overlays/lucid-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucid-rest-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/lucid/overlays/lucid-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucid-data-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/lucid/overlays/lucid-scim-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucid-scim-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lucid/agentic-access/lucid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lucid-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lucid/security/lucid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lucid-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lucid/security/lucid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lucid-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lucid/scopes/lucid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lucid-scopes.yml
- group: auth
  href: https://artifacts.apis.io/lucid/authentication/lucid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lucid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lucid.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lucid.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lucid.co/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lucid.co/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lucid.co/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://community.lucid.co/lucid-for-developers-6
- group: company
  title: ''
  type: Blog
  url: https://lucid.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidsoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://lucid.app/pricing/lucidchart
- group: start
  title: ''
  type: SignUp
  url: https://lucid.app/users/login?activate=lucidchart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lucid.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucid.co/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://lucid.co/security
- group: auth
  title: ''
  type: Security
  url: https://lucid.co/security
- group: auth
  href: https://artifacts.apis.io/lucid/security/lucid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lucid-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucid.co/
- group: design
  href: https://artifacts.apis.io/lucid/lifecycle/lucid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lucid-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/lucid/changelog/lucid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lucid-changelog.yml
- group: agent
  href: https://artifacts.apis.io/lucid/well-known/lucid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lucid-well-known.yml
- group: design
  href: https://artifacts.apis.io/lucid/conventions/lucid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lucid-conventions.yml
- group: design
  href: https://artifacts.apis.io/lucid/conformance/lucid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lucid-conformance.yml
- group: design
  href: https://artifacts.apis.io/lucid/errors/lucid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lucid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lucid/data-model/lucid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lucid-data-model.yml
- group: operate
  href: https://artifacts.apis.io/lucid/rate-limits/lucid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lucid-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/lucid/packages/lucid-packages.yml
  title: ''
  type: Packages
  url: packages/lucid-packages.yml
- group: build
  href: https://artifacts.apis.io/lucid/packages/lucid-packages.yml
  title: ''
  type: SDKs
  url: packages/lucid-packages.yml
- group: build
  href: https://artifacts.apis.io/lucid/cli/lucid-cli.yml
  title: ''
  type: CLI
  url: cli/lucid-cli.yml
- group: design
  href: https://artifacts.apis.io/lucid/components/lucid-components.yml
  title: ''
  type: Components
  url: components/lucid-components.yml
- group: agent
  href: https://artifacts.apis.io/lucid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lucid/llms/lucid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lucid-llms.txt
- group: agent
  href: https://artifacts.apis.io/lucid/mcp/lucid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lucid-mcp.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/lucid_stock/
created: '2026-08-01'
description: 'Lucid Software Inc. is the visual collaboration company behind the Lucid Suite — Lucidchart (intelligent diagramming), Lucidspark (virtual whiteboarding) and Lucidscale (cloud visualization) — plus the Lucid Cloud, Process and Enterprise Shield accelerators and airfocus. The Lucid Developer Platform at developer.lucid.co publishes three OpenAPI-described surfaces: the Lucid REST API on api.lucid.co for documents, folders, sharing, embeds, comments, teams, repositories, legal holds, licenses and audit logs; the Lucid Data API on data.lucid.app for the structured data sets, collections, schemas and data items that back data-linked diagrams; and a SCIM 2.0 API on users.lucid.app for enterprise user and group provisioning. Lucid also ships an in-editor Extension API (lucid-extension-sdk plus the lucid-package CLI), an Embed SDK, and an OAuth-gated remote MCP server at mcp.lucid.app that lets AI clients search, read, edit and create Lucid documents. Lucid is privately held and trades
  on secondary markets.'
finops:
- has_sources: true
  method: derived
  name: Lucid Finops
  primary_unit: month when billed annually
  service_category: ''
  slug: lucid-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidchart.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lucid.app.
  name: Lucid MCP Server
  slug: lucid-mcp-yml
modified: '2026-10-06'
name: Lucid
nav: Providers
network: true
overview: 'Lucid publishes 37 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Audit Logs API, Cloud API, and 34 more. Tagged areas include Visual Collaboration, Diagramming, Whiteboarding, Productivity, and Software-as-a-Service.


  The Lucid catalog on APIs.io includes 1 Spectral governance ruleset.


  Lucid''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, pricing, and 37 more developer resources.'
plans:
- name: Lucid Plans Pricing
  plan_count: 4
  slug: lucid-plans-pricing
- name: Lucid Price Estimates
  plan_count: 0
  slug: lucid-price-estimates
random_paper: 1
rate_limits:
- limit_count: 5
  name: Lucid Rate Limits
  slug: lucid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Lucid API Rules
  rule_count: 68
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 25
  slug: lucid-rules
scopes:
- name: Lucid Scopes
  scope_count: 143
  slug: lucid-scopes
  summary_line: 143 scopes · authorizationCode
score:
  band: exemplar
  composite: 79.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 63.6
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 76.3
  previous_composite: 78.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 94.4
      total: 36
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/lucid/lucid-2026-08-07T171817.png
security:
- kind: authentication
  name: Lucid Authentication
  slug: lucid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lucid Domain Security
  slug: lucid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lucid Vulnerability Disclosure
  slug: lucid-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Lucid Trust Center
  slug: lucid-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001 (AI management systems), CSA STAR, PCI DSS, FedRAMP Moderate, TX-RAMP, IRAP (Australia), GDPR, CCPA
skill_count: 6
skills:
- name: Create and share a Lucid document
  slug: lucid-create-and-share-a-document
- name: Run the Lucid OAuth 2.0 token lifecycle
  slug: lucid-oauth-token-lifecycle
- name: Provision Lucid users and groups with SCIM 2.0
  slug: lucid-provision-users-with-scim
- name: Pull Lucid audit logs
  slug: lucid-pull-audit-logs
- name: Search and export Lucid documents
  slug: lucid-search-and-export-documents
- name: Sync external data into Lucid diagrams
  slug: lucid-sync-external-data-into-diagrams
slug: lucid
tags:
- Visual Collaboration
- Diagramming
- Whiteboarding
- Productivity
- Software-as-a-Service
- Cloud Visualization
- SCIM
- Identity
- Data
- MCP
website: https://lucid.co/
---
