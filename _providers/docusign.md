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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 275
  human_in_the_loop: 7
  name: Docusign Agentic Access
  operation_count: 505
  slug: docusign-agentic-access
  summary_line: 505 operations · 275 acting · 7 human-in-the-loop
api_count: 134
apis:
- description: The Docusign Web Forms API facilitates generating semantic HTML forms around everyday contracts. It enables developers to embed and prefill forms from the systems they control, creating web form confi
  name: Docusign Web Forms API
  slug: docusign-web-forms-api
- description: The Docusign Notary API enables developers to manage remote online notary tasks programmatically. It provides capabilities for sending signature requests to notary groups, managing notary on-demand se
  name: Docusign Notary API
  slug: docusign-notary-api
- description: The Docusign Navigator API offers developers access to AI-extracted data from the Navigator smart agreement repository. It provides capabilities to analyze existing agreements, extract insights, and c
  name: Docusign Navigator API
  slug: docusign-navigator-api
- description: The Docusign Workspaces API allows developers to create, manage, and integrate Docusign Workspaces into their own applications, enabling structured, secure, and scalable agreement workflows. It provid
  name: Docusign Workspaces API
  slug: docusign-workspaces-api
- description: The Docusign CLM API enables developers to integrate contract lifecycle management workflow, document generation, and document management into Salesforce and custom applications. It provides access to
  name: Docusign CLM API
  slug: docusign-clm-api
- description: The Docusign Connected Fields API enables developers to validate envelope field data programmatically. It allows integration with extension apps to verify custom data in real-time within eSignature ag
  name: Docusign Connected Fields API
  slug: docusign-connected-fields-api
- description: The AcccountBrands resource provides methods that allow you to create and delete the account brand associated with an account. Branding allows you to add the look and feel of your organization's brand
  name: Docusign AccountBrands API
  slug: docusign-accountbrands-api
- description: The AccountConsumerDisclosures resource provides methods that allow you to retrieve the consumer disclosures associated with the account.
  name: Docusign AccountConsumerDisclosures API
  slug: docusign-accountconsumerdisclosures-api
- description: The CustomFields resource provides a method that enables you to retrieve the custom fields associated with an account. These fields can be used with your account's envelopes to record information abou
  name: Docusign AccountCustomFields API
  slug: docusign-accountcustomfields-api
- description: The AccountPasswordRules resource provides methods that allow you to obtain and update account password rules, as well as membership and account rules.
  name: Docusign AccountPasswordRules API
  slug: docusign-accountpasswordrules-api
- description: The AccountPermissionProfiles resource provides methods that allow you to manage permission profiles.
  name: Docusign AccountPermissionProfiles API
  slug: docusign-accountpermissionprofiles-api
- description: The Accounts resource provides methods that allow you to create, delete, and manage your accounts.
  name: Docusign Accounts API
  slug: docusign-accounts-api
- description: The AccountSealProviders API from Docusign — 1 operation(s) for accountsealproviders.
  name: Docusign AccountSealProviders API
  slug: docusign-accountsealproviders-api
- description: Methods and objects to get account information.
  name: Docusign AccountSettingsExport API
  slug: docusign-accountsettingsexport-api
- description: Methods and objects to update account settings.
  name: Docusign AccountSettingsImport API
  slug: docusign-accountsettingsimport-api
- description: This resource provides information on the Standards Based Signature providers that have been provisioned for this account.
  name: Docusign AccountSignatureProviders API
  slug: docusign-accountsignatureproviders-api
- description: The AccountTabSettings resource provides methods that allow you to manage tab settings for an account.
  name: Docusign AccountTabSettings API
  slug: docusign-accounttabsettings-api
- description: The AccountWatermarks resource provides methods that allow you to obtain, preview and update watermark information.
  name: Docusign AccountWatermarks API
  slug: docusign-accountwatermarks-api
- description: '**Note:** This information is provided for legacy reference only. Please see our supported forms of authentication referenced below and use our [REST API Authentication Guides](https://developers.docu'
  name: Docusign Authentication API
  slug: docusign-authentication-api
- description: The Billing resource provides methods that allow you to manage the billing plans,associated with an account.
  name: Docusign BillingPlans API
  slug: docusign-billingplans-api
- description: The ChunkedUploads resource provides methods to complete integrity checks, and to add, commit, retrieve, initiate and delete chunked uploads.
  name: Docusign ChunkedUploads API
  slug: docusign-chunkeduploads-api
- description: The ClickWraps API from Docusign — 12 operation(s) for clickwraps.
  name: Docusign ClickWraps API
  slug: docusign-clickwraps-api
- description: The ClosingStatuses API from Docusign — 1 operation(s) for closingstatuses.
  name: Docusign ClosingStatuses API
  slug: docusign-closingstatuses-api
- description: The CloudStorage resource provides methods that allow you to list files stored on your cloud storage provider.
  name: Docusign CloudStorage API
  slug: docusign-cloudstorage-api
- description: 'The CloudStorageProviders resource provides methods that allow you to manage the cloud storage providers associate with an account. The following providers are supported: * Google Drive * Dropbox * Bo'
  name: Docusign CloudStorageProviders API
  slug: docusign-cloudstorageproviders-api
- description: The Comments API from Docusign — 1 operation(s) for comments.
  name: Docusign Comments API
  slug: docusign-comments-api
- description: The ConnectConfigurations resource methods enable you to configure the DocuSign Connect service associated with an account.
  name: Docusign ConnectConfigurations API
  slug: docusign-connectconfigurations-api
- description: The ConnectEvents resource provides methods that allow you to read, delete, and republish the connect logs associated with an envelope.
  name: Docusign ConnectEvents API
  slug: docusign-connectevents-api
- description: The ConnectSecret API from Docusign — 2 operation(s) for connectsecret.
  name: Docusign ConnectSecret API
  slug: docusign-connectsecret-api
- description: The Contacts resource provides methods that allow you to manage contacts.
  name: Docusign Contacts API
  slug: docusign-contacts-api
- description: The ContactSides API from Docusign — 1 operation(s) for contactsides.
  name: Docusign ContactSides API
  slug: docusign-contactsides-api
- description: The Countries API from Docusign — 1 operation(s) for countries.
  name: Docusign Countries API
  slug: docusign-countries-api
- description: The Currencies API from Docusign — 1 operation(s) for currencies.
  name: Docusign Currencies API
  slug: docusign-currencies-api
- description: The CustomTabs resource provides methods that allow you create and manage custom tabs based on the existing DocuSign tabs. You can create a tab with pre-defined properties, such as a text tab with a c
  name: Docusign CustomTabs API
  slug: docusign-customtabs-api
- description: The DataSet resource provides methods that allow you to fetch organization event data. The `dataSet` path parameter must be set to `monitor`.
  name: Docusign DataSet API
  slug: docusign-dataset-api
- description: The DocumentResponsiveHtmlPreview API from Docusign — 1 operation(s) for documentresponsivehtmlpreview.
  name: Docusign DocumentResponsiveHtmlPreview API
  slug: docusign-documentresponsivehtmlpreview-api
- description: Methods to grant access, delete, and get information, including contents, to a document.
  name: Docusign Documents API
  slug: docusign-documents-api
- description: The ENoteConfigurations resource provides methods that allow you to manage information for the eNote eOriginal integration.
  name: Docusign ENoteConfigurations API
  slug: docusign-enoteconfigurations-api
- description: The EnvelopeAttachments resource provides methods that allow you to manage attachments.
  name: Docusign EnvelopeAttachments API
  slug: docusign-envelopeattachments-api
- description: The EnvelopeConsumerDisclosures resource provides a method that allows you to retrieve the consumer disclosure for an envelope.
  name: Docusign EnvelopeConsumerDisclosures API
  slug: docusign-envelopeconsumerdisclosures-api
- description: The EnvelopeCustomFields resource provides methods that allow you manage custom fields in an envelope. Custom fields can be used in the envelopes for your account to record information about the envel
  name: Docusign EnvelopeCustomFields API
  slug: docusign-envelopecustomfields-api
- description: The EnvelopeDocumentFields resource provides methods that allow you to manage custom fields on a document. You can create custom versions of standard fields that combine of field properties, such as f
  name: Docusign EnvelopeDocumentFields API
  slug: docusign-envelopedocumentfields-api
- description: The EnvelopeDocumentHtmlDefinitions API from Docusign — 1 operation(s) for envelopedocumenthtmldefinitions.
  name: Docusign EnvelopeDocumentHtmlDefinitions API
  slug: docusign-envelopedocumenthtmldefinitions-api
- description: Manage documents within envelopes including adding, retrieving, and deleting documents attached to envelopes.
  name: Docusign EnvelopeDocuments API
  slug: docusign-envelopedocuments-api
- description: The EnvelopeDocumentTabs resource provides methods that allow you to manage various tabs in envelopes. For a complete list of options see the following Properties section.
  name: Docusign EnvelopeDocumentTabs API
  slug: docusign-envelopedocumenttabs-api
- description: The Envelope Documents Visibility resource provides methods that manage document views and insights in an envelope.
  name: Docusign EnvelopeDocumentVisibility API
  slug: docusign-envelopedocumentvisibility-api
- description: The EnvelopeEmailSettings provide methods that allow you to manage the email override settings for an envelope. Email override settings change the reply to email address, name, or the BCC for email ar
  name: Docusign EnvelopeEmailSettings API
  slug: docusign-envelopeemailsettings-api
- description: The EnvelopeFormData resource provides methods that manage forms in an envelope.
  name: Docusign EnvelopeFormData API
  slug: docusign-envelopeformdata-api
- description: The EnvelopeHtmlDefinitions API from Docusign — 1 operation(s) for envelopehtmldefinitions.
  name: Docusign EnvelopeHtmlDefinitions API
  slug: docusign-envelopehtmldefinitions-api
- description: The EnvelopeLocks resource provides methods that allow you to manage locks on an envelope. You can lock the envelope, and set the time until the lock expires, to prevent users or recipients from acces
  name: Docusign EnvelopeLocks API
  slug: docusign-envelopelocks-api
- description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The EnvelopeRecipients resource '
  name: Docusign EnvelopeRecipients API
  slug: docusign-enveloperecipients-api
- description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The EnvelopeRecipientTabs resour'
  name: Docusign EnvelopeRecipientTabs API
  slug: docusign-enveloperecipienttabs-api
- description: Create, send, and manage envelopes. An envelope is the fundamental unit of a DocuSign transaction, containing the documents to be signed, the recipients who will sign them, and the workflow rules.
  name: Docusign Envelopes API
  slug: docusign-envelopes-api
- description: The EnvelopeTemplates resource provides methods that allow you to add and delete templates on envelopes and documents.
  name: Docusign EnvelopeTemplates API
  slug: docusign-envelopetemplates-api
- description: Generate URL tokens for embedded signing, sending, and recipient views to integrate DocuSign experiences directly into your application.
  name: Docusign EnvelopeViews API
  slug: docusign-envelopeviews-api
- description: This resource provides a method that returns a list of the eSignature permission profiles that the current user can assign to a new member.
  name: Docusign ESignPermissionProfiles API
  slug: docusign-esignpermissionprofiles-api
- description: Methods to manage eSignature users in an account.
  name: Docusign eSignUserManagement API
  slug: docusign-esignusermanagement-api
- description: The ExternalFormFillSessions API from Docusign — 1 operation(s) for externalformfillsessions.
  name: Docusign ExternalFormFillSessions API
  slug: docusign-externalformfillsessions-api
- description: Information about field sets.
  name: Docusign Fields API
  slug: docusign-fields-api
- description: The FinancingTypes API from Docusign — 1 operation(s) for financingtypes.
  name: Docusign FinancingTypes API
  slug: docusign-financingtypes-api
- description: The Folders resource provides methods that allow you to view contents of folders on the account and move envelopes between folders.
  name: Docusign Folders API
  slug: docusign-folders-api
- description: This section shows you how to retrieve a form's details.
  name: Docusign FormDetails API
  slug: docusign-formdetails-api
- description: With the appropriate permissions, form administrators at your company can create form groups, or curated set of forms gathered from the association **form libraries** to which DocuSign provides access
  name: Docusign FormGroups API
  slug: docusign-formgroups-api
- description: The FormLibraries API from Docusign — 2 operation(s) for formlibraries.
  name: Docusign FormLibraries API
  slug: docusign-formlibraries-api
- description: The FormProviders API from Docusign — 1 operation(s) for formproviders.
  name: Docusign FormProviders API
  slug: docusign-formproviders-api
- description: The GroupBrands resource provides methods that allow you to manage
  name: Docusign GroupBrands API
  slug: docusign-groupbrands-api
- description: The Groups resource provides methods that allow you to manage groups for the account. Groups can be used to help manage users by associating users with a group. A group can be associated with a Permis
  name: Docusign Groups API
  slug: docusign-groups-api
- description: The GroupUsers resource provides methods that allow you to manage the users in a group.
  name: Docusign GroupUsers API
  slug: docusign-groupusers-api
- description: Methods to get a list of identity providers.
  name: Docusign IdentityProviders API
  slug: docusign-identityproviders-api
- description: The IdentityVerifications API from Docusign — 1 operation(s) for identityverifications.
  name: Docusign IdentityVerifications API
  slug: docusign-identityverifications-api
- description: The Invoices resource provides methods that allow you to manage the invoices for an account.
  name: Docusign Invoices API
  slug: docusign-invoices-api
- description: Methods to manage multi-product users in an account.
  name: Docusign MultiProductUserManagement API
  slug: docusign-multiproductusermanagement-api
- description: The NotaryJournals API from Docusign — 1 operation(s) for notaryjournals.
  name: Docusign NotaryJournals API
  slug: docusign-notaryjournals-api
- description: The `Offices` resource enables you to create and manage offices for your company. You can also retrieve the number and type of objects that reference an office.
  name: Docusign Offices API
  slug: docusign-offices-api
- description: Methods for working with organizations.
  name: Docusign Organization API
  slug: docusign-organization-api
- description: In the console, these are the values that can appear on a room's **Details** tab in the **Origin of lead** field.
  name: Docusign OriginsOfLeads API
  slug: docusign-originsofleads-api
- description: The PaymentGatewayAccounts API from Docusign — 1 operation(s) for paymentgatewayaccounts.
  name: Docusign PaymentGatewayAccounts API
  slug: docusign-paymentgatewayaccounts-api
- description: The Payments resource provides methods that allow you to manage payments for an account. These calls can only be used by users with account administrator privileges.
  name: Docusign Payments API
  slug: docusign-payments-api
- description: The PowerFormData resource provides a method to access power form data.
  name: Docusign PowerFormData API
  slug: docusign-powerformdata-api
- description: The PowerForms resource provides methods that allow you to manage power forms.
  name: Docusign PowerForms API
  slug: docusign-powerforms-api
- description: In the console, these are the values that can appear on a room's **Details** tab in the **Property type** field.
  name: Docusign PropertyTypes API
  slug: docusign-propertytypes-api
- description: Manage envelope recipients including signers, carbon copy recipients, certified deliveries, and other recipient types.
  name: Docusign Recipients API
  slug: docusign-recipients-api
- description: The Regions API from Docusign — 3 operation(s) for regions.
  name: Docusign Regions API
  slug: docusign-regions-api
- description: The RequestLogs resource provide methods that allow you to retrieve and delete the API request log files. The log files contain the API requests associated with your integration. They can aid you in t
  name: Docusign RequestLogs API
  slug: docusign-requestlogs-api
- description: Methods to get a list of reserved domains.
  name: Docusign ReservedDomains API
  slug: docusign-reserveddomains-api
- description: The Resources resource provides a method which retrieves the base resources that are available.
  name: Docusign Resources API
  slug: docusign-resources-api
- description: The ResponsiveHtmlPreview API from Docusign — 1 operation(s) for responsivehtmlpreview.
  name: Docusign ResponsiveHtmlPreview API
  slug: docusign-responsivehtmlpreview-api
- description: Each role is associated with specific permissions. Each new member is assigned a role when you create them, automatically granting them the permissions associated with that role. Roles use the followi
  name: Docusign Roles API
  slug: docusign-roles-api
- description: The RoomContactTypes API from Docusign — 1 operation(s) for roomcontacttypes.
  name: Docusign RoomContactTypes API
  slug: docusign-roomcontacttypes-api
- description: The RoomFolders API from Docusign — 1 operation(s) for roomfolders.
  name: Docusign RoomFolders API
  slug: docusign-roomfolders-api
- description: A room can hold documents, envelopes, a list of tasks comprising a workflow, and other related information. You can invite others to this space and assign them permissions on a per-room basis.
  name: Docusign Rooms API
  slug: docusign-rooms-api
- description: You can use a room template to set the transaction side and task lists for rooms. For example, a broker can create a room template for agents to use. You can enable the room template for all regions a
  name: Docusign RoomTemplates API
  slug: docusign-roomtemplates-api
- description: The SellerDecisionTypes API from Docusign — 1 operation(s) for sellerdecisiontypes.
  name: Docusign SellerDecisionTypes API
  slug: docusign-sellerdecisiontypes-api
- description: The Service Information API from Docusign — 1 operation(s) for service information.
  name: Docusign Service Information API
  slug: docusign-service-information-api
- description: The SigningGroups resource provides methods that allow you manage signing groups. Signing Groups allow you to create a group of people to which an envelope is sent. Any member of that group can open a
  name: Docusign SigningGroups API
  slug: docusign-signinggroups-api
- description: The SigningGroupUsers resource provides methods that allow you to manage users in Signing Groups.
  name: Docusign SigningGroupUsers API
  slug: docusign-signinggroupusers-api
- description: Methods to import users.
  name: Docusign SingleAccountUserImport API
  slug: docusign-singleaccountuserimport-api
- description: The SpecialCircumstanceTypes API from Docusign — 1 operation(s) for specialcircumstancetypes.
  name: Docusign SpecialCircumstanceTypes API
  slug: docusign-specialcircumstancetypes-api
- description: The States API from Docusign — 1 operation(s) for states.
  name: Docusign States API
  slug: docusign-states-api
- description: Manage tabs (fields) placed on documents for recipients to interact with during the signing process, including signature, date, text, and checkbox tabs.
  name: Docusign Tabs API
  slug: docusign-tabs-api
- description: Task date types are the options that appear in the **Due Date** drop-down list when you create a task by using the console.
  name: Docusign TaskDateTypes API
  slug: docusign-taskdatetypes-api
- description: The TaskLists API from Docusign — 2 operation(s) for tasklists.
  name: Docusign TaskLists API
  slug: docusign-tasklists-api
- description: If your administrator created room templates, those room templates may include task lists for you to use.
  name: Docusign TaskListTemplates API
  slug: docusign-tasklisttemplates-api
- description: The TaskResponsibilityTypes API from Docusign — 1 operation(s) for taskresponsibilitytypes.
  name: Docusign TaskResponsibilityTypes API
  slug: docusign-taskresponsibilitytypes-api
- description: The TaskStatuses API from Docusign — 1 operation(s) for taskstatuses.
  name: Docusign TaskStatuses API
  slug: docusign-taskstatuses-api
- description: The TemplateBulkRecipients resource provide methods that allow you manage the bulk recipient file for an template. The bulk recipient CSV (Comma Separated Value) file contains the list of recipient na
  name: Docusign TemplateBulkRecipients API
  slug: docusign-templatebulkrecipients-api
- description: The TemplateCustomFields resource provides methods that allow you manage custom fields in an template. Custom fields can be used in the templates for your account to record information about the templ
  name: Docusign TemplateCustomFields API
  slug: docusign-templatecustomfields-api
- description: The TemplateDocumentFields resource provides methods that allow you to manage custom fields on a document. You can create custom versions of standard fields that combine of field properties, such as f
  name: Docusign TemplateDocumentFields API
  slug: docusign-templatedocumentfields-api
- description: The TemplateDocumentHtmlDefinitions API from Docusign — 1 operation(s) for templatedocumenthtmldefinitions.
  name: Docusign TemplateDocumentHtmlDefinitions API
  slug: docusign-templatedocumenthtmldefinitions-api
- description: The TemplateDocumentResponsiveHtmlPreview API from Docusign — 1 operation(s) for templatedocumentresponsivehtmlpreview.
  name: Docusign TemplateDocumentResponsiveHtmlPreview API
  slug: docusign-templatedocumentresponsivehtmlpreview-api
- description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The TemplateDocuments resource p'
  name: Docusign TemplateDocuments API
  slug: docusign-templatedocuments-api
- description: The TemplateDocumentTabs API from Docusign — 2 operation(s) for templatedocumenttabs.
  name: Docusign TemplateDocumentTabs API
  slug: docusign-templatedocumenttabs-api
- description: The Template Document Visibility resource provides methods that allow views into envelope templates.
  name: Docusign TemplateDocumentVisibility API
  slug: docusign-templatedocumentvisibility-api
- description: The TemplateHtmlDefinitions API from Docusign — 1 operation(s) for templatehtmldefinitions.
  name: Docusign TemplateHtmlDefinitions API
  slug: docusign-templatehtmldefinitions-api
- description: The TemplateLocks resource provides methods that allow you to manage locks on an template. You can lock the template, and set the time until the lock expires, to prevent users from accessing and chang
  name: Docusign TemplateLocks API
  slug: docusign-templatelocks-api
- description: 'The TemplateRecipients resource allows you manage the recipients of an template. The exact parameters associated with a recipient depend on the recipient type. There are seven recipient types: Agents,'
  name: Docusign TemplateRecipients API
  slug: docusign-templaterecipients-api
- description: '<!-- resources aren''t rendered the same way as other pages. This is a little hack to make the headings work better --> <style> h1, h2, h3 { margin-top: 1em; } </style> The TemplateRecipientTabs resour'
  name: Docusign TemplateRecipientTabs API
  slug: docusign-templaterecipienttabs-api
- description: The TemplateResponsiveHtmlPreview API from Docusign — 1 operation(s) for templateresponsivehtmlpreview.
  name: Docusign TemplateResponsiveHtmlPreview API
  slug: docusign-templateresponsivehtmlpreview-api
- description: Create and manage reusable templates that define documents, recipients, tabs, and routing for common agreement workflows.
  name: Docusign Templates API
  slug: docusign-templates-api
- description: 'The TemplateViews resource provides a method returns a URL that you can embed into your application to provide access to the DocuSign UI. One template view is available: * Edit View - the DocuSign UI '
  name: Docusign TemplateViews API
  slug: docusign-templateviews-api
- description: The TimeZones API from Docusign — 1 operation(s) for timezones.
  name: Docusign TimeZones API
  slug: docusign-timezones-api
- description: The TransactionSides API from Docusign — 1 operation(s) for transactionsides.
  name: Docusign TransactionSides API
  slug: docusign-transactionsides-api
- description: The UserCustomSettings resource provides methods that allow you to manage the custom settings for a user. Custom settings are a flexible way to store and retrieve custom user information that can be u
  name: Docusign UserCustomSettings API
  slug: docusign-usercustomsettings-api
- description: Methods for exporting a user list.
  name: Docusign UserExport API
  slug: docusign-userexport-api
- description: Methods to import users. To ensure your CSV is properly formatted, use the [Sample Bulk Add CSV file](https://admin.docusign.com/static-resources/organization-user-import.csv) as a template. You can a
  name: Docusign UserImport API
  slug: docusign-userimport-api
- description: The UserProfiles resource provides methods that allow you to manage a user's profile.
  name: Docusign UserProfiles API
  slug: docusign-userprofiles-api
- description: Methods to manage users in an account.
  name: Docusign Users API
  slug: docusign-users-api
- description: The UserSignatures resource provides methods that allow you manage the intials and signature images for a user.
  name: Docusign UserSignatures API
  slug: docusign-usersignatures-api
- description: The UserSocialAccountLogins resource provides methods that allow you to manage the social login accounts for a user.
  name: Docusign UserSocialAccountLogins API
  slug: docusign-usersocialaccountlogins-api
- description: Methods to get information about workflow instances.
  name: Docusign WorkflowInstanceManagement API
  slug: docusign-workflowinstancemanagement-api
- description: Returns the history of the workflow instance steps.
  name: Docusign WorkflowManagement API
  slug: docusign-workflowmanagement-api
- description: Method to trigger a workflow.
  name: Docusign WorkflowTrigger API
  slug: docusign-workflowtrigger-api
- description: The WorkspaceItems resource provides methods that allow you to manage workspace items.
  name: Docusign WorkspaceItems API
  slug: docusign-workspaceitems-api
- description: The Workspaces resource provides methods that allow you to manage workspaces.
  name: Docusign Workspaces API
  slug: docusign-workspaces-api
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
artifact_total: 333
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
  name: DocuSign eSignature REST API
  slug: open-docusign-esignature
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docusign-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docusign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docusign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/docusign-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/docusign/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-bulk-send-from-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-correct-recipient-email-and-resend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-create-template-and-send-envelope-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-download-completed-documents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-draft-envelope-add-recipients-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-draft-envelope-sender-view-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-embedded-signing-view-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-find-template-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-inspect-recipient-tabs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-list-sent-envelopes-and-check-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-multi-signer-routing-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-prefill-text-tabs-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-resend-envelope-to-pending-recipients-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-send-envelope-and-track-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-send-envelope-with-custom-fields-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-send-from-template-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/docusign-update-template-recipients-workflow.yml
- group: design
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
- name: Docusign Finops
  service_category: E-Signature
  slug: docusign-finops
graphqls:
- description: DocuSign does not currently offer a native GraphQL API. The platform exposes its functionality through a suite of REST APIs — including the eSignature REST API, Admin API, Click API, Maestro API, Moni
  name: DocuSign GraphQL
  slug: docusign-graphql
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
overview: 'Docusign publishes 129 APIs on the [APIs.io](https://apis.io/) network, including Workspaces API, AccountBrands API, AccountConsumerDisclosures API, and 126 more. Tagged areas include Agreements, Contracts, Digital Transaction Management, Documents, and Electronic Signatures.


  The Docusign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Docusign''s developer surface includes authentication, developer portal, support, Stack Overflow tag, FAQ, YouTube channel, changelog, and 43 more developer resources.'
plans:
- name: Docusign Plans Pricing
  plan_count: 4
  slug: docusign-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 4
  name: Docusign Rate Limits
  slug: docusign-rate-limits
rules:
- name: Docusign API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: docusign-asyncapi-spectral-rules
- name: Docusign API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: docusign-jsonschema-spectral-rules
- name: Docusign API Rules
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
  composite: 68.1
  delta: -3.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 77.4
    developer_ergonomics: 63.0
    discoverability: 59.3
    governance: 47.9
    operational_transparency: 78.9
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 128
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docusign/refs/heads/main/screenshots/docusign-2026-06-20T180123.png
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
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
website: https://developers.docusign.com/
---
