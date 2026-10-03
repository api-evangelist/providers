---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 114
  human_in_the_loop: 93
  name: Drata Agentic Access
  operation_count: 238
  slug: drata-agentic-access
  summary_line: 238 operations · 114 acting · 93 human-in-the-loop
api_count: 3
apis:
- description: Drata's hosted remote Model Context Protocol server (Beta). MCP-compatible clients (Claude, ChatGPT, Cursor, Microsoft Copilot) connect over OAuth 2.1 with PKCE to regional endpoints for the US, EU an
  name: Drata MCP Server
  slug: mcp
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Account Members API from Drata — 3 operation(s) for account members.
  name: Drata Account Members API
  phrasing_intents:
  - id: searchForAccountMembers
    intent: Search account members
    question: Which accounts does a given member email belong to?
  - id: addMemberToAccount
    intent: Add members to an account
    question: How do I add people to a customer account?
  - id: deleteMemberFromAccount
    intent: Remove members from an account
    question: How do I take someone off a customer account?
  - id: accountMemberNotify
    intent: Email an invitation to account members
    question: What's the way to resend an invitation email to an account member?
  phrasing_ops: 4
  slug: drata-account-members-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Accounts API from Drata — 3 operation(s) for accounts.
  name: Drata Accounts API
  phrasing_intents:
  - id: getAccounts
    intent: Find trust accounts
    question: How do I find a customer account by its company domain?
  - id: addAccount
    intent: Create a trust account
    question: How do I add a new customer account to SafeBase?
  - id: getAccount
    intent: Get an account by ID
    question: Where can I see one account's details by its ID?
  - id: deleteAccount
    intent: Delete an account
    question: How do I delete an account we no longer need?
  - id: patchAccountsById
    intent: Change an existing account's access expiration
    question: Can I set an expiry date on an existing trust center account's access?
  - id: getAccountPageUrl
    intent: Get an account's private page URL
    question: Where do I find an account's private trust page link?
  phrasing_ops: 6
  slug: drata-accounts-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Assets let you build an inventory of policies, personnel and computer infrastructure. The [help docs](https://help.drata.com/en/collections/10485424) have more information.
  name: Drata Assets API
  phrasing_intents:
  - id: AssetsPublicV2Controller_listAssets
    intent: List assets
    question: Which assets are assigned to a given user?
  - id: AssetsPublicV2Controller_createAsset
    intent: Add an asset manually
    question: How do I manually add an asset to the inventory?
  - id: AssetsPublicV2Controller_getAsset
    intent: Get an asset
    question: What do we know about one specific asset?
  - id: AssetsPublicV2Controller_updateAsset
    intent: Update an asset
    question: How do I reassign an asset to a new owner?
  - id: AssetsPublicV2Controller_deleteAsset
    intent: Remove an asset
    question: Can removing a manually-added asset be undone?
  phrasing_ops: 5
  slug: drata-assets-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Audit Requests API from Drata — 2 operation(s) for audit requests.
  name: Drata Audit Requests API
  phrasing_intents:
  - id: AuditRequestsPublicV2Controller_listAuditRequests
    intent: List an audit's requests
    question: Which auditor requests are open on an audit?
  - id: AuditRequestsPublicV2Controller_getAuditRequest
    intent: Get an audit request
    question: What are the details of one auditor request?
  phrasing_ops: 2
  slug: drata-audit-requests-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Audits represent compliance assessments for a specific framework and time period. Audit Requests are evidence requests associated with an audit.
  name: Drata Audits API
  phrasing_intents:
  - id: AuditsPublicV2Controller_listAudits
    intent: List audits
    question: Which audits are running in my workspace?
  - id: AuditsPublicV2Controller_getAudit
    intent: Get an audit
    question: What are the details of one audit?
  phrasing_ops: 2
  slug: drata-audits-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Background checks verify a person’s identity, history, and qualifications to ensure they meet legal, regulatory, or policy standards. The [help docs](https://help.drata.com/en/articles/5833999-backgro
  name: Drata Background Checks API
  phrasing_intents:
  - id: BackgroundChecksPublicV2Controller_createBackgroundCheck
    intent: Record a manual background check
    question: How do I record a background check done outside Drata?
  phrasing_ops: 1
  slug: drata-background-checks-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Company tracks essential information about your organization. The [help docs](https://help.drata.com/en/articles/8283910) have more information on the purpose of each field.
  name: Drata Company API
  phrasing_intents:
  - id: CompaniesPublicV2Controller_getCompany
    intent: Get company settings
    question: What company details and settings does Drata hold for us?
  phrasing_ops: 1
  slug: drata-company-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Control Library is a catalog of pre-built Control Templates that can be provisioned into a Workspace. Each item carries default mappings to Tests, Policies, Evidence, and Framework Requirements.
  name: Drata Control Library API
  phrasing_intents:
  - id: ControlLibraryPublicV2Controller_listControlLibrary
    intent: Browse control library templates
    question: What control templates are available in the control library?
  - id: ControlLibraryPublicV2Controller_getControlLibraryItem
    intent: Get one control template
    question: What mappings come with a specific control template?
  - id: ControlLibraryPublicV2Controller_importControlLibrary
    intent: Import controls from library templates
    question: How do I add controls to my workspace from the control library?
  phrasing_ops: 3
  slug: drata-control-library-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Control Notes allow you to provide additional information about Controls.
  name: Drata Control Notes API
  phrasing_intents:
  - id: ControlNotesPublicV2Controller_getControlNotes
    intent: List notes on a control
    question: What notes have been left on a control?
  - id: ControlNotesPublicV2Controller_createControlNote
    intent: Add a note to a control
    question: How do I leave a comment on a control?
  - id: ControlNotesPublicV2Controller_getControlNote
    intent: Get one control note
    question: Can I read a specific note on a control?
  - id: ControlNotesPublicV2Controller_updateNote
    intent: Edit a control note
    question: Can I edit a note I left on a control?
  - id: ControlNotesPublicV2Controller_deleteNote
    intent: Delete a control note
    question: Can I remove a note from a control?
  phrasing_ops: 5
  slug: drata-control-notes-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Control Owners are the Users responsible for Controls. They ensure the right evidence is associated, that any automated tests are passing, and help prepare for an audit.
  name: Drata Control Owners API
  phrasing_intents:
  - id: ControlOwnersPublicV2Controller_getControlOwnersForAControl
    intent: List a control's owners
    question: Who owns a given control?
  - id: ControlOwnersPublicV2Controller_createControlOwner
    intent: Add an owner to a control
    question: How do I add one more owner to a control?
  - id: ControlOwnersPublicV2Controller_modifyControlOwners
    intent: Replace all owners of a control
    question: Can I set the full list of owners for a control in one go?
  - id: ControlOwnersPublicV2Controller_deleteControlOwner
    intent: Remove an owner from a control
    question: Can I take someone off as owner of a control?
  phrasing_ops: 4
  slug: drata-control-owners-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Controls are a strategic measure or safeguard that an organization puts in place to protect its assets and meet the requirements of specific compliance frameworks.
  name: Drata Controls API
  phrasing_intents:
  - id: ControlsPublicV2Controller_getControls
    intent: List controls in a workspace
    question: Which of our controls are not ready yet?
  - id: ControlsPublicV2Controller_createControl
    intent: Create a custom control
    question: How do I add our own custom control?
  - id: ControlsPublicV2Controller_getControlById
    intent: Get a control's full detail
    question: What is everything recorded about one control?
  - id: ControlsPublicV2Controller_modifyControl
    intent: Edit a control
    question: Can I rename a control or change its code?
  - id: ControlsPublicV2Controller_getMappedRequirements
    intent: List the requirements a control maps to
    question: Which framework requirements does a control satisfy?
  - id: ControlsPublicV2Controller_resetControlRequirementMappings
    intent: Reset controls to template mappings
    question: Can I undo our changes to control requirement mappings?
  - id: ControlsPublicV2Controller_performControlAction
    intent: Mark a control in or out of scope
    question: How do I mark a control as out of scope?
  - id: ControlsPublicV2Controller_compareControlRequirements
    intent: Compare control mappings with templates
    question: How do our control requirement mappings differ from the template defaults?
  phrasing_ops: 8
  slug: drata-controls-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Custom Connections allow users to integrate external systems with Drata. CUSTOM connections push arbitrary JSON evidence records using a user-defined schema. MDM and HRIS connections use a fixed commo
  name: Drata Custom Connections API
  phrasing_intents:
  - id: CustomConnectionsPublicV2Controller_listCustomConnections
    intent: List custom connections
    question: Which custom connections have we set up?
  - id: CustomConnectionsPublicV2Controller_createCustomConnection
    intent: Create a custom connection
    question: How do I create a custom connection for my own data source?
  - id: CustomConnectionsPublicV2Controller_getCustomConnection
    intent: Get a custom connection
    question: What are the settings of one custom connection?
  - id: CustomConnectionsPublicV2Controller_updateCustomConnection
    intent: Update a custom connection
    question: How do I rename a custom connection's alias?
  - id: CustomConnectionsPublicV2Controller_deleteCustomConnection
    intent: Delete a custom connection
    question: Is there a way to delete a custom connection we stopped using?
  phrasing_ops: 5
  slug: drata-custom-connections-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Custom Data Records are JSON evidence records pushed to a Custom Connection resource. Use the session management endpoints to batch upload records and track the status of bulk operations. You can crea
  name: Drata Custom Data Records API
  phrasing_intents:
  - id: CustomDataRecordsPublicV2Controller_listCustomDataRecords
    intent: List records for a custom connection resource
    question: What data records have we pushed to a custom connection?
  - id: CustomDataRecordsPublicV2Controller_createCustomData
    intent: Upsert custom data records
    question: How do I push my own data into a custom connection?
  - id: CustomDataRecordsPublicV2Controller_listSessions
    intent: List upload sessions for a resource
    question: Which batch upload sessions exist for a custom resource?
  - id: CustomDataRecordsPublicV2Controller_uploadSessionRecords
    intent: Upload a batch of records in a session
    question: Can I upload custom data in batches inside a session?
  - id: CustomDataRecordsPublicV2Controller_performSessionAction
    intent: Act on a custom data upload session
    question: How do I finish or close a custom data upload session?
  - id: CustomDataRecordsPublicV2Controller_updateCustomData
    intent: Update one custom data record
    question: Can I update a single custom data record by its ID?
  - id: CustomDataRecordsPublicV2Controller_deleteCustomData
    intent: Delete one custom data record
    question: Can I delete a single record from a custom connection?
  phrasing_ops: 7
  slug: drata-custom-data-records-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: 'Custom Field Definitions describe the schema - name, required, type, options, entity placements, and framework scope - of the Custom Fields configured on your account. Use them to discover the option '
  name: Drata Custom Field Definitions API
  phrasing_intents:
  - id: CustomFieldDefinitionsPublicV2Controller_listCustomFieldDefinitions
    intent: List custom field definitions
    question: What custom fields have we defined in Drata?
  - id: CustomFieldDefinitionsPublicV2Controller_getCustomFieldDefinition
    intent: Get one custom field definition
    question: Can I look up a custom field by its name instead of its ID?
  phrasing_ops: 2
  slug: drata-custom-field-definitions-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Device Documents allow you to provide manual evidence of Devices compliance. Using the Drata Agent or an MDM connection automatically provides this information.
  name: Drata Device Documents API
  phrasing_intents:
  - id: DeviceDocumentsPublicV2Controller_getDeviceDocuments
    intent: List a device's compliance documents
    question: What compliance documents are attached to a device?
  - id: DeviceDocumentsPublicV2Controller_uploadDocumentForDevice
    intent: Upload a device compliance document
    question: How do I upload a compliance document for a device?
  - id: DeviceDocumentsPublicV2Controller_getDeviceDocument
    intent: Get a device document
    question: Can I view one specific document attached to a device?
  - id: DeviceDocumentsPublicV2Controller_deleteDeviceDocument
    intent: Delete a device document
    question: How do I remove a document uploaded to a device?
  phrasing_ops: 4
  slug: drata-device-documents-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Devices are computers used by personnel. The data is provided by the Drata Agent or an MDM connection.
  name: Drata Devices API
  phrasing_intents:
  - id: DevicesPublicV2Controller_getDevices
    intent: List all devices across the company
    question: Which employee laptops and devices does Drata know about?
  - id: DevicesPublicV2Controller_getDevicesForPersonnel
    intent: List a person's devices
    question: What devices belong to one specific employee?
  - id: DevicesPublicV2Controller_getDevice
    intent: Get one device
    question: What compliance details are recorded for one device?
  - id: DevicesPublicV2Controller_getDevicesForCustomConnection
    intent: List devices reported by a connection
    question: Which devices came in through a particular connection?
  - id: DevicesPublicV2Controller_getDeviceApps
    intent: List apps installed on a device
    question: What applications are installed on an employee's device?
  - id: DevicesPublicV2Controller_createDeviceForCustomConnection
    intent: Create or update a device via custom connection
    question: How do I report a device from my own MDM into Drata?
  - id: DevicesPublicV2Controller_deleteDeviceFromCustomConnection
    intent: Delete a device from a custom connection
    question: Can I remove a device I pushed through a custom connection?
  phrasing_ops: 7
  slug: drata-devices-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Documents API from Drata — 4 operation(s) for documents.
  name: Drata Documents API
  phrasing_intents:
  - id: getDocument
    intent: Get a trust center document
    question: How do I fetch a trust center document using my own external ID?
  - id: deleteDocument
    intent: Delete a trust center document
    question: What's the way to delete a document from our trust center library?
  - id: patchDocument
    intent: Update a document's details
    question: How do I change when a trust center document expires?
  - id: getDocuments
    intent: List trust center documents
    question: Which documents are in my trust center library?
  - id: postDocumentUpload
    intent: Request a presigned document upload URL
    question: Where do I get a presigned URL to upload a document file?
  - id: putDocumentUpload
    intent: Create a document from an uploaded file
    question: How do I create a document after the file has been uploaded?
  - id: getDocumentTypes
    intent: List allowed document types
    question: What document types can I assign to a document?
  phrasing_ops: 7
  slug: drata-documents-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Events record the activity of User and automated processes in the Drata platform.
  name: Drata Events API
  phrasing_intents:
  - id: EventsPublicV2Controller_listEvents
    intent: List activity events
    question: What happened in our Drata account last week?
  - id: EventsPublicV2Controller_getEvent
    intent: Get one event
    question: What are the details of a specific event?
  - id: EventsPublicV2Controller_createEventDownloadJob
    intent: Start a PDF export of an event
    question: Can I export an event as a PDF?
  - id: EventsPublicV2Controller_getEventDownloadJobStatus
    intent: Check an event PDF export job
    question: Is my event PDF ready to download yet?
  phrasing_ops: 4
  slug: drata-events-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: 'Evidence items hold one or more artifacts, the files, URLs, or ticket references that demonstrate a control is operating. <br/>Use the evidence-files endpoint to pre-upload a file, then reference the '
  name: Drata Evidence API
  phrasing_intents:
  - id: EvidencePublicV2Controller_listEvidence
    intent: List evidence items in a workspace
    question: What evidence do we have collected for our compliance program?
  - id: EvidencePublicV2Controller_createEvidence
    intent: Create an evidence item with artifacts
    question: How do I add new evidence and attach files to it?
  - id: EvidencePublicV2Controller_uploadArtifactFile
    intent: Pre-upload a file for evidence
    question: Can I send an evidence file as Base64 instead of multipart?
  - id: EvidencePublicV2Controller_getEvidence
    intent: Get one evidence item
    question: What does a single evidence item contain?
  - id: EvidencePublicV2Controller_updateEvidence
    intent: Update an evidence item and its artifacts
    question: Can I replace or archive artifacts while editing an evidence item?
  - id: EvidencePublicV2Controller_deleteEvidence
    intent: Permanently delete an evidence item
    question: Can I remove an evidence item together with all its artifacts?
  - id: EvidencePublicV2Controller_listEvidenceArtifacts
    intent: List the artifacts on an evidence item
    question: Which files, URLs or tickets are attached to an evidence item?
  - id: EvidencePublicV2Controller_updateEvidenceArtifact
    intent: Rename an artifact or change its filed date
    question: Can I rename a single artifact without replacing its file?
  phrasing_ops: 10
  slug: drata-evidence-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Drata's Evidence Library serves as a repository for all the evidence you need to collect across your controls. The [help docs](https://help.drata.com/en/articles/8288579-evidence-library-overview) hav
  name: Drata Evidence Library API
  phrasing_intents:
  - id: EvidenceLibraryPublicV2Controller_listEvidenceLibrary
    intent: List evidence library items (legacy)
    question: What items are in our evidence library under the older endpoint?
  - id: EvidenceLibraryPublicV2Controller_createEvidenceLibrary
    intent: Create an evidence library item (legacy)
    question: Can I still add a single-file evidence library item the old way?
  - id: EvidenceLibraryPublicV2Controller_getEvidenceLibrary
    intent: Get an evidence library item (legacy)
    question: Can I fetch one evidence library item by its legacy ID?
  - id: EvidenceLibraryPublicV2Controller_updateEvidenceLibrary
    intent: Update an evidence library item (legacy)
    question: Can I change the renewal date on a legacy evidence library item?
  - id: EvidenceLibraryPublicV2Controller_deleteEvidenceLibrary
    intent: Delete an evidence library item
    question: Can I remove an item from the evidence library by its library ID?
  - id: EvidenceLibraryPublicV2Controller_getEvidenceLibraryVersion
    intent: Get a version of an evidence library item
    question: Can I see an earlier version of an evidence library item?
  phrasing_ops: 6
  slug: drata-evidence-library-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Frameworks are collections of controls that are used to assess compliance with specific standards or regulations. The [help docs](https://help.drata.com/en/articles/5329593-frameworks) have more infor
  name: Drata Frameworks API
  phrasing_intents:
  - id: FrameworksPublicV2Controller_getFrameworks
    intent: List compliance frameworks
    question: Which compliance frameworks are enabled in my workspace?
  - id: FrameworksPublicV2Controller_createFramework
    intent: Create a custom compliance framework
    question: How do I add my own custom compliance framework?
  - id: FrameworksPublicV2Controller_getFrameworkRequirementsLegacy
    intent: List requirements workspace-wide (legacy)
    question: Can I list requirements across all frameworks filtered by framework tag?
  - id: FrameworksPublicV2Controller_updateFrameworkRequirementLegacy
    intent: Set requirement custom fields (legacy)
    question: Is there an older endpoint to update requirement custom fields without the framework ID?
  - id: FrameworksPublicV2Controller_listFrameworkRequirements
    intent: List one framework's requirements
    question: What requirements make up one specific framework?
  - id: FrameworksPublicV2Controller_createFrameworkRequirements
    intent: Add requirements to a custom framework
    question: How do I add requirements to my custom framework in bulk?
  - id: FrameworksPublicV2Controller_listFrameworkRequirementControls
    intent: List controls mapped to a requirement
    question: Which controls are mapped to a specific framework requirement?
  - id: FrameworksPublicV2Controller_updateFrameworkRequirement
    intent: Update a custom framework requirement
    question: How do I change which controls map to a custom framework requirement?
  phrasing_ops: 9
  slug: drata-frameworks-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Groups are collections of Users that can be used to manage permissions and access to resources.
  name: Drata Groups API
  phrasing_intents:
  - id: GroupsPublicV2Controller_listGroups
    intent: List personnel groups
    question: Which teams or departments exist as personnel groups?
  phrasing_ops: 1
  slug: drata-groups-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: HR user identity records for a Custom HRIS connection. Use the batch upsert endpoint to submit employee records keyed by your own `identityId`, then use the update endpoint to reflect employment chang
  name: Drata HRIS User Identities API
  phrasing_intents:
  - id: CustomHrisUserIdentitiesPublicV2Controller_listCustomHrisUserIdentities
    intent: List HRIS user identities
    question: Which HR user identities are active on my custom HRIS connection?
  - id: CustomHrisUserIdentitiesPublicV2Controller_createCustomHrisUserIdentities
    intent: Create or update HRIS user identities
    question: How do I push employee records into a custom HRIS connection?
  - id: CustomHrisUserIdentitiesPublicV2Controller_getCustomHrisUserIdentity
    intent: Get an HRIS user identity
    question: Can I look up one HR identity using our own employee identityId?
  - id: CustomHrisUserIdentitiesPublicV2Controller_deleteCustomHrisUserIdentity
    intent: Delete an HRIS user identity
    question: How do I remove an employee identity from a custom HRIS connection?
  phrasing_ops: 4
  slug: drata-hris-user-identities-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Knowledge Base API from Drata — 3 operation(s) for knowledge base.
  name: Drata Knowledge Base API
  phrasing_intents:
  - id: searchKnowledgeBase
    intent: Search the knowledge base
    question: Do we already have an approved answer about data encryption?
  - id: addKbEntry
    intent: Add a knowledge base entry
    question: How do I add a new question and answer to our knowledge base?
  - id: updateKbEntry
    intent: Update a knowledge base entry
    question: Can I change the answer on an existing knowledge base entry?
  phrasing_ops: 3
  slug: drata-knowledge-base-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Monitoring Tests are compliance tests used to determine whether a person, system, process, or organization is adhering to standards set by compliance controls within a framework. The [help docs](https
  name: Drata Monitoring Tests API
  phrasing_intents:
  - id: MonitorsPublicV2Controller_listMonitors
    intent: List monitoring tests
    question: Which monitoring tests are currently failing in my workspace?
  - id: MonitorsPublicV2Controller_getMonitor
    intent: Get a monitoring test
    question: How do I look up a single monitoring test by its test ID?
  - id: MonitorsPublicV2Controller_updateMonitor
    intent: Rename, describe or disable a monitoring test
    question: Can I turn off a monitoring test we don't need?
  - id: MonitorsPublicV2Controller_listMonitorExclusions
    intent: List a monitoring test's exclusions
    question: Which resources are excluded from a monitoring test?
  - id: MonitorsPublicV2Controller_listMonitorTestFailures
    intent: List a monitoring test's failures
    question: Which resources are failing a particular monitoring test?
  - id: MonitorsPublicV2Controller_listMonitorTestPasses
    intent: List resources passing a monitoring test
    question: Which resources currently pass a given monitoring test?
  phrasing_ops: 6
  slug: drata-monitoring-tests-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Organization API from Drata — 4 operation(s) for organization.
  name: Drata Organization API
  phrasing_intents:
  - id: getOrganization
    intent: Get the current organization
    question: What organization is my SafeBase API key tied to?
  - id: getOrganizationNDASettings
    intent: Get the organization's NDA settings
    question: What NDA settings does our Trust Center use?
  - id: getOrganizationSettings
    intent: Get organization settings
    question: What general settings are configured for our organization?
  - id: getOrganizationMemberMe
    intent: Get my own organization member record
    question: Which member account am I authenticated as?
  phrasing_ops: 4
  slug: drata-organization-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Personnel are people who work for your organization. The [help docs](https://help.drata.com/en/collections/2653981) have more information.
  name: Drata Personnel API
  phrasing_intents:
  - id: PersonnelPublicV2Controller_listPersonnel
    intent: List personnel records
    question: Which employees on our personnel roster are out of compliance right now?
  - id: PersonnelPublicV2Controller_searchPersonnelAcrossWorkspaces
    intent: Search personnel across all workspaces
    question: How do I find a person by name or email across every workspace I can access?
  - id: PersonnelPublicV2Controller_searchPersonnel
    intent: Search personnel within one workspace
    question: Can I search the people in a single workspace by first name prefix?
  - id: PersonnelPublicV2Controller_getPerson
    intent: Get one person's personnel record
    question: How do I pull up a single employee's personnel record using their email?
  - id: PersonnelPublicV2Controller_modifyPerson
    intent: Update a person's employment details
    question: How do I record the separation date for someone who left the company?
  - id: PersonnelPublicV2Controller_performPersonnelAction
    intent: Reset personnel IdP/HRIS sync
    question: How can I restore automatic identity provider updates after editing people manually?
  - id: ScopedPersonnelGroupsPublicV2Controller_listScopedPersonnelGroups
    intent: List groups in a workspace's personnel scope
    question: Which personnel groups are currently in scope for a workspace?
  - id: ScopedPersonnelGroupsPublicV2Controller_addScopedPersonnelGroup
    intent: Add a group to a workspace's personnel scope
    question: How do I add one more team to a workspace's personnel scope?
  phrasing_ops: 11
  slug: drata-personnel-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: 'A policy is a document that outlines an organization’s commitment to following standards relevant to its operations. The [help docs](https://help.drata.com/en/articles/9202419-policy-center-overview) '
  name: Drata Policies API
  phrasing_intents:
  - id: PoliciesPublicV2Controller_listPolicies
    intent: List published policies
    question: Which published policies does our Drata account have?
  - id: PoliciesPublicV2Controller_createPolicy
    intent: Create a new policy with a draft version
    question: How do I add a brand new security policy with its first draft?
  - id: PoliciesPublicV2Controller_listPolicyVersions
    intent: List the versions of a policy
    question: What versions exist for one of our policies?
  - id: PoliciesPublicV2Controller_createPolicyVersion
    intent: Create a new version of a policy
    question: How do I publish a revised version of an existing policy?
  - id: PoliciesPublicV2Controller_getPolicy
    intent: Get one published policy
    question: What are the details of a specific published policy?
  - id: PoliciesPublicV2Controller_modifyPolicy
    intent: Edit a policy's settings
    question: Can I change a policy's renewal date or renewal schedule?
  - id: PoliciesPublicV2Controller_assignPolicyOwner
    intent: Change who owns a policy
    question: Can I hand ownership of a policy to another person?
  - id: PoliciesPublicV2Controller_getApprovalConfiguration
    intent: Get a policy's approval workflow
    question: Which review groups have to approve this policy, and in what order?
  phrasing_ops: 14
  slug: drata-policies-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Policy Languages let an organization publish the same Policy Version in several languages. Settings endpoints expose the languages an organization has configured and which one is the default; Policy L
  name: Drata Policy Languages API
  phrasing_intents:
  - id: PolicyLanguagesPublicV2Controller_listPolicyLanguageSettings
    intent: List configured policy languages
    question: Which languages are our policies configured for?
  - id: PolicyLanguagesPublicV2Controller_listPolicyLanguageVersions
    intent: List policy version language variants
    question: Which translations exist for a given policy version?
  - id: PolicyLanguagesPublicV2Controller_getPolicyLanguageVersion
    intent: Get a policy language variant
    question: Can I fetch one translated variant of a policy version by its ID?
  phrasing_ops: 3
  slug: drata-policy-languages-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Portals API from Drata — 1 operation(s) for portals.
  name: Drata Portals API
  phrasing_intents:
  - id: getPortal
    intent: List the products in the Trust Center portal
    question: Which products make up our Trust Center portal?
  phrasing_ops: 1
  slug: drata-portals-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Procurement Connection Mappings API from Drata — 1 operation(s) for procurement connection mappings.
  name: Drata Procurement Connection Mappings API
  phrasing_intents:
  - id: ProcurementConnectionMappingsPublicV2Controller_getVendorMapping
    intent: Get a procurement vendor mapping
    question: How is our Ironclad or Tropic data mapped into vendors?
  - id: ProcurementConnectionMappingsPublicV2Controller_updateVendorMapping
    intent: Update a procurement vendor mapping
    question: Can I change how procurement records map to vendor fields?
  phrasing_ops: 2
  slug: drata-procurement-connection-mappings-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Products API from Drata — 1 operation(s) for products.
  name: Drata Products API
  phrasing_intents:
  - id: getProducts
    intent: List products
    question: Which products are set up in our trust center?
  phrasing_ops: 1
  slug: drata-products-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Questionnaires API from Drata — 2 operation(s) for questionnaires.
  name: Drata Questionnaires API
  phrasing_intents:
  - id: submitQnrFile
    intent: Upload a security questionnaire
    question: How do I submit a customer's security questionnaire to SafeBase?
  - id: getCompletedQuestionnaireUrl
    intent: Get a download link for a completed questionnaire
    question: Where can I download a questionnaire once it's completed?
  phrasing_ops: 2
  slug: drata-questionnaires-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Requests API from Drata — 3 operation(s) for requests.
  name: Drata Requests API
  phrasing_intents:
  - id: getRequests
    intent: List Trust Center access requests
    question: Who is waiting for access to our Trust Center?
  - id: approveRequest
    intent: Approve an access request
    question: How do I grant someone's request to view our Trust Center?
  - id: declineRequest
    intent: Decline an access request
    question: Can I turn down a Trust Center access request with a message?
  phrasing_ops: 3
  slug: drata-requests-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Risk Documents are supporting documents, evidence, or other materials that are associated with a risk.
  name: Drata Risk Documents API
  phrasing_intents:
  - id: RiskDocumentsPublicV2Controller_listRiskDocuments
    intent: List documents on a risk
    question: Which documents are attached to a specific risk?
  - id: RiskDocumentsPublicV2Controller_uploadRiskDocuments
    intent: Upload documents to a risk
    question: How do I attach supporting files to a risk?
  - id: RiskDocumentsPublicV2Controller_getRiskDocument
    intent: Get a risk document
    question: Can I retrieve one specific document attached to a risk?
  - id: RiskDocumentsPublicV2Controller_deleteRiskDocument
    intent: Delete a risk document
    question: How do I remove a document that was attached to the wrong risk?
  phrasing_ops: 4
  slug: drata-risk-documents-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Risk Library is a collection of Risks that can be copied into a Risk Register. The [help docs](https://help.drata.com/en/articles/13371089-drata-s-risk-library-new-experience) have more informatio
  name: Drata Risk Library API
  phrasing_intents:
  - id: RiskLibraryPublicV2Controller_listRiskLibrary
    intent: Browse the risk library
    question: Which prebuilt risks are in the risk library?
  - id: RiskLibraryPublicV2Controller_getRiskLibraryItem
    intent: Get a risk library item
    question: What are the details of one risk template in the library?
  - id: RiskLibraryPublicV2Controller_copyRiskLibrary
    intent: Copy library risks into a register
    question: How do I copy risks from the library into my risk register?
  phrasing_ops: 3
  slug: drata-risk-library-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Risk Notes allow you to provide additional information about Risks.
  name: Drata Risk Notes API
  phrasing_intents:
  - id: RiskNotesPublicV2Controller_getRiskNotes
    intent: List notes on a risk
    question: What notes have been recorded on a risk?
  - id: RiskNotesPublicV2Controller_createRiskNote
    intent: Add a note to a risk
    question: How do I add a comment to a risk?
  - id: RiskNotesPublicV2Controller_getRiskNote
    intent: Get one risk note
    question: Can I read a specific note on a risk?
  - id: RiskNotesPublicV2Controller_updateRiskNote
    intent: Edit a risk note
    question: Can I edit a note I left on a risk?
  - id: RiskNotesPublicV2Controller_deleteRiskNote
    intent: Delete a risk note
    question: Can I remove a note from a risk?
  phrasing_ops: 5
  slug: drata-risk-notes-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Risk Registers are a collection of Risks. They are used to organize and manage Risks.
  name: Drata Risk Registers API
  phrasing_intents:
  - id: RiskRegisterPublicV2Controller_listRiskRegisters
    intent: List risk registers
    question: Which risk registers exist in our account?
  - id: RiskRegisterPublicV2Controller_createRiskRegister
    intent: Create a risk register
    question: How do I create a new risk register?
  - id: RiskRegisterPublicV2Controller_getRiskRegister
    intent: Get a risk register
    question: What are the details of one risk register?
  - id: RiskRegisterPublicV2Controller_updateRiskRegister
    intent: Update a risk register
    question: How do I rename a risk register?
  - id: RiskRegisterPublicV2Controller_deleteRiskRegister
    intent: Delete a risk register
    question: Can I delete a risk register we no longer use?
  phrasing_ops: 5
  slug: drata-risk-registers-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Risks are potential events that could impact the security, reputation, and financial health of a company.
  name: Drata Risks API
  phrasing_intents:
  - id: RiskManagementPublicV2Controller_listRisks
    intent: List risks in a register
    question: Which risks in a register are currently active?
  - id: RiskManagementPublicV2Controller_createRisk
    intent: Create a risk in a register
    question: How do I add a custom risk to a risk register?
  - id: RiskManagementPublicV2Controller_searchRisks
    intent: Search risks within one register
    question: Can I full-text search the risks inside one register?
  - id: RiskManagementPublicV2Controller_searchRisksAcrossRegisters
    intent: Search risks across all registers
    question: How do I search risks across every risk register I can access?
  - id: RiskManagementPublicV2Controller_getRisk
    intent: Get a risk's details
    question: What are the details of risk RISK-001?
  - id: RiskManagementPublicV2Controller_updateRisk
    intent: Update a risk
    question: How do I change a risk's treatment plan?
  - id: RiskManagementPublicV2Controller_deleteRisk
    intent: Delete a risk
    question: How do I delete a risk that was logged by mistake?
  - id: RiskManagementPublicV2Controller_getRiskInsights
    intent: Get risk register insights
    question: What does the risk heatmap look like for a register?
  phrasing_ops: 8
  slug: drata-risks-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Tags API from Drata — 1 operation(s) for tags.
  name: Drata Tags API
  phrasing_intents:
  - id: getTags
    intent: List tags
    question: What tags are available for labelling content?
  phrasing_ops: 1
  slug: drata-tags-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Tasks are individual units of work that can be assigned to users.
  name: Drata Tasks API
  phrasing_intents:
  - id: TasksPublicV2Controller_listTasks
    intent: List tasks in a workspace
    question: Which compliance tasks are assigned to a given person?
  - id: TasksPublicV2Controller_createTask
    intent: Create a task
    question: How do I create a follow-up task with a due date?
  - id: TasksPublicV2Controller_getTask
    intent: Get one task
    question: What are the details of a specific task?
  - id: TasksPublicV2Controller_updateTask
    intent: Update a task
    question: Can I push back a task's due date?
  - id: TasksPublicV2Controller_performTaskAction
    intent: Complete or reopen a task
    question: How do I mark a task as done?
  - id: UpcomingTasksPublicV2Controller_listUpcomingTasks
    intent: List upcoming Drata-assigned tasks
    question: What policy renewals and vendor reviews are coming due?
  phrasing_ops: 6
  slug: drata-tasks-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: The Trust Center Updates API from Drata — 4 operation(s) for trust center updates.
  name: Drata Trust Center Updates API
  phrasing_intents:
  - id: createTopic
    intent: Create a Trust Center update topic
    question: How do I start a new topic for Trust Center announcements?
  - id: listTopics
    intent: List Trust Center update topics
    question: What topics are set up for Trust Center updates?
  - id: updateTrustCenterTopic
    intent: Update a Trust Center topic
    question: Can I change the subject or visibility of a Trust Center topic?
  - id: deleteTrustCenterTopic
    intent: Delete a Trust Center topic
    question: Can I remove a Trust Center topic we no longer use?
  - id: getTrustCenterTopic
    intent: Get a Trust Center topic
    question: What are the details of one Trust Center topic?
  - id: createTrustCenterUpdate
    intent: Post an update to a Trust Center topic
    question: How do I post a new security update to our Trust Center?
  - id: getTrustCenterUpdateById
    intent: Get one Trust Center update
    question: Can I retrieve a specific Trust Center update we posted?
  - id: updateTrustCenterUpdate
    intent: Edit the message of a Trust Center update
    question: Can I fix a typo in a Trust Center update after posting it?
  phrasing_ops: 9
  slug: drata-trust-center-updates-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Uploads let you request a pre-signed S3 URL to upload a file for a given purpose (e.g. Evidence), then reference the resulting object key when creating the associated resource.
  name: Drata Uploads API
  phrasing_intents:
  - id: UploadsPublicV2Controller_requestUploadUrl
    intent: Request a presigned upload URL
    question: How do I get a presigned URL to upload evidence files?
  phrasing_ops: 1
  slug: drata-uploads-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: User Documents allow you to provide manual evidence of User and Personnel compliance.
  name: Drata User Documents API
  phrasing_intents:
  - id: UserDocumentsPublicV2Controller_listUserDocuments
    intent: List a user's documents
    question: What documents has an employee uploaded, like training certificates?
  - id: UserDocumentsPublicV2Controller_uploadUserDocument
    intent: Upload a document for a user
    question: How do I upload proof that an employee finished security training?
  - id: UserDocumentsPublicV2Controller_getUserDocument
    intent: Get one user document
    question: Can I retrieve a specific document a user uploaded?
  - id: UserDocumentsPublicV2Controller_deleteUserDocument
    intent: Delete a user document
    question: Can I remove a document uploaded for an employee?
  phrasing_ops: 4
  slug: drata-user-documents-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: User's Assigned Policies track the acknowledgement of Policy Versions by Users.
  name: Drata User's Assigned Policies API
  phrasing_intents:
  - id: UsersPoliciesPublicV2Controller_getPolicyVersionsForUser
    intent: List a user's assigned policies
    question: Which policies has a given employee been assigned?
  - id: UsersPoliciesPublicV2Controller_acceptUserPolicyVersion
    intent: Record a user's policy acknowledgment
    question: How do I mark that an employee accepted a policy?
  phrasing_ops: 2
  slug: drata-user-s-assigned-policies-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: '**Users** are are people with access to the Drata platform. **Roles** grant permissions to Users. The [help docs](https://help.drata.com/en/collections/5993507) have more information on the default Ro'
  name: Drata Users and Roles API
  phrasing_intents:
  - id: RolesPublicV2Controller_listRoles
    intent: List roles
    question: What roles are defined in our Drata account?
  - id: RolesPublicV2Controller_getRole
    intent: Get one role
    question: What does a particular role include?
  - id: RolesPublicV2Controller_listUsers
    intent: List users who have a role
    question: Who has the admin role?
  - id: UsersPublicV2Controller_listUsers
    intent: List users
    question: Which users are in our Drata account?
  - id: UsersPublicV2Controller_getUser
    intent: Get one user
    question: What is recorded about a specific user?
  phrasing_ops: 5
  slug: drata-users-and-roles-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Vendor Documents provide compliance-related documentation, such as bridge letters, questionnaires, and SOC reports.
  name: Drata Vendor Documents API
  phrasing_intents:
  - id: VendorDocumentsPublicV2Controller_getVendorDocuments
    intent: List a vendor's documents
    question: What documents do we have on file for a vendor, like a SOC 2 report?
  - id: VendorDocumentsPublicV2Controller_uploadVendorDocument
    intent: Upload a vendor document
    question: How do I upload a vendor's security report?
  - id: VendorDocumentsPublicV2Controller_getVendorDocument
    intent: Get one vendor document
    question: Can I retrieve a single document we stored for a vendor?
  phrasing_ops: 3
  slug: drata-vendor-documents-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Vendor Security Reviews track the status of security reviews for Vendors. You can create a security review, upload questionnaires, and track the progress of the review. The [help docs](https://help.dr
  name: Drata Vendor Security Reviews API
  phrasing_intents:
  - id: VendorSecurityReviewsPublicV2Controller_listVendorSecurityReviews
    intent: List a vendor's security reviews
    question: What security reviews have been done for one particular vendor?
  - id: VendorSecurityReviewsPublicV2Controller_createVendorSecurityReview
    intent: Start a vendor security review
    question: How do I open a new security review for a vendor with a deadline?
  - id: VendorSecurityReviewsPublicV2Controller_createVendorSecurityReviewWithFile
    intent: Create a vendor review with an attached file
    question: Can I create a vendor security review and upload its report file in one step?
  - id: VendorSecurityReviewsPublicV2Controller_listVendorSecurityReviewsAcrossVendors
    intent: List security reviews across all vendors
    question: Where can I see every vendor security review in the account at once?
  - id: VendorSecurityReviewsPublicV2Controller_getVendorSecurityReview
    intent: Get one vendor security review
    question: How do I see the SOC report form data for one vendor review?
  - id: VendorSecurityReviewsPublicV2Controller_updateVendorSecurityReview
    intent: Update a vendor security review
    question: Can I rename a vendor security review after it's created?
  - id: VendorSecurityReviewsPublicV2Controller_sendSecurityQuestionnaire
    intent: Upload a questionnaire to a vendor
    question: Can I upload a completed security questionnaire at the vendor level, not tied to a review?
  - id: VendorSecurityReviewsPublicV2Controller_listVendorSecurityReviewSecurityQuestionnaires
    intent: List questionnaires on a security review
    question: Which questionnaires belong to one vendor security review?
  phrasing_ops: 11
  slug: drata-vendor-security-reviews-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Vendor Types are user-defined classifications used to categorize and organize vendors.
  name: Drata Vendor Types API
  phrasing_intents:
  - id: VendorTypesPublicV2Controller_listVendorTypes
    intent: List vendor types
    question: Which vendor types are configured for our account?
  - id: VendorTypesPublicV2Controller_createVendorType
    intent: Create a vendor type
    question: How do I add a new vendor type?
  - id: VendorTypesPublicV2Controller_updateVendorType
    intent: Rename a vendor type
    question: How do I rename an existing vendor type?
  - id: VendorTypesPublicV2Controller_deleteVendorType
    intent: Delete a vendor type
    question: Can I delete a vendor type we no longer need?
  phrasing_ops: 4
  slug: drata-vendor-types-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Vendors are third-parties that your organization is working with. Drata allows you to track and review risks associated with these third-parties. The [help docs](https://help.drata.com/en/articles/967
  name: Drata Vendors API
  phrasing_intents:
  - id: VendorsPublicV2Controller_listVendors
    intent: List vendors
    question: Which of my vendors are rated high risk?
  - id: VendorsPublicV2Controller_createVendor
    intent: Add a vendor
    question: How do I add a new third-party vendor to my inventory?
  - id: VendorsPublicV2Controller_getVendorStats
    intent: Get vendor statistics
    question: What do my vendor counts look like broken down by scope?
  - id: VendorsPublicV2Controller_getVendor
    intent: Get a vendor's details
    question: What details do we have on file for a particular vendor?
  - id: VendorsPublicV2Controller_updateVendor
    intent: Update a vendor
    question: How do I change an existing vendor's risk level or renewal date?
  - id: VendorsPublicV2Controller_deleteVendor
    intent: Remove a vendor
    question: How do I remove a vendor we no longer use?
  - id: VendorsPublicV2Controller_listVendorQuestionnaires
    intent: List questionnaires sent to a vendor
    question: Which questionnaires have we sent to a vendor?
  - id: VendorsPublicV2Controller_sendQuestionnaireToVendor
    intent: Email a questionnaire to a vendor
    question: How do I email a security questionnaire to a vendor contact?
  phrasing_ops: 9
  slug: drata-vendors-api
- baseURL: https://public-api.drata.com/public/v2
  baseurl_source: declared
  description: Workspaces allow you to represent different products or business lines that have different compliance requirements. Each Workspace can have its own Frameworks and Controls. The [help docs](https://hel
  name: Drata Workspaces API
  phrasing_intents:
  - id: WorkspacesPublicV2Controller_listWorkspaces
    intent: List workspaces
    question: Which workspaces exist in our Drata account?
  phrasing_ops: 1
  slug: drata-workspaces-api
artifact_total: 62
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/capabilities/drata-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/drata-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/agentic-access/drata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drata-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/security/drata-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/drata-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/security/drata-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drata-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/security/drata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drata-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/authentication/drata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drata
- group: company
  title: ''
  type: Website
  url: https://drata.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.drata.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/plans/drata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drata-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/rate-limits/drata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drata-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/finops/drata-finops.yml
  title: ''
  type: FinOps
  url: finops/drata-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/mcp/drata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drata-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/mcp/drata-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/drata-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/scopes/drata-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/drata-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/well-known/drata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drata-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/conventions/drata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drata-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/errors/drata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drata-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/lifecycle/drata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drata-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/changelog/drata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/drata-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/conformance/drata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drata-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/data-model/drata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drata-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/packages/drata-packages.yml
  title: ''
  type: Packages
  url: packages/drata-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/llms/drata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drata-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/overlays/drata-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/drata-api-v2-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/examples/drata-examples.yml
  title: ''
  type: Examples
  url: examples/drata-examples.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.drata.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/security/drata-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/drata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.drata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.drata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.drata.com/openapi/reference/v2/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.drata.com/openapi/reference/v2/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.drata.com/developer-portal/v2/recipes/create-an-api-key/
- group: operate
  title: ''
  type: Support
  url: https://help.drata.com/
- group: company
  title: ''
  type: Blog
  url: https://drata.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://drata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://drata.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.drata.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drata.com/privacy
created: '2026-05-08'
description: Drata is a continuous security and compliance automation platform supporting SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, and more, with policies, evidence, and trust center. Drata exposes a public REST API plus the SafeBase Trust API (acquired) and a Custom Connections framework for evidence collection.
finops:
- name: Drata Finops
  service_category: GRC
  slug: drata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drata.png
layout: provider
mcp_servers:
- description: Drata's official hosted, remote Model Context Protocol server. It exposes Drata's live compliance, control, policy, monitoring-test, risk and workspace data to MCP-compatible clients (Claude, ChatGPT,
  name: Drata MCP Server
  slug: drata-mcp-server
modified: '2026-08-27'
name: Drata
nav: Providers
network: true
overview: 'Drata publishes 52 APIs on the [APIs.io](https://apis.io/) network, including Account Members API, Accounts API, Assets API, and 49 more. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Security.


  Drata''s developer surface includes authentication, changelog, code examples, documentation, API reference, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Drata Plans Pricing
  plan_count: 1
  slug: drata-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Drata Rate Limits
  slug: drata-rate-limits
scopes:
- name: Drata Scopes
  scope_count: 0
  slug: drata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 59.0
    catalog_earned_first_party: 16.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 89.5
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 58.9
    discoverability: 73.3
    operational_transparency: 65.8
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 52
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/screenshots/drata-2026-06-20T180244.png
security:
- kind: authentication
  name: Drata Authentication
  slug: drata-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Drata Domain Security
  slug: drata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Drata Vulnerability Disclosure
  slug: drata-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Drata Trust Center
  slug: drata-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: drata
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Security
- Risk Management
- Trust Center
- Audit
- Third-Party Risk Management
- Compliance Automation
website: https://drata.com/
---
