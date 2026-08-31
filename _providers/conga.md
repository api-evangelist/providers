---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-30'
api_count: 31
apis:
- description: A hosted, remote Model Context Protocol server on every regional Conga Advantage Platform gateway. It answers MCP JSON-RPC over Streamable HTTP, rejects anonymous calls with an RFC 6750 bearer challen
  name: Conga Advantage Platform MCP Server
  slug: conga-advantage-platform-mcp-server
- description: A multi-tenant GraphQL API over the Conga Advantage Platform data core, with Relay-style connections, cursor pagination, SOQL-like where predicates and Server-Sent-Event subscriptions. Each tenant get
  name: Conga GraphQL API
  slug: conga-graphql-api
- description: Manages the complete lifecycle of your orders from initial confirmation through activation, modification, and cancellation.
  name: Conga 2. Order Actions API
  slug: conga-2-order-actions-api
- description: Manages order line items represent each product, service, or subscription that a customer has purchased as part of an order.
  name: Conga 3. Order Line Items API
  slug: conga-3-order-line-items-api
- description: The Account API from Conga — 8 operation(s) for account.
  name: Conga Account API
  slug: conga-account-api
- description: The AccountAttachmentsBlacklist API from Conga — 1 operation(s) for accountattachmentsblacklist.
  name: Conga Account Attachments Blacklist API
  slug: conga-accountattachmentsblacklist-api
- description: The AccountAttachmentsWhitelist API from Conga — 1 operation(s) for accountattachmentswhitelist.
  name: Conga Account Attachments Whitelist API
  slug: conga-accountattachmentswhitelist-api
- description: The AccountDesignerSettings API from Conga — 1 operation(s) for accountdesignersettings.
  name: Conga Account Designer Settings API
  slug: conga-accountdesignersettings-api
- description: The AccountEmailReminderSettings API from Conga — 1 operation(s) for accountemailremindersettings.
  name: Conga Account Email Reminder Settings API
  slug: conga-accountemailremindersettings-api
- description: The AccountFeatureSettings API from Conga — 1 operation(s) for accountfeaturesettings.
  name: Conga Account Feature Settings API
  slug: conga-accountfeaturesettings-api
- description: The AccountPackageSettings API from Conga — 1 operation(s) for accountpackagesettings.
  name: Conga Account Package Settings API
  slug: conga-accountpackagesettings-api
- description: The AccountRoles API from Conga — 4 operation(s) for accountroles.
  name: Conga Account Roles API
  slug: conga-accountroles-api
- description: The Accounts API from Conga — 4 operation(s) for accounts.
  name: Conga Accounts API
  slug: conga-accounts-api
- description: The AccountSettings API from Conga — 1 operation(s) for accountsettings.
  name: Conga Account Settings API
  slug: conga-accountsettings-api
- description: The AccountSigningLogos API from Conga — 1 operation(s) for accountsigninglogos.
  name: Conga Account Signing Logos API
  slug: conga-accountsigninglogos-api
- description: The AccountSigningTheme API from Conga — 1 operation(s) for accountsigningtheme.
  name: Conga Account Signing Theme API
  slug: conga-accountsigningtheme-api
- description: The AccountSigningUIOptions API from Conga — 1 operation(s) for accountsigninguioptions.
  name: Conga Account Signing UI Options API
  slug: conga-accountsigninguioptions-api
- description: The AccountSupportedLanguages API from Conga — 1 operation(s) for accountsupportedlanguages.
  name: Conga Account Supported Languages API
  slug: conga-accountsupportedlanguages-api
- description: The AccountSystemSettings API from Conga — 1 operation(s) for accountsystemsettings.
  name: Conga Account System Settings API
  slug: conga-accountsystemsettings-api
- description: The Action Permissions API from Conga — 1 operation(s) for action permissions.
  name: Conga Action Permissions API
  slug: conga-action-permissions-api
- description: The Activities API from Conga — 1 operation(s) for activities.
  name: Conga Activities API
  slug: conga-activities-api
- description: The ActivityHistory API from Conga — 1 operation(s) for activityhistory.
  name: Conga Activity History API
  slug: conga-activityhistory-api
- description: The AdHoc Groups Controller
  name: Conga Ad Hoc Groups API
  slug: conga-adhocgroups-api
- description: The AdhocProcess API from Conga — 5 operation(s) for adhocprocess.
  name: Conga Adhoc Process API
  slug: conga-adhocprocess-api
- description: Adjustments controller
  name: Conga Adjustments API
  slug: conga-adjustments-api
- description: The Admin Permissions API from Conga — 1 operation(s) for admin permissions.
  name: Conga Admin Permissions API
  slug: conga-admin-permissions-api
- description: This class contains API endpoints for admin setting
  name: Conga Admin Settings API
  slug: conga-adminsettings-api
- description: Adobe sign
  name: Conga Adobe Sign API
  slug: conga-adobesign-api
- description: This class contains API endpoints for Agreements
  name: Conga Agreement API
  slug: conga-agreement-api
- description: This class holds APIs related to agreement clauses
  name: Conga Agreement Clause API
  slug: conga-agreementclause-api
- description: This class contains APIs related to agreement documents.
  name: Conga Agreement Document API
  slug: conga-agreementdocument-api
- description: This class contains APIs related to agreement document checkins
  name: Conga Agreement Document Checkin API
  slug: conga-agreementdocumentcheckin-api
- description: This class contains API endpoints for Agreement Document's Lock.
  name: Conga Agreement Lock API
  slug: conga-agreementlock-api
- description: This class contains APIs for agreement metadata.
  name: Conga Agreement Metadata API
  slug: conga-agreementmetadata-api
- description: This class contains APIs related to offline agreements.
  name: Conga Agreement Offline API
  slug: conga-agreementoffline-api
- description: This class contains APIs for Agreement Review Controller.
  name: Conga Agreement Review API
  slug: conga-agreementreview-api
- description: Provides endpoints for managing and retrieving agreement signing cycles.
  name: Conga Agreement Signing Cycle API
  slug: conga-agreementsigningcycle-api
- description: This class contains APIs related to agreement and template related operations.
  name: Conga Agreement Template API
  slug: conga-agreementtemplate-api
- description: This class contains API endpoints for documents AI operation
  name: Conga AI Redline API
  slug: conga-airedline-api
- description: This class contains API endpoints for alternate clauses related operations.
  name: Conga Alternate Clause API
  slug: conga-alternateclause-api
- description: This class holds APIs related to application usage
  name: Conga Analytics API
  slug: conga-analytics-api
- description: The API Connections API from Conga — 3 operation(s) for api connections.
  name: Conga API Connections API
  slug: conga-api-connections-api
- description: The API Resource API from Conga — 7 operation(s) for api resource.
  name: Conga API Resource API
  slug: conga-api-resource-api
- description: The Approval API from Conga — 6 operation(s) for approval.
  name: Conga Approval API
  slug: conga-approval-api
- description: Controller to manage the asset action(s)
  name: Conga Asset Actions API
  slug: conga-assetactions-api
- description: Controller to manage assets
  name: Conga Assets API
  slug: conga-assets-api
- description: The AsyncOperationStatus API from Conga — 1 operation(s) for asyncoperationstatus.
  name: Conga Async Operation Status API
  slug: conga-asyncoperationstatus-api
- description: The Attribute Constraint Rule Entries API from Conga — 4 operation(s) for attribute constraint rule entries.
  name: Conga Attribute Constraint Rule Entries API
  slug: conga-attribute-constraint-rule-entries-api
- description: The Attribute Constraint Rules API from Conga — 2 operation(s) for attribute constraint rules.
  name: Conga Attribute Constraint Rules API
  slug: conga-attribute-constraint-rules-api
- description: The Attribute Group Members API from Conga — 2 operation(s) for attribute group members.
  name: Conga Attribute Group Members API
  slug: conga-attribute-group-members-api
- description: The Attribute Groups API from Conga — 2 operation(s) for attribute groups.
  name: Conga Attribute Groups API
  slug: conga-attribute-groups-api
- description: The Attribute Matrices API from Conga — 2 operation(s) for attribute matrices.
  name: Conga Attribute Matrices API
  slug: conga-attribute-matrices-api
- description: The Attribute Matrix Entries API from Conga — 4 operation(s) for attribute matrix entries.
  name: Conga Attribute Matrix Entries API
  slug: conga-attribute-matrix-entries-api
- description: Controller for managing attributes.
  name: Conga Attributes API
  slug: conga-attributes-api
- description: The AuthenticationTokens API from Conga — 4 operation(s) for authenticationtokens.
  name: Conga Authentication Tokens API
  slug: conga-authenticationtokens-api
- description: This class contains endpoints for authorizing sign providers like Conga Sign, Adobe Sign, or DocuSign, or wet signature.
  name: Conga Authorization API
  slug: conga-authorization-api
- description: The BackupAdmin API from Conga — 1 operation(s) for backupadmin.
  name: Conga Backup Admin API
  slug: conga-backupadmin-api
- description: The BackupDelegates API from Conga — 5 operation(s) for backupdelegates.
  name: Conga Backup Delegates API
  slug: conga-backupdelegates-api
- description: The Bulk Import API from Conga — 5 operation(s) for bulk import.
  name: Conga Bulk Import API
  slug: conga-bulk-import-api
- description: The BundleLineItemStructure API from Conga — 1 operation(s) for bundlelineitemstructure.
  name: Conga Bundle Line Item Structure API
  slug: conga-bundlelineitemstructure-api
- description: The business object controller
  name: Conga Business Object API
  slug: conga-businessobject-api
- description: The BusinessObjects API from Conga — 15 operation(s) for businessobjects.
  name: Conga Business Objects API
  slug: conga-businessobjects-api
- description: The Callback API from Conga — 7 operation(s) for callback.
  name: Conga Callback API
  slug: conga-callback-api
- description: Config Debug Rule Controller
  name: Conga Cart Analyzers API
  slug: conga-cart-analyzers-api
- description: The cart actions controller
  name: Conga Cart Actions API
  slug: conga-cartactions-api
- description: The Cart Item Controller
  name: Conga Cart Items API
  slug: conga-cartitems-api
- description: The Cart Controller
  name: Conga Carts API
  slug: conga-carts-api
- description: The Categories API from Conga — 11 operation(s) for categories.
  name: Conga Categories API
  slug: conga-categories-api
- description: The CDN Store API from Conga — 3 operation(s) for cdn store.
  name: Conga CDN Store API
  slug: conga-cdn-store-api
- description: This class contains API endpoints for clauses.
  name: Conga Clause API
  slug: conga-clause-api
- description: The Clause Obligations API from Conga — 3 operation(s) for clause obligations.
  name: Conga Clause Obligations API
  slug: conga-clause-obligations-api
- description: This class contains API endpoints for clause semantic comparison
  name: Conga Clause Comparison API
  slug: conga-clausecomparison-api
- description: This class contains API endpoints for clause's content.
  name: Conga Clause Content API
  slug: conga-clausecontent-api
- description: This class contains API endpoints for clauses.
  name: Conga Clause Library API
  slug: conga-clauselibrary-api
- description: This class contains API endpoints for template clause metadata
  name: Conga Clause Metadata API
  slug: conga-clausemetadata-api
- description: This class contains API endpoints for clause's version-related operations.
  name: Conga Clause Version API
  slug: conga-clauseversion-api
- description: The Clone API from Conga — 3 operation(s) for clone.
  name: Conga Clone API
  slug: conga-clone-api
- description: The Collaboration Request Controller
  name: Conga Collaboration Request API
  slug: conga-collaborationrequest-api
- description: The Complex Field Definition API from Conga — 3 operation(s) for complex field definition.
  name: Conga Complex Field Definition API
  slug: conga-complex-field-definition-api
- description: The ComposerParameter API from Conga — 2 operation(s) for composerparameter.
  name: Conga Composer Parameter API
  slug: conga-composerparameter-api
- description: The ComprehensiveHealthCheck API from Conga — 1 operation(s) for comprehensivehealthcheck.
  name: Conga Comprehensive Health Check API
  slug: conga-comprehensivehealthcheck-api
- description: The Configuration API from Conga — 10 operation(s) for configuration.
  name: Conga Configuration API
  slug: conga-configuration-api
- description: This class contains APIs related to configuration management
  name: Conga Configuration Management API
  slug: conga-configurationmanagement-api
- description: The Configurations API from Conga — 1 operation(s) for configurations.
  name: Conga Configurations API
  slug: conga-configurations-api
- description: The Conga Hooks API from Conga — 4 operation(s) for conga hooks.
  name: Conga Conga Hooks API
  slug: conga-conga-hooks-api
- description: The Conga Hooks Rules API from Conga — 4 operation(s) for conga hooks rules.
  name: Conga Conga Hooks Rules API
  slug: conga-conga-hooks-rules-api
- description: Send transaction using Conga Sign
  name: Conga Conga Sign API
  slug: conga-congasign-api
- description: The Constraint Rule Actions API from Conga — 5 operation(s) for constraint rule actions.
  name: Conga Constraint Rule Actions API
  slug: conga-constraint-rule-actions-api
- description: The Constraint Rule Conditions API from Conga — 2 operation(s) for constraint rule conditions.
  name: Conga Constraint Rule Conditions API
  slug: conga-constraint-rule-conditions-api
- description: The Constraint Rules API from Conga — 2 operation(s) for constraint rules.
  name: Conga Constraint Rules API
  slug: conga-constraint-rules-api
- description: Controller for CRUD operations on usage inputs, supporting rating, unrating, and draft rating in synchronous and asynchronous modes.
  name: Conga Consumption Billing API
  slug: conga-consumption-billing-api
- description: The Contact API from Conga — 8 operation(s) for contact.
  name: Conga Contact API
  slug: conga-contact-api
- description: The Contact Users API from Conga — 3 operation(s) for contact users.
  name: Conga Contact Users API
  slug: conga-contact-users-api
- description: The Contract API from Conga — 4 operation(s) for contract.
  name: Conga Contract API
  slug: conga-contract-api
- description: The Contract Clause API from Conga — 6 operation(s) for contract clause.
  name: Conga Contract Clause API
  slug: conga-contract-clause-api
- description: The Contract Cycle Time API from Conga — 4 operation(s) for contract cycle time.
  name: Conga Contract Cycle Time API
  slug: conga-contract-cycle-time-api
- description: The Contract Documents API from Conga — 15 operation(s) for contract documents.
  name: Conga Contract Documents API
  slug: conga-contract-documents-api
- description: The Contract Lifecycle API from Conga — 9 operation(s) for contract lifecycle.
  name: Conga Contract Lifecycle API
  slug: conga-contract-lifecycle-api
- description: The Contract Obligations API from Conga — 6 operation(s) for contract obligations.
  name: Conga Contract Obligations API
  slug: conga-contract-obligations-api
- description: The Contract Obligations Fulfillment API from Conga — 6 operation(s) for contract obligations fulfillment.
  name: Conga Contract Obligations Fulfillment API
  slug: conga-contract-obligations-fulfillment-api
- description: The Contract Related List API from Conga — 3 operation(s) for contract related list.
  name: Conga Contract Related List API
  slug: conga-contract-related-list-api
- description: The Contract Relationship API from Conga — 5 operation(s) for contract relationship.
  name: Conga Contract Relationship API
  slug: conga-contract-relationship-api
- description: The Contract Request API from Conga — 7 operation(s) for contract request.
  name: Conga Contract Request API
  slug: conga-contract-request-api
- description: The Contract Request Team Members API from Conga — 4 operation(s) for contract request team members.
  name: Conga Contract Request Team Members API
  slug: conga-contract-request-team-members-api
- description: The Contract Team Members API from Conga — 4 operation(s) for contract team members.
  name: Conga Contract Team Members API
  slug: conga-contract-team-members-api
- description: Controller for managing Contract Type Document Requirement Settings
  name: Conga Contract Type Document Requirement Settings API
  slug: conga-contract-type-document-requirement-settings-api
- description: This class contains APIs related to agreement document checkins
  name: Conga Contract Checkin API
  slug: conga-contractcheckin-api
- description: Provides endpoints for managing conversation threads.
  name: Conga Conversation Thread API
  slug: conga-conversation-thread-api
- description: API controller for managing credit memo operations.
  name: Conga Credit Memos API
  slug: conga-credit-memos-api
- description: The Currency Admin API from Conga — 3 operation(s) for currency admin.
  name: Conga Currency Admin API
  slug: conga-currency-admin-api
- description: The Currency API from Conga — 1 operation(s) for currency.
  name: Conga Currency API
  slug: conga-currency-api
- description: The Currency Format API from Conga — 1 operation(s) for currency format.
  name: Conga Currency Format API
  slug: conga-currency-format-api
- description: The Currency Runtime API from Conga — 3 operation(s) for currency runtime.
  name: Conga Currency Runtime API
  slug: conga-currency-runtime-api
- description: The Custom Code API from Conga — 14 operation(s) for custom code.
  name: Conga Custom Code API
  slug: conga-custom-code-api
- description: The Custom Object API from Conga — 9 operation(s) for custom object.
  name: Conga Custom Object API
  slug: conga-custom-object-api
- description: The CustomPlanTemplate (also called BillingPlanTemplate) Controller
  name: Conga Custom Plan Template API
  slug: conga-custom-plan-template-api
- description: Controller for managing generic custom billing plans. Provides endpoints to create, retrieve, and delete custom plans.
  name: Conga Custom Plans API
  slug: conga-custom-plans-api
- description: The CustomBranding API from Conga — 3 operation(s) for custombranding.
  name: Conga Custom Branding API
  slug: conga-custombranding-api
- description: The CustomerOnboarded API from Conga — 1 operation(s) for customeronboarded.
  name: Conga Customer Onboarded API
  slug: conga-customeronboarded-api
- description: The CustomerRegistration API from Conga — 1 operation(s) for customerregistration.
  name: Conga Customer Registration API
  slug: conga-customerregistration-api
- description: The CustomFields API from Conga — 2 operation(s) for customfields.
  name: Conga Custom Fields API
  slug: conga-customfields-api
- description: The CustomSettings API from Conga — 9 operation(s) for customsettings.
  name: Conga Custom Settings API
  slug: conga-customsettings-api
- description: To do the operation reated to Discovery extraction and checking the status and marking
  name: Conga DAI API
  slug: conga-dai-api
- description: This class contains API endpoints for data correction-related operations.
  name: Conga Data Correction API
  slug: conga-datacorrection-api
- description: The DataManagement API from Conga — 2 operation(s) for datamanagement.
  name: Conga Data Management API
  slug: conga-datamanagement-api
- description: The Deal Color Bands API from Conga — 2 operation(s) for deal color bands.
  name: Conga Deal Color Bands API
  slug: conga-deal-color-bands-api
- description: The Deal Guidance Dimension Set Members API from Conga — 2 operation(s) for deal guidance dimension set members.
  name: Conga Deal Guidance Dimension Set Members API
  slug: conga-deal-guidance-dimension-set-members-api
- description: The Deal Guidance Dimension Sets API from Conga — 2 operation(s) for deal guidance dimension sets.
  name: Conga Deal Guidance Dimension Sets API
  slug: conga-deal-guidance-dimension-sets-api
- description: The Deal Guidance Dimensions API from Conga — 2 operation(s) for deal guidance dimensions.
  name: Conga Deal Guidance Dimensions API
  slug: conga-deal-guidance-dimensions-api
- description: The Deal Guidance Rule Entries API from Conga — 2 operation(s) for deal guidance rule entries.
  name: Conga Deal Guidance Rule Entries API
  slug: conga-deal-guidance-rule-entries-api
- description: The Deal Guidance Rules API from Conga — 2 operation(s) for deal guidance rules.
  name: Conga Deal Guidance Rules API
  slug: conga-deal-guidance-rules-api
- description: The Dependent Picklist Definition API from Conga — 1 operation(s) for dependent picklist definition.
  name: Conga Dependent Picklist Definition API
  slug: conga-dependent-picklist-definition-api
- description: This class contains API endpoints for Document.
  name: Conga Document API
  slug: conga-document-api
- description: The Document Generation API from Conga — 5 operation(s) for document generation.
  name: Conga Document Generation API
  slug: conga-document-generation-api
- description: The Document Settings API from Conga — 7 operation(s) for document settings.
  name: Conga Document Settings API
  slug: conga-document-settings-api
- description: This class contains API endpoints for document metadata.
  name: Conga Document Metadata API
  slug: conga-documentmetadata-api
- description: This class contains API endpoints for Document protection.
  name: Conga Document Protection API
  slug: conga-documentprotection-api
- description: This class contains API endpoints for Document Review.
  name: Conga Document Review API
  slug: conga-documentreview-api
- description: The Documents API from Conga — 38 operation(s) for documents.
  name: Conga Documents API
  slug: conga-documents-api
- description: This class contains API endpoints for Document Transfer Metadata Sync.
  name: Conga Document Sync API
  slug: conga-documentsync-api
- description: The Draft API from Conga — 2 operation(s) for draft.
  name: Conga Draft API
  slug: conga-draft-api
- description: This controller provides access to email operations like sending email in post delivery.
  name: Conga Email API
  slug: conga-email-api
- description: The Email Delivery Status API from Conga — 2 operation(s) for email delivery status.
  name: Conga Email Delivery Status API
  slug: conga-email-delivery-status-api
- description: The Email Profile API from Conga — 2 operation(s) for email profile.
  name: Conga Email Profile API
  slug: conga-email-profile-api
- description: The Email Sender API from Conga — 4 operation(s) for email sender.
  name: Conga Email Sender API
  slug: conga-email-sender-api
- description: The Email Template API from Conga — 8 operation(s) for email template.
  name: Conga Email Template API
  slug: conga-email-template-api
- description: The Email Template Category API from Conga — 2 operation(s) for email template category.
  name: Conga Email Template Category API
  slug: conga-email-template-category-api
- description: Encryption controller which will be used to create all the methods for encrypt/decrypt.
  name: Conga Encryption API
  slug: conga-encryption-api
- description: Export cart data (line items) as CSV.
  name: Conga Export API
  slug: conga-export-api
- description: The External Endpoint Auth Credentials API from Conga — 2 operation(s) for external endpoint auth credentials.
  name: Conga External Endpoint Auth Credentials API
  slug: conga-external-endpoint-auth-credentials-api
- description: The External Endpoint Configuration API from Conga — 3 operation(s) for external endpoint configuration.
  name: Conga External Endpoint Configuration API
  slug: conga-external-endpoint-configuration-api
- description: The ExternalAuthentication API from Conga — 1 operation(s) for externalauthentication.
  name: Conga External Authentication API
  slug: conga-externalauthentication-api
- description: The Favorites API from Conga — 7 operation(s) for favorites.
  name: Conga Favorites API
  slug: conga-favorites-api
- description: The Feature API from Conga — 2 operation(s) for feature.
  name: Conga Feature API
  slug: conga-feature-api
- description: The Feature Sets API from Conga — 4 operation(s) for feature sets.
  name: Conga Feature Sets API
  slug: conga-feature-sets-api
- description: The Features API from Conga — 2 operation(s) for features.
  name: Conga Features API
  slug: conga-features-api
- description: Controller to fetch the feature settings
  name: Conga Feature Settings API
  slug: conga-featuresettings-api
- description: The Field Definition API from Conga — 5 operation(s) for field definition.
  name: Conga Field Definition API
  slug: conga-field-definition-api
- description: The Field Expressions API from Conga — 5 operation(s) for field expressions.
  name: Conga Field Expressions API
  slug: conga-field-expressions-api
- description: The Field History Tracking API from Conga — 1 operation(s) for field history tracking.
  name: Conga Field History Tracking API
  slug: conga-field-history-tracking-api
- description: The Field History Tracking Config API from Conga — 2 operation(s) for field history tracking config.
  name: Conga Field History Tracking Config API
  slug: conga-field-history-tracking-config-api
- description: The Field Permission API from Conga — 3 operation(s) for field permission.
  name: Conga Field Permission API
  slug: conga-field-permission-api
- description: This class contains API endpoints for field's marking-related operations.
  name: Conga Field Data API
  slug: conga-fielddata-api
- description: This class contains API endpoints for retrieving document field data related operations.
  name: Conga Field Data Retrieval API
  slug: conga-fielddataretrieval-api
- description: This class contains API endpoints for field's marking-related operations.
  name: Conga Field Mark API
  slug: conga-fieldmark-api
- description: This class contains API endpoints for the document field's related operations.
  name: Conga Fields API
  slug: conga-fields-api
- description: The FieldSetSettings API from Conga — 2 operation(s) for fieldsetsettings.
  name: Conga Field Set Settings API
  slug: conga-fieldsetsettings-api
- description: This class contains API endpoints for document field validation operations.
  name: Conga Fields Validate API
  slug: conga-fieldsvalidate-api
- description: The File Store API from Conga — 17 operation(s) for file store.
  name: Conga File Store API
  slug: conga-file-store-api
- description: The FileAttachment API from Conga — 7 operation(s) for fileattachment.
  name: Conga File Attachment API
  slug: conga-fileattachment-api
- description: The Forecast Billing API from Conga — 3 operation(s) for forecast billing.
  name: Conga Forecast Billing API
  slug: conga-forecast-billing-api
- description: The Frequency Conversion Admin API from Conga — 3 operation(s) for frequency conversion admin.
  name: Conga Frequency Conversion Admin API
  slug: conga-frequency-conversion-admin-api
- description: The Frequency Conversion Runtime API from Conga — 3 operation(s) for frequency conversion runtime.
  name: Conga Frequency Conversion Runtime API
  slug: conga-frequency-conversion-runtime-api
- description: The GlobalSearch Runtime API from Conga — 1 operation(s) for globalsearch runtime.
  name: Conga GlobalSearch Runtime API
  slug: conga-globalsearch-runtime-api
- description: This class contains API endpoints for google configurations such as google drive enabled and service configuration info
  name: Conga Google Config API
  slug: conga-googleconfig-api
- description: The Grant Login API from Conga — 3 operation(s) for grant login.
  name: Conga Grant Login API
  slug: conga-grant-login-api
- description: The Guest User API from Conga — 4 operation(s) for guest user.
  name: Conga Guest User API
  slug: conga-guest-user-api
- description: The Health Check API from Conga — 2 operation(s) for health check.
  name: Conga Health Check API
  slug: conga-health-check-api
- description: The Hierarchies API from Conga — 4 operation(s) for hierarchies.
  name: Conga Hierarchies API
  slug: conga-hierarchies-api
- description: The IdvEvidenceSummary API from Conga — 3 operation(s) for idvevidencesummary.
  name: Conga Idv Evidence Summary API
  slug: conga-idvevidencesummary-api
- description: The IdvWorkflow API from Conga — 1 operation(s) for idvworkflow.
  name: Conga Idv Workflow API
  slug: conga-idvworkflow-api
- description: The IFWorkflowConfiguration API from Conga — 1 operation(s) for ifworkflowconfiguration.
  name: Conga IF Workflow Configuration API
  slug: conga-ifworkflowconfiguration-api
- description: The ImprintFields API from Conga — 3 operation(s) for imprintfields.
  name: Conga Imprint Fields API
  slug: conga-imprintfields-api
- description: The In-Effect View API from Conga — 3 operation(s) for in-effect view.
  name: Conga In-Effect View API
  slug: conga-in-effect-view-api
- description: The InAppReports API from Conga — 4 operation(s) for inappreports.
  name: Conga In App Reports API
  slug: conga-inappreports-api
- description: The Incentive Conditions API from Conga — 2 operation(s) for incentive conditions.
  name: Conga Incentive Conditions API
  slug: conga-incentive-conditions-api
- description: The Incentive Coupons API from Conga — 3 operation(s) for incentive coupons.
  name: Conga Incentive Coupons API
  slug: conga-incentive-coupons-api
- description: The Incentive Limits API from Conga — 2 operation(s) for incentive limits.
  name: Conga Incentive Limits API
  slug: conga-incentive-limits-api
- description: The Incentive Programs API from Conga — 2 operation(s) for incentive programs.
  name: Conga Incentive Programs API
  slug: conga-incentive-programs-api
- description: The Incentive Rule Entries API from Conga — 2 operation(s) for incentive rule entries.
  name: Conga Incentive Rule Entries API
  slug: conga-incentive-rule-entries-api
- description: The Incentive Rules API from Conga — 2 operation(s) for incentive rules.
  name: Conga Incentive Rules API
  slug: conga-incentive-rules-api
- description: The Incentives API from Conga — 3 operation(s) for incentives.
  name: Conga Incentives API
  slug: conga-incentives-api
- description: The Index Definition API from Conga — 2 operation(s) for index definition.
  name: Conga Index Definition API
  slug: conga-index-definition-api
- description: Controller to handle Billing Schedule related operations
  name: Conga Initiate Billing API
  slug: conga-initiate-billing-api
- description: The IntelligentImport API from Conga — 5 operation(s) for intelligentimport.
  name: Conga Intelligent Import API
  slug: conga-intelligentimport-api
- description: The IntelligentImportRisk API from Conga — 4 operation(s) for intelligentimportrisk.
  name: Conga Intelligent Import Risk API
  slug: conga-intelligentimportrisk-api
- description: Provides endpoints for configuring and managing invoice run requests.
  name: Conga Invoice Configurations API
  slug: conga-invoice-configurations-api
- description: Controller for managing invoice request results. Provides endpoints to retrieve invoice request result information.
  name: Conga Invoice Request Results API
  slug: conga-invoice-request-results-api
- description: API controller for managing invoice operations.
  name: Conga Invoices API
  slug: conga-invoices-api
- description: Handles actions related to workflow jobs
  name: Conga Jobs API
  slug: conga-jobs-api
- description: API to return job status details
  name: Conga Job Status API
  slug: conga-jobstatus-api
- description: The Json API from Conga — 2 operation(s) for json.
  name: Conga JSON API
  slug: conga-json-api
- description: The Layout API from Conga — 2 operation(s) for layout.
  name: Conga Layout API
  slug: conga-layout-api
- description: Catalog APIs for Locations
  name: Conga Locations API
  slug: conga-locations-api
- description: LockController
  name: Conga Lock API
  slug: conga-lock-api
- description: This class contains APIs for application logs.
  name: Conga Log API
  slug: conga-log-api
- description: The Lookup Field Settings API from Conga — 2 operation(s) for lookup field settings.
  name: Conga Lookup Field Settings API
  slug: conga-lookup-field-settings-api
- description: Lookup Field Data Controller
  name: Conga Lookup Field Data API
  slug: conga-lookupfielddata-api
- description: This controller initiates Composer API Merge
  name: Conga Merge API
  slug: conga-merge-api
- description: The Migration API from Conga — 1 operation(s) for migration.
  name: Conga Migration API
  slug: conga-migration-api
- description: The Milestone Schedule API from Conga — 7 operation(s) for milestone schedule.
  name: Conga Milestone Schedule API
  slug: conga-milestone-schedule-api
- description: The Notification API from Conga — 5 operation(s) for notification.
  name: Conga Notification API
  slug: conga-notification-api
- description: The OAuth2 API from Conga — 4 operation(s) for oauth2.
  name: Conga O Auth2 API
  slug: conga-oauth2-api
- description: The Object Definition API from Conga — 6 operation(s) for object definition.
  name: Conga Object Definition API
  slug: conga-object-definition-api
- description: The Object Definition Translation API from Conga — 1 operation(s) for object definition translation.
  name: Conga Object Definition Translation API
  slug: conga-object-definition-translation-api
- description: The Object Metadata API from Conga — 8 operation(s) for object metadata.
  name: Conga Object Metadata API
  slug: conga-object-metadata-api
- description: The Object Permission API from Conga — 6 operation(s) for object permission.
  name: Conga Object Permission API
  slug: conga-object-permission-api
- description: Controller for managing obligations.
  name: Conga Obligations API
  slug: conga-obligations-api
- description: The OneSpanPackage API from Conga — 1 operation(s) for onespanpackage.
  name: Conga One Span Package API
  slug: conga-onespanpackage-api
- description: The OneSpanUrl API from Conga — 1 operation(s) for onespanurl.
  name: Conga One Span URL API
  slug: conga-onespanurl-api
- description: The OpenSearchSyncAudit API from Conga — 1 operation(s) for opensearchsyncaudit.
  name: Conga Open Search Sync Audit API
  slug: conga-opensearchsyncaudit-api
- description: The Opportunity API from Conga — 7 operation(s) for opportunity.
  name: Conga Opportunity API
  slug: conga-opportunity-api
- description: The Option Group Members API from Conga — 2 operation(s) for option group members.
  name: Conga Option Group Members API
  slug: conga-option-group-members-api
- description: The Option Groups API from Conga — 8 operation(s) for option groups.
  name: Conga Option Groups API
  slug: conga-option-groups-api
- description: The Orchestrate API from Conga — 1 operation(s) for orchestrate.
  name: Conga Orchestrate API
  slug: conga-orchestrate-api
- description: The Organization API from Conga — 4 operation(s) for organization.
  name: Conga Organization API
  slug: conga-organization-api
- description: The Organization External Integration API from Conga — 4 operation(s) for organization external integration.
  name: Conga Organization External Integration API
  slug: conga-organization-external-integration-api
- description: The Package API from Conga — 12 operation(s) for package.
  name: Conga Package API
  slug: conga-package-api
- description: The Package Deployment API from Conga — 8 operation(s) for package deployment.
  name: Conga Package Deployment API
  slug: conga-package-deployment-api
- description: This class contains API endpoints for package migration.
  name: Conga Package Migration API
  slug: conga-packagemigration-api
- description: The PasswordPolicy API from Conga — 1 operation(s) for passwordpolicy.
  name: Conga Password Policy API
  slug: conga-passwordpolicy-api
- description: Controller for managing payment terms.
  name: Conga Payment Terms API
  slug: conga-payment-terms-api
- description: The Permission Groups API from Conga — 2 operation(s) for permission groups.
  name: Conga Permission Groups API
  slug: conga-permission-groups-api
- description: The Picklist Definition API from Conga — 6 operation(s) for picklist definition.
  name: Conga Picklist Definition API
  slug: conga-picklist-definition-api
- description: The PlatformComposerFeatureFlag API from Conga — 1 operation(s) for platformcomposerfeatureflag.
  name: Conga Platform Composer Feature Flag API
  slug: conga-platformcomposerfeatureflag-api
- description: Provides API endpoints for managing playbooks associated with a contract. Supports retrieving available playbooks, playbook rules, and matched playbooks based on contract metadata.
  name: Conga Playbook API
  slug: conga-playbook-api
- description: Provides API endpoints for executing playbooks against contract documents and retrieving playbook execution results including clause and document rule outcomes.
  name: Conga Playbook Execution API
  slug: conga-playbookexecution-api
- description: The Billing Preference Controller
  name: Conga Preferences API
  slug: conga-preferences-api
- description: The Preview API from Conga — 1 operation(s) for preview.
  name: Conga Preview API
  slug: conga-preview-api
- description: The Price Dimensions API from Conga — 3 operation(s) for price dimensions.
  name: Conga Price Dimensions API
  slug: conga-price-dimensions-api
- description: The Price Lists API from Conga — 9 operation(s) for price lists.
  name: Conga Price Lists API
  slug: conga-price-lists-api
- description: The Price Matrices API from Conga — 2 operation(s) for price matrices.
  name: Conga Price Matrices API
  slug: conga-price-matrices-api
- description: The Price Matrix Entries API from Conga — 2 operation(s) for price matrix entries.
  name: Conga Price Matrix Entries API
  slug: conga-price-matrix-entries-api
- description: The Price Program Associations API from Conga — 5 operation(s) for price program associations.
  name: Conga Price Program Associations API
  slug: conga-price-program-associations-api
- description: The Price Program Rule Entries API from Conga — 2 operation(s) for price program rule entries.
  name: Conga Price Program Rule Entries API
  slug: conga-price-program-rule-entries-api
- description: The Price Program Rules API from Conga — 2 operation(s) for price program rules.
  name: Conga Price Program Rules API
  slug: conga-price-program-rules-api
- description: The Price Programs API from Conga — 2 operation(s) for price programs.
  name: Conga Price Programs API
  slug: conga-price-programs-api
- description: The Price Rule Entries API from Conga — 2 operation(s) for price rule entries.
  name: Conga Price Rule Entries API
  slug: conga-price-rule-entries-api
- description: The Price Rule Sets API from Conga — 2 operation(s) for price rule sets.
  name: Conga Price Rule Sets API
  slug: conga-price-rule-sets-api
- description: The Price Rules API from Conga — 2 operation(s) for price rules.
  name: Conga Price Rules API
  slug: conga-price-rules-api
- description: The PriceEscalator API from Conga — 2 operation(s) for priceescalator.
  name: Conga Price Escalator API
  slug: conga-priceescalator-api
- description: Catalog APIs for Pricelists
  name: Conga Price Lists API
  slug: conga-pricelists-api
- description: PriceWaterfall controller
  name: Conga Price Waterfall API
  slug: conga-pricewaterfall-api
- description: The Process API from Conga — 15 operation(s) for process.
  name: Conga Process API
  slug: conga-process-api
- description: The ProcessSteps API from Conga — 3 operation(s) for processsteps.
  name: Conga Process Steps API
  slug: conga-processsteps-api
- description: The Product Attribute Groups API from Conga — 2 operation(s) for product attribute groups.
  name: Conga Product Attribute Groups API
  slug: conga-product-attribute-groups-api
- description: The Product Attribute Rule Actions API from Conga — 2 operation(s) for product attribute rule actions.
  name: Conga Product Attribute Rule Actions API
  slug: conga-product-attribute-rule-actions-api
- description: The Product Attribute Rules API from Conga — 2 operation(s) for product attribute rules.
  name: Conga Product Attribute Rules API
  slug: conga-product-attribute-rules-api
- description: The Product Billing Configuration Controller
  name: Conga Product Configurations API
  slug: conga-product-configurations-api
- description: The Product Groups API from Conga — 8 operation(s) for product groups.
  name: Conga Product Groups API
  slug: conga-product-groups-api
- description: The Product Information API from Conga — 2 operation(s) for product information.
  name: Conga Product Information API
  slug: conga-product-information-api
- description: The Product Option Components API from Conga — 2 operation(s) for product option components.
  name: Conga Product Option Components API
  slug: conga-product-option-components-api
- description: The Product Option Prices API from Conga — 2 operation(s) for product option prices.
  name: Conga Product Option Prices API
  slug: conga-product-option-prices-api
- description: The ProductOptionGroups API from Conga — 4 operation(s) for productoptiongroups.
  name: Conga Product Option Groups API
  slug: conga-productoptiongroups-api
- description: The Products API from Conga — 26 operation(s) for products.
  name: Conga Products API
  slug: conga-products-api
- description: The Property Permission API from Conga — 2 operation(s) for property permission.
  name: Conga Property Permission API
  slug: conga-property-permission-api
- description: The Proposal Locations API from Conga — 2 operation(s) for proposal locations.
  name: Conga Proposal Locations API
  slug: conga-proposal-locations-api
- description: This class contains APIs for querying objects
  name: Conga Query API
  slug: conga-query-api
- description: The quote controller
  name: Conga Quote API
  slug: conga-quote-api
- description: The Ramp Line Items Controller
  name: Conga Ramp Line Items API
  slug: conga-ramplineitems-api
- description: The Ramps Controller
  name: Conga Ramps API
  slug: conga-ramps-api
- description: <p> <H3> <strong>⚠️ Deprecated:</strong> Rebate Program APIs have been deprecated from the Rebates-Admin Service.</H3> </p> <p> <H3>Please find these APIs under Incentive Programs here → <a href="/api
  name: Conga Rebate Programs API
  slug: conga-rebate-programs-api
- description: The Rebate Rule Entries API from Conga — 2 operation(s) for rebate rule entries.
  name: Conga Rebate Rule Entries API
  slug: conga-rebate-rule-entries-api
- description: The Rebate Rules API from Conga — 2 operation(s) for rebate rules.
  name: Conga Rebate Rules API
  slug: conga-rebate-rules-api
- description: Controller for handling rebate-related actions in the cart API.
  name: Conga Rebates API
  slug: conga-rebates-api
- description: This class contains API endpoints related to document reconciliation
  name: Conga Reconciliation API
  slug: conga-reconciliation-api
- description: The Record Share API from Conga — 6 operation(s) for record share.
  name: Conga Record Share API
  slug: conga-record-share-api
- description: The Record Type Permission API from Conga — 5 operation(s) for record type permission.
  name: Conga Record Type Permission API
  slug: conga-record-type-permission-api
- description: This class contains APIs for the record type object
  name: Conga Record Type API
  slug: conga-recordtype-api
- description: The RecordType Definition API from Conga — 2 operation(s) for recordtype definition.
  name: Conga RecordType Definition API
  slug: conga-recordtype-definition-api
- description: Provides API endpoints for polling the status of a redline execution. Tracks extraction and redlining progress for rules applied against a contract document.
  name: Conga Redline Execution Status API
  slug: conga-redlineexecutionstatus-api
- description: The Related Incentives API from Conga — 2 operation(s) for related incentives.
  name: Conga Related Incentives API
  slug: conga-related-incentives-api
- description: The Related Price List Items API from Conga — 2 operation(s) for related price list items.
  name: Conga Related Price List Items API
  slug: conga-related-price-list-items-api
- description: The Reminder API from Conga — 1 operation(s) for reminder.
  name: Conga Reminder API
  slug: conga-reminder-api
- description: The Reports API from Conga — 6 operation(s) for reports.
  name: Conga Reports API
  slug: conga-reports-api
- description: The Requests API from Conga — 27 operation(s) for requests.
  name: Conga Requests API
  slug: conga-requests-api
- description: ResponseFieldConfigurationController
  name: Conga Response Field Configuration API
  slug: conga-responsefieldconfiguration-api
- description: The Review API from Conga — 12 operation(s) for review.
  name: Conga Review API
  slug: conga-review-api
- description: Conga Reviewer APIs
  name: Conga Reviewer API
  slug: conga-reviewer-api
- description: Review Site APIs
  name: Conga Review Sites API
  slug: conga-reviewsites-api
- description: The Role Admin API from Conga — 7 operation(s) for role admin.
  name: Conga Role Admin API
  slug: conga-role-admin-api
- description: The Role API from Conga — 6 operation(s) for role.
  name: Conga Role API
  slug: conga-role-api
- description: The RolesVerification API from Conga — 2 operation(s) for rolesverification.
  name: Conga Roles Verification API
  slug: conga-rolesverification-api
- description: The RuleDimensions API from Conga — 2 operation(s) for ruledimensions.
  name: Conga Rule Dimensions API
  slug: conga-ruledimensions-api
- description: The RuleEntries API from Conga — 4 operation(s) for ruleentries.
  name: Conga Rule Entries API
  slug: conga-ruleentries-api
- description: Provides API endpoints for executing individual playbook rules against contract documents and retrieving clause-level and document-level rule execution results.
  name: Conga Rule Execution API
  slug: conga-ruleexecution-api
- description: The Rules API from Conga — 10 operation(s) for rules.
  name: Conga Rules API
  slug: conga-rules-api
- description: This controller provides access to information inside a customer's salesforce account.
  name: Conga Salesforce API
  slug: conga-salesforce-api
- description: The Scheduler API from Conga — 11 operation(s) for scheduler.
  name: Conga Scheduler API
  slug: conga-scheduler-api
- description: This class contains APIs for Schema metadata.
  name: Conga Schema Metadata API
  slug: conga-schemametadata-api
- description: The Search Admin API from Conga — 10 operation(s) for search admin.
  name: Conga Search Admin API
  slug: conga-search-admin-api
- description: The Search Runtime API from Conga — 6 operation(s) for search runtime.
  name: Conga Search Runtime API
  slug: conga-search-runtime-api
- description: The SearchFilters API from Conga — 5 operation(s) for searchfilters.
  name: Conga Search Filters API
  slug: conga-searchfilters-api
- description: The Sender API from Conga — 6 operation(s) for sender.
  name: Conga Sender API
  slug: conga-sender-api
- description: Catalog APIs to search service products
  name: Conga Services API
  slug: conga-services-api
- description: The Session API from Conga — 1 operation(s) for session.
  name: Conga Session API
  slug: conga-session-api
- description: The Settings API from Conga — 2 operation(s) for settings.
  name: Conga Settings API
  slug: conga-settings-api
- description: sign APIs
  name: Conga Sign API
  slug: conga-sign-api
- description: The SignatureImage API from Conga — 1 operation(s) for signatureimage.
  name: Conga Signature Image API
  slug: conga-signatureimage-api
- description: The SignatureLayout API from Conga — 1 operation(s) for signaturelayout.
  name: Conga Signature Layout API
  slug: conga-signaturelayout-api
- description: Search APIs to search product details
  name: Conga Smart Search API
  slug: conga-smartsearch-api
- description: The Solution API from Conga — 5 operation(s) for solution.
  name: Conga Solution API
  slug: conga-solution-api
- description: Provides endpoints for managing invoice split criteria setups, including creation, activation, and deactivation.
  name: Conga Split Criteria API
  slug: conga-split-criteria-api
- description: Get merge process status
  name: Conga Status API
  slug: conga-status-api
- description: The Storefronts API from Conga — 3 operation(s) for storefronts.
  name: Conga Storefronts API
  slug: conga-storefronts-api
- description: The SubAccounts API from Conga — 4 operation(s) for subaccounts.
  name: Conga Sub Accounts API
  slug: conga-subaccounts-api
- description: The Summary Groups Controller
  name: Conga Summary Groups API
  slug: conga-summarygroups-api
- description: The SystemProperties API from Conga — 5 operation(s) for systemproperties.
  name: Conga System Properties API
  slug: conga-systemproperties-api
- description: TaxCodes Controller
  name: Conga Tax Codes API
  slug: conga-tax-codes-api
- description: The Team Role API from Conga — 3 operation(s) for team role.
  name: Conga Team Role API
  slug: conga-team-role-api
- description: Controller for Templates APIs
  name: Conga Template API
  slug: conga-template-api
- description: This class contains API endpoints for template migration.
  name: Conga Template Migrate API
  slug: conga-templatemigrate-api
- description: The Timezone and Locale API from Conga — 9 operation(s) for timezone and locale.
  name: Conga Timezone and Locale API
  slug: conga-timezone-and-locale-api
- description: The Token API from Conga — 3 operation(s) for token.
  name: Conga Token API
  slug: conga-token-api
- description: The Translation Audit History Tracking API from Conga — 1 operation(s) for translation audit history tracking.
  name: Conga Translation Audit History Tracking API
  slug: conga-translation-audit-history-tracking-api
- description: The Translation Management Runtime API from Conga — 1 operation(s) for translation management runtime.
  name: Conga Translation Management Runtime API
  slug: conga-translation-management-runtime-api
- description: The Translation Runtime API from Conga — 5 operation(s) for translation runtime.
  name: Conga Translation Runtime API
  slug: conga-translation-runtime-api
- description: The Translations Management Admin API from Conga — 11 operation(s) for translations management admin.
  name: Conga Translations Management Admin API
  slug: conga-translations-management-admin-api
- description: The TypeAhead API from Conga — 1 operation(s) for typeahead.
  name: Conga Type Ahead API
  slug: conga-typeahead-api
- description: The UFC API from Conga — 2 operation(s) for ufc.
  name: Conga UFC API
  slug: conga-ufc-api
- description: The UOM Conversion Admin API from Conga — 3 operation(s) for uom conversion admin.
  name: Conga UOM Conversion Admin API
  slug: conga-uom-conversion-admin-api
- description: The UOM Conversion Runtime API from Conga — 3 operation(s) for uom conversion runtime.
  name: Conga UOM Conversion Runtime API
  slug: conga-uom-conversion-runtime-api
- description: Usage Tiers Controller
  name: Conga Usage Tiers API
  slug: conga-usagetiers-api
- description: The User Admin API from Conga — 15 operation(s) for user admin.
  name: Conga User Admin API
  slug: conga-user-admin-api
- description: User Search APIs
  name: Conga User API
  slug: conga-user-api
- description: The User Group API from Conga — 3 operation(s) for user group.
  name: Conga User Group API
  slug: conga-user-group-api
- description: The User Group Member API from Conga — 5 operation(s) for user group member.
  name: Conga User Group Member API
  slug: conga-user-group-member-api
- description: The UserDashboard API from Conga — 4 operation(s) for userdashboard.
  name: Conga User Dashboard API
  slug: conga-userdashboard-api
- description: The UserGroup API from Conga — 4 operation(s) for usergroup.
  name: Conga User Group API
  slug: conga-usergroup-api
- description: The Validation API from Conga — 2 operation(s) for validation.
  name: Conga Validation API
  slug: conga-validation-api
- description: The VirtualRoom API from Conga — 5 operation(s) for virtualroom.
  name: Conga Virtual Room API
  slug: conga-virtualroom-api
- description: The Visibility Rules API from Conga — 2 operation(s) for visibility rules.
  name: Conga Visibility Rules API
  slug: conga-visibility-rules-api
- description: The Waterfall Charts API from Conga — 2 operation(s) for waterfall charts.
  name: Conga Waterfall Charts API
  slug: conga-waterfall-charts-api
- description: The Waterfall Rules API from Conga — 2 operation(s) for waterfall rules.
  name: Conga Waterfall Rules API
  slug: conga-waterfall-rules-api
- description: The WaterfallRuleEntry API from Conga — 2 operation(s) for waterfallruleentry.
  name: Conga Waterfall Rule Entry API
  slug: conga-waterfallruleentry-api
- description: The WaterfallRuleset API from Conga — 2 operation(s) for waterfallruleset.
  name: Conga Waterfall Ruleset API
  slug: conga-waterfallruleset-api
- description: The Waterfalls API from Conga — 2 operation(s) for waterfalls.
  name: Conga Waterfalls API
  slug: conga-waterfalls-api
artifact_total: 357
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
  title: ''
  type: CapabilityMap
  url: capabilities/conga-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conga-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/conga-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/conga-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/conga-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/conga-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/conga-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/conga-graphql.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conga-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/conga-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/conga-platform-overlay.yaml
- group: commercial
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
  title: ''
  type: Authentication
  url: authentication/conga-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/conga-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conga-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conga-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conga-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conga-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conga.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conga-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conga-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://conga.com/trust-compliance-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/conga-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conga-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/conga-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conga-llms.txt
- group: start
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
created: '2026-07-17'
description: 'Conga (formerly Apttus + Conga) is an enterprise Revenue Lifecycle Management vendor whose Conga Advantage Platform unifies Configure-Price-Quote (CPQ), Contract Lifecycle Management (CLM), document generation and e-signature, X-Author authoring, approvals, billing and incentives, and AI-assisted contract intelligence. It is one of the largest documented API surfaces in the catalog: Conga publishes a complete OpenAPI 3.0.1 definition for every operation on its ReadMe-hosted developer portal at developer.conga.com - 2,136 operations across 31 services, captured here in openapi/. The platform is regionally partitioned (NA/EU/AU), secured with OAuth 2.0 bearer tokens minted from region-specific Conga login services that publish OIDC discovery and a real per-service scope set (api.cart, api.catalog, api.quote, api.order, api.user-management, api.revenue-admin, sign, doc-gen.composer and more), and uses JSON bodies, page/limit pagination with Content-Range headers, URI filter functions
  and a JSON:API-style error envelope. Conga also runs two machine surfaces it documents nowhere: a hosted, OAuth-gated MCP server at /mcp on every regional gateway, and a multi-tenant GraphQL API evidenced only by its own first-party npm client @conga-cloud/graphql. Conga is backed by ICONIQ Capital and Insight Partners.'
image: https://conga.com/sites/default/files/styles/large/public/image/2026-03/Social%20Share%20%281%29%20%281%29.png?itok=uH7gF5iu
layout: provider
mcp_servers:
- description: Conga runs a hosted, remote Model Context Protocol server at /mcp on every regional Conga Advantage Platform gateway. It is undocumented on developer.conga.com and does not appear on conga.com, but it
  name: Conga Advantage Platform MCP Server
  slug: conga-advantage-platform-mcp-server
modified: '2026-08-13'
name: Conga
nav: Providers
network: true
overview: 'Conga publishes 345 APIs on the [APIs.io](https://apis.io/) network, including 2. Order Actions API, 3. Order Line Items API, Account API, and 342 more. Tagged areas include Company, Enterprise Software, Contract Lifecycle Management, CPQ, and Revenue Lifecycle Management.


  The Conga catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Conga''s developer surface includes CLI, documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 33 more developer resources.'
plans:
- name: Conga Plans Pricing
  plan_count: 0
  slug: conga-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Conga Rate Limits
  slug: conga-rate-limits
scopes:
- name: Conga Scopes
  scope_count: 28
  slug: conga-scopes
  summary_line: 28 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 26
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.9
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 65.2
    developer_ergonomics: 66.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 59.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conga/refs/heads/main/screenshots/conga-2026-07-25T210254.png
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
  summary_line: disclosure policy published
- kind: trust-center
  name: Conga Trust Center
  slug: conga-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO 27001, ISO 27701, HIPAA, GDPR, CCPA, PCI
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
website: https://www.conga.com/
---
