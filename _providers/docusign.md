---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 275
  human_in_the_loop: 7
  name: Docusign Agentic Access
  operation_count: 505
  slug: docusign-agentic-access
  summary_line: 505 operations · 275 acting · 7 human-in-the-loop
api_count: 8
apis:
- description: The Docusign Web Forms API facilitates generating semantic HTML forms around everyday contracts. It enables developers to embed and prefill forms from the systems they control, creating web form confi
  name: Docusign Web Forms API
  slug: docusign-web-forms-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: The Docusign Notary API enables developers to manage remote online notary tasks programmatically. It provides capabilities for sending signature requests to notary groups, managing notary on-demand se
  name: Docusign Notary API
  slug: docusign-notary-api
- description: The Docusign Navigator API offers developers access to AI-extracted data from the Navigator smart agreement repository. It provides capabilities to analyze existing agreements, extract insights, and c
  name: Docusign Navigator API
  slug: docusign-navigator-api
- description: The Docusign CLM API enables developers to integrate contract lifecycle management workflow, document generation, and document management into Salesforce and custom applications. It provides access to
  name: Docusign CLM API
  slug: docusign-clm-api
- description: The Docusign Connected Fields API enables developers to validate envelope field data programmatically. It allows integration with extension apps to verify custom data in real-time within eSignature ag
  name: Docusign Connected Fields API
  slug: docusign-connected-fields-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AcccountBrands resource provides methods that allow you to create and delete the account brand associated with an account. Branding allows you to add the look and feel of your organization's brand
  name: Docusign AccountBrands API
  phrasing_intents:
  - id: Brands_GetBrands
    intent: List brand profiles
    question: Which brand profiles are set up on my account?
  - id: Brands_PostBrands
    intent: Create a brand profile
    question: How do I create a new brand profile with my company name and colors?
  - id: Brands_DeleteBrands
    intent: Delete several brand profiles at once
    question: How do I remove multiple brand profiles in one request?
  - id: Brand_GetBrand
    intent: Get one brand profile
    question: What colors, logos and landing pages does a specific brand use?
  - id: Brand_PutBrand
    intent: Update a brand profile
    question: How do I rename an existing brand or change its colors?
  - id: Brand_DeleteBrand
    intent: Delete one brand profile
    question: How do I delete a single brand by its ID?
  - id: BrandExport_GetBrandExportFile
    intent: Export a brand to a file
    question: Can I export a brand's configuration as a file?
  - id: BrandLogo_GetBrandLogo
    intent: Get a brand logo image
    question: How do I download the primary or email logo of a brand?
  phrasing_ops: 13
  slug: docusign-accountbrands-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AccountConsumerDisclosures resource provides methods that allow you to retrieve the consumer disclosures associated with the account.
  name: Docusign AccountConsumerDisclosures API
  phrasing_intents:
  - id: ConsumerDisclosure_GetConsumerDisclosure
    intent: Get the account's e-signature disclosure
    question: What does my account's Electronic Record and Signature Disclosure say?
  - id: ConsumerDisclosure_GetConsumerDisclosureLangCode
    intent: Get the disclosure for a specific language
    question: How do I fetch the Spanish version of our signing disclosure?
  - id: ConsumerDisclosure_PutConsumerDisclosure
    intent: Edit the e-signature disclosure for a language
    question: Can I customize the company name and withdrawal instructions in our disclosure?
  phrasing_ops: 3
  slug: docusign-accountconsumerdisclosures-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The CustomFields resource provides a method that enables you to retrieve the custom fields associated with an account. These fields can be used with your account's envelopes to record information abou
  name: Docusign AccountCustomFields API
  phrasing_intents:
  - id: AccountCustomFields_GetAccountCustomFields
    intent: List account-level envelope custom fields
    question: What envelope custom fields are defined for my account?
  - id: AccountCustomFields_PostAccountCustomFields
    intent: Create an account custom field
    question: How do I add a new custom field that all envelopes in my account can use?
  - id: AccountCustomFields_PutAccountCustomFields
    intent: Update an account custom field
    question: How do I change the options on an existing account custom field?
  - id: AccountCustomFields_DeleteAccountCustomFields
    intent: Delete an account custom field
    question: How do I remove an account-wide custom field?
  phrasing_ops: 4
  slug: docusign-accountcustomfields-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AccountPasswordRules resource provides methods that allow you to obtain and update account password rules, as well as membership and account rules.
  name: Docusign AccountPasswordRules API
  phrasing_intents:
  - id: AccountPasswordRules_GetAccountPasswordRules
    intent: Get an account's password rules
    question: What password policy is set for my account, like minimum length and expiry?
  - id: AccountPasswordRules_PutAccountPasswordRules
    intent: Update an account's password rules
    question: Can I require passwords to include digits or special characters?
  - id: PasswordRules_GetPasswordRules
    intent: Get password rules for my membership account
    question: What password requirements apply to me as the current user?
  phrasing_ops: 3
  slug: docusign-accountpasswordrules-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AccountPermissionProfiles resource provides methods that allow you to manage permission profiles.
  name: Docusign AccountPermissionProfiles API
  phrasing_intents:
  - id: PermissionProfiles_GetPermissionProfiles
    intent: List permission profiles
    question: What permission profiles exist on my account?
  - id: PermissionProfiles_PostPermissionProfiles
    intent: Create a permission profile
    question: How do I create a new set of user permissions I can assign to people?
  - id: PermissionProfiles_GetPermissionProfile
    intent: Get one permission profile
    question: What settings does a specific permission profile grant?
  - id: PermissionProfiles_PutPermissionProfiles
    intent: Update a permission profile
    question: How do I rename an existing permission profile?
  - id: PermissionProfiles_DeletePermissionProfiles
    intent: Delete a permission profile
    question: What happens to users when I delete their permission profile?
  phrasing_ops: 5
  slug: docusign-accountpermissionprofiles-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Accounts resource provides methods that allow you to create, delete, and manage your accounts.
  name: Docusign Accounts API
  phrasing_intents:
  - id: Accounts_PostAccounts
    intent: Create one or more new eSignature accounts
    question: How do I programmatically create a new DocuSign account for a customer?
  - id: Accounts_GetAccount
    intent: Get an account's information
    question: Where can I see the basic details of my eSignature account?
  - id: Accounts_DeleteAccount
    intent: Close an account
    question: What happens when I close my eSignature account?
  - id: BillingCharges_GetAccountBillingCharges
    intent: List recurring and usage charges for an account
    question: What recurring and usage charges are on my account?
  - id: CaptiveRecipients_DeleteCaptiveRecipientsPart
    intent: Reset signatures for captive recipients
    question: Can I reset the saved signature for an embedded signer during testing?
  - id: RecipientNames_GetRecipientNames
    intent: Find recipient names linked to an email
    question: Which recipient names are tied to a particular email address in my account?
  - id: Settings_GetSettings
    intent: Get account-wide settings
    question: What account-level settings are currently enabled for us?
  - id: Settings_PutSettings
    intent: Update account-wide settings
    question: Can I change account-level settings through the API?
  phrasing_ops: 14
  slug: docusign-accounts-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AccountSealProviders API from Docusign — 1 operation(s) for accountsealproviders.
  name: Docusign AccountSealProviders API
  phrasing_intents:
  - id: AccountSignatureProviders_GetSealProviders
    intent: List the electronic seals available to an account
    question: Which electronic seal providers are available on my account?
  phrasing_ops: 1
  slug: docusign-accountsealproviders-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods and objects to get account information.
  name: Docusign AccountSettingsExport API
  phrasing_intents:
  - id: OrganizationExport_OrganizationExport_GetAccountCompare
    intent: List account settings export requests
    question: What account settings exports are pending or finished in my organization?
  - id: OrganizationExport_OrganizationExport_AccountCompare
    intent: Request an account settings export
    question: How do I export and compare settings across several accounts in my organization?
  - id: OrganizationExport_OrganizationExport_GetAccountSettingsExportByExportId
    intent: Get an account settings export's results
    question: How do I get the results of an account settings export?
  - id: OrganizationExport_OrganizationExport_DeleteByAccountSettingsExportId
    intent: Delete an account settings export
    question: Can I delete an old settings export and its data?
  phrasing_ops: 4
  slug: docusign-accountsettingsexport-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods and objects to update account settings.
  name: Docusign AccountSettingsImport API
  phrasing_intents:
  - id: OrganizationImport_OrganizationImportAccountSettings_Get
    intent: List bulk account settings imports
    question: What bulk account settings imports has my organization run?
  - id: OrganizationImport_OrganizationImportAccountSettings_Post
    intent: Start a bulk account settings import
    question: How do I apply account settings to many accounts from a CSV file?
  - id: OrganizationImport_OrganizationImportAccountSettings_GetById
    intent: Get results of one settings import
    question: Did my account settings import succeed?
  - id: OrganizationImport_OrganizationImportAccountSettings_DeleteById
    intent: Delete an account settings import request
    question: Can I delete an old settings import and its data?
  phrasing_ops: 4
  slug: docusign-accountsettingsimport-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: This resource provides information on the Standards Based Signature providers that have been provisioned for this account.
  name: Docusign AccountSignatureProviders API
  phrasing_intents:
  - id: AccountSignatureProviders_GetSignatureProviders
    intent: List signature providers available to an account
    question: Which standards-based signature providers can my account use?
  phrasing_ops: 1
  slug: docusign-accountsignatureproviders-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AccountTabSettings resource provides methods that allow you to manage tab settings for an account.
  name: Docusign AccountTabSettings API
  phrasing_intents:
  - id: TabSettings_GetTabSettings
    intent: Get the account's tab settings
    question: Which tab types and features are enabled on my account?
  - id: TabSettings_PutSettings
    intent: Change the account's tab settings
    question: How do I enable calculated fields or checkbox tabs on my account?
  phrasing_ops: 2
  slug: docusign-accounttabsettings-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The AccountWatermarks resource provides methods that allow you to obtain, preview and update watermark information.
  name: Docusign AccountWatermarks API
  phrasing_intents:
  - id: Watermark_GetWatermark
    intent: Get the account watermark settings
    question: What watermark is applied to our documents right now?
  - id: Watermark_PutWatermark
    intent: Change the account watermark
    question: How do I change the watermark text or font on our documents?
  - id: WatermarkPreview_PutWatermarkPreview
    intent: Preview a watermark before saving it
    question: Can I see what a watermark looks like before applying it?
  phrasing_ops: 3
  slug: docusign-accountwatermarks-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: '**Note:** This information is provided for legacy reference only. Please see our supported forms of authentication referenced below and use our [REST API Authentication Guides](https://developers.docu'
  name: Docusign Authentication API
  phrasing_intents:
  - id: LoginInformation_GetLoginInformation
    intent: Get the accounts the signed-in user can access
    question: Which accounts does my authenticated user have access to?
  - id: LoginInformation_PutLoginInformation
    intent: Change a user's password
    question: Can I change my password through the API?
  - id: OAuth2_PostRevoke
    intent: Revoke a legacy OAuth token
    question: Can I revoke an access token with the older deprecated OAuth endpoint?
  - id: OAuth2_PostToken
    intent: Create a legacy OAuth token
    question: Can I still get an access token from the deprecated OAuth token endpoint?
  phrasing_ops: 4
  slug: docusign-authentication-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The ChunkedUploads resource provides methods to complete integrity checks, and to add, commit, retrieve, initiate and delete chunked uploads.
  name: Docusign ChunkedUploads API
  phrasing_intents:
  - id: ChunkedUploads_PostChunkedUploads
    intent: Start a chunked upload
    question: How do I upload a document too large to send in one request?
  - id: ChunkedUploads_GetChunkedUpload
    intent: Get a chunked upload's metadata
    question: How can I check which parts of a chunked upload have arrived?
  - id: ChunkedUploads_PutChunkedUploads
    intent: Commit a chunked upload
    question: How do I finalize a chunked upload so I can use it in an envelope?
  - id: ChunkedUploads_DeleteChunkedUpload
    intent: Delete a chunked upload
    question: Can I discard a chunked upload I no longer need?
  - id: ChunkedUploads_PutChunkedUploadPart
    intent: Add a part to a chunked upload
    question: How do I add the next chunk to an in-progress upload?
  phrasing_ops: 5
  slug: docusign-chunkeduploads-api
- baseURL: https://www.docusign.net/clickapi
  baseurl_source: declared
  description: The ClickWraps API from Docusign — 12 operation(s) for clickwraps.
  name: Docusign ClickWraps API
  phrasing_intents:
  - id: ServiceInformation_GetServiceInformation
    intent: Check the Click API version and build
    question: Which version of the DocuSign Click API is currently running?
  - id: Clickwraps_GetClickwraps
    intent: List the clickwraps in an account
    question: What clickwraps exist in my account right now?
  - id: Clickwraps_PostClickwrap
    intent: Create a new clickwrap agreement
    question: How do I create a clickwrap terms-of-service agreement for my website?
  - id: Clickwraps_DeleteClickwraps
    intent: Bulk delete clickwraps in an account
    question: Can I delete several clickwraps at once by listing their IDs?
  - id: Clickwraps_GetClickwrap
    intent: Get a single clickwrap's details
    question: How can I look up the settings of one particular clickwrap?
  - id: Clickwraps_PutClickwrap
    intent: Transfer a clickwrap to a different owner
    question: Can I hand ownership of a clickwrap from one user to another?
  - id: Clickwraps_DeleteClickwrap
    intent: Delete one clickwrap and all its versions
    question: Can I delete a clickwrap that is still active?
  - id: UserAgreements_PostHasAgreed
    intent: Check whether a user agreed to a clickwrap
    question: How do I find out if a site visitor has already accepted my clickwrap?
  phrasing_ops: 21
  slug: docusign-clickwraps-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The ClosingStatuses API from Docusign — 1 operation(s) for closingstatuses.
  name: Docusign ClosingStatuses API
  phrasing_intents:
  - id: ClosingStatuses_GetClosingStatuses
    intent: List room closing statuses
    question: What are the valid reasons for closing a room?
  phrasing_ops: 1
  slug: docusign-closingstatuses-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: 'The CloudStorageProviders resource provides methods that allow you to manage the cloud storage providers associate with an account. The following providers are supported: * Google Drive * Dropbox * Bo'
  name: Docusign CloudStorageProviders API
  phrasing_intents:
  - id: CloudStorage_GetCloudStorageProviders
    intent: List a user's cloud storage connections
    question: Which cloud storage providers are enabled for my account and connected for a user?
  - id: CloudStorage_PostCloudStorage
    intent: Set redirect URLs for cloud storage providers
    question: Can I configure the return redirect URL for a user's cloud storage login?
  - id: CloudStorage_DeleteCloudStorageProviders
    intent: Disconnect a user from several storage providers
    question: Can I clear a user's saved logins for multiple cloud storage providers at once?
  - id: CloudStorage_GetCloudStorage
    intent: Get one cloud storage provider config for a user
    question: Is a particular cloud storage service connected for a user?
  - id: CloudStorage_DeleteCloudStorage
    intent: Disconnect a user from one storage provider
    question: Can I remove a user's login for just one cloud storage service?
  phrasing_ops: 5
  slug: docusign-cloudstorageproviders-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Comments API from Docusign — 1 operation(s) for comments.
  name: Docusign Comments API
  phrasing_intents:
  - id: Comments_GetCommentsTranscript
    intent: Download an envelope's comments transcript
    question: How do I get a transcript of all comments on an envelope?
  phrasing_ops: 1
  slug: docusign-comments-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The ConnectConfigurations resource methods enable you to configure the DocuSign Connect service associated with an account.
  name: Docusign ConnectConfigurations API
  phrasing_intents:
  - id: Connect_GetConnectConfigs
    intent: List Connect webhook configurations
    question: Which Connect webhook configurations are set up on my account?
  - id: Connect_PutConnectConfiguration
    intent: Update a Connect webhook configuration
    question: How do I change the URL an existing Connect configuration publishes to?
  - id: Connect_PostConnectConfiguration
    intent: Create a Connect webhook configuration
    question: How do I get real-time envelope status updates pushed to my server?
  - id: Connect_GetConnectConfig
    intent: Get one Connect configuration
    question: What events and URL does a specific Connect configuration use?
  - id: Connect_DeleteConnectConfig
    intent: Delete a Connect configuration
    question: How do I stop a Connect listener from sending updates permanently?
  - id: Connect_GetConnectUsers
    intent: List users covered by a Connect configuration
    question: Which users are included in a Connect configuration?
  phrasing_ops: 6
  slug: docusign-connectconfigurations-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The ConnectEvents resource provides methods that allow you to read, delete, and republish the connect logs associated with an envelope.
  name: Docusign ConnectEvents API
  phrasing_intents:
  - id: ConnectPublish_PutConnectRetryByEnvelope
    intent: Republish Connect events for one envelope
    question: Can I resend the Connect webhook for a single envelope?
  - id: ConnectPublish_PutConnectRetry
    intent: Republish Connect events for many envelopes
    question: Is there a way to republish Connect failures for a batch of envelopes?
  - id: ConnectFailures_GetConnectLogs
    intent: List Connect delivery failures
    question: Which envelopes failed to post to my Connect listener?
  - id: ConnectFailures_DeleteConnectFailureLog
    intent: Delete a Connect failure log entry
    question: Can I clear a single entry from the Connect failure log?
  - id: ConnectLog_GetConnectLogs
    intent: List Connect log entries
    question: Where can I review the Connect log entries for my account?
  - id: ConnectLog_DeleteConnectLogs
    intent: Clear the entire Connect log
    question: Can I wipe all Connect log entries for my account at once?
  - id: ConnectLog_GetConnectLog
    intent: Get one Connect log entry
    question: How do I inspect a single Connect log entry in detail?
  - id: ConnectLog_DeleteConnectLog
    intent: Delete one Connect log entry
    question: Can I delete just one entry from the Connect log?
  phrasing_ops: 8
  slug: docusign-connectevents-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The ConnectSecret API from Docusign — 2 operation(s) for connectsecret.
  name: Docusign ConnectSecret API
  phrasing_intents:
  - id: ConnectHMAC_CreateConnectSecret
    intent: Generate a Connect HMAC secret
    question: How do I create an HMAC key to verify Connect webhook messages?
  - id: ConnectHMAC_DeleteConnectSecret
    intent: Delete a Connect HMAC secret
    question: Can I revoke an old Connect HMAC key?
  phrasing_ops: 2
  slug: docusign-connectsecret-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Contacts resource provides methods that allow you to manage contacts.
  name: Docusign Contacts API
  phrasing_intents:
  - id: Contacts_PutContacts
    intent: Replace contacts in the address book
    question: How do I update existing contacts in my address book?
  - id: Contacts_PostContacts
    intent: Import new contacts
    question: How do I add new contacts to my address book?
  - id: Contacts_DeleteContacts
    intent: Delete several contacts
    question: How do I remove a batch of contacts from my address book?
  - id: Contacts_GetContactById
    intent: Get a single contact
    question: What details are stored for a particular contact?
  - id: Contacts_DeleteContactWithId
    intent: Delete a single contact
    question: How do I delete one contact by its ID?
  phrasing_ops: 5
  slug: docusign-contacts-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The ContactSides API from Docusign — 1 operation(s) for contactsides.
  name: Docusign ContactSides API
  phrasing_intents:
  - id: ContactSides_GetContactSides
    intent: List valid transaction contact sides
    question: What contact side values can I use on a Rooms transaction contact?
  phrasing_ops: 1
  slug: docusign-contactsides-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The Countries API from Docusign — 1 operation(s) for countries.
  name: Docusign Countries API
  phrasing_intents:
  - id: Countries_GetCountries
    intent: List supported countries
    question: Which countries can I create an office in?
  phrasing_ops: 1
  slug: docusign-countries-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The Currencies API from Docusign — 1 operation(s) for currencies.
  name: Docusign Currencies API
  phrasing_intents:
  - id: Currencies_GetCurrencies
    intent: List valid currencies for listings and offers
    question: Which currencies can I use for listing, offer and loan amounts?
  phrasing_ops: 1
  slug: docusign-currencies-api
- baseURL: https://lens.docusign.net
  baseurl_source: declared
  description: The DataSet resource provides methods that allow you to fetch organization event data. The `dataSet` path parameter must be set to `monitor`.
  name: Docusign DataSet API
  phrasing_intents:
  - id: Api_Version_DatasetsByDataSetNameStreamGet
    intent: Stream customer event data from a dataset
    question: How can I pull my organization's event data from a DocuSign dataset?
  phrasing_ops: 1
  slug: docusign-dataset-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The DocumentResponsiveHtmlPreview API from Docusign — 1 operation(s) for documentresponsivehtmlpreview.
  name: Docusign DocumentResponsiveHtmlPreview API
  phrasing_intents:
  - id: ResponsiveHtml_PostDocumentResponsiveHtmlPreview
    intent: Preview one document as responsive HTML
    question: Can I see how a single envelope document will look as responsive HTML on mobile?
  phrasing_ops: 1
  slug: docusign-documentresponsivehtmlpreview-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: Methods to grant access, delete, and get information, including contents, to a document.
  name: Docusign Documents API
  phrasing_intents:
  - id: Documents_GetDocument
    intent: Get a room document
    question: How do I fetch a document stored in a room?
  - id: Documents_DeleteDocument
    intent: Permanently delete a room document
    question: How do I permanently delete a document from a room?
  - id: Documents_CreateDocumentUser
    intent: Grant a user access to a room document
    question: How do I share a room document with another user?
  phrasing_ops: 3
  slug: docusign-documents-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The ENoteConfigurations resource provides methods that allow you to manage information for the eNote eOriginal integration.
  name: Docusign ENoteConfigurations API
  phrasing_intents:
  - id: ENoteConfiguration_GetENoteConfiguration
    intent: Get the eNote eOriginal integration settings
    question: Is the eNote eOriginal integration configured on my account?
  - id: ENoteConfiguration_PutENoteConfiguration
    intent: Update the eNote eOriginal integration
    question: How do I set up the eNote eOriginal integration credentials?
  - id: ENoteConfiguration_DeleteENoteConfiguration
    intent: Remove the eNote eOriginal integration
    question: Can I remove the eNote eOriginal configuration from my account?
  phrasing_ops: 3
  slug: docusign-enoteconfigurations-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeAttachments resource provides methods that allow you to manage attachments.
  name: Docusign EnvelopeAttachments API
  phrasing_intents:
  - id: Attachments_GetAttachments
    intent: List an envelope's attachments
    question: What attachments are on an envelope?
  - id: Attachments_PutAttachments
    intent: Add several attachments to an envelope
    question: Can I attach multiple files to a draft or in-process envelope in one call?
  - id: Attachments_DeleteAttachments
    intent: Delete attachments from a draft envelope
    question: How do I remove attachments from an envelope that hasn't been sent?
  - id: Attachments_GetAttachment
    intent: Retrieve one envelope attachment
    question: Can I download a specific attachment from an envelope?
  - id: Attachments_PutAttachment
    intent: Add or replace a single envelope attachment
    question: Can I set a label and access control on one attachment I add to an envelope?
  phrasing_ops: 5
  slug: docusign-envelopeattachments-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeConsumerDisclosures resource provides a method that allows you to retrieve the consumer disclosure for an envelope.
  name: Docusign EnvelopeConsumerDisclosures API
  phrasing_intents:
  - id: ConsumerDisclosure_GetConsumerDisclosureEnvelopeIdRecipientId
    intent: Get the disclosure shown to an envelope recipient
    question: Which e-signature disclosure did a recipient on my envelope see?
  - id: ConsumerDisclosure_GetConsumerDisclosureEnvelopeIdRecipientIdLangCode
    intent: Get a recipient's disclosure by language code
    question: Can I fetch an envelope recipient's disclosure for a language set in the path?
  phrasing_ops: 2
  slug: docusign-envelopeconsumerdisclosures-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeCustomFields resource provides methods that allow you manage custom fields in an envelope. Custom fields can be used in the envelopes for your account to record information about the envel
  name: Docusign EnvelopeCustomFields API
  phrasing_intents:
  - id: CustomFields_GetCustomFields
    intent: Get custom fields on an envelope
    question: What custom field values were recorded on an envelope?
  - id: CustomFields_PutCustomFields
    intent: Update existing envelope custom fields
    question: How do I change a custom field value on an in-process envelope?
  - id: CustomFields_PostCustomFields
    intent: Add custom fields to an envelope
    question: How do I add a new custom field to an envelope that's already out?
  - id: CustomFields_DeleteCustomFields
    intent: Delete custom fields from an envelope
    question: How do I remove custom fields from a draft envelope?
  phrasing_ops: 4
  slug: docusign-envelopecustomfields-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeDocumentFields resource provides methods that allow you to manage custom fields on a document. You can create custom versions of standard fields that combine of field properties, such as f
  name: Docusign EnvelopeDocumentFields API
  phrasing_intents:
  - id: DocumentFields_GetDocumentFields
    intent: Get custom fields on an envelope document
    question: What custom document fields are set on a document in a sent envelope?
  - id: DocumentFields_PutDocumentFields
    intent: Update custom fields on an envelope document
    question: How do I change the value of an existing custom field on an envelope document?
  - id: DocumentFields_PostDocumentFields
    intent: Add custom fields to an envelope document
    question: Can I attach new custom metadata fields to a document in an envelope?
  - id: DocumentFields_DeleteDocumentFields
    intent: Remove custom fields from an envelope document
    question: Can I delete custom fields from a document in an envelope?
  phrasing_ops: 4
  slug: docusign-envelopedocumentfields-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeDocumentHtmlDefinitions API from Docusign — 1 operation(s) for envelopedocumenthtmldefinitions.
  name: Docusign EnvelopeDocumentHtmlDefinitions API
  phrasing_intents:
  - id: ResponsiveHtml_GetEnvelopeDocumentHtmlDefinitions
    intent: Get responsive HTML definitions for an envelope document
    question: Where can I see the responsive HTML settings used for a document in an envelope?
  phrasing_ops: 1
  slug: docusign-envelopedocumenthtmldefinitions-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: Manage documents within envelopes including adding, retrieving, and deleting documents attached to envelopes.
  name: Docusign EnvelopeDocuments API
  phrasing_intents:
  - id: EnvelopeDocuments_ListDocuments
    intent: List envelope documents (unversioned endpoint)
    question: Which documents are inside an envelope, with their names, types and order?
  - id: EnvelopeDocuments_GetDocument
    intent: Download an envelope document (unversioned endpoint)
    question: Can I fetch a single document's content from an envelope through the simpler non-v2 endpoint?
  - id: Documents_GetDocuments
    intent: List an envelope's documents with optional sizes
    question: How do I see every document attached to an envelope along with file sizes?
  - id: Documents_PutDocuments
    intent: Add documents to an existing envelope
    question: Can I add more documents to an envelope that's already been created?
  - id: Documents_DeleteDocuments
    intent: Remove documents from a draft envelope
    question: How do I remove a document from an envelope that hasn't been completed?
  - id: Documents_GetDocument
    intent: Download a document, combined PDF or certificate
    question: How do I download all of an envelope's documents combined into one PDF?
  - id: Documents_PutDocument
    intent: Add or replace one document in a draft envelope
    question: Can I upload a single document into a specific slot of a draft envelope?
  phrasing_ops: 7
  slug: docusign-envelopedocuments-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeDocumentTabs resource provides methods that allow you to manage various tabs in envelopes. For a complete list of options see the following Properties section.
  name: Docusign EnvelopeDocumentTabs API
  phrasing_intents:
  - id: Tabs_GetPageTabs
    intent: Get tabs on one page of an envelope document
    question: Which fields are placed on a specific page of an envelope document?
  - id: Tabs_GetDocumentTabs
    intent: Get tabs on an envelope document
    question: What tabs are on a document inside an envelope?
  phrasing_ops: 2
  slug: docusign-envelopedocumenttabs-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Envelope Documents Visibility resource provides methods that manage document views and insights in an envelope.
  name: Docusign EnvelopeDocumentVisibility API
  phrasing_intents:
  - id: Recipients_GetRecipientDocumentVisibility
    intent: See which envelope documents a recipient can view
    question: Which documents in an envelope can a particular recipient see?
  - id: Recipients_PutRecipientDocumentVisibility
    intent: Set document visibility for one envelope recipient
    question: Can I hide a document from one specific recipient on an envelope?
  - id: Recipients_PutRecipientsDocumentVisibility
    intent: Set document visibility for all envelope recipients
    question: Can I update document visibility for several recipients of an envelope at once?
  phrasing_ops: 3
  slug: docusign-envelopedocumentvisibility-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeEmailSettings provide methods that allow you to manage the email override settings for an envelope. Email override settings change the reply to email address, name, or the BCC for email ar
  name: Docusign EnvelopeEmailSettings API
  phrasing_intents:
  - id: EmailSettings_GetEmailSettings
    intent: Get an envelope's email overrides
    question: What reply-to and BCC overrides are set on an envelope?
  - id: EmailSettings_PutEmailSettings
    intent: Change an envelope's existing email overrides
    question: How do I change the reply-to address already overridden on an envelope?
  - id: EmailSettings_PostEmailSettings
    intent: Add email overrides to an envelope
    question: Can replies to an envelope's emails go to a different address?
  - id: EmailSettings_DeleteEmailSettings
    intent: Remove all email overrides from an envelope
    question: How do I go back to the account's normal email settings for an envelope?
  phrasing_ops: 4
  slug: docusign-envelopeemailsettings-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeFormData resource provides methods that manage forms in an envelope.
  name: Docusign EnvelopeFormData API
  phrasing_intents:
  - id: FormData_GetFormData
    intent: Get the form data filled in on an envelope
    question: Can I pull the values signers entered into an envelope's fields?
  phrasing_ops: 1
  slug: docusign-envelopeformdata-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeHtmlDefinitions API from Docusign — 1 operation(s) for envelopehtmldefinitions.
  name: Docusign EnvelopeHtmlDefinitions API
  phrasing_intents:
  - id: ResponsiveHtml_GetEnvelopeHtmlDefinitions
    intent: Get an envelope's responsive HTML definitions
    question: Where can I see the responsive HTML definitions used to render an envelope?
  phrasing_ops: 1
  slug: docusign-envelopehtmldefinitions-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeLocks resource provides methods that allow you to manage locks on an envelope. You can lock the envelope, and set the time until the lock expires, to prevent users or recipients from acces
  name: Docusign EnvelopeLocks API
  phrasing_intents:
  - id: Lock_GetEnvelopeLock
    intent: Check whether an envelope is locked
    question: Who has an envelope locked and when does the lock expire?
  - id: Lock_PutEnvelopeLock
    intent: Extend or change an envelope lock
    question: Can I extend how long my lock on an envelope lasts?
  - id: Lock_PostEnvelopeLock
    intent: Lock an envelope for editing
    question: Can I lock an envelope so nobody else changes it while I edit?
  - id: Lock_DeleteEnvelopeLock
    intent: Release an envelope lock
    question: Can I unlock an envelope once I'm done editing?
  phrasing_ops: 4
  slug: docusign-envelopelocks-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The EnvelopeRecipients resource '
  name: Docusign EnvelopeRecipients API
  phrasing_intents:
  - id: Recipients_GetRecipients
    intent: Check recipient status on an envelope
    question: Who has signed an envelope so far and whose turn is it now?
  - id: Recipients_PutRecipients
    intent: Correct recipients on a draft or sent envelope
    question: Can I fix a signer's email address on an envelope that was already sent?
  - id: Recipients_PostRecipients
    intent: Add recipients to an envelope
    question: Can I add another signer to an envelope that's already in process?
  - id: Recipients_DeleteRecipients
    intent: Remove several recipients from an envelope
    question: Can I remove multiple recipients from an envelope in one request?
  - id: Recipients_DeleteRecipient
    intent: Remove one recipient from an envelope
    question: Can I delete a single recipient from an envelope by recipient ID?
  phrasing_ops: 5
  slug: docusign-enveloperecipients-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The EnvelopeRecipientTabs resour'
  name: Docusign EnvelopeRecipientTabs API
  phrasing_intents:
  - id: Recipients_GetRecipientTabs
    intent: Get a recipient's tabs and values
    question: How do I read the values a signer typed into fields on a completed envelope?
  - id: Recipients_PutRecipientTabs
    intent: Update a recipient's existing tabs
    question: How do I change the value of a text field already assigned to a recipient?
  - id: Recipients_PostRecipientTabs
    intent: Add tabs for a recipient
    question: How do I add a new sign-here field for a recipient?
  - id: Recipients_DeleteRecipientTabs
    intent: Delete a recipient's tabs
    question: How do I remove fields from a recipient on a draft envelope?
  phrasing_ops: 4
  slug: docusign-enveloperecipienttabs-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: Create, send, and manage envelopes. An envelope is the fundamental unit of a DocuSign transaction, containing the documents to be signed, the recipients who will sign them, and the workflow rules.
  name: Docusign Envelopes API
  phrasing_intents:
  - id: Envelopes_CreateEnvelope
    intent: Create an envelope from a template or documents
    question: How do I create an envelope from a template and fill in the template roles?
  - id: Envelopes_ListEnvelopes
    intent: Search envelopes by date, status or text
    question: How do I find envelopes sent in a date range using the newer envelopes endpoint?
  - id: Envelopes_GetEnvelope
    intent: Get an envelope's details (unversioned path)
    question: Where can I see an envelope's sender, recipients and documents on the unversioned envelope endpoint?
  - id: Envelopes_UpdateEnvelope
    intent: Update an envelope's subject or message
    question: How do I change the email subject on an envelope through the unversioned update endpoint?
  - id: Envelopes_GetEnvelopes
    intent: Get envelope status changes
    question: What envelopes changed status since a given date on the v2 API?
  - id: Envelopes_PostEnvelopes
    intent: Create and send an envelope (v2)
    question: How do I send documents for signature with the v2 envelopes API?
  - id: getV2AccountsByAccountIdEnvelopesByEnvelopeId
    intent: Get the status of one envelope (v2)
    question: What is the current status of a single envelope on the v2 API?
  - id: Envelopes_PutEnvelope
    intent: Send, void or purge an envelope
    question: How do I void an envelope that's still in process and give a reason?
  phrasing_ops: 21
  slug: docusign-envelopes-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeTemplates resource provides methods that allow you to add and delete templates on envelopes and documents.
  name: Docusign EnvelopeTemplates API
  phrasing_intents:
  - id: Templates_GetDocumentTemplates
    intent: List templates applied to an envelope document
    question: Which templates are applied to a particular document in an envelope?
  - id: Templates_PostDocumentTemplates
    intent: Apply templates to an envelope document
    question: How do I apply a template to one document inside an envelope?
  - id: Templates_DeleteDocumentTemplates
    intent: Remove a template from an envelope document
    question: How do I detach a template from a document in an envelope?
  - id: Templates_GetEnvelopeTemplates
    intent: List templates used in an envelope
    question: Which server-side templates were used to build an envelope?
  - id: Templates_PostEnvelopeTemplates
    intent: Add templates to an envelope
    question: How do I add a template to an envelope I've already created?
  phrasing_ops: 5
  slug: docusign-envelopetemplates-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: Generate URL tokens for embedded signing, sending, and recipient views to integrate DocuSign experiences directly into your application.
  name: Docusign EnvelopeViews API
  phrasing_intents:
  - id: EnvelopeViews_CreateRecipientView
    intent: Get an embedded signing URL for a recipient
    question: How do I let a recipient sign inside my own app using the unversioned views endpoint?
  - id: EnvelopeViews_CreateSenderView
    intent: Get an embedded sender URL (unversioned)
    question: Can I let a sender edit a draft envelope inside my app through the unversioned sender view?
  - id: Views_PostEnvelopeCorrectView
    intent: Get a URL to correct an envelope
    question: How do I embed the envelope correction screen in my app?
  - id: Views_DeleteEnvelopeCorrectView
    intent: Revoke an envelope correction view URL
    question: Can I invalidate a correction view link I generated earlier?
  - id: Views_PostEnvelopeEditView
    intent: Get a URL to the envelope edit view
    question: How do I embed the envelope editing screen with a one-time login token?
  - id: Views_PostEnvelopeRecipientView
    intent: Get a v2 embedded recipient signing URL
    question: How do I start the v2 signing ceremony for an embedded signer?
  - id: Views_PostEnvelopeSenderView
    intent: Get a v2 embedded sender URL
    question: Can I embed the v2 sender view so users can tag and send an envelope in my app?
  - id: Views_PostEnvelopeRecipientSharedView
    intent: Get a shared recipient view URL
    question: How can a user view an envelope shared with them through an embedded shared view?
  phrasing_ops: 9
  slug: docusign-envelopeviews-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: This resource provides a method that returns a list of the eSignature permission profiles that the current user can assign to a new member.
  name: Docusign ESignPermissionProfiles API
  phrasing_intents:
  - id: ESignPermissionProfiles_GetESignPermissionProfiles
    intent: List assignable eSignature permission profiles
    question: Which eSignature permission profiles can I give a new Rooms member?
  phrasing_ops: 1
  slug: docusign-esignpermissionprofiles-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to manage eSignature users in an account.
  name: Docusign eSignUserManagement API
  phrasing_intents:
  - id: Account_Accounts_GetPermissionProfilesV2
    intent: List an account's permission profiles from the org
    question: Which permission profiles exist in one of my organization's accounts?
  - id: Account_Accounts_GetGroupsV2
    intent: List an account's groups from the org
    question: What groups are set up in a specific account under my organization?
  - id: User_Users_UpdateV2
    intent: Update users' profile information
    question: How do I change a user's name or details across the organization?
  - id: User_Users_CloseMembershipsV2
    intent: Close a user's account memberships
    question: How do I remove a user's access to specific accounts in my organization?
  - id: OrganizationUser_Users_AddV2
    intent: Create a new user in the organization
    question: How do I add a brand-new user to my organization with access to accounts?
  - id: OrganizationUser_Users_ActivateMembershipV2
    intent: Activate a user's membership
    question: How can I activate a pending membership for an organization user?
  - id: OrganizationUser_OrganizationUsers_GetProfileV2
    intent: Look up recently modified users
    question: Which users in my organization were changed in the last ten days?
  - id: OrganizationUser_DeleteIdentitiesV2
    intent: Delete a user's login identities
    question: Can I remove a linked login identity from a user?
  phrasing_ops: 9
  slug: docusign-esignusermanagement-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The ExternalFormFillSessions API from Docusign — 1 operation(s) for externalformfillsessions.
  name: Docusign ExternalFormFillSessions API
  phrasing_intents:
  - id: ExternalFormFillSessions_CreateExternalFormFillSession
    intent: Start an external form fill session
    question: How do I get a URL for someone to fill out a form in a room?
  phrasing_ops: 1
  slug: docusign-externalformfillsessions-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: Information about field sets.
  name: Docusign Fields API
  phrasing_intents:
  - id: Fields_GetFieldSet
    intent: Get a room field set
    question: What fields make up a given field set for room details?
  phrasing_ops: 1
  slug: docusign-fields-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The FinancingTypes API from Docusign — 1 operation(s) for financingtypes.
  name: Docusign FinancingTypes API
  phrasing_intents:
  - id: FinancingTypes_GetFinancingTypes
    intent: List financing types
    question: What financing types can be used in a room?
  phrasing_ops: 1
  slug: docusign-financingtypes-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Folders resource provides methods that allow you to view contents of folders on the account and move envelopes between folders.
  name: Docusign Folders API
  phrasing_intents:
  - id: Folders_GetFolders
    intent: List folders
    question: What folders exist in my account, including the folder hierarchy?
  - id: Folders_GetFolderItems
    intent: List the envelopes in a folder
    question: Which envelopes are in a particular folder?
  - id: Folders_PutFolderById
    intent: Move envelopes to another folder
    question: How do I move an envelope into a different folder?
  - id: SearchFolders_GetSearchFolderContents
    intent: List envelopes in a search folder
    question: How do I see envelopes awaiting my signature or recently completed?
  phrasing_ops: 4
  slug: docusign-folders-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: This section shows you how to retrieve a form's details.
  name: Docusign FormDetails API
  phrasing_intents:
  - id: FormDetails_GetFormDetails
    intent: Get details about a Rooms form
    question: When was a form created, and who owns it?
  phrasing_ops: 1
  slug: docusign-formdetails-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The FormProviders API from Docusign — 1 operation(s) for formproviders.
  name: Docusign FormProviders API
  phrasing_intents:
  - id: FormProviderAssociations_GetFormProviderAssociations
    intent: List form provider associations
    question: Which associations exist for a given form provider?
  phrasing_ops: 1
  slug: docusign-formproviders-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The GroupBrands resource provides methods that allow you to manage
  name: Docusign GroupBrands API
  phrasing_intents:
  - id: Brands_GetGroupBrands
    intent: List brands assigned to a group
    question: Which brands can members of a group use?
  - id: Brands_PutGroupBrands
    intent: Assign brands to a group
    question: Can I give a group access to specific sending brands?
  - id: Brands_DeleteGroupBrands
    intent: Remove brands from a group
    question: How do I take a brand away from a group?
  phrasing_ops: 3
  slug: docusign-groupbrands-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Groups resource provides methods that allow you to manage groups for the account. Groups can be used to help manage users by associating users with a group. A group can be associated with a Permis
  name: Docusign Groups API
  phrasing_intents:
  - id: Groups_GetGroups
    intent: List user groups in an account
    question: What user groups exist in my account?
  - id: Groups_PutGroups
    intent: Rename groups or change their permission profile
    question: Can I rename an existing group?
  - id: Groups_PostGroups
    intent: Create user groups
    question: How do I create a new group to manage users together?
  - id: Groups_DeleteGroups
    intent: Delete user groups
    question: Can I delete a group I no longer need?
  phrasing_ops: 4
  slug: docusign-groups-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Invoices resource provides methods that allow you to manage the invoices for an account.
  name: Docusign Invoices API
  phrasing_intents:
  - id: BillingInvoices_GetBillingInvoices
    intent: List billing invoices
    question: Where can I see my DocuSign invoices for the past year?
  - id: BillingInvoices_GetBillingInvoice
    intent: Get a billing invoice
    question: How do I get the details of one invoice?
  - id: BillingInvoices_GetBillingInvoicesPastDue
    intent: List past-due invoices
    question: Do I have any overdue invoices on my account?
  phrasing_ops: 3
  slug: docusign-invoices-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to manage multi-product users in an account.
  name: Docusign MultiProductUserManagement API
  phrasing_intents:
  - id: DocuSignGroupsv21_GetDSGroups_V2_1
    intent: List DS groups in an account
    question: Which DS groups exist on an account in my organization?
  - id: DocuSignGroupsv21_AddDSGroup_V2_1
    intent: Create a DS group
    question: How do I create a new DS group for an account?
  - id: DocuSignGroupsv21_GetDSGroup_V2_1
    intent: Get details of a DS group
    question: What details can I see about a single DS group?
  - id: DocuSignGroupsv21_DeleteDSGroup_V2_1
    intent: Delete a DS group
    question: Can I delete a DS group I no longer need?
  - id: DocuSignGroupsv21_GetDSGroupUsers_V2_1
    intent: List the members of a DS group
    question: Who are the members of a particular DS group?
  - id: DocuSignGroupsv21_AddDSGroupUsers_V2_1
    intent: Add users to a DS group
    question: How do I add several users to a DS group at once?
  - id: DocuSignGroupsv21_RemoveDSGroupUsers_V2_1
    intent: Remove users from a DS group
    question: Can I remove a list of users from a DS group in one request?
  - id: OrganizationProductPermissionProfile_GetProductPermissionProfiles
    intent: List products and permission profiles for an account
    question: Which products does an account have and what permission profiles are available for each?
  phrasing_ops: 11
  slug: docusign-multiproductusermanagement-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The NotaryJournals API from Docusign — 1 operation(s) for notaryjournals.
  name: Docusign NotaryJournals API
  phrasing_intents:
  - id: NotaryJournals_GetNotaryJournals
    intent: List my notary journal entries
    question: Where can I see my notary journal entries?
  phrasing_ops: 1
  slug: docusign-notaryjournals-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The `Offices` resource enables you to create and manage offices for your company. You can also retrieve the number and type of objects that reference an office.
  name: Docusign Offices API
  phrasing_intents:
  - id: Offices_GetOffices
    intent: List offices
    question: Which offices are set up in my Rooms account?
  - id: Offices_CreateOffice
    intent: Create an office
    question: How do I add a new office to a Rooms account?
  - id: Offices_GetOffice
    intent: Get an office
    question: How do I get the details of one office?
  - id: Offices_DeleteOffice
    intent: Delete an office
    question: Can I delete an office from my Rooms account?
  - id: Offices_GetReferenceCounts
    intent: Count objects that reference an office
    question: What is still referencing an office I want to delete?
  phrasing_ops: 5
  slug: docusign-offices-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods for working with organizations.
  name: Docusign Organization API
  phrasing_intents:
  - id: Organization_Organization_GetListV2
    intent: List my organizations
    question: Which organizations does my user belong to?
  phrasing_ops: 1
  slug: docusign-organization-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: In the console, these are the values that can appear on a room's **Details** tab in the **Origin of lead** field.
  name: Docusign OriginsOfLeads API
  phrasing_intents:
  - id: OriginsOfLeads_GetOriginsOfLeads
    intent: List lead origins for rooms
    question: Which lead sources can I record on a room?
  phrasing_ops: 1
  slug: docusign-originsofleads-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The PaymentGatewayAccounts API from Docusign — 1 operation(s) for paymentgatewayaccounts.
  name: Docusign PaymentGatewayAccounts API
  phrasing_intents:
  - id: PaymentGatewayAccounts_GetAllPaymentGatewayAccounts
    intent: List payment gateway accounts
    question: Which payment gateways are connected to my account for collecting payments?
  phrasing_ops: 1
  slug: docusign-paymentgatewayaccounts-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Payments resource provides methods that allow you to manage payments for an account. These calls can only be used by users with account administrator privileges.
  name: Docusign Payments API
  phrasing_intents:
  - id: BillingPayments_GetPaymentList
    intent: List billing payments
    question: What payments has my account made over the last year?
  - id: BillingPayments_PostPayment
    intent: Pay a past due invoice
    question: Can I pay an overdue invoice through the API?
  - id: BillingPayments_GetPayment
    intent: Get a billing payment
    question: Can I see the details of one specific payment?
  phrasing_ops: 3
  slug: docusign-payments-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The PowerFormData resource provides a method to access power form data.
  name: Docusign PowerFormData API
  phrasing_intents:
  - id: PowerForms_GetPowerFormFormData
    intent: Export data submitted through a PowerForm
    question: How do I get the data people entered into a PowerForm?
  phrasing_ops: 1
  slug: docusign-powerformdata-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The PowerForms resource provides methods that allow you to manage power forms.
  name: Docusign PowerForms API
  phrasing_intents:
  - id: PowerForms_GetPowerFormsList
    intent: List my PowerForms
    question: Which self-service PowerForms are available to me?
  - id: PowerForms_PostPowerForm
    intent: Create a PowerForm from a template
    question: Can I turn a template into a self-service PowerForm link people can sign from?
  - id: PowerForms_DeletePowerFormsList
    intent: Delete several PowerForms at once
    question: Can I delete multiple PowerForms in a single request?
  - id: PowerForms_GetPowerForm
    intent: Get one PowerForm
    question: Can I see the settings and URL of one particular PowerForm?
  - id: PowerForms_PutPowerForm
    intent: Update an existing PowerForm
    question: Can I deactivate an existing PowerForm or change its instructions?
  - id: PowerForms_DeletePowerForm
    intent: Delete a single PowerForm
    question: Can I delete one PowerForm by its ID?
  - id: PowerForms_GetPowerFormsSenders
    intent: List PowerForm senders
    question: Who are the senders behind the PowerForms in my account?
  phrasing_ops: 7
  slug: docusign-powerforms-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: Manage envelope recipients including signers, carbon copy recipients, certified deliveries, and other recipient types.
  name: Docusign Recipients API
  phrasing_intents:
  - id: Recipients_ListRecipients
    intent: List an envelope's recipients and their status
    question: Which people are on an envelope and what is each one's signing status?
  - id: Recipients_UpdateRecipients
    intent: Edit recipients on an envelope
    question: Can I change a recipient's name, email or routing order on an envelope?
  - id: Recipients_CreateRecipients
    intent: Add new recipients to an envelope
    question: Does adding a recipient to a sent envelope create a corrected version?
  - id: Recipients_DeleteRecipients
    intent: Delete recipients from an envelope
    question: Can I take signers off a draft or sent envelope?
  phrasing_ops: 4
  slug: docusign-recipients-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The Regions API from Docusign — 3 operation(s) for regions.
  name: Docusign Regions API
  phrasing_intents:
  - id: Regions_GetRegions
    intent: List regions in a Rooms account
    question: Which regions are set up in my Rooms account?
  - id: Regions_CreateRegion
    intent: Create a region in Rooms
    question: How do I add a new region to my Rooms account?
  - id: Regions_GetRegion
    intent: Get details of a Rooms region
    question: Can I look up one region's name and creation date?
  - id: Regions_DeleteRegion
    intent: Delete a Rooms region
    question: Can I remove a region that's no longer used?
  - id: Regions_GetRegionReferenceCounts
    intent: Count objects that reference a region
    question: What is still referencing a region I want to delete?
  phrasing_ops: 5
  slug: docusign-regions-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The RequestLogs resource provide methods that allow you to retrieve and delete the API request log files. The log files contain the API requests associated with your integration. They can aid you in t
  name: Docusign RequestLogs API
  phrasing_intents:
  - id: APIRequestLog_GetRequestLogs
    intent: List API request log entries
    question: Can I download my recent API request logs for troubleshooting?
  - id: APIRequestLog_DeleteRequestLogs
    intent: Clear all API request logs
    question: Can I wipe out all the captured API request logs?
  - id: APIRequestLog_GetRequestLog
    intent: Get a single API request log entry
    question: Can I view the full request and response of one logged API call?
  - id: APIRequestLog_GetRequestLogSettings
    intent: Check API request logging settings
    question: Is API request logging currently turned on for me?
  - id: APIRequestLog_PutRequestLogSettings
    intent: Turn API request logging on or off
    question: Can I enable request logging to troubleshoot my integration?
  phrasing_ops: 5
  slug: docusign-requestlogs-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Resources resource provides a method which retrieves the base resources that are available.
  name: Docusign Resources API
  phrasing_intents:
  - id: ServiceInformation_GetResourceInformation
    intent: List the base resources of the REST API
    question: What resources are available in version 2 of the eSignature REST API?
  phrasing_ops: 1
  slug: docusign-resources-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The ResponsiveHtmlPreview API from Docusign — 1 operation(s) for responsivehtmlpreview.
  name: Docusign ResponsiveHtmlPreview API
  phrasing_intents:
  - id: ResponsiveHtml_PostResponsiveHtmlPreview
    intent: Preview a whole envelope as responsive HTML
    question: Can I preview all of an envelope's documents as responsive HTML?
  phrasing_ops: 1
  slug: docusign-responsivehtmlpreview-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: Each role is associated with specific permissions. Each new member is assigned a role when you create them, automatically granting them the permissions associated with that role. Roles use the followi
  name: Docusign Roles API
  phrasing_intents:
  - id: Roles_GetRoles
    intent: List company roles
    question: What company roles are defined in my Rooms account?
  - id: Roles_CreateRole
    intent: Create a company role
    question: How do I create a new role for my company account?
  - id: Roles_GetRole
    intent: Get a company role and its permissions
    question: What permissions does a specific role include?
  - id: Roles_UpdateRole
    intent: Update a company role
    question: How do I change the permissions on an existing role?
  - id: Roles_DeleteRole
    intent: Delete a company role
    question: How do I delete a role from my company account?
  phrasing_ops: 5
  slug: docusign-roles-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The RoomContactTypes API from Docusign — 1 operation(s) for roomcontacttypes.
  name: Docusign RoomContactTypes API
  phrasing_intents:
  - id: RoomContactTypes_GetRoomContactTypes
    intent: List room contact types
    question: What contact types like Buyer or Seller can I use in a room?
  phrasing_ops: 1
  slug: docusign-roomcontacttypes-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The RoomFolders API from Docusign — 1 operation(s) for roomfolders.
  name: Docusign RoomFolders API
  phrasing_intents:
  - id: RoomFolders_GetRoomFolders
    intent: List folders in a room
    question: What folders can I access inside a room?
  phrasing_ops: 1
  slug: docusign-roomfolders-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: A room can hold documents, envelopes, a list of tasks comprising a workflow, and other related information. You can invite others to this space and assign them permissions on a per-room basis.
  name: Docusign Rooms API
  phrasing_intents:
  - id: RoomEnvelopes_CreateRoomEnvelope
    intent: Create an eSignature envelope from room documents
    question: Can I send documents that already live in a room out for signature as an envelope?
  - id: Rooms_GetRoomFieldData
    intent: Get a room's details field values
    question: Where can I read the values shown on a room's Details tab?
  - id: Rooms_UpdateRoomFieldData
    intent: Update a room's details field values
    question: Can I change the values on a room's Details tab through the API?
  - id: Rooms_AddFormToRoom
    intent: Add a library form to a room
    question: Can I attach a form from our form library to a transaction room?
  - id: Rooms_GetRoomUsers
    intent: List the people in a room
    question: Who has been added as a member of a particular room?
  - id: Rooms_InviteUser
    intent: Invite someone to a room by email
    question: How do I invite a new person into a transaction room by email address?
  - id: Rooms_PutRoomUser
    intent: Change a room member's side or role
    question: Can I change which side of the transaction a room member is on?
  - id: Rooms_RevokeRoomUserAccess
    intent: Revoke a user's access to a room
    question: Can I remove someone's access to a room immediately or schedule it for a later date?
  phrasing_ops: 19
  slug: docusign-rooms-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The SellerDecisionTypes API from Docusign — 1 operation(s) for sellerdecisiontypes.
  name: Docusign SellerDecisionTypes API
  phrasing_intents:
  - id: SellerDecisionTypes_GetSellerDecisionTypes
    intent: List seller decision types for offers
    question: What decisions can a seller record on an offer?
  phrasing_ops: 1
  slug: docusign-sellerdecisiontypes-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Service Information API from Docusign — 1 operation(s) for service information.
  name: Docusign Service Information API
  phrasing_intents:
  - id: ServiceInformation_GetServiceInformation
    intent: List available REST API versions
    question: Which REST API versions are available on the service?
  phrasing_ops: 1
  slug: docusign-service-information-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The SigningGroups resource provides methods that allow you manage signing groups. Signing Groups allow you to create a group of people to which an envelope is sent. Any member of that group can open a
  name: Docusign SigningGroups API
  phrasing_intents:
  - id: SigningGroups_GetSigningGroups
    intent: List signing groups in an account
    question: Which signing groups exist in my account?
  - id: SigningGroups_PutSigningGroups
    intent: Rename several signing groups
    question: Can I rename more than one signing group in a single request?
  - id: SigningGroups_PostSigningGroups
    intent: Create signing groups
    question: How many signing groups and members can an account have?
  - id: SigningGroups_DeleteSigningGroups
    intent: Delete signing groups
    question: Can I delete one or more signing groups at once?
  - id: SigningGroups_GetSigningGroup
    intent: Get a signing group and its members
    question: Who are the members of a specific signing group?
  - id: SigningGroups_PutSigningGroup
    intent: Update a signing group's name or members
    question: Can I add new members to an existing signing group?
  phrasing_ops: 6
  slug: docusign-signinggroups-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The SigningGroupUsers resource provides methods that allow you to manage users in Signing Groups.
  name: Docusign SigningGroupUsers API
  phrasing_intents:
  - id: SigningGroups_GetSigningGroupUsers
    intent: List members of a signing group
    question: Who belongs to a signing group?
  - id: SigningGroups_PutSigningGroupUsers
    intent: Add members to a signing group
    question: How do I add people to a signing group?
  - id: SigningGroups_DeleteSigningGroupUsers
    intent: Remove members from a signing group
    question: Can I take someone out of a signing group?
  phrasing_ops: 3
  slug: docusign-signinggroupusers-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to import users.
  name: Docusign SingleAccountUserImport API
  phrasing_intents:
  - id: OrganizationImport_OrganizationImportSingleAccountUsers_Insert
    intent: Bulk-import new users into one account
    question: How do I bulk add users to one account from a CSV without an AccountId column?
  - id: OrganizationImport_OrganizationImportSingleAccountUsers_Update
    intent: Bulk-update existing users in one account
    question: Can I update many existing users in one account by uploading a CSV?
  phrasing_ops: 2
  slug: docusign-singleaccountuserimport-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The SpecialCircumstanceTypes API from Docusign — 1 operation(s) for specialcircumstancetypes.
  name: Docusign SpecialCircumstanceTypes API
  phrasing_intents:
  - id: SpecialCircumstanceTypes_GetSpecialCircumstanceTypes
    intent: List special circumstance types
    question: What special circumstance values, like short sale or foreclosure, can a room have?
  phrasing_ops: 1
  slug: docusign-specialcircumstancetypes-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The States API from Docusign — 1 operation(s) for states.
  name: Docusign States API
  phrasing_intents:
  - id: States_GetStates
    intent: List states
    question: What states or provinces can I choose for a room or office address?
  phrasing_ops: 1
  slug: docusign-states-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: Manage tabs (fields) placed on documents for recipients to interact with during the signing process, including signature, date, text, and checkbox tabs.
  name: Docusign Tabs API
  phrasing_intents:
  - id: Tabs_ListTabs
    intent: List a recipient's tabs in an envelope
    question: Which signature and form fields are assigned to a recipient?
  - id: Tabs_UpdateTabs
    intent: Update a recipient's tabs in a draft envelope
    question: How do I move or change a signer's sign-here fields before sending?
  phrasing_ops: 2
  slug: docusign-tabs-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: Task date types are the options that appear in the **Due Date** drop-down list when you create a task by using the console.
  name: Docusign TaskDateTypes API
  phrasing_intents:
  - id: TaskDateTypes_GetTaskDateTypes
    intent: List date types available for tasks
    question: What due date options can I use when creating a task?
  phrasing_ops: 1
  slug: docusign-taskdatetypes-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The TaskLists API from Docusign — 2 operation(s) for tasklists.
  name: Docusign TaskLists API
  phrasing_intents:
  - id: TaskLists_GetTaskLists
    intent: List a room's task lists
    question: What task lists are attached to a room?
  - id: TaskLists_CreateTaskList
    intent: Apply a task list template to a room
    question: How do I add a checklist of tasks to a room from a template?
  - id: TaskLists_DeleteTaskList
    intent: Delete a task list from a room
    question: How do I remove a task list from a room?
  phrasing_ops: 3
  slug: docusign-tasklists-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: If your administrator created room templates, those room templates may include task lists for you to use.
  name: Docusign TaskListTemplates API
  phrasing_intents:
  - id: TaskListTemplates_GetTaskListTemplates
    intent: List task list templates
    question: What task list templates does my company have?
  phrasing_ops: 1
  slug: docusign-tasklisttemplates-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The TaskResponsibilityTypes API from Docusign — 1 operation(s) for taskresponsibilitytypes.
  name: Docusign TaskResponsibilityTypes API
  phrasing_intents:
  - id: TaskResponsibilityTypes_GetTaskResponsibilityTypes
    intent: List task responsibility types
    question: What responsibility types can I assign to people on a task?
  phrasing_ops: 1
  slug: docusign-taskresponsibilitytypes-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateBulkRecipients resource provide methods that allow you manage the bulk recipient file for an template. The bulk recipient CSV (Comma Separated Value) file contains the list of recipient na
  name: Docusign TemplateBulkRecipients API
  phrasing_intents:
  - id: Recipients_GetTemplateBulkRecipients
    intent: Get a template's bulk recipient list
    question: How do I see the bulk recipient list on a template?
  - id: Recipients_PutTemplateBulkRecipients
    intent: Upload a template's bulk recipient list
    question: How do I upload a CSV of bulk recipients to a template?
  - id: Recipients_DeleteTemplateBulkRecipientsFile
    intent: Delete a template's bulk recipient list
    question: Can I remove the bulk recipient list from a template?
  phrasing_ops: 3
  slug: docusign-templatebulkrecipients-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateCustomFields resource provides methods that allow you manage custom fields in an template. Custom fields can be used in the templates for your account to record information about the templ
  name: Docusign TemplateCustomFields API
  phrasing_intents:
  - id: CustomFields_GetTemplateCustomFields
    intent: Get custom fields on a template
    question: What custom fields are defined on a template?
  - id: CustomFields_PutTemplateCustomFields
    intent: Update custom fields on a template
    question: How do I change an existing custom field on a template?
  - id: CustomFields_PostTemplateCustomFields
    intent: Add custom fields to a template
    question: How do I add new custom fields to a template?
  - id: CustomFields_DeleteTemplateCustomFields
    intent: Delete custom fields from a template
    question: How do I remove custom fields from a template?
  phrasing_ops: 4
  slug: docusign-templatecustomfields-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateDocumentFields resource provides methods that allow you to manage custom fields on a document. You can create custom versions of standard fields that combine of field properties, such as f
  name: Docusign TemplateDocumentFields API
  phrasing_intents:
  - id: DocumentFields_GetTemplateDocumentFields
    intent: Get custom fields on a template document
    question: What custom document fields are defined on a template's document?
  - id: DocumentFields_PutTemplateDocumentFields
    intent: Update custom fields on a template document
    question: How do I change existing custom field values on a template document?
  - id: DocumentFields_PostTemplateDocumentFields
    intent: Add custom fields to a template document
    question: Can I add new custom metadata fields to a template document?
  - id: DocumentFields_DeleteTemplateDocumentFields
    intent: Remove custom fields from a template document
    question: Can I delete custom fields from a template document?
  phrasing_ops: 4
  slug: docusign-templatedocumentfields-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateDocumentHtmlDefinitions API from Docusign — 1 operation(s) for templatedocumenthtmldefinitions.
  name: Docusign TemplateDocumentHtmlDefinitions API
  phrasing_intents:
  - id: ResponsiveHtml_GetTemplateDocumentHtmlDefinitions
    intent: Get responsive HTML definitions for a template document
    question: What responsive HTML settings are stored for a template's document?
  phrasing_ops: 1
  slug: docusign-templatedocumenthtmldefinitions-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateDocumentResponsiveHtmlPreview API from Docusign — 1 operation(s) for templatedocumentresponsivehtmlpreview.
  name: Docusign TemplateDocumentResponsiveHtmlPreview API
  phrasing_intents:
  - id: ResponsiveHtml_PostTemplateDocumentResponsiveHtmlPreview
    intent: Preview a template document as responsive HTML
    question: How will a template document look as responsive HTML on mobile?
  phrasing_ops: 1
  slug: docusign-templatedocumentresponsivehtmlpreview-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The TemplateDocuments resource p'
  name: Docusign TemplateDocuments API
  phrasing_intents:
  - id: Documents_GetTemplateDocuments
    intent: List the documents in a template
    question: Which documents are included in a template?
  - id: Documents_PutTemplateDocuments
    intent: Add documents to a template
    question: How do I add several documents to an existing template?
  - id: Documents_DeleteTemplateDocuments
    intent: Remove documents from a template
    question: Can I delete one or more documents from a template?
  - id: Documents_GetTemplateDocument
    intent: Download a template document as PDF
    question: How do I download a template's document as a PDF?
  - id: Documents_PutTemplateDocument
    intent: Add or replace one document in a template
    question: Can I add a single document to a template at a specific document ID?
  phrasing_ops: 5
  slug: docusign-templatedocuments-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateDocumentTabs API from Docusign — 2 operation(s) for templatedocumenttabs.
  name: Docusign TemplateDocumentTabs API
  phrasing_intents:
  - id: Tabs_GetTemplatePageTabs
    intent: Get tabs on one page of a template document
    question: Which fields sit on a specific page of a template document?
  - id: Tabs_GetTemplateDocumentTabs
    intent: Get tabs on a template document
    question: What tabs are defined on a document in my template?
  phrasing_ops: 2
  slug: docusign-templatedocumenttabs-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Template Document Visibility resource provides methods that allow views into envelope templates.
  name: Docusign TemplateDocumentVisibility API
  phrasing_intents:
  - id: Recipients_GetTemplateRecipientDocumentVisibility
    intent: See which template documents a recipient can view
    question: Which documents in a template will a given recipient be able to see?
  - id: Recipients_PutTemplateRecipientDocumentVisibility
    intent: Set document visibility for one template recipient
    question: Can I hide a template document from one particular recipient?
  - id: Recipients_PutTemplateRecipientsDocumentVisibility
    intent: Set document visibility for all template recipients
    question: Can I update document visibility for several template recipients in one request?
  phrasing_ops: 3
  slug: docusign-templatedocumentvisibility-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateHtmlDefinitions API from Docusign — 1 operation(s) for templatehtmldefinitions.
  name: Docusign TemplateHtmlDefinitions API
  phrasing_intents:
  - id: ResponsiveHtml_GetTemplateHtmlDefinitions
    intent: Get a template's responsive HTML definitions
    question: Can I see the responsive HTML definitions used for a template's documents?
  phrasing_ops: 1
  slug: docusign-templatehtmldefinitions-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateLocks resource provides methods that allow you to manage locks on an template. You can lock the template, and set the time until the lock expires, to prevent users from accessing and chang
  name: Docusign TemplateLocks API
  phrasing_intents:
  - id: Lock_GetTemplateLock
    intent: Check a template's lock
    question: Who currently has a template locked, and until when?
  - id: Lock_PutTemplateLock
    intent: Extend or change a template lock
    question: Can I extend how long my template lock lasts?
  - id: Lock_PostTemplateLock
    intent: Lock a template for editing
    question: How do I stop others from changing a template while I edit it?
  - id: Lock_DeleteTemplateLock
    intent: Release a template lock
    question: How do I unlock a template when I'm done editing?
  phrasing_ops: 4
  slug: docusign-templatelocks-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: 'The TemplateRecipients resource allows you manage the recipients of an template. The exact parameters associated with a recipient depend on the recipient type. There are seven recipient types: Agents,'
  name: Docusign TemplateRecipients API
  phrasing_intents:
  - id: Recipients_GetTemplateRecipients
    intent: List the recipients on a template
    question: Who are the recipients defined on a template?
  - id: Recipients_PutTemplateRecipients
    intent: Update existing recipients on a template
    question: Can I change a template recipient's email or routing order?
  - id: Recipients_PostTemplateRecipients
    intent: Add new recipients to a template
    question: How do I add another signer to an existing template?
  - id: Recipients_DeleteTemplateRecipients
    intent: Remove several recipients from a template
    question: Can I remove multiple recipients from a template at once?
  - id: Recipients_DeleteTemplateRecipient
    intent: Remove one recipient from a template
    question: How do I delete just one recipient from a template?
  phrasing_ops: 5
  slug: docusign-templaterecipients-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The TemplateRecipientTabs resour'
  name: Docusign TemplateRecipientTabs API
  phrasing_intents:
  - id: Recipients_GetTemplateRecipientTabs
    intent: List a template recipient's tabs
    question: Which fields and sign-here tabs are assigned to a recipient in a template?
  - id: Recipients_PutTemplateRecipientTabs
    intent: Update a template recipient's tabs
    question: Can I move or change existing tabs for a recipient on a template?
  - id: Recipients_PostTemplateRecipientTabs
    intent: Add tabs for a template recipient
    question: Can I add new sign-here or date tabs for a recipient on a template?
  - id: Recipients_DeleteTemplateRecipientTabs
    intent: Delete tabs from a template recipient
    question: Can I remove specific tabs from a recipient in a template?
  phrasing_ops: 4
  slug: docusign-templaterecipienttabs-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The TemplateResponsiveHtmlPreview API from Docusign — 1 operation(s) for templateresponsivehtmlpreview.
  name: Docusign TemplateResponsiveHtmlPreview API
  phrasing_intents:
  - id: ResponsiveHtml_PostTemplateResponsiveHtmlPreview
    intent: Preview a template as responsive HTML
    question: How do I see what a template's documents look like in responsive signing?
  phrasing_ops: 1
  slug: docusign-templateresponsivehtmlpreview-api
- baseURL: https://demo.docusign.net/restapi
  baseurl_source: declared
  description: Create and manage reusable templates that define documents, recipients, tabs, and routing for common agreement workflows.
  name: Docusign Templates API
  phrasing_intents:
  - id: Templates_ListTemplates
    intent: List templates in an account
    question: Which reusable envelope templates exist in my DocuSign account?
  - id: Templates_CreateTemplate
    intent: Create a reusable envelope template
    question: Can I create a template from scratch with documents, recipients and routing?
  - id: Templates_GetTemplate
    intent: Get a template's full definition
    question: What documents, recipients and tabs does a given template contain?
  - id: Templates_UpdateTemplate
    intent: Rename or edit a template
    question: Can I change a template's name, description or documents after creating it?
  - id: Templates_DeleteTemplate
    intent: Delete a template
    question: Can a deleted template be recovered from the recycle bin?
  - id: TemplateRecipients_ListRecipients
    intent: List the recipients defined on a template
    question: Which recipient roles and routing order are set up on a template?
  - id: TemplateRecipients_UpdateRecipients
    intent: Update recipients on a template
    question: Can I change the signers or carbon copies defined on a template?
  - id: Templates_GetTemplates
    intent: List templates via the v2 API
    question: With the v2 API, can I list templates modified within a date range?
  phrasing_ops: 19
  slug: docusign-templates-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: 'The TemplateViews resource provides a method returns a URL that you can embed into your application to provide access to the DocuSign UI. One template view is available: * Edit View - the DocuSign UI '
  name: Docusign TemplateViews API
  phrasing_intents:
  - id: Views_PostTemplateEditView
    intent: Get a URL to edit a template in the UI
    question: How can I embed the template editor in my own app?
  phrasing_ops: 1
  slug: docusign-templateviews-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The TimeZones API from Docusign — 1 operation(s) for timezones.
  name: Docusign TimeZones API
  phrasing_intents:
  - id: TimeZones_GetTimeZones
    intent: List time zones for offices
    question: Which time zones can I assign to an office?
  phrasing_ops: 1
  slug: docusign-timezones-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The TransactionSides API from Docusign — 1 operation(s) for transactionsides.
  name: Docusign TransactionSides API
  phrasing_intents:
  - id: TransactionSides_GetTransactionSides
    intent: List real estate transaction sides
    question: Which sides of a real estate transaction can a room member be placed on?
  phrasing_ops: 1
  slug: docusign-transactionsides-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The UserCustomSettings resource provides methods that allow you to manage the custom settings for a user. Custom settings are a flexible way to store and retrieve custom user information that can be u
  name: Docusign UserCustomSettings API
  phrasing_intents:
  - id: UserCustomSettings_GetCustomSettings
    intent: Get a user's custom settings
    question: What custom key-value settings are stored for a user?
  - id: UserCustomSettings_PutCustomSettings
    intent: Add or update a user's custom settings
    question: How do I store my own app data against a user?
  - id: UserCustomSettings_DeleteCustomSettings
    intent: Delete a user's custom settings
    question: Can I delete specific custom settings from a user?
  phrasing_ops: 3
  slug: docusign-usercustomsettings-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to import users. To ensure your CSV is properly formatted, use the [Sample Bulk Add CSV file](https://admin.docusign.com/static-resources/organization-user-import.csv) as a template. You can a
  name: Docusign UserImport API
  phrasing_intents:
  - id: OrganizationImport_OrganizationImportUsers_Insert
    intent: Bulk import new users from CSV
    question: How do I add a batch of new users to my organization from a CSV file?
  - id: OrganizationImport_OrganizationImportUsers_Update
    intent: Bulk update existing users from CSV
    question: Can I update details for lots of existing users at once with a CSV?
  - id: OrganizationImport_OrganizationImportUsers_Close
    intent: Bulk close user accounts
    question: How do I close a list of users' accounts in one go?
  - id: OrganizationImport_OrganizationImportUsers_CloseExternal
    intent: Close external memberships
    question: How do I remove users on my verified domain who don't belong to my organization?
  - id: OrganizationImport_OrganizationImportUsers_Get
    intent: List user import requests
    question: Which bulk user imports have been run for my organization?
  - id: OrganizationImport_OrganizationImportUsers_GetById
    intent: Check a user import request's status
    question: Has my bulk user import finished processing?
  - id: OrganizationImport_OrganizationImportUsers_DeleteById
    intent: Delete a user import request
    question: Can I delete an old import request and its results?
  - id: OrganizationImport_OrganizationImportUsers_GetCSVResults
    intent: Download a user import's CSV results
    question: Where can I see which rows of my user import failed?
  phrasing_ops: 8
  slug: docusign-userimport-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to manage users in an account.
  name: Docusign Users API
  phrasing_intents:
  - id: User_Users_UpdateEmailAddressesV2
    intent: Change users' email addresses in an organization
    question: Can an org admin change the email address a DocuSign user signs in with?
  - id: OrganizationUser_OrganizationUsers_GetV2
    intent: List the users in an organization
    question: Which people belong to my DocuSign organization, across all its accounts?
  - id: Users_GetUsers
    intent: List the users in an account
    question: Who are all the users on my eSignature account?
  - id: Users_PutUsers
    intent: Bulk-update several users in an account
    question: Can I change details for many account users in one request?
  - id: Users_PostUsers
    intent: Add new users to an account
    question: How do I add new users to my DocuSign account through the API?
  - id: Users_DeleteUsers
    intent: Close several user records in an account
    question: Can I close several user accounts at once so they can't use the account anymore?
  - id: User_GetUser
    intent: Get one user's details
    question: How can I look up a specific user's profile and last login date?
  - id: User_PutUser
    intent: Update a user's profile information
    question: Can I change a user's name, job title or permission profile through the API?
  phrasing_ops: 22
  slug: docusign-users-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The UserSignatures resource provides methods that allow you manage the intials and signature images for a user.
  name: Docusign UserSignatures API
  phrasing_intents:
  - id: UserSignatures_GetUserSignatures
    intent: List a user's saved signatures
    question: Which signature styles has a user saved on their account?
  - id: UserSignatures_PutUserSignature
    intent: Add or update a user's signatures in bulk
    question: Can I add or replace several of a user's signatures in one request?
  - id: UserSignatures_PostUserSignatures
    intent: Add signature and initials images for a user
    question: Can I upload a new signature image and initials image for a user?
  - id: UserSignatures_GetUserSignature
    intent: Get one of a user's signatures
    question: Can I look up a single user signature by its ID or name?
  - id: UserSignatures_PutUserSignatureById
    intent: Change a signature's font, name or initials
    question: Can I change the font used for a user's adopted signature?
  - id: UserSignatures_DeleteUserSignature
    intent: Remove a user's signature
    question: Can I delete a saved signature from a user's account?
  - id: UserSignatures_GetUserSignatureImage
    intent: Download a signature or initials image
    question: Can I download the actual image of a user's signature or initials?
  - id: UserSignatures_PutUserSignatureImage
    intent: Upload a new signature or initials image
    question: What image formats and file size are allowed for a signature image?
  phrasing_ops: 9
  slug: docusign-usersignatures-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The UserSocialAccountLogins resource provides methods that allow you to manage the social login accounts for a user.
  name: Docusign UserSocialAccountLogins API
  phrasing_intents:
  - id: UserSocialLogin_GetUserSocialLogin
    intent: List a user's linked social accounts
    question: Which social accounts are linked to a user's login?
  - id: UserSocialLogin_PutUserSocialLogin
    intent: Link a social account to a user
    question: How do I let a user sign in with a social account?
  - id: UserSocialLogin_DeleteUserSocialLogin
    intent: Unlink a social account from a user
    question: How do I remove a social login from a user?
  phrasing_ops: 3
  slug: docusign-usersocialaccountlogins-api
- baseURL: https://apps.docusign.com/api/maestro
  baseurl_source: declared
  description: Method to trigger a workflow.
  name: Docusign WorkflowTrigger API
  phrasing_intents:
  - id: triggerWorkflowViaPost
    intent: Trigger a new workflow instance
    question: How do I start a Maestro workflow from my application?
  phrasing_ops: 1
  slug: docusign-workflowtrigger-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The WorkspaceItems resource provides methods that allow you to manage workspace items.
  name: Docusign WorkspaceItems API
  phrasing_intents:
  - id: WorkspaceFolder_GetWorkspaceFolder
    intent: List the contents of a workspace folder
    question: What files and subfolders are in a workspace folder?
  - id: WorkspaceFolder_DeleteWorkspaceItems
    intent: Delete files or folders from a workspace
    question: Can I delete several workspace files and folders at once?
  - id: WorkspaceFile_PostWorkspaceFiles
    intent: Upload a file to a workspace folder
    question: How do I upload a new file into a workspace folder?
  - id: WorkspaceFile_GetWorkspaceFile
    intent: Download a workspace file
    question: Can I download the binary of a file stored in a workspace?
  - id: WorkspaceFile_PutWorkspaceFile
    intent: Update a workspace file's metadata
    question: Can I rename or change the metadata of a workspace file?
  - id: WorkspaceFilePages_GetWorkspaceFilePages
    intent: Render a workspace file as page images
    question: Can I get a workspace file as rasterized page images for a preview?
  phrasing_ops: 6
  slug: docusign-workspaceitems-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Docusign Workspaces API allows developers to create, manage, and integrate Docusign Workspaces into their own applications, enabling structured, secure, and scalable agreement workflows. It provid
  name: Docusign Workspaces API
  phrasing_intents:
  - id: Workspace_GetWorkspaces
    intent: List workspaces
    question: Which workspaces have been created in my account?
  - id: Workspace_PostWorkspace
    intent: Create a workspace
    question: Can I create a new shared workspace with a name and description?
  - id: Workspace_GetWorkspace
    intent: Get a workspace
    question: What are the properties of a specific workspace?
  - id: Workspace_PutWorkspace
    intent: Update a workspace
    question: Can I rename a workspace or change its description?
  - id: Workspace_DeleteWorkspace
    intent: Delete a workspace
    question: Is deleting a workspace a logical delete rather than a permanent purge?
  phrasing_ops: 5
  slug: docusign-workspaces-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: In certain countries, stamps are used to certify documents. This resource provides methods to manage stamps available in your account. To use these endpoints, your account must have Managed Stamps ena
  name: Docusign Account Signatures API
  slug: docusign-accountsignatures-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: A user authorization is created to share access between users on the same account. One user can be given access to sign, manage, or send on behalf of another. These endpoints allow you to create, dele
  name: Docusign Authorizations API
  slug: docusign-authorizations-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: You can configure automatic archiving of emails sent from all of your Docusign accounts. For more information, see [Email Archive Configuration](https://support.docusign.com/s/document-item?bundleId=p
  name: Docusign BCC Email Archive API
  slug: docusign-bccemailarchive-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: You can use bulk send lists send documents to a large number of recipients on a recurring basis. You can use a bulk send list to send up to 1,000 copies at a time. After you create a bulk send list, i
  name: Docusign Bulk Send API
  slug: docusign-bulksend-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: '[Document generation][webapp support page] enables you to create reusable templates with professionally formatted documents that include personalized data. For example, you can create a boilerplate em'
  name: Docusign Document Generation API
  slug: docusign-documentgeneration-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopePublish resource provides a method for submitting existing envelopes to a webhook using an ad hoc Connect configuration. See the [Connect category](/docs/esign-rest-api/reference/connect/)
  name: Docusign Envelope Publish API
  slug: docusign-envelopepublish-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The EnvelopeShares API from Docusign — 3 operation(s) for envelopeshares.
  name: Docusign Envelope Shares API
  slug: docusign-envelopeshares-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: Envelope transfer rules enable administrators to transfer envelopes and templates from user to another. For example, you might do this when an employee leaves the company. To transfer ownership of env
  name: Docusign Envelope Transfer Rules API
  slug: docusign-envelopetransferrules-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: Describes the workflow for an envelope or template. These methods enable you to use the [scheduled sending](/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/) and [delayed routing](
  name: Docusign Envelope Workflow Definition API
  slug: docusign-envelopeworkflowdefinition-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: 'The FavoriteTemplates resource enables you to get, add, and remove favorite templates. ### Related topics - [Common API Tasks: Working With Favorite Templates](https://www.docusign.com/blog/developers'
  name: Docusign Favorite Templates API
  slug: docusign-favoritetemplates-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: Docusign eNotary makes the notarization process fully digital for senders, signers, and notaries. It enables a notary public to act as an in-person witness to electronic signing of documents. Check th
  name: Docusign Notary API
  slug: docusign-notary-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: Creating, updating, and deleting notary jurisdiction objects.
  name: Docusign Notary Jurisdiction API
  slug: docusign-notaryjurisdiction-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Services resource provides a method that allow you to retrieve the available service versions.
  name: Docusign Services API
  slug: docusign-services-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: This resource has been deprecated.
  name: Docusign Tabs Blob API
  slug: docusign-tabsblob-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Billing resource provides methods that allow you to manage the billing plans,associated with an account.
  name: Docusign Billing Plans API
  phrasing_intents:
  - id: BillingPlan_GetBillingPlan
    intent: Get an account's current billing plan
    question: What billing plan is my account on, and what can it upgrade to?
  - id: BillingPlan_PutBillingPlan
    intent: Change an account's billing plan or payment details
    question: How do I switch my account to a different billing plan?
  - id: BillingPlan_GetCreditCardInfo
    intent: Get the credit card on file
    question: Which credit card is on file for my account?
  - id: PurchasedEnvelopes_PutPurchasedEnvelopes
    intent: Purchase additional envelopes (internal use)
    question: Can I buy extra envelopes for my account through the API?
  - id: BillingPlans_GetBillingPlans
    intent: List available billing plans
    question: What billing plans are available from my distributor?
  - id: BillingPlans_GetBillingPlan
    intent: Get details of a specific billing plan
    question: What's included in a particular billing plan?
  phrasing_ops: 6
  slug: docusign-billing-plans-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The CloudStorage resource provides methods that allow you to list files stored on your cloud storage provider.
  name: Docusign Cloud Storage API
  phrasing_intents:
  - id: CloudStorageFolder_GetCloudStorageFolderAll
    intent: Browse items across a user's cloud storage folders
    question: Can I search through everything a user has in a connected cloud storage service?
  - id: CloudStorageFolder_GetCloudStorageFolder
    intent: List items in a specific cloud storage folder
    question: What files are inside one particular folder of a user's cloud storage?
  phrasing_ops: 2
  slug: docusign-cloud-storage-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The CustomTabs resource provides methods that allow you create and manage custom tabs based on the existing DocuSign tabs. You can create a tab with pre-defined properties, such as a text tab with a c
  name: Docusign Custom Tabs API
  phrasing_intents:
  - id: Tabs_GetTabDefinitions
    intent: List the account's tab definitions
    question: What custom tabs have been defined on my account?
  - id: Tabs_PostTabDefinitions
    intent: Create a custom tab
    question: How do I create a reusable custom tab with a set font and validation pattern?
  - id: Tab_GetCustomTab
    intent: Get a custom tab
    question: How can I see the settings of one custom tab?
  - id: Tab_PutCustomTab
    intent: Update a custom tab
    question: Can I change the font or validation of an existing custom tab?
  - id: Tab_DeleteCustomTab
    intent: Delete a custom tab
    question: How do I delete a custom tab from my account?
  phrasing_ops: 5
  slug: docusign-custom-tabs-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: With the appropriate permissions, form administrators at your company can create form groups, or curated set of forms gathered from the association **form libraries** to which DocuSign provides access
  name: Docusign Form Groups API
  phrasing_intents:
  - id: FormGroups_GetFormGroups
    intent: List form groups
    question: Which company form groups can I access?
  - id: FormGroups_CreateFormGroup
    intent: Create a form group
    question: How do I create a new form group?
  - id: FormGroups_GetFormGroup
    intent: Get a form group
    question: Can I fetch the details of a single form group?
  - id: FormGroups_RenameFormGroup
    intent: Rename a form group
    question: Is it possible to rename an existing form group?
  - id: FormGroups_DeleteFormGroup
    intent: Delete a form group
    question: How do I delete a form group?
  - id: FormGroupForms_GetFormGroupForms
    intent: List the forms in a form group
    question: Which forms are in a given form group?
  - id: FormGroups_RemoveFormGroupForm
    intent: Remove a form from a form group
    question: Can I take one form out of a form group?
  - id: FormGroups_AssignFormGroupForm
    intent: Add a form to a form group
    question: How do I assign a form to a form group?
  phrasing_ops: 10
  slug: docusign-form-groups-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The Form Libraries API from Docusign — 2 operation(s) for form libraries.
  name: Docusign Form Libraries API
  phrasing_intents:
  - id: FormLibraries_GetFormLibraries
    intent: List form libraries I can access
    question: Which form libraries are available to me for rooms?
  - id: FormLibraries_GetFormLibraryForms
    intent: List forms in a form library
    question: What forms are inside a particular form library?
  phrasing_ops: 2
  slug: docusign-form-libraries-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The GroupUsers resource provides methods that allow you to manage the users in a group.
  name: Docusign Group Users API
  phrasing_intents:
  - id: Groups_GetGroupUsers
    intent: List users in a group
    question: Who is in a particular user group?
  - id: Groups_PutGroupUsers
    intent: Add users to a group
    question: How do I add people to an existing group?
  - id: Groups_DeleteGroupUsers
    intent: Remove users from a group
    question: How do I take users out of a group?
  phrasing_ops: 3
  slug: docusign-group-users-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to get a list of identity providers.
  name: Docusign Identity Providers API
  phrasing_intents:
  - id: Organization_GetIdentityProviders
    intent: List an organization's identity providers
    question: Which single sign-on identity providers are configured for my organization?
  phrasing_ops: 1
  slug: docusign-identity-providers-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The Identity Verifications API from Docusign — 2 operation(s) for identity verifications.
  name: Docusign Identity Verifications API
  phrasing_intents:
  - id: AccountIdentityVerification_GetAccountIdentityVerification
    intent: List identity verification options for an account
    question: Which identity verification workflows are available to my account?
  phrasing_ops: 1
  slug: docusign-identity-verifications-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: In the console, these are the values that can appear on a room's **Details** tab in the **Property type** field.
  name: Docusign Property Types API
  phrasing_intents:
  - id: PropertyTypes_GetPropertyTypes
    intent: List property types
    question: What property types can a room be tagged with?
  phrasing_ops: 1
  slug: docusign-property-types-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods to get a list of reserved domains.
  name: Docusign Reserved Domains API
  phrasing_intents:
  - id: Organization_GetReservedDomains
    intent: List an organization's reserved domains
    question: Which email domains has my organization reserved?
  phrasing_ops: 1
  slug: docusign-reserved-domains-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: You can use a room template to set the transaction side and task lists for rooms. For example, a broker can create a room template for agents to use. You can enable the room template for all regions a
  name: Docusign Room Templates API
  phrasing_intents:
  - id: RoomTemplates_GetRoomTemplates
    intent: List room templates
    question: Which room templates can I use to create a new room?
  phrasing_ops: 1
  slug: docusign-room-templates-api
- baseURL: https://rooms.docusign.com/restapi
  baseurl_source: declared
  description: The Task Statuses API from Docusign — 1 operation(s) for task statuses.
  name: Docusign Task Statuses API
  phrasing_intents:
  - id: TaskStatuses_GetTaskStatuses
    intent: List valid task statuses
    question: What statuses can a room task have?
  phrasing_ops: 1
  slug: docusign-task-statuses-api
- baseURL: https://api.docusign.net/Management
  baseurl_source: declared
  description: Methods for exporting a user list.
  name: Docusign User Export API
  phrasing_intents:
  - id: OrganizationExport_OrganizationExport_Get
    intent: List user list export requests
    question: Which user list exports have I requested for my organization?
  - id: OrganizationExport_OrganizationExport_Insert
    intent: Request a user list export
    question: How do I export a list of all users in my organization?
  - id: OrganizationExport_OrganizationExport_GetByExportId
    intent: Get a user list export's results
    question: Is my user list export ready to download?
  - id: OrganizationExport_OrganizationExport_DeleteByExportId
    intent: Delete a user list export request
    question: How do I delete a user export request I no longer need?
  phrasing_ops: 4
  slug: docusign-user-export-api
- baseURL: https://www.docusign.net/restapi
  baseurl_source: declared
  description: The UserProfiles resource provides methods that allow you to manage a user's profile.
  name: Docusign User Profiles API
  phrasing_intents:
  - id: UserProfile_GetProfile
    intent: Get a user's profile
    question: What personal details and privacy settings are on my user profile?
  - id: UserProfile_PutProfile
    intent: Update a user's profile
    question: Can I change a user's name or job title in their profile?
  phrasing_ops: 2
  slug: docusign-user-profiles-api
- baseURL: https://apps.docusign.com/api/maestro
  baseurl_source: declared
  description: Methods to get information about workflow instances.
  name: Docusign Workflow Instance Management API
  phrasing_intents:
  - id: cancelWorkflowInstance
    intent: Cancel a running workflow instance
    question: How do I stop a Maestro workflow instance that's still running?
  - id: getConfigInstances
    intent: List configuration instances of a workflow
    question: What configuration instances exist for a workflow definition?
  - id: getWorkflowInstances
    intent: List instances of a deployed workflow
    question: Which runs have been started for a deployed workflow?
  - id: getWorkflowInstance
    intent: Get details of a workflow instance
    question: How can I check the status of one specific workflow run?
  phrasing_ops: 4
  slug: docusign-workflow-instance-management-api
- baseURL: https://apps.docusign.com/api/maestro
  baseurl_source: declared
  description: Returns the history of the workflow instance steps.
  name: Docusign Workflow Management API
  phrasing_intents:
  - id: getWorkflowHistory
    intent: Get the step history of a workflow instance
    question: Which steps has a running Maestro workflow instance already completed?
  - id: getWorkflowDefinitions
    intent: List workflow definitions
    question: What Maestro workflow definitions exist in my account?
  - id: createNewWorkflowDefinition
    intent: Create a workflow definition
    question: Can I create a Maestro workflow definition through the API instead of the web UI?
  - id: getWorkflowDefinition
    intent: Get a workflow definition
    question: How do I fetch the full definition of one Maestro workflow?
  - id: updateWorkflowDefinition
    intent: Update a workflow definition
    question: Can I edit an existing Maestro workflow definition via the API?
  - id: deleteWorkflowDefinition
    intent: Delete a workflow definition
    question: How do I delete a Maestro workflow definition?
  - id: publishOrUnPublishWorkflowDefinition
    intent: Publish or unpublish a workflow definition
    question: How do I publish a workflow so it can be triggered?
  phrasing_ops: 7
  slug: docusign-workflow-management-api
arazzos:
- description: Resolve a template, then fan out multiple template-based envelopes to a list of recipients in one workflow run.
  name: DocuSign Bulk Send From Template
  slug: docusign-bulk-send-from-template-workflow
- description: List an envelope's recipients, update a recipient's email address, and resend the corrected envelope.
  name: DocuSign Correct Recipient Email and Resend
  slug: docusign-correct-recipient-email-and-resend-workflow
- description: Create a reusable template with a document and signer role, then send an envelope based on it.
  name: DocuSign Create Template and Send Envelope
  slug: docusign-create-template-and-send-envelope-workflow
- description: Confirm an envelope is completed, list its documents, and download the combined signed PDF.
  name: DocuSign Download Completed Documents
  slug: docusign-download-completed-documents-workflow
- description: Create a draft envelope with a document, add recipients to it, then send it by updating its status.
  name: DocuSign Build a Draft Envelope and Send
  slug: docusign-draft-envelope-add-recipients-and-send-workflow
- description: Create a draft envelope with a document, then generate an embedded sender view URL for in-app tagging and sending.
  name: DocuSign Draft Envelope Sender View
  slug: docusign-draft-envelope-sender-view-workflow
- description: Create and send an envelope to an embedded signer, then generate a recipient view URL for in-app signing.
  name: DocuSign Embedded Signing View
  slug: docusign-embedded-signing-view-workflow
- description: Search templates by name, read the matched template's roles, and send an envelope from it.
  name: DocuSign Find Template and Send
  slug: docusign-find-template-and-send-workflow
- description: List an envelope's recipients, then retrieve the tabs assigned to a chosen recipient.
  name: DocuSign Inspect Recipient Tabs
  slug: docusign-inspect-recipient-tabs-workflow
- description: List envelopes sent in a date range, then fetch full status detail for the first matching envelope.
  name: DocuSign List Sent Envelopes and Check Status
  slug: docusign-list-sent-envelopes-and-check-status-workflow
- description: Send an envelope to two signers in sequential routing order, then poll the recipients until both complete.
  name: DocuSign Multi-Signer Sequential Routing
  slug: docusign-multi-signer-routing-order-workflow
- description: Create a draft envelope, set a recipient's text tab values, then send the envelope.
  name: DocuSign Prefill Text Tabs and Send
  slug: docusign-prefill-text-tabs-and-send-workflow
- description: List an envelope's recipients and, if any are still pending, resend the envelope notification.
  name: DocuSign Resend Envelope to Pending Recipients
  slug: docusign-resend-envelope-to-pending-recipients-workflow
- description: Create and send an envelope with a document and signer, then poll until it reaches a terminal status.
  name: DocuSign Send Envelope and Track Status
  slug: docusign-send-envelope-and-track-status-workflow
- description: Send an envelope carrying envelope custom fields, then read them back via the envelope status.
  name: DocuSign Send Envelope With Custom Fields
  slug: docusign-send-envelope-with-custom-fields-workflow
- description: Create and send an envelope from an existing template by filling its roles, then poll the envelope to completion.
  name: DocuSign Send From Template and Poll
  slug: docusign-send-from-template-and-poll-workflow
- description: Read a template's recipients, update a role's default name and email, then verify the change.
  name: DocuSign Update Template Recipients
  slug: docusign-update-template-recipients-workflow
- description: Check an envelope's status and void it only if signing has not yet completed.
  name: DocuSign Void Envelope If Not Completed
  slug: docusign-void-envelope-if-not-completed-workflow
artifact_total: 470
asyncapis:
- description: DocuSign Connect is a webhook notification service that sends real-time updates about envelope and recipient events to your application. Connect pushes notifications to your listener endpoint when env
  name: DocuSign Connect Webhooks
  slug: docusign-connect-asyncapi
collections:
- collection_type: postman
  name: DocuSign Admin API
  slug: postman-docusign-admin-openapi-original
- collection_type: postman
  name: DocuSign Click API
  slug: postman-docusign-click-openapi-original
- collection_type: postman
  name: DocuSign eSignature REST API
  slug: postman-docusign-esignature
- collection_type: postman
  name: Docusign Maestro API
  slug: postman-docusign-maestro-openapi-original
- collection_type: postman
  name: Docusign Monitor API
  slug: postman-docusign-monitor-openapi-original
- collection_type: postman
  name: DocuSign REST API
  slug: postman-docusign-openapi-original
- collection_type: postman
  name: DocuSign Rooms API - v2
  slug: postman-docusign-rooms-openapi-original
- collection_type: open
  name: DocuSign Admin AccountBrands API
  slug: open-docusign-accountbrands-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountConsumerDisclosures API
  slug: open-docusign-accountconsumerdisclosures-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountCustomFields API
  slug: open-docusign-accountcustomfields-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountPasswordRules API
  slug: open-docusign-accountpasswordrules-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountPermissionProfiles API
  slug: open-docusign-accountpermissionprofiles-api
- collection_type: open
  name: DocuSign Admin AccountBrands Accounts API
  slug: open-docusign-accounts-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountSealProviders API
  slug: open-docusign-accountsealproviders-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountSettingsExport API
  slug: open-docusign-accountsettingsexport-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountSettingsImport API
  slug: open-docusign-accountsettingsimport-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountSignatureProviders API
  slug: open-docusign-accountsignatureproviders-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountTabSettings API
  slug: open-docusign-accounttabsettings-api
- collection_type: open
  name: DocuSign Admin AccountBrands AccountWatermarks API
  slug: open-docusign-accountwatermarks-api
- collection_type: open
  name: DocuSign Admin AccountBrands Authentication API
  slug: open-docusign-authentication-api
- collection_type: open
  name: DocuSign Admin AccountBrands BillingPlans API
  slug: open-docusign-billingplans-api
- collection_type: open
  name: DocuSign Admin AccountBrands ChunkedUploads API
  slug: open-docusign-chunkeduploads-api
- collection_type: open
  name: DocuSign Admin AccountBrands ClickWraps API
  slug: open-docusign-clickwraps-api
- collection_type: open
  name: DocuSign Admin AccountBrands ClosingStatuses API
  slug: open-docusign-closingstatuses-api
- collection_type: open
  name: DocuSign Admin AccountBrands CloudStorage API
  slug: open-docusign-cloudstorage-api
- collection_type: open
  name: DocuSign Admin AccountBrands CloudStorageProviders API
  slug: open-docusign-cloudstorageproviders-api
- collection_type: open
  name: DocuSign Admin AccountBrands Comments API
  slug: open-docusign-comments-api
- collection_type: open
  name: DocuSign Admin AccountBrands ConnectConfigurations API
  slug: open-docusign-connectconfigurations-api
- collection_type: open
  name: DocuSign Admin AccountBrands ConnectEvents API
  slug: open-docusign-connectevents-api
- collection_type: open
  name: DocuSign Admin AccountBrands ConnectSecret API
  slug: open-docusign-connectsecret-api
- collection_type: open
  name: DocuSign Admin AccountBrands Contacts API
  slug: open-docusign-contacts-api
- collection_type: open
  name: DocuSign Admin AccountBrands ContactSides API
  slug: open-docusign-contactsides-api
- collection_type: open
  name: DocuSign Admin AccountBrands Countries API
  slug: open-docusign-countries-api
- collection_type: open
  name: DocuSign Admin AccountBrands Currencies API
  slug: open-docusign-currencies-api
- collection_type: open
  name: DocuSign Admin AccountBrands CustomTabs API
  slug: open-docusign-customtabs-api
- collection_type: open
  name: DocuSign Admin AccountBrands DataSet API
  slug: open-docusign-dataset-api
- collection_type: open
  name: DocuSign Admin AccountBrands Documents API
  slug: open-docusign-documents-api
- collection_type: open
  name: DocuSign Admin AccountBrands ENoteConfigurations API
  slug: open-docusign-enoteconfigurations-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeAttachments API
  slug: open-docusign-envelopeattachments-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeConsumerDisclosures API
  slug: open-docusign-envelopeconsumerdisclosures-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeCustomFields API
  slug: open-docusign-envelopecustomfields-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeDocumentFields API
  slug: open-docusign-envelopedocumentfields-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeDocumentHtmlDefinitions API
  slug: open-docusign-envelopedocumenthtmldefinitions-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeDocuments API
  slug: open-docusign-envelopedocuments-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeDocumentTabs API
  slug: open-docusign-envelopedocumenttabs-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeDocumentVisibility API
  slug: open-docusign-envelopedocumentvisibility-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeEmailSettings API
  slug: open-docusign-envelopeemailsettings-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeFormData API
  slug: open-docusign-envelopeformdata-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeHtmlDefinitions API
  slug: open-docusign-envelopehtmldefinitions-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeLocks API
  slug: open-docusign-envelopelocks-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeRecipients API
  slug: open-docusign-enveloperecipients-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeRecipientTabs API
  slug: open-docusign-enveloperecipienttabs-api
- collection_type: open
  name: DocuSign Admin AccountBrands Envelopes API
  slug: open-docusign-envelopes-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeTemplates API
  slug: open-docusign-envelopetemplates-api
- collection_type: open
  name: DocuSign Admin AccountBrands EnvelopeViews API
  slug: open-docusign-envelopeviews-api
- collection_type: open
  name: DocuSign eSignature REST API
  slug: open-docusign-esignature
- collection_type: open
  name: DocuSign Admin AccountBrands ESignPermissionProfiles API
  slug: open-docusign-esignpermissionprofiles-api
- collection_type: open
  name: DocuSign Admin AccountBrands eSignUserManagement API
  slug: open-docusign-esignusermanagement-api
- collection_type: open
  name: DocuSign Admin AccountBrands ExternalFormFillSessions API
  slug: open-docusign-externalformfillsessions-api
- collection_type: open
  name: DocuSign Admin AccountBrands Fields API
  slug: open-docusign-fields-api
- collection_type: open
  name: DocuSign Admin AccountBrands FinancingTypes API
  slug: open-docusign-financingtypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands Folders API
  slug: open-docusign-folders-api
- collection_type: open
  name: DocuSign Admin AccountBrands FormDetails API
  slug: open-docusign-formdetails-api
- collection_type: open
  name: DocuSign Admin AccountBrands FormGroups API
  slug: open-docusign-formgroups-api
- collection_type: open
  name: DocuSign Admin AccountBrands FormLibraries API
  slug: open-docusign-formlibraries-api
- collection_type: open
  name: DocuSign Admin AccountBrands FormProviders API
  slug: open-docusign-formproviders-api
- collection_type: open
  name: DocuSign Admin AccountBrands GroupBrands API
  slug: open-docusign-groupbrands-api
- collection_type: open
  name: DocuSign Admin AccountBrands Groups API
  slug: open-docusign-groups-api
- collection_type: open
  name: DocuSign Admin AccountBrands GroupUsers API
  slug: open-docusign-groupusers-api
- collection_type: open
  name: DocuSign Admin AccountBrands IdentityProviders API
  slug: open-docusign-identityproviders-api
- collection_type: open
  name: DocuSign Admin AccountBrands IdentityVerifications API
  slug: open-docusign-identityverifications-api
- collection_type: open
  name: DocuSign Admin AccountBrands Invoices API
  slug: open-docusign-invoices-api
- collection_type: open
  name: DocuSign Admin AccountBrands MultiProductUserManagement API
  slug: open-docusign-multiproductusermanagement-api
- collection_type: open
  name: DocuSign Admin AccountBrands NotaryJournals API
  slug: open-docusign-notaryjournals-api
- collection_type: open
  name: DocuSign Admin AccountBrands Offices API
  slug: open-docusign-offices-api
- collection_type: open
  name: DocuSign Admin AccountBrands Organization API
  slug: open-docusign-organization-api
- collection_type: open
  name: DocuSign Admin AccountBrands OriginsOfLeads API
  slug: open-docusign-originsofleads-api
- collection_type: open
  name: DocuSign Admin AccountBrands PaymentGatewayAccounts API
  slug: open-docusign-paymentgatewayaccounts-api
- collection_type: open
  name: DocuSign Admin AccountBrands Payments API
  slug: open-docusign-payments-api
- collection_type: open
  name: DocuSign Admin AccountBrands PowerFormData API
  slug: open-docusign-powerformdata-api
- collection_type: open
  name: DocuSign Admin AccountBrands PowerForms API
  slug: open-docusign-powerforms-api
- collection_type: open
  name: DocuSign Admin AccountBrands PropertyTypes API
  slug: open-docusign-propertytypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands Recipients API
  slug: open-docusign-recipients-api
- collection_type: open
  name: DocuSign Admin AccountBrands Regions API
  slug: open-docusign-regions-api
- collection_type: open
  name: DocuSign Admin AccountBrands RequestLogs API
  slug: open-docusign-requestlogs-api
- collection_type: open
  name: DocuSign Admin AccountBrands ReservedDomains API
  slug: open-docusign-reserveddomains-api
- collection_type: open
  name: DocuSign Admin AccountBrands Resources API
  slug: open-docusign-resources-api
- collection_type: open
  name: DocuSign Admin AccountBrands Roles API
  slug: open-docusign-roles-api
- collection_type: open
  name: DocuSign Admin AccountBrands RoomContactTypes API
  slug: open-docusign-roomcontacttypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands RoomFolders API
  slug: open-docusign-roomfolders-api
- collection_type: open
  name: DocuSign Admin AccountBrands Rooms API
  slug: open-docusign-rooms-api
- collection_type: open
  name: DocuSign Admin AccountBrands RoomTemplates API
  slug: open-docusign-roomtemplates-api
- collection_type: open
  name: DocuSign Admin AccountBrands SellerDecisionTypes API
  slug: open-docusign-sellerdecisiontypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands Service Information API
  slug: open-docusign-service-information-api
- collection_type: open
  name: DocuSign Admin AccountBrands SigningGroups API
  slug: open-docusign-signinggroups-api
- collection_type: open
  name: DocuSign Admin AccountBrands SigningGroupUsers API
  slug: open-docusign-signinggroupusers-api
- collection_type: open
  name: DocuSign Admin AccountBrands SingleAccountUserImport API
  slug: open-docusign-singleaccountuserimport-api
- collection_type: open
  name: DocuSign Admin AccountBrands SpecialCircumstanceTypes API
  slug: open-docusign-specialcircumstancetypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands States API
  slug: open-docusign-states-api
- collection_type: open
  name: DocuSign Admin AccountBrands Tabs API
  slug: open-docusign-tabs-api
- collection_type: open
  name: DocuSign Admin AccountBrands TaskDateTypes API
  slug: open-docusign-taskdatetypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands TaskLists API
  slug: open-docusign-tasklists-api
- collection_type: open
  name: DocuSign Admin AccountBrands TaskListTemplates API
  slug: open-docusign-tasklisttemplates-api
- collection_type: open
  name: DocuSign Admin AccountBrands TaskResponsibilityTypes API
  slug: open-docusign-taskresponsibilitytypes-api
- collection_type: open
  name: DocuSign Admin AccountBrands TaskStatuses API
  slug: open-docusign-taskstatuses-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateBulkRecipients API
  slug: open-docusign-templatebulkrecipients-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateCustomFields API
  slug: open-docusign-templatecustomfields-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateDocumentFields API
  slug: open-docusign-templatedocumentfields-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateDocumentHtmlDefinitions API
  slug: open-docusign-templatedocumenthtmldefinitions-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateDocuments API
  slug: open-docusign-templatedocuments-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateDocumentTabs API
  slug: open-docusign-templatedocumenttabs-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateDocumentVisibility API
  slug: open-docusign-templatedocumentvisibility-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateHtmlDefinitions API
  slug: open-docusign-templatehtmldefinitions-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateLocks API
  slug: open-docusign-templatelocks-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateRecipients API
  slug: open-docusign-templaterecipients-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateRecipientTabs API
  slug: open-docusign-templaterecipienttabs-api
- collection_type: open
  name: DocuSign Admin AccountBrands Templates API
  slug: open-docusign-templates-api
- collection_type: open
  name: DocuSign Admin AccountBrands TemplateViews API
  slug: open-docusign-templateviews-api
- collection_type: open
  name: DocuSign Admin AccountBrands TimeZones API
  slug: open-docusign-timezones-api
- collection_type: open
  name: DocuSign Admin AccountBrands TransactionSides API
  slug: open-docusign-transactionsides-api
- collection_type: open
  name: DocuSign Admin AccountBrands UserCustomSettings API
  slug: open-docusign-usercustomsettings-api
- collection_type: open
  name: DocuSign Admin AccountBrands UserExport API
  slug: open-docusign-userexport-api
- collection_type: open
  name: DocuSign Admin AccountBrands UserImport API
  slug: open-docusign-userimport-api
- collection_type: open
  name: DocuSign Admin AccountBrands UserProfiles API
  slug: open-docusign-userprofiles-api
- collection_type: open
  name: DocuSign Admin AccountBrands Users API
  slug: open-docusign-users-api
- collection_type: open
  name: DocuSign Admin AccountBrands UserSignatures API
  slug: open-docusign-usersignatures-api
- collection_type: open
  name: DocuSign Admin AccountBrands UserSocialAccountLogins API
  slug: open-docusign-usersocialaccountlogins-api
- collection_type: open
  name: DocuSign Admin AccountBrands WorkflowInstanceManagement API
  slug: open-docusign-workflowinstancemanagement-api
- collection_type: open
  name: DocuSign Admin AccountBrands WorkflowManagement API
  slug: open-docusign-workflowmanagement-api
- collection_type: open
  name: DocuSign Admin AccountBrands WorkflowTrigger API
  slug: open-docusign-workflowtrigger-api
- collection_type: open
  name: DocuSign Admin AccountBrands WorkspaceItems API
  slug: open-docusign-workspaceitems-api
- collection_type: open
  name: DocuSign Admin AccountBrands Workspaces API
  slug: open-docusign-workspaces-api
common:
- group: commercial
  href: https://artifacts.apis.io/docusign/finops/docusign-finops.yml
  title: ''
  type: FinOps
  url: finops/docusign-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ecom.docusign.com/plans-and-pricing/esignature
- group: commercial
  href: https://artifacts.apis.io/docusign/plans/docusign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docusign-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.docusign.com/
- group: other
  href: https://artifacts.apis.io/docusign/capabilities/docusign-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/docusign-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/docusign/agentic-access/docusign-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docusign-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/docusign/security/docusign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docusign-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/docusign/authentication/docusign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docusign-authentication.yml
- group: auth
  href: https://artifacts.apis.io/docusign/scopes/docusign-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/docusign-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/docusign/overview
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-bulk-send-from-template-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-bulk-send-from-template-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-correct-recipient-email-and-resend-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-correct-recipient-email-and-resend-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-create-template-and-send-envelope-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-create-template-and-send-envelope-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-download-completed-documents-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-download-completed-documents-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-draft-envelope-add-recipients-and-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-draft-envelope-add-recipients-and-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-draft-envelope-sender-view-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-draft-envelope-sender-view-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-embedded-signing-view-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-embedded-signing-view-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-find-template-and-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-find-template-and-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-inspect-recipient-tabs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-inspect-recipient-tabs-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-list-sent-envelopes-and-check-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-list-sent-envelopes-and-check-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-multi-signer-routing-order-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-multi-signer-routing-order-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-prefill-text-tabs-and-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-prefill-text-tabs-and-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-resend-envelope-to-pending-recipients-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-resend-envelope-to-pending-recipients-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-send-envelope-and-track-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-send-envelope-and-track-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-send-envelope-with-custom-fields-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-send-envelope-with-custom-fields-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-send-from-template-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-send-from-template-and-poll-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-update-template-recipients-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-update-template-recipients-workflow.yml
- group: design
  href: https://artifacts.apis.io/docusign/arazzo/docusign-void-envelope-if-not-completed-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/docusign-void-envelope-if-not-completed-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docusign
- group: start
  title: ''
  type: Portal
  url: https://developers.docusign.com/
- group: build
  title: ''
  type: SDKs
  url: https://developers.docusign.com/docs/esign-rest-api/sdks/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.docusign.com/platform/auth/
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.docusign.com/tools/openapi-files/
- group: operate
  title: ''
  type: Support
  url: https://developers.docusign.com/support/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/docusignapi
- group: operate
  title: ''
  type: FAQ
  url: https://support.docusign.com/s/articles/DocuSign-Developer-Support-FAQs
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCJSJ2kMs_qeQotmw4-lX2NQ
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.docusign.com/changelog?filter=
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docusign
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.docusign.com/docs/esign-rest-api/quickstart/
- group: other
  title: ''
  type: Resources
  url: https://www.docusign.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docusign.com/company/terms-and-conditions/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.docusign.com/docs/esign-rest-api/quickstart/
- group: build
  title: ''
  type: CodeExamples
  url: https://developers.docusign.com/docs/esign-rest-api/code-examples/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docusign.com/
- group: company
  title: ''
  type: Blog
  url: https://www.docusign.com/blog/developers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docusign.com/company/privacy-policy
- group: start
  title: ''
  type: Sandbox
  url: https://go.docusign.com/sandbox/productshot/
- group: start
  title: ''
  type: Signup
  url: https://developers.docusign.com/platform/account/
- group: commercial
  title: ''
  type: Pricing
  url: https://ecom.docusign.com/plans-and-pricing/developer
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.docusign.com/platform/resource-limits/
- group: auth
  title: ''
  type: Security
  url: https://www.docusign.com/trust/security
- group: learn
  title: ''
  type: Training
  url: https://developers.docusign.com/training/
- group: build
  title: ''
  type: SDKs
  url: https://developers.docusign.com/docs/sdks/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/docusign/mcp-agent-foundry-procurement-python
created: '2024-06-07T00:00:00.000Z'
description: DocuSign helps organizations connect and automate how they prepare, sign, act on, and manage agreements. As part of the DocuSign Agreement Cloud, DocuSign offers eSignature, the world's.
examples:
- key_count: 5
  name: Docusign Esignature Agent Example
  slug: docusign-esignature-agent-example
- key_count: 8
  name: Docusign Esignature Approve Example
  slug: docusign-esignature-approve-example
- key_count: 7
  name: Docusign Esignature Carbon Copy Example
  slug: docusign-esignature-carbon-copy-example
- key_count: 5
  name: Docusign Esignature Certified Delivery Example
  slug: docusign-esignature-certified-delivery-example
- key_count: 11
  name: Docusign Esignature Checkbox Example
  slug: docusign-esignature-checkbox-example
- key_count: 3
  name: Docusign Esignature Composite Template Example
  slug: docusign-esignature-composite-template-example
- key_count: 2
  name: Docusign Esignature Custom Fields Example
  slug: docusign-esignature-custom-fields-example
- key_count: 9
  name: Docusign Esignature Date Signed Example
  slug: docusign-esignature-date-signed-example
- key_count: 9
  name: Docusign Esignature Date Tab Example
  slug: docusign-esignature-date-tab-example
- key_count: 9
  name: Docusign Esignature Decline Example
  slug: docusign-esignature-decline-example
- key_count: 10
  name: Docusign Esignature Document Example
  slug: docusign-esignature-document-example
- key_count: 5
  name: Docusign Esignature Editor Example
  slug: docusign-esignature-editor-example
- key_count: 9
  name: Docusign Esignature Email Tab Example
  slug: docusign-esignature-email-tab-example
- key_count: 9
  name: Docusign Esignature Envelope Definition Example
  slug: docusign-esignature-envelope-definition-example
- key_count: 9
  name: Docusign Esignature Envelope Document Example
  slug: docusign-esignature-envelope-document-example
- key_count: 2
  name: Docusign Esignature Envelope Documents Result Example
  slug: docusign-esignature-envelope-documents-result-example
- key_count: 24
  name: Docusign Esignature Envelope Example
  slug: docusign-esignature-envelope-example
- key_count: 15
  name: Docusign Esignature Envelope Recipient Tabs Example
  slug: docusign-esignature-envelope-recipient-tabs-example
- key_count: 4
  name: Docusign Esignature Envelope Summary Example
  slug: docusign-esignature-envelope-summary-example
- key_count: 15
  name: Docusign Esignature Envelope Template Example
  slug: docusign-esignature-envelope-template-example
- key_count: 8
  name: Docusign Esignature Envelope Template Results Example
  slug: docusign-esignature-envelope-template-results-example
- key_count: 5
  name: Docusign Esignature Envelope Update Summary Example
  slug: docusign-esignature-envelope-update-summary-example
- key_count: 7
  name: Docusign Esignature Envelopes Information Example
  slug: docusign-esignature-envelopes-information-example
- key_count: 2
  name: Docusign Esignature Error Details Example
  slug: docusign-esignature-error-details-example
- key_count: 12
  name: Docusign Esignature Event Notification Example
  slug: docusign-esignature-event-notification-example
- key_count: 10
  name: Docusign Esignature Formula Tab Example
  slug: docusign-esignature-formula-tab-example
- key_count: 9
  name: Docusign Esignature Full Name Example
  slug: docusign-esignature-full-name-example
- key_count: 7
  name: Docusign Esignature In Person Signer Example
  slug: docusign-esignature-in-person-signer-example
- key_count: 10
  name: Docusign Esignature Initial Here Example
  slug: docusign-esignature-initial-here-example
- key_count: 5
  name: Docusign Esignature Intermediary Example
  slug: docusign-esignature-intermediary-example
- key_count: 11
  name: Docusign Esignature List Tab Example
  slug: docusign-esignature-list-tab-example
- key_count: 8
  name: Docusign Esignature Note Tab Example
  slug: docusign-esignature-note-tab-example
- key_count: 3
  name: Docusign Esignature Notification Example
  slug: docusign-esignature-notification-example
- key_count: 9
  name: Docusign Esignature Number Tab Example
  slug: docusign-esignature-number-tab-example
- key_count: 5
  name: Docusign Esignature Radio Group Example
  slug: docusign-esignature-radio-group-example
- key_count: 3
  name: Docusign Esignature Recipient Email Notification Example
  slug: docusign-esignature-recipient-email-notification-example
- key_count: 11
  name: Docusign Esignature Recipient View Request Example
  slug: docusign-esignature-recipient-view-request-example
- key_count: 10
  name: Docusign Esignature Recipients Example
  slug: docusign-esignature-recipients-example
- key_count: 1
  name: Docusign Esignature Recipients Update Summary Example
  slug: docusign-esignature-recipients-update-summary-example
- key_count: 14
  name: Docusign Esignature Sign Here Example
  slug: docusign-esignature-sign-here-example
- key_count: 17
  name: Docusign Esignature Signer Example
  slug: docusign-esignature-signer-example
- key_count: 7
  name: Docusign Esignature Template Role Example
  slug: docusign-esignature-template-role-example
- key_count: 3
  name: Docusign Esignature Template Summary Example
  slug: docusign-esignature-template-summary-example
- key_count: 23
  name: Docusign Esignature Text Example
  slug: docusign-esignature-text-example
- key_count: 4
  name: Docusign Esignature User Info Example
  slug: docusign-esignature-user-info-example
- key_count: 1
  name: Docusign Esignature View Url Example
  slug: docusign-esignature-view-url-example
- key_count: 5
  name: Docusign Esignature Witness Example
  slug: docusign-esignature-witness-example
features:
- Personal at $10/mo annual with 5 envelopes/month
- Standard at $25/user/mo with 100 envelopes/user/year
- Business Pro at $40/user/mo with bulk send, payment collection
- Enterprise with API access, Salesforce/Workday integrations
- Envelope overage $3-$8 each depending on plan
- 'REST API: 1,000 req/hr, 10 req/sec burst, 200 envelopes/hr'
- 30 concurrent connection cap
- OAuth 2.0 (JWT, ACG, AGCG, IGCG)
- Webhooks via DocuSign Connect
- eSignature, CLM, Maestro Workflow, ID Verification, Insight, Notary APIs
- REST API access requires premium / Enterprise plan
- Signature workflows with conditional routing
- Embedded signing (signer & sender)
- Templates with reusable fields
- Bulk send for high-volume campaigns
- Payment collection at signing (Stripe/Authorize.net)
finops:
- has_sources: true
  method: derived
  name: Docusign Finops
  primary_unit: user
  service_category: ''
  slug: docusign-finops
  template: false
image: https://www.docusign.com/sites/default/files/docusign_logo.png
json_schemas:
- name: DocuSign Envelope Schema
  property_count: 1
  slug: docusign-envelope
- name: Agent
  property_count: 5
  slug: docusign-esignature-agent
- name: Approve
  property_count: 8
  slug: docusign-esignature-approve
- name: CarbonCopy
  property_count: 7
  slug: docusign-esignature-carbon-copy
- name: CertifiedDelivery
  property_count: 5
  slug: docusign-esignature-certified-delivery
- name: Checkbox
  property_count: 11
  slug: docusign-esignature-checkbox
- name: CompositeTemplate
  property_count: 3
  slug: docusign-esignature-composite-template
- name: CustomFields
  property_count: 2
  slug: docusign-esignature-custom-fields
- name: DateSigned
  property_count: 9
  slug: docusign-esignature-date-signed
- name: DateTab
  property_count: 9
  slug: docusign-esignature-date-tab
- name: Decline
  property_count: 9
  slug: docusign-esignature-decline
- name: Document
  property_count: 10
  slug: docusign-esignature-document
- name: Editor
  property_count: 5
  slug: docusign-esignature-editor
- name: EmailTab
  property_count: 9
  slug: docusign-esignature-email-tab
- name: EnvelopeDefinition
  property_count: 9
  slug: docusign-esignature-envelope-definition
- name: EnvelopeDocument
  property_count: 9
  slug: docusign-esignature-envelope-document
- name: EnvelopeDocumentsResult
  property_count: 2
  slug: docusign-esignature-envelope-documents-result
- name: EnvelopeRecipientTabs
  property_count: 15
  slug: docusign-esignature-envelope-recipient-tabs
- name: Envelope
  property_count: 24
  slug: docusign-esignature-envelope
- name: EnvelopeSummary
  property_count: 4
  slug: docusign-esignature-envelope-summary
- name: EnvelopeTemplateResults
  property_count: 8
  slug: docusign-esignature-envelope-template-results
- name: EnvelopeTemplate
  property_count: 15
  slug: docusign-esignature-envelope-template
- name: EnvelopeUpdateSummary
  property_count: 5
  slug: docusign-esignature-envelope-update-summary
- name: EnvelopesInformation
  property_count: 7
  slug: docusign-esignature-envelopes-information
- name: ErrorDetails
  property_count: 2
  slug: docusign-esignature-error-details
- name: EventNotification
  property_count: 12
  slug: docusign-esignature-event-notification
- name: FormulaTab
  property_count: 10
  slug: docusign-esignature-formula-tab
- name: FullName
  property_count: 9
  slug: docusign-esignature-full-name
- name: InPersonSigner
  property_count: 7
  slug: docusign-esignature-in-person-signer
- name: InitialHere
  property_count: 10
  slug: docusign-esignature-initial-here
- name: Intermediary
  property_count: 5
  slug: docusign-esignature-intermediary
- name: ListTab
  property_count: 11
  slug: docusign-esignature-list-tab
- name: NoteTab
  property_count: 8
  slug: docusign-esignature-note-tab
- name: Notification
  property_count: 3
  slug: docusign-esignature-notification
- name: NumberTab
  property_count: 9
  slug: docusign-esignature-number-tab
- name: RadioGroup
  property_count: 5
  slug: docusign-esignature-radio-group
- name: RecipientEmailNotification
  property_count: 3
  slug: docusign-esignature-recipient-email-notification
- name: RecipientViewRequest
  property_count: 11
  slug: docusign-esignature-recipient-view-request
- name: Recipients
  property_count: 10
  slug: docusign-esignature-recipients
- name: RecipientsUpdateSummary
  property_count: 1
  slug: docusign-esignature-recipients-update-summary
- name: SignHere
  property_count: 14
  slug: docusign-esignature-sign-here
- name: Signer
  property_count: 17
  slug: docusign-esignature-signer
- name: TemplateRole
  property_count: 7
  slug: docusign-esignature-template-role
- name: TemplateSummary
  property_count: 3
  slug: docusign-esignature-template-summary
- name: Text
  property_count: 23
  slug: docusign-esignature-text
- name: UserInfo
  property_count: 4
  slug: docusign-esignature-user-info
- name: ViewUrl
  property_count: 1
  slug: docusign-esignature-view-url
- name: Witness
  property_count: 5
  slug: docusign-esignature-witness
json_structures:
- name: Docusign Esignature Agent Structure
  property_count: 5
  slug: docusign-esignature-agent-structure
- name: Docusign Esignature Approve Structure
  property_count: 8
  slug: docusign-esignature-approve-structure
- name: Docusign Esignature Carbon Copy Structure
  property_count: 7
  slug: docusign-esignature-carbon-copy-structure
- name: Docusign Esignature Certified Delivery Structure
  property_count: 5
  slug: docusign-esignature-certified-delivery-structure
- name: Docusign Esignature Checkbox Structure
  property_count: 11
  slug: docusign-esignature-checkbox-structure
- name: Docusign Esignature Composite Template Structure
  property_count: 3
  slug: docusign-esignature-composite-template-structure
- name: Docusign Esignature Custom Fields Structure
  property_count: 2
  slug: docusign-esignature-custom-fields-structure
- name: Docusign Esignature Date Signed Structure
  property_count: 9
  slug: docusign-esignature-date-signed-structure
- name: Docusign Esignature Date Tab Structure
  property_count: 9
  slug: docusign-esignature-date-tab-structure
- name: Docusign Esignature Decline Structure
  property_count: 9
  slug: docusign-esignature-decline-structure
- name: Docusign Esignature Document Structure
  property_count: 10
  slug: docusign-esignature-document-structure
- name: Docusign Esignature Editor Structure
  property_count: 5
  slug: docusign-esignature-editor-structure
- name: Docusign Esignature Email Tab Structure
  property_count: 9
  slug: docusign-esignature-email-tab-structure
- name: Docusign Esignature Envelope Definition Structure
  property_count: 9
  slug: docusign-esignature-envelope-definition-structure
- name: Docusign Esignature Envelope Document Structure
  property_count: 9
  slug: docusign-esignature-envelope-document-structure
- name: Docusign Esignature Envelope Documents Result Structure
  property_count: 2
  slug: docusign-esignature-envelope-documents-result-structure
- name: Docusign Esignature Envelope Recipient Tabs Structure
  property_count: 15
  slug: docusign-esignature-envelope-recipient-tabs-structure
- name: Docusign Esignature Envelope Structure
  property_count: 24
  slug: docusign-esignature-envelope-structure
- name: Docusign Esignature Envelope Summary Structure
  property_count: 4
  slug: docusign-esignature-envelope-summary-structure
- name: Docusign Esignature Envelope Template Results Structure
  property_count: 8
  slug: docusign-esignature-envelope-template-results-structure
- name: Docusign Esignature Envelope Template Structure
  property_count: 15
  slug: docusign-esignature-envelope-template-structure
- name: Docusign Esignature Envelope Update Summary Structure
  property_count: 5
  slug: docusign-esignature-envelope-update-summary-structure
- name: Docusign Esignature Envelopes Information Structure
  property_count: 7
  slug: docusign-esignature-envelopes-information-structure
- name: Docusign Esignature Error Details Structure
  property_count: 2
  slug: docusign-esignature-error-details-structure
- name: Docusign Esignature Event Notification Structure
  property_count: 12
  slug: docusign-esignature-event-notification-structure
- name: Docusign Esignature Formula Tab Structure
  property_count: 10
  slug: docusign-esignature-formula-tab-structure
- name: Docusign Esignature Full Name Structure
  property_count: 9
  slug: docusign-esignature-full-name-structure
- name: Docusign Esignature In Person Signer Structure
  property_count: 7
  slug: docusign-esignature-in-person-signer-structure
- name: Docusign Esignature Initial Here Structure
  property_count: 10
  slug: docusign-esignature-initial-here-structure
- name: Docusign Esignature Intermediary Structure
  property_count: 5
  slug: docusign-esignature-intermediary-structure
- name: Docusign Esignature List Tab Structure
  property_count: 11
  slug: docusign-esignature-list-tab-structure
- name: Docusign Esignature Note Tab Structure
  property_count: 8
  slug: docusign-esignature-note-tab-structure
- name: Docusign Esignature Notification Structure
  property_count: 3
  slug: docusign-esignature-notification-structure
- name: Docusign Esignature Number Tab Structure
  property_count: 9
  slug: docusign-esignature-number-tab-structure
- name: Docusign Esignature Radio Group Structure
  property_count: 5
  slug: docusign-esignature-radio-group-structure
- name: Docusign Esignature Recipient Email Notification Structure
  property_count: 3
  slug: docusign-esignature-recipient-email-notification-structure
- name: Docusign Esignature Recipient View Request Structure
  property_count: 11
  slug: docusign-esignature-recipient-view-request-structure
- name: Docusign Esignature Recipients Structure
  property_count: 10
  slug: docusign-esignature-recipients-structure
- name: Docusign Esignature Recipients Update Summary Structure
  property_count: 1
  slug: docusign-esignature-recipients-update-summary-structure
- name: Docusign Esignature Sign Here Structure
  property_count: 14
  slug: docusign-esignature-sign-here-structure
- name: Docusign Esignature Signer Structure
  property_count: 17
  slug: docusign-esignature-signer-structure
- name: Docusign Esignature Template Role Structure
  property_count: 7
  slug: docusign-esignature-template-role-structure
- name: Docusign Esignature Template Summary Structure
  property_count: 3
  slug: docusign-esignature-template-summary-structure
- name: Docusign Esignature Text Structure
  property_count: 23
  slug: docusign-esignature-text-structure
- name: Docusign Esignature User Info Structure
  property_count: 4
  slug: docusign-esignature-user-info-structure
- name: Docusign Esignature View Url Structure
  property_count: 1
  slug: docusign-esignature-view-url-structure
- name: Docusign Esignature Witness Structure
  property_count: 5
  slug: docusign-esignature-witness-structure
jsonld:
- class_count: 0
  name: Docusign Context
  property_count: 15
  slug: docusign-context
- class_count: 0
  name: Docusign Esignature Context
  property_count: 0
  slug: docusign-esignature-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Docusign
nav: Providers
network: true
overview: 'Docusign publishes 147 API contracts indexed on the [APIs.io](https://apis.io/) network, including Notary API, AccountBrands API, AccountConsumerDisclosures API, and 144 more. Tagged areas include E-Signature, DocuSign, Agreements, Contracts, and Digital Transaction Management.


  The Docusign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Docusign''s developer surface includes pricing, authentication, developer portal, support, Stack Overflow tag, FAQ, YouTube channel, and 48 more developer resources.'
plans:
- name: Docusign Plans Pricing
  plan_count: 6
  slug: docusign-plans-pricing
- name: Docusign Price Estimates
  plan_count: 0
  slug: docusign-price-estimates
random_paper: 20
rate_limits:
- limit_count: 4
  name: Docusign Rate Limits
  slug: docusign-rate-limits
rules:
- authorship: generated
  effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Docusign — asyncapi rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: docusign-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Docusign — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: docusign-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Docusign API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: docusign-spectral-rules
scopes:
- name: Docusign Scopes
  scope_count: 13
  slug: docusign-scopes
  summary_line: 13 scopes · authorizationCode/implicit
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.9
    catalog_earned_first_party: 12.0
    catalog_gap: 44.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 78.9
    contract_governance: 13.6
    contract_quality: 69.5
    developer_ergonomics: 75.0
    discoverability: 61.7
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 72.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 259
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/docusign/docusign-2026-06-20T180123.png
security:
- kind: authentication
  name: Docusign Authentication
  slug: docusign-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Docusign Domain Security
  slug: docusign-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: docusign
tags:
- E-Signature
- DocuSign
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Contract Lifecycle Management
- Contract Management
website: https://www.docusign.com/
---
