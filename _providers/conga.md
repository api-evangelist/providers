---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
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
  score: 48.7
  scored_at: '2026-11-06'
api_count: 31
apis:
- description: A hosted, remote Model Context Protocol server on every regional Conga Advantage Platform gateway. It answers MCP JSON-RPC over Streamable HTTP, rejects anonymous calls with an RFC 6750 bearer challen
  name: Conga Advantage Platform MCP Server
  slug: conga-advantage-platform-mcp-server
- description: A multi-tenant GraphQL API over the Conga Advantage Platform data core, with Relay-style connections, cursor pagination, SOQL-like where predicates and Server-Sent-Event subscriptions. Each tenant get
  name: Conga GraphQL API
  slug: conga-graphql-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Manages the complete lifecycle of your orders from initial confirmation through activation, modification, and cancellation.
  name: Conga 2. Order Actions API
  phrasing_intents:
  - id: postOrdersByIdAcceptChange
    intent: Accept the changes on an amended order
    question: How do I finalize the amendments I made to an order?
  - id: postOrdersByIdRevertChange
    intent: Discard the changes on an amended order
    question: Can I throw away an order amendment and go back to the original order?
  phrasing_ops: 2
  slug: conga-2-order-actions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Manages order line items represent each product, service, or subscription that a customer has purchased as part of an order.
  name: Conga 3. Order Line Items API
  phrasing_intents:
  - id: patchOrderByParentIdOrderlineitems
    intent: Update several order line items at once
    question: How can I change quantities on many lines of an order in one go?
  phrasing_ops: 1
  slug: conga-3-order-line-items-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Account API from Conga — 8 operation(s) for account.
  name: Conga Account API
  phrasing_intents:
  - id: getApiDataV1Account
    intent: List account records
    question: Which customer accounts are stored in the platform?
  - id: postApiDataV1Account
    intent: Create an account record
    question: How do I add a new customer account?
  - id: deleteApiDataV1AccountBulk
    intent: Delete many account records
    question: Can I delete a batch of accounts in one request?
  - id: patchApiDataV1AccountBulk
    intent: Upsert many account records
    question: How do I insert new accounts and update existing ones in a single call?
  - id: postApiDataV1AccountBulk
    intent: Create many account records
    question: Can I insert a list of new accounts at once?
  - id: putApiDataV1AccountBulk
    intent: Update many account records
    question: How do I update a batch of existing accounts in one call?
  - id: deleteApiDataV1AccountByExternalIdByExternalId
    intent: Delete an account by external ID
    question: How do I delete an account using its external ID?
  - id: getApiDataV1AccountByExternalIdByExternalId
    intent: Get an account by external ID
    question: How do I find an account using the ID from my CRM?
  phrasing_ops: 16
  slug: conga-account-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountAttachmentsBlacklist API from Conga — 1 operation(s) for accountattachmentsblacklist.
  name: Conga Account Attachments Blacklist API
  phrasing_intents:
  - id: AccountAttachmentsBlacklist_GetAccountAttachmentsBlacklist
    intent: List blocked attachment file types
    question: Which file types are signers blocked from uploading?
  phrasing_ops: 1
  slug: conga-accountattachmentsblacklist-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountAttachmentsWhitelist API from Conga — 1 operation(s) for accountattachmentswhitelist.
  name: Conga Account Attachments Whitelist API
  phrasing_intents:
  - id: AccountAttachmentsWhitelist_DeleteAccountAttachmentsWhitelist
    intent: Reset allowed attachment types to defaults
    question: Can I go back to the default allowed attachment types?
  - id: AccountAttachmentsWhitelist_GetAccountAttachmentsWhitelist
    intent: Get allowed attachment file types
    question: Which file types are signers allowed to attach during signing?
  - id: AccountAttachmentsWhitelist_UpdateAccountAttachmentsWhitelist
    intent: Replace the allowed attachment file types
    question: How do I let signers upload JPG and PDF attachments only?
  phrasing_ops: 3
  slug: conga-accountattachmentswhitelist-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountDesignerSettings API from Conga — 1 operation(s) for accountdesignersettings.
  name: Conga Account Designer Settings API
  phrasing_intents:
  - id: AccountDesignerSettings_DeleteAccountDesignerSettings
    intent: Reset Designer settings to defaults
    question: How do I reset Designer settings to their defaults?
  - id: AccountDesignerSettings_GetAccountDesignerSettings
    intent: Get account Designer settings
    question: What are my current Designer settings?
  - id: AccountDesignerSettings_UpdateAccountDesignerSettings
    intent: Update account Designer settings
    question: Can I stop senders from adding documents in the Designer?
  phrasing_ops: 3
  slug: conga-accountdesignersettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountEmailReminderSettings API from Conga — 1 operation(s) for accountemailremindersettings.
  name: Conga Account Email Reminder Settings API
  phrasing_intents:
  - id: AccountEmailReminderSettings_DeleteEmailReminderSettings
    intent: Reset account email reminder settings
    question: Can I clear custom reminder settings so no reminders go out?
  - id: AccountEmailReminderSettings_GetEmailReminderSettings
    intent: Get account email reminder settings
    question: What default email reminder schedule does my account use?
  - id: AccountEmailReminderSettings_UpdateEmailReminderSettings
    intent: Update account email reminder settings
    question: Can I change the account default for days before the first reminder?
  phrasing_ops: 3
  slug: conga-accountemailremindersettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountFeatureSettings API from Conga — 1 operation(s) for accountfeaturesettings.
  name: Conga Account Feature Settings API
  phrasing_intents:
  - id: AccountFeatureSettings_DeleteAccountFeatureSettings
    intent: Reset feature settings to defaults
    question: Can I undo all our customized feature settings at once?
  - id: AccountFeatureSettings_GetAccountFeatureSettings
    intent: Get the account's feature settings
    question: Which signing features are switched on for our account?
  - id: AccountFeatureSettings_PatchAccountFeatureSettings
    intent: Turn account features on or off
    question: How do I enable delegation for senders in our account?
  phrasing_ops: 3
  slug: conga-accountfeaturesettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountPackageSettings API from Conga — 1 operation(s) for accountpackagesettings.
  name: Conga Account Package Settings API
  phrasing_intents:
  - id: AccountPackageSettings_AddAccountPackageSettings
    intent: Update Backoffice package settings
    question: Can I hide the decline button for signers account-wide?
  - id: AccountPackageSettings_DeleteAccountPackageSettings
    intent: Reset Backoffice package settings
    question: How do I reset package settings back to defaults?
  - id: AccountPackageSettings_GetAccountPackageSettings
    intent: Get Backoffice package settings
    question: What are my account's Backoffice package settings?
  phrasing_ops: 3
  slug: conga-accountpackagesettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Accounts API from Conga — 4 operation(s) for accounts.
  name: Conga Accounts API
  phrasing_intents:
  - id: Accounts
    intent: Get the active account's price list
    question: Which price list applies to the active account?
  - id: Accounts_GetAccountUsage
    intent: Get e-signature usage for my account
    question: How many signing transactions has our account used?
  - id: postApiClmV1AccountsByAccountIdContractsHierarchyQuery
    intent: Query the contract hierarchy for an account
    question: How can I see every contract under an account arranged as a parent-child hierarchy?
  - id: postApiClmV1AccountsByAccountIdContractsByContractIdHierarchyQuery
    intent: Get the hierarchy below one contract of an account
    question: Which child agreements sit beneath a specific contract on an account?
  phrasing_ops: 4
  slug: conga-accounts-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountSigningLogos API from Conga — 1 operation(s) for accountsigninglogos.
  name: Conga Account Signing Logos API
  phrasing_intents:
  - id: AccountSigningLogos_CreateAccountSigningLogos
    intent: Set or clear signing ceremony logos
    question: How do I upload a custom logo for the signing ceremony?
  - id: AccountSigningLogos_GetAccountSigningLogos
    intent: Get signing ceremony logos
    question: What logo do signers see during the signing ceremony?
  phrasing_ops: 2
  slug: conga-accountsigninglogos-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountSigningTheme API from Conga — 1 operation(s) for accountsigningtheme.
  name: Conga Account Signing Theme API
  phrasing_intents:
  - id: AccountSigningTheme_CreateSigningTheme
    intent: Create a custom signing theme
    question: Can I brand the signing experience with my corporate colors?
  - id: AccountSigningTheme_DeleteSigningTheme
    intent: Delete the custom signing theme
    question: Can I remove my branded signing theme and go back to the default?
  - id: AccountSigningTheme_GetSigningTheme
    intent: Get the custom signing theme
    question: What colors does my branded signing theme use?
  - id: AccountSigningTheme_UpdateSigningTheme
    intent: Replace the custom signing theme
    question: Can I change the colors of the signing theme I already have?
  phrasing_ops: 4
  slug: conga-accountsigningtheme-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountSigningUIOptions API from Conga — 1 operation(s) for accountsigninguioptions.
  name: Conga Account Signing UI Options API
  phrasing_intents:
  - id: AccountSigningUIOptions_DeleteAccountSigningUIOptions
    intent: Reset signer experience UI to defaults
    question: Can I drop our signing screen customizations and use the defaults?
  - id: AccountSigningUIOptions_GetAccountSigningUIOptions
    intent: Get signer experience UI settings
    question: What does our new signer experience currently show on the overview screen?
  - id: AccountSigningUIOptions_PatchAccountSigningUIOptions
    intent: Customize signer experience screens
    question: How do I change what signers see on the completion summary screen?
  phrasing_ops: 3
  slug: conga-accountsigninguioptions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountSupportedLanguages API from Conga — 1 operation(s) for accountsupportedlanguages.
  name: Conga Account Supported Languages API
  phrasing_intents:
  - id: AccountSupportedLanguages_DeleteAccountSupportedLanguages
    intent: Reset signing language settings
    question: How do I remove my custom signing language restrictions?
  - id: AccountSupportedLanguages_GetAccountSupportedLanguages
    intent: Get supported signer languages
    question: Which languages can my signers use?
  - id: AccountSupportedLanguages_UpdateAccountSupportedLanguages
    intent: Set default and allowed signer languages
    question: How do I limit the languages available to signers?
  phrasing_ops: 3
  slug: conga-accountsupportedlanguages-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AccountSystemSettings API from Conga — 1 operation(s) for accountsystemsettings.
  name: Conga Account System Settings API
  phrasing_intents:
  - id: AccountSystemSettings_DeleteAccountSystemSettings
    intent: Reset account system settings
    question: Can I put system settings like session timeout back to the defaults?
  - id: AccountSystemSettings_GetAccountSystemSettings
    intent: Get account system settings
    question: What session timeout and token expiry are set on my account?
  - id: AccountSystemSettings_UpdateAccountSystemSettings
    intent: Update account system settings
    question: Can I lengthen the login session timeout?
  phrasing_ops: 3
  slug: conga-accountsystemsettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Action Permissions API from Conga — 1 operation(s) for action permissions.
  name: Conga Action Permissions API
  phrasing_intents:
  - id: getApiUserManagementV1Actionpermissions
    intent: List all action permissions
    question: What action permissions can be granted to users?
  phrasing_ops: 1
  slug: conga-action-permissions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Activities API from Conga — 1 operation(s) for activities.
  name: Conga Activities API
  phrasing_intents:
  - id: Activities_GetActivities
    intent: List approval activities for a record
    question: What approval activity has happened on this agreement or quote?
  phrasing_ops: 1
  slug: conga-activities-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ActivityHistory API from Conga — 1 operation(s) for activityhistory.
  name: Conga Activity History API
  phrasing_intents:
  - id: postApiClmV1ContractsByContractIdActivityhistoryQuery
    intent: Query a contract's activity history
    question: What has happened on a contract so far, and who did it?
  phrasing_ops: 1
  slug: conga-activityhistory-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AdHoc Groups Controller
  name: Conga Ad Hoc Groups API
  phrasing_intents:
  - id: deleteApiCartV1CartsByCartIdAdhocGroups
    intent: Delete several ad hoc groups from a cart
    question: Can I remove a batch of ad hoc groups from a cart at once?
  - id: getApiCartV1CartsByCartIdAdhocGroups
    intent: List a cart's ad hoc groups
    question: Which ad hoc groups have been set up in a quote cart?
  - id: patchApiCartV1CartsByCartIdAdhocGroups
    intent: Update several ad hoc groups in a cart
    question: How do I rename or resequence multiple ad hoc groups together?
  - id: postApiCartV1CartsByCartIdAdhocGroups
    intent: Create ad hoc groups in a cart
    question: How do I group cart line items into custom ad hoc groups?
  - id: deleteApiCartV1CartsByCartIdAdhocGroupsByAdhocGroupId
    intent: Delete one ad hoc group from a cart
    question: How do I remove a single ad hoc group I no longer need?
  - id: getApiCartV1CartsByCartIdAdhocGroupsByAdhocGroupId
    intent: Get one ad hoc group in a cart
    question: What does a specific ad hoc group in my cart contain?
  - id: patchApiCartV1CartsByCartIdAdhocGroupsByAdhocGroupId
    intent: Update one ad hoc group in a cart
    question: How do I change the name or sequence of one ad hoc group?
  phrasing_ops: 7
  slug: conga-adhocgroups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AdhocProcess API from Conga — 5 operation(s) for adhocprocess.
  name: Conga Adhoc Process API
  phrasing_intents:
  - id: AdhocProcess_Save
    intent: Define an ad hoc approval process
    question: How do I set up ad hoc approver groups for a record?
  - id: AdhocProcess_Submit
    intent: Submit a record for ad hoc approval
    question: Can I send a record for ad hoc approval with a comment and attachments?
  - id: AdhocProcess_DeleteAdhocProcessDefinition
    intent: Delete a record's ad hoc approvals
    question: Can I remove the ad hoc approvals from a record?
  - id: AdhocProcess_GetAdhocProcessDefinition
    intent: Get a saved, unsubmitted ad hoc process
    question: What ad hoc process is saved on a record before it is submitted?
  - id: AdhocProcess_PostSubmit
    intent: Get a submitted ad hoc process
    question: What does the ad hoc process look like after it was submitted?
  - id: AdhocProcess_ReSubmitApproval
    intent: Resubmit an ad hoc approval
    question: Can I resubmit an ad hoc approval that was already submitted?
  phrasing_ops: 6
  slug: conga-adhocprocess-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Adjustments controller
  name: Conga Adjustments API
  phrasing_intents:
  - id: deleteApiCartV1CartsByCartIdAdjustments
    intent: Delete several adjustments from a cart
    question: Can I remove multiple adjustments from a cart in one call?
  - id: getApiCartV1CartsByCartIdAdjustments
    intent: List a cart's price adjustments
    question: What discounts and price adjustments are applied in a cart?
  - id: patchApiCartV1CartsByCartIdAdjustments
    intent: Update several adjustments in a cart
    question: Is there a way to edit many cart adjustments together?
  - id: postApiCartV1CartsByCartIdAdjustments
    intent: Add price adjustments to a cart
    question: How do I add a discount adjustment to a quote cart?
  - id: deleteApiCartV1CartsByCartIdAdjustmentsByAdjustmentId
    intent: Delete one cart adjustment
    question: How do I remove a single discount adjustment from a cart?
  - id: getApiCartV1CartsByCartIdAdjustmentsByAdjustmentId
    intent: Get one cart adjustment
    question: What are the details of a specific adjustment in my cart?
  - id: patchApiCartV1CartsByCartIdAdjustmentsByAdjustmentId
    intent: Change one cart adjustment's amount or type
    question: How do I change the amount on one adjustment in a cart?
  - id: deleteApiCartV1CartsByCartIdItemsByLineItemIdAdjustments
    intent: Remove adjustments from one line item
    question: How do I clear all discounts from a single line in the cart?
  phrasing_ops: 8
  slug: conga-adjustments-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Admin Permissions API from Conga — 1 operation(s) for admin permissions.
  name: Conga Admin Permissions API
  phrasing_intents:
  - id: getApiUserManagementV1AdminPermissions
    intent: List all admin permissions
    question: What administrator permissions exist that I can assign?
  phrasing_ops: 1
  slug: conga-admin-permissions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Adobe sign
  name: Conga Adobe Sign API
  phrasing_intents:
  - id: getApiEsignV1AdobeByTransactionIdAudittrail
    intent: Get the Adobe Sign audit trail for a transaction
    question: What signing events happened on an Adobe Sign transaction?
  phrasing_ops: 1
  slug: conga-adobesign-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for Agreements
  name: Conga Agreement API
  phrasing_intents:
  - id: postApiXauthorV1Contracts
    intent: Create an agreement from X-Author
    question: How do I create a new agreement record while authoring in Word?
  - id: postApiXauthorV1ContractsAdvanceQuery
    intent: Search agreements with advanced filters
    question: Can I search agreements with complex filter expressions and grouping?
  - id: postApiXauthorV1ContractsQuery
    intent: Search agreements by keyword
    question: How do I find agreements that match a search term?
  - id: postApiXauthorV1ContractsQueryMe
    intent: List agreements I own
    question: Which agreements am I the owner of?
  - id: postApiXauthorV1ContractsRecentlyViewed
    intent: List recently viewed agreements
    question: Which agreements have I opened recently?
  - id: getApiXauthorV1ContractsByContractId
    intent: Get an agreement's details
    question: What are the details of a specific agreement?
  - id: getApiXauthorV1ContractsByContractIdRecordType
    intent: Get an agreement's record type
    question: What record type is a given agreement?
  phrasing_ops: 7
  slug: conga-agreement-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class holds APIs related to agreement clauses
  name: Conga Agreement Clause API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdClausesFinal
    intent: Record agreement clauses as final
    question: How do I save an agreement's clause entries as the final version?
  - id: postApiXauthorV1ContractsByContractIdClausesOriginal
    intent: Record an agreement's original clauses
    question: How do I capture the original clause entries for an agreement?
  - id: postApiXauthorV1ContractsByContractIdDocumentsByDocumentIdClausesFinal
    intent: Finalize one document's clause entries
    question: How do I finalize the clauses within one specific agreement document?
  - id: getApiXauthorV1ContractsByContractIdDocumentsByDocumentVersionIdClausesRevertible
    intent: List clause changes that can be reverted
    question: Which modified clauses in a document version can still be reverted?
  - id: postApiXauthorV1ContractsByContractIdDocumentsByDocumentVersionIdFilesByFileIdClausesOriginal
    intent: Record original clauses from an attached file
    question: How do I extract original clause entries from a specific attached file?
  - id: postApiXauthorV1ContractsByContractIdDocumentsByDocumentVersionIdMetadataByMetadataFileIdClausesOriginal
    intent: Record original clauses from a metadata file
    question: Can I create original clause entries using a document's metadata file?
  phrasing_ops: 6
  slug: conga-agreementclause-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs related to agreement documents.
  name: Conga Agreement Document API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdDocumentsCompareandmerge
    intent: Compare and merge agreement documents
    question: How do I compare a counterparty's version against my agreement document and merge them?
  - id: postApiXauthorV1ContractsByContractIdDocumentsRegenerate
    intent: Regenerate an agreement document from a template
    question: How do I regenerate an agreement's document using a different template?
  - id: postApiXauthorV1ContractsByContractIdDocumentsVersions
    intent: List an agreement's document versions
    question: What versions of the document exist on an agreement?
  - id: getApiXauthorV1ContractsByContractIdDocumentsByDocumentIdTags
    intent: Get the tags on an agreement document
    question: Which tags are attached to a document on an agreement?
  phrasing_ops: 4
  slug: conga-agreementdocument-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs related to agreement document checkins
  name: Conga Agreement Document Checkin API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdDocumentsCheckIn
    intent: Check in an agreement document
    question: How do I check my edited document back into an agreement?
  phrasing_ops: 1
  slug: conga-agreementdocumentcheckin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for Agreement Document's Lock.
  name: Conga Agreement Lock API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdDocumentsLockStatus
    intent: Check whether an agreement document is locked
    question: Is someone else currently editing this agreement document?
  - id: postApiXauthorV1ContractsByContractIdDocumentsReleaseLock
    intent: Release the edit lock on an agreement
    question: How do I unlock an agreement so others can edit it?
  - id: postApiXauthorV1ContractsByContractIdDocumentsByDocumentidAcquireLock
    intent: Lock an agreement document for editing
    question: How do I lock an agreement document so nobody else edits it while I work?
  phrasing_ops: 3
  slug: conga-agreementlock-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs for agreement metadata.
  name: Conga Agreement Metadata API
  phrasing_intents:
  - id: getApiXauthorV1ContractsByContractIdMetadata
    intent: Get an agreement's field metadata
    question: Which fields and values are defined on an agreement?
  phrasing_ops: 1
  slug: conga-agreementmetadata-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs related to offline agreements.
  name: Conga Agreement Offline API
  phrasing_intents:
  - id: postApiXauthorV1ContractsDocumentsCreateOffline
    intent: Create a new agreement from an offline document
    question: How do I turn a document I drafted outside the system into a new agreement?
  - id: postApiXauthorV1ContractsDocumentsCreateOfflineMultipart
    intent: Create an offline agreement by file upload
    question: Can I upload a file directly to create a new offline agreement record?
  - id: postApiXauthorV1ContractsDocumentsStoreExecutedMultipart
    intent: Store an already-executed agreement
    question: How do I store a contract that was already signed outside the system?
  - id: postApiXauthorV1ContractsByContractIdDocumentsImportOffline
    intent: Import an offline document into an existing agreement
    question: How do I add an externally drafted document to an agreement that already exists?
  - id: postApiXauthorV1ContractsByContractIdDocumentsImportOfflineMultipart
    intent: Upload an offline file into an existing agreement
    question: Can I upload a file into an existing agreement and convert a PDF to Word?
  phrasing_ops: 5
  slug: conga-agreementoffline-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs for Agreement Review Controller.
  name: Conga Agreement Review API
  phrasing_intents:
  - id: getApiXauthorV1ContractsByContractIdReviews
    intent: List reviews on an agreement
    question: What reviews are in progress or done on an agreement?
  phrasing_ops: 1
  slug: conga-agreementreview-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides endpoints for managing and retrieving agreement signing cycles.
  name: Conga Agreement Signing Cycle API
  phrasing_intents:
  - id: getApiEsignV1AgreementByAgreementIdSigningCycle
    intent: List an agreement's signing cycles
    question: How many times has an agreement been sent out for signature?
  phrasing_ops: 1
  slug: conga-agreementsigningcycle-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs related to agreement and template related operations.
  name: Conga Agreement Template API
  phrasing_intents:
  - id: getApiXauthorV1ContractsByContractIdTemplates
    intent: Get the template for an agreement
    question: Which templates can be used to generate a given agreement's document?
  phrasing_ops: 1
  slug: conga-agreementtemplate-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for documents AI operation
  name: Conga AI Redline API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdAIRedlineCheckIn
    intent: Check in a document with AI redline changes
    question: How do I publish the clause changes suggested by AI redlining back to the agreement?
  - id: postApiXauthorV1ContractsByContractIdAIRedlinePreview
    intent: Preview a document with AI redline changes
    question: Can I see what the agreement would look like after the AI redline edits before committing?
  - id: postApiXauthorV1ContractsByContractIdAIRedlineRisks
    intent: Analyze document content for AI redline risks
    question: Can AI flag risky language in the agreement text I'm drafting?
  - id: getApiXauthorV1ContractsByContractIdAIRedlineRisksByAttachmentId
    intent: Get AI redline risks for an attachment
    question: What risks did AI find in a specific agreement attachment?
  phrasing_ops: 4
  slug: conga-airedline-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for alternate clauses related operations.
  name: Conga Alternate Clause API
  phrasing_intents:
  - id: postApiXauthorV1ClausesByClauseIdAlternatesLink
    intent: Link alternate clauses to a clause
    question: How do I offer fallback alternate clauses for a standard clause?
  - id: deleteApiXauthorV1ClausesByClauseIdAlternatesByAlternateclausemappingId
    intent: Unlink an alternate clause
    question: How do I stop offering an alternate clause for a clause?
  - id: postApiXauthorV1ClausesByClauseIdConfigurationsByConfigurationIdAlternatesReOrder
    intent: Reorder a clause's alternate clauses
    question: Can I change the order in which alternate clauses are presented?
  phrasing_ops: 3
  slug: conga-alternateclause-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class holds APIs related to application usage
  name: Conga Analytics API
  phrasing_intents:
  - id: postApiXauthorV1Analytics
    intent: Record an X-Author usage event
    question: How do I log usage analytics from the X-Author add-in?
  phrasing_ops: 1
  slug: conga-analytics-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The API Connections API from Conga — 3 operation(s) for api connections.
  name: Conga API Connections API
  phrasing_intents:
  - id: getApiUserManagementV1ApiConnections
    intent: List all API connections
    question: Which API connections and clients are set up for our tenant?
  - id: getApiUserManagementV1ApiConnectionsByExternalIdentifier
    intent: Get an API connection
    question: What are the settings of a particular API connection?
  - id: postApiUserManagementV1ApiConnectionsByExternalIdentifier
    intent: Add an API connection
    question: How do I register a new API client connection?
  - id: putApiUserManagementV1ApiConnectionsByExternalIdentifier
    intent: Update an API connection's settings
    question: How do I change the redirect URI on an existing API connection?
  - id: putApiUserManagementV1ApiConnectionsByExternalIdentifierStatus
    intent: Activate or deactivate an API connection
    question: Can I disable an API connection without deleting it?
  phrasing_ops: 5
  slug: conga-api-connections-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The API Resource API from Conga — 7 operation(s) for api resource.
  name: Conga API Resource API
  phrasing_intents:
  - id: getApiExtensibilityV1CustomcodeApiResource
    intent: List custom API resources
    question: Which custom API resources have been defined in custom code?
  - id: postApiExtensibilityV1CustomcodeApiResource
    intent: Create a custom API resource
    question: How do I define a new custom API resource backed by custom code?
  - id: getApiExtensibilityV1CustomcodeApiResourceCancellationSettings
    intent: Get the custom API cancellation timeout
    question: How long can a custom API call run before it is cancelled?
  - id: putApiExtensibilityV1CustomcodeApiResourceCancellationSettings
    intent: Set the custom API cancellation timeout
    question: How do I change when long-running custom API calls are cancelled?
  - id: postApiExtensibilityV1CustomcodeApiResourceResolve
    intent: Resolve a custom API route to its URI entry
    question: Which custom code method will handle a given resource path and HTTP verb?
  - id: deleteApiExtensibilityV1CustomcodeApiResourceByName
    intent: Delete a custom API resource
    question: How do I remove a custom API resource I no longer use?
  - id: getApiExtensibilityV1CustomcodeApiResourceByName
    intent: Get a custom API resource by name
    question: What is configured on a particular custom API resource?
  - id: postApiExtensibilityV1CustomcodeApiResourceByNameClone
    intent: Clone a custom API resource
    question: Can I copy an existing API resource along with all its URI entries?
  phrasing_ops: 12
  slug: conga-api-resource-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Approval API from Conga — 6 operation(s) for approval.
  name: Conga Approval API
  phrasing_intents:
  - id: Approval_CreateApproval
    intent: Add a signature approval to a document
    question: How do I add a new signature block for a role on a Conga Sign document?
  - id: Approval_UpdateApprovals
    intent: Update all approvals on a document
    question: Can I update every signature approval on a document in one request?
  - id: Approval_DeleteApproval
    intent: Delete an approval from a document
    question: Can I remove a signature approval from a document before sending it?
  - id: Approval_GetApproval
    intent: Retrieve one approval on a document
    question: What fields and role are set on a specific approval in a document?
  - id: Approval_UpdateApproval
    intent: Update a specific approval on a document
    question: Can I change the role or make one existing approval optional?
  - id: Approval_CreateApprovalField
    intent: Add a field to an approval with a generated name
    question: How do I place a new signature or input field on an existing approval?
  - id: Approval_CreateApprovalFieldById
    intent: Add a field to an approval with a chosen field ID
    question: Can I create an approval field using a field ID I pick myself?
  - id: Approval_DeleteFieldById
    intent: Delete a field from an approval
    question: Can I remove a single field from an approval without deleting the approval?
  phrasing_ops: 12
  slug: conga-approval-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller to manage the asset action(s)
  name: Conga Asset Actions API
  phrasing_intents:
  - id: postApiAssetV1AssetsByCartIdChange
    intent: Amend a customer's assets in a cart
    question: How do I bring existing assets into a cart so I can amend them?
  - id: postApiAssetV1AssetsByCartIdChangeConfiguration
    intent: Reconfigure an asset
    question: How do I change the configuration of a product a customer already owns?
  - id: postApiAssetV1AssetsByCartIdChangeQuantity
    intent: Change the quantity of assets
    question: How do I increase the number of seats on an asset a customer owns?
  - id: postApiAssetV1AssetsByCartIdRenew
    intent: Renew assets
    question: How do I renew a customer's subscriptions for another term?
  - id: postApiAssetV1AssetsByCartIdRestore
    intent: Restore line items to their original asset values
    question: Can I undo edits to an amended line item and go back to the asset's values?
  - id: postApiAssetV1AssetsByCartIdResume
    intent: Resume suspended assets
    question: How do I reactivate a customer's suspended subscription?
  - id: postApiAssetV1AssetsByCartIdSuspend
    intent: Suspend assets for a period
    question: How do I pause a customer's subscription for a few months?
  - id: postApiAssetV1AssetsByCartIdSwap
    intent: Swap an asset for another product
    question: How do I upgrade a customer from one product to an eligible replacement?
  phrasing_ops: 10
  slug: conga-assetactions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller to manage assets
  name: Conga Assets API
  phrasing_intents:
  - id: getApiAssetV1Assets
    intent: List an account's asset line items
    question: What products and subscriptions does a customer account currently own?
  - id: getApiAssetV1AssetsGroupSummary
    intent: Summarize assets grouped by a field
    question: Can I see a customer's assets rolled up by a field such as product family?
  - id: postApiAssetV1AssetsRelatedPurchases
    intent: List purchases related to given assets
    question: What other purchases are related to a set of assets?
  - id: getApiAssetV1AssetsByCartId
    intent: List asset line items in a cart's context
    question: Which existing assets are available to amend inside a particular cart?
  - id: postApiAssetV1TerminatePreview
    intent: Preview the impact of terminating assets
    question: What would the financial impact be if we cancelled these assets on a date?
  - id: getApiAssetV1ByAssetIdCoterm
    intent: Find assets that co-terminate with an asset
    question: Which other assets on the account share the same end date criteria as this one?
  - id: getApiAssetV1ByParentAssetIdAssets
    intent: List the child assets of a bundle
    question: What options and components sit inside a bundle asset?
  phrasing_ops: 7
  slug: conga-assets-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AsyncOperationStatus API from Conga — 1 operation(s) for asyncoperationstatus.
  name: Conga Async Operation Status API
  phrasing_intents:
  - id: AsyncOperationStatus_GetByCorrelationId
    intent: Check an async operation status
    question: Is my background operation finished yet?
  phrasing_ops: 1
  slug: conga-asyncoperationstatus-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Attribute Constraint Rule Entries API from Conga — 4 operation(s) for attribute constraint rule entries.
  name: Conga Attribute Constraint Rule Entries API
  phrasing_intents:
  - id: deleteAttributeConstraintRulesByParentIdEntries
    intent: Delete several attribute constraint rule entries
    question: Can I remove multiple entries from an attribute constraint rule at once?
  - id: getAttributeConstraintRulesByParentIdEntries
    intent: List an attribute constraint rule's entries
    question: Which entries make up an attribute constraint rule?
  - id: patchAttributeConstraintRulesByParentIdEntries
    intent: Update several attribute constraint rule entries
    question: Is there a way to edit many constraint rule entries together?
  - id: postAttributeConstraintRulesByParentIdEntries
    intent: Add entries to an attribute constraint rule
    question: How do I add new entries to an attribute constraint rule?
  - id: getAttributeConstraintRulesByParentIdEntriesExport
    intent: Export constraint rule entries to CSV
    question: Can I download an attribute constraint rule's entries as a CSV?
  - id: postAttributeConstraintRulesByParentIdEntriesImport
    intent: Import constraint rule entries from CSV
    question: How do I load attribute constraint rule entries from a CSV file?
  - id: deleteAttributeConstraintRulesByParentIdEntriesById
    intent: Delete one attribute constraint rule entry
    question: How do I remove a single entry from an attribute constraint rule?
  - id: getAttributeConstraintRulesByParentIdEntriesById
    intent: Get one attribute constraint rule entry
    question: What does a single attribute constraint rule entry contain?
  phrasing_ops: 9
  slug: conga-attribute-constraint-rule-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Attribute Constraint Rules API from Conga — 2 operation(s) for attribute constraint rules.
  name: Conga Attribute Constraint Rules API
  phrasing_intents:
  - id: deleteAttributeConstraintRules
    intent: Delete attribute constraint rules in bulk
    question: Is there a way to remove many attribute constraint rules at once by passing a list of IDs?
  - id: getAttributeConstraintRules
    intent: List attribute constraint rules
    question: Which attribute constraint rules are currently set up in Conga CPQ?
  - id: patchAttributeConstraintRules
    intent: Update attribute constraint rules in bulk
    question: Can I edit several attribute constraint rules together in one bulk update?
  - id: postAttributeConstraintRules
    intent: Create attribute constraint rules in bulk
    question: How do I add several new attribute constraint rules in one request?
  - id: deleteAttributeConstraintRulesById
    intent: Delete one attribute constraint rule
    question: How can I remove just one attribute constraint rule by its identifier?
  - id: getAttributeConstraintRulesById
    intent: Get one attribute constraint rule
    question: What are the details of a single attribute constraint rule when I know its ID?
  - id: patchAttributeConstraintRulesById
    intent: Update one attribute constraint rule
    question: Can I change the settings of one specific attribute constraint rule by its ID?
  phrasing_ops: 7
  slug: conga-attribute-constraint-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Attribute Group Members API from Conga — 2 operation(s) for attribute group members.
  name: Conga Attribute Group Members API
  phrasing_intents:
  - id: deleteAttributeGroupsByParentIdAttributes
    intent: Remove several attributes from an attribute group
    question: Is there a way to remove multiple attributes from an attribute group at once?
  - id: getAttributeGroupsByParentIdAttributes
    intent: List the attributes in an attribute group
    question: Which product attributes belong to a given attribute group in Conga CPQ?
  - id: patchAttributeGroupsByParentIdAttributes
    intent: Update several members of an attribute group
    question: Can I edit many attribute group members in one batch update?
  - id: postAttributeGroupsByParentIdAttributes
    intent: Add attributes to an attribute group
    question: Can I add several attributes to an attribute group in one request?
  - id: deleteAttributeGroupsByParentIdAttributesById
    intent: Remove one attribute from an attribute group
    question: Can I drop a single attribute from an attribute group by its member ID?
  - id: getAttributeGroupsByParentIdAttributesById
    intent: Get one member of an attribute group
    question: What are the details of a single attribute group member record?
  - id: patchAttributeGroupsByParentIdAttributesById
    intent: Update one member of an attribute group
    question: Can I change the settings of one attribute group member without touching the others?
  phrasing_ops: 7
  slug: conga-attribute-group-members-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Attribute Groups API from Conga — 2 operation(s) for attribute groups.
  name: Conga Attribute Groups API
  phrasing_intents:
  - id: deleteAttributeGroups
    intent: Delete attribute groups in bulk
    question: Is it possible to delete multiple attribute groups at once?
  - id: getAttributeGroups
    intent: List attribute groups
    question: Which attribute groups exist in my Conga product catalog?
  - id: patchAttributeGroups
    intent: Update attribute groups in bulk
    question: Can I edit many attribute groups in one bulk update?
  - id: postAttributeGroups
    intent: Create attribute groups in bulk
    question: Can I create several new attribute groups in one request?
  - id: deleteAttributeGroupsById
    intent: Delete one attribute group
    question: How do I remove a single attribute group by its ID?
  - id: getAttributeGroupsById
    intent: Get one attribute group
    question: What details are stored on a single attribute group?
  - id: patchAttributeGroupsById
    intent: Update one attribute group
    question: Can I rename or edit one particular attribute group by its ID?
  phrasing_ops: 7
  slug: conga-attribute-groups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Attribute Matrices API from Conga — 2 operation(s) for attribute matrices.
  name: Conga Attribute Matrices API
  phrasing_intents:
  - id: deleteAttributeMatrices
    intent: Delete several attribute matrices
    question: Can I delete a whole list of attribute matrices at once by their IDs?
  - id: getAttributeMatrices
    intent: List attribute matrices
    question: Which attribute matrices exist in my Conga CPQ org?
  - id: patchAttributeMatrices
    intent: Update several attribute matrices
    question: Can I edit multiple attribute matrices in a single batch?
  - id: postAttributeMatrices
    intent: Create attribute matrices
    question: Can I create several product-scoped attribute matrices in one request?
  - id: deleteAttributeMatricesById
    intent: Delete an attribute matrix
    question: How do I delete one attribute matrix by its ID?
  - id: getAttributeMatricesById
    intent: Get an attribute matrix
    question: What does one particular attribute matrix record contain?
  - id: patchAttributeMatricesById
    intent: Update an attribute matrix
    question: Can I change one attribute matrix by its identifier?
  phrasing_ops: 7
  slug: conga-attribute-matrices-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Attribute Matrix Entries API from Conga — 4 operation(s) for attribute matrix entries.
  name: Conga Attribute Matrix Entries API
  phrasing_intents:
  - id: deleteAttributeMatricesByParentIdEntries
    intent: Delete several entries from an attribute matrix
    question: Can I remove many attribute matrix rows in a single call?
  - id: getAttributeMatricesByParentIdEntries
    intent: List the entries in an attribute matrix
    question: Which rows are currently defined in one of my attribute matrices?
  - id: patchAttributeMatricesByParentIdEntries
    intent: Update several attribute matrix entries
    question: Can values on many attribute matrix rows be changed together?
  - id: postAttributeMatricesByParentIdEntries
    intent: Add several entries to an attribute matrix
    question: Is there a way to add a batch of new rows to an attribute matrix at once?
  - id: getAttributeMatricesByParentIdEntriesExport
    intent: Export attribute matrix entries to CSV
    question: Can I download an attribute matrix's entries as a CSV spreadsheet?
  - id: postAttributeMatricesByParentIdEntriesImport
    intent: Import attribute matrix entries from CSV
    question: Can I load attribute matrix rows from a CSV file instead of JSON?
  - id: deleteAttributeMatricesByParentIdEntriesById
    intent: Delete one attribute matrix entry
    question: How do I remove one specific row from an attribute matrix?
  - id: getAttributeMatricesByParentIdEntriesById
    intent: Get one attribute matrix entry
    question: How do I look up a single row of an attribute matrix by its ID?
  phrasing_ops: 9
  slug: conga-attribute-matrix-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for managing attributes.
  name: Conga Attributes API
  phrasing_intents:
  - id: deleteAttributes
    intent: Delete several attributes at once
    question: How can I bulk-remove a set of attributes by their IDs?
  - id: getAttributes
    intent: List product attributes
    question: Where can I see every attribute defined in my Conga admin setup?
  - id: patchAttributes
    intent: Update several attributes at once
    question: Can I update fields on many attribute records in one request?
  - id: postAttributes
    intent: Create attributes
    question: How do I add new attributes to the catalog administration?
  - id: deleteAttributesById
    intent: Delete one attribute by ID
    question: How do I remove a single attribute when I know its ID?
  - id: getAttributesById
    intent: Get a single attribute
    question: How do I look up one attribute's full record by its ID?
  - id: patchAttributesById
    intent: Update one attribute by ID
    question: How do I change fields on one specific attribute?
  phrasing_ops: 7
  slug: conga-attributes-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The AuthenticationTokens API from Conga — 4 operation(s) for authenticationtokens.
  name: Conga Authentication Tokens API
  phrasing_intents:
  - id: AuthenticationTokens_CreateSenderAuthToken
    intent: Create a sender token to edit a package
    question: How can a package owner get a session to edit it in the Designer view?
  - id: AuthenticationTokens_CreateMultiUseSignerAuthToken
    intent: Create a reusable signer session token
    question: Can I create a signer token that works more than once?
  - id: AuthenticationTokens_CreateSingleUseSignerAuthToken
    intent: Create a one-time signer session token
    question: How do I embed signing by giving a signer a one-time session token?
  - id: AuthenticationTokens_GetUserAuthToken
    intent: Create a user token to view package details
    question: Can I get an access token tied to a signer's email to view package details?
  phrasing_ops: 4
  slug: conga-authenticationtokens-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains endpoints for authorizing sign providers like Conga Sign, Adobe Sign, or DocuSign, or wet signature.
  name: Conga Authorization API
  phrasing_intents:
  - id: postApiEsignV1AuthorizeRefresh
    intent: Get an eSignature refresh token
    question: How do I exchange an authentication code for a refresh token for my eSignature provider?
  - id: getApiEsignV1AuthorizeToken
    intent: Get an eSignature access token
    question: Where do I get an access token for my eSignature service provider in Conga?
  - id: postApiReviewV1GoogleAuthorize
    intent: Get a token for a Google service account
    question: How do I turn my encrypted Google service account JSON into an access token for document review?
  - id: getApiReviewV1ByReviewtypeAuthorize
    intent: Get review auth URL or token for a user
    question: How do I get the authorization URL for Office365 document review?
  - id: getApiReviewV1ByReviewtypeDelegatedToken
    intent: Get a review token in delegated flow
    question: How do I swap the auth code from the delegated login for a review token?
  - id: getApiXauthorV1AuthorizationTokenInfo
    intent: Check who a login token belongs to
    question: How can I verify whether my logged-in token is valid on the Conga Platform or Salesforce?
  phrasing_ops: 6
  slug: conga-authorization-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The BackupAdmin API from Conga — 1 operation(s) for backupadmin.
  name: Conga Backup Admin API
  phrasing_intents:
  - id: BackupAdmin_DeleteBackupAdminUser
    intent: Remove my backup administrator
    question: Can I clear my backup admin so nobody covers for me?
  - id: BackupAdmin_GetBackupAdminUser
    intent: Get my backup administrator
    question: Who is set as my backup administrator for approvals?
  - id: BackupAdmin_UpsertBackupAdminUser
    intent: Set or change my backup administrator
    question: How do I name someone as my backup admin for approvals?
  phrasing_ops: 3
  slug: conga-backupadmin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The BackupDelegates API from Conga — 5 operation(s) for backupdelegates.
  name: Conga Backup Delegates API
  phrasing_intents:
  - id: BackupDelegates_SaveBackupDelegates
    intent: Create or update a backup or delegate approver
    question: How do I set someone as my backup approver while I'm out of office?
  - id: BackupDelegates_Search
    intent: List backup and delegate approvers
    question: Who is set up as a backup or delegate approver?
  - id: BackupDelegates_GetActiveInactiveCount
    intent: Count backup and delegate approvers
    question: How many backup and delegate approvers are active versus inactive?
  - id: BackupDelegates_Delete
    intent: Delete a backup or delegate approver record
    question: Can I remove a backup approver assignment entirely?
  - id: BackupDelegates_GetById
    intent: Get a backup or delegate approver record
    question: What are the dates and users on one backup assignment?
  - id: BackupDelegates_Activate
    intent: Activate a backup or delegate
    question: Can I turn a saved backup assignment on now?
  - id: BackupDelegates_DeActivate
    intent: Deactivate a backup or delegate
    question: Can I switch off a backup approver when I'm back in office?
  phrasing_ops: 7
  slug: conga-backupdelegates-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Bulk Import API from Conga — 5 operation(s) for bulk import.
  name: Conga Bulk Import API
  phrasing_intents:
  - id: postApiClmV1ImportJobs
    intent: Start a bulk CSV import job
    question: How do I bulk-load accounts, contacts or agreements into Conga CLM from a CSV?
  - id: postApiClmV1ImportJobsQuery
    intent: List bulk import jobs
    question: Which bulk import jobs have been run so far?
  - id: deleteApiClmV1ImportJobsByJobId
    intent: Delete a bulk import job record
    question: Can I permanently remove the record of an old import job?
  - id: getApiClmV1ImportJobsByJobId
    intent: Get the result of a bulk import job
    question: Did my bulk import job succeed or fail?
  - id: getApiClmV1ImportJobsByJobIdBatchByBatchId
    intent: Get the file uploaded in an import batch
    question: How can I see what was in the CSV file uploaded for an import batch?
  - id: getApiClmV1ImportTemplatesByFormat
    intent: Download a bulk import template
    question: Where do I get the CSV template needed to bulk-import agreements?
  phrasing_ops: 6
  slug: conga-bulk-import-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The BundleLineItemStructure API from Conga — 1 operation(s) for bundlelineitemstructure.
  name: Conga Bundle Line Item Structure API
  phrasing_intents:
  - id: getApiCartV1CartsByCartIdBundleByLineNumberDetails
    intent: Get a cart bundle's structure details
    question: How can I see the option groups and options inside a bundle on a Conga cart?
  phrasing_ops: 1
  slug: conga-bundlelineitemstructure-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The BusinessObjects API from Conga — 15 operation(s) for businessobjects.
  name: Conga Business Objects API
  phrasing_intents:
  - id: BusinessObjects_GetBusinessObjects
    intent: List business object types
    question: Which business object types can approvals run on in Conga?
  - id: BusinessObjects_GetAssigneePicklists
    intent: List assignee type values for all objects
    question: What related-user assignee values exist across all business objects?
  - id: BusinessObjects_GetAssigneePicklistsByBusinessObject
    intent: List one object's assignee type values
    question: Which related-user assignee values can I use for a specific object type?
  - id: BusinessObjects_GetEmailTemplatesByBusinessObjectAndEmailTemplateCategory
    intent: List email templates for an object and category
    question: Which email templates exist for one object type within a specific category?
  - id: BusinessObjects_GetChildObjectTypes
    intent: List a business object's child types
    question: What child object types sit under a given business object?
  - id: BusinessObjects_GetCustomUserAssigneeFields
    intent: List an object's custom user fields
    question: Which user fields on an object can drive a Custom User assignee?
  - id: BusinessObjects_ValidateCustomUserAssigneePayload
    intent: Validate a custom assignee definition
    question: Can I check a custom assignee expression is valid before saving the step?
  - id: BusinessObjects_GetEmailTemplatesForBusinessObject
    intent: List email templates for an object type
    question: Which notification email templates are available for a given object type?
  phrasing_ops: 15
  slug: conga-businessobjects-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Callback API from Conga — 7 operation(s) for callback.
  name: Conga Callback API
  phrasing_intents:
  - id: Callback_AddCallback
    intent: Register a package event callback
    question: How do I get notified at my URL when a package is signed?
  - id: Callback_GetCallback
    intent: Get my package event callback
    question: What webhook URL is set to receive package event notifications?
  - id: Callback_AddConnectorCallback
    intent: Register a callback for a connector
    question: How do I add an event callback for a Dynamics connector?
  - id: Callback_GetConnectorCallback
    intent: Get callbacks for a connector
    question: What callbacks are configured for my SharePoint or Dynamics connector?
  - id: getApiExtensibilityV1Callbacks
    intent: List all custom code callback contracts
    question: Which callback contracts exist for custom code extensibility?
  - id: putApiExtensibilityV1Callbacks
    intent: Map a callback contract to custom code
    question: How do I point a callback contract at my own custom code project and class?
  - id: getApiExtensibilityV1CallbacksModules
    intent: List modules that expose callbacks
    question: Which modules have registered extensibility callbacks?
  - id: getApiExtensibilityV1CallbacksModulesByModuleName
    intent: List callback contracts for one module
    question: Which callback contracts does a particular module expose?
  phrasing_ops: 11
  slug: conga-callback-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Config Debug Rule Controller
  name: Conga Cart Analyzers API
  phrasing_intents:
  - id: getApiCartV1CartsByCartIdApplicableAttributeRules
    intent: List attribute rules that could apply to a cart
    question: Which product attribute rules are applicable to my cart's line items?
  - id: getApiCartV1CartsByCartIdApplicableFieldExpression
    intent: List field expressions that could apply to a cart
    question: What field expressions are applicable to a given cart?
  - id: getApiCartV1CartsByCartIdApplicableRules
    intent: List constraint rules that could apply to a cart
    question: Which rules are applicable to my cart overall, not just attribute rules?
  - id: getApiCartV1CartsByCartIdAppliedAttributeRules
    intent: List attribute rules already applied to a cart
    question: Which product attribute rules were actually applied to my cart?
  - id: getApiCartV1CartsByCartIdAppliedFieldExpression
    intent: List field expressions already applied to a cart
    question: Which field expressions have been applied to my cart so far?
  - id: getApiCartV1CartsByCartIdAppliedRules
    intent: List rules already applied to a cart
    question: What rules have already been applied to a cart in total?
  phrasing_ops: 6
  slug: conga-cart-analyzers-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Cart Controller
  name: Conga Carts API
  phrasing_intents:
  - id: deleteApiCartV1Carts
    intent: Delete carts in bulk
    question: Is there a way to delete many carts at once?
  - id: getApiCartV1Carts
    intent: List carts
    question: Which shopping carts exist in Conga CPQ right now?
  - id: patchApiCartV1Carts
    intent: Update carts in bulk
    question: Can I update multiple carts together?
  - id: postApiCartV1Carts
    intent: Create carts in bulk
    question: Can I create several carts at once from a list?
  - id: deleteApiCartV1CartsById
    intent: Delete one cart
    question: How do I delete a single cart by its identifier?
  - id: getApiCartV1CartsById
    intent: Get one cart
    question: What's in a specific cart when I know its ID?
  - id: patchApiCartV1CartsById
    intent: Update one cart
    question: Can I change fields on one particular cart by ID?
  phrasing_ops: 7
  slug: conga-carts-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Categories API from Conga — 11 operation(s) for categories.
  name: Conga Categories API
  phrasing_intents:
  - id: deleteCategories
    intent: Delete categories in bulk
    question: Is there a way to delete multiple categories by a list of IDs?
  - id: getCategories
    intent: List categories
    question: Which product categories exist in my Conga catalog?
  - id: patchCategories
    intent: Update categories in bulk
    question: Can I edit many categories in one request?
  - id: postCategories
    intent: Create categories in bulk
    question: Can I create several catalog categories in one request?
  - id: deleteCategoriesById
    intent: Delete one category
    question: How do I delete a single category by ID?
  - id: getCategoriesById
    intent: Get one category record
    question: What does a single category record contain?
  - id: patchCategoriesById
    intent: Update one category
    question: Can I edit one specific category record?
  - id: getCategoriesByCategoryIdPriceLists
    intent: List price lists for a category
    question: Which price lists use a given category?
  phrasing_ops: 21
  slug: conga-categories-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The CDN Store API from Conga — 3 operation(s) for cdn store.
  name: Conga CDN Store API
  phrasing_intents:
  - id: deleteApiCdnstoreV1Files
    intent: Delete one file from the CDN store
    question: How do I delete a single file from the CDN store by name and path?
  - id: deleteApiCdnstoreV1FilesBulk
    intent: Delete multiple files from the CDN store
    question: Can I delete several CDN files under the same folder in one request?
  - id: getApiCdnstoreV1FilesByFileFullPath
    intent: Download a file from the CDN store
    question: How do I fetch a file's contents and details from the CDN store?
  - id: postApiCdnstoreV1FilesByFileFullPath
    intent: Upload a file to the CDN store
    question: How do I upload a file to the Conga CDN store?
  phrasing_ops: 4
  slug: conga-cdn-store-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for clauses.
  name: Conga Clause API
  phrasing_intents:
  - id: postApiXauthorV1ClausesAlternate
    intent: Get alternate clauses for negotiation
    question: What alternate wording is available for a clause during contract negotiation?
  - id: postApiXauthorV1ClausesAlternatesCheck
    intent: Validate alternate clauses
    question: How do I check that the alternate clauses I picked are valid?
  - id: getApiXauthorV1ClausesBundlesByName
    intent: Get a clause bundle by name
    question: Which clauses are packaged inside a named clause bundle?
  - id: getApiXauthorV1ClausesConfigurationsByClauseConfigId
    intent: List alternates and sub-clauses for a configuration
    question: What alternate clauses and sub-clauses belong to a clause configuration?
  phrasing_ops: 4
  slug: conga-clause-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Clause Obligations API from Conga — 3 operation(s) for clause obligations.
  name: Conga Clause Obligations API
  phrasing_intents:
  - id: deleteApiClmV1ClausesByClauseIdObligations
    intent: Delete obligations from a clause
    question: Can I remove several obligations from a clause at once?
  - id: postApiClmV1ClausesByClauseIdObligations
    intent: Create an obligation on a clause
    question: Can I attach a new obligation to a clause in the clause library?
  - id: postApiClmV1ClausesByClauseIdObligationsQuery
    intent: List a clause's obligations
    question: Which obligations are defined on a particular clause?
  - id: deleteApiClmV1ClausesByClauseIdObligationsByObligationId
    intent: Delete one clause obligation
    question: How do I delete a single obligation from a clause by its ID?
  - id: getApiClmV1ClausesByClauseIdObligationsByObligationId
    intent: Get one clause obligation
    question: How do I read the details of a single obligation on a clause?
  - id: putApiClmV1ClausesByClauseIdObligationsByObligationId
    intent: Update a clause obligation
    question: What's the way to edit an obligation that is attached to a clause?
  phrasing_ops: 6
  slug: conga-clause-obligations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for clause semantic comparison
  name: Conga Clause Comparison API
  phrasing_intents:
  - id: postApiXauthorV1ClauseCompare
    intent: Start a semantic clause comparison
    question: How do I check whether a clause in a contract deviates from our standard wording?
  - id: getApiXauthorV1ClauseCompareStatuses
    intent: Check the status of several clause comparisons
    question: Can I check the progress of many clause comparisons in one call?
  - id: getApiXauthorV1ClauseCompareByComparisonIdResults
    intent: Get the results of a clause comparison
    question: Where do I read the outcome of a finished semantic clause comparison?
  - id: getApiXauthorV1ClauseCompareByComparisonIdStatus
    intent: Check the status of one clause comparison
    question: Is my single clause comparison still running or complete?
  phrasing_ops: 4
  slug: conga-clausecomparison-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for clause's content.
  name: Conga Clause Content API
  phrasing_intents:
  - id: postApiXauthorV1ClauseContentMark
    intent: Mark plain text as a clause
    question: How can I turn a passage of plain text in an agreement into a tracked clause?
  - id: postApiXauthorV1ClauseContentMarkupMetadata
    intent: Get encoded clause markup details
    question: Where do I get the markup clause details for a template or agreement in encoded form?
  - id: postApiXauthorV1ClauseContentByClauseId
    intent: Get clause content to insert in a document
    question: How do I pull a library clause's content so I can insert it into a document?
  phrasing_ops: 3
  slug: conga-clausecontent-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for clauses.
  name: Conga Clause Library API
  phrasing_intents:
  - id: postApiXauthorV1ClausesAdvanceQuery
    intent: Filter clauses with an advanced query
    question: Can I filter clauses by arbitrary fields, sort them and group them?
  - id: postApiXauthorV1ClausesPromote
    intent: Promote a marked clause to the clause library
    question: How do I add a clause marked in an agreement into the shared clause library?
  - id: postApiXauthorV1ClausesQuery
    intent: Browse clauses in the clause library
    question: Which reusable clauses in the library fit a given category and locale?
  phrasing_ops: 3
  slug: conga-clauselibrary-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for template clause metadata
  name: Conga Clause Metadata API
  phrasing_intents:
  - id: getApiXauthorV1ClausesMarkMetadataByContractId
    intent: Get marked clause metadata for a contract
    question: How do I see metadata for the clauses marked in a specific contract?
  - id: getApiXauthorV1ClausesMetadata
    intent: Get template clause metadata
    question: Where do I find metadata for the clauses in a template?
  phrasing_ops: 2
  slug: conga-clausemetadata-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for clause's version-related operations.
  name: Conga Clause Version API
  phrasing_intents:
  - id: getApiXauthorV1ClausesByClauseIdVersionsByClauseVersionIdRichtextContent
    intent: Get a clause version's content as text or HTML
    question: How do I read the rich text of a specific clause version in Conga?
  phrasing_ops: 1
  slug: conga-clauseversion-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Clone API from Conga — 3 operation(s) for clone.
  name: Conga Clone API
  phrasing_intents:
  - id: getCloneStatusById
    intent: Check the status of a deep clone job
    question: Has my deep clone job in Conga finished?
  - id: getCloneByObjectNameSupportedObjects
    intent: List related objects that can be cloned
    question: Which related records get copied along when I clone an object?
  - id: postByObjectNameByObjectIdClone
    intent: Clone a record
    question: How do I duplicate an existing record in Conga?
  phrasing_ops: 3
  slug: conga-clone-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Collaboration Request Controller
  name: Conga Collaboration Request API
  phrasing_intents:
  - id: getApiCartV1CartsCollaborationRequest
    intent: List collaboration requests
    question: Which cart collaboration requests are open in Conga CPQ?
  - id: deleteApiCartV1CartsCollaborationRequestById
    intent: Cancel a collaboration request
    question: How do I cancel a collaboration request I no longer need?
  - id: getApiCartV1CartsCollaborationRequestById
    intent: Get a collaboration request
    question: What are the details of one specific collaboration request?
  - id: patchApiCartV1CartsCollaborationRequestById
    intent: Update a collaboration request
    question: Can I change the due date or priority of an existing collaboration request?
  - id: postApiCartV1CartsByCartIdCollaborationRequest
    intent: Create a collaboration request on a cart
    question: How do I ask a colleague to collaborate on some line items of my cart?
  - id: postApiCartV1CartsByCartIdCollaborationRequestByIdMerge
    intent: Merge a collaboration request into its cart
    question: How do I bring a collaborator's changes back into the parent cart?
  - id: postApiCartV1CartsByCartIdCollaborationRequestByIdSubmitForMerge
    intent: Submit a collaboration request for merge
    question: As a collaborator, how do I hand my finished work back for merging?
  phrasing_ops: 7
  slug: conga-collaborationrequest-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Complex Field Definition API from Conga — 3 operation(s) for complex field definition.
  name: Conga Complex Field Definition API
  phrasing_intents:
  - id: postApiSchemaV1ObjectsByObjectNameComplexFieldByComplexFieldMetadataName
    intent: Create one complex field
    question: How do I add a single new complex field under existing complex field metadata?
  - id: putApiSchemaV1ObjectsByObjectNameComplexFieldByComplexFieldMetadataName
    intent: Update a complex field definition
    question: How do I change an existing complex field definition on an object?
  - id: postApiSchemaV1ObjectsByObjectNameComplexFields
    intent: Create complex field metadata
    question: How do I define new complex field metadata for an object?
  - id: postApiSchemaV1ObjectsByObjectNameComplexFieldsByComplexFieldMetadataName
    intent: Create several complex fields at once
    question: Can I create multiple complex fields under the same metadata in one request?
  phrasing_ops: 4
  slug: conga-complex-field-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ComposerParameter API from Conga — 2 operation(s) for composerparameter.
  name: Conga Composer Parameter API
  phrasing_intents:
  - id: ComposerParameter_GetAllParameters
    intent: List Composer parameters
    question: Which Composer parameters are available?
  - id: ComposerParameter_GetParameterById
    intent: Get a Composer parameter
    question: What does a specific Composer parameter do?
  phrasing_ops: 2
  slug: conga-composerparameter-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ComprehensiveHealthCheck API from Conga — 1 operation(s) for comprehensivehealthcheck.
  name: Conga Comprehensive Health Check API
  phrasing_intents:
  - id: ComprehensiveHealthCheck_CheckComprehensiveHealth
    intent: Run a comprehensive service health check
    question: Is the e-signature service fully healthy right now?
  phrasing_ops: 1
  slug: conga-comprehensivehealthcheck-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Configuration API from Conga — 10 operation(s) for configuration.
  name: Conga Configuration API
  phrasing_intents:
  - id: postApiConfigManagementV1Configurations
    intent: Add a new configuration
    question: How do I add a brand-new configuration entry to the platform?
  - id: putApiConfigManagementV1Configurations
    intent: Update an existing configuration value
    question: How do I change the value of a configuration setting that already exists?
  - id: getApiConfigManagementV1ConfigurationsCategories
    intent: List configuration categories
    question: What configuration categories are available?
  - id: postApiConfigManagementV1ConfigurationsExport
    intent: Export custom configuration as a zip
    question: How can I export my custom configuration to move it to another environment?
  - id: postApiConfigManagementV1ConfigurationsImport
    intent: Import custom configuration from a zip
    question: How do I load a configuration zip exported from another environment?
  - id: getApiConfigManagementV1ConfigurationsByCategory
    intent: List all configurations in a category
    question: Which configurations belong to the eSign category?
  - id: postApiConfigManagementV1ConfigurationsByCategory
    intent: Fetch several named configurations at once
    question: Can I fetch a handful of specific configuration names from a category in one request?
  - id: deleteApiConfigManagementV1ConfigurationsByCategoryByName
    intent: Delete a configuration
    question: Can I remove a configuration setting I no longer need?
  phrasing_ops: 14
  slug: conga-configuration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Configurations API from Conga — 1 operation(s) for configurations.
  name: Conga Configurations API
  phrasing_intents:
  - id: getApiClmV1ConfigurationsCategoryByCategoryNameByName
    intent: Get a CLM configuration setting
    question: How do I read a Conga CLM configuration setting by category and name?
  phrasing_ops: 1
  slug: conga-configurations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Conga Hooks API from Conga — 4 operation(s) for conga hooks.
  name: Conga Hooks API
  phrasing_intents:
  - id: getApiExtensibilityV1ServicehooksDatachangerules
    intent: List data change rules
    question: Which service hook data change rules are configured in my Conga org?
  - id: postApiExtensibilityV1ServicehooksDatachangerules
    intent: Create a data change rule
    question: How do I set up a service hook that runs custom code when an object's data changes?
  - id: getApiExtensibilityV1ServicehooksDatachangerulesCancellationSettings
    intent: View service hook cancellation settings
    question: What's the current cancellation token timeout configured for service hooks?
  - id: putApiExtensibilityV1ServicehooksDatachangerulesCancellationSettings
    intent: Set service hook cancellation timeout
    question: How do I change how long a service hook can run before it's aborted?
  - id: getApiExtensibilityV1ServicehooksDatachangerulesSupportedEventTypes
    intent: List supported service hook event types
    question: Which event types can a data change rule listen for?
  - id: deleteApiExtensibilityV1ServicehooksDatachangerulesByName
    intent: Delete a data change rule
    question: How do I remove a service hook data change rule I no longer need?
  - id: getApiExtensibilityV1ServicehooksDatachangerulesByName
    intent: Get a data change rule by name
    question: How do I view the details of one data change rule?
  - id: putApiExtensibilityV1ServicehooksDatachangerulesByName
    intent: Update a data change rule
    question: How do I change the condition or event types on an existing data change rule?
  phrasing_ops: 8
  slug: conga-conga-hooks-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Conga Hooks Rules API from Conga — 4 operation(s) for conga hooks rules.
  name: Conga Hooks Rules API
  phrasing_intents:
  - id: getApiExtensibilityV1ServicehooksRules
    intent: List service hook rules
    question: Which service hook rules are set up in my Conga platform?
  - id: postApiExtensibilityV1ServicehooksRules
    intent: Create a service hook rule
    question: How do I run custom code automatically when a record changes?
  - id: getApiExtensibilityV1ServicehooksRulesCancellationSettings
    intent: Get the service hook cancellation timeout setting
    question: What abort timeout is configured for service hook executions?
  - id: putApiExtensibilityV1ServicehooksRulesCancellationSettings
    intent: Set the service hook cancellation timeout
    question: How do I change how long a service hook can run before it is aborted?
  - id: getApiExtensibilityV1ServicehooksRulesSupportedEventTypes
    intent: List supported service hook event types
    question: Which events can a service hook rule be triggered by?
  - id: deleteApiExtensibilityV1ServicehooksRulesByName
    intent: Delete a service hook rule
    question: How do I remove a service hook rule I no longer want?
  - id: getApiExtensibilityV1ServicehooksRulesByName
    intent: Get a service hook rule by name
    question: What condition and events does a particular service hook rule use?
  - id: patchApiExtensibilityV1ServicehooksRulesByName
    intent: Update a service hook rule
    question: Can I deactivate a service hook rule without deleting it?
  phrasing_ops: 8
  slug: conga-conga-hooks-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Send transaction using Conga Sign
  name: Conga Sign API
  phrasing_intents:
  - id: postApiEsignV1CongasignSend
    intent: Create and send a Conga Sign transaction
    question: How do I send documents out for signature with Conga Sign?
  phrasing_ops: 1
  slug: conga-congasign-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Constraint Rule Actions API from Conga — 5 operation(s) for constraint rule actions.
  name: Conga Constraint Rule Actions API
  phrasing_intents:
  - id: getConstraintRuleActionsByIdFieldExpressions
    intent: Get lookup records for a field expression
    question: How do I see the lookup records behind a constraint rule action's field expression?
  - id: deleteConstraintRuleActionsByParentIdConstraintRuleActionExpressions
    intent: Delete several expressions from a rule action
    question: How do I remove a batch of action expressions from a rule action?
  - id: getConstraintRuleActionsByParentIdConstraintRuleActionExpressions
    intent: List expressions on a constraint rule action
    question: Which action expressions belong to a constraint rule action?
  - id: patchConstraintRuleActionsByParentIdConstraintRuleActionExpressions
    intent: Update several expressions on a rule action
    question: Can I edit fields on many action expressions of one rule action together?
  - id: postConstraintRuleActionsByParentIdConstraintRuleActionExpressions
    intent: Add expressions to a constraint rule action
    question: How do I create action expressions inside a constraint rule action?
  - id: deleteConstraintRuleActionsByParentIdConstraintRuleActionExpressionsById
    intent: Delete one expression from a rule action
    question: How do I delete just one action expression from a rule action?
  - id: getConstraintRuleActionsByParentIdConstraintRuleActionExpressionsById
    intent: Get one expression on a rule action
    question: How do I view a single action expression on a constraint rule action?
  - id: patchConstraintRuleActionsByParentIdConstraintRuleActionExpressionsById
    intent: Update one expression on a rule action
    question: How do I change fields on a single rule action expression?
  phrasing_ops: 15
  slug: conga-constraint-rule-actions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Constraint Rule Conditions API from Conga — 2 operation(s) for constraint rule conditions.
  name: Conga Constraint Rule Conditions API
  phrasing_intents:
  - id: deleteConstraintRulesByParentIdConditions
    intent: Delete several conditions from a constraint rule
    question: How do I remove multiple conditions from a constraint rule at once?
  - id: getConstraintRulesByParentIdConditions
    intent: List conditions in a constraint rule
    question: Which conditions are defined on a constraint rule?
  - id: patchConstraintRulesByParentIdConditions
    intent: Update several conditions in a constraint rule
    question: Can I edit fields on many constraint rule conditions together?
  - id: postConstraintRulesByParentIdConditions
    intent: Add conditions to a constraint rule
    question: How do I create new conditions on a constraint rule?
  - id: deleteConstraintRulesByParentIdConditionsById
    intent: Delete one condition from a constraint rule
    question: How do I delete a single condition from a constraint rule?
  - id: getConstraintRulesByParentIdConditionsById
    intent: Get one condition in a constraint rule
    question: How do I view a single condition on a constraint rule?
  - id: patchConstraintRulesByParentIdConditionsById
    intent: Update one condition in a constraint rule
    question: How do I change a single condition on a constraint rule?
  phrasing_ops: 7
  slug: conga-constraint-rule-conditions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Constraint Rules API from Conga — 2 operation(s) for constraint rules.
  name: Conga Constraint Rules API
  phrasing_intents:
  - id: deleteConstraintRules
    intent: Delete constraint rules in bulk
    question: How many constraint rules can I delete in a single call?
  - id: getConstraintRules
    intent: List constraint rules
    question: Which product constraint rules are configured?
  - id: patchConstraintRules
    intent: Update constraint rules in bulk
    question: Can I change fields on many constraint rules together?
  - id: postConstraintRules
    intent: Create constraint rules in bulk
    question: How do I create up to 1000 constraint rules in one request?
  - id: deleteConstraintRulesById
    intent: Delete a constraint rule
    question: How do I delete one specific constraint rule?
  - id: getConstraintRulesById
    intent: Get a constraint rule
    question: How do I look up one constraint rule by its ID?
  - id: patchConstraintRulesById
    intent: Update a constraint rule
    question: How do I change fields on a single constraint rule?
  phrasing_ops: 7
  slug: conga-constraint-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for CRUD operations on usage inputs, supporting rating, unrating, and draft rating in synchronous and asynchronous modes.
  name: Conga Consumption Billing API
  phrasing_intents:
  - id: deleteUsageInputs
    intent: Delete usage input records
    question: How do I remove usage input records I loaded by mistake?
  - id: getUsageInputs
    intent: List usage input records
    question: Where can I see all the usage inputs loaded for consumption billing?
  - id: patchUsageInputs
    intent: Update usage input records
    question: Can I correct fields on several usage inputs at once?
  - id: postUsageInputs
    intent: Load usage input records
    question: How do I add usage records so Conga can bill customers for consumption?
  - id: postUsageInputsEstimate
    intent: Estimate ratings for usage inputs
    question: Can I preview what usage inputs would be rated at without saving anything?
  - id: postUsageInputsRate
    intent: Rate usage input records
    question: How do I rate usage inputs so they're ready to bill?
  - id: postUsageInputsUnrate
    intent: Reverse ratings on usage inputs
    question: How do I undo the rating on usage inputs that were rated incorrectly?
  - id: getUsageInputsByUsageInputId
    intent: Get a usage input record
    question: How do I look up one usage input by its ID?
  phrasing_ops: 8
  slug: conga-consumption-billing-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contact API from Conga — 8 operation(s) for contact.
  name: Conga Contact API
  phrasing_intents:
  - id: getApiDataV1Contact
    intent: List contact records
    question: Where can I see all contacts stored in Conga?
  - id: postApiDataV1Contact
    intent: Create a contact
    question: How do I add a single new contact with name and email?
  - id: deleteApiDataV1ContactBulk
    intent: Delete many contacts at once
    question: Can a batch of contact records be removed together?
  - id: patchApiDataV1ContactBulk
    intent: Upsert many contacts
    question: Can I insert new contacts and update existing ones in the same call?
  - id: postApiDataV1ContactBulk
    intent: Create many contacts at once
    question: Is it possible to insert a list of new contacts in a single call?
  - id: putApiDataV1ContactBulk
    intent: Update many contacts at once
    question: Can I update a batch of existing contacts in one request?
  - id: deleteApiDataV1ContactByExternalIdByExternalId
    intent: Delete a contact by external ID
    question: How do I delete a contact using its external identifier?
  - id: getApiDataV1ContactByExternalIdByExternalId
    intent: Get a contact by external ID
    question: Which contact matches the ID from my other system?
  phrasing_ops: 16
  slug: conga-contact-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contact Users API from Conga — 3 operation(s) for contact users.
  name: Conga Contact Users API
  phrasing_intents:
  - id: postApiUserManagementV1ContactUsers
    intent: Create a user for a contact
    question: Can I give an external contact a user login mapped to their contact record?
  - id: deleteApiUserManagementV1ContactUsersByUserId
    intent: Deactivate a contact user
    question: How do I deactivate a contact user's access?
  - id: putApiUserManagementV1ContactUsersByUserId
    intent: Update a contact user
    question: Can I change a contact user's timezone or locale?
  - id: putApiUserManagementV1ContactUsersByUserIdRestore
    intent: Reactivate a contact user
    question: Can I bring back a contact user I deactivated earlier?
  phrasing_ops: 4
  slug: conga-contact-users-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract API from Conga — 4 operation(s) for contract.
  name: Conga Contract API
  phrasing_intents:
  - id: deleteApiClmV1Contracts
    intent: Delete several contracts permanently
    question: Can I permanently delete a whole list of contracts at once?
  - id: postApiClmV1Contracts
    intent: Create a contract record
    question: How do I create a new contract record in Conga CLM?
  - id: postApiClmV1ContractsQuery
    intent: Search contract records
    question: Which contracts match a set of criteria I define?
  - id: deleteApiClmV1ContractsByContractId
    intent: Delete a contract permanently
    question: How do I permanently remove a single contract?
  - id: getApiClmV1ContractsByContractId
    intent: Get a contract's details
    question: What are all the field values, including custom fields, on a particular contract?
  - id: putApiClmV1ContractsByContractId
    intent: Update a contract record
    question: Can I change the account, owner or custom fields on an existing contract?
  - id: putApiClmV1ContractsByContractIdSignstatus
    intent: Set a contract's signature status
    question: Can I mark a contract as signed, declined or out for signature?
  phrasing_ops: 7
  slug: conga-contract-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Clause API from Conga — 6 operation(s) for contract clause.
  name: Conga Contract Clause API
  phrasing_intents:
  - id: getApiClmV1ContractsClausesByContractClauseId
    intent: Get a contract clause's details
    question: What text and status does a particular contract clause have?
  - id: postApiClmV1ContractsByContractIdClause
    intent: Add a clause to a contract
    question: How do I add a single new clause to a contract?
  - id: putApiClmV1ContractsByContractIdClauseByContractClauseId
    intent: Update a clause on a contract
    question: How do I edit one clause that's already on a contract?
  - id: postApiClmV1ContractsByContractIdClauses
    intent: List the clauses of a contract
    question: Which clauses are in a contract, grouped by document version?
  - id: deleteApiClmV1ContractsByContractIdClausesBulk
    intent: Delete many clauses from a contract
    question: Can I remove several clauses from a contract in a single call?
  - id: postApiClmV1ContractsByContractIdClausesBulk
    intent: Add many clauses to a contract
    question: How can I create a batch of clauses on a contract together?
  - id: putApiClmV1ContractsByContractIdClausesBulk
    intent: Update many clauses of a contract
    question: Can I update several contract clauses in one request?
  - id: deleteApiClmV1ContractsByContractIdClausesByContractClauseId
    intent: Delete one clause from a contract
    question: How do I remove a single clause from a contract?
  phrasing_ops: 8
  slug: conga-contract-clause-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Cycle Time API from Conga — 4 operation(s) for contract cycle time.
  name: Conga Contract Cycle Time API
  phrasing_intents:
  - id: postApiClmV1Cycletimes
    intent: Create a cycle-time group
    question: How do I define a new cycle-time group that measures time between two contract field values?
  - id: getApiClmV1CycletimesContractfields
    intent: List contract fields for cycle-time tracking
    question: Which contract fields can be used when building a cycle-time group?
  - id: getApiClmV1CycletimesDashboard
    intent: Get cycle-time dashboard data
    question: How long have contracts spent in each status over the past 12 months?
  - id: deleteApiClmV1CycletimesByCycleTimeGroupId
    intent: Delete a cycle-time group
    question: How do I remove a cycle-time group I no longer need?
  - id: getApiClmV1CycletimesByCycleTimeGroupId
    intent: Get a cycle-time group
    question: What's configured on one particular cycle-time group?
  - id: putApiClmV1CycletimesByCycleTimeGroupId
    intent: Update a cycle-time group
    question: Can I change the start and end values a cycle-time group measures?
  phrasing_ops: 6
  slug: conga-contract-cycle-time-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Documents API from Conga — 15 operation(s) for contract documents.
  name: Conga Contract Documents API
  phrasing_intents:
  - id: postApiClmV1ContractsCreateoffline
    intent: Create a contract from third-party paper
    question: How do I bring a counterparty's contract document into Conga CLM as a new contract?
  - id: postApiClmV1ContractsCreateofflineLarge
    intent: Create a contract from a large third-party file
    question: What if the third-party contract file is too big to upload directly?
  - id: postApiClmV1ContractsStoreexecuted
    intent: Create an activated contract from a signed document
    question: How do I record a contract that is already signed so it goes straight to Activated?
  - id: postApiClmV1ContractsStoreexecutedLarge
    intent: Store a large executed contract document
    question: Can I store a large signed contract file that is already in the filestore?
  - id: deleteApiClmV1ContractsByContractIdDocuments
    intent: Delete documents from a contract
    question: Can I wipe every document attached to a contract at once?
  - id: postApiClmV1ContractsByContractIdDocuments
    intent: Add a document to an existing contract
    question: How do I upload a new document onto a contract that already exists?
  - id: postApiClmV1ContractsByContractIdDocumentsLarge
    intent: Attach a large document to a contract
    question: How do I add a very large file to an existing contract?
  - id: postApiClmV1ContractsByContractIdDocumentsQuery
    intent: Search a contract's documents
    question: Can I search the documents on a contract with my own criteria?
  phrasing_ops: 17
  slug: conga-contract-documents-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Lifecycle API from Conga — 9 operation(s) for contract lifecycle.
  name: Conga Contract Lifecycle API
  phrasing_intents:
  - id: postApiClmV1ContractsByContractIdActivate
    intent: Activate a signed contract
    question: How do I bring a fully signed contract into effect?
  - id: postApiClmV1ContractsByContractIdAmend
    intent: Amend a contract
    question: Can I modify a contract's terms mid-term by creating an amended version?
  - id: postApiClmV1ContractsByContractIdCancel
    intent: Cancel a contract
    question: Which contract statuses allow a contract to be canceled?
  - id: postApiClmV1ContractsByContractIdClone
    intent: Clone a contract
    question: Can I copy an existing contract into a new version without changing the original?
  - id: postApiClmV1ContractsByContractIdExpire
    intent: Expire a contract
    question: How do I mark a contract as expired when its term ends?
  - id: postApiClmV1ContractsByContractIdRenew
    intent: Renew a contract
    question: Can I renew a contract at the end of its term?
  - id: postApiClmV1ContractsByContractIdSubmitrequest
    intent: Submit a contract request for processing
    question: How does a contract get sent through the steps in its agreement rule?
  - id: postApiClmV1ContractsByContractIdTerminate
    intent: Terminate an active contract
    question: Can I terminate an executed contract early?
  phrasing_ops: 9
  slug: conga-contract-lifecycle-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Obligations API from Conga — 6 operation(s) for contract obligations.
  name: Conga Contract Obligations API
  phrasing_intents:
  - id: postApiClmV1ContractsByContractIdObligationFulfillments
    intent: Get a contract's obligations and fulfillments
    question: Which obligations on a contract have been fulfilled, with their documents?
  - id: deleteApiClmV1ContractsByContractIdObligations
    intent: Delete obligations from a contract
    question: Can I delete all obligations on a contract at once?
  - id: postApiClmV1ContractsByContractIdObligations
    intent: Create an obligation on a contract
    question: How do I add a new obligation to a contract?
  - id: postApiClmV1ContractsByContractIdObligationsQuery
    intent: List a contract's obligations
    question: Which obligations are tracked against a given contract?
  - id: deleteApiClmV1ContractsByContractIdObligationsByObligationId
    intent: Delete one contract obligation
    question: How do I delete a single obligation from a contract?
  - id: getApiClmV1ContractsByContractIdObligationsByObligationId
    intent: Get one contract obligation
    question: What are the details of a specific obligation on a contract?
  - id: putApiClmV1ContractsByContractIdObligationsByObligationId
    intent: Update a contract obligation
    question: How do I change the due date or details of a contract obligation?
  - id: postApiClmV1ContractsByContractIdObligationsByObligationIdDocuments
    intent: Upload a document to a contract obligation
    question: How do I attach proof of fulfillment to a contract obligation?
  phrasing_ops: 10
  slug: conga-contract-obligations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Obligations Fulfillment API from Conga — 6 operation(s) for contract obligations fulfillment.
  name: Conga Contract Obligations Fulfillment API
  phrasing_intents:
  - id: postApiClmV1ContractsObligationsFulfillmentsQuery
    intent: List active obligation fulfillments across contracts
    question: Which obligation fulfillments are still pending or overdue across all my contracts?
  - id: postApiClmV1ContractsByContractIdObligationsByObligationIdActivityhistoryQuery
    intent: Get activity history across an obligation's fulfillments
    question: Who acted on the fulfillments of a contract obligation, and when?
  - id: postApiClmV1ContractsByContractIdObligationsByObligationIdFulfillmentsQuery
    intent: List fulfillments for a contract obligation
    question: What fulfillment records exist for one obligation on a contract?
  - id: getApiClmV1ContractsByContractIdObligationsByObligationIdFulfillmentsByFulfillmentId
    intent: Get a contract obligation fulfillment
    question: What are the details of one specific obligation fulfillment?
  - id: putApiClmV1ContractsByContractIdObligationsByObligationIdFulfillmentsByFulfillmentId
    intent: Update a contract obligation fulfillment
    question: Can I edit field values on an existing obligation fulfillment?
  - id: postApiClmV1ContractsByContractIdObligationsByObligationIdFulfillmentsByFulfillmentIdHistoryQuery
    intent: Get the history of one fulfillment
    question: What changes have been made to one particular obligation fulfillment?
  - id: postApiClmV1ContractsByContractIdObligationsByObligationIdFulfillmentsByFulfillmentIdByFulfillmentAction
    intent: Perform an action on an obligation fulfillment
    question: How do I mark an obligation fulfillment as fulfilled with a date and comments?
  phrasing_ops: 7
  slug: conga-contract-obligations-fulfillment-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Related List API from Conga — 3 operation(s) for contract related list.
  name: Conga Contract Related List API
  phrasing_intents:
  - id: deleteApiClmV1ContractsByContractIdByObjectName
    intent: Delete related records from a contract
    question: How do I remove several related list records from a contract?
  - id: postApiClmV1ContractsByContractIdByObjectName
    intent: Create related records on a contract
    question: How do I add new related list records to a contract?
  - id: putApiClmV1ContractsByContractIdByObjectName
    intent: Update several related records on a contract
    question: How do I bulk-update related list records on a contract?
  - id: postApiClmV1ContractsByContractIdByObjectNameQuery
    intent: Query related records on a contract
    question: How do I filter and sort a contract's related list records?
  - id: deleteApiClmV1ContractsByContractIdByObjectNameByObjectId
    intent: Delete one related record from a contract
    question: How do I delete a single related record from a contract?
  - id: getApiClmV1ContractsByContractIdByObjectNameByObjectId
    intent: Get one related record on a contract
    question: How do I see the details of one specific related record on a contract?
  - id: putApiClmV1ContractsByContractIdByObjectNameByObjectId
    intent: Update one related record on a contract
    question: How do I change a single related record on a contract?
  phrasing_ops: 7
  slug: conga-contract-related-list-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Relationship API from Conga — 5 operation(s) for contract relationship.
  name: Conga Contract Relationship API
  phrasing_intents:
  - id: getApiClmV1ContractsByContractIdHierarchy
    intent: Get a contract's hierarchy of child contracts
    question: Which child and descendant contracts sit under a parent contract?
  - id: getApiClmV1ContractsByContractIdRelationships
    intent: Get a contract's relationship details
    question: Is a contract linked to any amendments or renewals?
  - id: postApiClmV1ContractsByContractIdRelationships
    intent: Link a contract as amendment or renewal of another
    question: How do I mark one contract as an amendment or renewal of another?
  - id: postApiClmV1ContractsByContractIdRelationshipsLink
    intent: Link two contracts with from and to relationship types
    question: Can I set both directions of a contract relationship explicitly when linking?
  - id: postApiClmV1ContractsByContractIdRelationshipsQuery
    intent: Search a contract's related contracts
    question: Can I get a sorted list of the contracts related to one contract?
  - id: deleteApiClmV1ContractsByContractIdRelationshipsByRelationshipId
    intent: Unlink two related contracts
    question: How do I remove the link between two contracts?
  phrasing_ops: 6
  slug: conga-contract-relationship-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Request API from Conga — 7 operation(s) for contract request.
  name: Conga Contract Request API
  phrasing_intents:
  - id: postApiClmV1Requests
    intent: Create a contract request
    question: How do I submit a new contract request in Conga CLM?
  - id: postApiClmV1RequestsIncomingRequests
    intent: List incoming requests awaiting my approval
    question: Which contract requests are waiting for me or my groups to approve?
  - id: postApiClmV1RequestsQuery
    intent: Search contract requests
    question: Can I search all contract request records with custom criteria?
  - id: postApiClmV1RequestsByContractRequestIdConvert
    intent: Convert a contract request to an agreement
    question: How do I turn an approved contract request into an agreement?
  - id: deleteApiClmV1RequestsById
    intent: Delete a contract request
    question: How do I permanently remove a contract request?
  - id: getApiClmV1RequestsById
    intent: Get a contract request
    question: What are the details of a specific contract request?
  - id: putApiClmV1RequestsById
    intent: Update a contract request
    question: Can I edit an existing contract request's fields?
  - id: getApiClmV1RequestsByIdActionEligibility
    intent: Check my authority on a contract request
    question: Am I allowed to approve, reject or convert a given contract request?
  phrasing_ops: 11
  slug: conga-contract-request-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Request Team Members API from Conga — 4 operation(s) for contract request team members.
  name: Conga Contract Request Team Members API
  phrasing_intents:
  - id: postApiClmV1RequestsByContractRequestIdTeammembers
    intent: Add team members to a contract request
    question: How do I add people to a contract request team and give them a role?
  - id: getApiClmV1RequestsByContractRequestIdTeammembersByActionByActionName
    intent: Get team members for a contract action
    question: Which team members on a contract request are tied to a specific action?
  - id: postApiClmV1RequestsByContractRequestIdTeammembersQuery
    intent: List team members on a contract request
    question: Who is on the team for a contract request?
  - id: deleteApiClmV1RequestsByContractRequestIdTeammembersByTeamMemberId
    intent: Remove a team member from a contract request
    question: How do I take someone off a contract request team?
  - id: getApiClmV1RequestsByContractRequestIdTeammembersByTeamMemberId
    intent: Get a contract request team member
    question: How do I see one team member's details and role on a contract request?
  - id: putApiClmV1RequestsByContractRequestIdTeammembersByTeamMemberId
    intent: Update a contract request team member
    question: How do I change a team member's role on a contract request?
  phrasing_ops: 6
  slug: conga-contract-request-team-members-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Contract Team Members API from Conga — 4 operation(s) for contract team members.
  name: Conga Contract Team Members API
  phrasing_intents:
  - id: postApiClmV1ContractsByContractIdTeammembers
    intent: Add team members to a contract
    question: How do I add people to a contract's team with a team role?
  - id: getApiClmV1ContractsByContractIdTeammembersByActionByActionName
    intent: List contract team members for an action
    question: Which team members on a contract are tied to a specific action?
  - id: postApiClmV1ContractsByContractIdTeammembersQuery
    intent: List all team members of a contract
    question: Who is on the team for a contract?
  - id: deleteApiClmV1ContractsByContractIdTeammembersByTeamMemberId
    intent: Remove a team member from a contract
    question: How do I take someone off a contract's team?
  - id: getApiClmV1ContractsByContractIdTeammembersByTeamMemberId
    intent: Get a contract team member
    question: What role does a specific team member have on a contract?
  - id: putApiClmV1ContractsByContractIdTeammembersByTeamMemberId
    intent: Update a contract team member
    question: How do I change a team member's role on a contract?
  phrasing_ops: 6
  slug: conga-contract-team-members-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for managing Contract Type Document Requirement Settings
  name: Conga Contract Type Document Requirement Settings API
  phrasing_intents:
  - id: getApiClmV1SettingsDocumentsContractTypeRequirements
    intent: Get document requirements for a contract type
    question: Which documents are required for a contract type when a given action happens?
  - id: putApiClmV1SettingsDocumentsContractTypeRequirements
    intent: Update document requirement settings
    question: Can I change existing document requirement settings in bulk?
  - id: postApiClmV1SettingsDocumentsContractTypeRequirementsQuery
    intent: Query document requirement settings
    question: How do I search document requirement settings with sorting and paging?
  - id: getApiClmV1SettingsDocumentsContractTypeRequirementsById
    intent: Get one document requirement setting
    question: What does a single document requirement setting contain?
  phrasing_ops: 4
  slug: conga-contract-type-document-requirement-settings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs related to agreement document checkins
  name: Conga Contract Checkin API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdCheckIn
    intent: Check in a contract document
    question: What happens after I check a contract document back in, like reconciliation or PDF creation?
  phrasing_ops: 1
  slug: conga-contractcheckin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides endpoints for managing conversation threads.
  name: Conga Conversation Thread API
  phrasing_intents:
  - id: postApiClmV1ConversationThreadsQuery
    intent: Search conversation threads
    question: How do I find conversation threads on contracts in Conga CLM?
  phrasing_ops: 1
  slug: conga-conversation-thread-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: API controller for managing credit memo operations.
  name: Conga Credit Memos API
  phrasing_intents:
  - id: postCreditmemosApprove
    intent: Approve credit memos
    question: How do I approve draft or pending credit memos in bulk?
  - id: postCreditmemosCancel
    intent: Cancel credit memos
    question: How do I cancel approved credit memos that haven't been credited yet?
  - id: getCreditmemosById
    intent: Get credit memo details
    question: How do I view a credit memo I already created?
  phrasing_ops: 3
  slug: conga-credit-memos-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Currency Admin API from Conga — 3 operation(s) for currency admin.
  name: Conga Currency Admin API
  phrasing_intents:
  - id: getApiCurrencyManagementV1CurrencyRates
    intent: List currency rates
    question: Which currency conversion rates are configured?
  - id: postApiCurrencyManagementV1CurrencyRates
    intent: Add a currency rate
    question: How do I add a new exchange rate between two currencies?
  - id: postApiCurrencyManagementV1CurrencyRatesBulk
    intent: Add many currency rates
    question: How do I load a whole set of new exchange rates in one call?
  - id: putApiCurrencyManagementV1CurrencyRatesBulk
    intent: Update many currency rates
    question: Can I update a batch of currency rates at once?
  - id: deleteApiCurrencyManagementV1CurrencyRatesById
    intent: Delete a currency rate
    question: How do I delete an exchange rate I no longer use?
  - id: getApiCurrencyManagementV1CurrencyRatesById
    intent: Get a currency rate
    question: What is the stored conversion rate for a particular rate record?
  - id: putApiCurrencyManagementV1CurrencyRatesById
    intent: Update a currency rate
    question: Can I correct a single exchange rate?
  phrasing_ops: 7
  slug: conga-currency-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Currency API from Conga — 1 operation(s) for currency.
  name: Conga Currency API
  phrasing_intents:
  - id: getApiDataV1Currencies
    intent: List available currencies
    question: Which currencies are set up in my Conga org?
  phrasing_ops: 1
  slug: conga-currency-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Currency Format API from Conga — 1 operation(s) for currency format.
  name: Conga Currency Format API
  phrasing_intents:
  - id: getApiUserManagementV1CurrencyFormats
    intent: List currency formats
    question: Which currency formats are available for users in Conga?
  phrasing_ops: 1
  slug: conga-currency-format-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Currency Runtime API from Conga — 3 operation(s) for currency runtime.
  name: Conga Currency Runtime API
  phrasing_intents:
  - id: postApiCurrencyManagementV1QueryCurrencyConversion
    intent: Convert an amount between currencies
    question: What is a given amount worth in another currency on a specific date?
  - id: postApiCurrencyManagementV1QueryCurrencyRates
    intent: Get the effective rate for a currency pair
    question: Which exchange rate is in effect between two currencies today?
  - id: postApiCurrencyManagementV1QueryCurrencyRatesBulk
    intent: Get effective rates for many currency pairs
    question: Can I look up effective exchange rates for several currency pairs at once?
  phrasing_ops: 3
  slug: conga-currency-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Custom Code API from Conga — 14 operation(s) for custom code.
  name: Conga Custom Code API
  phrasing_intents:
  - id: getApiExtensibilityV1Customcode
    intent: List all custom code projects
    question: Which custom code projects are deployed in my Conga platform?
  - id: postApiExtensibilityV1CustomcodeExecute
    intent: Run a custom code method
    question: How do I invoke a method in one of my custom code projects on demand?
  - id: postApiExtensibilityV1CustomcodeMigrationExportByType
    intent: Export custom code projects or resources
    question: How do I export custom code projects to move them to another org?
  - id: postApiExtensibilityV1CustomcodeMigrationImportByType
    intent: Import custom code projects or resources
    question: How do I bring exported custom code projects into this org?
  - id: getApiExtensibilityV1CustomcodeTrustedApis
    intent: List trusted API configurations
    question: Which external APIs is custom code allowed to call?
  - id: postApiExtensibilityV1CustomcodeTrustedApis
    intent: Add a trusted API configuration
    question: How do I allow custom code to call a new external endpoint?
  - id: getApiExtensibilityV1CustomcodeTrustedApisAllowedHttpVerbs
    intent: List HTTP verbs allowed for trusted APIs
    question: What HTTP methods can a trusted API configuration permit?
  - id: getApiExtensibilityV1CustomcodeTrustedApisUri
    intent: Find a trusted API configuration by URI
    question: Is a given endpoint URL already registered as a trusted API?
  phrasing_ops: 21
  slug: conga-custom-code-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Custom Object API from Conga — 9 operation(s) for custom object.
  name: Conga Custom Object API
  phrasing_intents:
  - id: postApiDataV1CustomObjectsQueryParallel
    intent: Run several custom object queries in parallel
    question: Can I send multiple custom object queries in one request and get each result back?
  - id: postApiDataV1CustomObjectsQueryByObjectName
    intent: Query a custom object's records
    question: How do I query records of one custom object with criteria, sorting and grouping?
  - id: getApiDataV1CustomObjectsByObjectName
    intent: List all records of a custom object
    question: What records exist in a given custom object?
  - id: postApiDataV1CustomObjectsByObjectName
    intent: Insert one custom object record
    question: How do I add a single new record to a custom object?
  - id: deleteApiDataV1CustomObjectsByObjectNameBulk
    intent: Delete many custom object records
    question: Can I remove a list of records from a custom object in one request?
  - id: patchApiDataV1CustomObjectsByObjectNameBulk
    intent: Upsert custom object records
    question: Can I insert new records and update existing ones in a single call?
  - id: postApiDataV1CustomObjectsByObjectNameBulk
    intent: Insert many custom object records
    question: Can I create a batch of records in a custom object at once?
  - id: putApiDataV1CustomObjectsByObjectNameBulk
    intent: Update many custom object records
    question: Can I update multiple records of a custom object in one call?
  phrasing_ops: 18
  slug: conga-custom-object-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The CustomPlanTemplate (also called BillingPlanTemplate) Controller
  name: Conga Custom Plan Template API
  phrasing_intents:
  - id: patchCustomPlanTemplates
    intent: Edit custom plan templates in bulk
    question: Can I edit several custom plan templates and their line items together?
  - id: postCustomPlanTemplates
    intent: Create custom billing plan templates
    question: How do I create custom billing plan templates with installment or milestone line items?
  - id: patchCustomPlanTemplatesActivate
    intent: Activate or deactivate plan templates in bulk
    question: Can I switch a list of custom plan templates active or inactive at once?
  - id: getCustomPlanTemplatesByPlanTemplateId
    intent: Get a custom plan template
    question: What line items and settings does a specific custom plan template have?
  - id: patchCustomPlanTemplatesByPlanTemplateIdActivate
    intent: Activate or deactivate one plan template
    question: How do I turn a single custom plan template on or off?
  phrasing_ops: 5
  slug: conga-custom-plan-template-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for managing generic custom billing plans. Provides endpoints to create, retrieve, and delete custom plans.
  name: Conga Custom Plans API
  phrasing_intents:
  - id: deleteCustomPlans
    intent: Delete custom plans
    question: Can I delete several custom billing plans along with their line items?
  - id: postCustomPlansSearch
    intent: Search custom plans and their line items
    question: How do I find custom billing plans tied to an order or proposal?
  - id: getCustomPlansByCustomPlanId
    intent: Get a custom plan
    question: What are the details of one custom billing plan?
  phrasing_ops: 3
  slug: conga-custom-plans-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The CustomerOnboarded API from Conga — 1 operation(s) for customeronboarded.
  name: Conga Customer Onboarded API
  phrasing_intents:
  - id: CustomerOnboarded_Get
    intent: Check whether the customer is onboarded
    question: Has my organization finished onboarding?
  phrasing_ops: 1
  slug: conga-customeronboarded-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The CustomSettings API from Conga — 9 operation(s) for customsettings.
  name: Conga Custom Settings API
  phrasing_intents:
  - id: getFlows
    intent: List flows
    question: Which custom flows are defined in my Conga admin settings?
  - id: postFlows
    intent: Create a flow
    question: How do I create a new custom flow?
  - id: getFlowsByFlowNameViews
    intent: List views for a flow
    question: What views are configured for a flow?
  - id: postFlowsByFlowNameViews
    intent: Create views for a flow
    question: How do I add new views to a flow?
  - id: putFlowsByFlowNameViews
    intent: Update views for a flow
    question: How do I update the views on a flow?
  - id: deleteFlowsByFlowNameViewsByViewName
    intent: Delete a named view of a flow
    question: How do I remove a view from a flow?
  - id: getFlowsByFlowNameViewsByViewName
    intent: Get a named view of a flow
    question: How do I see one specific view on a flow by name?
  - id: deleteFlowsByFlowname
    intent: Delete a flow
    question: How do I delete a whole flow?
  phrasing_ops: 25
  slug: conga-customsettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: To do the operation reated to Discovery extraction and checking the status and marking
  name: Conga DAI API
  phrasing_intents:
  - id: getApiXauthorV1DiscoveryAiContractsByContractIdDocumentsByAttachmentIdStatus
    intent: Check the AI extraction job status for a document
    question: Has the Discovery AI extraction finished for a contract document?
  - id: postApiXauthorV1DiscoveryAiContractsByContractidDocumentsByAttachmentIdMarkupDocument
    intent: Mark up clauses and fields in a contract document
    question: Can Discovery AI tag the clauses and fields it found inside my contract document?
  phrasing_ops: 2
  slug: conga-dai-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for data correction-related operations.
  name: Conga Data Correction API
  phrasing_intents:
  - id: putApiXauthorV1DataCorrectionTemplateFieldRecordType
    intent: Rename RecordType to ContractType on templates
    question: Can I migrate template records from the RecordType field to ContractType?
  phrasing_ops: 1
  slug: conga-datacorrection-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Deal Color Bands API from Conga — 2 operation(s) for deal color bands.
  name: Conga Deal Color Bands API
  phrasing_intents:
  - id: deleteDealGuidanceColorBands
    intent: Delete deal color bands in bulk
    question: Can I delete multiple deal color bands at once?
  - id: getDealGuidanceColorBands
    intent: List deal guidance color bands
    question: Which color bands are set up for deal guidance rules?
  - id: patchDealGuidanceColorBands
    intent: Update deal color bands in bulk
    question: Can I change fields on several color bands in one request?
  - id: postDealGuidanceColorBands
    intent: Create deal color bands
    question: How do I add color bands with shapes and colors to tell deals apart?
  - id: deleteDealGuidanceColorBandsById
    intent: Delete a deal color band
    question: How do I remove one color band by its ID?
  - id: getDealGuidanceColorBandsById
    intent: Get a deal color band
    question: What shape and color does a particular deal color band use?
  - id: patchDealGuidanceColorBandsById
    intent: Update a deal color band
    question: Can I change the color or shape of a single color band?
  phrasing_ops: 7
  slug: conga-deal-color-bands-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Deal Guidance Dimension Set Members API from Conga — 2 operation(s) for deal guidance dimension set members.
  name: Conga Deal Guidance Dimension Set Members API
  phrasing_intents:
  - id: deleteDealGuidanceDimensionSetsByParentIdDimensions
    intent: Remove several dimensions from a dimension set
    question: Can I remove multiple dimensions from a dimension set at once?
  - id: getDealGuidanceDimensionSetsByParentIdDimensions
    intent: List the dimensions in a deal guidance dimension set
    question: Which dimensions make up a deal guidance dimension set?
  - id: patchDealGuidanceDimensionSetsByParentIdDimensions
    intent: Update several dimensions in a dimension set
    question: Can I edit many dimension set members in one batch?
  - id: postDealGuidanceDimensionSetsByParentIdDimensions
    intent: Add dimensions to a deal guidance dimension set
    question: How do I add new dimensions to a deal guidance dimension set?
  - id: deleteDealGuidanceDimensionSetsByParentIdDimensionsById
    intent: Remove one dimension from a dimension set
    question: Can I drop just one dimension from a deal guidance dimension set?
  - id: getDealGuidanceDimensionSetsByParentIdDimensionsById
    intent: Get one dimension from a dimension set
    question: What are the details of a single dimension in a deal guidance set?
  - id: patchDealGuidanceDimensionSetsByParentIdDimensionsById
    intent: Update one dimension in a dimension set
    question: Can I change a single dimension in a deal guidance dimension set?
  phrasing_ops: 7
  slug: conga-deal-guidance-dimension-set-members-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Deal Guidance Dimension Sets API from Conga — 2 operation(s) for deal guidance dimension sets.
  name: Conga Deal Guidance Dimension Sets API
  phrasing_intents:
  - id: deleteDealGuidanceDimensionSets
    intent: Delete several deal guidance dimension sets
    question: How do I bulk-delete deal guidance dimension sets?
  - id: getDealGuidanceDimensionSets
    intent: List deal guidance dimension sets
    question: Which dimension sets are set up for deal guidance pricing?
  - id: patchDealGuidanceDimensionSets
    intent: Update several deal guidance dimension sets
    question: Can I update many deal guidance dimension sets together?
  - id: postDealGuidanceDimensionSets
    intent: Create deal guidance dimension sets
    question: How do I add new dimension sets for deal guidance?
  - id: deleteDealGuidanceDimensionSetsById
    intent: Delete one deal guidance dimension set
    question: How do I delete a single deal guidance dimension set?
  - id: getDealGuidanceDimensionSetsById
    intent: Get a deal guidance dimension set
    question: How do I view one deal guidance dimension set by ID?
  - id: patchDealGuidanceDimensionSetsById
    intent: Update one deal guidance dimension set
    question: How do I edit one deal guidance dimension set?
  phrasing_ops: 7
  slug: conga-deal-guidance-dimension-sets-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Deal Guidance Dimensions API from Conga — 2 operation(s) for deal guidance dimensions.
  name: Conga Deal Guidance Dimensions API
  phrasing_intents:
  - id: deleteDealGuidanceDimensions
    intent: Delete deal guidance dimensions in bulk
    question: Can I remove several deal guidance dimensions at once?
  - id: getDealGuidanceDimensions
    intent: List deal guidance dimensions
    question: Which dimensions are defined for deal guidance rules?
  - id: patchDealGuidanceDimensions
    intent: Update deal guidance dimensions in bulk
    question: Can I edit many deal guidance dimensions with one payload?
  - id: postDealGuidanceDimensions
    intent: Create deal guidance dimensions
    question: How do I define new dimensions on a field for deal rule criteria?
  - id: deleteDealGuidanceDimensionsById
    intent: Delete a deal guidance dimension
    question: How do I delete one specific deal guidance dimension?
  - id: getDealGuidanceDimensionsById
    intent: Get a deal guidance dimension
    question: What field and settings does one deal guidance dimension use?
  - id: patchDealGuidanceDimensionsById
    intent: Update a deal guidance dimension
    question: How do I edit one deal guidance dimension?
  phrasing_ops: 7
  slug: conga-deal-guidance-dimensions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Deal Guidance Rule Entries API from Conga — 2 operation(s) for deal guidance rule entries.
  name: Conga Deal Guidance Rule Entries API
  phrasing_intents:
  - id: deleteDealGuidanceRulesByParentIdEntries
    intent: Delete entries from a deal guidance rule
    question: Can I remove several entries from a deal guidance rule in one call?
  - id: getDealGuidanceRulesByParentIdEntries
    intent: List entries of a deal guidance rule
    question: Which entries make up a particular deal guidance rule?
  - id: patchDealGuidanceRulesByParentIdEntries
    intent: Update entries of a deal guidance rule
    question: Can I edit several entries of a guidance rule together?
  - id: postDealGuidanceRulesByParentIdEntries
    intent: Add entries to a deal guidance rule
    question: How do I add new entries to a deal guidance rule?
  - id: deleteDealGuidanceRulesByParentIdEntriesById
    intent: Delete a deal guidance rule entry
    question: How do I delete just one entry from a guidance rule?
  - id: getDealGuidanceRulesByParentIdEntriesById
    intent: Get a deal guidance rule entry
    question: What does one specific entry in a deal guidance rule contain?
  - id: patchDealGuidanceRulesByParentIdEntriesById
    intent: Update a deal guidance rule entry
    question: Can I change a single entry in a deal guidance rule?
  phrasing_ops: 7
  slug: conga-deal-guidance-rule-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Deal Guidance Rules API from Conga — 2 operation(s) for deal guidance rules.
  name: Conga Deal Guidance Rules API
  phrasing_intents:
  - id: deleteDealGuidanceRules
    intent: Delete several deal guidance rules
    question: Can I delete a list of deal guidance rules in one go?
  - id: getDealGuidanceRules
    intent: List deal guidance rules
    question: Which deal guidance rules are configured in Conga CPQ?
  - id: patchDealGuidanceRules
    intent: Update several deal guidance rules
    question: Can I edit multiple deal guidance rules in a single batch?
  - id: postDealGuidanceRules
    intent: Create deal guidance rules
    question: How do I set up new deal guidance rules?
  - id: deleteDealGuidanceRulesById
    intent: Delete a deal guidance rule
    question: How do I delete one deal guidance rule by ID?
  - id: getDealGuidanceRulesById
    intent: Get a deal guidance rule
    question: What does one particular deal guidance rule contain?
  - id: patchDealGuidanceRulesById
    intent: Update a deal guidance rule
    question: Can I change one deal guidance rule by its ID?
  phrasing_ops: 7
  slug: conga-deal-guidance-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Dependent Picklist Definition API from Conga — 1 operation(s) for dependent picklist definition.
  name: Conga Dependent Picklist Definition API
  phrasing_intents:
  - id: deleteApiSchemaV1ObjectsByObjectNameFieldsByFieldNameDependentPicklists
    intent: Remove a field's dependent picklist mapping
    question: Can I remove the dependency so a picklist no longer depends on another field?
  - id: getApiSchemaV1ObjectsByObjectNameFieldsByFieldNameDependentPicklists
    intent: Get a field's dependent picklist mapping
    question: Which controlling field drives the values of a dependent picklist in Conga?
  - id: postApiSchemaV1ObjectsByObjectNameFieldsByFieldNameDependentPicklists
    intent: Create a dependent picklist mapping
    question: How do I make one picklist's options depend on another field's value?
  - id: putApiSchemaV1ObjectsByObjectNameFieldsByFieldNameDependentPicklists
    intent: Update a field's dependent picklist mapping
    question: Can I change which dependent values show for a controlling picklist value?
  phrasing_ops: 4
  slug: conga-dependent-picklist-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for Document.
  name: Conga Document API
  phrasing_intents:
  - id: postApiXauthorV1DocumentsContentConvertOpcxmlToHtml
    intent: Convert OPC XML document content to HTML
    question: How do I turn Word OPC XML content into HTML with Conga X-Author?
  - id: postApiXauthorV1DocumentsContentNoDatepicker
    intent: Replace Word content controls with plain text
    question: Why do date pickers and drop-downs break in Word online, and can I flatten them?
  - id: postApiXauthorV1DocumentsMetadata
    intent: Read agreement details from a document file
    question: Can I find out which agreement a Word file belongs to by uploading it?
  - id: postApiXauthorV1DocumentsSuggestedFilename
    intent: Get a suggested file name for a document
    question: What file name should a generated agreement document get?
  - id: getApiXauthorV1DocumentsByAttachmentId
    intent: Get a document or attachment record
    question: How do I look up an attachment record by its ID in X-Author?
  - id: getApiXauthorV1DocumentsByAttachmentIdClauses
    intent: List the clauses in a document
    question: Which clauses appear inside an agreement document?
  - id: getApiXauthorV1DocumentsByAttachmentIdContent
    intent: Download a document's content for Windows or Mac
    question: How do I download the file content of an attachment for the desktop add-in?
  - id: getApiXauthorV1DocumentsByAttachmentIdContentBody
    intent: Get a document's content as a string and bytes
    question: Can I get the body of a document both as text and as raw bytes?
  phrasing_ops: 13
  slug: conga-document-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Document Generation API from Conga — 5 operation(s) for document generation.
  name: Conga Document Generation API
  phrasing_intents:
  - id: postApiClmV1ContractsByContractIdGenerate
    intent: Generate a contract document from a template
    question: How do I generate the first contract document from a template in Conga CLM?
  - id: postApiClmV1ContractsByContractIdJoindocuments
    intent: Merge several contract documents into one
    question: Can I combine multiple documents on a contract into a single file?
  - id: postApiClmV1ContractsByContractIdPreviewdocument
    intent: Preview a contract document from a template
    question: Can I see what a contract would look like from a template before generating it for real?
  - id: postApiClmV1ContractsByContractIdRegenerate
    intent: Regenerate a contract document
    question: How do I rebuild a contract document after the contract data changed?
  - id: postApiClmV1ContractsByContractIdSupportingdocument
    intent: Generate a supporting document for a contract
    question: Can I generate an extra supporting document, like an exhibit, for a contract?
  phrasing_ops: 5
  slug: conga-document-generation-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Document Settings API from Conga — 7 operation(s) for document settings.
  name: Conga Document Settings API
  phrasing_intents:
  - id: postApiClmV1SettingsDocumentsOutputFormats
    intent: Create a document output format
    question: How do I set up a new document output format like PDF or DOCX?
  - id: putApiClmV1SettingsDocumentsOutputFormats
    intent: Update a document output format
    question: How do I change an existing document output format's properties?
  - id: postApiClmV1SettingsDocumentsOutputFormatsQuery
    intent: Query document output formats
    question: Which document output format records match my criteria?
  - id: deleteApiClmV1SettingsDocumentsOutputFormatsById
    intent: Delete a document output format
    question: How do I delete a document output format I no longer use?
  - id: getApiClmV1SettingsDocumentsOutputFormatsById
    intent: Get a document output format
    question: How do I look up one document output format by ID?
  - id: postApiClmV1SettingsDocumentsProtections
    intent: Add a document protection setting
    question: How do I add document protection for a user role and contract type?
  - id: putApiClmV1SettingsDocumentsProtections
    intent: Update a document protection setting
    question: How do I change fields on a document protection setting?
  - id: postApiClmV1SettingsDocumentsProtectionsClone
    intent: Copy protection settings between roles
    question: Can I copy one role's document protection settings to other roles?
  phrasing_ops: 11
  slug: conga-document-settings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for document metadata.
  name: Conga Document Metadata API
  phrasing_intents:
  - id: getApiXauthorV1DocumentsGdocsByGdocFileIdMetadata
    intent: Get V2 metadata for a Google Doc
    question: How do I get the V2 metadata JSON for a document stored in Google Docs?
  - id: getApiXauthorV1DocumentsByAttachmentIdDocumentProperties
    intent: Get document metadata with custom properties
    question: Which custom properties are set on a document attachment?
  - id: getApiXauthorV1DocumentsByAttachmentIdMetadata
    intent: Get document metadata
    question: What metadata is stored for a document attachment?
  - id: getApiXauthorV1DocumentsByAttachmentIdMetadataV2
    intent: Get V2 metadata for an attachment
    question: Is there a V2 metadata JSON format for document attachments?
  - id: getApiXauthorV1DocumentsByAttachmentIdSmartElements
    intent: List fields and clauses in a document
    question: Which merge fields and clauses are embedded in a document?
  phrasing_ops: 5
  slug: conga-documentmetadata-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for Document protection.
  name: Conga Document Protection API
  phrasing_intents:
  - id: postApiXauthorV1DocumentsProtect
    intent: Protect an agreement document
    question: How do I lock an agreement document without sharing a password?
  - id: postApiXauthorV1DocumentsUnprotect
    intent: Unprotect an agreement document
    question: How do I remove protection from an agreement document so it's fully editable?
  - id: getApiXauthorV1DocumentsByCurrentprotectionProtections
    intent: Get a document's protection type
    question: What protection type maps to a document's current protection?
  - id: getApiXauthorV1DocumentsBySaveoptionProtection
    intent: Get a document's protection level by save option
    question: Which protection level applies when I save a document version a certain way?
  phrasing_ops: 4
  slug: conga-documentprotection-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Documents API from Conga — 38 operation(s) for documents.
  name: Conga Documents API
  phrasing_intents:
  - id: Documents_CreateDocument
    intent: Add a document to a package
    question: How do I upload another document to a package I already created?
  - id: Documents_DeleteDocuments
    intent: Delete several documents from a package
    question: Can I remove multiple documents from a package at once?
  - id: Documents_UpdateDocuments
    intent: Reorder or update all documents in a package
    question: Can I change the order documents appear in within a signing package?
  - id: Documents_GetAllDocumentsZip
    intent: Download all documents including supporting docs as zip
    question: How do I download every document in a package, supporting documents included, as a zip?
  - id: Documents_CreateSignatureConfirmation
    intent: Confirm a document can be signed
    question: How do I confirm the application is allowed to run signing on a document?
  - id: Documents_SignAllDocuments
    intent: Sign every document in a package
    question: Can I sign all documents in a package in a single call?
  - id: Documents_GetDocumentVisibility
    intent: See which recipients can view which documents
    question: Which signers can see which documents during the signing ceremony?
  - id: Documents_UpdateDocumentsVisibility
    intent: Set which recipients can view documents
    question: How do I hide a document from certain signers in a package?
  phrasing_ops: 51
  slug: conga-documents-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for Document Transfer Metadata Sync.
  name: Conga Document Sync API
  phrasing_intents:
  - id: postApiXauthorV1DocumentSync
    intent: Sync a document back to its agreement
    question: How do I save edits made in X-Author back to the agreement record?
  - id: postApiXauthorV1DocumentSyncUpdateDocumentProperties
    intent: Update a document's properties
    question: Can I refresh the Word document properties on an agreement file?
  - id: getApiXauthorV1DocumentSyncByExternalIdAttachmentId
    intent: Find an attachment ID from an external ID
    question: How do I find the attachment that matches an external document ID?
  phrasing_ops: 3
  slug: conga-documentsync-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Draft API from Conga — 2 operation(s) for draft.
  name: Conga Draft API
  phrasing_intents:
  - id: Draft_CreateDraft
    intent: Save a document solution as a draft
    question: Can I save a document generation solution as a draft before deploying it?
  - id: Draft_GetDraftById
    intent: Retrieve a saved solution draft
    question: Can I reopen a solution draft I saved earlier?
  phrasing_ops: 2
  slug: conga-draft-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This controller provides access to email operations like sending email in post delivery.
  name: Conga Email API
  phrasing_intents:
  - id: Email_CreateSignPackage
    intent: Generate a signing package URL for delivery
    question: Can I turn a merged document into an e-signature package link for email delivery?
  - id: Email_MergeEmailTemplate
    intent: Merge an email template with record data
    question: Can I fill an email template with Salesforce data from the original merge?
  - id: Email_MockCreateSignPackage
    intent: Mock generating a signing package URL
    question: Is there a mock version of sign package generation for testing?
  - id: Email_MockSendEmail
    intent: Mock sending an email with attachments
    question: Can I dry-run an email send and get back JSON instead of delivering it?
  - id: Email_SendEmail
    intent: Send an email with attachments
    question: How do I email generated documents as attachments to a recipient?
  phrasing_ops: 5
  slug: conga-email-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Email Delivery Status API from Conga — 2 operation(s) for email delivery status.
  name: Conga Email Delivery Status API
  phrasing_intents:
  - id: getApiEmailV1EmailsJobsByJobId
    intent: Get email delivery status by job
    question: Was the email sent by a particular job delivered?
  - id: postApiEmailV1EmailsStatusBatch
    intent: Get email delivery status for recipients
    question: Which recipients of an email send actually received it?
  phrasing_ops: 2
  slug: conga-email-delivery-status-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Email Profile API from Conga — 2 operation(s) for email profile.
  name: Conga Email Profile API
  phrasing_intents:
  - id: postApiEmailV1EmailProfiles
    intent: Create an email profile
    question: What do I need to set up a new sender email profile?
  - id: deleteApiEmailV1EmailProfilesByName
    intent: Delete an email profile
    question: Can I remove a sender email profile I no longer use?
  - id: getApiEmailV1EmailProfilesByName
    intent: Get an email profile by name
    question: What sender address does a named email profile use?
  - id: putApiEmailV1EmailProfilesByName
    intent: Update an email profile
    question: Can I change the sender address on an existing email profile?
  phrasing_ops: 4
  slug: conga-email-profile-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Email Sender API from Conga — 4 operation(s) for email sender.
  name: Conga Email Sender API
  phrasing_intents:
  - id: postApiEmailV1Emails
    intent: Send a single email
    question: How do I send one email to a recipient through Conga?
  - id: postApiEmailV1EmailsBulk
    intent: Send a mass email from a template
    question: Can I send the same email template to many recipients at once?
  - id: getApiEmailV1EmailsDomainVerify
    intent: Verify a sending email domain
    question: Is my sending domain verified for outgoing email?
  - id: postApiEmailV2EmailsBulk
    intent: Send a mass email with the v2 contract
    question: What does the newer v2 bulk email endpoint accept?
  phrasing_ops: 4
  slug: conga-email-sender-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Email Template API from Conga — 8 operation(s) for email template.
  name: Conga Email Template API
  phrasing_intents:
  - id: getApiEmailV1EmailTemplates
    intent: List email templates with filters
    question: Which email templates do we have, sorted by name?
  - id: postApiEmailV1EmailTemplates
    intent: Create an email template
    question: How do I create a new reusable email template?
  - id: postApiEmailV1EmailTemplatesRender
    intent: Preview an unsaved email template
    question: Can I preview how a draft template renders before saving it?
  - id: getApiEmailV1EmailTemplatesSearch
    intent: Search email templates by criteria
    question: What templates match a search criteria expression?
  - id: deleteApiEmailV1EmailTemplatesById
    intent: Delete an email template
    question: How do I remove an email template we no longer use?
  - id: getApiEmailV1EmailTemplatesById
    intent: Get an email template
    question: Where can I see the full details of one email template?
  - id: postApiEmailV1EmailTemplatesById
    intent: Attach a file to an email template
    question: Can I add an attachment to a saved email template?
  - id: putApiEmailV1EmailTemplatesById
    intent: Update an email template
    question: How do I edit an existing email template's subject or body?
  phrasing_ops: 12
  slug: conga-email-template-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Email Template Category API from Conga — 2 operation(s) for email template category.
  name: Conga Email Template Category API
  phrasing_intents:
  - id: getApiEmailV1EmailTemplateCategories
    intent: List email template categories
    question: What categories are my email templates organized into?
  - id: postApiEmailV1EmailTemplateCategories
    intent: Create an email template category
    question: How do I add a new folder-like category for templates?
  - id: deleteApiEmailV1EmailTemplateCategoriesById
    intent: Delete an email template category
    question: Can I delete a template category I no longer need?
  - id: getApiEmailV1EmailTemplateCategoriesById
    intent: Get an email template category
    question: Can I look up a single template category's details?
  - id: putApiEmailV1EmailTemplateCategoriesById
    intent: Update an email template category
    question: How do I rename an existing template category?
  phrasing_ops: 5
  slug: conga-email-template-category-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Encryption controller which will be used to create all the methods for encrypt/decrypt.
  name: Conga Encryption API
  phrasing_intents:
  - id: postApiXauthorV1EncryptionEncrypt
    intent: Encrypt a text value
    question: Can X-Author encrypt a piece of text for me?
  phrasing_ops: 1
  slug: conga-encryption-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Export cart data (line items) as CSV.
  name: Conga Export API
  phrasing_intents:
  - id: postApiCartV1CartsByCartIdExport
    intent: Export cart line items to CSV
    question: Can I download a cart's line items as a CSV file?
  - id: postApiClmV1ObjectsExportByFileNameByFormat
    intent: Export CLM query results to a file
    question: How do I export a CLM object query to Excel?
  - id: postApiClmV1ObjectsMultipleExportByFileNameByFormat
    intent: Export multi-object search results
    question: Can I export search results that span several object types?
  phrasing_ops: 3
  slug: conga-export-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The External Endpoint Auth Credentials API from Conga — 2 operation(s) for external endpoint auth credentials.
  name: Conga External Endpoint Auth Credentials API
  phrasing_intents:
  - id: postApiExternalEndpointConfigV1Credentials
    intent: Create an endpoint auth credential
    question: How do I store new credentials for calling an external endpoint?
  - id: putApiExternalEndpointConfigV1Credentials
    intent: Update an endpoint auth credential
    question: How do I change the secrets on an existing external auth configuration?
  - id: deleteApiExternalEndpointConfigV1CredentialsByName
    intent: Delete an endpoint auth credential
    question: How do I remove stored credentials for an external endpoint?
  - id: getApiExternalEndpointConfigV1CredentialsByName
    intent: Get an endpoint auth credential
    question: Can I look up a saved authentication configuration by name?
  phrasing_ops: 4
  slug: conga-external-endpoint-auth-credentials-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The External Endpoint Configuration API from Conga — 3 operation(s) for external endpoint configuration.
  name: Conga External Endpoint Configuration API
  phrasing_intents:
  - id: getApiExternalEndpointConfigV1Endpoints
    intent: List external endpoint configurations
    question: Which external endpoints have we configured?
  - id: postApiExternalEndpointConfigV1Endpoints
    intent: Create an external endpoint configuration
    question: How do I register a new external endpoint to call?
  - id: postApiExternalEndpointConfigV1EndpointsValidate
    intent: Validate an external endpoint schema
    question: Can I check a request and response schema before saving an endpoint?
  - id: deleteApiExternalEndpointConfigV1EndpointsById
    intent: Delete an external endpoint configuration
    question: Can I remove an endpoint configuration we stopped using?
  - id: getApiExternalEndpointConfigV1EndpointsById
    intent: Get an external endpoint configuration
    question: Where do I see the details of one endpoint configuration?
  - id: putApiExternalEndpointConfigV1EndpointsById
    intent: Update an external endpoint configuration
    question: How do I change the URL of a configured endpoint?
  phrasing_ops: 6
  slug: conga-external-endpoint-configuration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ExternalAuthentication API from Conga — 1 operation(s) for externalauthentication.
  name: Conga External Authentication API
  phrasing_intents:
  - id: ExternalAuthentication_GetExternalAuthenticationOptions
    intent: List the account's external sign-in options
    question: Which SSO providers are configured for our signing account?
  phrasing_ops: 1
  slug: conga-externalauthentication-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Favorites API from Conga — 7 operation(s) for favorites.
  name: Conga Favorites API
  phrasing_intents:
  - id: getFavorites
    intent: List favorite configurations
    question: Which favorite configurations have been saved?
  - id: deleteFavorites
    intent: Delete favorite records in bulk
    question: Can I delete several favorites in a single request?
  - id: getFavoritesById
    intent: Get a favorite configuration (lowercase id path)
    question: Is there a separate lookup for a favorite configuration by identifier?
  - id: deleteFavoritesById
    intent: Delete a favorite
    question: Can I delete one favorite I saved?
  - id: getFavoritesById
    intent: Fetch a favorite by ID
    question: How do I fetch a single favorite?
  - id: patchFavoritesById
    intent: Update a favorite
    question: How do I change a saved favorite?
  - id: postFavoritesByIdAddtocartByCartId
    intent: Add a favorite to a cart
    question: Can I drop a saved favorite into a cart?
  - id: deleteFavoritesByIdItems
    intent: Remove line items from a favorite
    question: How do I clear the line items inside a favorite?
  phrasing_ops: 10
  slug: conga-favorites-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Feature API from Conga — 2 operation(s) for feature.
  name: Conga Feature API
  phrasing_intents:
  - id: deleteFeatureSetsByParentIdFeatures
    intent: Delete features from a feature set
    question: Can I remove multiple features from a feature set?
  - id: getFeatureSetsByParentIdFeatures
    intent: List features in a feature set
    question: Which features belong to a feature set?
  - id: patchFeatureSetsByParentIdFeatures
    intent: Update features in a feature set
    question: Can I edit several features in a set in one call?
  - id: postFeatureSetsByParentIdFeatures
    intent: Add features to a feature set
    question: How do I add new features to a feature set?
  - id: deleteFeatureSetsByParentIdFeaturesById
    intent: Delete one feature from a feature set
    question: Can I delete a single feature from a set?
  - id: getFeatureSetsByParentIdFeaturesById
    intent: Get one feature in a feature set
    question: Where can I see a single feature's details?
  - id: patchFeatureSetsByParentIdFeaturesById
    intent: Update one feature in a feature set
    question: How do I edit a single feature?
  phrasing_ops: 7
  slug: conga-feature-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Feature Sets API from Conga — 4 operation(s) for feature sets.
  name: Conga Feature Sets API
  phrasing_intents:
  - id: deleteFeatureSets
    intent: Delete feature sets in bulk
    question: Can I delete several feature sets at once?
  - id: getFeatureSets
    intent: List feature sets
    question: What feature sets exist in my catalog?
  - id: patchFeatureSets
    intent: Update feature sets in bulk
    question: Can I update many feature sets in one call?
  - id: postFeatureSets
    intent: Create feature sets
    question: How do I create new feature sets?
  - id: deleteFeatureSetsById
    intent: Delete a feature set
    question: Can I delete a single feature set?
  - id: getFeatureSetsById
    intent: Get a feature set
    question: Where can I see one feature set's details?
  - id: patchFeatureSetsById
    intent: Update a feature set
    question: How do I edit one feature set?
  - id: deleteFeatureSetsByParentIdProductFeatures
    intent: Delete product features in bulk
    question: Can I unlink many products from a feature set at once?
  phrasing_ops: 14
  slug: conga-feature-sets-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Features API from Conga — 2 operation(s) for features.
  name: Conga Features API
  phrasing_intents:
  - id: deleteFeaturesByParentIdProductFeatureValues
    intent: Delete product feature values in bulk
    question: Can I remove many product values from a feature at once?
  - id: getFeaturesByParentIdProductFeatureValues
    intent: List product feature values
    question: What values do products have for a given feature?
  - id: patchFeaturesByParentIdProductFeatureValues
    intent: Update product feature values in bulk
    question: Can I edit multiple product feature values in one call?
  - id: postFeaturesByParentIdProductFeatureValues
    intent: Create product feature values
    question: How do I set feature values on products?
  - id: deleteFeaturesByParentIdProductFeatureValuesById
    intent: Delete a product feature value
    question: Can I delete one product's value for a feature?
  - id: getFeaturesByParentIdProductFeatureValuesById
    intent: Get a product feature value
    question: Where can I see one product's value for a feature?
  - id: patchFeaturesByParentIdProductFeatureValuesById
    intent: Update a product feature value
    question: How do I change one product's value for a feature?
  phrasing_ops: 7
  slug: conga-features-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller to fetch the feature settings
  name: Conga Feature Settings API
  phrasing_intents:
  - id: getApiXauthorV1FeatureSettings
    intent: Check external connection status
    question: Is the X-Author external connection currently active?
  - id: getApiXauthorV1FeatureSettingsAi
    intent: Get AI feature settings
    question: Which AI features are turned on in X-Author?
  - id: getApiXauthorV1FeatureSettingsAll
    intent: Get all X-Author feature settings
    question: What are all the feature settings configured in X-Author?
  phrasing_ops: 3
  slug: conga-featuresettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Field Definition API from Conga — 5 operation(s) for field definition.
  name: Conga Field Definition API
  phrasing_intents:
  - id: getApiSchemaV1ObjectsFormulaFunctions
    intent: List formula functions
    question: Which functions can I use in formula fields?
  - id: postApiSchemaV1ObjectsByObjectNameFields
    intent: Create a field on an object
    question: How do I add a custom field to an object?
  - id: deleteApiSchemaV1ObjectsByObjectNameFieldsByFieldName
    intent: Delete a custom field
    question: Can I delete a custom field from an object?
  - id: putApiSchemaV1ObjectsByObjectNameFieldsByFieldName
    intent: Update a field definition
    question: How do I change an existing field's display name or default?
  - id: patchApiSchemaV1ObjectsByObjectNameFieldsByFieldNameDeprecate
    intent: Deprecate a field
    question: Can I mark a field as deprecated instead of deleting it?
  - id: postApiSchemaV1ObjectsByObjectNameFieldsByFieldNameExpressionValidate
    intent: Validate a formula field expression
    question: Is my formula expression valid before I save it?
  phrasing_ops: 6
  slug: conga-field-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Field Expressions API from Conga — 5 operation(s) for field expressions.
  name: Conga Field Expressions API
  phrasing_intents:
  - id: deleteFieldExpressions
    intent: Delete field expressions in bulk
    question: Can I delete many field expressions at once?
  - id: getFieldExpressions
    intent: List field expressions
    question: What field expressions are defined?
  - id: patchFieldExpressions
    intent: Update field expressions in bulk
    question: Can I edit several field expressions in one call?
  - id: postFieldExpressions
    intent: Create field expressions
    question: How do I create new field expressions?
  - id: deleteFieldExpressionsById
    intent: Delete a field expression
    question: Can I delete a single field expression?
  - id: getFieldExpressionsById
    intent: Get a field expression
    question: Where can I see one field expression's definition?
  - id: patchFieldExpressionsById
    intent: Update a field expression
    question: How do I edit one field expression?
  - id: getFieldExpressionsByIdConstraintRuleActions
    intent: Look up constraint rule actions for an expression
    question: Which constraint rule actions can a field expression reference?
  phrasing_ops: 15
  slug: conga-field-expressions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Field History Tracking API from Conga — 1 operation(s) for field history tracking.
  name: Conga Field History Tracking API
  phrasing_intents:
  - id: postApiAuditV1ObjectsByObjectNameRecordsByRecordIdFieldHistoryTracking
    intent: Get a record's field change history
    question: Who changed fields on a record and when?
  phrasing_ops: 1
  slug: conga-field-history-tracking-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Field History Tracking Config API from Conga — 2 operation(s) for field history tracking config.
  name: Conga Field History Tracking Config API
  phrasing_intents:
  - id: getApiAuditV1FieldHistoryTrackingConfig
    intent: Get field history tracking configuration
    question: Which objects and fields are tracked for history?
  - id: deleteApiAuditV1ObjectsByObjectNameFieldHistoryTrackingConfig
    intent: Stop tracking history on an object
    question: Can I turn off field history tracking for an object?
  - id: putApiAuditV1ObjectsByObjectNameFieldHistoryTrackingConfig
    intent: Track fields for history on an object
    question: How do I start tracking field changes on an object?
  phrasing_ops: 3
  slug: conga-field-history-tracking-config-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Field Permission API from Conga — 3 operation(s) for field permission.
  name: Conga Field Permission API
  phrasing_intents:
  - id: deleteApiUserManagementV1FieldPermissions
    intent: Delete field permissions by group and object
    question: Can I remove a group's field permissions on an object?
  - id: getApiUserManagementV1FieldPermissions
    intent: Get field permissions for an object and group
    question: What field access does a permission group have on an object?
  - id: postApiUserManagementV1FieldPermissions
    intent: Set field permissions
    question: How do I grant a permission group field access on an object for the first time?
  - id: putApiUserManagementV1FieldPermissions
    intent: Update field permissions by group and object
    question: How do I change field access for a group on an object?
  - id: postApiUserManagementV1FieldPermissionsBulk
    intent: Set multiple field permissions in bulk
    question: Can I set field permissions for many objects or groups at once?
  - id: deleteApiUserManagementV1FieldPermissionsByFieldPermissionId
    intent: Delete a field permission by ID
    question: Can I delete one field permission record by its ID?
  - id: getApiUserManagementV1FieldPermissionsByFieldPermissionId
    intent: Get a field permission by ID
    question: Where can I see one field permission record?
  - id: putApiUserManagementV1FieldPermissionsByFieldPermissionId
    intent: Update a field permission by ID
    question: How do I edit a single field permission record?
  phrasing_ops: 8
  slug: conga-field-permission-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for field's marking-related operations.
  name: Conga Field Data API
  phrasing_intents:
  - id: postApiXauthorV1Metadata1FieldsRetrieveData
    intent: Get locale-formatted field values
    question: Can X-Author return field values formatted for a document's locale?
  phrasing_ops: 1
  slug: conga-fielddata-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for retrieving document field data related operations.
  name: Conga Field Data Retrieval API
  phrasing_intents:
  - id: postApiXauthorV1Metadata2FieldsRetrieveData
    intent: Get a record's field data by locale
    question: Can I fetch a record's field values formatted for a locale?
  phrasing_ops: 1
  slug: conga-fielddataretrieval-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for field's marking-related operations.
  name: Conga Field Mark API
  phrasing_intents:
  - id: postApiXauthorV1FieldsMarkContent
    intent: Mark document content as a field
    question: How do I tag text in a contract document as a field?
  - id: postApiXauthorV1FieldsMarkContent2
    intent: Mark text as a field (v2 metadata)
    question: Is there a newer way to mark selected text as a field using document metadata?
  phrasing_ops: 2
  slug: conga-fieldmark-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for the document field's related operations.
  name: Conga Fields API
  phrasing_intents:
  - id: postApiXauthorV1FieldsDataFetch
    intent: Fetch locale-formatted field values for documents
    question: Can I fetch formatted field values for several document objects?
  - id: postApiXauthorV1FieldsDataRetrieve
    intent: Retrieve field data
    question: Can I retrieve raw field data for a set of requests?
  - id: postApiXauthorV1FieldsReferencesMetadata
    intent: Resolve field name references
    question: How do I find what a field reference points to?
  - id: postApiXauthorV1FieldsValidate
    intent: Validate field data in a document
    question: Are the field values in my document valid?
  - id: postApiXauthorV1FieldsValidateV2
    intent: Validate field data with v2 metadata
    question: Is there a v2 field validation that uses document metadata?
  phrasing_ops: 5
  slug: conga-fields-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The FieldSetSettings API from Conga — 2 operation(s) for fieldsetsettings.
  name: Conga Field Set Settings API
  phrasing_intents:
  - id: getFieldSets
    intent: List field sets
    question: Which field sets are configured in administration?
  - id: getFieldSetsByName
    intent: List the fields in a field set
    question: Which fields belong to a particular field set?
  - id: putFieldSetsByName
    intent: Update the fields in a field set
    question: How do I change which fields a field set includes?
  phrasing_ops: 3
  slug: conga-fieldsetsettings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for document field validation operations.
  name: Conga Fields Validate API
  phrasing_intents:
  - id: postApiXauthorV1ObjectsByObjectNameByObjectIdFieldsByFieldAPIValidate
    intent: Validate a field value on a record
    question: Is the value I typed into a document field valid for that record?
  phrasing_ops: 1
  slug: conga-fieldsvalidate-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The File Store API from Conga — 17 operation(s) for file store.
  name: Conga File Store API
  phrasing_intents:
  - id: deleteApiFilestoreV1Files
    intent: Delete a file from the file store
    question: How do I delete one file from the file store?
  - id: deleteApiFilestoreV1FilesBulk
    intent: Delete multiple files
    question: Can I delete many files from one path in one call?
  - id: postApiFilestoreV1FilesBulk
    intent: Upload multiple files
    question: Can I upload several files to the file store at once?
  - id: getApiFilestoreV1FilesLimits
    intent: Get file size limits
    question: What is the maximum file size the file store accepts?
  - id: deleteApiFilestoreV1FilesMultipartUploads
    intent: Abort a multipart upload
    question: Can I cancel an unfinished multipart upload?
  - id: postApiFilestoreV1FilesMultipartUploads
    intent: Start a multipart upload
    question: How do I begin uploading a very large file in parts?
  - id: putApiFilestoreV1FilesMultipartUploads
    intent: Upload one part of a multipart upload
    question: How do I send the next chunk of a large file upload?
  - id: postApiFilestoreV1FilesMultipartUploadsComplete
    intent: Complete a multipart upload
    question: How do I finish a multipart upload once all parts are sent?
  phrasing_ops: 20
  slug: conga-file-store-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The FileAttachment API from Conga — 7 operation(s) for fileattachment.
  name: Conga File Attachment API
  phrasing_intents:
  - id: FileAttachment_GetZipAttachment
    intent: Download all of a package's attachments as a zip
    question: Can I download every file signers attached to a package in one zip?
  - id: FileAttachment_GetZipAttachmentByRole
    intent: Download one role's attachments as a zip
    question: Can I zip only the attachments uploaded by one signer role?
  - id: FileAttachment_CheckZipAttachmentByRoleExists
    intent: Check if a role has attachments with uploads
    question: Has a given signer role uploaded any attachments yet?
  - id: FileAttachment_AddAttachment
    intent: Upload a file to a package attachment
    question: Can I upload a supporting document to an attachment requirement on a package?
  - id: FileAttachment_GetAttachmentById
    intent: Download one attachment from a package
    question: How do I download a single attachment requirement's files from a package?
  - id: FileAttachment_CheckAttachmentExists
    intent: Check if an attachment has signer uploads
    question: Has the signer uploaded anything for a specific attachment requirement?
  - id: FileAttachment_DeleteAttachmentFile
    intent: Delete an uploaded file from an attachment
    question: Can I remove a wrong file a signer uploaded to an attachment?
  - id: FileAttachment_GetAttachmentFile
    intent: Download a specific file within an attachment
    question: An attachment has several uploaded files; can I download just one of them?
  phrasing_ops: 9
  slug: conga-fileattachment-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Forecast Billing API from Conga — 3 operation(s) for forecast billing.
  name: Conga Forecast Billing API
  phrasing_intents:
  - id: postForecast
    intent: Create billing forecast data
    question: How do I generate a billing forecast?
  - id: postForecastRegenerateForecastSummary
    intent: Regenerate a forecast summary
    question: Can I rebuild the forecast summary after changes?
  - id: getForecastByBusinessObjectTypeByBusinessObjectId
    intent: Get forecast data for a business object
    question: What billing is forecast for a specific order or agreement?
  phrasing_ops: 3
  slug: conga-forecast-billing-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Frequency Conversion Admin API from Conga — 3 operation(s) for frequency conversion admin.
  name: Conga Frequency Conversion Admin API
  phrasing_intents:
  - id: getApiConversionManagementV1FrequencyConversionRates
    intent: List frequency conversion rates
    question: What frequency conversion rates are set up?
  - id: postApiConversionManagementV1FrequencyConversionRates
    intent: Add a frequency conversion rate
    question: How do I define a rate to convert monthly to yearly?
  - id: postApiConversionManagementV1FrequencyConversionRatesBulk
    intent: Add many frequency conversion rates
    question: Can I create several frequency conversion rates in one call?
  - id: putApiConversionManagementV1FrequencyConversionRatesBulk
    intent: Update many frequency conversion rates
    question: Can I edit several conversion rates in one request?
  - id: deleteApiConversionManagementV1FrequencyConversionRatesById
    intent: Delete a frequency conversion rate
    question: Can I delete a conversion rate we no longer use?
  - id: getApiConversionManagementV1FrequencyConversionRatesById
    intent: Get a frequency conversion rate
    question: Where do I see one frequency conversion rate?
  - id: putApiConversionManagementV1FrequencyConversionRatesById
    intent: Update a frequency conversion rate
    question: How do I change one conversion rate?
  phrasing_ops: 7
  slug: conga-frequency-conversion-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Frequency Conversion Runtime API from Conga — 3 operation(s) for frequency conversion runtime.
  name: Conga Frequency Conversion Runtime API
  phrasing_intents:
  - id: postApiConversionManagementV1QueryFrequencyConversion
    intent: Convert a value between frequencies
    question: What is a monthly amount worth when converted to yearly?
  - id: postApiConversionManagementV1QueryFrequencyConversionRates
    intent: Look up the effective conversion rate
    question: Which conversion rate applies between two frequencies right now?
  - id: postApiConversionManagementV1QueryFrequencyConversionRatesBulk
    intent: Look up effective conversion rates in bulk
    question: Can I look up many effective conversion rates at once?
  phrasing_ops: 3
  slug: conga-frequency-conversion-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The GlobalSearch Runtime API from Conga — 1 operation(s) for globalsearch runtime.
  name: Conga GlobalSearch Runtime API
  phrasing_intents:
  - id: postApiSearchV1GlobalQuery
    intent: Search across configured objects
    question: Can I search every configured object for a term?
  phrasing_ops: 1
  slug: conga-globalsearch-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for google configurations such as google drive enabled and service configuration info
  name: Conga Google Config API
  phrasing_intents:
  - id: getApiXauthorV1GoogleConfig
    intent: Get Google Drive configuration
    question: Is Google Drive support turned on for X-Author?
  phrasing_ops: 1
  slug: conga-googleconfig-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Grant Login API from Conga — 3 operation(s) for grant login.
  name: Conga Grant Login API
  phrasing_intents:
  - id: getApiUserManagementV1Grantlogin
    intent: List grant login requests
    question: Which grant login requests are open?
  - id: postApiUserManagementV1Grantlogin
    intent: Request login access for support
    question: How do I grant support access to log in as a user?
  - id: getApiUserManagementV1GrantloginDurations
    intent: List login access durations
    question: How long can a login grant last?
  - id: getApiUserManagementV1GrantloginByGrantLoginId
    intent: Get a grant login request
    question: Where can I see the details of one login grant?
  - id: putApiUserManagementV1GrantloginByGrantLoginId
    intent: Cancel a grant login request
    question: Can I revoke a login grant before it expires?
  phrasing_ops: 5
  slug: conga-grant-login-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Guest User API from Conga — 4 operation(s) for guest user.
  name: Conga Guest User API
  phrasing_intents:
  - id: postApiUserManagementV1UserGuest
    intent: Create a guest user
    question: How do I create a guest user for a storefront?
  - id: patchApiUserManagementV1UserGuestStorefront
    intent: Register a storefront for a guest user
    question: How do I register a storefront URL for guest access?
  - id: deleteApiUserManagementV1UserGuestByUserId
    intent: Deactivate a guest user
    question: Can I deactivate a guest user?
  - id: putApiUserManagementV1UserGuestByUserId
    intent: Update a guest user
    question: How do I change a guest user's email or name?
  - id: putApiUserManagementV1UserGuestByUserIdRestore
    intent: Restore a deactivated guest user
    question: Can I bring back a guest user I deactivated?
  phrasing_ops: 5
  slug: conga-guest-user-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Health Check API from Conga — 2 operation(s) for health check.
  name: Conga Health Check API
  phrasing_intents:
  - id: getApiConversionManagementV1HealthLive
    intent: Check service liveness
    question: Is the conversion management service alive?
  - id: getApiConversionManagementV1HealthReady
    intent: Check service readiness
    question: Is the conversion service ready to take requests?
  phrasing_ops: 2
  slug: conga-health-check-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Hierarchies API from Conga — 4 operation(s) for hierarchies.
  name: Conga Hierarchies API
  phrasing_intents:
  - id: deleteHierarchies
    intent: Delete hierarchies in bulk
    question: Can I delete multiple hierarchies at once?
  - id: getHierarchies
    intent: List catalog hierarchies
    question: Which catalog hierarchies exist?
  - id: patchHierarchies
    intent: Update hierarchies in bulk
    question: Can I edit several hierarchies in one request?
  - id: postHierarchies
    intent: Create hierarchies
    question: How do I create a new catalog hierarchy?
  - id: deleteHierarchiesById
    intent: Delete a hierarchy
    question: Can I delete a single hierarchy?
  - id: getHierarchiesById
    intent: Get a hierarchy
    question: Where can I see one hierarchy's details?
  - id: patchHierarchiesById
    intent: Update a hierarchy
    question: How do I edit one hierarchy?
  - id: deleteHierarchiesByParentIdPriceListCategories
    intent: Delete price list categories in bulk
    question: Can I remove many price list categories from a hierarchy?
  phrasing_ops: 14
  slug: conga-hierarchies-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The IdvEvidenceSummary API from Conga — 3 operation(s) for idvevidencesummary.
  name: Conga Idv Evidence Summary API
  phrasing_intents:
  - id: IdvEvidenceSummary_GetIdvEvidenceSummary
    intent: Get a package's identity verification evidence
    question: What identity verification evidence was captured for a signing package?
  - id: IdvEvidenceSummary_GetIdvEvidenceSummaryImages
    intent: List IDV verification report image URLs
    question: Which images are in the detailed verification report for a package?
  - id: IdvEvidenceSummary_GetIdvEvidenceSummarySignerImage
    intent: Download an IDV signer image
    question: Can I download the signer's ID image from a verification?
  phrasing_ops: 3
  slug: conga-idvevidencesummary-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The IdvWorkflow API from Conga — 1 operation(s) for idvworkflow.
  name: Conga Idv Workflow API
  phrasing_intents:
  - id: IdvWorkflow_CreateIdvWorkflowConfigs
    intent: Create an IDV workflow configuration
    question: How do I set up a new DV or DVF identity verification workflow?
  - id: IdvWorkflow_DeleteIdvWorkflowConfigs
    intent: Delete the IDV workflow configuration
    question: Can I remove the identity verification workflow from the account?
  - id: IdvWorkflow_GetIdvWorkflowConfigs
    intent: Get the IDV workflow configuration
    question: What identity verification workflow is configured for our signing account?
  - id: IdvWorkflow_UpdateIdvWorkflowConfigs
    intent: Update the IDV workflow configuration
    question: Can I change the existing identity verification workflow settings?
  phrasing_ops: 4
  slug: conga-idvworkflow-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The IFWorkflowConfiguration API from Conga — 1 operation(s) for ifworkflowconfiguration.
  name: Conga IF Workflow Configuration API
  phrasing_intents:
  - id: IFWorkflowConfiguration_GetIFWorkflowConfiguration
    intent: Get IF workflow configuration
    question: What IF workflows are configured for my account?
  phrasing_ops: 1
  slug: conga-ifworkflowconfiguration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ImprintFields API from Conga — 3 operation(s) for imprintfields.
  name: Conga Imprint Fields API
  phrasing_intents:
  - id: ImprintFields_DeleteImprintFields
    intent: Delete all imprint fields from a document
    question: Can I clear every imprint field off a document at once?
  - id: ImprintFields_PostImprintField
    intent: Add an imprint field to a document
    question: How do I stamp a pre-filled imprint field onto a document page?
  - id: ImprintFields_UpdateImprintFields
    intent: Replace all imprint fields on a document
    question: Can I swap out every imprint field on a document in one request?
  - id: ImprintFields_DeleteImprintFields2
    intent: Delete one imprint field
    question: Can I remove just one imprint field and keep the rest?
  - id: ImprintFields_GetExistingImprintField
    intent: Retrieve one imprint field
    question: What value and position does a specific imprint field have?
  - id: ImprintFields_UpdateExistingImprintField
    intent: Update one imprint field
    question: How do I change the text or font size of one existing imprint field?
  - id: ImprintFields_ImprintFieldCopies
    intent: Copy an imprint field to other documents
    question: Can I copy an imprint field to every other document in the package?
  phrasing_ops: 7
  slug: conga-imprintfields-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The In-Effect View API from Conga — 3 operation(s) for in-effect view.
  name: Conga In-Effect View API
  phrasing_intents:
  - id: getApiClmV1ContractsByContractIdInEffectViewClauses
    intent: View in-effect clause changes on a contract
    question: Which clauses are currently in effect after amendments?
  - id: getApiClmV1ContractsByContractIdInEffectViewDetails
    intent: View in-effect detail changes on a contract
    question: What contract details are in effect after all amendments?
  - id: getApiClmV1ContractsByContractIdInEffectViewDocuments
    intent: View in-effect document changes on a contract
    question: Which documents are currently in effect on a contract?
  phrasing_ops: 3
  slug: conga-in-effect-view-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The InAppReports API from Conga — 4 operation(s) for inappreports.
  name: Conga In App Reports API
  phrasing_intents:
  - id: InAppReports_DeleteAllInAppReports
    intent: Delete several report CSV files
    question: How do I delete a set of generated report CSVs?
  - id: InAppReports_GetAllInAppReports
    intent: List report files by date and type
    question: How do I get in-app report files for a date range?
  - id: InAppReports_GetAllInAppReportSummaries
    intent: Get report summaries by date and type
    question: Can I see summaries of reports rather than the full files?
  - id: InAppReports_DeleteInAppReportById
    intent: Delete one report CSV
    question: How do I delete a single report file by its name?
  - id: InAppReports_GetInAppReportById
    intent: Download one report CSV
    question: How do I download a specific report CSV by file name?
  - id: InAppReports_GetInAppReportAsZip
    intent: Download report CSVs as a zip
    question: Can I download several report CSVs bundled in a zip?
  phrasing_ops: 6
  slug: conga-inappreports-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentive Conditions API from Conga — 2 operation(s) for incentive conditions.
  name: Conga Incentive Conditions API
  phrasing_intents:
  - id: deleteRebatesByParentIdConditions
    intent: Delete incentive conditions in bulk
    question: Can I remove many conditions from a rebate?
  - id: getRebatesByParentIdConditions
    intent: List a rebate's incentive conditions
    question: What conditions apply to a rebate?
  - id: patchRebatesByParentIdConditions
    intent: Update incentive conditions in bulk
    question: Can I edit several rebate conditions in one call?
  - id: postRebatesByParentIdConditions
    intent: Create incentive conditions on a rebate
    question: How do I add conditions to a rebate?
  - id: deleteRebatesByParentIdConditionsById
    intent: Delete an incentive condition
    question: Can I delete one condition from a rebate?
  - id: getRebatesByParentIdConditionsById
    intent: Get an incentive condition
    question: Where can I see one rebate condition?
  - id: patchRebatesByParentIdConditionsById
    intent: Update an incentive condition
    question: How do I edit one rebate condition?
  phrasing_ops: 7
  slug: conga-incentive-conditions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentive Coupons API from Conga — 3 operation(s) for incentive coupons.
  name: Conga Incentive Coupons API
  phrasing_intents:
  - id: deleteIncentivesByParentIdCoupons
    intent: Delete incentive coupons in bulk
    question: Can I remove many coupons from an incentive?
  - id: getIncentivesByParentIdCoupons
    intent: List an incentive's coupons
    question: Which coupon codes exist for an incentive?
  - id: patchIncentivesByParentIdCoupons
    intent: Update incentive coupons in bulk
    question: Can I edit several coupons in one request?
  - id: postIncentivesByParentIdCoupons
    intent: Create incentive coupons
    question: How do I add specific coupon codes to an incentive?
  - id: postIncentivesByParentIdCouponsGenerateByNumberOfCoupons
    intent: Auto-generate incentive coupons
    question: Can the system generate a batch of coupon codes for me?
  - id: deleteIncentivesByParentIdCouponsById
    intent: Delete an incentive coupon
    question: Can I delete a single coupon code?
  - id: getIncentivesByParentIdCouponsById
    intent: Get an incentive coupon
    question: Where can I see one coupon's details?
  - id: patchIncentivesByParentIdCouponsById
    intent: Update an incentive coupon
    question: How do I edit one coupon?
  phrasing_ops: 8
  slug: conga-incentive-coupons-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentive Limits API from Conga — 2 operation(s) for incentive limits.
  name: Conga Incentive Limits API
  phrasing_intents:
  - id: deleteIncentivesByParentIdLimits
    intent: Delete incentive limits in bulk
    question: Can I remove many limits from an incentive?
  - id: getIncentivesByParentIdLimits
    intent: List an incentive's limits
    question: What usage limits apply to an incentive?
  - id: patchIncentivesByParentIdLimits
    intent: Update incentive limits in bulk
    question: Can I edit several incentive limits in one call?
  - id: postIncentivesByParentIdLimits
    intent: Create incentive limits
    question: How do I cap how often an incentive can be used?
  - id: deleteIncentivesByParentIdLimitsById
    intent: Delete an incentive limit
    question: Can I delete a single incentive limit?
  - id: getIncentivesByParentIdLimitsById
    intent: Get an incentive limit
    question: Where can I see one incentive limit?
  - id: patchIncentivesByParentIdLimitsById
    intent: Update an incentive limit
    question: How do I change one incentive limit?
  phrasing_ops: 7
  slug: conga-incentive-limits-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentive Programs API from Conga — 2 operation(s) for incentive programs.
  name: Conga Incentive Programs API
  phrasing_intents:
  - id: deleteIncentivePrograms
    intent: Delete incentive programs in bulk
    question: Can I delete several incentive programs at once?
  - id: getIncentivePrograms
    intent: List incentive programs
    question: Which incentive programs are set up?
  - id: patchIncentivePrograms
    intent: Update incentive programs in bulk
    question: Can I edit multiple incentive programs in one request?
  - id: postIncentivePrograms
    intent: Create incentive programs
    question: How do I create a new incentive program?
  - id: deleteIncentiveProgramsById
    intent: Delete an incentive program
    question: Can I delete a single incentive program?
  - id: getIncentiveProgramsById
    intent: Get an incentive program
    question: Where can I see one incentive program?
  - id: patchIncentiveProgramsById
    intent: Update an incentive program
    question: How do I edit one incentive program?
  phrasing_ops: 7
  slug: conga-incentive-programs-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentive Rule Entries API from Conga — 2 operation(s) for incentive rule entries.
  name: Conga Incentive Rule Entries API
  phrasing_intents:
  - id: deleteIncentiveRulesByParentIdEntries
    intent: Delete incentive rule entries in bulk
    question: Can I remove many entries from an incentive rule?
  - id: getIncentiveRulesByParentIdEntries
    intent: List an incentive rule's entries
    question: Which entries make up an incentive rule?
  - id: patchIncentiveRulesByParentIdEntries
    intent: Update incentive rule entries in bulk
    question: Can I edit several rule entries in one call?
  - id: postIncentiveRulesByParentIdEntries
    intent: Create incentive rule entries
    question: How do I add entries to an incentive rule?
  - id: deleteIncentiveRulesByParentIdEntriesById
    intent: Delete an incentive rule entry
    question: Can I delete one entry from an incentive rule?
  - id: getIncentiveRulesByParentIdEntriesById
    intent: Get an incentive rule entry
    question: Where can I see one incentive rule entry?
  - id: patchIncentiveRulesByParentIdEntriesById
    intent: Update an incentive rule entry
    question: How do I edit one incentive rule entry?
  phrasing_ops: 7
  slug: conga-incentive-rule-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentive Rules API from Conga — 2 operation(s) for incentive rules.
  name: Conga Incentive Rules API
  phrasing_intents:
  - id: deleteIncentivesByParentIdRules
    intent: Delete incentive rules in bulk
    question: Can I remove many rules from an incentive?
  - id: getIncentivesByParentIdRules
    intent: List an incentive's rules
    question: Which rules are attached to an incentive?
  - id: patchIncentivesByParentIdRules
    intent: Update incentive rules in bulk
    question: Can I edit several incentive rules in one call?
  - id: postIncentivesByParentIdRules
    intent: Create incentive rules
    question: How do I add rules to an incentive?
  - id: deleteIncentivesByParentIdRulesById
    intent: Delete an incentive rule
    question: Can I delete a single incentive rule?
  - id: getIncentivesByParentIdRulesById
    intent: Get an incentive rule
    question: Where can I see one incentive rule?
  - id: patchIncentivesByParentIdRulesById
    intent: Update an incentive rule
    question: How do I edit one incentive rule?
  phrasing_ops: 7
  slug: conga-incentive-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Incentives API from Conga — 3 operation(s) for incentives.
  name: Conga Incentives API
  phrasing_intents:
  - id: deleteIncentives
    intent: Delete incentives in bulk
    question: Can I delete several incentive definitions at once?
  - id: getIncentives
    intent: List incentives
    question: Which promotions and incentives are defined in the catalog?
  - id: patchIncentives
    intent: Update incentives in bulk
    question: Can I edit multiple incentive definitions in one request?
  - id: postIncentives
    intent: Create incentives
    question: How do I set up a new incentive or promotion?
  - id: deleteIncentivesById
    intent: Delete an incentive
    question: Can I delete a single incentive definition?
  - id: getIncentivesById
    intent: Get an incentive
    question: Where can I see one incentive's setup?
  - id: patchIncentivesById
    intent: Update an incentive
    question: How do I edit one incentive's definition?
  - id: deleteApiCartV1CartsByCartIdIncentives
    intent: Remove an incentive from a cart
    question: Can I take a promo code off my cart?
  phrasing_ops: 11
  slug: conga-incentives-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Index Definition API from Conga — 2 operation(s) for index definition.
  name: Conga Index Definition API
  phrasing_intents:
  - id: postApiSchemaV1ObjectsByObjectNameIndexes
    intent: Index a field on an object
    question: How do I add an index to speed up queries on a field?
  - id: deleteApiSchemaV1ObjectsByObjectNameIndexesByIndexFieldName
    intent: Delete a field index
    question: Can I drop an index I no longer need?
  phrasing_ops: 2
  slug: conga-index-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller to handle Billing Schedule related operations
  name: Conga Initiate Billing API
  phrasing_intents:
  - id: postSchedulesAdjustmentsApplyAdjustment
    intent: Apply adjustments to a billing schedule
    question: How do I apply an adjustment to a billing schedule?
  - id: putSchedulesAdjustmentsUpdateApprovalStage
    intent: Update a billing adjustment's approval stage
    question: How do I move a billing adjustment to the next approval stage?
  - id: postSchedulesAmend
    intent: Amend billing schedules
    question: How do I update billing schedules after an order is amended?
  - id: deleteSchedulesDeleteAdjustments
    intent: Delete billing schedule adjustments
    question: Can I remove adjustment lines from a billing schedule?
  - id: postSchedulesEvergreenRenew
    intent: Renew evergreen billing schedules
    question: How do I extend billing on evergreen subscriptions?
  - id: postSchedulesEvergreenByScheduleIdRenew
    intent: Renew one evergreen billing schedule
    question: Can I renew just a single evergreen schedule?
  - id: postSchedulesInitiate
    intent: Create billing records from order line item status
    question: How do I start billing for activated order line items?
  - id: postSchedulesNew
    intent: Create billing schedules for new sales
    question: How do I create billing schedules for newly sold line items?
  phrasing_ops: 13
  slug: conga-initiate-billing-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The IntelligentImport API from Conga — 5 operation(s) for intelligentimport.
  name: Conga Intelligent Import API
  phrasing_intents:
  - id: postApiXauthorV1IntelligentImportsDocuments
    intent: Extract data from a contract document
    question: How do I extract terms from an uploaded agreement document?
  - id: postApiXauthorV1IntelligentImportsDocumentsMarkClausesAndFields
    intent: Extract and mark clauses and fields
    question: Can intelligent import mark the clauses and fields it finds in a document?
  - id: postApiXauthorV1IntelligentImportsDocumentsRetrievePropertiesByContractId
    intent: Get extracted field and clause properties
    question: What field and clause properties were extracted for a contract?
  - id: getApiXauthorV1IntelligentImportsDocumentsStatusByContractIdByAttachmentId
    intent: Check document extraction status
    question: Has extraction finished for a contract document?
  - id: getApiXauthorV1IntelligentImportsJobsStatusByContractIdByAttachmentId
    intent: Check intelligent import job status
    question: What is the status of the IDE job for an attachment?
  phrasing_ops: 5
  slug: conga-intelligentimport-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The IntelligentImportRisk API from Conga — 4 operation(s) for intelligentimportrisk.
  name: Conga Intelligent Import Risk API
  phrasing_intents:
  - id: postApiXauthorV1IntelligentImportsRisksInsightDelete
    intent: Delete risk insights
    question: Can I delete risk insights recorded for a contract?
  - id: patchApiXauthorV1IntelligentImportsRisksInsights
    intent: Update a risk insight score
    question: Can I change the risk score on a record?
  - id: postApiXauthorV1IntelligentImportsRisksInsights
    intent: Add a risk insight score
    question: How do I record a risk insight for a document?
  - id: postApiXauthorV1IntelligentImportsRisksInsightsQuery
    intent: Get risk insight data
    question: What risk insights exist for a document?
  - id: getApiXauthorV1IntelligentImportsRisksScales
    intent: Get the risk scale
    question: What risk levels and scale does intelligent import use?
  phrasing_ops: 5
  slug: conga-intelligentimportrisk-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides endpoints for configuring and managing invoice run requests.
  name: Conga Invoice Configurations API
  phrasing_intents:
  - id: patchConfigureRequests
    intent: Update an invoice run configuration
    question: How do I change the settings of an existing invoice run?
  - id: postConfigureRequests
    intent: Configure an invoice run
    question: How do I set up an invoice run?
  - id: postConfigureRequestsEstimate
    intent: Preview an invoice run before saving
    question: Can I preview what an invoice run would bill before creating it?
  - id: getConfigureRequestsById
    intent: Get an invoice run configuration
    question: Where can I see the settings of one invoice run?
  - id: postConfigureRequestsByIdClone
    intent: Clone an invoice run configuration
    question: Can I copy an existing invoice run as a new one?
  - id: getConfigureRequestsByIdEstimate
    intent: Preview a saved invoice run
    question: What would a saved invoice run produce if it ran now?
  - id: getConfigureRequestsByIdRequestResults
    intent: Get results of an invoice run configuration
    question: What happened when an invoice run executed?
  phrasing_ops: 7
  slug: conga-invoice-configurations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for managing invoice request results. Provides endpoints to retrieve invoice request result information.
  name: Conga Invoice Request Results API
  phrasing_intents:
  - id: getRequestResultsById
    intent: Get an invoice request result
    question: Where can I see one invoice request result?
  - id: getRequestResultsByIdInvoices
    intent: List invoices from a request result
    question: Which invoices were created by an invoice run result?
  phrasing_ops: 2
  slug: conga-invoice-request-results-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: API controller for managing invoice operations.
  name: Conga Invoices API
  phrasing_intents:
  - id: postInvoicesApprove
    intent: Approve invoices
    question: How do I approve pending invoices?
  - id: postInvoicesCancel
    intent: Cancel invoices
    question: Can I cancel an invoice that was issued in error?
  - id: getInvoicesById
    intent: Get invoice details
    question: Where can I see the details of one invoice?
  phrasing_ops: 3
  slug: conga-invoices-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Handles actions related to workflow jobs
  name: Conga Jobs API
  phrasing_intents:
  - id: Jobs_Get
    intent: Get a workflow job and its results
    question: What is the status of a document generation job?
  phrasing_ops: 1
  slug: conga-jobs-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Json API from Conga — 2 operation(s) for json.
  name: Conga JSON API
  phrasing_intents:
  - id: Json_DataSchemaProcess
    intent: Get the data schema JSON
    question: How do I get the JSON data schema for my merge data?
  - id: Json_DataTranslateProcess
    intent: Translate JSON data
    question: Can I send JSON data to be translated into the merge data format?
  phrasing_ops: 2
  slug: conga-json-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Layout API from Conga — 2 operation(s) for layout.
  name: Conga Layout API
  phrasing_intents:
  - id: Layout_CreateLayout
    intent: Create a document layout
    question: How do I save a reusable layout of signature fields?
  - id: Layout_GetLayouts
    intent: List document layouts
    question: Which signing layouts do I have available?
  - id: getApiXauthorV1LayoutsByLayoutName
    intent: Get an X-Author page layout's fields
    question: Which page fields does an X-Author layout define?
  phrasing_ops: 3
  slug: conga-layout-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Catalog APIs for Locations
  name: Conga Locations API
  phrasing_intents:
  - id: getLocations
    intent: List account locations
    question: Which locations does an account have?
  phrasing_ops: 1
  slug: conga-locations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: LockController
  name: Conga Lock API
  phrasing_intents:
  - id: postApiCartV1CartsByCartIdLock
    intent: Lock a cart for editing
    question: How do I get edit access to a shared cart?
  - id: deleteApiCartV1CartsByCartIdUnlock
    intent: Release a cart lock
    question: How do I release my edit lock on a cart?
  phrasing_ops: 2
  slug: conga-lock-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs for application logs.
  name: Conga Log API
  phrasing_intents:
  - id: postApiXauthorV1Logs
    intent: Log application exceptions
    question: How do I report X-Author application errors?
  - id: postApiXauthorV1LogsCustomMetrics
    intent: Log custom metrics
    question: Can I record custom usage metrics for an X-Author user?
  phrasing_ops: 2
  slug: conga-log-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Lookup Field Settings API from Conga — 2 operation(s) for lookup field settings.
  name: Conga Lookup Field Settings API
  phrasing_intents:
  - id: deleteLookupfieldSettings
    intent: Delete lookup field settings in bulk
    question: Can I delete several lookup field settings at once?
  - id: getLookupfieldSettings
    intent: List lookup field settings
    question: Which lookup field settings are configured?
  - id: patchLookupfieldSettings
    intent: Update lookup field settings in bulk
    question: Can I edit multiple lookup field settings in one request?
  - id: postLookupfieldSettings
    intent: Create lookup field settings
    question: How do I configure a new lookup field setting?
  - id: deleteLookupfieldSettingsById
    intent: Delete a lookup field setting
    question: Can I delete a single lookup field setting?
  - id: getLookupfieldSettingsById
    intent: Get a lookup field setting
    question: Where can I see one lookup field setting?
  - id: patchLookupfieldSettingsById
    intent: Update a lookup field setting
    question: How do I edit one lookup field setting?
  phrasing_ops: 7
  slug: conga-lookup-field-settings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Lookup Field Data Controller
  name: Conga Lookup Field Data API
  phrasing_intents:
  - id: postApiCartV1LookupfieldDataQuery
    intent: Query lookup field records
    question: What records can I pick for a lookup field in the cart?
  phrasing_ops: 1
  slug: conga-lookupfielddata-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This controller initiates Composer API Merge
  name: Conga Merge API
  phrasing_intents:
  - id: Merge_Post
    intent: Start a Composer document merge
    question: How do I generate a document by merging data into a template with Conga Composer?
  - id: Merge_GetPreviewFiles
    intent: Get preview and merged document URLs
    question: Where can I download the preview of a merged document?
  - id: Merge_Upload
    intent: Start a merge from an uploaded JSON file
    question: Can I upload a JSON data file and local templates to run a merge?
  - id: Merge_AcceptPreview
    intent: Accept a previewed merge
    question: How do I approve a merge that is waiting in preview so post-merge actions run?
  - id: Merge_RejectPreview
    intent: Reject a previewed merge
    question: Can I stop a merge in preview so nothing is delivered?
  - id: Merge_Get
    intent: Get merge information
    question: What is the status and info of a merge I started?
  phrasing_ops: 6
  slug: conga-merge-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Migration API from Conga — 1 operation(s) for migration.
  name: Conga Migration API
  phrasing_intents:
  - id: Migration_RunMigration
    intent: Fix finalized solutions stuck in Draft status
    question: Can I bulk-correct finalized solutions that still show as Draft?
  phrasing_ops: 1
  slug: conga-migration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Milestone Schedule API from Conga — 7 operation(s) for milestone schedule.
  name: Conga Milestone Schedule API
  phrasing_intents:
  - id: putMilestoneComplete
    intent: Mark milestone billing details complete
    question: How do I mark a billing milestone as complete?
  - id: postMilestoneHeader
    intent: Get milestone details for several billing headers
    question: Can I get milestone billing details for many billing headers at once?
  - id: postMilestoneHeaderByBillingHeaderId
    intent: Get milestone details for one billing header
    question: Which milestones are due on a single billing header?
  - id: postMilestoneOrderLineItem
    intent: Get milestone details for several order line items
    question: Can I see milestone billing for multiple order line items?
  - id: postMilestoneOrderLineItemByOrderLineItemId
    intent: Get milestone details for one order line item
    question: What billing milestones exist for one order line?
  - id: postMilestoneScheduleRecord
    intent: Get milestone schedules by several record IDs
    question: Can I look up milestone-type schedules for several schedule records?
  - id: postMilestoneScheduleRecordByScheduleRecordId
    intent: Get milestone schedule by a record ID
    question: What milestone schedule details does one schedule record have?
  phrasing_ops: 7
  slug: conga-milestone-schedule-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Notification API from Conga — 5 operation(s) for notification.
  name: Conga Notification API
  phrasing_intents:
  - id: Notification_ResendMobileNotificationsForPackageDocumentApproval
    intent: Send myself a mobile signing link for an approval
    question: Can I send myself a link to sign a specific approval on my phone?
  - id: Notification_ResendNotificationsForPackage
    intent: Resend the signing email to a signer
    question: How do I resend the signing invitation email to a signer who lost it?
  - id: Notification_ResendNotificationsForPackageAndRole
    intent: Resend notification to a role's signers
    question: How do I re-notify every signer linked to one role of a package?
  - id: Notification_ResendSMSNotificationsForPackageAndRole
    intent: Send an SMS signing notification to a role
    question: How do I text a signing reminder to the signers of a role?
  - id: Notification_ResendSMSCodeForSigner
    intent: Resend a signer's SMS verification code
    question: My signer didn't get their SMS authentication code. Can I resend it?
  phrasing_ops: 5
  slug: conga-notification-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Object Definition API from Conga — 6 operation(s) for object definition.
  name: Conga Object Definition API
  phrasing_intents:
  - id: getApiSchemaV1Objects
    intent: List object names
    question: Which objects exist in the schema?
  - id: postApiSchemaV1Objects
    intent: Define a new object
    question: How do I create a new custom object?
  - id: postApiSchemaV1ObjectsCustomschemaImport
    intent: Import a custom schema
    question: Can I import a custom schema from a file?
  - id: postApiSchemaV1ObjectsByLookupObjectNameLookupCriteriaValidate
    intent: Validate lookup criteria
    question: Is my lookup filter criteria valid for an object?
  - id: getApiSchemaV1ObjectsByObjectName
    intent: Get a translated object definition
    question: Can I see an object's schema translated into another locale?
  - id: putApiSchemaV1ObjectsByObjectName
    intent: Update an object definition
    question: How do I rename an object's display label?
  - id: patchApiSchemaV1ObjectsByObjectNameDeprecate
    intent: Deprecate an object
    question: Can I mark an object as deprecated?
  - id: putApiSchemaV1ObjectsByObjectNameSharedByIsShared
    intent: Set an object's shared status
    question: Can I share an object across apps?
  phrasing_ops: 8
  slug: conga-object-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Object Definition Translation API from Conga — 1 operation(s) for object definition translation.
  name: Conga Object Definition Translation API
  phrasing_intents:
  - id: deleteApiSchemaV1ObjectsByObjectNameTranslationsByLocale
    intent: Delete an object translation
    question: Can I remove a translation for an object?
  - id: getApiSchemaV1ObjectsByObjectNameTranslationsByLocale
    intent: Get an object translation
    question: What are the translated labels of an object in a locale?
  - id: postApiSchemaV1ObjectsByObjectNameTranslationsByLocale
    intent: Define an object translation
    question: How do I add a new language translation for an object?
  - id: putApiSchemaV1ObjectsByObjectNameTranslationsByLocale
    intent: Update an object translation
    question: How do I change an existing object translation?
  phrasing_ops: 4
  slug: conga-object-definition-translation-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Object Metadata API from Conga — 8 operation(s) for object metadata.
  name: Conga Object Metadata API
  phrasing_intents:
  - id: getApiMetadataV1Objects
    intent: List scoped object names
    question: Which objects are in scope for my metadata?
  - id: postApiMetadataV1ObjectsCustomschemaExport
    intent: Export the custom schema
    question: Can I export my custom schema definitions?
  - id: getApiMetadataV1ObjectsByObjectName
    intent: Get an object's metadata
    question: What fields and settings does an object have?
  - id: getApiMetadataV1ObjectsByObjectNameDependencies
    intent: List an object's dependencies
    question: What depends on a given object?
  - id: getApiMetadataV1ObjectsByObjectNameFieldsByFieldName
    intent: Get field metadata
    question: What type and settings does a field have?
  - id: getApiMetadataV1ObjectsByObjectNameFieldsByFieldNameDependencyFields
    intent: List a field's dependencies
    question: Which other fields depend on a field?
  - id: getApiMetadataV1ObjectsByObjectNameFieldsByFieldNameDependentPicklists
    intent: Get a dependent picklist definition
    question: How is a dependent picklist wired to its controlling field?
  - id: getApiMetadataV1ObjectsByObjectNameReferences
    intent: List an object's references
    question: Which objects reference a given object?
  phrasing_ops: 8
  slug: conga-object-metadata-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Object Permission API from Conga — 6 operation(s) for object permission.
  name: Conga Object Permission API
  phrasing_intents:
  - id: getApiUserManagementV1Objectpermissions
    intent: List object permissions
    question: What object permissions are configured?
  - id: postApiUserManagementV1Objectpermissions
    intent: Create an object permission
    question: How do I give a permission group access to an object?
  - id: deleteApiUserManagementV1ObjectpermissionsBulk
    intent: Delete object permissions in bulk
    question: Can I remove many object permissions at once?
  - id: postApiUserManagementV1ObjectpermissionsBulk
    intent: Create object permissions in bulk
    question: Can I create many object permissions at once?
  - id: getApiUserManagementV1ObjectpermissionsObjects
    intent: List objects available for permissions
    question: Which objects can I set permissions on?
  - id: getApiUserManagementV1ObjectpermissionsObjectsByObjectName
    intent: Get permissions for an object
    question: Who has access to a given object?
  - id: getApiUserManagementV1ObjectpermissionsByObjectNameActionpermissionsByActionNameValidate
    intent: Check an action permission on an object
    question: Am I allowed to perform a given action on an object?
  - id: deleteApiUserManagementV1ObjectpermissionsByObjectPermissionId
    intent: Delete an object permission
    question: Can I remove one object permission?
  phrasing_ops: 10
  slug: conga-object-permission-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for managing obligations.
  name: Conga Obligations API
  phrasing_intents:
  - id: postApiClmV1ObligationsActivatedContracts
    intent: List activated contracts with obligations
    question: Which activated contracts carry obligations?
  phrasing_ops: 1
  slug: conga-obligations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The OneSpanPackage API from Conga — 1 operation(s) for onespanpackage.
  name: Conga One Span Package API
  phrasing_intents:
  - id: OneSpanPackage_ListPackages
    intent: List all document packages
    question: How do I list every package in my account?
  phrasing_ops: 1
  slug: conga-onespanpackage-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The OneSpanUrl API from Conga — 1 operation(s) for onespanurl.
  name: Conga One Span URL API
  phrasing_intents:
  - id: OneSpanUrl_Get
    intent: Get OneSpan base URLs by region
    question: Which OneSpan base URL should I use for my region?
  phrasing_ops: 1
  slug: conga-onespanurl-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The OpenSearchSyncAudit API from Conga — 1 operation(s) for opensearchsyncaudit.
  name: Conga Open Search Sync Audit API
  phrasing_intents:
  - id: getOpenSearchSyncAudit
    intent: Get search sync audit records
    question: Did records sync correctly to the search index?
  phrasing_ops: 1
  slug: conga-opensearchsyncaudit-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Opportunity API from Conga — 7 operation(s) for opportunity.
  name: Conga Opportunity API
  phrasing_intents:
  - id: getApiDataV1Opportunity
    intent: List opportunity records
    question: Which opportunities do we have?
  - id: postApiDataV1Opportunity
    intent: Create an opportunity
    question: How do I add a new sales opportunity?
  - id: deleteApiDataV1OpportunityBulk
    intent: Delete multiple opportunities
    question: Can I delete many opportunities at once?
  - id: patchApiDataV1OpportunityBulk
    intent: Upsert multiple opportunities
    question: Can I insert-or-update opportunities in one call?
  - id: postApiDataV1OpportunityBulk
    intent: Create multiple opportunities
    question: Can I insert several opportunities in one request?
  - id: putApiDataV1OpportunityBulk
    intent: Update multiple opportunities
    question: Can I update many opportunities at once?
  - id: deleteApiDataV1OpportunityByExternalIdByExternalId
    intent: Delete an opportunity by external ID
    question: Can I delete an opportunity using its external ID?
  - id: getApiDataV1OpportunityByExternalIdByExternalId
    intent: Get an opportunity by external ID
    question: Can I look up an opportunity using our external system ID?
  phrasing_ops: 15
  slug: conga-opportunity-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Option Group Members API from Conga — 2 operation(s) for option group members.
  name: Conga Option Group Members API
  phrasing_intents:
  - id: deleteOptionGroupsByParentIdProducts
    intent: Remove option group members in bulk
    question: Can I remove many products from an option group?
  - id: getOptionGroupsByParentIdProducts
    intent: List option group members
    question: Which products are members of an option group?
  - id: patchOptionGroupsByParentIdProducts
    intent: Update option group members in bulk
    question: Can I edit several option group members in one call?
  - id: postOptionGroupsByParentIdProducts
    intent: Add products to an option group
    question: How do I add products as options in a group?
  - id: deleteOptionGroupsByParentIdProductsById
    intent: Remove an option group member
    question: Can I remove a single product from an option group?
  - id: getOptionGroupsByParentIdProductsById
    intent: Get an option group member
    question: Where can I see one option group member?
  - id: patchOptionGroupsByParentIdProductsById
    intent: Update an option group member
    question: How do I edit one option group member?
  phrasing_ops: 7
  slug: conga-option-group-members-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Option Groups API from Conga — 8 operation(s) for option groups.
  name: Conga Option Groups API
  phrasing_intents:
  - id: deleteOptionGroups
    intent: Delete option groups in bulk
    question: Can I delete several option groups at once?
  - id: getOptionGroups
    intent: List option groups
    question: Which option groups are defined for bundles?
  - id: patchOptionGroups
    intent: Update option groups in bulk
    question: Can I edit multiple option groups in one request?
  - id: postOptionGroups
    intent: Create option groups
    question: How do I create new option groups?
  - id: deleteOptionGroupsById
    intent: Delete an option group
    question: Can I delete a single option group?
  - id: getOptionGroupsById
    intent: Get an option group
    question: Where can I see one option group's details?
  - id: patchOptionGroupsById
    intent: Update an option group
    question: How do I edit one option group?
  - id: getOptionGroupsByIdBundles
    intent: List bundles using an option group
    question: Which bundle products use a given option group?
  phrasing_ops: 13
  slug: conga-option-groups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Orchestrate API from Conga — 1 operation(s) for orchestrate.
  name: Conga Orchestrate API
  phrasing_intents:
  - id: Orchestrate_MergeGET
    intent: Call the orchestrated merge endpoint via GET
    question: Is there a GET form of the v2 orchestrate merge endpoint?
  - id: Orchestrate_MergePOST
    intent: Start an orchestrated document merge
    question: Can I kick off a document merge through the v2 orchestration endpoint?
  phrasing_ops: 2
  slug: conga-orchestrate-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Organization API from Conga — 4 operation(s) for organization.
  name: Conga Organization API
  phrasing_intents:
  - id: getApiUserManagementV1OrganizationCurrency
    intent: Get the organization currency
    question: What currency is my organization set to?
  - id: getApiUserManagementV1OrganizationInfo
    intent: Get organization information
    question: What details are stored about my organization?
  - id: patchApiUserManagementV1OrganizationInfo
    intent: Update organization information
    question: How do I change my organization's time zone or currency?
  - id: getApiUserManagementV1OrganizationLocale
    intent: Get the organization locale
    question: Which locale does my organization use?
  - id: getApiUserManagementV1OrganizationTimezone
    intent: Get the organization time zone
    question: What time zone is my organization in?
  phrasing_ops: 5
  slug: conga-organization-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Organization External Integration API from Conga — 4 operation(s) for organization external integration.
  name: Conga Organization External Integration API
  phrasing_intents:
  - id: deleteApiUserManagementV1Integrations
    intent: Delete external identifiers
    question: Can I remove all external identifiers from the org?
  - id: getApiUserManagementV1Integrations
    intent: List external integration identifiers
    question: Which external integrations are linked to our org?
  - id: postApiUserManagementV1Integrations
    intent: Add an external identity integration
    question: How do I connect a SAML identity provider?
  - id: putApiUserManagementV1Integrations
    intent: Update external identifiers
    question: How do I update several external identifiers at once?
  - id: getApiUserManagementV1IntegrationsIdentityProviders
    intent: List identity providers
    question: Which identity providers can we sign in with?
  - id: deleteApiUserManagementV1IntegrationsByExternalIntegrationId
    intent: Remove one integration's identifiers
    question: Can I remove the identifiers of a single integration?
  - id: getApiUserManagementV1IntegrationsByExternalIntegrationId
    intent: Get identifiers for an integration
    question: Which identifiers belong to one external integration?
  - id: postApiUserManagementV1IntegrationsByExternalIntegrationId
    intent: Add identifiers to one integration
    question: Can I add more identifiers to an existing integration?
  phrasing_ops: 10
  slug: conga-organization-external-integration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Package API from Conga — 12 operation(s) for package.
  name: Conga Package API
  phrasing_intents:
  - id: Package_CreatePackage
    intent: Create a package or template
    question: How do I create a new signing transaction without attachments?
  - id: Package_ListPackages
    intent: List document packages
    question: How do I list the signing packages in my Conga Sign account?
  - id: Package_DeletePackageById
    intent: Delete a package or template
    question: How do I permanently delete a package?
  - id: Package_GetPackageById
    intent: Get a package's details
    question: How do I look up a package's status, roles and documents?
  - id: Package_UpdatePackage
    intent: Update a package
    question: How do I change the name or due date of an existing package?
  - id: Package_GetPackageAudit
    intent: Get a package's audit trail
    question: Where can I see the audit trail of who did what on a package?
  - id: Package_CreatePackagesUsingBulkSend
    intent: Bulk send packages from a template
    question: How do I send the same template to many signers using bulk send?
  - id: Package_CreatePackageClone
    intent: Clone a package or template
    question: Can I make a new package by copying an existing one?
  phrasing_ops: 15
  slug: conga-package-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Package Deployment API from Conga — 8 operation(s) for package deployment.
  name: Conga Package Deployment API
  phrasing_intents:
  - id: getApiExtensibilityV2DeploymentHistory
    intent: List package deployment history
    question: What custom code packages have been deployed?
  - id: postApiExtensibilityV2DeploymentPackageDeploy
    intent: Deploy a source package
    question: How do I deploy a custom code package?
  - id: postApiExtensibilityV2DeploymentPackagePromote
    intent: Promote a package to another environment
    question: How do I promote a package to production?
  - id: getApiExtensibilityV2DeploymentPackageByNameHistory
    intent: Get a package's deployment history
    question: Where has a particular package been deployed?
  - id: getApiExtensibilityV2DeploymentPackageByNameInfo
    intent: Get package information
    question: What version and details does a package have?
  - id: postApiExtensibilityV2DeploymentPackageByNameRollback
    intent: Roll back a package deployment
    question: Can I undo a custom code deployment?
  - id: getApiExtensibilityV2DeploymentByDeploymentIdLogs
    intent: Get deployment logs
    question: Why did a package deployment fail?
  - id: getApiExtensibilityV2DeploymentByDeploymentIdStatus
    intent: Track deployment status
    question: Is my package deployment finished?
  phrasing_ops: 8
  slug: conga-package-deployment-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for package migration.
  name: Conga Package Migration API
  phrasing_intents:
  - id: postApiXauthorV1TemplateMigrationExport
    intent: Export a template migration package
    question: How do I export X-Author templates for migration?
  - id: postApiXauthorV1TemplateMigrationImport
    intent: Import a template migration package
    question: How do I import X-Author templates into another org?
  phrasing_ops: 2
  slug: conga-packagemigration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for managing payment terms.
  name: Conga Payment Terms API
  phrasing_intents:
  - id: getPaymentTerms
    intent: List payment terms
    question: Which payment terms are configured?
  - id: patchPaymentTerms
    intent: Update payment terms
    question: Can I edit several payment terms in one request?
  - id: postPaymentTerms
    intent: Create payment terms
    question: How do I add a new payment term?
  - id: patchPaymentTermsActivate
    intent: Activate or deactivate payment terms in bulk
    question: Can I switch several payment terms on or off at once?
  - id: getPaymentTermsById
    intent: Get a payment term
    question: Where can I see one payment term?
  - id: putPaymentTermsByIdDefault
    intent: Make a payment term the default
    question: How do I set the default payment term?
  - id: patchPaymentTermsByPaymentTermIdActivate
    intent: Activate or deactivate one payment term
    question: Can I deactivate a single payment term?
  phrasing_ops: 7
  slug: conga-payment-terms-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Permission Groups API from Conga — 2 operation(s) for permission groups.
  name: Conga Permission Groups API
  phrasing_intents:
  - id: deleteApiUserManagementV1Permissiongroups
    intent: Delete permission groups
    question: Can I delete permission groups?
  - id: getApiUserManagementV1Permissiongroups
    intent: List permission groups
    question: Which permission groups exist?
  - id: postApiUserManagementV1Permissiongroups
    intent: Add permission groups
    question: How do I create new permission groups?
  - id: postApiUserManagementV1PermissiongroupsByPermissionGroupNameClone
    intent: Clone a permission group
    question: Can I copy an existing permission group's access?
  phrasing_ops: 4
  slug: conga-permission-groups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Picklist Definition API from Conga — 6 operation(s) for picklist definition.
  name: Conga Picklist Definition API
  phrasing_intents:
  - id: postApiSchemaV1ObjectsByObjectNamePicklists
    intent: Create a picklist
    question: How do I add a new picklist to an object?
  - id: patchApiSchemaV1ObjectsByObjectNamePicklistsRename
    intent: Rename a picklist
    question: Can I rename an existing picklist?
  - id: putApiSchemaV1ObjectsByObjectNamePicklistsByPicklistName
    intent: Update a picklist
    question: Can I deprecate a picklist?
  - id: postApiSchemaV1ObjectsByObjectNamePicklistsByPicklistNamePicklistEntries
    intent: Add a picklist entry
    question: How do I add one value to a picklist?
  - id: postApiSchemaV1ObjectsByObjectNamePicklistsByPicklistNamePicklistEntriesBulk
    intent: Add picklist entries in bulk
    question: Can I add many values to a picklist in one call?
  - id: putApiSchemaV1ObjectsByObjectNamePicklistsByPicklistNamePicklistEntriesBulk
    intent: Update picklist entries in bulk
    question: Can I edit many picklist values at once?
  - id: putApiSchemaV1ObjectsByObjectNamePicklistsByPicklistNamePicklistEntriesByPicklistEntryValue
    intent: Update one picklist entry
    question: How do I change the label of one picklist value?
  phrasing_ops: 7
  slug: conga-picklist-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The PlatformComposerFeatureFlag API from Conga — 1 operation(s) for platformcomposerfeatureflag.
  name: Conga Platform Composer Feature Flag API
  phrasing_intents:
  - id: PlatformComposerFeatureFlag_Get
    intent: Check a Composer feature flag for an org
    question: Is a given Composer feature flag turned on for our Salesforce org?
  phrasing_ops: 1
  slug: conga-platformcomposerfeatureflag-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides API endpoints for managing playbooks associated with a contract. Supports retrieving available playbooks, playbook rules, and matched playbooks based on contract metadata.
  name: Conga Playbook API
  phrasing_intents:
  - id: getApiXauthorV1ContractsByContractIdPlaybooks
    intent: List playbooks for a contract
    question: Which playbooks apply to a contract's type and legal entity?
  - id: getApiXauthorV1ContractsByContractIdPlaybooksMatch
    intent: Find playbooks that match a contract
    question: Which playbooks match a specific contract?
  - id: getApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdRules
    intent: List playbook rules for a contract
    question: Which playbook rules apply to a contract?
  phrasing_ops: 3
  slug: conga-playbook-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides API endpoints for executing playbooks against contract documents and retrieving playbook execution results including clause and document rule outcomes.
  name: Conga Playbook Execution API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdExecute
    intent: Run a playbook against a document
    question: How do I review a contract document with a playbook?
  - id: postApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdExecutionsByExecutionIdResults
    intent: Get playbook execution results
    question: What did a playbook review find in my contract?
  phrasing_ops: 2
  slug: conga-playbookexecution-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Billing Preference Controller
  name: Conga Preferences API
  phrasing_intents:
  - id: getPreferences
    intent: List billing preferences
    question: Which billing preferences are configured?
  - id: patchPreferences
    intent: Update billing preferences
    question: Can I edit several billing preferences in one request?
  - id: postPreferences
    intent: Create billing preferences
    question: How do I create a new billing preference?
  - id: patchPreferencesActivate
    intent: Activate or deactivate preferences in bulk
    question: Can I switch several billing preferences on or off at once?
  - id: patchPreferencesByIdDefault
    intent: Make a preference the default
    question: How do I set the default billing preference?
  - id: getPreferencesByPreferenceId
    intent: Get a billing preference
    question: Where can I see one billing preference?
  - id: patchPreferencesByPreferenceIdActivate
    intent: Activate or deactivate one preference
    question: Can I deactivate a single billing preference?
  phrasing_ops: 7
  slug: conga-preferences-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Preview API from Conga — 1 operation(s) for preview.
  name: Conga Preview API
  phrasing_intents:
  - id: Preview_MergeTemplate
    intent: Preview a template merged with data
    question: Can I preview what a template looks like merged with sample data?
  phrasing_ops: 1
  slug: conga-preview-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Dimensions API from Conga — 3 operation(s) for price dimensions.
  name: Conga Price Dimensions API
  phrasing_intents:
  - id: deletePriceDimensions
    intent: Delete price dimensions in bulk
    question: Can I delete several price dimensions at once?
  - id: getPriceDimensions
    intent: List price dimensions
    question: Which price dimensions are defined?
  - id: patchPriceDimensions
    intent: Update price dimensions in bulk
    question: Can I edit multiple price dimensions in one request?
  - id: postPriceDimensions
    intent: Create price dimensions
    question: How do I create a new price dimension?
  - id: deletePriceDimensionsById
    intent: Delete a price dimension
    question: Can I delete a single price dimension?
  - id: getPriceDimensionsById
    intent: Get a price dimension
    question: Where can I see one price dimension?
  - id: patchPriceDimensionsById
    intent: Update a price dimension
    question: How do I edit one price dimension?
  - id: getPriceDimensionsByNameDatasourceValue
    intent: Get a price dimension's data source value
    question: What value does a price dimension resolve to for a record?
  phrasing_ops: 8
  slug: conga-price-dimensions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Lists API from Conga — 9 operation(s) for price lists.
  name: Conga Price Lists API
  phrasing_intents:
  - id: deletePriceLists
    intent: Delete price lists in bulk
    question: Can I delete several price lists at once?
  - id: getPriceLists
    intent: List price lists
    question: Which price lists do we have?
  - id: patchPriceLists
    intent: Update price lists in bulk
    question: Can I edit multiple price lists in one request?
  - id: postPriceLists
    intent: Create price lists
    question: How do I create a new price list?
  - id: deletePriceListsById
    intent: Delete a price list
    question: Can I delete a single price list?
  - id: getPriceListsById
    intent: Get a price list
    question: Where can I see one price list's details?
  - id: patchPriceListsById
    intent: Update a price list
    question: How do I edit one price list?
  - id: getPriceListsByIdProducts
    intent: Look up products available for a price list
    question: Which product lookup records can I pick for a price list?
  phrasing_ops: 25
  slug: conga-price-lists-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Matrices API from Conga — 2 operation(s) for price matrices.
  name: Conga Price Matrices API
  phrasing_intents:
  - id: deleteMatrices
    intent: Delete price matrices in bulk
    question: Can I delete several price matrices at once?
  - id: getMatrices
    intent: List price matrices
    question: Which price matrices are defined?
  - id: patchMatrices
    intent: Update price matrices in bulk
    question: Can I edit multiple price matrices in one request?
  - id: postMatrices
    intent: Create price matrices
    question: How do I create a new price matrix?
  - id: deleteMatricesById
    intent: Delete a price matrix
    question: Can I delete a single price matrix?
  - id: getMatricesById
    intent: Get a price matrix
    question: Where can I see one price matrix?
  - id: patchMatricesById
    intent: Update a price matrix
    question: How do I edit one price matrix?
  phrasing_ops: 7
  slug: conga-price-matrices-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Matrix Entries API from Conga — 2 operation(s) for price matrix entries.
  name: Conga Price Matrix Entries API
  phrasing_intents:
  - id: deleteMatricesByParentIdMatrixEntries
    intent: Delete price matrix entries in bulk
    question: Can I remove many entries from a price matrix?
  - id: getMatricesByParentIdMatrixEntries
    intent: List price matrix entries
    question: What entries does a price matrix contain?
  - id: patchMatricesByParentIdMatrixEntries
    intent: Update price matrix entries in bulk
    question: Can I edit several matrix entries in one call?
  - id: postMatricesByParentIdMatrixEntries
    intent: Create price matrix entries
    question: How do I add rows to a price matrix?
  - id: deleteMatricesByParentIdMatrixEntriesById
    intent: Delete a price matrix entry
    question: Can I delete one row from a price matrix?
  - id: getMatricesByParentIdMatrixEntriesById
    intent: Get a price matrix entry
    question: Where can I see one price matrix entry?
  - id: patchMatricesByParentIdMatrixEntriesById
    intent: Update a price matrix entry
    question: How do I change one price matrix entry?
  phrasing_ops: 7
  slug: conga-price-matrix-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Program Associations API from Conga — 5 operation(s) for price program associations.
  name: Conga Price Program Associations API
  phrasing_intents:
  - id: deleteBusinessObjectsByBusinessObjectIdPriceProgramAssociations
    intent: Remove price programs from a business object
    question: Can I detach price programs from an account or other business object?
  - id: getBusinessObjectsByBusinessObjectIdPricePrograms
    intent: List price programs on a business object
    question: Which price programs are linked to a business object?
  - id: postPriceProgramAssociations
    intent: Associate price programs with business objects
    question: How do I link a price program to accounts or other business objects?
  - id: getPriceProgramsByPriceProgramIdBusinessObjects
    intent: List business objects on a price program
    question: Which accounts or business objects belong to a price program?
  - id: deletePriceProgramsByPriceProgramIdPriceProgramAssociations
    intent: Remove business objects from a price program
    question: Can I detach business objects from a price program?
  phrasing_ops: 5
  slug: conga-price-program-associations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Program Rule Entries API from Conga — 2 operation(s) for price program rule entries.
  name: Conga Price Program Rule Entries API
  phrasing_intents:
  - id: deletePriceProgramRulesByParentIdEntries
    intent: Delete several entries from an incentive rule
    question: How do I remove many entries from an incentive rule at once?
  - id: getPriceProgramRulesByParentIdEntries
    intent: List the entries of a price program incentive rule
    question: How do I see every entry defined under one of my price program incentive rules?
  - id: patchPriceProgramRulesByParentIdEntries
    intent: Update several entries of an incentive rule at once
    question: How can I edit many incentive rule entries in a single bulk update?
  - id: postPriceProgramRulesByParentIdEntries
    intent: Add entries to a price program incentive rule
    question: How can I add several new entries to an incentive rule in one request?
  - id: deletePriceProgramRulesByParentIdEntriesById
    intent: Delete one entry from an incentive rule
    question: How do I delete just one entry from an incentive rule?
  - id: getPriceProgramRulesByParentIdEntriesById
    intent: Get one entry of an incentive rule
    question: How do I look up a single incentive rule entry by its ID?
  - id: patchPriceProgramRulesByParentIdEntriesById
    intent: Update one entry of an incentive rule
    question: How do I change the values on one specific incentive rule entry?
  phrasing_ops: 7
  slug: conga-price-program-rule-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Program Rules API from Conga — 2 operation(s) for price program rules.
  name: Conga Price Program Rules API
  phrasing_intents:
  - id: deletePriceProgramsByParentIdRules
    intent: Delete several incentive rules from a price program
    question: How can I bulk remove many rules from an incentive at once?
  - id: getPriceProgramsByParentIdRules
    intent: List the incentive rules of a price program
    question: How do I see all the incentive rules attached to one price program?
  - id: patchPriceProgramsByParentIdRules
    intent: Update several incentive rules of a price program
    question: Can I edit many incentive rules of a price program in one bulk update?
  - id: postPriceProgramsByParentIdRules
    intent: Add incentive rules to a price program
    question: What's the way to add several new rules to an incentive in one call?
  - id: deletePriceProgramsByParentIdRulesById
    intent: Delete one incentive rule from a price program
    question: How do I delete a single incentive rule from a price program?
  - id: getPriceProgramsByParentIdRulesById
    intent: Get one incentive rule of a price program
    question: How do I look up a single incentive rule by its ID?
  - id: patchPriceProgramsByParentIdRulesById
    intent: Update one incentive rule of a price program
    question: What do I call to change the settings of one incentive rule?
  phrasing_ops: 7
  slug: conga-price-program-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Programs API from Conga — 2 operation(s) for price programs.
  name: Conga Price Programs API
  phrasing_intents:
  - id: deletePricePrograms
    intent: Delete several incentives at once
    question: How can I bulk delete multiple incentives?
  - id: getPricePrograms
    intent: List price program incentives
    question: How do I see all the price program incentives set up in Conga CPQ?
  - id: patchPricePrograms
    intent: Update several incentives at once
    question: Can I update many incentives together in one bulk call?
  - id: postPricePrograms
    intent: Create several incentives at once
    question: What's the way to create several new incentives in a single request?
  - id: deletePriceProgramsById
    intent: Delete one incentive
    question: How do I delete a single incentive by its ID?
  - id: getPriceProgramsById
    intent: Get one incentive by ID
    question: How do I look up a single incentive by its identifier?
  - id: patchPriceProgramsById
    intent: Update one incentive
    question: What do I call to change the details of one specific incentive?
  phrasing_ops: 7
  slug: conga-price-programs-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Rule Entries API from Conga — 2 operation(s) for price rule entries.
  name: Conga Price Rule Entries API
  phrasing_intents:
  - id: deleteRulesByParentIdRuleEntries
    intent: Delete several entries from a price rule
    question: How can I bulk delete entries from a condition or dimension price rule?
  - id: getRulesByParentIdRuleEntries
    intent: List the entries of a price rule
    question: How do I see all the entries inside one of my price rules?
  - id: patchRulesByParentIdRuleEntries
    intent: Update several entries of a price rule
    question: Can I change fields on many price rule entries in one bulk update?
  - id: postRulesByParentIdRuleEntries
    intent: Add entries to a price rule
    question: What's the way to add several new entries to a price rule at once?
  - id: deleteRulesByParentIdRuleEntriesById
    intent: Delete one entry from a price rule
    question: How do I delete just one entry from a price rule?
  - id: getRulesByParentIdRuleEntriesById
    intent: Get one entry of a price rule
    question: How do I look up a single price rule entry by its ID?
  - id: patchRulesByParentIdRuleEntriesById
    intent: Update one entry of a price rule
    question: What do I call to edit a single price rule entry?
  phrasing_ops: 7
  slug: conga-price-rule-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Rule Sets API from Conga — 2 operation(s) for price rule sets.
  name: Conga Price Rule Sets API
  phrasing_intents:
  - id: deleteRuleSets
    intent: Delete several price rule sets
    question: How many price rule sets can I bulk delete in one call?
  - id: getRuleSets
    intent: List price rule sets
    question: How do I see all the price rule sets configured in Conga CPQ?
  - id: patchRuleSets
    intent: Update several price rule sets
    question: Can I change fields on many price rule sets in one bulk update?
  - id: postRuleSets
    intent: Create price rule sets
    question: What's the way to create one or more new price rule sets?
  - id: deleteRuleSetsById
    intent: Delete one price rule set
    question: How do I delete a single price rule set by its ID?
  - id: getRuleSetsById
    intent: Get one price rule set
    question: How do I look up a single price rule set by its ID?
  - id: patchRuleSetsById
    intent: Update one price rule set
    question: What do I call to edit a single price rule set?
  phrasing_ops: 7
  slug: conga-price-rule-sets-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Price Rules API from Conga — 2 operation(s) for price rules.
  name: Conga Price Rules API
  phrasing_intents:
  - id: deleteRuleSetsByParentIdRules
    intent: Delete several price rules from a rule set
    question: How many price rules can I bulk delete from a rule set in one call?
  - id: getRuleSetsByParentIdRules
    intent: List the price rules in a price rule set
    question: How do I see all the price rules inside one price rule set?
  - id: patchRuleSetsByParentIdRules
    intent: Update several price rules in a rule set
    question: Can I change fields on many price rules in one bulk update?
  - id: postRuleSetsByParentIdRules
    intent: Add price rules to a price rule set
    question: What's the way to add several new price rules to a rule set at once?
  - id: deleteRuleSetsByParentIdRulesById
    intent: Delete one price rule from a rule set
    question: How do I delete just one price rule from a rule set?
  - id: getRuleSetsByParentIdRulesById
    intent: Get one price rule in a rule set
    question: How do I look up a single price rule by its ID?
  - id: patchRuleSetsByParentIdRulesById
    intent: Update one price rule in a rule set
    question: What do I call to edit a single price rule?
  phrasing_ops: 7
  slug: conga-price-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The PriceEscalator API from Conga — 2 operation(s) for priceescalator.
  name: Conga Price Escalator API
  phrasing_intents:
  - id: deletePriceListItemsByParentIdPriceEscalators
    intent: Delete several price escalators from a price list item
    question: How can I bulk remove many price escalators from a price list item?
  - id: getPriceListItemsByParentIdPriceEscalators
    intent: List the price escalators on a price list item
    question: How do I see the price escalators set up for a price list item?
  - id: patchPriceListItemsByParentIdPriceEscalators
    intent: Update several price escalators on a price list item
    question: Can I edit many price escalators on a price list item in one bulk update?
  - id: postPriceListItemsByParentIdPriceEscalators
    intent: Add price escalators to a price list item
    question: What's the way to add several price escalators to a price list item at once?
  - id: deletePriceListItemsByParentIdPriceEscalatorsById
    intent: Delete one price escalator
    question: How do I delete just one price escalator from a price list item?
  - id: getPriceListItemsByParentIdPriceEscalatorsById
    intent: Get one price escalator
    question: How do I look up a single price escalator by its ID?
  - id: patchPriceListItemsByParentIdPriceEscalatorsById
    intent: Update one price escalator
    question: What do I call to change a single price escalator?
  phrasing_ops: 7
  slug: conga-priceescalator-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: PriceWaterfall controller
  name: Conga Price Waterfall API
  phrasing_intents:
  - id: getApiCartV1CartsByCartIdItemsByLineitemIdWaterfallchart
    intent: Get the price waterfall for a cart line item
    question: How do I see the price waterfall breakdown for one line item in a cart?
  - id: getApiCartV1CartsByCartIdItemsByLineitemIdWaterfallchartByChartId
    intent: Get one waterfall chart for a cart line item
    question: Can I pull a specific waterfall chart for a cart line item by chart ID?
  - id: getApiCartV1CartsByCartIdSummarygroupsBySummarygroupIdWaterfallchart
    intent: Get the price waterfall for a cart summary group
    question: How do I see a price waterfall rolled up for a summary group in a cart?
  - id: getApiCartV1CartsByCartIdSummarygroupsBySummarygroupIdWaterfallchartByChartId
    intent: Get one waterfall chart for a cart summary group
    question: Can I fetch one specific waterfall chart for a cart summary group by its chart ID?
  - id: getApiCartV1CartsByCartIdWaterfallchart
    intent: Get price waterfalls for all lines in a cart
    question: How do I get the price waterfall for every line item in a cart at once?
  phrasing_ops: 5
  slug: conga-pricewaterfall-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Process API from Conga — 15 operation(s) for process.
  name: Conga Process API
  phrasing_intents:
  - id: Process_GetAll
    intent: Search approval processes for a business object
    question: Which approval processes are set up for agreements in Conga Approvals?
  - id: Process_Save
    intent: Create an approval process
    question: How do I set up a new approval process with entry criteria and steps?
  - id: Process_ReorderProcess
    intent: Change the order approval processes run in
    question: Can I change the evaluation order of my approval processes?
  - id: Process_GetActiveInactiveCount
    intent: Count a business object's active and inactive processes
    question: How many active versus inactive approval processes does an object have?
  - id: Process_Validate
    intent: Check whether an approval process name is taken
    question: Does an approval process with this name already exist for this object type?
  - id: Process_DeleteById
    intent: Delete an approval process
    question: Can I permanently remove an approval process I no longer need?
  - id: Process_GetById
    intent: Get an approval process by ID
    question: What does a specific approval process look like in full?
  - id: Process_UpdateById
    intent: Update an existing approval process
    question: How do I rename or change the entry criteria of an existing approval process?
  phrasing_ops: 19
  slug: conga-process-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ProcessSteps API from Conga — 3 operation(s) for processsteps.
  name: Conga Process Steps API
  phrasing_intents:
  - id: ProcessSteps_CreateApprovalProcessStep
    intent: Add a step to an approval process
    question: How do I add a new approval step to a process?
  - id: ProcessSteps_UpdateApprovalProcessStep
    intent: Update an approval process step
    question: How do I change who approves a step in an approval process?
  - id: ProcessSteps_ValidateExistingStepName
    intent: Check if a step name is unique in a process
    question: Is a step name already used in this approval process?
  - id: ProcessSteps_GetApprovalProcessStep
    intent: Get an approval process step
    question: How do I look up an approval step by its ID?
  phrasing_ops: 4
  slug: conga-processsteps-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Attribute Groups API from Conga — 2 operation(s) for product attribute groups.
  name: Conga Product Attribute Groups API
  phrasing_intents:
  - id: deleteProductsByParentIdAttributeGroups
    intent: Remove several attribute groups from a product
    question: How can I bulk remove attribute groups from a product?
  - id: getProductsByParentIdAttributeGroups
    intent: List the attribute groups on a product
    question: How do I see which attribute groups are assigned to a product?
  - id: patchProductsByParentIdAttributeGroups
    intent: Update several attribute groups on a product
    question: Can I edit many of a product's attribute groups in one bulk update?
  - id: postProductsByParentIdAttributeGroups
    intent: Assign attribute groups to a product
    question: What's the way to attach several attribute groups to a product at once?
  - id: deleteProductsByParentIdAttributeGroupsById
    intent: Remove one attribute group from a product
    question: How do I remove just one attribute group from a product?
  - id: getProductsByParentIdAttributeGroupsById
    intent: Get one attribute group on a product
    question: How do I look up a single product attribute group by its ID?
  - id: patchProductsByParentIdAttributeGroupsById
    intent: Update one attribute group on a product
    question: What do I call to change a single product attribute group?
  phrasing_ops: 7
  slug: conga-product-attribute-groups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Attribute Rule Actions API from Conga — 2 operation(s) for product attribute rule actions.
  name: Conga Product Attribute Rule Actions API
  phrasing_intents:
  - id: deleteAttributeRulesByParentIdActions
    intent: Delete several actions from an attribute rule
    question: How can I bulk delete actions from a product attribute rule?
  - id: getAttributeRulesByParentIdActions
    intent: List the actions of a product attribute rule
    question: How do I see the actions an attribute rule performs when it fires?
  - id: patchAttributeRulesByParentIdActions
    intent: Update several actions of an attribute rule
    question: Can I edit many attribute rule actions together in one bulk update?
  - id: postAttributeRulesByParentIdActions
    intent: Add actions to a product attribute rule
    question: What's the way to add several actions to an attribute rule at once?
  - id: deleteAttributeRulesByParentIdActionsById
    intent: Delete one action from an attribute rule
    question: How do I delete just one action from an attribute rule?
  - id: getAttributeRulesByParentIdActionsById
    intent: Get one action of a product attribute rule
    question: How do I look up a single attribute rule action by its ID?
  - id: patchAttributeRulesByParentIdActionsById
    intent: Update one action of an attribute rule
    question: What do I call to change a single attribute rule action?
  phrasing_ops: 7
  slug: conga-product-attribute-rule-actions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Attribute Rules API from Conga — 2 operation(s) for product attribute rules.
  name: Conga Product Attribute Rules API
  phrasing_intents:
  - id: deleteAttributeRules
    intent: Delete several product attribute rules
    question: How can I bulk delete multiple product attribute rules?
  - id: getAttributeRules
    intent: List product attribute rules
    question: How do I see every product attribute rule in the system?
  - id: patchAttributeRules
    intent: Update several product attribute rules
    question: Can I update many attribute rules and their conditions in one bulk call?
  - id: postAttributeRules
    intent: Create product attribute rules with conditions
    question: What's the way to create several attribute rules, each with its condition, in one request?
  - id: deleteAttributeRulesById
    intent: Delete one product attribute rule
    question: How do I delete a single product attribute rule?
  - id: getAttributeRulesById
    intent: Get one product attribute rule
    question: How do I look up a single product attribute rule by its ID?
  - id: patchAttributeRulesById
    intent: Update one product attribute rule
    question: What do I call to edit a single product attribute rule?
  phrasing_ops: 7
  slug: conga-product-attribute-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Billing Configuration Controller
  name: Conga Product Configurations API
  phrasing_intents:
  - id: getProductConfigurations
    intent: List product billing configurations
    question: How do I see the billing configuration records linked to my products?
  - id: patchProductConfigurations
    intent: Update several product billing configurations
    question: Can I change billing settings on many product configurations in one bulk update?
  - id: postProductConfigurations
    intent: Create product billing configurations
    question: What's the way to link billing configuration settings to several products at once?
  - id: getProductConfigurationsByProductConfigurationId
    intent: Get one product billing configuration
    question: How do I look up a single product billing configuration by its ID?
  phrasing_ops: 4
  slug: conga-product-configurations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Groups API from Conga — 8 operation(s) for product groups.
  name: Conga Product Groups API
  phrasing_intents:
  - id: deleteProductGroups
    intent: Delete product groups in bulk
    question: Is there a way to remove many product groups at the same time?
  - id: getProductGroups
    intent: List product groups
    question: How do I see every product group set up in Conga CPQ?
  - id: patchProductGroups
    intent: Update product groups in bulk
    question: Is it possible to edit several product groups in a single request?
  - id: postProductGroups
    intent: Create product groups in bulk
    question: What's the way to create several new product groups in one request?
  - id: deleteProductGroupsById
    intent: Delete a product group
    question: What happens when I delete one specific product group?
  - id: getProductGroupsById
    intent: Get a product group
    question: How do I look up the details of one product group by its ID?
  - id: patchProductGroupsById
    intent: Update a product group
    question: Where do I change the details of one product group?
  - id: getProductGroupsByIdAttributeMatrices
    intent: List a product group's attribute matrices
    question: Which attribute matrices apply to a product group?
  phrasing_ops: 18
  slug: conga-product-groups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Information API from Conga — 2 operation(s) for product information.
  name: Conga Product Information API
  phrasing_intents:
  - id: deleteProductsByParentIdInformation
    intent: Delete a product's information documents in bulk
    question: Is there a way to remove several information documents from a product at once?
  - id: getProductsByParentIdInformation
    intent: List a product's information documents
    question: How do I see all the information documents attached to a product?
  - id: patchProductsByParentIdInformation
    intent: Update a product's information documents in bulk
    question: How do I edit many information documents on a product in one go?
  - id: postProductsByParentIdInformation
    intent: Add information documents to a product
    question: How do I attach new information documents to a product?
  - id: deleteProductsByParentIdInformationById
    intent: Delete one product information document
    question: How do I delete a single information document from a product?
  - id: getProductsByParentIdInformationById
    intent: Get one product information document
    question: How do I fetch a single information document for a product by its ID?
  - id: patchProductsByParentIdInformationById
    intent: Update one product information document
    question: What's the call to edit a single product information document?
  phrasing_ops: 7
  slug: conga-product-information-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Option Components API from Conga — 2 operation(s) for product option components.
  name: Conga Product Option Components API
  phrasing_intents:
  - id: deleteProductOptionGroupByParentIdProducts
    intent: Remove option components from a bundle in bulk
    question: Is there a way to remove several products or options from a bundle at once?
  - id: getProductOptionGroupByParentIdProducts
    intent: List a bundle's option components
    question: How do I see every option group and option in a bundle product?
  - id: patchProductOptionGroupByParentIdProducts
    intent: Update option components in bulk
    question: How do I edit many option components in one request?
  - id: postProductOptionGroupByParentIdProducts
    intent: Add products and options to a bundle
    question: How do I add standalone products or sub-bundles to a bundle?
  - id: deleteProductOptionGroupByParentIdProductsById
    intent: Delete a single option component
    question: How do I delete just one option component?
  - id: getProductOptionGroupByParentIdProductsById
    intent: Get a single option component
    question: How do I look up one option component by its ID?
  - id: patchProductOptionGroupByParentIdProductsById
    intent: Update a single option component
    question: What's the call to change one option component's settings?
  phrasing_ops: 7
  slug: conga-product-option-components-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Product Option Prices API from Conga — 2 operation(s) for product option prices.
  name: Conga Product Option Prices API
  phrasing_intents:
  - id: deleteProductOptionPrices
    intent: Delete product option prices in bulk
    question: Is there a way to remove many product option prices at the same time?
  - id: getProductOptionPrices
    intent: List product option prices
    question: How do I see all product option prices in Conga CPQ?
  - id: patchProductOptionPrices
    intent: Update product option prices in bulk
    question: How do I change several product option prices in one request?
  - id: postProductOptionPrices
    intent: Create product option prices in bulk
    question: How do I create several product option prices in one request?
  - id: deleteProductOptionPricesById
    intent: Delete a product option price
    question: How do I delete one specific product option price?
  - id: getProductOptionPricesById
    intent: Get a product option price
    question: How do I look up one product option price by its ID?
  - id: patchProductOptionPricesById
    intent: Update a product option price
    question: What's the call to change one product option price?
  phrasing_ops: 7
  slug: conga-product-option-prices-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The ProductOptionGroups API from Conga — 4 operation(s) for productoptiongroups.
  name: Conga Product Option Groups API
  phrasing_intents:
  - id: deleteProductsByParentIdOptionGroups
    intent: Delete a product's option groups in bulk
    question: Is there a way to remove several option groups from a product at once?
  - id: getProductsByParentIdOptionGroups
    intent: List a product's option groups
    question: How do I see the option groups configured on a bundle product?
  - id: patchProductsByParentIdOptionGroups
    intent: Update a product's option groups in bulk
    question: How do I edit many option groups on a product in one go?
  - id: postProductsByParentIdOptionGroups
    intent: Create option groups on a product
    question: How do I create new option groups for a product?
  - id: deleteProductsByParentIdOptionGroupsById
    intent: Delete a product option group
    question: How do I delete just one option group from a product?
  - id: getProductsByParentIdOptionGroupsById
    intent: Get a product option group
    question: How do I look up one option group on a product by its ID?
  - id: patchProductsByParentIdOptionGroupsById
    intent: Update a product option group
    question: What's the call to change one option group on a product?
  - id: postProductsByParentIdOptionGroupsByIdBulk
    intent: Nest existing option groups as sub option groups
    question: How do I add existing option groups as sub option groups in a bundle?
  phrasing_ops: 9
  slug: conga-productoptiongroups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Products API from Conga — 26 operation(s) for products.
  name: Conga Products API
  phrasing_intents:
  - id: deleteProducts
    intent: Delete several products in bulk
    question: Can I remove a whole batch of products from the catalog at once?
  - id: getProducts
    intent: List products in the catalog
    question: What products are in my Conga product catalog?
  - id: patchProducts
    intent: Update several products in bulk
    question: Can I edit fields on many products in a single request?
  - id: postProducts
    intent: Create several products at once
    question: Can I add a batch of new products to the catalog in one request?
  - id: deleteProductsById
    intent: Delete one product
    question: Can I delete just one product from the catalog by its ID?
  - id: getProductsById
    intent: Retrieve a product record by ID
    question: How can I look up a single product record by its ID?
  - id: patchProductsById
    intent: Update one product
    question: How do I change the details of one specific product?
  - id: getProductsByIdAttributeMatrices
    intent: List a product's attribute matrices
    question: Which attribute matrices are attached to a given product?
  phrasing_ops: 56
  slug: conga-products-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Property Permission API from Conga — 2 operation(s) for property permission.
  name: Conga Property Permission API
  phrasing_intents:
  - id: getApiUserManagementV1PropertyPermissionsByPermissionGroupNamePropertyObjects
    intent: List property objects for a permission group
    question: Which property objects does a permission group have in Conga?
  - id: deleteApiUserManagementV1PropertyPermissionsByPermissionGroupNameByPropertyName
    intent: Remove a property permission
    question: What's the way to revoke a permission group's access to a property?
  - id: getApiUserManagementV1PropertyPermissionsByPermissionGroupNameByPropertyName
    intent: Get a property permission
    question: What access does a permission group have to a specific property?
  - id: putApiUserManagementV1PropertyPermissionsByPermissionGroupNameByPropertyName
    intent: Set a property permission
    question: How do I grant or change a permission group's access to a property?
  phrasing_ops: 4
  slug: conga-property-permission-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Proposal Locations API from Conga — 2 operation(s) for proposal locations.
  name: Conga Proposal Locations API
  phrasing_intents:
  - id: deleteQuotesByParentIdLocations
    intent: Remove locations from a proposal in bulk
    question: Is there a way to remove several locations from a proposal at once?
  - id: getQuotesByParentIdLocations
    intent: List a proposal's locations
    question: How do I see every location attached to a proposal?
  - id: patchQuotesByParentIdLocations
    intent: Update a proposal's locations in bulk
    question: How do I edit many proposal locations in one request?
  - id: postQuotesByParentIdLocations
    intent: Add locations to a proposal
    question: How do I add new locations to a proposal?
  - id: deleteQuotesByParentIdLocationsById
    intent: Delete a proposal location
    question: How do I delete just one location from a proposal?
  - id: getQuotesByParentIdLocationsById
    intent: Get a proposal location
    question: How do I look up one location on a proposal by its ID?
  - id: patchQuotesByParentIdLocationsById
    intent: Update a proposal location
    question: What's the call to change one location on a proposal?
  phrasing_ops: 7
  slug: conga-proposal-locations-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs for querying objects
  name: Conga Query API
  phrasing_intents:
  - id: postApiXauthorV1QueryByObjectName
    intent: Query dynamic lookup data for an object
    question: How do I pull dynamic lookup data for an object in Conga X-Author?
  phrasing_ops: 1
  slug: conga-query-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The quote controller
  name: Conga Quote API
  phrasing_intents:
  - id: postApiCartV1QuotesByQuoteIdCartsActivate
    intent: Launch the cart for a quote
    question: How do I open a shopping cart to configure products on a quote?
  - id: getApiCartV1QuotesByQuoteIdCartsActive
    intent: Get a quote's active cart
    question: Which cart is currently active on a quote?
  - id: deleteQuotes
    intent: Delete several quotes
    question: Can I delete a batch of quote records at once?
  - id: getQuotes
    intent: List quotes
    question: What quotes do we have in Conga CPQ?
  - id: patchQuotes
    intent: Update several quotes
    question: Can I change fields on many quotes in one request?
  - id: postQuotes
    intent: Create one or more quotes
    question: How do I create new quotes and get their IDs back?
  - id: postQuotesUpsertQuote
    intent: Upsert a quote
    question: Can I create a quote or update it if it already exists in one call?
  - id: postQuotesByExternalIdCloneQuote
    intent: Clone a quote by its external ID
    question: Can I copy a quote when I only know its external quote ID?
  phrasing_ops: 14
  slug: conga-quote-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Ramp Line Items Controller
  name: Conga Ramp Line Items API
  phrasing_intents:
  - id: deleteApiCartV1CartsByCartIdItemsRampLines
    intent: Delete the ramp lines in a cart
    question: Is there a way to remove all the ramp lines from a cart?
  - id: postApiCartV1CartsByCartIdItemsRampLines
    intent: Mass-create ramp lines in a cart
    question: How do I create ramp lines for many cart line items in one go?
  - id: putApiCartV1CartsByCartIdItemsRampLines
    intent: Update all ramp lines in a cart
    question: Can I update every ramp line in a quote cart at once?
  - id: postApiCartV1CartsByCartIdItemsByItemIdAutoRamps
    intent: Auto-generate ramps for a cart line item
    question: Can Conga generate ramp periods automatically for a single line item by frequency?
  - id: deleteApiCartV1CartsByCartIdItemsByItemIdRampLines
    intent: Delete one line item's ramp line
    question: Can I delete the ramp line from just one product in a cart?
  - id: postApiCartV1CartsByCartIdItemsByItemIdRampLines
    intent: Add a ramp line to a cart line item
    question: How do I add another ramp period line to a product in my cart?
  - id: putApiCartV1CartsByCartIdItemsByItemIdRampLines
    intent: Update one line item's ramp line
    question: What's the way to edit the ramp line on one specific cart line item?
  - id: putApiCartV1CartsByCartIdItemsByItemIdRampLinesSplit
    intent: Split a ramp line into periods
    question: How do I split one ramp line into several shorter periods?
  phrasing_ops: 9
  slug: conga-ramplineitems-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Ramps Controller
  name: Conga Ramps API
  phrasing_intents:
  - id: deleteApiCartV1CartsByCartIdItemsRamps
    intent: Delete ramp lines from a cart
    question: What's the way to remove ramp lines from a cart?
  - id: patchApiCartV1CartsByCartIdItemsRamps
    intent: Update existing ramp lines
    question: Where do I change the details of ramp lines already in a cart?
  - id: postApiCartV1CartsByCartIdItemsRamps
    intent: Ramp cart line items
    question: How do I set up a ramp for a line item in a Conga cart for the first time?
  - id: putApiCartV1CartsByCartIdItemsRamps
    intent: Add ramp lines to already ramped items
    question: How do I add more ramp periods to a cart line item that is already ramped?
  phrasing_ops: 4
  slug: conga-ramps-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: <p> <H3> <strong>⚠️ Deprecated:</strong> Rebate Program APIs have been deprecated from the Rebates-Admin Service.</H3> </p> <p> <H3>Please find these APIs under Incentive Programs here → <a href="/api
  name: Conga Rebate Programs API
  phrasing_intents:
  - id: deletePrograms
    intent: Delete rebate programs in bulk
    question: Can I delete multiple rebate programs together?
  - id: getPrograms
    intent: List rebate programs
    question: Which rebate programs are set up in Conga Rebate Administration?
  - id: patchPrograms
    intent: Update rebate programs in bulk
    question: Can I update many rebate programs in a single call?
  - id: postPrograms
    intent: Create rebate programs in bulk
    question: How do I create several rebate programs in one request?
  - id: deleteProgramsById
    intent: Delete a rebate program
    question: How do I delete a single rebate program?
  - id: getProgramsById
    intent: Get a rebate program
    question: How do I look up one rebate program by its ID?
  - id: patchProgramsById
    intent: Update a rebate program
    question: How do I edit one rebate program's details?
  phrasing_ops: 7
  slug: conga-rebate-programs-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Rebate Rule Entries API from Conga — 2 operation(s) for rebate rule entries.
  name: Conga Rebate Rule Entries API
  phrasing_intents:
  - id: deleteRebateRulesByParentIdEntries
    intent: Delete several rebate rule entries
    question: Can I delete multiple entries from a rebate rule in one request?
  - id: getRebateRulesByParentIdEntries
    intent: List a rebate rule's entries
    question: Which entries belong to a given rebate rule?
  - id: patchRebateRulesByParentIdEntries
    intent: Update several rebate rule entries
    question: Is there a bulk update for a rebate rule's entries?
  - id: postRebateRulesByParentIdEntries
    intent: Add entries to a rebate rule
    question: How do I add entries to a rebate rule?
  - id: deleteRebateRulesByParentIdEntriesById
    intent: Delete a rebate rule entry
    question: How do I remove one entry from a rebate rule?
  - id: getRebateRulesByParentIdEntriesById
    intent: Get a rebate rule entry
    question: How do I look up a single entry on a rebate rule?
  - id: patchRebateRulesByParentIdEntriesById
    intent: Update a rebate rule entry
    question: How do I edit a single rebate rule entry?
  phrasing_ops: 7
  slug: conga-rebate-rule-entries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Rebate Rules API from Conga — 2 operation(s) for rebate rules.
  name: Conga Rebate Rules API
  phrasing_intents:
  - id: deleteRebatesByParentIdRules
    intent: Delete several rules from a rebate
    question: Can I delete multiple rules from a rebate in one call?
  - id: getRebatesByParentIdRules
    intent: List a rebate's rules
    question: Which rules are attached to a given rebate?
  - id: patchRebatesByParentIdRules
    intent: Update several rules on a rebate
    question: Is there a bulk update for a rebate's rules?
  - id: postRebatesByParentIdRules
    intent: Add rules to a rebate
    question: How do I add rules to a rebate?
  - id: deleteRebatesByParentIdRulesById
    intent: Delete a rebate rule
    question: How do I remove one rule from a rebate?
  - id: getRebatesByParentIdRulesById
    intent: Get a rebate rule
    question: How do I look up a single rule on a rebate?
  - id: patchRebatesByParentIdRulesById
    intent: Update a rebate rule
    question: How do I edit a single rule on a rebate?
  phrasing_ops: 7
  slug: conga-rebate-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for handling rebate-related actions in the cart API.
  name: Conga Rebates API
  phrasing_intents:
  - id: postApiCartV1CartsByCartIdRebateEstimates
    intent: Estimate rebates for a cart
    question: What rebates would the customer earn on the products in this cart?
  - id: deleteRebates
    intent: Delete rebates in bulk
    question: Can I delete multiple rebates together?
  - id: getRebates
    intent: List rebates
    question: Which rebates are defined in Conga?
  - id: patchRebates
    intent: Update rebates in bulk
    question: Can I update many rebates in a single call?
  - id: postRebates
    intent: Create rebates in bulk
    question: How do I create several rebates in one request?
  - id: deleteRebatesById
    intent: Delete a rebate
    question: How do I delete a single rebate?
  - id: getRebatesById
    intent: Get a rebate
    question: How do I look up one rebate by its ID?
  - id: patchRebatesById
    intent: Update a rebate
    question: How do I edit one rebate's details?
  phrasing_ops: 9
  slug: conga-rebates-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints related to document reconciliation
  name: Conga Reconciliation API
  phrasing_intents:
  - id: postApiXauthorV1ReconcilePreviewData
    intent: Prepare a document for reconciliation preview
    question: How do I validate and reconcile the fields and clauses in an authored document before applying changes?
  - id: postApiXauthorV1ReconcilePreviewDataSametagfields
    intent: Preview reconciliation for same-tag fields
    question: Can I preview reconciliation data for fields that share the same tag?
  phrasing_ops: 2
  slug: conga-reconciliation-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Record Share API from Conga — 6 operation(s) for record share.
  name: Conga Record Share API
  phrasing_intents:
  - id: putApiDataV1ObjectsByObjectNameByRecordIdAccessLevel
    intent: Change a shared record's access level
    question: How do I change someone's access on a shared record from View to Edit?
  - id: postApiDataV1ObjectsByObjectNameByRecordIdShare
    intent: Share a record with users or groups
    question: How do I share a record with other users and groups in Conga?
  - id: getApiDataV1ObjectsByObjectNameByRecordIdSharingInfo
    intent: See who a record is shared with
    question: Who has access to this record, and with what permissions?
  - id: deleteApiDataV1ObjectsByObjectNameByRecordIdUnShare
    intent: Un-share a record
    question: How do I revoke someone's access to a record I shared?
  - id: getApiDataV1ObjectsByObjectNameByRecordIdByTrackingIdSharingStatus
    intent: Check a group record-share's progress
    question: Has sharing a record with a user group finished yet?
  - id: getApiDataV1ObjectsByObjectNameByRecordIdByUserIdAccessLevel
    intent: Get one user's access on a shared record
    question: Can a specific user view, edit or delete this shared record?
  phrasing_ops: 6
  slug: conga-record-share-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Record Type Permission API from Conga — 5 operation(s) for record type permission.
  name: Conga Record Type Permission API
  phrasing_intents:
  - id: postApiUserManagementV1RecordtypePermissions
    intent: Grant a record type permission
    question: How do I give a permission group access to specific record types on an object?
  - id: putApiUserManagementV1RecordtypePermissions
    intent: Update record type access by group and object
    question: How do I change which record types a permission group can use on an object, without knowing the permission ID?
  - id: postApiUserManagementV1RecordtypePermissionsBulk
    intent: Grant many record type permissions at once
    question: Can I set record type permissions for several groups and objects in one request?
  - id: deleteApiUserManagementV1RecordtypePermissionsByPermissionGroupNameByObjectName
    intent: Revoke record type access by group and object
    question: How do I remove a permission group's record type access on an object?
  - id: getApiUserManagementV1RecordtypePermissionsByPermissionGroupNameByObjectName
    intent: Get record type access by group and object
    question: Which record types can a given permission group access on an object?
  - id: deleteApiUserManagementV1RecordtypePermissionsByRecordTypePermissionId
    intent: Delete a record type permission by ID
    question: How do I delete a record type permission when I have its ID?
  - id: getApiUserManagementV1RecordtypePermissionsByRecordtypePermissionId
    intent: Get a record type permission by ID
    question: How do I fetch a record type permission's details from its ID?
  - id: putApiUserManagementV1RecordtypePermissionsByRecordtypePermissionId
    intent: Update a record type permission by ID
    question: Can I edit a record type permission using its permission ID?
  phrasing_ops: 8
  slug: conga-record-type-permission-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains APIs for the record type object
  name: Conga Record Type API
  phrasing_intents:
  - id: getApiXauthorV1RecordTypes
    intent: List available record types
    question: Which record types are available in a Conga X-Author document?
  phrasing_ops: 1
  slug: conga-recordtype-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The RecordType Definition API from Conga — 2 operation(s) for recordtype definition.
  name: Conga RecordType Definition API
  phrasing_intents:
  - id: postApiSchemaV1ObjectsByObjectNameRecordtypeEntries
    intent: Add a record type picklist value
    question: Can I add a new record type value to an object in Conga?
  - id: putApiSchemaV1ObjectsByObjectNameRecordtypeEntriesBulk
    intent: Update record type picklist values in bulk
    question: Is there a way to update all the record type values on an object at once?
  phrasing_ops: 2
  slug: conga-recordtype-definition-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides API endpoints for polling the status of a redline execution. Tracks extraction and redlining progress for rules applied against a contract document.
  name: Conga Redline Execution Status API
  phrasing_intents:
  - id: getApiXauthorV1ContractsByContractIdRedlinesExecutionsByExecutionIdStatus
    intent: Check a contract redline execution's status
    question: Has the redline run on my contract finished yet?
  phrasing_ops: 1
  slug: conga-redlineexecutionstatus-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Related Incentives API from Conga — 2 operation(s) for related incentives.
  name: Conga Related Incentives API
  phrasing_intents:
  - id: deleteIncentivesByParentIdRelatedIncentives
    intent: Remove several related incentives
    question: Can I unlink multiple related incentives from an incentive at once?
  - id: getIncentivesByParentIdRelatedIncentives
    intent: List an incentive's related incentives
    question: Which incentives are linked to a given incentive?
  - id: patchIncentivesByParentIdRelatedIncentives
    intent: Update several related incentives
    question: Is there a bulk update for an incentive's related incentives?
  - id: postIncentivesByParentIdRelatedIncentives
    intent: Link related incentives to an incentive
    question: How do I relate other incentives to an incentive?
  - id: deleteIncentivesByParentIdRelatedIncentivesById
    intent: Remove a related incentive
    question: How do I unlink one related incentive from an incentive?
  - id: getIncentivesByParentIdRelatedIncentivesById
    intent: Get a related incentive
    question: How do I look up one related incentive?
  - id: patchIncentivesByParentIdRelatedIncentivesById
    intent: Update a related incentive
    question: How do I edit a single related incentive?
  phrasing_ops: 7
  slug: conga-related-incentives-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Related Price List Items API from Conga — 2 operation(s) for related price list items.
  name: Conga Related Price List Items API
  phrasing_intents:
  - id: deletePriceListItemsByParentIdRelatedPriceListItems
    intent: Remove several related price list items
    question: Can I delete multiple related price list items at once?
  - id: getPriceListItemsByParentIdRelatedPriceListItems
    intent: List a price list item's related items
    question: Which price list items are related to a given price list item?
  - id: patchPriceListItemsByParentIdRelatedPriceListItems
    intent: Update several related price list items
    question: Is there a bulk update for related price list items?
  - id: postPriceListItemsByParentIdRelatedPriceListItems
    intent: Add related price list items
    question: How do I relate other price list items to a price list item?
  - id: deletePriceListItemsByParentIdRelatedPriceListItemsById
    intent: Remove a related price list item
    question: How do I remove one related price list item?
  - id: getPriceListItemsByParentIdRelatedPriceListItemsById
    intent: Get a related price list item
    question: How do I look up one related price list item?
  - id: patchPriceListItemsByParentIdRelatedPriceListItemsById
    intent: Update a related price list item
    question: How do I edit a single related price list item?
  phrasing_ops: 7
  slug: conga-related-price-list-items-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Reminder API from Conga — 1 operation(s) for reminder.
  name: Conga Reminder API
  phrasing_intents:
  - id: Reminder_CreateReminders
    intent: Create a reminder schedule for a package
    question: How do I add signer reminders to a package before sending it?
  - id: Reminder_DeleteReminders
    intent: Delete a package's reminder schedule
    question: Can I stop all reminders for a package?
  - id: Reminder_GetReminders
    intent: Get a package's reminder schedule
    question: What reminder schedule is set on a signing package?
  - id: Reminder_UpdateReminders
    intent: Change a package's existing reminder schedule
    question: Can I change the reminder interval on a package that already has a schedule?
  phrasing_ops: 4
  slug: conga-reminder-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Reports API from Conga — 6 operation(s) for reports.
  name: Conga Reports API
  phrasing_intents:
  - id: Reports_GetCompletionReport
    intent: Report on a sender's completed packages
    question: Which transactions has a particular sender gotten fully signed?
  - id: Reports_GetDelegationReport
    intent: Get the delegation report for a sender
    question: What has been delegated for the sender I'm logged in as?
  - id: Reports_GetSenderTransactionSummaryReport
    intent: Summarize transactions per sender over a period
    question: How many transactions did each sender send between two dates?
  - id: Reports_GetTransactionDetailReportById
    intent: Get a detail report for one transaction
    question: What's the full detail report for a specific signing transaction?
  - id: Reports_GetTransactionSummaryReport
    intent: Summarize account transactions by status
    question: How many transactions in the account are still in draft or sent?
  - id: Reports_GetUsageReport
    intent: Get my sender usage report
    question: How much have I used e-signature as the logged-in sender?
  phrasing_ops: 6
  slug: conga-reports-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Requests API from Conga — 27 operation(s) for requests.
  name: Conga Requests API
  phrasing_intents:
  - id: Requests_GetAttachmentsByRequestIds
    intent: Get attachments for several approval requests
    question: What files are attached to these approval requests?
  - id: Requests_ApproveMultiple
    intent: Approve several approval requests at once
    question: Can I approve a whole batch of pending approval requests in one call?
  - id: Requests_ReassignMultiple
    intent: Reassign several approval requests at once
    question: Is there a way to hand off many approval requests to someone else in one go?
  - id: Requests_RejectMultiple
    intent: Reject several approval requests at once
    question: Can I reject a batch of approval requests in a single call?
  - id: Requests_BulkProcessMultipleContextObjects
    intent: Run an action on many business objects in bulk
    question: Can I apply one approval action type across many business objects in bulk?
  - id: Requests_CheckRequired
    intent: Check which objects require approval
    question: Does this quote and its line items need approval before I continue?
  - id: Requests_CheckRequired2
    intent: Check asynchronously which objects need approval
    question: Can I run the approval-required check asynchronously for a large object?
  - id: Requests_AddComments
    intent: Add a comment to approval requests
    question: Can I leave a comment on an approval request without approving or rejecting it?
  phrasing_ops: 28
  slug: conga-requests-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: ResponseFieldConfigurationController
  name: Conga Response Field Configuration API
  phrasing_intents:
  - id: getResponsefieldConfigurationByCategoryName
    intent: List response field configurations in a category
    question: Which response field configurations exist for a category?
  - id: deleteResponsefieldConfigurationByCategoryNameByConfigName
    intent: Delete a response field configuration
    question: How do I remove a response field configuration I no longer need?
  - id: getResponsefieldConfigurationByCategoryNameByConfigName
    intent: Get a response field configuration
    question: What fields does a named response field configuration return?
  - id: putResponsefieldConfigurationByCategoryNameByConfigName
    intent: Update a response field configuration
    question: How do I change the fields in an existing response field configuration?
  - id: postResponsefieldConfigurationByCategoryNameByDefaultConfigNameByNewConfigName
    intent: Create a response field configuration from a default
    question: How do I create a new response field configuration based on a default one?
  phrasing_ops: 5
  slug: conga-responsefieldconfiguration-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Review API from Conga — 12 operation(s) for review.
  name: Conga Review API
  phrasing_intents:
  - id: getApiClmV1ContractsByContractIdReviews
    intent: Get a contract's active review cycle
    question: Is there a review cycle running on this CLM contract, and who's reviewing it?
  - id: postApiClmV1ContractsByContractIdReviews
    intent: Send a CLM contract out for review
    question: How do I start a Simple Review or Microsoft 365 Review on a contract?
  - id: postApiClmV1ContractsByContractIdReviewsByReviewIdCancel
    intent: Cancel a contract's Microsoft 365 review
    question: What happens to the contract status when I cancel a Microsoft 365 review?
  - id: postApiClmV1ContractsByContractIdReviewsByReviewIdEnd
    intent: Complete a contract review
    question: How do I finish a contract review so it's ready for signature?
  - id: postApiClmV1ContractsByContractIdReviewsByReviewIdReviewers
    intent: Add reviewers to a contract review cycle
    question: Can I bring more people into a contract review that's already active?
  - id: postApiClmV1ContractsByContractIdReviewsByReviewIdReviewersCancel
    intent: Remove reviewers from a contract review
    question: How do I take someone off an active contract review?
  - id: postApiClmV1ContractsByContractIdReviewsByReviewIdReviewersEnd
    intent: End the review for specific contract reviewers
    question: Can I end the review for some reviewers on a contract while it stays open for others?
  - id: getApiClmV1ContractsByContractIdReviewsByReviewTypeBySearchString
    intent: Find users to add as contract reviewers
    question: Who can I add as a reviewer on a contract, searching by name or email?
  phrasing_ops: 14
  slug: conga-review-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Conga Reviewer APIs
  name: Conga Reviewer API
  phrasing_intents:
  - id: getApiReviewV1ByReviewtypeByReviewidReviewers
    intent: Get reviewers' status on a review
    question: Who are the reviewers on a review request and where are they up to?
  - id: postApiReviewV1ByReviewtypeByReviewidReviewers
    intent: Add reviewers to a started review
    question: How do I add more reviewers to a review that's already in progress?
  - id: deleteApiReviewV1ByReviewtypeByReviewidReviewersByReviewerid
    intent: Cancel a reviewer
    question: How do I cancel one reviewer and revoke their access to the document?
  - id: postApiReviewV1ByReviewtypeByReviewidReviewersByRevieweridEnd
    intent: End one reviewer's review
    question: Can I end the review for just one reviewer while others keep going?
  phrasing_ops: 4
  slug: conga-reviewer-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Role Admin API from Conga — 7 operation(s) for role admin.
  name: Conga Role Admin API
  phrasing_intents:
  - id: getApiUserManagementV1Roles
    intent: List roles as an admin
    question: Which roles exist in user management, filtered by my criteria?
  - id: postApiUserManagementV1Roles
    intent: Create a role
    question: How do I create a new user-management role with permission groups?
  - id: postApiUserManagementV1RolesBulk
    intent: Create many roles at once
    question: Can I create several roles in one request?
  - id: deleteApiUserManagementV1RolesByRoleId
    intent: Delete a role
    question: How do I delete a role I no longer use?
  - id: getApiUserManagementV1RolesByRoleId
    intent: Get a role's details
    question: What permission groups and settings does a role have?
  - id: putApiUserManagementV1RolesByRoleId
    intent: Rename or redescribe a role
    question: Can I change a role's name and description?
  - id: deleteApiUserManagementV1RolesByRoleIdAdminPermissions
    intent: Remove admin permissions from a role
    question: Can I strip specific admin permissions from a role?
  - id: putApiUserManagementV1RolesByRoleIdAdminPermissions
    intent: Grant admin permissions to a role
    question: How do I give a role additional admin permissions?
  phrasing_ops: 12
  slug: conga-role-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Role API from Conga — 6 operation(s) for role.
  name: Conga Role API
  phrasing_intents:
  - id: Role_CreateAdHocGroup
    intent: Add an ad hoc signer group to a transaction
    question: How do I create a group where any one member can sign for everyone?
  - id: Role_DeleteAdHocGroup
    intent: Delete an ad hoc group
    question: What happens to member roles when I delete an ad hoc group?
  - id: Role_UpdateAdHocGroup
    intent: Update an ad hoc group's members
    question: How do I change the members of an ad hoc group in a transaction?
  - id: Role_CreateRole
    intent: Add a signer role to a package
    question: How do I add another signer to an existing package?
  - id: Role_ListRoles
    intent: List a package's roles
    question: Who are the signers and roles on a package?
  - id: Role_ReorderRoles
    intent: Reorder a package's signing roles
    question: Can I change the signing order of roles in a package?
  - id: Role_DeleteRole
    intent: Remove a role from a package
    question: How do I remove a signer from a package?
  - id: Role_GetRole
    intent: Get one role in a package
    question: How do I look up a single signer role on a package?
  phrasing_ops: 11
  slug: conga-role-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The RolesVerification API from Conga — 2 operation(s) for rolesverification.
  name: Conga Roles Verification API
  phrasing_intents:
  - id: RolesVerification_GetAccountVerificationTypes
    intent: List the account's verification types
    question: Which advanced identity verification methods are available in my account?
  - id: RolesVerification_CreateRoleVerification
    intent: Add advanced verification to a role
    question: How do I require an external identity check before a signer can sign?
  - id: RolesVerification_DeleteRoleVerification
    intent: Remove a role's advanced verification
    question: Can I drop the extra identity verification from a signer role?
  - id: RolesVerification_GetRoleVerification
    intent: Get a role's verification method
    question: What verification method is set for a signer role in a package?
  - id: RolesVerification_UpdateRoleVerification
    intent: Change a role's verification method
    question: Can I switch the verification type already set on a signer role?
  phrasing_ops: 5
  slug: conga-rolesverification-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The RuleDimensions API from Conga — 2 operation(s) for ruledimensions.
  name: Conga Rule Dimensions API
  phrasing_intents:
  - id: RuleDimensions_Save
    intent: Create an approval rule dimension
    question: How do I define a new dimension that approval rules can evaluate?
  - id: RuleDimensions_DeleteById
    intent: Delete an approval rule dimension
    question: Can I delete a rule dimension we no longer use in approval rules?
  - id: RuleDimensions_GetById
    intent: Get an approval rule dimension
    question: What datasource and business object does a rule dimension use?
  - id: RuleDimensions_UpdateById
    intent: Update an approval rule dimension
    question: Can I change the datasource on an existing rule dimension?
  phrasing_ops: 4
  slug: conga-ruledimensions-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The RuleEntries API from Conga — 4 operation(s) for ruleentries.
  name: Conga Rule Entries API
  phrasing_intents:
  - id: RuleEntries_Save
    intent: Save an approval rule entry
    question: How do I create or edit an entry in an approval rule?
  - id: RuleEntries_Reorder
    intent: Reorder entries within an approval rule
    question: Can I change the order rule entries are evaluated in?
  - id: RuleEntries_Validate
    intent: Check if a rule entry label is taken
    question: Is a rule entry label already used in this rule?
  - id: RuleEntries_GetById
    intent: Get an approval rule entry
    question: How do I fetch a single approval rule entry?
  phrasing_ops: 4
  slug: conga-ruleentries-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides API endpoints for executing individual playbook rules against contract documents and retrieving clause-level and document-level rule execution results.
  name: Conga Rule Execution API
  phrasing_intents:
  - id: getApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdRulesClauseRuleByExecutionIdResults
    intent: Get a clause rule execution result
    question: What did a clause-level playbook rule find when it ran against my contract?
  - id: getApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdRulesDocumentRuleByExecutionIdResults
    intent: Get a document rule execution result
    question: What did a whole-document playbook rule conclude about my contract?
  - id: postApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdRulesByRuleIdContentRun
    intent: Run a playbook rule on contract document content
    question: How do I run a playbook rule against the raw text of a contract document?
  - id: postApiXauthorV1ContractsByContractIdPlaybooksByPlaybookIdRulesByRuleIdRun
    intent: Run a playbook rule on pre-extracted rule text
    question: Can I run a playbook rule using rule text that was already extracted from the contract?
  phrasing_ops: 4
  slug: conga-ruleexecution-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Rules API from Conga — 10 operation(s) for rules.
  name: Conga Rules API
  phrasing_intents:
  - id: Rules_GetAll
    intent: Search approval rules for a business object
    question: Which approval rules exist for a business object, by name?
  - id: Rules_Save
    intent: Save an approval rule
    question: How do I create an approval rule with its rule entries?
  - id: Rules_Validate
    intent: Check whether a rule name is already used
    question: Is this rule name already taken for the object type?
  - id: Rules_DeleteById
    intent: Delete an approval rule
    question: Can I permanently remove an approval rule?
  - id: Rules_GetById
    intent: Get an approval rule by ID
    question: What does one approval rule contain?
  - id: Rules_Activate
    intent: Activate an approval rule
    question: How do I turn an approval rule on?
  - id: Rules_Clone
    intent: Copy an approval rule
    question: Can I duplicate a rule to use as a template?
  - id: Rules_Deactivate
    intent: Deactivate an approval rule
    question: Can I switch off a whole rule without deleting it?
  phrasing_ops: 12
  slug: conga-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This controller provides access to information inside a customer's salesforce account.
  name: Conga Salesforce API
  phrasing_intents:
  - id: Salesforce_MockGetRelatedContacts
    intent: Get mock related contacts for testing
    question: Is there a mock endpoint that returns sample related contacts for a Salesforce record?
  - id: Salesforce_GetRecentSalesforceAttachments
    intent: Get recent attachments on a Salesforce record
    question: How do I list the recent files and attachments on a Salesforce record?
  - id: Salesforce_GetObjectType
    intent: Identify a Salesforce record's object type
    question: What type of Salesforce object is this record ID?
  - id: Salesforce_GetRelatedContacts
    intent: Get real contacts related to a Salesforce record
    question: Which contacts are related to a given Salesforce record?
  - id: Salesforce_SalesforceContactsLeadsUsers
    intent: Search Salesforce leads, contacts and users
    question: How do I search across Salesforce leads, contacts and users by name?
  - id: Salesforce_SalesforceTemplates
    intent: List managed package Salesforce templates
    question: What CET and CGT templates are in my Salesforce org's managed package?
  phrasing_ops: 6
  slug: conga-salesforce-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Scheduler API from Conga — 11 operation(s) for scheduler.
  name: Conga Scheduler API
  phrasing_intents:
  - id: getApiSchedulerV1Jobs
    intent: List scheduled jobs
    question: Which jobs are scheduled to run in my Conga platform?
  - id: postApiSchedulerV1JobsCron
    intent: Schedule a recurring cron job
    question: How do I schedule a job that runs on a cron expression?
  - id: postApiSchedulerV1JobsExport
    intent: Export all scheduled jobs as a ZIP
    question: Can I download every scheduled job's definition in one zip file?
  - id: postApiSchedulerV1JobsOnetime
    intent: Schedule a one-time job
    question: How do I schedule a job to run once at a specific time?
  - id: deleteApiSchedulerV1JobsByJobName
    intent: Delete a scheduled job
    question: Does deleting a scheduled job also wipe its execution history?
  - id: getApiSchedulerV1JobsByJobName
    intent: Get a scheduled job's details
    question: What schedule and payload does a named job have?
  - id: putApiSchedulerV1JobsByJobNameCron
    intent: Change a cron job's schedule
    question: Can I change the cron expression of an existing scheduled job?
  - id: putApiSchedulerV1JobsByJobNameDisable
    intent: Pause a scheduled job
    question: Can I stop a scheduled job from running without deleting it?
  phrasing_ops: 12
  slug: conga-scheduler-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Search Admin API from Conga — 10 operation(s) for search admin.
  name: Conga Search Admin API
  phrasing_intents:
  - id: getApiSearchV1Datasyncstatus
    intent: Get search data sync status for all objects
    question: Are the search index and database in sync for every object?
  - id: getApiSearchV1DatasyncstatusByTrackingId
    intent: Check a search sync job by tracking ID
    question: Has the data sync I started finished yet?
  - id: postApiSearchV1DocumentIndex
    intent: Index a document for search
    question: How do I make a document searchable?
  - id: getApiSearchV1GlobalSearchDataTypes
    intent: List field types allowed in global search
    question: Which field data types can be used in global search configuration?
  - id: postApiSearchV1RbacMigrate
    intent: Migrate search RBAC settings
    question: How do I add missing RBAC fields to existing search settings?
  - id: postApiSearchV1Resyncdata
    intent: Resync search data for all non-document objects
    question: Can I resync every object whose search count doesn't match the database?
  - id: getApiSearchV1Setting
    intent: List all objects' search settings
    question: What search settings are configured across objects?
  - id: postApiSearchV1Setting
    intent: Create a search setting for an object
    question: How do I enable search on a new object?
  phrasing_ops: 12
  slug: conga-search-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Search Runtime API from Conga — 6 operation(s) for search runtime.
  name: Conga Search Runtime API
  phrasing_intents:
  - id: postApiSearchV1DocumentQuery
    intent: Search documents
    question: How do I run a full-text or advanced search across documents?
  - id: postApiSearchV1ObjectsMultipleQuery
    intent: Search across several objects
    question: Can I search several record types in one query?
  - id: getApiSearchV1ObjectsByObjectNameIndexedfields
    intent: List an object's searchable fields
    question: Which fields of an object are searchable or indexed?
  - id: postApiSearchV1ObjectsByObjectNameQuery
    intent: Search records of one object
    question: How do I query records of a single object type with criteria and sorting?
  - id: getApiSearchV1SettingList
    intent: List objects with search enabled
    question: Which objects have search settings enabled?
  - id: getApiSearchV1SettingByObjectName
    intent: Get an object's search setting
    question: How is search configured for a specific object?
  phrasing_ops: 6
  slug: conga-search-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Sender API from Conga — 6 operation(s) for sender.
  name: Conga Sender API
  phrasing_intents:
  - id: Sender_CreateSender
    intent: Add a new user to the signing account
    question: How do I add a new sender to my e-signature account?
  - id: Sender_ListSenders
    intent: List users in the signing account
    question: Who are the senders set up in my Conga Sign account?
  - id: Sender_DeleteSender
    intent: Remove a sender from the account
    question: Can I delete a user who has left the company from my signing account?
  - id: Sender_GetSender
    intent: Get a sender's account details
    question: What details are stored for a specific sender in the account?
  - id: Sender_UpdateSender
    intent: Update a sender's details
    question: Can I change an existing sender's name, title or phone number?
  - id: Sender_InviteSender
    intent: Email an account invitation to a user
    question: How do I send an invitation email so a user can join the account?
  - id: Sender_UpdatePassword
    intent: Change my own sender password
    question: Can I change my own password through the API if I know the current one?
  - id: Sender_ResetPassword
    intent: Send a password reset email to a user
    question: A user forgot their password; can I trigger a reset email for them?
  phrasing_ops: 11
  slug: conga-sender-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Catalog APIs to search service products
  name: Conga Services API
  phrasing_intents:
  - id: postServices
    intent: List service products on a price list
    question: Which active service products can I sell from a given price list?
  phrasing_ops: 1
  slug: conga-services-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Session API from Conga — 1 operation(s) for session.
  name: Conga Session API
  phrasing_intents:
  - id: Session_GetSession
    intent: Get the current session
    question: What does my current signing session object contain?
  phrasing_ops: 1
  slug: conga-session-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Settings API from Conga — 2 operation(s) for settings.
  name: Conga Settings API
  phrasing_intents:
  - id: getFeatureSettings
    intent: List all feature settings
    question: Which feature settings are turned on in my Conga tenant?
  - id: patchFeatureSettings
    intent: Toggle feature settings
    question: How do I switch feature settings on or off?
  - id: getFeatureSettingsByFeatureSettingName
    intent: Get one feature setting
    question: Is a particular feature setting enabled?
  phrasing_ops: 3
  slug: conga-settings-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: sign APIs
  name: Conga Sign API
  phrasing_intents:
  - id: postApiClmV1SignEsignaturesWetsignByTransactionIdEnd
    intent: Finish a CLM wet signature and attach it to the contract
    question: Once a contract has been signed on paper, can I close out the wet signature in CLM and attach the scanned copy to the agreement?
  - id: postApiEsignV1Esignatures
    intent: Create an eSignature envelope for documents
    question: How do I send contract documents out for electronic signature from Conga?
  - id: getApiEsignV1EsignaturesEventlogs
    intent: Page through all eSignature event logs
    question: Where can I see the full log of eSignature listener events across every package?
  - id: getApiEsignV1EsignaturesEventlogsByPackageId
    intent: Get the event log for one signature package
    question: What events have been recorded for a single signature package I sent?
  - id: getApiEsignV1EsignaturesSignertypes
    intent: List signer roles an eSignature provider allows
    question: What signer types can I put in the Role field when building an envelope?
  - id: getApiEsignV1EsignaturesTemplates
    intent: List templates held by the eSignature provider
    question: What signing templates already exist in my eSignature provider account?
  - id: getApiEsignV1EsignaturesTransactionByObjectIdLatestSignTransaction
    intent: Find which sign provider handled a record's latest signing
    question: Which eSignature provider was used for the most recent signing on this agreement?
  - id: getApiEsignV1EsignaturesTransactionByObjectIdByObjectId
    intent: Look up signature transaction details by record ID
    question: I only have the agreement record ID I used for the envelope; can I still get its signing status?
  phrasing_ops: 12
  slug: conga-sign-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The SignatureImage API from Conga — 1 operation(s) for signatureimage.
  name: Conga Signature Image API
  phrasing_intents:
  - id: SignatureImage_GetSignatureImage
    intent: Get a role's signature image in a package
    question: Can I download the signature a signer role used in a package?
  phrasing_ops: 1
  slug: conga-signatureimage-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The SignatureLayout API from Conga — 1 operation(s) for signaturelayout.
  name: Conga Signature Layout API
  phrasing_intents:
  - id: SignatureLayout_GetSignatureLayout
    intent: Get signature layout configuration
    question: What logo and capture layout does my signature block use?
  - id: SignatureLayout_UpdateSignatureLayout
    intent: Update signature layout configuration
    question: Can I change the logo shown in signatures?
  phrasing_ops: 2
  slug: conga-signaturelayout-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Solution API from Conga — 5 operation(s) for solution.
  name: Conga Solution API
  phrasing_intents:
  - id: Solution_CreateSolution
    intent: Create a Composer solution
    question: How do I create a new document generation solution?
  - id: Solution_GetAllSolutions
    intent: List Composer solutions
    question: Which Composer solutions have I built?
  - id: Solution_GetLanguages
    intent: List code languages for a solution's deploy step
    question: Which programming languages can the deploy step generate code in?
  - id: Solution_SalesforceContacts
    intent: Search Salesforce contacts
    question: Can I look up Salesforce contacts while configuring a solution?
  - id: Solution_GetSnippet
    intent: Generate a code snippet for a solution
    question: Can I get ready-to-use code that calls my solution?
  - id: Solution_DeleteSolution
    intent: Delete a Composer solution
    question: Can I permanently remove a solution I no longer use?
  - id: Solution_GetSolutionById
    intent: Get a Composer solution
    question: What templates and delivery options does a solution use?
  - id: Solution_PatchSolution
    intent: Partially update a Composer solution
    question: Can I change just one field, like the status, on a solution?
  phrasing_ops: 8
  slug: conga-solution-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Provides endpoints for managing invoice split criteria setups, including creation, activation, and deactivation.
  name: Conga Split Criteria API
  phrasing_intents:
  - id: getSplitCriteria
    intent: List invoice split criteria
    question: Which invoice split criteria setups are configured?
  - id: patchSplitCriteria
    intent: Bulk-update invoice split criteria
    question: Can I update several split criteria setups in one request?
  - id: postSplitCriteria
    intent: Create an invoice split criteria setup
    question: How do I set up new criteria for splitting invoices?
  - id: patchSplitCriteriaActivate
    intent: Toggle active status on several split criteria
    question: How do I activate or deactivate multiple split criteria setups together?
  - id: getSplitCriteriaById
    intent: Get a split criteria setup
    question: How do I look up one invoice split criteria setup?
  - id: patchSplitCriteriaByIdActivate
    intent: Activate one split criteria setup
    question: Can I activate or deactivate a single split criteria setup by ID?
  phrasing_ops: 6
  slug: conga-split-criteria-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Get merge process status
  name: Conga Status API
  phrasing_intents:
  - id: Status_Get
    intent: Get a merge process status
    question: Is my document merge finished yet?
  phrasing_ops: 1
  slug: conga-status-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Storefronts API from Conga — 3 operation(s) for storefronts.
  name: Conga Storefronts API
  phrasing_intents:
  - id: deleteStorefronts
    intent: Delete several storefronts at once
    question: Can I remove a whole list of storefronts by their IDs in one go?
  - id: getStorefronts
    intent: List storefronts
    question: What storefronts are set up in my Conga commerce admin?
  - id: patchStorefronts
    intent: Update several storefronts at once
    question: Can I change settings on many storefronts with one request?
  - id: postStorefronts
    intent: Create one or more storefronts
    question: How do I add a new storefront?
  - id: getStorefrontsActive
    intent: Get the active storefront
    question: Which storefront is currently active for my session?
  - id: deleteStorefrontsById
    intent: Delete one storefront
    question: Can I delete a single storefront I no longer use?
  - id: getStorefrontsById
    intent: Retrieve a single storefront
    question: How can I see the full details of one specific storefront?
  - id: patchStorefrontsById
    intent: Update one storefront
    question: Can I edit the details of just one storefront?
  phrasing_ops: 8
  slug: conga-storefronts-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The SubAccounts API from Conga — 4 operation(s) for subaccounts.
  name: Conga Sub Accounts API
  phrasing_intents:
  - id: SubAccounts_ListAccessibleSubAccounts
    intent: List sub-accounts I can access
    question: Which sub-accounts am I allowed to access?
  - id: SubAccounts_ListSubAccountApiKeys
    intent: List my API keys across sub-accounts
    question: How do I get my API keys for each sub-account?
  - id: SubAccounts_CreateSubAccount
    intent: Create a sub-account
    question: How do I create a child account for a department or region?
  - id: SubAccounts_ListSubAccounts
    intent: List child sub-accounts of my account
    question: What sub-accounts sit under my current account?
  - id: SubAccounts_UpdateSubAccount
    intent: Update a sub-account
    question: How do I rename an existing sub-account?
  phrasing_ops: 5
  slug: conga-subaccounts-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Summary Groups Controller
  name: Conga Summary Groups API
  phrasing_intents:
  - id: getApiCartV1CartsByCartIdSummarygroups
    intent: Get a cart's summary groups
    question: What summary groups and subtotals does a cart have?
  - id: postApiCartV1CartsByCartIdSummarygroups
    intent: Add summary groups to a cart
    question: Can I add new summary group records to a cart?
  - id: putApiCartV1CartsByCartIdSummarygroups
    intent: Update a cart's summary groups
    question: How do I apply adjustments to a cart's summary groups?
  - id: putApiCartV1CartsByCartIdSummarygroupsAdhoc
    intent: Update a cart's ad hoc summary groups
    question: How do I save changes to ad hoc summary groups in a cart?
  phrasing_ops: 4
  slug: conga-summarygroups-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: TaxCodes Controller
  name: Conga Tax Codes API
  phrasing_intents:
  - id: deleteTaxCodes
    intent: Delete several tax codes at once
    question: Can I delete a list of tax codes in one request, and is there a maximum?
  - id: getTaxCodes
    intent: List tax codes
    question: What tax codes are defined in my CPQ setup?
  - id: patchTaxCodes
    intent: Update several tax codes at once
    question: Can I change fields on many tax codes together?
  - id: postTaxCodes
    intent: Create one or more tax codes
    question: How do I add new tax codes to CPQ?
  - id: deleteTaxCodesById
    intent: Delete one tax code
    question: Can I delete a single tax code by its ID?
  - id: getTaxCodesById
    intent: Retrieve a single tax code
    question: How can I see the details of one particular tax code?
  - id: patchTaxCodesById
    intent: Update one tax code
    question: Can I edit just one tax code without touching the others?
  phrasing_ops: 7
  slug: conga-tax-codes-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Team Role API from Conga — 3 operation(s) for team role.
  name: Conga Team Role API
  phrasing_intents:
  - id: deleteApiClmV1Teamroles
    intent: Delete several team roles at once
    question: Can I permanently remove a batch of team roles by their IDs?
  - id: postApiClmV1Teamroles
    intent: Create a contract team role
    question: How do I set up a new team role for people who review or sign contracts in CLM?
  - id: postApiClmV1TeamrolesQuery
    intent: Search team roles with criteria
    question: What team roles exist in CLM, and can I filter them with a criteria expression?
  - id: deleteApiClmV1TeamrolesByTeamRoleId
    intent: Delete one team role
    question: Can I permanently delete a single team role?
  - id: getApiClmV1TeamrolesByTeamRoleId
    intent: Get a team role
    question: How can I view the details and actions of a specific team role?
  - id: putApiClmV1TeamrolesByTeamRoleId
    intent: Update a team role
    question: Can I rename an existing team role or change its description?
  phrasing_ops: 6
  slug: conga-team-role-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Controller for Templates APIs
  name: Conga Template API
  phrasing_intents:
  - id: postApiClmV1TemplatesQuery
    intent: Find contract templates
    question: Which CLM templates match a given name or type?
  phrasing_ops: 1
  slug: conga-template-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: This class contains API endpoints for template migration.
  name: Conga Template Migrate API
  phrasing_intents:
  - id: postApiXauthorV1TemplatesExport
    intent: Export an X-Author template as a zip
    question: How do I package an X-Author template with its clauses so I can move it to another org?
  - id: postApiXauthorV1TemplatesImport
    intent: Import an X-Author template from a zip
    question: Can I load a template into a new org using the zip I exported earlier?
  phrasing_ops: 2
  slug: conga-templatemigrate-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Timezone and Locale API from Conga — 9 operation(s) for timezone and locale.
  name: Conga Timezone and Locale API
  phrasing_intents:
  - id: getApiUserManagementV1DecimalSymbols
    intent: List decimal symbols used by locales
    question: Which decimal separator characters can a user pick for their number format?
  - id: getApiUserManagementV1DigitgroupingSymbols
    intent: List digit grouping symbols used by locales
    question: What thousands separator characters are supported in user locale settings?
  - id: getApiUserManagementV1Digitgroups
    intent: List digit grouping patterns used by locales
    question: What digit grouping patterns, like groups of three, do the locales support?
  - id: getApiUserManagementV1Locales
    intent: List all supported locales
    question: Which locales can I assign to a user in Conga?
  - id: getApiUserManagementV1LongdateFormats
    intent: List long date formats used by locales
    question: What long date formats, with the month spelled out, can users choose from?
  - id: getApiUserManagementV1NegativenumberFormats
    intent: List negative number formats used by locales
    question: How are negative numbers allowed to display, for example with a minus sign or parentheses?
  - id: getApiUserManagementV1ShortdateFormats
    intent: List short date formats used by locales
    question: Which short numeric date formats like MM/dd/yyyy can users choose?
  - id: getApiUserManagementV1TimeFormats
    intent: List time formats used by locales
    question: What time-of-day formats, 12-hour or 24-hour, are available for users?
  phrasing_ops: 9
  slug: conga-timezone-and-locale-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Token API from Conga — 3 operation(s) for token.
  name: Conga Token API
  phrasing_intents:
  - id: getApiXauthorV1GoogleToken
    intent: Get a Google auth token for X-Author
    question: Where does X-Author get the token it uses to talk to Google APIs?
  - id: getApiXauthorV1SitesBySiteNameValidate
    intent: Check that a SharePoint site is valid
    question: Can I verify a custom SharePoint site name before X-Author uses it?
  - id: postApiXauthorV1Token
    intent: Exchange credentials for an X-Author auth token
    question: What do I send to get an X-Author access token using a client ID and secret?
  phrasing_ops: 3
  slug: conga-token-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Translation Audit History Tracking API from Conga — 1 operation(s) for translation audit history tracking.
  name: Conga Translation Audit History Tracking API
  phrasing_intents:
  - id: getApiAuditV1TranslationsLocalesByLocaleModulesByModuleKeysByKeyAuditHistory
    intent: See the change history of a translation
    question: Who changed a translated label, and what did it say before?
  phrasing_ops: 1
  slug: conga-translation-audit-history-tracking-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Translation Management Runtime API from Conga — 1 operation(s) for translation management runtime.
  name: Conga Translation Management Runtime API
  phrasing_intents:
  - id: getApiLocalizationV1Translations
    intent: Get all string translations for several modules
    question: Can I load every string translation for a few modules at once, grouped by module?
  - id: postApiLocalizationV1Translations
    intent: Look up translations for chosen keys across modules
    question: Can I fetch translations for specific keys from several modules in a single request?
  phrasing_ops: 2
  slug: conga-translation-management-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Translation Runtime API from Conga — 5 operation(s) for translation runtime.
  name: Conga Translation Runtime API
  phrasing_intents:
  - id: getApiLocalizationV1TranslationsModulesByModuleBulk
    intent: Page through all translations in a module
    question: Can I download every translation in a module like CPQ.CART page by page?
  - id: postApiLocalizationV1TranslationsByModuleBulk
    intent: Translate a list of keys in one module
    question: Can I get the user's-locale text for a list of keys from one module in one call?
  - id: postApiLocalizationV1TranslationsByModuleBulkParameters
    intent: Translate many keys with message parameters
    question: Can I translate several keys at once and fill in their placeholder variables?
  - id: getApiLocalizationV1TranslationsByModuleByKey
    intent: Get the translation of one key
    question: What does a single translation key read as in my locale?
  - id: getApiLocalizationV1TranslationsByModuleByKeyParameters
    intent: Get one translated message with variables filled in
    question: Can I get a single translated message with its variables substituted?
  phrasing_ops: 5
  slug: conga-translation-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Translations Management Admin API from Conga — 11 operation(s) for translations management admin.
  name: Conga Translations Management Admin API
  phrasing_intents:
  - id: getApiLocalizationAdminV1Translations
    intent: Browse translations page by page
    question: Can I browse String or Schema translations by numbered page, with a total count?
  - id: deleteApiLocalizationAdminV1TranslationsLocalesByLocale
    intent: Bulk delete translations for a locale
    question: Can I remove a batch of translations from one locale?
  - id: postApiLocalizationAdminV1TranslationsLocalesByLocale
    intent: Bulk add new translations for a locale
    question: How do I add a batch of new translations for a locale that has none yet?
  - id: putApiLocalizationAdminV1TranslationsLocalesByLocale
    intent: Bulk update translations for a locale
    question: Can I overwrite many existing translations for one locale in a single request?
  - id: postApiLocalizationAdminV1TranslationsLocalesByLocaleCustomExport
    intent: Export a locale's custom translations to CSV
    question: Can I download a locale's custom translations as a CSV file to send to translators?
  - id: postApiLocalizationAdminV1TranslationsLocalesByLocaleCustomImport
    intent: Import a translation file for a locale
    question: How do I upload a file of translated strings back in for a locale?
  - id: getApiLocalizationAdminV1TranslationsModules
    intent: List translation modules for a type
    question: What translation modules are defined, such as CLM.DOC_GEN or CPQ.CART?
  - id: getApiLocalizationAdminV1TranslationsOrganizationLocales
    intent: View the organization's configured locales
    question: Which languages are currently enabled for my organization?
  phrasing_ops: 14
  slug: conga-translations-management-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The TypeAhead API from Conga — 1 operation(s) for typeahead.
  name: Conga Type Ahead API
  phrasing_intents:
  - id: getByObjectnameTypeAhead
    intent: Get type-ahead suggestions for an object
    question: Can I get autocomplete suggestions for records of an object as a user types?
  phrasing_ops: 1
  slug: conga-typeahead-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The UFC API from Conga — 2 operation(s) for ufc.
  name: Conga UFC API
  phrasing_intents:
  - id: postApiXauthorV1ContractsByContractIdUfcRepeatData
    intent: Load repeat and section data for the UFC screen
    question: Can I pull the repeat tables and section data from a contract document to show in the UFC screen?
  - id: postApiXauthorV1ContractsByContractIdUfcUpdateDocument
    intent: Save repeat and section edits to a contract document
    question: After editing repeat rows in the UFC screen, how do I write them back into the contract document?
  phrasing_ops: 2
  slug: conga-ufc-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The UOM Conversion Admin API from Conga — 3 operation(s) for uom conversion admin.
  name: Conga UOM Conversion Admin API
  phrasing_intents:
  - id: getApiConversionManagementV1UomConversionRates
    intent: List unit of measure conversion rates
    question: What unit of measure conversion rates are set up, for example from Box to Each?
  - id: postApiConversionManagementV1UomConversionRates
    intent: Add a unit of measure conversion rate
    question: How do I define how many Each are in a Box for a product?
  - id: postApiConversionManagementV1UomConversionRatesBulk
    intent: Add many UOM conversion rates at once
    question: Can I load a list of new unit conversion rates in one go?
  - id: putApiConversionManagementV1UomConversionRatesBulk
    intent: Update many UOM conversion rates at once
    question: Can I change a whole batch of unit conversion rates in a single request?
  - id: deleteApiConversionManagementV1UomConversionRatesById
    intent: Delete a UOM conversion rate
    question: Can I remove a unit conversion rate that's no longer valid?
  - id: getApiConversionManagementV1UomConversionRatesById
    intent: Get one UOM conversion rate
    question: Can I look up the details of one conversion rate record by its ID?
  - id: putApiConversionManagementV1UomConversionRatesById
    intent: Update one UOM conversion rate
    question: Can I correct the rate on a single unit conversion record?
  phrasing_ops: 7
  slug: conga-uom-conversion-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The UOM Conversion Runtime API from Conga — 3 operation(s) for uom conversion runtime.
  name: Conga UOM Conversion Runtime API
  phrasing_intents:
  - id: postApiConversionManagementV1QueryUomConversion
    intent: Convert a quantity between units of measure
    question: How many Each is 12 Box for this product?
  - id: postApiConversionManagementV1QueryUomConversionRates
    intent: Find the effective rate between two units
    question: What conversion rate currently applies between two units for a given product?
  - id: postApiConversionManagementV1QueryUomConversionRatesBulk
    intent: Look up effective rates for many unit pairs
    question: Can I get the effective conversion rates for many unit pairs in one request?
  phrasing_ops: 3
  slug: conga-uom-conversion-runtime-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: Usage Tiers Controller
  name: Conga Usage Tiers API
  phrasing_intents:
  - id: deleteApiCartV1CartsByCartIdItemsByItemIdUsageTiers
    intent: Remove usage price tiers from a line item
    question: Is there a way to strip all usage tiers off a cart line item?
  - id: getApiCartV1CartsByCartIdItemsByItemIdUsageTiers
    intent: View usage price tiers on a cart line item
    question: What usage-based price tiers are set on a line item in my Conga cart?
  - id: postApiCartV1CartsByCartIdItemsByItemIdUsageTiers
    intent: Add usage price tiers to a cart line item
    question: Can I add new usage-based pricing tiers to a line item that has none yet?
  - id: putApiCartV1CartsByCartIdItemsByItemIdUsageTiers
    intent: Change existing usage price tiers on a line item
    question: How do I edit usage price tiers that already exist on a cart line item?
  phrasing_ops: 4
  slug: conga-usagetiers-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The User Admin API from Conga — 15 operation(s) for user admin.
  name: Conga User Admin API
  phrasing_intents:
  - id: getApiUserManagementV1Users
    intent: List users in the organization
    question: Can I list every user in my Conga platform tenant?
  - id: postApiUserManagementV1Users
    intent: Create a single user
    question: How do I add one new user with a name, email and role?
  - id: patchApiUserManagementV1UsersBulk
    intent: Update many existing users at once
    question: Can I patch fields on a whole batch of existing users together?
  - id: postApiUserManagementV1UsersBulk
    intent: Create many new users in one request
    question: Can I create a batch of brand-new users in a single call?
  - id: putApiUserManagementV1UsersBulkUpsert
    intent: Create or update many users asynchronously
    question: Is there an upsert that updates existing users and creates missing ones in one go?
  - id: putApiUserManagementV1UsersBulkUpsertSync
    intent: Create or update many users synchronously
    question: Can I run a user upsert that waits and returns all IDs in the same response?
  - id: getApiUserManagementV1UsersTemplatesDownload
    intent: Download the CSV template for user upload
    question: Where do I get the CSV template with all user fields for importing users?
  - id: postApiUserManagementV1UsersUpload
    intent: Import users from a CSV file
    question: How do I import users from a CSV file?
  phrasing_ops: 21
  slug: conga-user-admin-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: User Search APIs
  name: Conga User API
  phrasing_intents:
  - id: getApiReviewV1Office365ActiveDirectoryUsers
    intent: Search Office 365 Active Directory users
    question: Can I look up people in our Office 365 Active Directory to add as reviewers?
  - id: getApiReviewV1ByReviewtypeReviewersQuery
    intent: Search for reviewers by review type
    question: Which users can I pick as reviewers for a given review type?
  - id: getApiUserManagementV1UserActionpermissions
    intent: List all my object action permissions
    question: What actions am I allowed to perform across all objects?
  - id: getApiUserManagementV1UserCurrency
    intent: Get my user currency
    question: Which currency is set for my logged-in user?
  - id: getApiUserManagementV1UserCurrencyFormat
    intent: Get my currency display format
    question: How are positive and negative amounts formatted for my user?
  - id: getApiUserManagementV1UserInfo
    intent: Get my signed-in user profile
    question: Who am I logged in as, and what's on my user profile?
  - id: getApiUserManagementV1UserLocale
    intent: Get my locale settings
    question: What locale is configured for my user account?
  - id: getApiUserManagementV1UserObjectAccessUsers
    intent: Find users with full access to objects
    question: Which users have full access to a set of objects?
  phrasing_ops: 18
  slug: conga-user-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The User Group API from Conga — 3 operation(s) for user group.
  name: Conga User Group API
  phrasing_intents:
  - id: getApiUserManagementV1UserGroups
    intent: Search platform user groups in user management
    question: Which user groups are defined in the platform's user management service?
  - id: postApiUserManagementV1UserGroups
    intent: Create a platform user group
    question: How do I add a new group in the platform user management service?
  - id: putApiUserManagementV1UserGroupsBulkUpsertUserGroups
    intent: Create or update many user groups in one call
    question: Is there a way to create and update a batch of user groups at once?
  - id: deleteApiUserManagementV1UserGroupsByUserGroupId
    intent: Delete a platform user group
    question: Can I remove a group from the user management service?
  - id: getApiUserManagementV1UserGroupsByUserGroupId
    intent: Get a platform user group's details
    question: What are the details of a particular user-management group?
  - id: putApiUserManagementV1UserGroupsByUserGroupId
    intent: Update a platform user group
    question: How do I change the email on a user-management group?
  - id: UserGroup_CreateUserGroup
    intent: Create a new user group
    question: How do I set up a new group of approvers?
  - id: UserGroup_GetUserGroups
    intent: List approval user groups
    question: What user groups exist for routing approvals?
  phrasing_ops: 14
  slug: conga-user-group-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The User Group Member API from Conga — 5 operation(s) for user group member.
  name: Conga User Group Member API
  phrasing_intents:
  - id: postApiUserManagementV1UserGroupsBulkCreateUserGroupMembers
    intent: Add members to user groups in bulk
    question: Can I add many members across several user groups in a single request?
  - id: getApiUserManagementV1UserGroupsMembers
    intent: List user group members across all groups
    question: Which user group memberships exist across every group in my org?
  - id: getApiUserManagementV1UserGroupsMembersByUserGroupMemberId
    intent: Get one user group membership
    question: What are the details of a single group membership record?
  - id: getApiUserManagementV1UserGroupsByUserGroupIdMembers
    intent: List the members of one user group
    question: Who belongs to a specific user group?
  - id: deleteApiUserManagementV1UserGroupsByUserGroupIdMembersByMemberId
    intent: Remove a member from a user group
    question: How do I take someone out of a user group?
  - id: postApiUserManagementV1UserGroupsByUserGroupIdMembersByMemberId
    intent: Add a member to a user group
    question: Can I add one user to a specific group?
  phrasing_ops: 6
  slug: conga-user-group-member-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The UserDashboard API from Conga — 4 operation(s) for userdashboard.
  name: Conga User Dashboard API
  phrasing_intents:
  - id: UserDashboard_GetCount
    intent: Count the user's approvals
    question: How many approvals are waiting for me overall?
  - id: UserDashboard_GetStatus
    intent: List my approval requests by status
    question: Which approval requests of mine are in a given status?
  - id: UserDashboard_GetDashboardData
    intent: Get dashboard approval data for a business object
    question: Can I get approval counts by status plus the records for one business object?
  - id: UserDashboard_GetDashboardCount
    intent: Count approvals for one business object
    question: How many approvals are there for a specific object type?
  phrasing_ops: 4
  slug: conga-userdashboard-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Validation API from Conga — 2 operation(s) for validation.
  name: Conga Validation API
  phrasing_intents:
  - id: postValidate
    intent: Validate data across multiple objects
    question: Can I check records from several different objects against validation rules in one call?
  - id: postByObjectNameValidate
    intent: Validate data for a single object
    question: How do I check one object's data against its validation criteria?
  phrasing_ops: 2
  slug: conga-validation-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The VirtualRoom API from Conga — 5 operation(s) for virtualroom.
  name: Conga Virtual Room API
  phrasing_intents:
  - id: VirtualRoom_GetVirtualRoomConfig
    intent: Get a package's virtual room settings
    question: How do I check whether a transaction has a virtual room with video enabled?
  - id: VirtualRoom_PutVirtualRoomConfig
    intent: Configure a package's virtual room
    question: How do I turn on video recording for a virtual room signing session?
  - id: VirtualRoom_GetVirtualRoomMaskedFields
    intent: List masked fields in a virtual room
    question: Which fields are hidden from other signers in a virtual room transaction?
  - id: VirtualRoom_PostVirtualRoomMaskedFields
    intent: Define the set of masked fields
    question: Can I define the whole list of fields to mask in a virtual room at once?
  - id: VirtualRoom_DeleteVirtualRoomMaskedFieldsById
    intent: Unmask a field in a virtual room
    question: How do I stop masking a field so other signers can see it?
  - id: VirtualRoom_PutVirtualRoomMaskedFieldsById
    intent: Mask one more field in a virtual room
    question: How do I add a single field to the masked list of a virtual room?
  - id: VirtualRoom_GetVirtualRoomRecordingById
    intent: Download a virtual room recording
    question: How do I download the video of a virtual room session?
  - id: VirtualRoom_GetVirtualRoomRecording
    intent: List virtual room recordings
    question: What session recordings are available for a virtual room transaction?
  phrasing_ops: 8
  slug: conga-virtualroom-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Visibility Rules API from Conga — 2 operation(s) for visibility rules.
  name: Conga Visibility Rules API
  phrasing_intents:
  - id: deleteVisibilityRule
    intent: Delete several visibility rules at once
    question: Can I remove a whole batch of visibility rules in one go?
  - id: getVisibilityRule
    intent: List catalog visibility rules
    question: Which visibility rules control what products show in my Conga catalog?
  - id: patchVisibilityRule
    intent: Update several visibility rules at once
    question: Can I deactivate many visibility rules with a single update?
  - id: postVisibilityRule
    intent: Create visibility rules
    question: How do I set up a new rule that hides certain products from the catalog?
  - id: deleteVisibilityRuleById
    intent: Delete one visibility rule
    question: How do I delete a single visibility rule by its ID?
  - id: getVisibilityRuleById
    intent: Get one visibility rule
    question: What does one particular visibility rule contain?
  - id: patchVisibilityRuleById
    intent: Update one visibility rule
    question: Can I edit just one visibility rule without touching the rest?
  phrasing_ops: 7
  slug: conga-visibility-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Waterfall Charts API from Conga — 2 operation(s) for waterfall charts.
  name: Conga Waterfall Charts API
  phrasing_intents:
  - id: deleteWaterfallsByParentIdCharts
    intent: Delete several charts from a waterfall
    question: Can I remove multiple charts from a waterfall in one request?
  - id: getWaterfallsByParentIdCharts
    intent: List the charts in a price waterfall
    question: Which charts are attached to a given price waterfall in Conga CPQ?
  - id: patchWaterfallsByParentIdCharts
    intent: Update several charts in a waterfall
    question: Can I edit fields on many of a waterfall's charts together?
  - id: postWaterfallsByParentIdCharts
    intent: Add charts to a waterfall
    question: How do I add a new chart to a price waterfall?
  - id: deleteWaterfallsByParentIdChartsById
    intent: Delete one waterfall chart
    question: Is there a way to delete just one chart from a waterfall?
  - id: getWaterfallsByParentIdChartsById
    intent: Get one waterfall chart
    question: What are the details of a single chart in a price waterfall?
  - id: patchWaterfallsByParentIdChartsById
    intent: Update one waterfall chart
    question: Can I change the settings of one chart in a price waterfall?
  phrasing_ops: 7
  slug: conga-waterfall-charts-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Waterfall Rules API from Conga — 2 operation(s) for waterfall rules.
  name: Conga Waterfall Rules API
  phrasing_intents:
  - id: deleteWaterfallRuleSetsByParentIdRules
    intent: Delete several rules from a waterfall rule set
    question: What's the maximum number of waterfall rules I can delete in one request?
  - id: getWaterfallRuleSetsByParentIdRules
    intent: List the rules in a waterfall rule set
    question: Which waterfall rules belong to a given rule set in Conga CPQ?
  - id: patchWaterfallRuleSetsByParentIdRules
    intent: Update several rules in a waterfall rule set
    question: Can I change fields on many waterfall rules in a rule set together?
  - id: postWaterfallRuleSetsByParentIdRules
    intent: Add rules to a waterfall rule set
    question: How do I add new rules to a waterfall rule set?
  - id: deleteWaterfallRuleSetsByParentIdRulesById
    intent: Delete one waterfall rule
    question: Is there a way to delete just one rule from a waterfall rule set?
  - id: getWaterfallRuleSetsByParentIdRulesById
    intent: Get one waterfall rule
    question: What does a single waterfall rule in a rule set look like?
  - id: patchWaterfallRuleSetsByParentIdRulesById
    intent: Update one waterfall rule
    question: Can I edit one waterfall rule without touching the others in its set?
  phrasing_ops: 7
  slug: conga-waterfall-rules-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The WaterfallRuleEntry API from Conga — 2 operation(s) for waterfallruleentry.
  name: Conga Waterfall Rule Entry API
  phrasing_intents:
  - id: deleteWaterfallRulesByParentIdEntries
    intent: Delete several entries from a waterfall rule
    question: Can I remove many entries from a condition or dimension waterfall rule at once?
  - id: getWaterfallRulesByParentIdEntries
    intent: List the entries in a waterfall rule
    question: Which entries make up a given waterfall rule in Conga CPQ?
  - id: patchWaterfallRulesByParentIdEntries
    intent: Update several entries in a waterfall rule
    question: Can I edit fields on many waterfall rule entries together?
  - id: postWaterfallRulesByParentIdEntries
    intent: Add entries to a waterfall rule
    question: How many entries can I create on one waterfall rule?
  - id: deleteWaterfallRulesByParentIdEntriesById
    intent: Delete one waterfall rule entry
    question: Is there a way to delete just one entry from a waterfall rule?
  - id: getWaterfallRulesByParentIdEntriesById
    intent: Get one waterfall rule entry
    question: What are the details of a single entry in a waterfall rule?
  - id: patchWaterfallRulesByParentIdEntriesById
    intent: Update one waterfall rule entry
    question: Can I change a single entry on a waterfall rule?
  phrasing_ops: 7
  slug: conga-waterfallruleentry-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The WaterfallRuleset API from Conga — 2 operation(s) for waterfallruleset.
  name: Conga Waterfall Ruleset API
  phrasing_intents:
  - id: deleteWaterfallRuleSets
    intent: Delete several waterfall rule sets at once
    question: Can I remove multiple waterfall rule sets in a single call?
  - id: getWaterfallRuleSets
    intent: List waterfall rule sets
    question: Which waterfall rule sets are defined in my Conga CPQ org?
  - id: patchWaterfallRuleSets
    intent: Update several waterfall rule sets at once
    question: Can I edit many waterfall rule sets with one update?
  - id: postWaterfallRuleSets
    intent: Create waterfall rule sets
    question: How do I create new waterfall rule sets?
  - id: deleteWaterfallRuleSetsById
    intent: Delete one waterfall rule set
    question: How do I delete a single waterfall rule set by ID?
  - id: getWaterfallRuleSetsById
    intent: Get one waterfall rule set
    question: What's configured on a single waterfall rule set?
  - id: patchWaterfallRuleSetsById
    intent: Update one waterfall rule set
    question: Can I edit just one waterfall rule set?
  phrasing_ops: 7
  slug: conga-waterfallruleset-api
- baseURL: https://rls.congacloud.com
  baseurl_source: declared
  description: The Waterfalls API from Conga — 2 operation(s) for waterfalls.
  name: Conga Waterfalls API
  phrasing_intents:
  - id: deleteWaterfalls
    intent: Delete several price waterfalls at once
    question: Can I remove multiple price waterfalls in one call?
  - id: getWaterfalls
    intent: List price waterfalls
    question: Which price waterfalls exist in my Conga CPQ setup?
  - id: patchWaterfalls
    intent: Update several price waterfalls at once
    question: Can I edit many price waterfalls with a single update?
  - id: postWaterfalls
    intent: Create price waterfalls
    question: How do I set up new price waterfalls?
  - id: deleteWaterfallsById
    intent: Delete one price waterfall
    question: How do I delete a single waterfall by its ID?
  - id: getWaterfallsById
    intent: Get one price waterfall
    question: What's configured on a single price waterfall?
  - id: patchWaterfallsById
    intent: Update one price waterfall
    question: Can I edit just one price waterfall?
  phrasing_ops: 7
  slug: conga-waterfalls-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The OAuth2 API from Conga — 4 operation(s) for oauth2.
  name: Conga O Auth2 API
  phrasing_intents:
  - id: OAuth2_CreateOAuth2Client
    intent: Create an OAuth2 client
    question: How do I get a client ID and secret for API access?
  - id: OAuth2_ListOAuth2Clients
    intent: List OAuth2 clients
    question: Which OAuth2 clients exist on my Conga account?
  - id: OAuth2_DeleteOAuth2Client
    intent: Delete an OAuth2 client
    question: Can I permanently revoke an OAuth2 client?
  - id: OAuth2_RegenerateOAuth2ClientSecret
    intent: Rotate an OAuth2 client secret
    question: How do I rotate a client secret that may have leaked?
  - id: OAuth2_GenerateOAuth2Token
    intent: Get an access token with client credentials
    question: How do I exchange my client ID and secret for an access token?
  phrasing_ops: 5
  slug: conga-oauth2-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Account Roles API from Conga — 4 operation(s) for account roles.
  name: Conga Account Roles API
  phrasing_intents:
  - id: AccountRoles_CreateAccountRole
    intent: Create an account role
    question: How do I create a custom role with specific permissions for my users?
  - id: AccountRoles_ListRoles
    intent: List account roles and permissions
    question: What account roles exist in my Conga Sign account and what permissions do they have?
  - id: AccountRoles_DeleteAccountRole
    intent: Delete an account role
    question: How do I delete an account role I no longer use?
  - id: AccountRoles_GetAccountRole
    intent: Get an account role
    question: How do I see the permissions on one account role?
  - id: AccountRoles_UpdateAccountRole
    intent: Update an account role
    question: How do I change the permissions of an existing account role?
  - id: AccountRoles_GetAccountUsers
    intent: List users assigned to an account role
    question: Which users have a particular account role?
  - id: AccountRoles_AssignAccountRoleToUser
    intent: Assign account roles to a user
    question: How do I give a user an account role?
  - id: AccountRoles_GetUserAccountRoles
    intent: Get a user's account roles
    question: What account roles does a specific sender have?
  phrasing_ops: 8
  slug: conga-account-roles-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Account Settings API from Conga — 1 operation(s) for account settings.
  name: Conga Account Settings API
  phrasing_intents:
  - id: AccountSettings_DeleteAccountSettings
    intent: Reset all Backoffice account settings
    question: Can I undo every customization and return account settings to defaults?
  - id: AccountSettings_GetAccountSettings
    intent: Get all Backoffice account settings
    question: What feature, package and designer settings are on my account?
  - id: AccountSettings_UpdateAccountSettings
    intent: Update Backoffice account settings
    question: Can I change only the package settings and leave the rest alone?
  phrasing_ops: 3
  slug: conga-account-settings-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: This class contains API endpoints for admin setting
  name: Conga Admin Settings API
  phrasing_intents:
  - id: getApiXauthorV1AdminSettings
    intent: Get X-Author administrator settings
    question: What user profile and org details does the X-Author add-in have configured?
  - id: getApiXauthorV1AdminSettingsGoogleServiceConfig
    intent: Get the Google Drive service configuration
    question: Which Google Drive service account and folder does X-Author use?
  phrasing_ops: 2
  slug: conga-admin-settings-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The business object controller
  name: Conga Business Object API
  phrasing_intents:
  - id: postApiCartV1BusinessObjectsByBusinessObjectIdCartsActivate
    intent: Launch the cart for a quote or business object
    question: How do I open a cart for a quote in Conga CPQ?
  - id: getApiCartV1BusinessObjectsByBusinessObjectIdCartsActive
    intent: Get the read-only active cart for a business object
    question: What is the current active cart on a quote, without opening it for edits?
  - id: postApiCartV1BusinessObjectsByBusinessObjectIdCartsReactivate
    intent: Reactivate a cart and sync quote fields into it
    question: How do I push updated quote fields like bill-to or ship-to account back into the cart?
  - id: postApiCartV1BusinessObjectsByBusinessObjectIdReactivate
    intent: Reactivate a cart via the legacy endpoint
    question: Is there an older reactivate endpoint that re-evaluates pricing without syncing any quote fields?
  phrasing_ops: 4
  slug: conga-business-object-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The cart actions controller
  name: Conga Cart Actions API
  phrasing_intents:
  - id: getApiCartV1CartsActive
    intent: Get the latest active cart
    question: Which cart is currently active for my quote?
  - id: postApiCartV1CartsByCartIdAbandon
    intent: Abandon a cart
    question: How do I abandon a cart I no longer need?
  - id: postApiCartV1CartsByCartIdActivate
    intent: Activate a cart
    question: Which cart statuses are allowed to be activated?
  - id: getApiCartV1CartsByCartIdAppliedRuleActions
    intent: List rule actions applied to a cart
    question: Which constraint rule actions have already been applied to my cart?
  - id: postApiCartV1CartsByCartIdClone
    intent: Clone a whole cart into a new cart
    question: How do I make a copy of an existing cart as a new cart?
  - id: postApiCartV1CartsByCartIdCloneLines
    intent: Copy lines from another cart into a cart
    question: Can I pull line items from a different cart into the cart I'm working on?
  - id: getApiCartV1CartsByCartIdConfigstatus
    intent: Get a cart's configuration status
    question: Is the product configuration on my cart complete?
  - id: getApiCartV1CartsByCartIdDisplayAction
    intent: Get display actions for a cart
    question: Which display actions are available on a cart in a given flow?
  phrasing_ops: 24
  slug: conga-cart-actions-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Cart Item Controller
  name: Conga Cart Items API
  phrasing_intents:
  - id: deleteApiCartV1CartsByCartIdItems
    intent: Remove line items from a cart
    question: Can I take products back out of a cart?
  - id: getApiCartV1CartsByCartIdItems
    intent: List the line items in a cart
    question: What products and line items are in my cart right now?
  - id: patchApiCartV1CartsByCartIdItems
    intent: Update line items in a cart
    question: How do I change quantities or fields on several cart line items?
  - id: postApiCartV1CartsByCartIdItems
    intent: Add products to a cart
    question: How do I add a bundle or standalone product to a cart?
  - id: postApiCartV1CartsByCartIdItemsClone
    intent: Duplicate line items within a cart
    question: Can I make an exact copy of a line item inside the same cart?
  - id: getApiCartV1CartsByCartIdItemsErrors
    intent: Get line item persistence errors for a cart
    question: Why did some of my cart line items fail to save?
  - id: postApiCartV1CartsByCartIdReprice
    intent: Reprice cart line items
    question: What do I call to reprice items after changing a cart?
  phrasing_ops: 7
  slug: conga-cart-items-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: This class contains APIs related to configuration management
  name: Conga Configuration Management API
  phrasing_intents:
  - id: putApiXauthorV1ConfigManagementCrmConnection
    intent: Toggle the connect-to-CRM flag
    question: How do I switch the X-Author connect-to-CRM setting on or off?
  phrasing_ops: 1
  slug: conga-configuration-management-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Custom Branding API from Conga — 3 operation(s) for custom branding.
  name: Conga Custom Branding API
  phrasing_intents:
  - id: CustomBranding_GetAllCustomBrandings
    intent: List uploaded custom branding logos
    question: Which custom branding logos have we uploaded?
  - id: CustomBranding_UploadCustomBranding
    intent: Upload a new branding logo
    question: How do I upload our company logo for document branding?
  - id: CustomBranding_DeleteCustomBranding
    intent: Delete a branding logo
    question: Can I delete an old logo we no longer brand documents with?
  - id: CustomBranding_GetCustomBrandingById
    intent: Get details of a branding logo
    question: What are the details of a specific uploaded logo?
  - id: CustomBranding_UpdateCustomBranding
    intent: Replace a logo image or rename it
    question: Can I swap the image on an existing branding logo without re-creating it?
  - id: CustomBranding_DownloadLogoFileById
    intent: Download a branding logo file
    question: How do I download the actual image file of an uploaded logo?
  phrasing_ops: 6
  slug: conga-custom-branding-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Custom Fields API from Conga — 2 operation(s) for custom fields.
  name: Conga Custom Fields API
  phrasing_intents:
  - id: CustomFields_CreateCustomField
    intent: Create an account custom field
    question: How do I add a new custom field to my account?
  - id: CustomFields_ListCustomFields
    intent: List account custom fields
    question: Which custom fields are defined on my Conga Sign account?
  - id: CustomFields_UpdateCustomField
    intent: Update an account custom field
    question: Can I change the value or translations of an existing custom field?
  - id: CustomFields_DeleteCustomField
    intent: Delete an account custom field
    question: Can I remove a custom field from my account?
  - id: CustomFields_GetCustomField
    intent: Get an account custom field
    question: What is configured on one custom field?
  phrasing_ops: 5
  slug: conga-custom-fields-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Customer Registration API from Conga — 1 operation(s) for customer registration.
  name: Conga Customer Registration API
  phrasing_intents:
  - id: CustomerRegistration_Delete
    intent: Delete OneSpan callback registration
    question: How do I remove the OneSpan callback customer registration?
  - id: CustomerRegistration_Get
    intent: Get OneSpan callback customer registration
    question: Is my OneSpan callback customer registration on file?
  - id: CustomerRegistration_Post
    intent: Register OneSpan callback client credentials
    question: How do I register client credentials for OneSpan callbacks?
  phrasing_ops: 3
  slug: conga-customer-registration-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Data Management API from Conga — 2 operation(s) for data management.
  name: Conga Data Management API
  phrasing_intents:
  - id: DataManagement_GetDataManagementPolicy
    intent: Get the data management policy
    question: How long does my account keep transactions before they are removed?
  - id: DataManagement_UpdateDataManagementPolicy
    intent: Update transaction retention policy
    question: Can I change how long transactions are retained?
  - id: DataManagement_GetExpiryTimeConfiguration
    intent: Get transaction expiry settings
    question: What expiry period is configured for transactions on my account?
  - id: DataManagement_UpdateExpiryTimeConfiguration
    intent: Update transaction expiry settings
    question: Can I set transactions to never expire?
  phrasing_ops: 4
  slug: conga-data-management-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: This class contains API endpoints for Document Review.
  name: Conga Document Review API
  phrasing_intents:
  - id: getApiXauthorV1DocumentsReviewsDetails
    intent: Check Send For Review status
    question: How do I check the Send For Review details of an agreement document?
  - id: getApiXauthorV1DocumentsReviewsStatus
    intent: Check whether a review cycle is pending
    question: Is there still a pending review cycle on my agreement?
  phrasing_ops: 2
  slug: conga-document-review-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: API to return job status details
  name: Conga Job Status API
  phrasing_intents:
  - id: deleteJobStatus
    intent: Delete a job and its child jobs
    question: Can I delete a job along with its child jobs?
  - id: postJobStatus
    intent: Get the status of several jobs
    question: Can I check the status of many background jobs at once?
  - id: getJobStatusByJobId
    intent: Get a job's status with child jobs
    question: Can I include child jobs when checking a job's status?
  - id: getJobStatusById
    intent: Get a job's status by record ID
    question: Is there a simple status lookup for one job record without child jobs?
  phrasing_ops: 4
  slug: conga-job-status-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Password Policy API from Conga — 1 operation(s) for password policy.
  name: Conga Password Policy API
  phrasing_intents:
  - id: PasswordPolicy_GetPasswordPolicy
    intent: Get the account password policy
    question: What is my account's password policy?
  - id: PasswordPolicy_UpdatePasswordPolicy
    intent: Update the account password policy
    question: How do I require longer passwords with special characters?
  phrasing_ops: 2
  slug: conga-password-policy-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: Review Site APIs
  name: Conga Review Sites API
  phrasing_intents:
  - id: getApiReviewV1Office365SitesBySiteNameValidate
    intent: Validate a SharePoint site for review
    question: How can I check that my custom SharePoint site is valid for document review?
  phrasing_ops: 1
  slug: conga-review-sites-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: This class contains APIs for Schema metadata.
  name: Conga Schema Metadata API
  phrasing_intents:
  - id: postApiXauthorV1SchemaMetadata
    intent: Get schema metadata for entities
    question: What fields and relationships do my CLM entities have for document authoring?
  phrasing_ops: 1
  slug: conga-schema-metadata-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The Search Filters API from Conga — 5 operation(s) for search filters.
  name: Conga Search Filters API
  phrasing_intents:
  - id: SearchFilters_GetAll
    intent: List saved search filters
    question: How do I find my saved search filters by name?
  - id: SearchFilters_Save
    intent: Create or update a search filter
    question: How do I save a new search filter?
  - id: SearchFilters_Validate
    intent: Check if a search filter name is taken
    question: Is a search filter name already in use for this object type?
  - id: SearchFilters_DeleteById
    intent: Delete a search filter
    question: How do I delete a saved search filter?
  - id: SearchFilters_GetById
    intent: Get a search filter
    question: How do I retrieve one saved search filter by ID?
  - id: SearchFilters_Activate
    intent: Activate a search filter
    question: How do I turn a saved search filter back on?
  - id: SearchFilters_Deactivate
    intent: Deactivate a search filter
    question: How do I disable a search filter without deleting it?
  phrasing_ops: 7
  slug: conga-search-filters-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: Search APIs to search product details
  name: Conga Smart Search API
  phrasing_intents:
  - id: postSearch
    intent: Search catalog products
    question: How do I search the product catalog with filters and facets?
  - id: getSearchTypeahead
    intent: Suggest products as the user types
    question: Can I get product suggestions from just the first few letters someone types?
  phrasing_ops: 2
  slug: conga-smart-search-api
- baseURL: https://rls.congacloud.com/mcp
  baseurl_source: declared
  description: The System Properties API from Conga — 5 operation(s) for system properties.
  name: Conga System Properties API
  phrasing_intents:
  - id: SystemProperties_GetSystemProperties
    intent: Get approvals system properties
    question: What are my current Approvals system properties, like max ad hoc groups?
  - id: SystemProperties_UpsertSystemConfig
    intent: Update approvals system properties
    question: How do I change the maximum number of ad hoc approvers per group?
  - id: SystemProperties_CreateEmailConfig
    intent: Create approvals email configuration
    question: Can I set up the approvals email configuration for the first time?
  - id: SystemProperties_GetEmailConfig
    intent: Get approvals email configuration
    question: What reply-to and compliance BCC addresses are configured for approval emails?
  - id: SystemProperties_UpdateEmailConfig
    intent: Change existing email configuration
    question: Can I change just the reply-to address on existing email settings?
  - id: SystemProperties_GetMultipleProductSettings
    intent: Get custom configurations by name
    question: Can I fetch several named product setting configurations at once?
  - id: SystemProperties_UpsertCustomConfig
    intent: Set a business object's custom configuration
    question: How do I set the approval status field for a business object?
  - id: SystemProperties_GetAllProductSettings
    intent: Get product settings for all objects
    question: What Approvals product settings are configured across every business object?
  phrasing_ops: 10
  slug: conga-system-properties-api
artifact_total: 363
asyncapis:
- description: ''
  name: Conga Webhooks
  slug: conga-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-conga-openapi-index
common:
- group: other
  href: https://artifacts.apis.io/conga/capabilities/conga-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/conga-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/conga/security/conga-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/conga-vulnerability-disclosure.yml
- group: build
  href: https://artifacts.apis.io/conga/packages/conga-packages.yml
  title: ''
  type: Packages
  url: packages/conga-packages.yml
- group: build
  href: https://artifacts.apis.io/conga/packages/conga-packages.yml
  title: ''
  type: SDKs
  url: packages/conga-packages.yml
- group: build
  href: https://artifacts.apis.io/conga/cli/conga-cli.yml
  title: ''
  type: CLI
  url: cli/conga-cli.yml
- group: agent
  href: https://artifacts.apis.io/conga/mcp/conga-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/conga-mcp.yml
- group: build
  href: https://artifacts.apis.io/conga/mcp/conga-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/conga-tool-crosswalk.yml
- group: docs
  href: https://artifacts.apis.io/conga/graphql/conga-graphql.yml
  title: ''
  type: GraphQL
  url: graphql/conga-graphql.yml
- group: design
  href: https://artifacts.apis.io/conga/data-model/conga-data-model.yml
  title: ''
  type: DataModel
  url: data-model/conga-data-model.yml
- group: design
  href: https://artifacts.apis.io/conga/asyncapi/conga-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/conga-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/conga/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/conga/overlays/conga-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/conga-platform-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/conga/plans/conga-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conga-plans-pricing.yml
- group: start
  title: ''
  type: Login
  url: https://login.conga.com/
- group: auth
  title: ''
  type: Security
  url: https://conga.com/vulnerability-disclosure
- group: company
  title: ''
  type: Website
  url: https://www.conga.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.conga.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.conga.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.conga.com/platform/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.conga.com/revenue/docs/user-authentication-to-conga-platform
- group: auth
  href: https://artifacts.apis.io/conga/authentication/conga-authentication.yml
  title: ''
  type: Authentication
  url: authentication/conga-authentication.yml
- group: auth
  href: https://artifacts.apis.io/conga/scopes/conga-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/conga-scopes.yml
- group: design
  href: https://artifacts.apis.io/conga/conventions/conga-conventions.yml
  title: ''
  type: Conventions
  url: conventions/conga-conventions.yml
- group: design
  href: https://artifacts.apis.io/conga/errors/conga-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/conga-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/conga/rate-limits/conga-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/conga-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/conga/lifecycle/conga-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/conga-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conga.com/
- group: operate
  href: https://artifacts.apis.io/conga/changelog/conga-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/conga-changelog.yml
- group: design
  href: https://artifacts.apis.io/conga/conformance/conga-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conga-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://conga.com/trust-compliance-center
- group: auth
  href: https://artifacts.apis.io/conga/security/conga-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/conga-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/conga/security/conga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conga-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/conga/well-known/conga-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/conga-well-known.yml
- group: agent
  href: https://artifacts.apis.io/conga/llms/conga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conga-llms.txt
- group: start
  href: https://artifacts.apis.io/conga/sandbox/conga-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/conga-sandbox.yml
- group: operate
  title: ''
  type: Support
  url: https://conga.com/support
- group: company
  title: ''
  type: Blog
  url: https://conga.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://conga.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conga.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conga.com/privacy
- group: company
  title: ''
  type: Website
  url: https://conga.com/
created: '2026-07-17'
description: 'Conga (formerly Apttus + Conga) is an enterprise Revenue Lifecycle Management vendor whose Conga Advantage Platform unifies Configure-Price-Quote (CPQ), Contract Lifecycle Management (CLM), document generation and e-signature, X-Author authoring, approvals, billing and incentives, and AI-assisted contract intelligence. It is one of the largest documented API surfaces in the catalog: Conga publishes a complete OpenAPI 3.0.1 definition for every operation on its ReadMe-hosted developer portal at developer.conga.com - 2,136 operations across 31 services, captured here in openapi/. The platform is regionally partitioned (NA/EU/AU), secured with OAuth 2.0 bearer tokens minted from region-specific Conga login services that publish OIDC discovery and a real per-service scope set (api.cart, api.catalog, api.quote, api.order, api.user-management, api.revenue-admin, sign, doc-gen.composer and more), and uses JSON bodies, page/limit pagination with Content-Range headers, URI filter functions
  and a JSON:API-style error envelope. Conga also runs two machine surfaces it documents nowhere: a hosted, OAuth-gated MCP server at /mcp on every regional gateway, and a multi-tenant GraphQL API evidenced only by its own first-party npm client @conga-cloud/graphql. Conga is backed by ICONIQ Capital and Insight Partners.'
finops:
- has_sources: true
  method: derived
  name: Conga Finops
  primary_unit: ''
  service_category: ''
  slug: conga-finops
  template: true
image: https://conga.com/sites/default/files/styles/large/public/image/2026-03/Social%20Share%20%281%29%20%281%29.png?itok=uH7gF5iu
layout: provider
mcp_servers:
- description: Conga runs a hosted, remote Model Context Protocol server at /mcp on every regional Conga Advantage Platform gateway. It is undocumented on developer.conga.com and does not appear on conga.com, but it
  name: Conga Advantage Platform MCP Server
  slug: conga-advantage-platform-mcp-server
modified: '2026-09-16'
name: Conga
nav: Providers
network: true
overview: 'Conga publishes 345 API contracts indexed on the [APIs.io](https://apis.io/) network, including 2. Order Actions API, 3. Order Line Items API, Account API, and 342 more. Tagged areas include Company, Enterprise Software, Contract Lifecycle Management, CPQ, and Revenue Lifecycle Management.


  The Conga catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Conga''s developer surface includes CLI, documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 34 more developer resources.'
plans:
- name: Conga Plans Pricing
  plan_count: 0
  slug: conga-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Conga Rate Limits
  slug: conga-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Conga API Rules
  rule_count: 60
  severity_counts:
    error: 40
    hint: 0
    info: 7
    warn: 13
  slug: conga-rules
scopes:
- name: Conga Scopes
  scope_count: 28
  slug: conga-scopes
  summary_line: 28 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 53.9
    contract_governance: 31.8
    contract_quality: 60.9
    developer_ergonomics: 70.8
    discoverability: 80.0
    operational_transparency: 71.1
  previous_composite: 70.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 343
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
    score: 61.1
screenshot: https://apis.io/screenshots/conga/conga-2026-07-25T210254.png
security:
- kind: authentication
  name: Conga Authentication
  slug: conga-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Conga Domain Security
  slug: conga-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Conga Vulnerability Disclosure
  slug: conga-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Conga Trust Center
  slug: conga-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO 27001, ISO 27701, HIPAA, GDPR, CCPA, PCI
skill_count: 6
skills:
- name: conga-authenticate
  slug: conga-authenticate
- name: conga-configure-price-quote
  slug: conga-configure-price-quote
- name: conga-contract-lifecycle
  slug: conga-contract-lifecycle
- name: conga-provision-users
  slug: conga-provision-users
- name: conga-send-for-signature
  slug: conga-send-for-signature
- name: conga-service-hooks
  slug: conga-service-hooks
slug: conga
tags:
- Company
- Enterprise Software
- Contract Lifecycle Management
- CPQ
- Revenue Lifecycle Management
- Document Automation
- E-Signature
- Contract Intelligence
- CRM
- OpenAPI
- MCP
- GraphQL
- Billing
- Approvals
- Contract Management
- Automation
website: https://www.conga.com/
---
