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
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 172
  human_in_the_loop: 3
  name: The Things Network Agentic Access
  operation_count: 329
  slug: the-things-network-agentic-access
  summary_line: 329 operations · 172 acting · 3 human-in-the-loop
api_count: 9
apis:
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The AppAs API from The Things Network / The Things Stack — 8 operation(s) for appas.
  name: The Things Network / The Things Stack AppAs API
  phrasing_intents:
  - id: AppAs_DownlinkQueueList
    intent: List a device's queued downlinks
    question: What downlink messages are currently waiting to be sent to my device?
  - id: AppAs_GetMQTTConnectionInfo
    intent: Get MQTT connection info for an application
    question: How do I connect an MQTT client to my application's data?
  - id: AppAs_DecodeDownlink
    intent: Decode a downlink payload with a formatter
    question: Can I test how a payload formatter decodes a downlink for my device?
  - id: AppAs_EncodeDownlink
    intent: Encode a downlink payload with a formatter
    question: How can I check what bytes my payload formatter produces for a downlink?
  - id: AppAs_DownlinkQueuePush
    intent: Queue downlinks to a device
    question: How do I send a downlink message to my end device?
  - id: AppAs_DownlinkQueueReplace
    intent: Replace or clear a device's downlink queue
    question: How do I clear all pending downlinks for a device?
  - id: AppAs_DecodeUplink
    intent: Decode an uplink payload with a formatter
    question: Can I test my uplink payload formatter against sample bytes?
  - id: AppAs_SimulateUplink
    intent: Simulate an uplink to test integrations
    question: How do I test my webhook or integration without a real device sending data?
  phrasing_ops: 8
  slug: the-things-network-appas-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationAccess API from The Things Network / The Things Stack — 9 operation(s) for applicationaccess.
  name: The Things Network / The Things Stack ApplicationAccess API
  phrasing_intents:
  - id: ApplicationAccess_ListAPIKeys
    intent: List an application's API keys
    question: Which API keys exist for my Things Stack application?
  - id: ApplicationAccess_CreateAPIKey
    intent: Create an application API key
    question: How do I create an API key that only has access to one application?
  - id: ApplicationAccess_UpdateAPIKey
    intent: Change the rights of an application API key
    question: Can I change what an existing application API key is allowed to do?
  - id: ApplicationAccess_GetAPIKey
    intent: Get one application API key
    question: What rights and expiry does a specific application API key have?
  - id: ApplicationAccess_DeleteAPIKey
    intent: Delete an application API key
    question: How do I revoke an API key that was issued for my application?
  - id: ApplicationAccess_GetCollaborator2
    intent: Get an organization collaborator's rights on an app
    question: What rights does a member organization have on my application?
  - id: ApplicationAccess_DeleteCollaborator2
    intent: Remove an organization from an application
    question: How do I take away an organization's collaborator access to my application?
  - id: ApplicationAccess_GetCollaborator
    intent: Get a user collaborator's rights on an app
    question: What can a particular user do on my application?
  phrasing_ops: 12
  slug: the-things-network-applicationaccess-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationActivationSettingRegistry API from The Things Network / The Things Stack — 1 operation(s) for applicationactivationsettingregistry.
  name: The Things Network / The Things Stack ApplicationActivationSettingRegistry API
  phrasing_intents:
  - id: ApplicationActivationSettingRegistry_Get
    intent: Get an application's activation settings
    question: What activation settings does the Join Server hold for my application?
  - id: ApplicationActivationSettingRegistry_Delete
    intent: Delete an application's activation settings
    question: Can I clear the activation settings stored for an application?
  - id: ApplicationActivationSettingRegistry_Set
    intent: Create or update application activation settings
    question: How do I configure the Join Server activation settings for my application?
  phrasing_ops: 3
  slug: the-things-network-applicationactivationsettingregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationPackageRegistry API from The Things Network / The Things Stack — 9 operation(s) for applicationpackageregistry.
  name: The Things Network / The Things Stack ApplicationPackageRegistry API
  phrasing_intents:
  - id: ApplicationPackageRegistry_List
    intent: List application packages available for a device
    question: Which application packages can I use with a given end device?
  - id: ApplicationPackageRegistry_DeleteDefaultAssociation
    intent: Remove an application-wide package default on an FPort
    question: How do I remove the default package association for an FPort across my whole application?
  - id: ApplicationPackageRegistry_SetAssociation
    intent: Associate a package with a device FPort
    question: How do I attach an application package to a specific FPort on one end device?
  - id: ApplicationPackageRegistry_SetDefaultAssociation
    intent: Set an application-wide package default on an FPort
    question: How do I make a package the default on an FPort for every device in my application?
  - id: ApplicationPackageRegistry_DeleteAssociation
    intent: Remove a device's package association on an FPort
    question: How do I remove the package association from one end device's FPort?
  - id: ApplicationPackageRegistry_ListAssociations
    intent: List a device's package associations
    question: Which package associations are set on my end device's FPorts?
  - id: ApplicationPackageRegistry_GetDefaultAssociation
    intent: Get an application-wide package default on an FPort
    question: What default package is registered on a given FPort for my application?
  - id: ApplicationPackageRegistry_ListDefaultAssociations
    intent: List an application's default package associations
    question: Which FPorts in my application have a default package association?
  phrasing_ops: 9
  slug: the-things-network-applicationpackageregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationPubSubRegistry API from The Things Network / The Things Stack — 6 operation(s) for applicationpubsubregistry.
  name: The Things Network / The Things Stack ApplicationPubSubRegistry API
  phrasing_intents:
  - id: ApplicationPubSubRegistry_GetFormats
    intent: List supported Pub/Sub message formats
    question: Which message formats can a Pub/Sub integration publish in?
  - id: ApplicationPubSubRegistry_List
    intent: List an application's Pub/Sub integrations
    question: Which Pub/Sub integrations are configured on my application?
  - id: ApplicationPubSubRegistry_Delete
    intent: Delete a Pub/Sub integration
    question: How do I remove a Pub/Sub integration from my application?
  - id: ApplicationPubSubRegistry_Get
    intent: Get a Pub/Sub integration
    question: What broker settings does one of my Pub/Sub integrations use?
  - id: ApplicationPubSubRegistry_Set2
    intent: Create a Pub/Sub integration
    question: How do I set up a new Pub/Sub integration to forward my application's messages to a broker?
  - id: ApplicationPubSubRegistry_Set
    intent: Update a Pub/Sub integration
    question: How do I change the broker or topics of an existing Pub/Sub integration?
  phrasing_ops: 6
  slug: the-things-network-applicationpubsubregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationRegistry API from The Things Network / The Things Stack — 9 operation(s) for applicationregistry.
  name: The Things Network / The Things Stack ApplicationRegistry API
  phrasing_intents:
  - id: ApplicationRegistry_List
    intent: List applications I can access
    question: Which Things Stack applications can I see with my credentials?
  - id: ApplicationRegistry_Update
    intent: Update an application's settings
    question: How do I rename an application or change its description?
  - id: ApplicationRegistry_Get
    intent: Get an application
    question: What are the details of a specific application?
  - id: ApplicationRegistry_Delete
    intent: Delete an application
    question: How do I delete an application, and do I need to remove its devices first?
  - id: ApplicationRegistry_IssueDevEUI
    intent: Issue a DevEUI for a device in an application
    question: Can the network assign a DevEUI from its address block for a new device in my app?
  - id: ApplicationRegistry_Purge
    intent: Permanently purge an application
    question: How do I purge an application so its ID can be reused?
  - id: ApplicationRegistry_Restore
    intent: Restore a deleted application
    question: Can I bring back an application I deleted by mistake?
  - id: ApplicationRegistry_List3
    intent: List an organization's applications
    question: Which applications does my organization collaborate on?
  phrasing_ops: 11
  slug: the-things-network-applicationregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationUpStorage API from The Things Network / The Things Stack — 4 operation(s) for applicationupstorage.
  name: The Things Network / The Things Stack ApplicationUpStorage API
  phrasing_intents:
  - id: ApplicationUpStorage_GetStoredApplicationUp2
    intent: Read stored messages for an application
    question: How do I pull historical uplinks stored for my whole application?
  - id: ApplicationUpStorage_GetStoredApplicationUpCount2
    intent: Count stored messages for an application
    question: How many messages has storage kept for my application?
  - id: ApplicationUpStorage_GetStoredApplicationUp
    intent: Read stored messages for one device
    question: How do I get the stored uplink history for a single end device?
  - id: ApplicationUpStorage_GetStoredApplicationUpCount
    intent: Count stored messages for one device
    question: How many messages have been stored for one of my devices?
  phrasing_ops: 4
  slug: the-things-network-applicationupstorage-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ApplicationWebhookRegistry API from The Things Network / The Things Stack — 8 operation(s) for applicationwebhookregistry.
  name: The Things Network / The Things Stack ApplicationWebhookRegistry API
  phrasing_intents:
  - id: ApplicationWebhookRegistry_GetFormats
    intent: List supported webhook payload formats
    question: Which payload formats can webhooks send, like JSON or protobuf?
  - id: ApplicationWebhookRegistry_ListTemplates
    intent: List webhook integration templates
    question: What ready-made webhook templates are available for integrations?
  - id: ApplicationWebhookRegistry_GetTemplate
    intent: Get a webhook template
    question: What fields and endpoints does a specific webhook template need?
  - id: ApplicationWebhookRegistry_List
    intent: List an application's webhooks
    question: Which webhooks are configured on my Things Stack application?
  - id: ApplicationWebhookRegistry_Delete
    intent: Delete a webhook
    question: How do I remove a webhook from my application?
  - id: ApplicationWebhookRegistry_Get
    intent: Get a webhook's configuration
    question: What URL and message types is a given webhook configured with?
  - id: ApplicationWebhookRegistry_Set2
    intent: Create a webhook for an application
    question: How do I add a new webhook to forward my application's uplinks to my server?
  - id: ApplicationWebhookRegistry_Set
    intent: Create or update a named webhook
    question: How do I change the endpoint of an existing webhook?
  phrasing_ops: 8
  slug: the-things-network-applicationwebhookregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The As API from The Things Network / The Things Stack — 4 operation(s) for as.
  name: The Things Network / The Things Stack As API
  phrasing_intents:
  - id: As_GetLink
    intent: Get an application's Network Server link config
    question: How is my application linked from the Application Server to the Network Server?
  - id: As_SetLink
    intent: Configure an application's Network Server link
    question: How do I link my application to a Network Server?
  - id: As_DeleteLink
    intent: Remove an application's Network Server link
    question: How do I unlink my application from the Network Server?
  - id: As_GetLinkStats
    intent: Get link statistics and errors
    question: Is my application's link to the Network Server healthy?
  - id: As_GetConfiguration
    intent: Get Application Server configuration
    question: What configuration is the Application Server running with?
  phrasing_ops: 5
  slug: the-things-network-as-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The AsEndDeviceBatchRegistry API from The Things Network / The Things Stack — 1 operation(s) for asenddevicebatchregistry.
  name: The Things Network / The Things Stack AsEndDeviceBatchRegistry API
  phrasing_intents:
  - id: AsEndDeviceBatchRegistry_Delete
    intent: Delete a batch of devices from the Application Server
    question: Can I delete many devices from the Application Server in one all-or-nothing request?
  phrasing_ops: 1
  slug: the-things-network-asenddevicebatchregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The AsEndDeviceRegistry API from The Things Network / The Things Stack — 4 operation(s) for asenddeviceregistry.
  name: The Things Network / The Things Stack AsEndDeviceRegistry API
  phrasing_intents:
  - id: AsEndDeviceRegistry_Delete
    intent: Delete a device from the Application Server
    question: Can I remove a device's record from the Application Server alone?
  - id: AsEndDeviceRegistry_Set2
    intent: Create a device on the Application Server
    question: How do I register a new end device on the Application Server?
  - id: AsEndDeviceRegistry_Set
    intent: Update a device on the Application Server
    question: How do I change an existing device's Application Server settings, like its payload formatter?
  - id: AsEndDeviceRegistry_Get
    intent: Get a device from the Application Server
    question: What does the Application Server store about one of my devices?
  phrasing_ops: 4
  slug: the-things-network-asenddeviceregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ClientAccess API from The Things Network / The Things Stack — 6 operation(s) for clientaccess.
  name: The Things Network / The Things Stack ClientAccess API
  phrasing_intents:
  - id: ClientAccess_GetCollaborator2
    intent: Get an organization's rights on an OAuth client
    question: What rights does an organization have on my OAuth client?
  - id: ClientAccess_GetCollaborator
    intent: Get a user's rights on an OAuth client
    question: What can a specific user do on my OAuth client?
  - id: ClientAccess_ListCollaborators
    intent: List an OAuth client's collaborators
    question: Who has collaborator access to my OAuth client?
  - id: ClientAccess_SetCollaborator
    intent: Add a collaborator or set rights on an OAuth client
    question: How do I give another user or organization access to manage my OAuth client?
  - id: ClientAccess_DeleteCollaborator2
    intent: Remove an organization from an OAuth client
    question: How do I remove an organization's access to my OAuth client?
  - id: ClientAccess_DeleteCollaborator
    intent: Remove a user from an OAuth client
    question: How do I take away a person's access to an OAuth client?
  - id: ClientAccess_ListRights
    intent: List my rights on an OAuth client
    question: What rights do my credentials give me on this OAuth client?
  phrasing_ops: 7
  slug: the-things-network-clientaccess-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ClientRegistry API from The Things Network / The Things Stack — 8 operation(s) for clientregistry.
  name: The Things Network / The Things Stack ClientRegistry API
  phrasing_intents:
  - id: ClientRegistry_List
    intent: List OAuth clients I can access
    question: Which OAuth clients are registered that I have access to on The Things Stack?
  - id: ClientRegistry_Update
    intent: Update an OAuth client
    question: How do I change the redirect URIs or name of an OAuth client?
  - id: ClientRegistry_Get
    intent: Get an OAuth client
    question: What is configured on a specific OAuth client?
  - id: ClientRegistry_Delete
    intent: Delete an OAuth client
    question: How do I delete an OAuth client I no longer need?
  - id: ClientRegistry_Purge
    intent: Permanently purge an OAuth client
    question: How do I purge an OAuth client so its client ID is released?
  - id: ClientRegistry_Restore
    intent: Restore a deleted OAuth client
    question: Can I restore an OAuth client that was recently deleted?
  - id: ClientRegistry_List3
    intent: List an organization's OAuth clients
    question: Which OAuth clients does an organization collaborate on?
  - id: ClientRegistry_Create2
    intent: Create an OAuth client under an organization
    question: How do I register a new OAuth client owned by an organization?
  phrasing_ops: 10
  slug: the-things-network-clientregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Configuration API from The Things Network / The Things Stack — 5 operation(s) for configuration.
  name: The Things Network / The Things Stack Configuration API
  phrasing_intents:
  - id: Configuration_ListBands
    intent: List LoRaWAN bands
    question: Which LoRaWAN regional bands does The Things Stack support?
  - id: Configuration_ListBands2
    intent: Get a band's definitions across PHY versions
    question: What are the parameters of a specific band like EU_863_870?
  - id: Configuration_ListBands3
    intent: Get a band for one PHY version
    question: What does a band look like under one exact regional parameters version?
  - id: Configuration_ListFrequencyPlans
    intent: List frequency plans
    question: Which frequency plans are available for my region?
  - id: Configuration_GetPhyVersions
    intent: List supported PHY versions for a band
    question: Which LoRaWAN PHY versions are supported for my band?
  phrasing_ops: 5
  slug: the-things-network-configuration-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ContactInfoRegistry API from The Things Network / The Things Stack — 1 operation(s) for contactinforegistry.
  name: The Things Network / The Things Stack ContactInfoRegistry API
  phrasing_intents:
  - id: ContactInfoRegistry_RequestValidation
    intent: Request contact info validation for an entity
    question: How do I resend the validation email for an entity's contact info?
  - id: ContactInfoRegistry_Validate
    intent: Confirm a contact info validation
    question: How do I confirm contact info using the validation token I received?
  phrasing_ops: 2
  slug: the-things-network-contactinforegistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The DeviceRepository API from The Things Network / The Things Stack — 20 operation(s) for devicerepository.
  name: The Things Network / The Things Stack DeviceRepository API
  phrasing_intents:
  - id: DeviceRepository_ListBrands2
    intent: List device brands as seen by an application
    question: Which device manufacturers can I pick from when adding devices to my Things Stack application?
  - id: DeviceRepository_GetBrand2
    intent: Get a device brand in an application context
    question: What details does the repository hold about one brand when I look it up through my application?
  - id: DeviceRepository_ListModels4
    intent: List a brand's models for an application
    question: Which device models does one manufacturer offer, as listed for my application?
  - id: DeviceRepository_GetModel2
    intent: Get a device model in an application context
    question: What does the Device Repository say about one specific model when accessed through my application?
  - id: DeviceRepository_GetDownlinkDecoder2
    intent: Get a model's downlink decoder for an application
    question: Where can I get the payload formatter that decodes downlinks for a device model in my application?
  - id: DeviceRepository_GetDownlinkEncoder2
    intent: Get a model's downlink encoder for an application
    question: How can my application get the formatter that encodes downlink messages for a given device model?
  - id: DeviceRepository_GetUplinkDecoder2
    intent: Get a model's uplink decoder for an application
    question: Can my application pull the ready-made uplink payload decoder for the sensor model I use?
  - id: DeviceRepository_GetTemplate3
    intent: Get an end device template by model for an application
    question: Can I get a pre-filled end device template for a model and firmware to onboard into my application?
  phrasing_ops: 20
  slug: the-things-network-devicerepository-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EmailValidationRegistry API from The Things Network / The Things Stack — 1 operation(s) for emailvalidationregistry.
  name: The Things Network / The Things Stack EmailValidationRegistry API
  phrasing_intents:
  - id: EmailValidationRegistry_RequestValidation
    intent: Request email address validation
    question: How do I get a new verification email for my user account?
  - id: EmailValidationRegistry_Validate
    intent: Confirm an email address
    question: How do I confirm my email address with the token from the email?
  phrasing_ops: 2
  slug: the-things-network-emailvalidationregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceBatchClaimingServer API from The Things Network / The Things Stack — 2 operation(s) for enddevicebatchclaimingserver.
  name: The Things Network / The Things Stack EndDeviceBatchClaimingServer API
  phrasing_intents:
  - id: EndDeviceBatchClaimingServer_GetInfoByJoinEUIs
    intent: Check claiming support for many JoinEUIs
    question: Can I check claiming support for a whole list of JoinEUIs in one request?
  - id: EndDeviceBatchClaimingServer_Unclaim
    intent: Unclaim a batch of end devices
    question: How do I unclaim many devices from an external Join Server at once?
  phrasing_ops: 2
  slug: the-things-network-enddevicebatchclaimingserver-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceBatchRegistry API from The Things Network / The Things Stack — 1 operation(s) for enddevicebatchregistry.
  name: The Things Network / The Things Stack EndDeviceBatchRegistry API
  phrasing_intents:
  - id: EndDeviceBatchRegistry_Get
    intent: Get several end devices at once
    question: Can I fetch multiple end devices in one call?
  - id: EndDeviceBatchRegistry_Delete
    intent: Delete several end devices from the registry
    question: How do I delete a batch of end devices from the Identity Server in one go?
  phrasing_ops: 2
  slug: the-things-network-enddevicebatchregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceClaimingServer API from The Things Network / The Things Stack — 5 operation(s) for enddeviceclaimingserver.
  name: The Things Network / The Things Stack EndDeviceClaimingServer API
  phrasing_intents:
  - id: EndDeviceClaimingServer_AuthorizeApplication
    intent: Authorize device claiming for an application
    question: How do I let the claiming server claim devices registered in my application?
  - id: EndDeviceClaimingServer_UnauthorizeApplication
    intent: Revoke device claiming for an application
    question: How do I stop the claiming server from claiming devices in my app?
  - id: EndDeviceClaimingServer_Claim
    intent: Claim an end device into an application
    question: How do I claim a device into my application using its QR code?
  - id: EndDeviceClaimingServer_GetInfoByJoinEUI
    intent: Check if claiming is available for a JoinEUI
    question: Can devices with a given JoinEUI be claimed?
  - id: EndDeviceClaimingServer_GetClaimStatus
    intent: Get an end device's claim status
    question: Has my end device been claimed on the Join Server?
  - id: EndDeviceClaimingServer_Unclaim
    intent: Unclaim a single end device
    question: How do I release one claimed device from the Join Server?
  phrasing_ops: 6
  slug: the-things-network-enddeviceclaimingserver-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceQRCodeGenerator API from The Things Network / The Things Stack — 5 operation(s) for enddeviceqrcodegenerator.
  name: The Things Network / The Things Stack EndDeviceQRCodeGenerator API
  phrasing_intents:
  - id: EndDeviceQRCodeGenerator_Generate
    intent: Generate a QR code for an end device
    question: How do I generate an onboarding QR code for one of my end devices?
  - id: EndDeviceQRCodeGenerator_ListFormats
    intent: List supported end device QR code formats
    question: Which QR code formats does The Things Stack support for devices?
  - id: EndDeviceQRCodeGenerator_GetFormat
    intent: Get an end device QR code format
    question: What fields does a specific device QR code format contain?
  - id: EndDeviceQRCodeGenerator_Parse
    intent: Parse a device QR code of any known format
    question: Can I decode a device QR code without knowing its format first?
  - id: EndDeviceQRCodeGenerator_Parse2
    intent: Parse a device QR code in a given format
    question: How do I decode a device QR code when I already know its format ID?
  phrasing_ops: 5
  slug: the-things-network-enddeviceqrcodegenerator-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceRegistry API from The Things Network / The Things Stack — 7 operation(s) for enddeviceregistry.
  name: The Things Network / The Things Stack EndDeviceRegistry API
  phrasing_intents:
  - id: EndDeviceRegistry_List
    intent: List end devices in an application
    question: Which end devices are registered in my application?
  - id: EndDeviceRegistry_Count
    intent: Count end devices in an application
    question: How many end devices does my application have?
  - id: EndDeviceRegistry_List2
    intent: List end devices with filters
    question: Can I filter an application's end devices using structured criteria?
  - id: EndDeviceRegistry_Delete
    intent: Delete an end device from the registry
    question: How do I delete an end device from the Identity Server registry?
  - id: EndDeviceRegistry_Create
    intent: Register a new end device
    question: How do I add a new end device to my application?
  - id: EndDeviceRegistry_Update
    intent: Update an end device
    question: How do I rename an end device or change its attributes?
  - id: EndDeviceRegistry_Get
    intent: Get an end device
    question: What details are registered for one of my end devices?
  phrasing_ops: 7
  slug: the-things-network-enddeviceregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceRegistrySearch API from The Things Network / The Things Stack — 1 operation(s) for enddeviceregistrysearch.
  name: The Things Network / The Things Stack EndDeviceRegistrySearch API
  phrasing_intents:
  - id: EndDeviceRegistrySearch_SearchEndDevices
    intent: Search end devices in an application
    question: Is there a way to find a device in my application by part of its name or DevEUI?
  phrasing_ops: 1
  slug: the-things-network-enddeviceregistrysearch-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EndDeviceTemplateConverter API from The Things Network / The Things Stack — 2 operation(s) for enddevicetemplateconverter.
  name: The Things Network / The Things Stack EndDeviceTemplateConverter API
  phrasing_intents:
  - id: EndDeviceTemplateConverter_Convert
    intent: Convert vendor data into end device templates
    question: How do I convert a vendor's device file into end device templates for bulk import?
  - id: EndDeviceTemplateConverter_ListFormats
    intent: List formats the template converter accepts
    question: Which import formats can the end device template converter read?
  phrasing_ops: 2
  slug: the-things-network-enddevicetemplateconverter-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EntityAccess API from The Things Network / The Things Stack — 1 operation(s) for entityaccess.
  name: The Things Network / The Things Stack EntityAccess API
  phrasing_intents:
  - id: EntityAccess_AuthInfo
    intent: Get info about the current authentication
    question: Who am I authenticated as, and with what rights?
  phrasing_ops: 1
  slug: the-things-network-entityaccess-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The EntityRegistrySearch API from The Things Network / The Things Stack — 10 operation(s) for entityregistrysearch.
  name: The Things Network / The Things Stack EntityRegistrySearch API
  phrasing_intents:
  - id: EntityRegistrySearch_SearchAccounts2
    intent: Search accounts to add to an application
    question: How do I find a user or organization to add as a collaborator on my application?
  - id: EntityRegistrySearch_SearchAccounts3
    intent: Search accounts for an OAuth client
    question: Can I search for accounts to add as collaborators on an OAuth client?
  - id: EntityRegistrySearch_SearchAccounts4
    intent: Search accounts for a gateway
    question: How can I look up a user or organization to share my gateway with?
  - id: EntityRegistrySearch_SearchAccounts5
    intent: Search accounts for an organization
    question: How do I search for people to invite into my organization?
  - id: EntityRegistrySearch_SearchAccounts
    intent: Search user and organization accounts
    question: How do I search all user and organization accounts by name?
  - id: EntityRegistrySearch_SearchApplications
    intent: Search applications
    question: Which of my applications have an ID or name containing a word?
  - id: EntityRegistrySearch_SearchClients
    intent: Search OAuth clients
    question: How do I find OAuth clients by name or ID?
  - id: EntityRegistrySearch_SearchGateways
    intent: Search gateways
    question: Can I search my gateways by part of their EUI?
  phrasing_ops: 10
  slug: the-things-network-entityregistrysearch-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Events API from The Things Network / The Things Stack — 2 operation(s) for events.
  name: The Things Network / The Things Stack Events API
  phrasing_intents:
  - id: Events_Stream
    intent: Stream live events
    question: How do I watch live events for my applications, gateways or devices?
  - id: Events_FindRelated
    intent: Find events related by correlation ID
    question: How do I find all events that share a correlation ID?
  phrasing_ops: 2
  slug: the-things-network-events-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayAccess API from The Things Network / The Things Stack — 9 operation(s) for gatewayaccess.
  name: The Things Network / The Things Stack GatewayAccess API
  phrasing_intents:
  - id: GatewayAccess_ListAPIKeys
    intent: List a gateway's API keys
    question: Which API keys exist for my gateway?
  - id: GatewayAccess_CreateAPIKey
    intent: Create an API key for a gateway
    question: How do I create an API key that only works for one gateway?
  - id: GatewayAccess_UpdateAPIKey
    intent: Change the rights of a gateway API key
    question: How do I change what an existing gateway API key is allowed to do?
  - id: GatewayAccess_GetAPIKey
    intent: Get one API key of a gateway
    question: What rights does a specific API key on my gateway have?
  - id: GatewayAccess_DeleteAPIKey
    intent: Delete a gateway API key
    question: How do I delete an API key from my gateway outright?
  - id: GatewayAccess_GetCollaborator2
    intent: Get an organization's rights on a gateway
    question: What rights does an organization have as a collaborator on my gateway?
  - id: GatewayAccess_GetCollaborator
    intent: Get a user's rights on a gateway
    question: What rights does a particular user have on my gateway?
  - id: GatewayAccess_ListCollaborators
    intent: List a gateway's collaborators
    question: Who has access to my gateway as a collaborator?
  phrasing_ops: 12
  slug: the-things-network-gatewayaccess-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayBatchAccess API from The Things Network / The Things Stack — 1 operation(s) for gatewaybatchaccess.
  name: The Things Network / The Things Stack GatewayBatchAccess API
  phrasing_intents:
  - id: GatewayBatchAccess_AssertRights
    intent: Check my rights across several gateways
    question: Can I verify that I hold certain rights on a whole set of gateways at once?
  phrasing_ops: 1
  slug: the-things-network-gatewaybatchaccess-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayBatchRegistry API from The Things Network / The Things Stack — 1 operation(s) for gatewaybatchregistry.
  name: The Things Network / The Things Stack GatewayBatchRegistry API
  phrasing_intents:
  - id: GatewayBatchRegistry_Delete
    intent: Delete several gateways at once
    question: Can I delete multiple gateways in one atomic call?
  phrasing_ops: 1
  slug: the-things-network-gatewaybatchregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayClaimingServer API from The Things Network / The Things Stack — 5 operation(s) for gatewayclaimingserver.
  name: The Things Network / The Things Stack GatewayClaimingServer API
  phrasing_intents:
  - id: GatewayClaimingServer_Claim
    intent: Claim a gateway
    question: How do I claim a gateway I bought using its claim authentication code?
  - id: GatewayClaimingServer_GetInfoByGatewayEUI
    intent: Check if a gateway EUI can be claimed
    question: Is claiming supported for my gateway's EUI?
  - id: GatewayClaimingServer_Unclaim
    intent: Unclaim a gateway
    question: How do I release a gateway I claimed so someone else can claim it?
  - id: GatewayClaimingServer_AuthorizeGateway
    intent: Authorize a gateway for claiming (deprecated)
    question: What did the deprecated gateway claim authorization do?
  - id: GatewayClaimingServer_UnauthorizeGateway
    intent: Lock a gateway against claiming (deprecated)
    question: How did I stop a gateway from being claimed with the old unauthorize call?
  phrasing_ops: 5
  slug: the-things-network-gatewayclaimingserver-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayConfigurationService API from The Things Network / The Things Stack — 2 operation(s) for gatewayconfigurationservice.
  name: The Things Network / The Things Stack GatewayConfigurationService API
  phrasing_intents:
  - id: GatewayConfigurationService_GetGatewayConfiguration
    intent: Download a gateway configuration file
    question: How do I download the configuration file for my gateway in a given format?
  - id: GatewayConfigurationService_GetGatewayConfiguration2
    intent: Download a typed gateway configuration file
    question: Can I fetch a gateway config file where the type is part of the URL path?
  phrasing_ops: 2
  slug: the-things-network-gatewayconfigurationservice-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayQRCodeGenerator API from The Things Network / The Things Stack — 2 operation(s) for gatewayqrcodegenerator.
  name: The Things Network / The Things Stack GatewayQRCodeGenerator API
  phrasing_intents:
  - id: GatewayQRCodeGenerator_Parse
    intent: Parse a gateway QR code
    question: How do I read the gateway details encoded in a QR code?
  - id: GatewayQRCodeGenerator_Parse2
    intent: Parse a gateway QR code of a known format
    question: Can I parse a gateway QR code when I already know its format?
  phrasing_ops: 2
  slug: the-things-network-gatewayqrcodegenerator-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GatewayRegistry API from The Things Network / The Things Stack — 9 operation(s) for gatewayregistry.
  name: The Things Network / The Things Stack GatewayRegistry API
  phrasing_intents:
  - id: GatewayRegistry_List
    intent: List gateways I can access
    question: Which gateways do I have access to on The Things Stack?
  - id: GatewayRegistry_List4
    intent: List gateways with filters
    question: Can I list gateways using filter criteria in a request body?
  - id: GatewayRegistry_Update
    intent: Update a gateway's settings
    question: How do I change a gateway's name, frequency plan or other settings?
  - id: GatewayRegistry_Get
    intent: Get a gateway
    question: What are the details of one of my gateways?
  - id: GatewayRegistry_Delete
    intent: Delete a gateway (restorable)
    question: What happens to the gateway EUI when I delete a gateway?
  - id: GatewayRegistry_Purge
    intent: Permanently purge a gateway
    question: How do I permanently remove a gateway so both its ID and EUI can be reused?
  - id: GatewayRegistry_Restore
    intent: Restore a recently deleted gateway
    question: Can I undo deleting a gateway?
  - id: GatewayRegistry_List3
    intent: List an organization's gateways
    question: Which gateways does my organization collaborate on?
  phrasing_ops: 11
  slug: the-things-network-gatewayregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Gs API from The Things Network / The Things Stack — 2 operation(s) for gs.
  name: The Things Network / The Things Stack Gs API
  phrasing_intents:
  - id: Gs_BatchGetGatewayConnectionStats
    intent: Get connection stats for many gateways
    question: Can I get connection statistics for several gateways in one call?
  - id: Gs_GetGatewayConnectionStats
    intent: Get one gateway's connection stats
    question: How do I see whether my gateway is connected and when it last sent traffic?
  phrasing_ops: 2
  slug: the-things-network-gs-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The GtwGs API from The Things Network / The Things Stack — 2 operation(s) for gtwgs.
  name: The Things Network / The Things Stack GtwGs API
  phrasing_intents:
  - id: GtwGs_GetMQTTConnectionInfo
    intent: Get MQTT connection info for a gateway
    question: How do I connect a gateway to the Gateway Server over MQTT?
  - id: GtwGs_GetMQTTV2ConnectionInfo
    intent: Get legacy V2 MQTT connection info for a gateway
    question: How do I connect an older The Things Network Stack V2 MQTT gateway?
  phrasing_ops: 2
  slug: the-things-network-gtwgs-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Is API from The Things Network / The Things Stack — 1 operation(s) for is.
  name: The Things Network / The Things Stack Is API
  phrasing_intents:
  - id: Is_GetConfiguration
    intent: Get the Identity Server configuration
    question: What features are enabled on this Things Stack Identity Server?
  phrasing_ops: 1
  slug: the-things-network-is-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Js API from The Things Network / The Things Stack — 2 operation(s) for js.
  name: The Things Network / The Things Stack Js API
  phrasing_intents:
  - id: Js_GetDefaultJoinEUI
    intent: Get the Join Server's default JoinEUI
    question: What default JoinEUI is configured on this Join Server?
  - id: Js_GetJoinEUIPrefixes
    intent: List the Join Server's JoinEUI prefixes
    question: Which JoinEUI prefixes does this Join Server handle?
  phrasing_ops: 2
  slug: the-things-network-js-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The JsEndDeviceBatchRegistry API from The Things Network / The Things Stack — 1 operation(s) for jsenddevicebatchregistry.
  name: The Things Network / The Things Stack JsEndDeviceBatchRegistry API
  phrasing_intents:
  - id: JsEndDeviceBatchRegistry_Delete
    intent: Delete several devices from the Join Server
    question: How do I remove many end devices from the Join Server at once?
  phrasing_ops: 1
  slug: the-things-network-jsenddevicebatchregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The JsEndDeviceRegistry API from The Things Network / The Things Stack — 5 operation(s) for jsenddeviceregistry.
  name: The Things Network / The Things Stack JsEndDeviceRegistry API
  phrasing_intents:
  - id: JsEndDeviceRegistry_Delete
    intent: Delete a device from the Join Server
    question: How do I remove an end device's keys and record from the Join Server?
  - id: JsEndDeviceRegistry_Provision
    intent: Provision devices on the Join Server (deprecated)
    question: Can I still bulk provision devices on the Join Server with vendor provisioning data?
  - id: JsEndDeviceRegistry_Set2
    intent: Create a device on the Join Server
    question: How do I register a new device's root keys on the Join Server?
  - id: JsEndDeviceRegistry_Set
    intent: Update a device on the Join Server
    question: How do I update an existing device's Join Server settings or keys?
  - id: JsEndDeviceRegistry_Get
    intent: Get a device from the Join Server
    question: What does the Join Server store about one of my devices?
  phrasing_ops: 5
  slug: the-things-network-jsenddeviceregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ManagedGatewayConfigurationService API from The Things Network / The Things Stack — 4 operation(s) for managedgatewayconfigurationservice.
  name: The Things Network / The Things Stack ManagedGatewayConfigurationService API
  phrasing_intents:
  - id: ManagedGatewayConfigurationService_Update
    intent: Update a managed gateway's configuration
    question: How do I change the settings of a managed gateway?
  - id: ManagedGatewayConfigurationService_Get
    intent: Get a managed gateway's configuration
    question: What configuration is my managed gateway running?
  - id: ManagedGatewayConfigurationService_StreamEvents
    intent: Stream events from a managed gateway
    question: Can I watch live events coming from my managed gateway?
  - id: ManagedGatewayConfigurationService_ScanWiFiAccessPoints
    intent: Scan WiFi networks from a managed gateway
    question: Which WiFi access points can my managed gateway see?
  phrasing_ops: 4
  slug: the-things-network-managedgatewayconfigurationservice-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ManagedGatewayEthernetProfileConfigurationService API from The Things Network / The Things Stack — 6 operation(s) for managedgatewayethernetprofileconfigurationservice.
  name: The Things Network / The Things Stack ManagedGatewayEthernetProfileConfigurationService API
  phrasing_intents:
  - id: ManagedGatewayEthernetProfileConfigurationService_List
    intent: List an organization's gateway Ethernet profiles
    question: Which Ethernet profiles has my organization saved for managed gateways?
  - id: ManagedGatewayEthernetProfileConfigurationService_Create
    intent: Create an Ethernet profile for an organization
    question: How do I save a reusable Ethernet network profile for my organization's managed gateways?
  - id: ManagedGatewayEthernetProfileConfigurationService_Update
    intent: Update an organization's Ethernet profile
    question: How do I change the settings of an organization's managed gateway Ethernet profile?
  - id: ManagedGatewayEthernetProfileConfigurationService_Get
    intent: Get an organization's Ethernet profile
    question: What settings are in one of my organization's Ethernet profiles?
  - id: ManagedGatewayEthernetProfileConfigurationService_Delete
    intent: Delete an organization's Ethernet profile
    question: How do I remove an Ethernet profile my organization no longer uses?
  - id: ManagedGatewayEthernetProfileConfigurationService_List2
    intent: List a user's gateway Ethernet profiles
    question: Which managed gateway Ethernet profiles are saved under my personal account?
  - id: ManagedGatewayEthernetProfileConfigurationService_Create2
    intent: Create an Ethernet profile for a user
    question: How do I save an Ethernet network profile to my own user account for a managed gateway?
  - id: ManagedGatewayEthernetProfileConfigurationService_Update2
    intent: Update a user's Ethernet profile
    question: How do I edit an Ethernet profile saved under my user account?
  phrasing_ops: 10
  slug: the-things-network-managedgatewayethernetprofileconfigurationservice-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The ManagedGatewayWiFiProfileConfigurationService API from The Things Network / The Things Stack — 6 operation(s) for managedgatewaywifiprofileconfigurationservice.
  name: The Things Network / The Things Stack ManagedGatewayWiFiProfileConfigurationService API
  phrasing_intents:
  - id: ManagedGatewayWiFiProfileConfigurationService_List
    intent: List an organization's WiFi profiles
    question: Which WiFi profiles has my organization saved for managed gateways?
  - id: ManagedGatewayWiFiProfileConfigurationService_Create
    intent: Create a WiFi profile for an organization
    question: How do I save a WiFi network profile that my organization's managed gateways can use?
  - id: ManagedGatewayWiFiProfileConfigurationService_Update
    intent: Update an organization's WiFi profile
    question: How do I change the SSID or credentials in an organization's gateway WiFi profile?
  - id: ManagedGatewayWiFiProfileConfigurationService_Get
    intent: Get an organization's WiFi profile
    question: What settings are stored in one of my organization's gateway WiFi profiles?
  - id: ManagedGatewayWiFiProfileConfigurationService_Delete
    intent: Delete an organization's WiFi profile
    question: How do I remove an old WiFi profile from my organization?
  - id: ManagedGatewayWiFiProfileConfigurationService_List2
    intent: List a user's WiFi profiles
    question: Which WiFi profiles have I saved on my own user account for managed gateways?
  - id: ManagedGatewayWiFiProfileConfigurationService_Create2
    intent: Create a WiFi profile for a user
    question: How do I save a personal WiFi profile for my managed gateway?
  - id: ManagedGatewayWiFiProfileConfigurationService_Update2
    intent: Update a user's WiFi profile
    question: How do I edit a WiFi profile stored on my user account?
  phrasing_ops: 10
  slug: the-things-network-managedgatewaywifiprofileconfigurationservice-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Ns API from The Things Network / The Things Stack — 4 operation(s) for ns.
  name: The Things Network / The Things Stack Ns API
  phrasing_intents:
  - id: Ns_GetDefaultMACSettings
    intent: Get default MAC settings for a frequency plan
    question: What default MAC settings does the Network Server use for a frequency plan?
  - id: Ns_GenerateDevAddr
    intent: Request a device address from the Network Server
    question: How do I get a DevAddr assigned for an ABP device?
  - id: Ns_GetDeviceAddressPrefixes
    intent: List the Network Server's DevAddr prefixes
    question: Which DevAddr prefixes is this Network Server configured to use?
  - id: Ns_GetNetID
    intent: Get the Network Server's NetID
    question: What NetID is this Network Server operating under?
  phrasing_ops: 4
  slug: the-things-network-ns-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The NsEndDeviceBatchRegistry API from The Things Network / The Things Stack — 2 operation(s) for nsenddevicebatchregistry.
  name: The Things Network / The Things Stack NsEndDeviceBatchRegistry API
  phrasing_intents:
  - id: NsEndDeviceBatchRegistry_Delete
    intent: Delete a batch of devices from the Network Server
    question: How do I delete many devices from the Network Server in one atomic call?
  - id: NsEndDeviceBatchRegistry_SetMACSettingsProfile
    intent: Apply a MAC settings profile to many devices
    question: Can I assign one MAC settings profile to a batch of devices at once?
  phrasing_ops: 2
  slug: the-things-network-nsenddevicebatchregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The NsEndDeviceRegistry API from The Things Network / The Things Stack — 4 operation(s) for nsenddeviceregistry.
  name: The Things Network / The Things Stack NsEndDeviceRegistry API
  phrasing_intents:
  - id: NsEndDeviceRegistry_Delete
    intent: Delete a device from the Network Server
    question: How do I remove an end device from the Network Server registry?
  - id: NsEndDeviceRegistry_Set2
    intent: Register a device on the Network Server
    question: How do I add a new end device's MAC settings to the Network Server?
  - id: NsEndDeviceRegistry_Set
    intent: Update a device on the Network Server
    question: How do I change an existing device's network-layer settings like its MAC version?
  - id: NsEndDeviceRegistry_Get
    intent: Get a device's Network Server state
    question: What network-layer settings and session does the Network Server hold for my device?
  - id: NsEndDeviceRegistry_ResetFactoryDefaults
    intent: Reset a device to factory defaults
    question: How do I reset an end device's Network Server state to factory defaults?
  phrasing_ops: 5
  slug: the-things-network-nsenddeviceregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The NsMACSettingsProfileRegistry API from The Things Network / The Things Stack — 3 operation(s) for nsmacsettingsprofileregistry.
  name: The Things Network / The Things Stack NsMACSettingsProfileRegistry API
  phrasing_intents:
  - id: NsMACSettingsProfileRegistry_List
    intent: List an application's MAC settings profiles
    question: Which MAC settings profiles exist in my application?
  - id: NsMACSettingsProfileRegistry_Create
    intent: Create a MAC settings profile
    question: How do I create a reusable MAC settings profile for devices in my application?
  - id: NsMACSettingsProfileRegistry_Get
    intent: Get a MAC settings profile
    question: What MAC settings are in a specific profile?
  - id: NsMACSettingsProfileRegistry_Delete
    intent: Delete a MAC settings profile
    question: How do I remove a MAC settings profile I no longer use?
  - id: NsMACSettingsProfileRegistry_Update
    intent: Update a MAC settings profile
    question: How do I change the settings in an existing MAC settings profile?
  phrasing_ops: 5
  slug: the-things-network-nsmacsettingsprofileregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The NsRelayConfigurationService API from The Things Network / The Things Stack — 4 operation(s) for nsrelayconfigurationservice.
  name: The Things Network / The Things Stack NsRelayConfigurationService API
  phrasing_intents:
  - id: NsRelayConfigurationService_CreateRelay
    intent: Configure an end device as a LoRaWAN relay
    question: How do I turn one of my end devices into a LoRaWAN relay on the Network Server?
  - id: NsRelayConfigurationService_GetRelay
    intent: Get a device's relay configuration
    question: What relay settings are configured on a particular end device?
  - id: NsRelayConfigurationService_DeleteRelay
    intent: Remove relay configuration from a device
    question: How do I stop an end device from acting as a relay?
  - id: NsRelayConfigurationService_UpdateRelay
    intent: Update a relay's settings
    question: How do I change the settings of an existing relay device?
  - id: NsRelayConfigurationService_ListRelayUplinkForwardingRules
    intent: List a relay's uplink forwarding rules
    question: Which uplink forwarding rules are set on my relay?
  - id: NsRelayConfigurationService_CreateRelayUplinkForwardingRule
    intent: Add an uplink forwarding rule to a relay
    question: How do I add a rule telling a relay which uplinks to forward?
  - id: NsRelayConfigurationService_GetRelayUplinkForwardingRule
    intent: Get one relay uplink forwarding rule
    question: What does the forwarding rule at a given index on my relay contain?
  - id: NsRelayConfigurationService_DeleteRelayUplinkForwardingRule
    intent: Delete a relay uplink forwarding rule
    question: How do I remove one forwarding rule from a relay?
  phrasing_ops: 9
  slug: the-things-network-nsrelayconfigurationservice-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The OAuthAuthorizationRegistry API from The Things Network / The Things Stack — 4 operation(s) for oauthauthorizationregistry.
  name: The Things Network / The Things Stack OAuthAuthorizationRegistry API
  phrasing_intents:
  - id: OAuthAuthorizationRegistry_List
    intent: List OAuth clients a user has authorized
    question: Which apps have I granted OAuth access to my account?
  - id: OAuthAuthorizationRegistry_Delete
    intent: De-authorize an OAuth client
    question: How do I revoke a third-party app's OAuth access to my account?
  - id: OAuthAuthorizationRegistry_ListTokens
    intent: List OAuth tokens issued to a client
    question: What access tokens has an OAuth client been issued on my behalf?
  - id: OAuthAuthorizationRegistry_DeleteToken
    intent: Invalidate an OAuth access token
    question: How do I invalidate a single OAuth access token?
  phrasing_ops: 4
  slug: the-things-network-oauthauthorizationregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The OrganizationRegistry API from The Things Network / The Things Stack — 7 operation(s) for organizationregistry.
  name: The Things Network / The Things Stack OrganizationRegistry API
  phrasing_intents:
  - id: OrganizationRegistry_List
    intent: List organizations I can access
    question: Which organizations do I belong to?
  - id: OrganizationRegistry_Update
    intent: Update an organization
    question: How do I rename my organization or change its description?
  - id: OrganizationRegistry_Get
    intent: Get an organization
    question: What details are stored for my organization?
  - id: OrganizationRegistry_Delete
    intent: Delete an organization (restorable)
    question: What happens when I delete an organization; can I get it back?
  - id: OrganizationRegistry_Purge
    intent: Permanently purge an organization
    question: How do I permanently remove an organization so its ID can be reused?
  - id: OrganizationRegistry_Restore
    intent: Restore a recently deleted organization
    question: Can I bring back an organization I just deleted?
  - id: OrganizationRegistry_List2
    intent: List a user's organizations
    question: Which organizations is a specific user a direct member of?
  - id: OrganizationRegistry_Create
    intent: Create an organization
    question: How do I create a new organization on The Things Stack?
  phrasing_ops: 8
  slug: the-things-network-organizationregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Pba API from The Things Network / The Things Stack — 12 operation(s) for pba.
  name: The Things Network / The Things Stack Pba API
  phrasing_intents:
  - id: Pba_ListForwarderRoutingPolicies
    intent: List routing policies forwarders set toward my network
    question: Which forwarders on Packet Broker have configured routing policies toward my network as Home Network?
  - id: Pba_ListHomeNetworks
    intent: List home networks available for routing policies
    question: What home networks are listed on Packet Broker that I can configure routing policies for?
  - id: Pba_GetHomeNetworkDefaultGatewayVisibility
    intent: Get the default gateway visibility
    question: What gateway information do we share with home networks by default through Packet Broker?
  - id: Pba_DeleteHomeNetworkDefaultGatewayVisibility
    intent: Remove the default gateway visibility
    question: How do I clear the default gateway visibility so no default is set?
  - id: Pba_SetHomeNetworkDefaultGatewayVisibility2
    intent: Set the default gateway visibility (POST)
    question: Is there a POST variant for setting the default gateway visibility?
  - id: Pba_SetHomeNetworkDefaultGatewayVisibility
    intent: Set the default gateway visibility (PUT)
    question: How do I change which gateway details home networks see by default, using PUT?
  - id: Pba_ListHomeNetworkRoutingPolicies
    intent: List my routing policies toward home networks
    question: Which routing policies has our Packet Broker Agent, as Forwarder, set for home networks?
  - id: Pba_GetHomeNetworkDefaultRoutingPolicy
    intent: Get the default routing policy
    question: What uplink and downlink routing applies by default to home networks without their own policy?
  phrasing_ops: 24
  slug: the-things-network-pba-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The UserBookmarkRegistry API from The Things Network / The Things Stack — 8 operation(s) for userbookmarkregistry.
  name: The Things Network / The Things Stack UserBookmarkRegistry API
  phrasing_intents:
  - id: UserBookmarkRegistry_List
    intent: List a user's bookmarks
    question: Which applications, gateways and devices has a user bookmarked?
  - id: UserBookmarkRegistry_Create
    intent: Bookmark an entity for a user
    question: How do I bookmark an application or gateway so it shows up in my favorites?
  - id: UserBookmarkRegistry_Delete
    intent: Remove an application bookmark
    question: How do I unbookmark an application?
  - id: UserBookmarkRegistry_Delete6
    intent: Remove an end device bookmark
    question: How do I unbookmark a single end device?
  - id: UserBookmarkRegistry_BatchDelete
    intent: Remove several bookmarks at once
    question: Can I clear multiple bookmarks in one atomic operation?
  - id: UserBookmarkRegistry_Delete2
    intent: Remove an OAuth client bookmark
    question: How do I unbookmark an OAuth client?
  - id: UserBookmarkRegistry_Delete3
    intent: Remove a gateway bookmark
    question: How do I unbookmark a gateway?
  - id: UserBookmarkRegistry_Delete4
    intent: Remove an organization bookmark
    question: How do I unbookmark an organization?
  phrasing_ops: 9
  slug: the-things-network-userbookmarkregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The UserInvitationRegistry API from The Things Network / The Things Stack — 1 operation(s) for userinvitationregistry.
  name: The Things Network / The Things Stack UserInvitationRegistry API
  phrasing_intents:
  - id: UserInvitationRegistry_List
    intent: List invitations I have sent
    question: Which network invitations have I sent that are still outstanding?
  - id: UserInvitationRegistry_Delete
    intent: Revoke a user invitation
    question: How do I cancel an invitation I sent by mistake?
  - id: UserInvitationRegistry_Send
    intent: Invite someone to join the network
    question: How do I invite a new person to join The Things Stack network by email?
  phrasing_ops: 3
  slug: the-things-network-userinvitationregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The UserRegistry API from The Things Network / The Things Stack — 8 operation(s) for userregistry.
  name: The Things Network / The Things Stack UserRegistry API
  phrasing_intents:
  - id: UserRegistry_List
    intent: List all users on the network
    question: Can an admin list every user registered on The Things Stack network?
  - id: UserRegistry_Create
    intent: Register a new user account
    question: How do I register a new user on the network?
  - id: UserRegistry_Update
    intent: Update a user's profile
    question: How do I change a user's name, email or other profile fields?
  - id: UserRegistry_Get
    intent: Get a user's profile
    question: What profile details are stored for a specific user?
  - id: UserRegistry_UpdatePassword
    intent: Change a user's password
    question: How do I change my password on The Things Stack?
  - id: UserRegistry_CreateTemporaryPassword
    intent: Email a temporary password for a forgotten one
    question: What do I do if a user forgot their password?
  - id: UserRegistry_Delete
    intent: Delete a user account
    question: How do I delete a user account from the network?
  - id: UserRegistry_Purge
    intent: Permanently purge a user account
    question: Can I purge a user so their ID can be reused?
  phrasing_ops: 9
  slug: the-things-network-userregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The UserSessionRegistry API from The Things Network / The Things Stack — 2 operation(s) for usersessionregistry.
  name: The Things Network / The Things Stack UserSessionRegistry API
  phrasing_intents:
  - id: UserSessionRegistry_List
    intent: List a user's active sessions
    question: Where am I currently logged in?
  - id: UserSessionRegistry_Delete
    intent: Revoke a user session
    question: How do I log out a session I don't recognize?
  phrasing_ops: 2
  slug: the-things-network-usersessionregistry-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Notification Service API from The Things Network / The Things Stack — 1 operation(s) for notification service.
  name: The Things Network / The Things Stack Notification Service API
  phrasing_intents:
  - id: NotificationService_List
    intent: List a user's notifications
    question: What notifications do I have on The Things Stack?
  - id: NotificationService_UpdateStatus
    intent: Mark notifications as read or archived
    question: How do I mark several notifications as read at once?
  phrasing_ops: 2
  slug: the-things-network-notification-service-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The Organization Access API from The Things Network / The Things Stack — 7 operation(s) for organization access.
  name: The Things Network / The Things Stack Organization Access API
  phrasing_intents:
  - id: OrganizationAccess_ListAPIKeys
    intent: List an organization's API keys
    question: Which API keys have been issued for my organization?
  - id: OrganizationAccess_CreateAPIKey
    intent: Create an organization API key
    question: How do I create an API key that can reach an organization and its applications and gateways?
  - id: OrganizationAccess_UpdateAPIKey
    intent: Change the rights of an organization API key
    question: Can I change the rights on an existing organization API key?
  - id: OrganizationAccess_GetAPIKey
    intent: Get one organization API key
    question: What rights does a specific organization API key carry?
  - id: OrganizationAccess_DeleteAPIKey
    intent: Delete an organization API key
    question: How do I revoke an API key issued for an organization?
  - id: OrganizationAccess_GetCollaborator
    intent: Get a member's rights in an organization
    question: What rights does a particular user have in my organization?
  - id: OrganizationAccess_ListCollaborators
    intent: List an organization's members
    question: Who are the members of my organization?
  - id: OrganizationAccess_SetCollaborator
    intent: Add a member or set their organization rights
    question: How do I add a user to my organization with specific rights?
  phrasing_ops: 10
  slug: the-things-network-organization-access-api
- baseURL: https://eu1.cloud.thethings.network/api/v3
  baseurl_source: declared
  description: The User Access API from The Things Network / The Things Stack — 5 operation(s) for user access.
  name: The Things Network / The Things Stack User Access API
  phrasing_intents:
  - id: UserAccess_ListAPIKeys
    intent: List a user's API keys
    question: Which personal API keys have I created on The Things Stack?
  - id: UserAccess_CreateAPIKey
    intent: Create a personal user API key
    question: How do I create a personal API key that can reach all my apps, gateways and organizations?
  - id: UserAccess_UpdateAPIKey
    intent: Change the rights of a user API key
    question: Can I change the rights on one of my personal API keys?
  - id: UserAccess_GetAPIKey
    intent: Get one user API key
    question: What rights does one of my personal API keys have?
  - id: UserAccess_DeleteAPIKey
    intent: Delete a user API key
    question: How do I revoke one of my personal API keys?
  - id: UserAccess_CreateLoginToken
    intent: Create a one-time login token for a user
    question: Can an admin generate a one-time login link for a user?
  - id: UserAccess_ListRights
    intent: List my rights on a user
    question: What rights do my credentials give me on this user account?
  phrasing_ops: 7
  slug: the-things-network-user-access-api
artifact_total: 217
asyncapis:
- description: ''
  name: The Things Network Webhooks
  slug: the-things-network-webhooks
collections:
- collection_type: postman
  name: The Things Stack — Application Server AppAs API
  slug: postman-the-things-network-appas-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationAccess API
  slug: postman-the-things-network-applicationaccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationActivationSettingRegistry API
  slug: postman-the-things-network-applicationactivationsettingregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationPackageRegistry API
  slug: postman-the-things-network-applicationpackageregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationPubSubRegistry API
  slug: postman-the-things-network-applicationpubsubregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationRegistry API
  slug: postman-the-things-network-applicationregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationUpStorage API
  slug: postman-the-things-network-applicationupstorage-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ApplicationWebhookRegistry API
  slug: postman-the-things-network-applicationwebhookregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs As API
  slug: postman-the-things-network-as-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs AsEndDeviceBatchRegistry API
  slug: postman-the-things-network-asenddevicebatchregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs AsEndDeviceRegistry API
  slug: postman-the-things-network-asenddeviceregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ClientAccess API
  slug: postman-the-things-network-clientaccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ClientRegistry API
  slug: postman-the-things-network-clientregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Configuration API
  slug: postman-the-things-network-configuration-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ContactInfoRegistry API
  slug: postman-the-things-network-contactinforegistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs DeviceRepository API
  slug: postman-the-things-network-devicerepository-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EmailValidationRegistry API
  slug: postman-the-things-network-emailvalidationregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceBatchClaimingServer API
  slug: postman-the-things-network-enddevicebatchclaimingserver-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceBatchRegistry API
  slug: postman-the-things-network-enddevicebatchregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceClaimingServer API
  slug: postman-the-things-network-enddeviceclaimingserver-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceQRCodeGenerator API
  slug: postman-the-things-network-enddeviceqrcodegenerator-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceRegistry API
  slug: postman-the-things-network-enddeviceregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceRegistrySearch API
  slug: postman-the-things-network-enddeviceregistrysearch-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EndDeviceTemplateConverter API
  slug: postman-the-things-network-enddevicetemplateconverter-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EntityAccess API
  slug: postman-the-things-network-entityaccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs EntityRegistrySearch API
  slug: postman-the-things-network-entityregistrysearch-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Events API
  slug: postman-the-things-network-events-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayAccess API
  slug: postman-the-things-network-gatewayaccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayBatchAccess API
  slug: postman-the-things-network-gatewaybatchaccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayBatchRegistry API
  slug: postman-the-things-network-gatewaybatchregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayClaimingServer API
  slug: postman-the-things-network-gatewayclaimingserver-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayConfigurationService API
  slug: postman-the-things-network-gatewayconfigurationservice-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayQRCodeGenerator API
  slug: postman-the-things-network-gatewayqrcodegenerator-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GatewayRegistry API
  slug: postman-the-things-network-gatewayregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Gs API
  slug: postman-the-things-network-gs-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs GtwGs API
  slug: postman-the-things-network-gtwgs-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Is API
  slug: postman-the-things-network-is-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Js API
  slug: postman-the-things-network-js-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs JsEndDeviceBatchRegistry API
  slug: postman-the-things-network-jsenddevicebatchregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs JsEndDeviceRegistry API
  slug: postman-the-things-network-jsenddeviceregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ManagedGatewayConfigurationService API
  slug: postman-the-things-network-managedgatewayconfigurationservice-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ManagedGatewayEthernetProfileConfigurationService API
  slug: postman-the-things-network-managedgatewayethernetprofileconfigurationservice-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs ManagedGatewayWiFiProfileConfigurationService API
  slug: postman-the-things-network-managedgatewaywifiprofileconfigurationservice-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs NotificationService API
  slug: postman-the-things-network-notificationservice-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Ns API
  slug: postman-the-things-network-ns-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs NsEndDeviceBatchRegistry API
  slug: postman-the-things-network-nsenddevicebatchregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs NsEndDeviceRegistry API
  slug: postman-the-things-network-nsenddeviceregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs NsMACSettingsProfileRegistry API
  slug: postman-the-things-network-nsmacsettingsprofileregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs NsRelayConfigurationService API
  slug: postman-the-things-network-nsrelayconfigurationservice-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs OAuthAuthorizationRegistry API
  slug: postman-the-things-network-oauthauthorizationregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs OrganizationAccess API
  slug: postman-the-things-network-organizationaccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs OrganizationRegistry API
  slug: postman-the-things-network-organizationregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs Pba API
  slug: postman-the-things-network-pba-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs UserAccess API
  slug: postman-the-things-network-useraccess-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs UserBookmarkRegistry API
  slug: postman-the-things-network-userbookmarkregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs UserInvitationRegistry API
  slug: postman-the-things-network-userinvitationregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs UserRegistry API
  slug: postman-the-things-network-userregistry-api
- collection_type: postman
  name: The Things Stack — Application Server AppAs UserSessionRegistry API
  slug: postman-the-things-network-usersessionregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs API
  slug: open-the-things-network-appas-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationAccess API
  slug: open-the-things-network-applicationaccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationActivationSettingRegistry API
  slug: open-the-things-network-applicationactivationsettingregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationPackageRegistry API
  slug: open-the-things-network-applicationpackageregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationPubSubRegistry API
  slug: open-the-things-network-applicationpubsubregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationRegistry API
  slug: open-the-things-network-applicationregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationUpStorage API
  slug: open-the-things-network-applicationupstorage-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ApplicationWebhookRegistry API
  slug: open-the-things-network-applicationwebhookregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs As API
  slug: open-the-things-network-as-api
- collection_type: open
  name: The Things Stack — Application Server AppAs AsEndDeviceBatchRegistry API
  slug: open-the-things-network-asenddevicebatchregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs AsEndDeviceRegistry API
  slug: open-the-things-network-asenddeviceregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ClientAccess API
  slug: open-the-things-network-clientaccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ClientRegistry API
  slug: open-the-things-network-clientregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Configuration API
  slug: open-the-things-network-configuration-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ContactInfoRegistry API
  slug: open-the-things-network-contactinforegistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs DeviceRepository API
  slug: open-the-things-network-devicerepository-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EmailValidationRegistry API
  slug: open-the-things-network-emailvalidationregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceBatchClaimingServer API
  slug: open-the-things-network-enddevicebatchclaimingserver-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceBatchRegistry API
  slug: open-the-things-network-enddevicebatchregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceClaimingServer API
  slug: open-the-things-network-enddeviceclaimingserver-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceQRCodeGenerator API
  slug: open-the-things-network-enddeviceqrcodegenerator-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceRegistry API
  slug: open-the-things-network-enddeviceregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceRegistrySearch API
  slug: open-the-things-network-enddeviceregistrysearch-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EndDeviceTemplateConverter API
  slug: open-the-things-network-enddevicetemplateconverter-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EntityAccess API
  slug: open-the-things-network-entityaccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs EntityRegistrySearch API
  slug: open-the-things-network-entityregistrysearch-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Events API
  slug: open-the-things-network-events-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayAccess API
  slug: open-the-things-network-gatewayaccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayBatchAccess API
  slug: open-the-things-network-gatewaybatchaccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayBatchRegistry API
  slug: open-the-things-network-gatewaybatchregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayClaimingServer API
  slug: open-the-things-network-gatewayclaimingserver-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayConfigurationService API
  slug: open-the-things-network-gatewayconfigurationservice-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayQRCodeGenerator API
  slug: open-the-things-network-gatewayqrcodegenerator-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GatewayRegistry API
  slug: open-the-things-network-gatewayregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Gs API
  slug: open-the-things-network-gs-api
- collection_type: open
  name: The Things Stack — Application Server AppAs GtwGs API
  slug: open-the-things-network-gtwgs-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Is API
  slug: open-the-things-network-is-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Js API
  slug: open-the-things-network-js-api
- collection_type: open
  name: The Things Stack — Application Server AppAs JsEndDeviceBatchRegistry API
  slug: open-the-things-network-jsenddevicebatchregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs JsEndDeviceRegistry API
  slug: open-the-things-network-jsenddeviceregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ManagedGatewayConfigurationService API
  slug: open-the-things-network-managedgatewayconfigurationservice-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ManagedGatewayEthernetProfileConfigurationService API
  slug: open-the-things-network-managedgatewayethernetprofileconfigurationservice-api
- collection_type: open
  name: The Things Stack — Application Server AppAs ManagedGatewayWiFiProfileConfigurationService API
  slug: open-the-things-network-managedgatewaywifiprofileconfigurationservice-api
- collection_type: open
  name: The Things Stack — Application Server AppAs NotificationService API
  slug: open-the-things-network-notificationservice-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Ns API
  slug: open-the-things-network-ns-api
- collection_type: open
  name: The Things Stack — Application Server AppAs NsEndDeviceBatchRegistry API
  slug: open-the-things-network-nsenddevicebatchregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs NsEndDeviceRegistry API
  slug: open-the-things-network-nsenddeviceregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs NsMACSettingsProfileRegistry API
  slug: open-the-things-network-nsmacsettingsprofileregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs NsRelayConfigurationService API
  slug: open-the-things-network-nsrelayconfigurationservice-api
- collection_type: open
  name: The Things Stack — Application Server AppAs OAuthAuthorizationRegistry API
  slug: open-the-things-network-oauthauthorizationregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs OrganizationAccess API
  slug: open-the-things-network-organizationaccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs OrganizationRegistry API
  slug: open-the-things-network-organizationregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs Pba API
  slug: open-the-things-network-pba-api
- collection_type: open
  name: The Things Stack — Application Server AppAs UserAccess API
  slug: open-the-things-network-useraccess-api
- collection_type: open
  name: The Things Stack — Application Server AppAs UserBookmarkRegistry API
  slug: open-the-things-network-userbookmarkregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs UserInvitationRegistry API
  slug: open-the-things-network-userinvitationregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs UserRegistry API
  slug: open-the-things-network-userregistry-api
- collection_type: open
  name: The Things Stack — Application Server AppAs UserSessionRegistry API
  slug: open-the-things-network-usersessionregistry-api
- collection_type: open
  name: The Things Stack — Application Server
  slug: open-the-things-stack-application-server
- collection_type: open
  name: The Things Stack — End Device Registry
  slug: open-the-things-stack-end-device-registry
- collection_type: open
  name: The Things Stack — Events
  slug: open-the-things-stack-events
- collection_type: open
  name: The Things Stack — Gateway Server
  slug: open-the-things-stack-gateway-server
- collection_type: open
  name: The Things Stack — Identity Server
  slug: open-the-things-stack-identity-server
- collection_type: open
  name: The Things Stack — Integrations
  slug: open-the-things-stack-integrations
- collection_type: open
  name: The Things Stack — Join Server
  slug: open-the-things-stack-join-server
- collection_type: open
  name: The Things Stack — Network Server
  slug: open-the-things-stack-network-server
- collection_type: open
  name: The Things Stack — Packet Broker Agent
  slug: open-the-things-stack-packet-broker-agent
common:
- group: other
  href: https://artifacts.apis.io/the-things-network/capabilities/the-things-network-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/the-things-network-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.thethingsnetwork.org/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/the-things-network--the-things-stack/overview
- group: agent
  href: https://artifacts.apis.io/the-things-network/agentic-access/the-things-network-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/the-things-network-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/the-things-network/security/the-things-network-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-things-network-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/the-things-network/security/the-things-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-things-network-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/the-things-network/authentication/the-things-network-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-things-network-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.thethingsnetwork.org
- group: start
  title: ''
  type: Portal
  url: https://www.thethingsindustries.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/api/
- group: build
  title: ''
  type: CLI
  url: https://www.thethingsindustries.com/docs/ttn-lw-cli/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TheThingsNetwork/lorawan-stack
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/TheThingsNetwork/lorawan-stack/releases
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TheThingsNetwork
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TheThingsIndustries
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TheThingsNetwork/lorawan-devices
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TheThingsNetwork/lorawan-frequency-plans
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TheThingsNetwork/lorawan-webhook-templates
- group: build
  title: ''
  type: Tools
  url: https://github.com/TheThingsNetwork/lorawan-stack-migrate
- group: operate
  title: ''
  type: Community
  url: https://www.thethingsnetwork.org/forum/
- group: operate
  title: ''
  type: Community
  url: https://www.thethingsnetwork.org/community
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.thethings.network
- group: other
  title: ''
  type: Events
  url: https://www.thethingsindustries.com/docs/concepts/features/events/
- group: operate
  title: ''
  type: RateLimits
  url: https://www.thethingsindustries.com/docs/enterprise/management/rate-limiting/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/enterprise/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thethings.industries/
- group: commercial
  title: ''
  type: License
  url: https://github.com/TheThingsNetwork/lorawan-stack/blob/v3.36/LICENSE
- group: commercial
  title: ''
  type: Plans
  url: https://www.thethingsindustries.com/stack/plans/
- group: commercial
  href: https://artifacts.apis.io/the-things-network/plans/the-things-network-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-things-network-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/the-things-network/rate-limits/the-things-network-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/the-things-network-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/the-things-network/finops/the-things-network-finops.yml
  title: ''
  type: FinOps
  url: finops/the-things-network-finops.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/vocabulary/the-things-network-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/the-things-network-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/json-ld/the-things-network-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/the-things-network-context.jsonld
- group: design
  href: https://artifacts.apis.io/the-things-network/json-structure/the-things-network-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/the-things-network-structure.json
- group: design
  href: https://artifacts.apis.io/the-things-network/rules/the-things-network-rules.yml
  title: ''
  type: Spectral
  url: rules/the-things-network-rules.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-things-industries/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/thethingsntwrk
- group: other
  title: ''
  type: Standards
  url: https://www.lora-alliance.org/
- group: company
  title: ''
  type: Blog
  url: https://www.thethingsindustries.com/news/
- group: build
  href: https://artifacts.apis.io/the-things-network/packages/the-things-network-packages.yml
  title: ''
  type: Packages
  url: packages/the-things-network-packages.yml
- group: build
  href: https://artifacts.apis.io/the-things-network/packages/the-things-network-packages.yml
  title: ''
  type: SDKs
  url: packages/the-things-network-packages.yml
- group: agent
  href: https://artifacts.apis.io/the-things-network/llms/the-things-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-things-network-llms.txt
- group: design
  href: https://artifacts.apis.io/the-things-network/conformance/the-things-network-conformance.yml
  title: ''
  type: Conformance
  url: conformance/the-things-network-conformance.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/errors/the-things-network-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/the-things-network-problem-types.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/lifecycle/the-things-network-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/the-things-network-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/the-things-network/lifecycle/the-things-network-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/the-things-network-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/the-things-network/scopes/the-things-network-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/the-things-network-scopes.yml
- group: auth
  href: https://artifacts.apis.io/the-things-network/security/the-things-network-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/the-things-network-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/the-things-network/sandbox/the-things-network-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/the-things-network-sandbox.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/conventions/the-things-network-conventions.yml
  title: ''
  type: Conventions
  url: conventions/the-things-network-conventions.yml
- group: operate
  href: https://artifacts.apis.io/the-things-network/changelog/the-things-network-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/the-things-network-changelog.yml
- group: build
  href: https://artifacts.apis.io/the-things-network/cli/the-things-network-cli.yml
  title: ''
  type: CLI
  url: cli/the-things-network-cli.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/data-model/the-things-network-data-model.yml
  title: ''
  type: DataModel
  url: data-model/the-things-network-data-model.yml
- group: design
  href: https://artifacts.apis.io/the-things-network/asyncapi/the-things-network-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/the-things-network-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/the-things-network/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-identity-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-identity-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-application-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-application-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-end-device-registry-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-end-device-registry-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-gateway-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-gateway-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-integrations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-join-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-join-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-network-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-network-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/overlays/the-things-network-packet-broker-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-things-network-packet-broker-agent-overlay.yaml
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-applicationserver.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-applicationserver.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-configuration_services.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-configuration_services.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-deviceclaimingserver.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-deviceclaimingserver.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-devicerepository.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-devicerepository.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-error.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-error.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-events.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-events.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-gatewayserver.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-gatewayserver.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-identityserver.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-identityserver.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-joinserver.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-joinserver.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-networkserver.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-networkserver.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-notification_service.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-notification_service.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-oauth_services.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-oauth_services.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-packetbrokeragent.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-packetbrokeragent.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-qrcodegenerator.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-qrcodegenerator.proto
- group: other
  href: https://artifacts.apis.io/the-things-network/grpc/the-things-network-rights.proto
  title: ''
  type: Protobuf
  url: grpc/the-things-network-rights.proto
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.thethingsindustries.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.thethingsindustries.com/docs/api/reference/
- group: docs
  title: ''
  type: APIReference
  url: https://www.thethingsindustries.com/docs/api/reference/http/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.thethingsindustries.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.thethingsindustries.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheThingsNetwork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheThingsIndustries
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thethingsindustries.com/stack/plans/
- group: start
  title: ''
  type: SignUp
  url: https://eu1.cloud.thethings.network/oauth/register
- group: start
  title: ''
  type: Login
  url: https://console.cloud.thethings.network
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thethingsindustries.com/document/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thethingsindustries.com/document/privacypolicy/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/api/concepts/auth/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/api/concepts/pagination/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/api/concepts/errors/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/concepts/advanced/purge/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/concepts/ttn/addresses/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/integrations/webhooks/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thethingsindustries.com/docs/integrations/other-integrations/mqtt/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.thethingsindustries.com/docs/whats-new/
created: '2026-05-25'
description: The Things Network (TTN) is a free, community-operated global LoRaWAN network with over 280,000 members and 21,000 gateways across 153 countries. It runs on The Things Stack, the open-source (Apache-2.0) LoRaWAN Network Server developed and maintained by The Things Industries. The Things Stack v3 implements the full LoRaWAN Network Reference Model — Identity Server, Application Server, Network Server, Gateway Server, Join Server, Device Repository, Packet Broker Agent — and exposes a unified HTTP REST and gRPC API plus MQTT, webhooks, and Pub/Sub integrations. The same software powers self-hosted deployments, the free The Things Network community network, The Things Stack Cloud (Discovery, Standard, Plus tiers), and The Things Stack Enterprise.
examples:
- key_count: 2
  name: The Things Stack End Device Create Example
  slug: the-things-stack-end-device-create-example
- key_count: 2
  name: The Things Stack Gateway Create Example
  slug: the-things-stack-gateway-create-example
- key_count: 4
  name: The Things Stack Uplink Message Example
  slug: the-things-stack-uplink-message-example
- key_count: 2
  name: The Things Stack Webhook Create Example
  slug: the-things-stack-webhook-create-example
finops:
- has_sources: true
  method: derived
  name: The Things Network Finops
  primary_unit: subscription
  service_category: ''
  slug: the-things-network-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-things-network.png
json_schemas:
- name: v3APIKey
  property_count: 7
  slug: the-things-stack-api-key
- name: v3ApplicationIdentifiers
  property_count: 1
  slug: the-things-stack-application-identifiers
- name: v3ApplicationPubSub
  property_count: 21
  slug: the-things-stack-application-pubsub
- name: v3ApplicationUp
  property_count: 15
  slug: the-things-stack-application-up
- name: v3ApplicationWebhook
  property_count: 23
  slug: the-things-stack-application-webhook
- name: lorawanv3DownlinkMessage
  property_count: 7
  slug: the-things-stack-downlink-message
- name: v3EndDevice
  property_count: 54
  slug: the-things-stack-end-device
- name: v3Gateway
  property_count: 31
  slug: the-things-stack-gateway
- name: v3GatewayStatus
  property_count: 7
  slug: the-things-stack-gateway-status
- name: v3Organization
  property_count: 11
  slug: the-things-stack-organization
- name: lorawanv3UplinkMessage
  property_count: 9
  slug: the-things-stack-uplink-message
- name: v3User
  property_count: 23
  slug: the-things-stack-user
json_structures:
- name: The Things Network Structure
  property_count: 0
  slug: the-things-network-structure
jsonld:
- class_count: 45
  name: The Things Network Context
  property_count: 3
  slug: the-things-network-context
layout: provider
modified: '2026-08-27'
name: The Things Network / The Things Stack
nav: Providers
network: true
overview: 'The Things Network / The Things Stack publishes 58 API contracts indexed on the [APIs.io](https://apis.io/) network, including AppAs API, ApplicationAccess API, ApplicationActivationSettingRegistry API, and 55 more. Tagged areas include LoRaWAN, IoT, Open Source, Network Server, and LPWAN.


  The The Things Network / The Things Stack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  The Things Network / The Things Stack''s developer surface includes authentication, developer portal, documentation, CLI, changelog, tooling, engineering blog, and 93 more developer resources.'
plans:
- name: The Things Network Plans Pricing
  plan_count: 6
  slug: the-things-network-plans-pricing
- name: The Things Network Price Estimates
  plan_count: 0
  slug: the-things-network-price-estimates
random_paper: 18
rate_limits:
- limit_count: 7
  name: The Things Network Rate Limits
  slug: the-things-network-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: The Things Network / The Things Stack — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: the-things-network-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: The Things Network / The Things Stack API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 2
    info: 0
    warn: 2
  slug: the-things-network-rules
scopes:
- name: The Things Network Scopes
  scope_count: 70
  slug: the-things-network-scopes
  summary_line: 70 scopes
score:
  band: exemplar
  composite: 78.1
  coverage:
    artifact_dirs: 38
    catalog_earned: 84.0
    catalog_earned_first_party: 12.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 84.2
    contract_governance: 45.5
    contract_quality: 67.7
    developer_ergonomics: 81.5
    discoverability: 78.6
    operational_transparency: 68.4
  previous_composite: 77.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/the-things-network/the-things-network-2026-06-20T195339.png
security:
- kind: authentication
  name: The Things Network Authentication
  slug: the-things-network-authentication
  summary_line: apiKey/oauth2/http · 5 schemes
- kind: domain-security
  name: The Things Network Domain Security
  slug: the-things-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: The Things Network Vulnerability Disclosure
  slug: the-things-network-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 4
skills:
- name: the-things-network-manage-access
  slug: the-things-network-manage-access
- name: the-things-network-register-end-device
  slug: the-things-network-register-end-device
- name: the-things-network-schedule-downlink
  slug: the-things-network-schedule-downlink
- name: the-things-network-stream-application-data
  slug: the-things-network-stream-application-data
slug: the-things-network
tags:
- LoRaWAN
- IoT
- Open Source
- Network Server
- LPWAN
- Telemetry
- Sensors
- Gateways
- Connectivity
- Apache 2.0
website: https://www.thethingsnetwork.org/
---
