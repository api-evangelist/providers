---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 1956
  human_in_the_loop: 18
  name: Azure Ad Agentic Access
  operation_count: 4496
  slug: azure-ad-agentic-access
  summary_line: 4496 operations · 1956 acting · 18 human-in-the-loop
api_count: 9
apis:
- description: Business-to-consumer identity management solution.
  name: Azure AD B2C API
  slug: azure-ad-b2c-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The admin.peopleAdminSettings API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for admin.peopleadminsettings.
  name: Microsoft Entra ID (formerly Azure AD) Admin.people Admin Settings API
  phrasing_intents:
  - id: admin_GetPerson
    intent: Get the organization's people admin settings
    question: Where can I see all the people settings an admin has configured for our organization?
  - id: admin.person_GetItemInsight
    intent: Get the organization's item insights privacy settings
    question: Are item insights turned on for our organization right now?
  - id: admin.person_UpdateItemInsight
    intent: Change who can see item insights in the organization
    question: How do I turn off item insights for the entire organization?
  - id: admin.person_DeleteItemInsight
    intent: Remove the organization's item insights settings
    question: Can I delete the item insights settings object for the whole organization?
  - id: admin.person_ListProfileCardProperty
    intent: List custom profile card properties
    question: Which extra attributes have we added to people's profile cards?
  - id: admin.person_CreateProfileCardProperty
    intent: Add a property to the organization's profile card
    question: How do I show an extra directory attribute on everyone's profile card?
  - id: admin.person_GetProfileCardProperty
    intent: Get one profile card property
    question: How is a specific attribute configured on our profile cards?
  - id: admin.person_UpdateProfileCardProperty
    intent: Update a profile card property
    question: Can I hide an existing profile card field without deleting it?
  phrasing_ops: 27
  slug: azure-ad-admin-peopleadminsettings-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreement API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for agreements.agreement.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement API
  phrasing_intents:
  - id: agreement_ListAgreement
    intent: List terms of use agreements
    question: What terms of use agreements have we set up in Microsoft Entra ID?
  - id: agreement_CreateAgreement
    intent: Create a terms of use agreement
    question: How do I create a new terms of use that users must accept?
  - id: agreement_GetAgreement
    intent: Get a terms of use agreement
    question: What are the settings of a specific terms of use agreement?
  - id: agreement_UpdateAgreement
    intent: Update a terms of use agreement
    question: How do I make users re-accept an existing agreement on a schedule?
  - id: agreement_DeleteAgreement
    intent: Delete a terms of use agreement
    question: Can I permanently remove a terms of use agreement from the tenant?
  phrasing_ops: 5
  slug: azure-ad-agreements-agreement-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreementAcceptance API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for agreements.agreementacceptance.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement Acceptance API
  phrasing_intents:
  - id: agreement_ListAcceptance
    intent: List who accepted a terms of use agreement
    question: Which users have accepted our terms of use agreement?
  - id: agreement_CreateAcceptance
    intent: Record an acceptance of an agreement
    question: How do I add an acceptance record to a terms of use agreement?
  - id: agreement_GetAcceptance
    intent: Get one acceptance of an agreement
    question: When did a particular user accept the terms of use, and on which device?
  - id: agreement_UpdateAcceptance
    intent: Update an agreement acceptance
    question: How do I change the state of an existing agreement acceptance?
  - id: agreement_DeleteAcceptance
    intent: Delete an agreement acceptance
    question: How do I remove an acceptance record from a terms of use agreement?
  - id: agreement.acceptance_GetCount
    intent: Count acceptances of an agreement
    question: How many people have accepted a terms of use agreement?
  phrasing_ops: 6
  slug: azure-ad-agreements-agreementacceptance-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreementFile API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for agreements.agreementfile.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement File API
  phrasing_intents:
  - id: agreement_GetFile
    intent: Get a terms of use agreement's default file
    question: How do I see the default file attached to a terms of use agreement, including its language?
  - id: agreement_UpdateFile
    intent: Update an agreement's default file
    question: Can I replace the localizations on an agreement's default file?
  - id: agreement_DeleteFile
    intent: Delete an agreement's default file
    question: Can I remove the default file from a terms of use agreement?
  - id: agreement.file_ListLocalization
    intent: List an agreement file's language versions
    question: Which languages is our terms of use agreement file available in?
  - id: agreement.file_CreateLocalization
    intent: Add a localized agreement file
    question: How do I add another language version of an agreement file?
  - id: agreement.file_GetLocalization
    intent: Get one localized agreement file
    question: What does a specific language version of our terms of use file contain?
  - id: agreement.file_UpdateLocalization
    intent: Update a localized agreement file
    question: Can I change the versions list on a localized agreement file?
  - id: agreement.file_DeleteLocalization
    intent: Delete a localized agreement file
    question: Can I remove one language version from a terms of use agreement?
  phrasing_ops: 15
  slug: azure-ad-agreements-agreementfile-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreementFileLocalization API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for agreements.agreementfilelocalization.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement File Localization API
  phrasing_intents:
  - id: agreement_ListFile
    intent: List a terms of use agreement's localized files
    question: Which language-specific PDFs are attached to a terms of use agreement in Entra?
  - id: agreement_CreateFile
    intent: Add a localized file to an agreement
    question: Can I add a new language version of the PDF to an existing terms of use agreement?
  - id: agreement_GetFile
    intent: Get one legacy localized file of an agreement
    question: How do I read a single language PDF from an agreement's deprecated files list?
  - id: agreement_UpdateFile
    intent: Update a localized file on an agreement
    question: How do I change the versions recorded on one language PDF of an agreement?
  - id: agreement_DeleteFile
    intent: Delete a localized file from an agreement
    question: Can I remove one language version of the PDF from a terms of use agreement?
  - id: agreement.file_ListVersion
    intent: List versions of a localized agreement file
    question: What customized versions exist for one language file of a terms of use agreement?
  - id: agreement.file_CreateVersion
    intent: Add a version to a localized agreement file
    question: Can I publish a new version of a localized terms of use file?
  - id: agreement.file_GetVersion
    intent: Get one version of a localized agreement file
    question: How do I read a specific version of a localized terms of use file?
  phrasing_ops: 12
  slug: azure-ad-agreements-agreementfilelocalization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Application registrations in Entra ID
  name: Microsoft Entra ID (formerly Azure AD) Applications API
  phrasing_intents:
  - id: listApplications
    intent: List app registrations
    question: Which applications are registered in our Microsoft Entra tenant?
  phrasing_ops: 1
  slug: azure-ad-applications-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.application.Actions API from Microsoft Entra ID (formerly Azure AD) — 14 operation(s) for applications.application.actions.
  name: Microsoft Entra ID (formerly Azure AD) Applications.application.Actions API
  phrasing_intents:
  - id: application_addKey
    intent: Add a certificate key credential to an app
    question: How do I roll an expiring certificate on an app registration automatically?
  - id: application_addPassword
    intent: Add a client secret to an app
    question: How do I generate a new client secret for my app registration?
  - id: application_checkMemberGroup
    intent: Check an app's membership in given groups
    question: Which of a list of groups does an application object belong to?
  - id: application_checkMemberObject
    intent: Check an app against directory object IDs
    question: Is an app a member of certain groups, admin units or roles by ID?
  - id: application_getMemberGroup
    intent: List all groups an app belongs to
    question: What groups is an app registration a member of?
  - id: application_getMemberObject
    intent: List groups, admin units and roles of an app
    question: Which groups, administrative units and directory roles include this application?
  - id: application_removeKey
    intent: Remove a certificate key credential from an app
    question: How do I retire an old certificate from an app registration after rolling it?
  - id: application_removePassword
    intent: Remove a client secret from an app
    question: How do I revoke a leaked client secret on my app registration?
  phrasing_ops: 14
  slug: azure-ad-applications-application-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.application API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for applications.application.
  name: Microsoft Entra ID (formerly Azure AD) Applications.application API
  phrasing_intents:
  - id: application_ListApplication
    intent: List app registrations in the organization
    question: Which app registrations exist in our Microsoft Entra tenant?
  - id: application_CreateApplication
    intent: Register a new application
    question: How do I register a new app in Microsoft Entra ID through the API?
  - id: application_GetApplication
    intent: Get an app registration by object ID
    question: How do I read an app registration's properties using its object ID?
  - id: application_UpdateApplication
    intent: Update or create an app registration by object ID
    question: How do I change the display name of an app registration using its object ID?
  - id: application_DeleteApplication
    intent: Delete an app registration by object ID
    question: How do I delete an app registration when I have its object ID?
  - id: application_GetLogo
    intent: Download an application's logo
    question: How do I download the main logo image of an app registration?
  - id: application_SetLogo
    intent: Upload an application's logo
    question: How do I upload a new logo for an app registration?
  - id: application_DeleteLogo
    intent: Remove an application's logo
    question: How do I remove the logo from an app registration?
  phrasing_ops: 15
  slug: azure-ad-applications-application-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.application.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for applications.application.functions.
  name: Microsoft Entra ID (formerly Azure AD) Applications.application.Functions API
  phrasing_intents:
  - id: application_delta
    intent: Track changes to app registrations
    question: How can I sync only the applications that were created, updated or deleted since my last run?
  phrasing_ops: 1
  slug: azure-ad-applications-application-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.appManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.appmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.app Management Policy API
  phrasing_intents:
  - id: application_ListAppManagementPolicy
    intent: List app management policies applied to an app
    question: Which app management policies are applied to one of our application registrations?
  - id: application.appManagementPolicy_DeleteAppManagementPolicyGraphBPreRef
    intent: Unassign a specific app management policy by path
    question: How do I detach one app management policy from an application using the policy's ID in the URL?
  - id: application.appManagementPolicy_GetCount
    intent: Count app management policies on an app
    question: How many app management policies are assigned to a given application?
  - id: application_ListAppManagementPolicyGraphBPreRef
    intent: List references to an app's management policies
    question: Can I get just the reference links for the app management policies on an application?
  - id: application_CreateAppManagementPolicyGraphBPreRef
    intent: Assign an app management policy to an app
    question: How do I apply an app management policy to an application so it overrides the tenant default?
  - id: application_DeleteAppManagementPolicyGraphBPreRef
    intent: Unassign an app management policy by reference
    question: Can I remove an app management policy from an app by passing the policy's @id reference as a query parameter?
  phrasing_ops: 6
  slug: azure-ad-applications-appmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 17 operation(s) for applications.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Applications.directory Object API
  phrasing_intents:
  - id: application_GetCreatedOnBehalfGraphOPre
    intent: See who an app registration was created on behalf of
    question: Which user or object was an Entra app registration created on behalf of?
  - id: application_ListOwner
    intent: List an application's owners
    question: Who owns a particular app registration in Microsoft Entra ID?
  - id: application.owner_DeleteDirectoryObjectGraphBPreRef
    intent: Remove a specific owner from an application
    question: Can I take a named owner off an app registration by that owner's object ID in the path?
  - id: application_GetOwnerAsAppRoleAssignment
    intent: Get an app owner cast as an app role assignment
    question: Can I read one application owner specifically as an app role assignment object?
  - id: application_GetOwnerAsEndpoint
    intent: Get an app owner cast as an endpoint
    question: Can I fetch a single application owner typed as an endpoint object?
  - id: application_GetOwnerAsServicePrincipal
    intent: Get an app owner that is a service principal
    question: Can I read one of my app's owners as a service principal rather than a generic object?
  - id: application_GetOwnerAsUser
    intent: Get an app owner that is a user
    question: Can I read one of my app's owners as a full user profile?
  - id: application.owner_GetCount
    intent: Count an application's owners
    question: How many owners does an app registration have in total?
  phrasing_ops: 19
  slug: azure-ad-applications-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.extensionProperty API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for applications.extensionproperty.
  name: Microsoft Entra ID (formerly Azure AD) Applications.extension Property API
  phrasing_intents:
  - id: application_ListExtensionProperty
    intent: List an app's directory extension definitions
    question: Which directory extensions has this application defined?
  - id: application_CreateExtensionProperty
    intent: Define a new directory extension on an app
    question: How do I add a custom attribute for users through an app's directory extension?
  - id: application_GetExtensionProperty
    intent: Get one directory extension definition
    question: What data type and target objects does a specific directory extension have?
  - id: application_UpdateExtensionProperty
    intent: Update a directory extension definition
    question: How do I change the target objects of an existing directory extension?
  - id: application_DeleteExtensionProperty
    intent: Delete a directory extension definition
    question: How do I remove a directory extension that an app defined?
  - id: application.extensionProperty_GetCount
    intent: Count an app's directory extensions
    question: How many directory extensions has an application defined?
  phrasing_ops: 6
  slug: azure-ad-applications-extensionproperty-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.federatedIdentityCredential API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.federatedidentitycredential.
  name: Microsoft Entra ID (formerly Azure AD) Applications.federated Identity Credential API
  phrasing_intents:
  - id: application_ListFederatedIdentityCredential
    intent: List an app's federated identity credentials
    question: Which external identity providers does my app registration trust for workload identity federation?
  - id: application_CreateFederatedIdentityCredential
    intent: Add a federated identity credential to an app
    question: How do I let an external CI pipeline get tokens for my app without storing a secret?
  - id: application_GetFederatedIdentityCredential
    intent: Get a federated identity credential by ID
    question: What issuer and subject are set on one federated credential of my app?
  - id: application_UpdateFederatedIdentityCredential
    intent: Upsert a federated identity credential by ID
    question: How do I change the subject on an existing federated credential identified by its ID?
  - id: application_DeleteFederatedIdentityCredential
    intent: Delete a federated identity credential by ID
    question: How do I stop an external workload from getting tokens for my app?
  - id: application.federatedIdentityCredential_GetGraphBPreName
    intent: Get a federated identity credential by name
    question: Can I read a federated credential using the name I gave it instead of its ID?
  - id: application.federatedIdentityCredential_UpdateGraphBPreName
    intent: Upsert a federated identity credential by name
    question: How do I create or update a federated credential addressed by its name?
  - id: application.federatedIdentityCredential_DeleteGraphBPreName
    intent: Delete a federated identity credential by name
    question: How do I delete a federated credential when I only know its name?
  phrasing_ops: 9
  slug: azure-ad-applications-federatedidentitycredential-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.homeRealmDiscoveryPolicy API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for applications.homerealmdiscoverypolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.home Realm Discovery Policy API
  phrasing_intents:
  - id: application_ListHomeRealmDiscoveryPolicy
    intent: List an application's home realm discovery policies
    question: Which home realm discovery policies are attached to my app registration?
  - id: application_GetHomeRealmDiscoveryPolicy
    intent: Get one home realm discovery policy on an app
    question: Can I read a single home realm discovery policy assigned to an application?
  - id: application.homeRealmDiscoveryPolicy_GetCount
    intent: Count an application's home realm discovery policies
    question: How many home realm discovery policies does an application have?
  phrasing_ops: 3
  slug: azure-ad-applications-homerealmdiscoverypolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.synchronization API from Microsoft Entra ID (formerly Azure AD) — 34 operation(s) for applications.synchronization.
  name: Microsoft Entra ID (formerly Azure AD) Applications.synchronization API
  phrasing_intents:
  - id: application_GetSynchronization
    intent: Get an application's provisioning sync setup
    question: What does the overall provisioning synchronization configuration look like for one of my Entra app registrations?
  - id: application_SetSynchronization
    intent: Replace an application's sync configuration
    question: How do I overwrite the entire synchronization object on an application in one request?
  - id: application_DeleteSynchronization
    intent: Remove an application's sync configuration
    question: Can I tear down the whole provisioning synchronization setup on an application at once?
  - id: application.synchronization_ListJob
    intent: List an application's provisioning sync jobs
    question: Which provisioning jobs are set up to sync users into one of my applications?
  - id: application.synchronization_CreateJob
    intent: Create a provisioning sync job for an application
    question: How do I set up a new provisioning job for an application from one of its sync templates?
  - id: application.synchronization_GetJob
    intent: Get one provisioning sync job
    question: What is the current status and schedule of a specific provisioning job on my app?
  - id: application.synchronization_UpdateJob
    intent: Update a provisioning sync job
    question: Can I change the schedule of an existing provisioning job on my app?
  - id: application.synchronization_DeleteJob
    intent: Delete a provisioning sync job
    question: How do I permanently remove one provisioning job from an application?
  phrasing_ops: 56
  slug: azure-ad-applications-synchronization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.tokenIssuancePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.tokenissuancepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.token Issuance Policy API
  phrasing_intents:
  - id: application_ListTokenIssuancePolicy
    intent: List token issuance policies on an app
    question: Which token issuance policies are assigned to an application?
  - id: application.tokenIssuancePolicy_DeleteTokenIssuancePolicyGraphBPreRef
    intent: Unassign a token issuance policy by its ID
    question: How do I remove a specific token issuance policy from an application by the policy's ID?
  - id: application.tokenIssuancePolicy_GetCount
    intent: Count token issuance policies on an app
    question: How many token issuance policies does an application have assigned?
  - id: application_ListTokenIssuancePolicyGraphBPreRef
    intent: List token issuance policy references on an app
    question: Can I get only the reference links for an app's token issuance policies?
  - id: application_CreateTokenIssuancePolicyGraphBPreRef
    intent: Assign a token issuance policy to an app
    question: How do I apply a token issuance policy to an application?
  - id: application_DeleteTokenIssuancePolicyGraphBPreRef
    intent: Unassign a token issuance policy by reference
    question: Can I unassign a token issuance policy by passing its reference in the query string?
  phrasing_ops: 6
  slug: azure-ad-applications-tokenissuancepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.tokenLifetimePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.tokenlifetimepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.token Lifetime Policy API
  phrasing_intents:
  - id: application_ListTokenLifetimePolicy
    intent: List token lifetime policies assigned to an app
    question: Which token lifetime policy is assigned to an application, with its full settings?
  - id: application.tokenLifetimePolicy_DeleteTokenLifetimePolicyGraphBPreRef
    intent: Unassign a token lifetime policy from an app
    question: How do I remove a specific token lifetime policy from an application by the policy's ID?
  - id: application.tokenLifetimePolicy_GetCount
    intent: Count token lifetime policies on an app
    question: How many token lifetime policies are assigned to an application?
  - id: application_ListTokenLifetimePolicyGraphBPreRef
    intent: List token lifetime policy references on an app
    question: Can I get just the reference links of the token lifetime policies assigned to an app?
  - id: application_CreateTokenLifetimePolicyGraphBPreRef
    intent: Assign a token lifetime policy to an app
    question: How do I apply a custom token lifetime policy to an application in Entra ID?
  - id: application_DeleteTokenLifetimePolicyGraphBPreRef
    intent: Unassign a token lifetime policy by reference
    question: Can I remove a token lifetime policy from an app by passing the policy reference as a query parameter?
  phrasing_ops: 6
  slug: azure-ad-applications-tokenlifetimepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applicationTemplates.applicationTemplate.Actions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for applicationtemplates.applicationtemplate.actions.
  name: Microsoft Entra ID (formerly Azure AD) Application Templates.application Template.Actions API
  phrasing_intents:
  - id: applicationTemplate_instantiate
    intent: Add a gallery app to the directory from a template
    question: How do I add an app from the application gallery into my directory?
  phrasing_ops: 1
  slug: azure-ad-applicationtemplates-applicationtemplate-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applicationTemplates.applicationTemplate API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for applicationtemplates.applicationtemplate.
  name: Microsoft Entra ID (formerly Azure AD) Application Templates.application Template API
  phrasing_intents:
  - id: applicationTemplate_ListApplicationTemplate
    intent: Browse the Entra application gallery
    question: Which apps are available in the Microsoft Entra application gallery?
  - id: applicationTemplate_GetApplicationTemplate
    intent: Get one application gallery template
    question: How do I see the details of a single gallery app template, like its supported SSO modes?
  - id: applicationTemplate_GetCount
    intent: Count application gallery templates
    question: How many application templates are in the Entra gallery in total?
  phrasing_ops: 3
  slug: azure-ad-applicationtemplates-applicationtemplate-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 28 operation(s) for contacts.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.directory Object API
  phrasing_intents:
  - id: contact_ListDirectReport
    intent: List an organizational contact's direct reports
    question: Who reports directly to this external contact in our directory?
  - id: contact_GetDirectReport
    intent: Get one direct report of an organizational contact
    question: Can I look up a single direct report of an org contact by its object ID?
  - id: contact_GetDirectReportAsOrgContact
    intent: Get a contact's direct report cast as an org contact
    question: How do I read a direct report of an org contact when that report is itself an organizational contact?
  - id: contact_GetDirectReportAsUser
    intent: Get a contact's direct report cast as a user
    question: How do I get user properties for someone who reports to an organizational contact?
  - id: contact.directReport_GetCount
    intent: Count an organizational contact's direct reports
    question: How many people report directly to this organizational contact?
  - id: contact_ListDirectReportAsOrgContact
    intent: List a contact's direct reports that are org contacts
    question: Which of an org contact's direct reports are themselves organizational contacts?
  - id: contact.DirectReport_GetCountAsOrgContact
    intent: Count a contact's direct reports that are org contacts
    question: How many organizational contacts report to this contact?
  - id: contact_ListDirectReportAsUser
    intent: List a contact's direct reports that are users
    question: Which users in our tenant report to an organizational contact?
  phrasing_ops: 28
  slug: azure-ad-contacts-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.onPremisesSyncBehavior API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for contacts.onpremisessyncbehavior.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.on Premises Sync Behavior API
  phrasing_intents:
  - id: contact_GetOnPremisesSyncBehavior
    intent: Check an org contact's on-premises sync behavior
    question: Is a given organizational contact still managed from on-premises Active Directory or from the cloud?
  - id: contact_UpdateOnPremisesSyncBehavior
    intent: Switch an org contact to cloud management
    question: How do I move an organizational contact's source of authority from on-premises AD to the cloud?
  - id: contact_DeleteOnPremisesSyncBehavior
    intent: Remove an org contact's sync behavior setting
    question: Can I clear the on-premises sync behavior object from an organizational contact?
  phrasing_ops: 3
  slug: azure-ad-contacts-onpremisessyncbehavior-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.orgContact.Actions API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for contacts.orgcontact.actions.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.org Contact.Actions API
  phrasing_intents:
  - id: contact_checkMemberGroup
    intent: Check an org contact's membership in given groups
    question: How do I check whether an organizational contact belongs to any of a list of groups?
  - id: contact_checkMemberObject
    intent: Check an org contact's membership in given objects
    question: Can I test an organizational contact against a mixed list of groups, roles and admin units?
  - id: contact_getMemberGroup
    intent: List all groups an org contact belongs to
    question: What are all the group IDs an organizational contact is a member of?
  - id: contact_getMemberObject
    intent: List groups, roles and admin units of an org contact
    question: Which groups, administrative units and directory roles is an organizational contact part of?
  - id: contact_restore
    intent: Restore a deleted organizational contact
    question: How do I bring back an organizational contact that was recently deleted?
  - id: contact_retryServiceProvisioning
    intent: Retry provisioning for an org contact
    question: An organizational contact failed to provision to a service; can I retry it?
  - id: contact_getAvailableExtensionProperty
    intent: List directory extension properties available
    question: What directory extension properties are registered in our tenant, including from multitenant apps?
  - id: contact_getGraphBPreId
    intent: Look up directory objects by a list of IDs
    question: How can I resolve a batch of object IDs to their directory objects in one call?
  phrasing_ops: 9
  slug: azure-ad-contacts-orgcontact-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.orgContact API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for contacts.orgcontact.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.org Contact API
  phrasing_intents:
  - id: contact.orgContact_ListOrgContact
    intent: List organizational contacts
    question: Which external contacts are in our organization's directory?
  - id: contact.orgContact_GetOrgContact
    intent: Get an organizational contact
    question: How do I look up an external contact's email, phones and company?
  - id: contact.orgContact_UpdateOrgContact
    intent: Update an organizational contact
    question: How do I change an external contact's job title or department?
  - id: contact.orgContact_DeleteOrgContact
    intent: Delete an organizational contact
    question: How do I remove an external contact from our directory?
  - id: contact_GetCount
    intent: Count organizational contacts
    question: How many organizational contacts do we have?
  phrasing_ops: 5
  slug: azure-ad-contacts-orgcontact-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.orgContact.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for contacts.orgcontact.functions.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.org Contact.Functions API
  phrasing_intents:
  - id: contact_delta
    intent: Track changes to organizational contacts
    question: How do I get only the organizational contacts created, updated or deleted since my last sync?
  phrasing_ops: 1
  slug: azure-ad-contacts-orgcontact-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.serviceProvisioningError API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for contacts.serviceprovisioningerror.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.service Provisioning Error API
  phrasing_intents:
  - id: contact_ListServiceProvisioningError
    intent: List an org contact's provisioning errors
    question: What provisioning errors have federated services reported for an organizational contact?
  - id: contact.ServiceProvisioningError_GetCount
    intent: Count an org contact's provisioning errors
    question: How many service provisioning errors does an org contact have?
  phrasing_ops: 2
  slug: azure-ad-contacts-serviceprovisioningerror-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contracts.contract.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for contracts.contract.actions.
  name: Microsoft Entra ID (formerly Azure AD) Contracts.contract.Actions API
  phrasing_intents:
  - id: contract_checkMemberGroup
    intent: Check a partner contract's membership in given groups
    question: Which of a list of groups does a partner contract object belong to?
  - id: contract_checkMemberObject
    intent: Check a partner contract against directory object IDs
    question: Is a partner contract a member of certain groups, admin units or roles by ID?
  - id: contract_getMemberGroup
    intent: List all groups a partner contract belongs to
    question: What groups is a partner contract object a member of?
  - id: contract_getMemberObject
    intent: List groups, admin units and roles of a contract
    question: Which groups, administrative units and directory roles include a partner contract?
  - id: contract_restore
    intent: Restore a deleted partner contract
    question: How do I recover a partner contract object that was deleted?
  - id: contract_getAvailableExtensionProperty
    intent: List registered directory extension properties
    question: What directory extension attributes are registered in my tenant, including by multitenant apps?
  - id: contract_getGraphBPreId
    intent: Fetch directory objects by a list of IDs
    question: How can I resolve a batch of object IDs to contracts, users or groups in one request?
  - id: contract_validateProperty
    intent: Check a group name against naming policy
    question: Will a Microsoft 365 group display name pass my tenant's naming policy?
  phrasing_ops: 8
  slug: azure-ad-contracts-contract-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contracts.contract API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for contracts.contract.
  name: Microsoft Entra ID (formerly Azure AD) Contracts.contract API
  phrasing_intents:
  - id: contract_ListContract
    intent: List partner contracts with customer tenants
    question: Which customer tenants does my partner tenant have contracts with?
  - id: contract_CreateContract
    intent: Add a partner contract
    question: Can I create a new contract object for a customer tenant?
  - id: contract_GetContract
    intent: Get one partner contract
    question: What customer and contract type does a specific partner contract cover?
  - id: contract_UpdateContract
    intent: Update a partner contract
    question: Can I change the display name on an existing partner contract?
  - id: contract_DeleteContract
    intent: Delete a partner contract
    question: Can I remove a contract object from my partner tenant?
  - id: contract_GetCount
    intent: Count partner contracts
    question: How many customer contracts does my partner tenant have?
  phrasing_ops: 6
  slug: azure-ad-contracts-contract-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contracts.contract.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for contracts.contract.functions.
  name: Microsoft Entra ID (formerly Azure AD) Contracts.contract.Functions API
  phrasing_intents:
  - id: contract_delta
    intent: Track changes to partner contracts
    question: How do I get only the contracts that were created, updated or deleted since my last sync?
  phrasing_ops: 1
  slug: azure-ad-contracts-contract-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The dataPolicyOperations.dataPolicyOperation API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for datapolicyoperations.datapolicyoperation.
  name: Microsoft Entra ID (formerly Azure AD) Data Policy Operations.data Policy Operation API
  phrasing_intents:
  - id: dataPolicyOperation_ListDataPolicyOperation
    intent: List data policy export operations
    question: What user data export requests have been submitted in my tenant?
  - id: dataPolicyOperation_CreateDataPolicyOperation
    intent: Record a new data policy operation
    question: Can I add a data policy operation entry for a user?
  - id: dataPolicyOperation_GetDataPolicyOperation
    intent: Check the status of a data policy operation
    question: Has a specific user data export finished, and where is it stored?
  - id: dataPolicyOperation_UpdateDataPolicyOperation
    intent: Update a data policy operation
    question: Can I change the status or progress recorded on a data policy operation?
  - id: dataPolicyOperation_DeleteDataPolicyOperation
    intent: Delete a data policy operation
    question: Can I remove a data policy operation record?
  - id: dataPolicyOperation_GetCount
    intent: Count data policy operations
    question: How many data policy operations exist in the tenant?
  phrasing_ops: 6
  slug: azure-ad-datapolicyoperations-datapolicyoperation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.device.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for devices.device.actions.
  name: Microsoft Entra ID (formerly Azure AD) Devices.device.Actions API
  phrasing_intents:
  - id: device_checkMemberGroup
    intent: Check a device's membership in given groups
    question: How do I check whether a device is in any of a specific list of groups?
  - id: device_checkMemberObject
    intent: Check a device's membership in given objects
    question: Can I test a device against a mixed list of groups and administrative units?
  - id: device_getMemberGroup
    intent: List all groups a device belongs to
    question: What groups is a particular device a member of, including transitively?
  - id: device_getMemberObject
    intent: List groups, roles and admin units of a device
    question: Which groups, administrative units and directory roles is a device part of?
  - id: device_restore
    intent: Restore a deleted device
    question: How do I bring back a device object that was recently deleted from Entra ID?
  - id: device_getAvailableExtensionProperty
    intent: List extension properties usable on devices
    question: What directory extension properties are registered that I could set on devices?
  - id: device_getGraphBPreId
    intent: Look up devices and objects by a list of IDs
    question: How can I fetch several devices at once from a list of their IDs?
  - id: device_validateProperty
    intent: Validate group naming from the devices collection
    question: Can I check a proposed group display name against naming policy via the devices endpoint?
  phrasing_ops: 8
  slug: azure-ad-devices-device-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.device API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for devices.device.
  name: Microsoft Entra ID (formerly Azure AD) Devices.device API
  phrasing_intents:
  - id: device_ListDevice
    intent: List devices registered in the organization
    question: Which devices are registered in our Microsoft Entra tenant?
  - id: device_CreateDevice
    intent: Register a new device
    question: How do I register a new device in the directory through the API?
  - id: device_GetDevice
    intent: Get a device by its object ID
    question: How do I read a registered device's properties using its directory object ID?
  - id: device_UpdateDevice
    intent: Update a device by its object ID
    question: How do I disable a registered device's account using its object ID?
  - id: device_DeleteDevice
    intent: Delete a device by its object ID
    question: How do I remove a registered device using its object ID?
  - id: device_GetDeviceGraphBPreDeviceId
    intent: Get a device by its hardware device ID
    question: Can I look up a device by its deviceId instead of the directory object ID?
  - id: device_UpdateDeviceGraphBPreDeviceId
    intent: Update a device by its hardware device ID
    question: How do I update a device addressed by its deviceId?
  - id: device_DeleteDeviceGraphBPreDeviceId
    intent: Delete a device by its hardware device ID
    question: How do I delete a registered device when I only have its deviceId?
  phrasing_ops: 9
  slug: azure-ad-devices-device-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.device.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for devices.device.functions.
  name: Microsoft Entra ID (formerly Azure AD) Devices.device.Functions API
  phrasing_intents:
  - id: device_delta
    intent: Track device changes with delta
    question: How do I get only the devices that were added, changed or deleted since my last sync?
  phrasing_ops: 1
  slug: azure-ad-devices-device-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 50 operation(s) for devices.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Devices.directory Object API
  phrasing_intents:
  - id: device_ListMemberGraphOPre
    intent: List a device's direct group and unit memberships
    question: Which groups and administrative units is this device directly a member of?
  - id: device_GetMemberGraphOPre
    intent: Get one direct membership of a device
    question: Can I fetch a single directory object from a device's direct memberOf list by its id?
  - id: device_GetMemberGraphOPreAsAdministrativeUnit
    intent: Get a device's direct membership as an admin unit
    question: Can I read a device's direct membership back typed as an administrative unit?
  - id: device_GetMemberGraphOPreAsGroup
    intent: Get a device's direct membership as a group
    question: Can I read a device's direct membership back typed as a group with its group properties?
  - id: device.memberOf_GetCount
    intent: Count a device's direct memberships
    question: How many groups and administrative units combined is a device directly a member of?
  - id: device_ListMemberGraphOPreAsAdministrativeUnit
    intent: List admin units a device directly belongs to
    question: Which administrative units has this device been placed in directly?
  - id: device.MemberOf_GetCountAsAdministrativeUnit
    intent: Count admin units a device directly belongs to
    question: How many administrative units directly contain a given device?
  - id: device_ListMemberGraphOPreAsGroup
    intent: List groups a device directly belongs to
    question: What groups is a device directly a member of, excluding administrative units?
  phrasing_ops: 54
  slug: azure-ad-devices-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for devices.extension.
  name: Microsoft Entra ID (formerly Azure AD) Devices.extension API
  phrasing_intents:
  - id: device_ListExtension
    intent: List open extensions on a device
    question: Which open extensions with custom data are attached to a device?
  - id: device_CreateExtension
    intent: Add an open extension to a device
    question: Can I attach my own custom data to a device as an open extension?
  - id: device_GetExtension
    intent: Get one open extension on a device
    question: Can I read a single named extension from a device?
  - id: device_UpdateExtension
    intent: Update an open extension on a device
    question: Can I change the custom values inside an existing device extension?
  - id: device_DeleteExtension
    intent: Delete an open extension from a device
    question: Can I remove custom extension data from a device?
  - id: device.extension_GetCount
    intent: Count open extensions on a device
    question: How many open extensions does a device carry?
  phrasing_ops: 6
  slug: azure-ad-devices-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.administrativeUnit API from Microsoft Entra ID (formerly Azure AD) — 32 operation(s) for directory.administrativeunit.
  name: Microsoft Entra ID (formerly Azure AD) Directory.administrative Unit API
  phrasing_intents:
  - id: directory_ListAdministrativeUnit
    intent: List administrative units in the directory
    question: What administrative units exist in my Microsoft Entra tenant?
  - id: directory_CreateAdministrativeUnit
    intent: Create an administrative unit
    question: How do I set up a new administrative unit to scope admin rights to one region?
  - id: directory_GetAdministrativeUnit
    intent: Get an administrative unit's details
    question: What are the properties of a specific administrative unit?
  - id: directory_UpdateAdministrativeUnit
    intent: Update an administrative unit
    question: How do I rename an existing administrative unit?
  - id: directory_DeleteAdministrativeUnit
    intent: Delete an administrative unit
    question: How do I remove an administrative unit we no longer need?
  - id: directory.administrativeUnit_ListExtension
    intent: List open extensions on an administrative unit
    question: What custom open extensions are attached to an administrative unit?
  - id: directory.administrativeUnit_CreateExtension
    intent: Add an open extension to an administrative unit
    question: How do I attach custom data to an administrative unit as an open extension?
  - id: directory.administrativeUnit_GetExtension
    intent: Get one open extension on an administrative unit
    question: What's stored in a particular open extension on an administrative unit?
  phrasing_ops: 44
  slug: azure-ad-directory-administrativeunit-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Directory roles and objects
  name: Microsoft Entra ID (formerly Azure AD) Directory API
  phrasing_intents:
  - id: listDirectoryRoles
    intent: List activated directory roles
    question: Which directory roles are activated in my Entra tenant?
  phrasing_ops: 1
  slug: azure-ad-directory-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.attributeSet API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.attributeset.
  name: Microsoft Entra ID (formerly Azure AD) Directory.attribute Set API
  phrasing_intents:
  - id: directory_ListAttributeSet
    intent: List custom security attribute sets
    question: Which attribute sets are defined in my directory?
  - id: directory_CreateAttributeSet
    intent: Create an attribute set
    question: Can I create a new attribute set to group custom security attributes?
  - id: directory_GetAttributeSet
    intent: Get one attribute set
    question: What properties does a particular attribute set have?
  - id: directory_UpdateAttributeSet
    intent: Update an attribute set
    question: How do I change the description of an existing attribute set?
  - id: directory_DeleteAttributeSet
    intent: Delete an attribute set
    question: Can I remove an attribute set from the directory?
  - id: directory.attributeSet_GetCount
    intent: Count attribute sets
    question: How many attribute sets exist in my tenant?
  phrasing_ops: 6
  slug: azure-ad-directory-attributeset-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.companySubscription API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for directory.companysubscription.
  name: Microsoft Entra ID (formerly Azure AD) Directory.company Subscription API
  phrasing_intents:
  - id: directory_ListSubscription
    intent: List the organization's commercial subscriptions
    question: Which commercial Microsoft subscriptions has my organization acquired?
  - id: directory_CreateSubscription
    intent: Add a company subscription record
    question: Can I create a new company subscription entry in the directory?
  - id: directory_GetSubscription
    intent: Get a company subscription by its directory ID
    question: What's the status and license count of one specific company subscription?
  - id: directory_UpdateSubscription
    intent: Update a company subscription by its directory ID
    question: Can I change the license total on a subscription I address by directory ID?
  - id: directory_DeleteSubscription
    intent: Delete a company subscription by its directory ID
    question: Can I remove a company subscription record using its directory object ID?
  - id: directory.subscription_GetGraphBPreCommerceSubscriptionId
    intent: Get a company subscription by commerce ID
    question: How do I look up a subscription when all I have is its commerce subscription ID?
  - id: directory.subscription_UpdateGraphBPreCommerceSubscriptionId
    intent: Update a company subscription by commerce ID
    question: Can I patch a subscription when I only know its commerce subscription ID?
  - id: directory.subscription_DeleteGraphBPreCommerceSubscriptionId
    intent: Delete a company subscription by commerce ID
    question: Can I delete a subscription record using its commerce subscription ID?
  phrasing_ops: 9
  slug: azure-ad-directory-companysubscription-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.customSecurityAttributeDefinition API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for directory.customsecurityattributedefinition.
  name: Microsoft Entra ID (formerly Azure AD) Directory.custom Security Attribute Definition API
  phrasing_intents:
  - id: directory_ListCustomSecurityAttributeDefinition
    intent: List custom security attribute definitions
    question: Which custom security attributes are defined in my Entra ID tenant?
  - id: directory_CreateCustomSecurityAttributeDefinition
    intent: Define a custom security attribute
    question: How do I add a new custom security attribute like ProjectCode to an attribute set?
  - id: directory_GetCustomSecurityAttributeDefinition
    intent: Get a custom security attribute definition
    question: What type and attribute set does a specific custom security attribute belong to?
  - id: directory_UpdateCustomSecurityAttributeDefinition
    intent: Update a custom security attribute definition
    question: How do I deprecate a custom security attribute so nobody assigns it anymore?
  - id: directory_DeleteCustomSecurityAttributeDefinition
    intent: Delete a custom security attribute definition
    question: How do I remove a custom security attribute definition from the directory?
  - id: directory.customSecurityAttributeDefinition_ListAllowedValue
    intent: List an attribute's allowed values
    question: Which predefined values can be assigned for a custom security attribute?
  - id: directory.customSecurityAttributeDefinition_CreateAllowedValue
    intent: Add an allowed value to an attribute
    question: How do I add a new predefined value to a custom security attribute?
  - id: directory.customSecurityAttributeDefinition_GetAllowedValue
    intent: Get one allowed value of an attribute
    question: Is a specific predefined value of a custom security attribute still active?
  phrasing_ops: 12
  slug: azure-ad-directory-customsecurityattributedefinition-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.deviceLocalCredentialInfo API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.devicelocalcredentialinfo.
  name: Microsoft Entra ID (formerly Azure AD) Directory.device Local Credential Info API
  phrasing_intents:
  - id: directory_ListDeviceLocalCredential
    intent: List devices with backed-up local admin passwords
    question: Which devices have a Windows LAPS local admin password backed up to the directory?
  - id: directory_CreateDeviceLocalCredential
    intent: Add a device local credential record
    question: Can I create a new local administrator credential record for a device by name?
  - id: directory_GetDeviceLocalCredential
    intent: Get a device's local admin credential info
    question: How do I retrieve the backed-up local admin password info for one device?
  - id: directory_UpdateDeviceLocalCredential
    intent: Update a device local credential record
    question: How do I change the refresh time on an existing device's local credential record?
  - id: directory_DeleteDeviceLocalCredential
    intent: Delete a device local credential record
    question: Can I remove a stale local admin credential record for a retired device?
  - id: directory.deviceLocalCredential_GetCount
    intent: Count device local credential records
    question: How many devices have local admin credentials backed up?
  phrasing_ops: 6
  slug: azure-ad-directory-devicelocalcredentialinfo-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.directory API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directory.directory.
  name: Microsoft Entra ID (formerly Azure AD) Directory.directory API
  phrasing_intents:
  - id: directory_GetDirectory
    intent: Get the tenant directory object
    question: What does the Microsoft Entra directory root expose, like administrative units and deleted items?
  - id: directory_UpdateDirectory
    intent: Update the tenant directory object
    question: Can I change directory-level settings such as on-premises synchronization in one patch?
  phrasing_ops: 2
  slug: azure-ad-directory-directory-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 29 operation(s) for directory.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Directory.directory Object API
  phrasing_intents:
  - id: directory_ListDeletedItem
    intent: List recently deleted directory objects
    question: What directory objects have been deleted recently in my Entra tenant?
  - id: directory_GetDeletedItem
    intent: Get a deleted directory object
    question: What did a soft-deleted directory object look like before it was removed?
  - id: directory_DeleteDeletedItem
    intent: Permanently delete an object from deleted items
    question: How do I purge something from deleted items so it can never be restored?
  - id: directory_GetDeletedItemAsAdministrativeUnit
    intent: Get a deleted administrative unit
    question: What were the settings of an administrative unit someone removed?
  - id: directory_GetDeletedItemAsApplication
    intent: Get a deleted app registration
    question: What was configured on an app registration that got deleted?
  - id: directory.deletedItem_checkMemberGroup
    intent: Check a deleted object's membership in given groups
    question: Which of a handful of groups was a deleted object a member of?
  - id: directory.deletedItem_checkMemberObject
    intent: Check a deleted object against directory object IDs
    question: Was a deleted object a member of certain groups, admin units or directory roles?
  - id: directory_GetDeletedItemAsDevice
    intent: Get a deleted device
    question: What do I know about a device record that was removed from the directory?
  phrasing_ops: 30
  slug: azure-ad-directory-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.identityProviderBase API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for directory.identityproviderbase.
  name: Microsoft Entra ID (formerly Azure AD) Directory.identity Provider Base API
  phrasing_intents:
  - id: directory_ListFederationConfiguration
    intent: List SAML/WS-Fed federation configurations
    question: Which external organizations are federated with my tenant over SAML or WS-Fed?
  - id: directory_CreateFederationConfiguration
    intent: Add a federation configuration
    question: How do I set up domain federation with a partner's SAML identity provider?
  - id: directory_GetFederationConfiguration
    intent: Get a federation configuration
    question: What are the settings of a specific external domain federation?
  - id: directory_UpdateFederationConfiguration
    intent: Update a federation configuration
    question: How do I rename an existing external identity provider federation?
  - id: directory_DeleteFederationConfiguration
    intent: Delete a SAML/WS-Fed federation
    question: How do I remove federation with a partner organization's identity provider?
  - id: directory.federationConfiguration_GetCount
    intent: Count federation configurations
    question: How many SAML or WS-Fed federations does my tenant have?
  - id: directory.federationConfiguration_availableProviderType
    intent: List supported identity provider types
    question: What identity provider types can my directory federate with?
  phrasing_ops: 7
  slug: azure-ad-directory-identityproviderbase-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.onPremisesDirectorySynchronization API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.onpremisesdirectorysynchronization.
  name: Microsoft Entra ID (formerly Azure AD) Directory.on Premises Directory Synchronization API
  phrasing_intents:
  - id: directory_ListOnPremisesSynchronization
    intent: List on-premises directory sync configurations
    question: How do I see the on-premises directory synchronization settings for my tenant?
  - id: directory_CreateOnPremisesSynchronization
    intent: Create an on-premises sync configuration
    question: Can I create a new onPremisesDirectorySynchronization object with its configuration?
  - id: directory_GetOnPremisesSynchronization
    intent: Get an on-premises sync configuration
    question: What does one specific on-premises directory synchronization object contain?
  - id: directory_UpdateOnPremisesSynchronization
    intent: Update on-premises sync settings
    question: How do I turn directory sync features on or off for our hybrid tenant?
  - id: directory_DeleteOnPremisesSynchronization
    intent: Delete an on-premises sync configuration
    question: Can I delete an onPremisesDirectorySynchronization object?
  - id: directory.onPremisesSynchronization_GetCount
    intent: Count on-premises sync configurations
    question: How many on-premises directory synchronization objects exist in the tenant?
  phrasing_ops: 6
  slug: azure-ad-directory-onpremisesdirectorysynchronization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.publicKeyInfrastructureRoot API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directory.publickeyinfrastructureroot.
  name: Microsoft Entra ID (formerly Azure AD) Directory.public Key Infrastructure Root API
  phrasing_intents:
  - id: directory_GetPublicKeyInfrastructure
    intent: Get the tenant's public key infrastructure root
    question: Where does Entra ID keep the public key infrastructure used for certificate-based authentication?
  - id: directory_UpdatePublicKeyInfrastructure
    intent: Update the tenant's public key infrastructure root
    question: Can I replace the set of certificate-based auth configurations on the PKI root in one update?
  - id: directory_DeletePublicKeyInfrastructure
    intent: Delete the tenant's public key infrastructure root
    question: Can I remove the entire public key infrastructure container from the directory?
  - id: directory.publicKeyInfrastructure_ListCertificateBasedAuthConfiguration
    intent: List certificate-based auth PKI configurations
    question: Which PKI configurations are set up for certificate-based authentication in my tenant?
  - id: directory.publicKeyInfrastructure_CreateCertificateBasedAuthConfiguration
    intent: Create a certificate-based auth PKI configuration
    question: How do I create a new PKI object to hold certificate authorities for certificate-based sign-in?
  - id: directory.publicKeyInfrastructure_GetCertificateBasedAuthConfiguration
    intent: Get a certificate-based auth PKI configuration
    question: What status and details does one certificateBasedAuthPki object report?
  - id: directory.publicKeyInfrastructure_UpdateCertificateBasedAuthConfiguration
    intent: Update a certificate-based auth PKI configuration
    question: Can I rename an existing certificateBasedAuthPki object?
  - id: directory.publicKeyInfrastructure_DeleteCertificateBasedAuthConfiguration
    intent: Delete a certificate-based auth PKI configuration
    question: Can I delete a PKI configuration I no longer use for certificate-based sign-in?
  phrasing_ops: 16
  slug: azure-ad-directory-publickeyinfrastructureroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.recovery API from Microsoft Entra ID (formerly Azure AD) — 14 operation(s) for directory.recovery.
  name: Microsoft Entra ID (formerly Azure AD) Directory.recovery API
  phrasing_intents:
  - id: directory_GetRecovery
    intent: Get the directory recovery settings
    question: What does the directory recovery resource in Microsoft Entra contain?
  - id: directory_UpdateRecovery
    intent: Update the directory recovery resource
    question: How do I change the directory recovery resource as a whole?
  - id: directory_DeleteRecovery
    intent: Delete the directory recovery resource
    question: Is it possible to delete the whole recovery resource from the directory?
  - id: directory.recovery_ListJob
    intent: List directory recovery jobs
    question: Which recovery jobs have been run against my directory?
  - id: directory.recovery_CreateJob
    intent: Start a directory recovery job
    question: How do I start a job to restore directory objects to an earlier state?
  - id: directory.recovery_GetJob
    intent: Get a directory recovery job
    question: What's the status of a specific directory recovery job?
  - id: directory.recovery_UpdateJob
    intent: Update a directory recovery job
    question: Can I change the target restore time on an existing recovery job?
  - id: directory.recovery_DeleteJob
    intent: Delete a directory recovery job
    question: How do I delete an old directory recovery job record?
  phrasing_ops: 22
  slug: azure-ad-directory-recovery-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.remoteTenantGroup API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.remotetenantgroup.
  name: Microsoft Entra ID (formerly Azure AD) Directory.remote Tenant Group API
  phrasing_intents:
  - id: directory_ListRemoteTenantGroup
    intent: List remote tenant groups
    question: Which groups from other tenants are linked into my directory?
  - id: directory_CreateRemoteTenantGroup
    intent: Add a remote tenant group
    question: How do I register a group from another tenant as a remote tenant group?
  - id: directory_GetRemoteTenantGroup
    intent: Get a remote tenant group
    question: Can I look up one remote tenant group by its ID?
  - id: directory_UpdateRemoteTenantGroup
    intent: Update a remote tenant group
    question: Can I rename a remote tenant group's display name?
  - id: directory_DeleteRemoteTenantGroup
    intent: Delete a remote tenant group
    question: Can I remove a remote tenant group from my directory?
  - id: directory.remoteTenantGroup_GetCount
    intent: Count remote tenant groups
    question: How many remote tenant groups does my directory have?
  phrasing_ops: 6
  slug: azure-ad-directory-remotetenantgroup-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryObjects.directoryObject.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directoryobjects.directoryobject.actions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Objects.directory Object.Actions API
  phrasing_intents:
  - id: directoryObject_checkMemberGroup
    intent: Check which of given groups an object belongs to
    question: How do I check if a user or device is a member of any groups in a list I have?
  - id: directoryObject_checkMemberObject
    intent: Check membership in groups, roles or admin units
    question: Can I check an object's membership against a mixed list of groups, directory roles and administrative units?
  - id: directoryObject_getMemberGroup
    intent: Get all group IDs an object is a member of
    question: What are all the group IDs a user, device or service principal belongs to?
  - id: directoryObject_getMemberObject
    intent: Get IDs of groups, roles and admin units an object is in
    question: Which groups, administrative units and directory roles does this object belong to?
  - id: directoryObject_restore
    intent: Restore a recently deleted directory object
    question: How do I bring back an app, group or user that was deleted recently?
  - id: directoryObject_getAvailableExtensionProperty
    intent: List all directory extension definitions in the tenant
    question: Which directory extensions are registered in our tenant, including from multitenant apps?
  - id: directoryObject_getGraphBPreId
    intent: Get multiple directory objects by their IDs
    question: How do I resolve a batch of object IDs to users, groups and devices in one request?
  - id: directoryObject_validateProperty
    intent: Validate a group name against naming policy
    question: Will a Microsoft 365 group display name pass our naming policy before I create it?
  phrasing_ops: 8
  slug: azure-ad-directoryobjects-directoryobject-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryObjects.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directoryobjects.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Directory Objects.directory Object API
  phrasing_intents:
  - id: directoryObject_ListDirectoryObject
    intent: List directory objects
    question: How do I list all directory objects in my Entra ID tenant?
  - id: directoryObject_CreateDirectoryObject
    intent: Add a directory object
    question: Can I post a new generic entity to the directoryObjects collection?
  - id: directoryObject_GetDirectoryObject
    intent: Get a directory object
    question: What kind of object is behind a given directory object ID?
  - id: directoryObject_UpdateDirectoryObject
    intent: Update a directory object
    question: Can I PATCH a directory object generically by its ID?
  - id: directoryObject_DeleteDirectoryObject
    intent: Delete a directory object
    question: How do I delete a group, user, application or service principal by its object ID?
  - id: directoryObject_GetCount
    intent: Count directory objects
    question: How many directory objects exist in the tenant?
  phrasing_ops: 6
  slug: azure-ad-directoryobjects-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryObjects.directoryObject.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directoryobjects.directoryobject.functions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Objects.directory Object.Functions API
  phrasing_intents:
  - id: directoryObject_delta
    intent: Track changes to directory objects
    question: How can I get directory objects created, updated or deleted since my last sync without a full read?
  phrasing_ops: 1
  slug: azure-ad-directoryobjects-directoryobject-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 22 operation(s) for directoryroles.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Object API
  phrasing_intents:
  - id: directoryRole_ListMember
    intent: List members of a directory role
    question: Who is assigned to the Global Administrator role in my Entra tenant?
  - id: directoryRole.member_DeleteDirectoryObjectGraphBPreRef
    intent: Remove a member from a directory role by id
    question: How do I take a user out of an admin role in Entra ID?
  - id: directoryRole_GetMemberAsApplication
    intent: Get a directory role member as an application
    question: How do I read a role member cast as an application object?
  - id: directoryRole_GetMemberAsDevice
    intent: Get a directory role member as a device
    question: How do I read a directory role member cast as a device?
  - id: directoryRole_GetMemberAsGroup
    intent: Get a directory role member as a group
    question: How do I read a role member cast as a group, for a role-assignable group?
  - id: directoryRole_GetMemberAsOrgContact
    intent: Get a directory role member as an org contact
    question: How do I read a role member cast as an organizational contact?
  - id: directoryRole_GetMemberAsServicePrincipal
    intent: Get a directory role member as a service principal
    question: How do I read a role member cast as a service principal?
  - id: directoryRole_GetMemberAsUser
    intent: Get a directory role member as a user
    question: How do I read one role member's user profile directly?
  phrasing_ops: 24
  slug: azure-ad-directoryroles-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryRole.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directoryroles.directoryrole.actions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Role.Actions API
  phrasing_intents:
  - id: directoryRole_checkMemberGroup
    intent: Check a directory role's membership in given groups
    question: Which of a list of groups is this directory role a member of?
  - id: directoryRole_checkMemberObject
    intent: Check a directory role's membership in given objects
    question: Is this directory role a member of any of these groups, administrative units or roles?
  - id: directoryRole_getMemberGroup
    intent: Get all groups a directory role belongs to
    question: What are all the group IDs a directory role is a member of?
  - id: directoryRole_getMemberObject
    intent: Get all groups, units and roles a directory role belongs to
    question: Which groups, administrative units and directory roles is a given directory role a member of?
  - id: directoryRole_restore
    intent: Restore a recently deleted directory object
    question: How do I bring back a directory object that was recently deleted?
  - id: directoryRole_getAvailableExtensionProperty
    intent: List registered directory extension properties
    question: Which directory extension definitions are registered in my tenant, including from multitenant apps?
  - id: directoryRole_getGraphBPreId
    intent: Fetch directory objects by a list of IDs
    question: How do I resolve a batch of object IDs to the directory objects they belong to?
  - id: directoryRole_validateProperty
    intent: Check a group name against naming policy
    question: Will a Microsoft 365 group display name comply with our naming policy before I create it?
  phrasing_ops: 8
  slug: azure-ad-directoryroles-directoryrole-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryRole API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for directoryroles.directoryrole.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Role API
  phrasing_intents:
  - id: directoryRole_ListDirectoryRole
    intent: List activated directory roles in the tenant
    question: Which admin roles are currently activated in my Entra tenant?
  - id: directoryRole_CreateDirectoryRole
    intent: Activate a directory role from a template
    question: How do I activate a built-in admin role so I can assign members to it?
  - id: directoryRole_GetDirectoryRole
    intent: Get a directory role by object ID
    question: What are the properties of an activated directory role, looked up by its object ID?
  - id: directoryRole_UpdateDirectoryRole
    intent: Update a directory role by object ID
    question: Can I change an activated directory role's display name or description using its object ID?
  - id: directoryRole_DeleteDirectoryRole
    intent: Delete a directory role by object ID
    question: Can I remove an activated directory role using its object ID?
  - id: directoryRole_GetDirectoryRoleGraphBPreRoleTemplateId
    intent: Get a directory role by its role template ID
    question: Can I look up an activated role using the well-known role template ID instead of the object ID?
  - id: directoryRole_UpdateDirectoryRoleGraphBPreRoleTemplateId
    intent: Update a directory role by its role template ID
    question: How do I patch an activated role when I only know its role template ID?
  - id: directoryRole_DeleteDirectoryRoleGraphBPreRoleTemplateId
    intent: Delete a directory role by its role template ID
    question: Can I delete an activated role by referencing its role template ID?
  phrasing_ops: 9
  slug: azure-ad-directoryroles-directoryrole-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryRole.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directoryroles.directoryrole.functions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Role.Functions API
  phrasing_intents:
  - id: directoryRole_delta
    intent: Track directory role changes with delta
    question: Is there a way to get only the directory roles that were created, updated or deleted since my last sync?
  phrasing_ops: 1
  slug: azure-ad-directoryroles-directoryrole-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.scopedRoleMembership API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directoryroles.scopedrolemembership.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.scoped Role Membership API
  phrasing_intents:
  - id: directoryRole_ListScopedMember
    intent: List scoped members of a directory role
    question: Who holds a directory role only within an administrative unit?
  - id: directoryRole_CreateScopedMember
    intent: Add a scoped member to a directory role
    question: How do I grant someone a directory role scoped to one administrative unit?
  - id: directoryRole_GetScopedMember
    intent: Get one scoped role membership
    question: Which administrative unit is a specific scoped role membership limited to?
  - id: directoryRole_UpdateScopedMember
    intent: Update a scoped role membership
    question: How do I move an existing scoped role membership to a different administrative unit?
  - id: directoryRole_DeleteScopedMember
    intent: Remove a scoped role membership
    question: How do I revoke someone's directory role within an administrative unit?
  - id: directoryRole.scopedMember_GetCount
    intent: Count scoped members of a directory role
    question: How many administrative-unit-scoped members does a directory role have?
  phrasing_ops: 6
  slug: azure-ad-directoryroles-scopedrolemembership-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoleTemplates.directoryRoleTemplate.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directoryroletemplates.directoryroletemplate.actions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Role Templates.directory Role Template.Actions API
  phrasing_intents:
  - id: directoryRoleTemplate_checkMemberGroup
    intent: Check a role template's membership in given groups
    question: Which of a list of group IDs is a directory role template a member of?
  - id: directoryRoleTemplate_checkMemberObject
    intent: Check a role template's membership in given objects
    question: Is a directory role template a member of any of these groups, roles or administrative units?
  - id: directoryRoleTemplate_getMemberGroup
    intent: Get all groups a role template belongs to
    question: What groups is a directory role template a member of?
  - id: directoryRoleTemplate_getMemberObject
    intent: Get all groups, units and roles a template is in
    question: Which groups, administrative units and directory roles include a given role template?
  - id: directoryRoleTemplate_restore
    intent: Restore a deleted directory object
    question: How do I bring back a recently deleted directory object from deleted items?
  - id: directoryRoleTemplate_getAvailableExtensionProperty
    intent: List registered directory extension properties
    question: What directory extension attributes are registered in my tenant, including from multitenant apps?
  - id: directoryRoleTemplate_getGraphBPreId
    intent: Fetch directory objects by a list of IDs
    question: Can I resolve a batch of directory object IDs to their objects in one call?
  - id: directoryRoleTemplate_validateProperty
    intent: Validate a group name against naming policy
    question: Does a proposed Microsoft 365 group name comply with my tenant's naming policy?
  phrasing_ops: 8
  slug: azure-ad-directoryroletemplates-directoryroletemplate-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoleTemplates.directoryRoleTemplate API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directoryroletemplates.directoryroletemplate.
  name: Microsoft Entra ID (formerly Azure AD) Directory Role Templates.directory Role Template API
  phrasing_intents:
  - id: directoryRoleTemplate_ListDirectoryRoleTemplate
    intent: List directory role templates
    question: Which built-in directory role templates are available in Entra ID?
  - id: directoryRoleTemplate_CreateDirectoryRoleTemplate
    intent: Add a directory role template
    question: Can I add a new entry to the directory role templates collection?
  - id: directoryRoleTemplate_GetDirectoryRoleTemplate
    intent: Get a directory role template
    question: What does a specific directory role template describe?
  - id: directoryRoleTemplate_UpdateDirectoryRoleTemplate
    intent: Update a directory role template
    question: Can I change the display name or description of a role template?
  - id: directoryRoleTemplate_DeleteDirectoryRoleTemplate
    intent: Delete a directory role template
    question: Can a directory role template be deleted from the collection?
  - id: directoryRoleTemplate_GetCount
    intent: Count directory role templates
    question: How many directory role templates exist?
  phrasing_ops: 6
  slug: azure-ad-directoryroletemplates-directoryroletemplate-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoleTemplates.directoryRoleTemplate.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directoryroletemplates.directoryroletemplate.functions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Role Templates.directory Role Template.Functions API
  phrasing_intents:
  - id: directoryRoleTemplate_delta
    intent: Track changes to directory role templates
    question: How do I get only the directory role templates that changed since my last sync?
  phrasing_ops: 1
  slug: azure-ad-directoryroletemplates-directoryroletemplate-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for domains.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Domains.directory Object API
  phrasing_intents:
  - id: domain_ListDomainNameReference
    intent: List objects that reference a domain
    question: Which users and groups are still using a domain I want to remove?
  - id: domain_GetDomainNameReference
    intent: Get one object that references a domain
    question: Does a particular user still reference a given domain?
  - id: domain.domainNameReference_GetCount
    intent: Count objects that reference a domain
    question: How many objects still reference a domain?
  phrasing_ops: 3
  slug: azure-ad-domains-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.domain.Actions API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for domains.domain.actions.
  name: Microsoft Entra ID (formerly Azure AD) Domains.domain.Actions API
  phrasing_intents:
  - id: domain_forceDelete
    intent: Force delete a domain
    question: How do I force delete a custom domain that still has users and groups referencing it?
  - id: domain_promote
    intent: Promote a subdomain to root domain
    question: How do I promote a verified subdomain to be a root domain in my tenant?
  - id: domain_verify
    intent: Verify domain ownership
    question: How do I verify that I own a custom domain I added to Entra ID?
  phrasing_ops: 3
  slug: azure-ad-domains-domain-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.domain API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for domains.domain.
  name: Microsoft Entra ID (formerly Azure AD) Domains.domain API
  phrasing_intents:
  - id: domain_ListDomain
    intent: List domains in the tenant
    question: Which domains are associated with my Microsoft Entra tenant?
  - id: domain_CreateDomain
    intent: Add a domain to the tenant
    question: How do I add my company's custom domain to the tenant?
  - id: domain_GetDomain
    intent: Get a domain's details
    question: Is a specific domain verified and set as the default?
  - id: domain_UpdateDomain
    intent: Update a verified domain
    question: How do I make a verified domain the default for new users?
  - id: domain_DeleteDomain
    intent: Delete a domain from the tenant
    question: How do I remove a custom domain from my tenant?
  - id: domain_GetRootDomain
    intent: Get the root domain of a subdomain
    question: Which root domain does a subdomain in my tenant belong to?
  - id: domain_GetCount
    intent: Count domains in the tenant
    question: How many domains does my tenant have?
  phrasing_ops: 7
  slug: azure-ad-domains-domain-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.domainDnsRecord API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for domains.domaindnsrecord.
  name: Microsoft Entra ID (formerly Azure AD) Domains.domain Dns Record API
  phrasing_intents:
  - id: domain_ListServiceConfigurationRecord
    intent: List DNS records needed to enable services on a domain
    question: Which DNS records do I need to add to my zone file so Microsoft Online services work on my domain?
  - id: domain_CreateServiceConfigurationRecord
    intent: Add a service configuration record to a domain
    question: Can I add a new service configuration DNS record entry to a domain?
  - id: domain_GetServiceConfigurationRecord
    intent: Get one service configuration record of a domain
    question: What are the details of one specific service configuration DNS record for my domain?
  - id: domain_UpdateServiceConfigurationRecord
    intent: Update a service configuration record of a domain
    question: Can I change the TTL or label of an existing service configuration record?
  - id: domain_DeleteServiceConfigurationRecord
    intent: Delete a service configuration record from a domain
    question: Can I remove a service configuration DNS record entry from a domain?
  - id: domain.serviceConfigurationRecord_GetCount
    intent: Count a domain's service configuration records
    question: How many service configuration DNS records does my domain require?
  - id: domain_ListVerificationDnsRecord
    intent: List DNS records needed to verify domain ownership
    question: Which DNS record do I add to prove I own a custom domain before using it in my tenant?
  - id: domain_CreateVerificationDnsRecord
    intent: Add a verification record to a domain
    question: Can I add a new ownership verification DNS record entry to a domain?
  phrasing_ops: 12
  slug: azure-ad-domains-domaindnsrecord-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.internalDomainFederation API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for domains.internaldomainfederation.
  name: Microsoft Entra ID (formerly Azure AD) Domains.internal Domain Federation API
  phrasing_intents:
  - id: domain_ListFederationConfiguration
    intent: List a domain's federation configuration
    question: How do I see the federation settings for a domain federated with an external identity provider?
  - id: domain_CreateFederationConfiguration
    intent: Federate a domain with an identity provider
    question: How do I set up federation for a domain in Microsoft Entra ID?
  - id: domain_GetFederationConfiguration
    intent: Get a domain's federation settings
    question: How do I read one internalDomainFederation object for a domain?
  - id: domain_UpdateFederationConfiguration
    intent: Update a domain's federation settings
    question: Can I roll over the next signing certificate on an already federated domain?
  - id: domain_DeleteFederationConfiguration
    intent: Remove federation from a domain
    question: How do I delete the federation configuration from a domain?
  - id: domain.federationConfiguration_GetCount
    intent: Count a domain's federation configurations
    question: Is a given domain federated at all, judging by the count of its federation configurations?
  phrasing_ops: 6
  slug: azure-ad-domains-internaldomainfederation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupLifecyclePolicies.groupLifecyclePolicy.Actions API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for grouplifecyclepolicies.grouplifecyclepolicy.actions.
  name: Microsoft Entra ID (formerly Azure AD) Group Lifecycle Policies.group Lifecycle Policy.Actions API
  phrasing_intents:
  - id: groupLifecyclePolicy_addGroup
    intent: Add a group to an expiration policy
    question: How do I make a Microsoft 365 group subject to the group expiration policy?
  - id: groupLifecyclePolicy_removeGroup
    intent: Remove a group from an expiration policy
    question: Can I exempt a specific group from expiring under a lifecycle policy?
  phrasing_ops: 2
  slug: azure-ad-grouplifecyclepolicies-grouplifecyclepolicy-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupLifecyclePolicies.groupLifecyclePolicy API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for grouplifecyclepolicies.grouplifecyclepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Group Lifecycle Policies.group Lifecycle Policy API
  phrasing_intents:
  - id: groupLifecyclePolicy_ListGroupLifecyclePolicy
    intent: List group expiration policies
    question: Do we have a group expiration policy set up in our tenant?
  - id: groupLifecyclePolicy_CreateGroupLifecyclePolicy
    intent: Create a group expiration policy
    question: How do I make Microsoft 365 groups expire automatically after a set number of days?
  - id: groupLifecyclePolicy_GetGroupLifecyclePolicy
    intent: Get a group expiration policy
    question: What lifetime in days does a specific group lifecycle policy use?
  - id: groupLifecyclePolicy_UpdateGroupLifecyclePolicy
    intent: Update a group expiration policy
    question: How do I change how many days groups live before they expire?
  - id: groupLifecyclePolicy_DeleteGroupLifecyclePolicy
    intent: Delete a group expiration policy
    question: How do I turn off group expiration for the tenant?
  - id: groupLifecyclePolicy_GetCount
    intent: Count group expiration policies
    question: How many group lifecycle policies exist in the tenant?
  phrasing_ops: 6
  slug: azure-ad-grouplifecyclepolicies-grouplifecyclepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Microsoft 365 and security groups
  name: Microsoft Entra ID (formerly Azure AD) Groups API
  phrasing_intents:
  - id: listGroups
    intent: List groups in the organization
    question: How do I list all the groups in my Entra ID tenant?
  - id: createGroup
    intent: Create a group
    question: How do I create a new security group in Entra ID?
  - id: getGroup
    intent: Get one group's details
    question: How can I look up a single group by its ID?
  phrasing_ops: 3
  slug: azure-ad-groups-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.appRoleAssignment API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.approleassignment.
  name: Microsoft Entra ID (formerly Azure AD) Groups.app Role Assignment API
  phrasing_intents:
  - id: group_ListAppRoleAssignment
    intent: List app roles granted to a group
    question: Which application roles has a security group been assigned?
  - id: group_CreateAppRoleAssignment
    intent: Assign an app role to a group
    question: How do I give every member of a security group an application role?
  - id: group_GetAppRoleAssignment
    intent: Get one app role assignment of a group
    question: How do I look up a specific app role a group has been granted?
  - id: group_UpdateAppRoleAssignment
    intent: Update a group's app role assignment
    question: Can I change which role an existing group app role assignment grants?
  - id: group_DeleteAppRoleAssignment
    intent: Revoke an app role from a group
    question: How do I take an application role away from a group?
  - id: group.appRoleAssignment_GetCount
    intent: Count app roles assigned to a group
    question: How many app role assignments does a group have?
  phrasing_ops: 6
  slug: azure-ad-groups-approleassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.conversation API from Microsoft Entra ID (formerly Azure AD) — 29 operation(s) for groups.conversation.
  name: Microsoft Entra ID (formerly Azure AD) Groups.conversation API
  phrasing_intents:
  - id: group_ListConversation
    intent: List a group's conversations
    question: How do I see every conversation in a Microsoft 365 group's inbox?
  - id: group_CreateConversation
    intent: Start a new conversation in a group
    question: Can I start a brand-new discussion in a group with its own topic?
  - id: group_GetConversation
    intent: Get one group conversation
    question: Where can I read the topic, preview and senders of a single group conversation?
  - id: group_DeleteConversation
    intent: Delete a group conversation
    question: Can I remove an entire conversation from a group, threads and all?
  - id: group.conversation_ListThread
    intent: List threads in a group conversation
    question: Which threads make up a particular group conversation?
  - id: group.conversation_CreateThread
    intent: Create a thread in a group conversation
    question: Can I add a new thread with its first post to an existing group conversation?
  - id: group.conversation_GetThread
    intent: Get one thread from a group conversation
    question: Can I look up a single conversation thread to see if it's locked and who it went to?
  - id: group.conversation_UpdateThread
    intent: Update a group conversation thread
    question: Can I lock a conversation thread so nobody can reply to it?
  phrasing_ops: 44
  slug: azure-ad-groups-conversation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.conversationThread API from Microsoft Entra ID (formerly Azure AD) — 26 operation(s) for groups.conversationthread.
  name: Microsoft Entra ID (formerly Azure AD) Groups.conversation Thread API
  phrasing_intents:
  - id: group_ListThread
    intent: List a group's conversation threads
    question: How do I see all the conversation threads in a Microsoft 365 group?
  - id: group_CreateThread
    intent: Start a new group conversation thread
    question: How do I start a brand new conversation in a group through the Graph API?
  - id: group_GetThread
    intent: Get one conversation thread in a group
    question: How do I read the details of a single thread in a group, like its topic and senders?
  - id: group_UpdateThread
    intent: Update a group conversation thread
    question: How do I lock an existing group thread so nobody can reply?
  - id: group_DeleteThread
    intent: Delete a group conversation thread
    question: How do I delete an entire conversation thread from a group?
  - id: group.thread_reply
    intent: Reply to a group conversation thread
    question: How do I reply to a whole group thread rather than to one specific post?
  - id: group.thread_ListPost
    intent: List the posts in a group thread
    question: How do I read every message posted in a group conversation thread?
  - id: group.thread_GetPost
    intent: Get a single post in a group thread
    question: How do I fetch one specific post from a group conversation thread?
  phrasing_ops: 39
  slug: azure-ad-groups-conversationthread-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 113 operation(s) for groups.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Groups.directory Object API
  phrasing_intents:
  - id: group_ListAcceptedSender
    intent: List who may post to a group's conversations
    question: Who is on the accepted senders list allowed to post in a group's conversations?
  - id: group.acceptedSender_DeleteDirectoryObjectGraphBPreRef
    intent: Remove one accepted sender from a group
    question: How do I take a specific user off a group's accepted senders list by their object id?
  - id: group.acceptedSender_GetCount
    intent: Count a group's accepted senders
    question: How many users and groups are on a group's accepted senders list?
  - id: group_ListAcceptedSenderGraphBPreRef
    intent: List accepted sender references for a group
    question: Can I get only the reference links of a group's accepted senders instead of full objects?
  - id: group_CreateAcceptedSenderGraphBPreRef
    intent: Allow a user or group to post to a group
    question: How do I add a user to a group's accepted senders so they can post to its conversations?
  - id: group_DeleteAcceptedSenderGraphBPreRef
    intent: Remove an accepted sender by reference link
    question: Can I remove an accepted sender from a group by passing its @id reference in the query?
  - id: group_GetCreatedOnBehalfGraphOPre
    intent: See who a group was created on behalf of
    question: Which user or application created a group on someone's behalf?
  - id: group_ListMemberGraphOPre
    intent: List groups and units a group directly belongs to
    question: Which groups, administrative units and admin roles is a group a direct member of?
  phrasing_ops: 121
  slug: azure-ad-groups-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.extension.
  name: Microsoft Entra ID (formerly Azure AD) Groups.extension API
  phrasing_intents:
  - id: group_ListExtension
    intent: List a group's open extensions
    question: What custom open extension data is stored on a group?
  - id: group_CreateExtension
    intent: Add an open extension to a group
    question: How do I attach my own custom data to a group?
  - id: group_GetExtension
    intent: Get one open extension on a group
    question: What values are held in a specific open extension on a group?
  - id: group_UpdateExtension
    intent: Update an open extension on a group
    question: How do I change the values stored in a group's open extension?
  - id: group_DeleteExtension
    intent: Delete an open extension from a group
    question: How do I remove custom extension data from a group?
  - id: group.extension_GetCount
    intent: Count a group's open extensions
    question: How many open extensions are defined on a group?
  phrasing_ops: 6
  slug: azure-ad-groups-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.group.Actions API from Microsoft Entra ID (formerly Azure AD) — 18 operation(s) for groups.group.actions.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group.Actions API
  phrasing_intents:
  - id: group_addFavorite
    intent: Add a group to my favorites
    question: How do I pin a Microsoft 365 group to my favorites so it shows up in Outlook and Teams?
  - id: group_assignLicense
    intent: Add or remove licenses on a group
    question: How do I give every member of a group a license using group-based licensing?
  - id: group_checkGrantedPermissionsGraphFPreApp
    intent: Check app permissions granted on a group
    question: Which resource-specific permissions have apps been granted on this group?
  - id: group_checkMemberGroup
    intent: Check a group's membership in listed groups
    question: Is this group a member of any of the groups on my shortlist, including nested membership?
  - id: group_checkMemberObject
    intent: Check a group's membership in listed objects
    question: Can I test whether a group belongs to specific groups, administrative units or directory roles by ID?
  - id: group_getMemberGroup
    intent: List every group a group belongs to
    question: What are all the groups this group is nested inside, directly or transitively?
  - id: group_getMemberObject
    intent: List groups, units and roles a group belongs to
    question: Which groups, administrative units and directory roles is this group a member of?
  - id: group_removeFavorite
    intent: Remove a group from my favorites
    question: How do I unpin a Microsoft 365 group from my favorites?
  phrasing_ops: 18
  slug: azure-ad-groups-group-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.group API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for groups.group.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group API
  phrasing_intents:
  - id: group_ListGroup
    intent: List groups in the organization
    question: How do I list all the groups in my Entra ID tenant?
  - id: group_CreateGroup
    intent: Create a group
    question: How do I create a new security group in Entra ID?
  - id: group_GetGroup
    intent: Get a group by id
    question: How do I get the properties of a group when I know its object id?
  - id: group_UpdateGroup
    intent: Update a group by id
    question: How do I rename a group or change its description using its object id?
  - id: group_DeleteGroup
    intent: Delete a group by id
    question: Can a deleted group be restored, and for how long?
  - id: group_GetGroupGraphBPreUniqueName
    intent: Get a group by its unique name
    question: Can I look up a group by its uniqueName instead of its object id?
  - id: group_UpdateGroupGraphBPreUniqueName
    intent: Upsert a group by its unique name
    question: How do I create a group only if one with this unique name doesn't already exist?
  - id: group_DeleteGroupGraphBPreUniqueName
    intent: Delete a group by its unique name
    question: Is it possible to delete a group addressing it by uniqueName rather than id?
  phrasing_ops: 9
  slug: azure-ad-groups-group-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.group.Functions API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for groups.group.functions.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group.Functions API
  phrasing_intents:
  - id: group.site.getGraphBPrePath_getActivitiesGraphBPreInterval
    intent: Get default activity stats for a group site path
    question: What activity has a site path in a group's site seen, without picking dates or an interval?
  - id: getGroupsByGroupIdSitesBySiteIdMicrosoftGraphGetByPath(path='{path}')MicrosoftGraphGetActivitiesByInterval(startDateTime='{startDateTime}',endDateTime='{endDateTime}',interval='{interval}')
    intent: Get activity for a group site path over a date range
    question: How much activity did a group site path see between two dates, broken down by day or week?
  - id: group.site.getGraphBPrePath_getApplicableContentTypesGraphFPreList
    intent: List content types addable to a group site list
    question: Which site content types can I add to a particular list on a group's SharePoint site?
  - id: group_delta
    intent: Track changes to groups and memberships
    question: How can I get only the groups that were created, updated or deleted since my last sync?
  phrasing_ops: 4
  slug: azure-ad-groups-group-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.groupLifecyclePolicy API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for groups.grouplifecyclepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group Lifecycle Policy API
  phrasing_intents:
  - id: group_ListGroupLifecyclePolicy
    intent: List lifecycle policies a group belongs to
    question: Which expiration policies apply to a given group?
  - id: group_CreateGroupLifecyclePolicy
    intent: Create a lifecycle policy under a group
    question: Can I create an expiration policy with a set lifetime in days from a group's endpoint?
  - id: group_GetGroupLifecyclePolicy
    intent: Get a group's lifecycle policy
    question: What lifetime and notification emails does one of a group's expiration policies use?
  - id: group_UpdateGroupLifecyclePolicy
    intent: Update a group's lifecycle policy
    question: Can I extend the lifetime of an existing group expiration policy?
  - id: group_DeleteGroupLifecyclePolicy
    intent: Delete a lifecycle policy via a group
    question: Can I delete an expiration policy through a group's lifecycle policy link?
  - id: group.groupLifecyclePolicy_addGroup
    intent: Add a group to a lifecycle policy
    question: How do I put a specific group under an expiration policy?
  - id: group.groupLifecyclePolicy_removeGroup
    intent: Remove a group from a lifecycle policy
    question: Can I stop a group from expiring by taking it out of a lifecycle policy?
  - id: group.groupLifecyclePolicy_GetCount
    intent: Count lifecycle policies on a group
    question: How many lifecycle policies is a group part of?
  phrasing_ops: 8
  slug: azure-ad-groups-grouplifecyclepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.groupSetting API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.groupsetting.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group Setting API
  phrasing_intents:
  - id: group_ListSetting
    intent: List a group's settings
    question: What settings objects are configured on a particular Microsoft 365 group?
  - id: group_CreateSetting
    intent: Create a setting on a group from a template
    question: How do I apply a group setting template, like guest access, to one specific group?
  - id: group_GetSetting
    intent: Get one setting on a group
    question: What values does a specific settings object on a group currently hold?
  - id: group_UpdateSetting
    intent: Change values of a group's setting
    question: How do I change a value, like allowing guests, in an existing group setting?
  - id: group_DeleteSetting
    intent: Delete a setting from a group
    question: Can I remove a group-specific setting so the group falls back to tenant defaults?
  - id: group.setting_GetCount
    intent: Count a group's settings
    question: How many settings objects are applied to a particular group?
  phrasing_ops: 6
  slug: azure-ad-groups-groupsetting-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.onPremisesSyncBehavior API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for groups.onpremisessyncbehavior.
  name: Microsoft Entra ID (formerly Azure AD) Groups.on Premises Sync Behavior API
  phrasing_intents:
  - id: group_GetOnPremisesSyncBehavior
    intent: Check whether a group is cloud-managed or synced
    question: How can I tell if a group's source of authority is still on-premises Active Directory?
  - id: group_UpdateOnPremisesSyncBehavior
    intent: Switch a group between cloud-managed and on-prem synced
    question: How do I move a synced group's source of authority to the cloud?
  - id: group_DeleteOnPremisesSyncBehavior
    intent: Remove a group's on-premises sync behavior setting
    question: Can I clear the on-premises sync behavior object from a group entirely?
  phrasing_ops: 3
  slug: azure-ad-groups-onpremisessyncbehavior-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.profilePhoto API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for groups.profilephoto.
  name: Microsoft Entra ID (formerly Azure AD) Groups.profile Photo API
  phrasing_intents:
  - id: group_GetPhoto
    intent: Get metadata for a group's main profile photo
    question: What are the dimensions of a group's current profile picture?
  - id: group_UpdatePhoto
    intent: Update a group's profile photo metadata
    question: Can I patch the height and width recorded on a group's profile photo?
  - id: group_DeletePhoto
    intent: Delete a group's profile photo object
    question: Can I delete the photo navigation property on a group entirely?
  - id: group_GetPhotoContent
    intent: Download a group's current profile picture
    question: How do I download the actual image file of a group's profile picture?
  - id: group_SetPhotoContent
    intent: Upload a new profile picture for a group
    question: How do I upload or replace the profile picture on a Microsoft 365 group?
  - id: group_DeletePhotoContent
    intent: Remove a group's profile picture image
    question: How can I clear the picture on a group so it falls back to the default?
  - id: group_ListPhoto
    intent: List all photo sizes a group owns
    question: Which photo sizes are available for a group's profile picture?
  - id: getGroupsByGroupIdPhotosByProfilePhotoId
    intent: Get details of one photo size for a group
    question: What are the pixel dimensions of one particular photo size in a group's collection?
  phrasing_ops: 11
  slug: azure-ad-groups-profilephoto-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.resourceSpecificPermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.resourcespecificpermissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Groups.resource Specific Permission Grant API
  phrasing_intents:
  - id: group_ListPermissionGrant
    intent: List apps with resource-specific access to a group
    question: Which Microsoft Entra apps have been granted access to this group?
  - id: group_CreatePermissionGrant
    intent: Grant an app a resource-specific permission on a group
    question: How do I give an app a resource-specific permission scoped to one group?
  - id: group_GetPermissionGrant
    intent: Get one permission grant on a group
    question: Can I look up a single resource-specific permission grant on a group?
  - id: group_UpdatePermissionGrant
    intent: Change an existing permission grant on a group
    question: How do I change the permission on an existing app grant for a group?
  - id: group_DeletePermissionGrant
    intent: Revoke an app's permission grant on a group
    question: How do I revoke an app's resource-specific access to a group?
  - id: group.permissionGrant_GetCount
    intent: Count permission grants on a group
    question: How many app permission grants exist on this group?
  phrasing_ops: 6
  slug: azure-ad-groups-resourcespecificpermissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettings.groupSetting API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groupsettings.groupsetting.
  name: Microsoft Entra ID (formerly Azure AD) Group Settings.group Setting API
  phrasing_intents:
  - id: groupSetting_ListGroupSetting
    intent: List group settings
    question: Which tenant-wide and group-specific settings objects exist?
  - id: groupSetting_CreateGroupSetting
    intent: Create group settings from a template
    question: How do I create a tenant-wide group setting from a settings template?
  - id: groupSetting_GetGroupSetting
    intent: Get a group setting
    question: How do I look up a single group setting by ID?
  - id: groupSetting_UpdateGroupSetting
    intent: Update a group setting
    question: How do I change the values of an existing group setting?
  - id: groupSetting_DeleteGroupSetting
    intent: Delete a group setting
    question: How do I delete a tenant-level or group-specific setting?
  - id: groupSetting_GetCount
    intent: Count group settings
    question: How many group settings objects are there in the tenant?
  phrasing_ops: 6
  slug: azure-ad-groupsettings-groupsetting-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for groupsettingtemplates.groupsettingtemplate.actions.
  name: Microsoft Entra ID (formerly Azure AD) Group Setting Templates.group Setting Template.Actions API
  phrasing_intents:
  - id: groupSettingTemplate_checkMemberGroup
    intent: Check group membership of a setting template
    question: Which of these group IDs is a group setting template object a member of?
  - id: groupSettingTemplate_checkMemberObject
    intent: Check object membership of a setting template
    question: Is a group setting template a member of any of these groups, administrative units or roles?
  - id: groupSettingTemplate_getMemberGroup
    intent: Get groups a setting template belongs to
    question: Which groups is a given group setting template object a member of?
  - id: groupSettingTemplate_getMemberObject
    intent: Get all memberships of a setting template
    question: What groups, administrative units and directory roles is a group setting template a member of?
  - id: groupSettingTemplate_restore
    intent: Restore a deleted group setting template
    question: Can I restore a recently deleted directory object through the group setting templates path?
  - id: groupSettingTemplate_getAvailableExtensionProperty
    intent: List available directory extension properties
    question: Which directory extension properties are registered in my tenant, including from multitenant apps?
  - id: groupSettingTemplate_getGraphBPreId
    intent: Get directory objects by a list of IDs
    question: How do I fetch several directory objects at once when I have their IDs?
  - id: groupSettingTemplate_validateProperty
    intent: Validate a group name against naming policy
    question: Will this Microsoft 365 group display name comply with our naming policy before I create it?
  phrasing_ops: 8
  slug: azure-ad-groupsettingtemplates-groupsettingtemplate-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groupsettingtemplates.groupsettingtemplate.
  name: Microsoft Entra ID (formerly Azure AD) Group Setting Templates.group Setting Template API
  phrasing_intents:
  - id: groupSettingTemplate_ListGroupSettingTemplate
    intent: List available group setting templates
    question: Which group setting templates are available in my tenant, like Group.Unified?
  - id: groupSettingTemplate_CreateGroupSettingTemplate
    intent: Add a group setting template
    question: Can I add a new entity to the group setting templates collection?
  - id: groupSettingTemplate_GetGroupSettingTemplate
    intent: Get a group setting template's defaults
    question: What default values and setting names does a particular group setting template define?
  - id: groupSettingTemplate_UpdateGroupSettingTemplate
    intent: Update a group setting template
    question: Can I rename or change the default values of a group setting template?
  - id: groupSettingTemplate_DeleteGroupSettingTemplate
    intent: Delete a group setting template
    question: Can I delete a group setting template from the tenant?
  - id: groupSettingTemplate_GetCount
    intent: Count group setting templates
    question: How many group setting templates exist in the tenant?
  phrasing_ops: 6
  slug: azure-ad-groupsettingtemplates-groupsettingtemplate-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for groupsettingtemplates.groupsettingtemplate.functions.
  name: Microsoft Entra ID (formerly Azure AD) Group Setting Templates.group Setting Template.Functions API
  phrasing_intents:
  - id: groupSettingTemplate_delta
    intent: Track changes to group setting templates
    question: How do I find group setting templates that were created, updated or deleted since my last sync?
  phrasing_ops: 1
  slug: azure-ad-groupsettingtemplates-groupsettingtemplate-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.authenticationEventListener API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identity.authenticationeventlistener.
  name: Microsoft Entra ID (formerly Azure AD) Identity.authentication Event Listener API
  phrasing_intents:
  - id: identity_ListAuthenticationEventListener
    intent: List authentication event listeners
    question: Which authentication event listeners are configured in my tenant?
  - id: identity_CreateAuthenticationEventListener
    intent: Create an authentication event listener
    question: How do I create a listener that triggers on an authentication event?
  - id: identity_GetAuthenticationEventListener
    intent: Get an authentication event listener
    question: What are the properties and conditions of one authentication event listener?
  - id: identity_UpdateAuthenticationEventListener
    intent: Update an authentication event listener
    question: Can I change the conditions or name of an existing authentication event listener?
  - id: identity_DeleteAuthenticationEventListener
    intent: Delete an authentication event listener
    question: Can I remove an authentication event listener I no longer use?
  - id: identity.authenticationEventListener_GetCount
    intent: Count authentication event listeners
    question: How many authentication event listeners are set up?
  phrasing_ops: 6
  slug: azure-ad-identity-authenticationeventlistener-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.authenticationEventsFlow API from Microsoft Entra ID (formerly Azure AD) — 26 operation(s) for identity.authenticationeventsflow.
  name: Microsoft Entra ID (formerly Azure AD) Identity.authentication Events Flow API
  phrasing_intents:
  - id: identity_ListAuthenticationEventsFlow
    intent: List authentication events flows (user flows)
    question: How do I see all the sign-up user flows configured in my Entra External ID tenant?
  - id: identity_CreateAuthenticationEventsFlow
    intent: Create an authentication events flow
    question: How do I create a new self-service sign-up user flow for external users?
  - id: identity_GetAuthenticationEventsFlow
    intent: Get one authentication events flow
    question: How can I look up the full settings of one specific user flow by its ID?
  - id: identity_UpdateAuthenticationEventsFlow
    intent: Update an authentication events flow
    question: How do I rename an existing user flow or change its description?
  - id: identity_DeleteAuthenticationEventsFlow
    intent: Delete an authentication events flow
    question: What happens to linked applications when I delete a user flow?
  - id: identity.authenticationEventsFlow_GetCondition
    intent: Get the conditions that trigger a user flow
    question: What conditions decide whether a particular user flow gets invoked?
  - id: identity.authenticationEventsFlow_ListIncludeApplication
    intent: List applications linked to a user flow
    question: Which apps are currently linked to my self-service sign-up user flow?
  - id: identity.authenticationEventsFlow_CreateIncludeApplication
    intent: Link an application to a user flow
    question: How do I enable a sign-up user flow for one of my applications?
  phrasing_ops: 39
  slug: azure-ad-identity-authenticationeventsflow-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.b2xIdentityUserFlow API from Microsoft Entra ID (formerly Azure AD) — 34 operation(s) for identity.b2xidentityuserflow.
  name: Microsoft Entra ID (formerly Azure AD) Identity.b2x Identity User Flow API
  phrasing_intents:
  - id: identity_ListB2xUserFlow
    intent: List B2X self-service sign-up user flows
    question: Which self-service sign-up user flows are set up for guests in my Entra tenant?
  - id: identity_CreateB2xUserFlow
    intent: Create a B2X self-service sign-up user flow
    question: How do I create a new self-service sign-up flow for external guests?
  - id: identity_GetB2xUserFlow
    intent: Get one B2X user flow
    question: What are the settings and relationships of one specific guest sign-up user flow?
  - id: identity_UpdateB2xUserFlow
    intent: Update a B2X user flow
    question: How do I change the settings of an existing B2X sign-up user flow?
  - id: identity_DeleteB2xUserFlow
    intent: Delete a B2X user flow
    question: How do I remove a guest self-service sign-up flow I no longer need?
  - id: identity.b2xUserFlow_GetApiConnectorConfiguration
    intent: Get the API connectors enabled for a user flow
    question: Which API connectors are enabled in a B2X user flow?
  - id: identity.b2xUserFlow_GetPostAttributeCollection
    intent: Get the post-attribute-collection API connector
    question: What API connector runs after attributes are collected in my sign-up flow?
  - id: identity.b2xUserFlow_UpdatePostAttributeCollection
    intent: Update the post-attribute-collection connector
    question: How do I change the target URL of the connector called after attribute collection?
  phrasing_ops: 63
  slug: azure-ad-identity-b2xidentityuserflow-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.conditionalAccessRoot API from Microsoft Entra ID (formerly Azure AD) — 36 operation(s) for identity.conditionalaccessroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity.conditional Access Root API
  phrasing_intents:
  - id: identity.conditionalAccess_ListAuthenticationContextClassReference
    intent: List authentication contexts
    question: Which authentication contexts are defined for Conditional Access in my tenant?
  - id: identity.conditionalAccess_CreateAuthenticationContextClassReference
    intent: Add an authentication context
    question: How do I add a new authentication context like c5 for step-up Conditional Access?
  - id: identity.conditionalAccess_GetAuthenticationContextClassReference
    intent: Get one authentication context
    question: What are the details of a specific authentication context class reference?
  - id: identity.conditionalAccess_UpdateAuthenticationContextClassReference
    intent: Create or update an authentication context
    question: Can I publish an existing authentication context so apps can start using it?
  - id: identity.conditionalAccess_DeleteAuthenticationContextClassReference
    intent: Delete an authentication context
    question: How do I remove an authentication context that no policy uses anymore?
  - id: identity.conditionalAccess.authenticationContextClassReference_GetCount
    intent: Count authentication contexts
    question: How many authentication context class references does my tenant have?
  - id: identity.conditionalAccess_GetAuthenticationStrength
    intent: Get the authentication strength root
    question: What does the authentication strength container under Conditional Access hold?
  - id: identity.conditionalAccess_UpdateAuthenticationStrength
    intent: Update the authentication strength root
    question: How do I change the authentication strength root object as a whole?
  phrasing_ops: 64
  slug: azure-ad-identity-conditionalaccessroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.customAuthenticationExtension API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for identity.customauthenticationextension.
  name: Microsoft Entra ID (formerly Azure AD) Identity.custom Authentication Extension API
  phrasing_intents:
  - id: identity_ListCustomAuthenticationExtension
    intent: List custom authentication extensions
    question: Which custom authentication extensions are registered in my Entra tenant?
  - id: identity_CreateCustomAuthenticationExtension
    intent: Create a custom authentication extension
    question: How do I register a new custom authentication extension that calls my API?
  - id: identity_GetCustomAuthenticationExtension
    intent: Get a custom authentication extension
    question: How do I read the configuration of one custom authentication extension?
  - id: identity_UpdateCustomAuthenticationExtension
    intent: Update a custom authentication extension
    question: Can I change the on-error behavior of an existing custom authentication extension?
  - id: identity_DeleteCustomAuthenticationExtension
    intent: Delete a custom authentication extension
    question: How do I delete a custom authentication extension I'm no longer using?
  - id: identity.customAuthenticationExtension_validateAuthenticationConfiguration
    intent: Validate a saved extension's endpoint and auth setup
    question: Is the endpoint and authentication configuration on my existing custom authentication extension valid?
  - id: identity.customAuthenticationExtension_GetCount
    intent: Count custom authentication extensions
    question: How many custom authentication extensions does my tenant have?
  - id: postIdentityCustomAuthenticationExtensionsMicrosoftGraphValidateAuthenticationConfiguration
    intent: Validate an endpoint and auth setup before saving
    question: Can I test an endpoint URL and its authentication settings before creating a custom authentication extension?
  phrasing_ops: 8
  slug: azure-ad-identity-customauthenticationextension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityApiConnector API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for identity.identityapiconnector.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity API Connector API
  phrasing_intents:
  - id: identity_ListApiConnector
    intent: List API connectors for sign-up flows
    question: Which API connectors are configured for my external identities sign-up flows?
  - id: identity_CreateApiConnector
    intent: Create an API connector
    question: How do I register an external REST endpoint to call during user sign-up?
  - id: identity_GetApiConnector
    intent: Get an API connector
    question: What URL and authentication does a specific API connector use?
  - id: identity_UpdateApiConnector
    intent: Update an API connector
    question: Can I point an existing API connector at a new endpoint URL?
  - id: identity_DeleteApiConnector
    intent: Delete an API connector
    question: Can I remove an API connector my sign-up flow no longer calls?
  - id: identity.apiConnector_uploadClientCertificate
    intent: Upload a client certificate to an API connector
    question: How do I set up certificate authentication on an API connector with a .pfx file?
  - id: identity.apiConnector_GetCount
    intent: Count API connectors
    question: How many API connectors are set up in my tenant?
  phrasing_ops: 7
  slug: azure-ad-identity-identityapiconnector-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityContainer API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identity.identitycontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity Container API
  phrasing_intents:
  - id: identity.identityContainer_GetIdentityContainer
    intent: Get the tenant's identity configuration container
    question: What identity settings, like user flows, identity providers and conditional access, sit under the identity container?
  - id: identity.identityContainer_UpdateIdentityContainer
    intent: Update the tenant's identity configuration container
    question: Can I update identity providers or user flow attributes through the identity container?
  phrasing_ops: 2
  slug: azure-ad-identity-identitycontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityProviderBase API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for identity.identityproviderbase.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity Provider Base API
  phrasing_intents:
  - id: identity_ListIdentityProvider
    intent: List configured identity providers
    question: Which identity providers, like Google or SAML federation, are configured in my tenant?
  - id: identity_CreateIdentityProvider
    intent: Configure a new identity provider
    question: How do I add a social identity provider so users can sign in with it?
  - id: identity_GetIdentityProvider
    intent: Get a configured identity provider
    question: How do I look up the settings of one identity provider in my tenant?
  - id: identity_UpdateIdentityProvider
    intent: Update an identity provider
    question: How do I rename or reconfigure an identity provider I already set up?
  - id: identity_DeleteIdentityProvider
    intent: Delete an identity provider
    question: How do I stop users signing in with a social provider I configured?
  - id: identity.identityProvider_GetCount
    intent: Count configured identity providers
    question: How many identity providers are configured in my tenant?
  - id: identity.identityProvider_availableProviderType
    intent: List identity provider types the directory supports
    question: Which kinds of identity providers can I add to my directory?
  phrasing_ops: 7
  slug: azure-ad-identity-identityproviderbase-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityUserFlowAttribute API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identity.identityuserflowattribute.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity User Flow Attribute API
  phrasing_intents:
  - id: identity_ListUserFlowAttribute
    intent: List user flow attributes
    question: Which built-in and custom attributes can I collect in my sign-up user flows?
  - id: identity_CreateUserFlowAttribute
    intent: Create a custom user flow attribute
    question: How do I add a custom attribute to collect during user sign-up?
  - id: identity_GetUserFlowAttribute
    intent: Get one user flow attribute
    question: What data type and description does a specific user flow attribute have?
  - id: identity_UpdateUserFlowAttribute
    intent: Update a custom user flow attribute
    question: Can I change the description of a custom user flow attribute?
  - id: identity_DeleteUserFlowAttribute
    intent: Delete a custom user flow attribute
    question: Can I delete a custom attribute I no longer collect in user flows?
  - id: identity.userFlowAttribute_GetCount
    intent: Count user flow attributes
    question: How many user flow attributes are defined in my tenant?
  phrasing_ops: 6
  slug: azure-ad-identity-identityuserflowattribute-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityVerifiedIdRoot API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for identity.identityverifiedidroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity Verified ID Root API
  phrasing_intents:
  - id: identity_GetVerifiedId
    intent: Get the Verified ID root configuration
    question: How do I read the tenant's Verified ID entry point in Microsoft Entra?
  - id: identity_UpdateVerifiedId
    intent: Update the Verified ID root object
    question: Can I patch the tenant-level Verified ID object and its profiles in one call?
  - id: identity_DeleteVerifiedId
    intent: Delete the Verified ID root object
    question: Can I remove the whole Verified ID entry point from my tenant's identity settings?
  - id: identity.verifiedId_ListProfile
    intent: List Verified ID profiles
    question: Which Verified ID profiles are configured in my tenant?
  - id: identity.verifiedId_CreateProfile
    intent: Create a Verified ID profile
    question: How do I set up a new Verified ID profile with Face Check?
  - id: identity.verifiedId_GetProfile
    intent: Get a Verified ID profile
    question: How do I read one Verified ID profile's settings and relationships?
  - id: identity.verifiedId_UpdateProfile
    intent: Update a Verified ID profile
    question: Can I change the state or priority of an existing Verified ID profile?
  - id: identity.verifiedId_DeleteProfile
    intent: Delete a Verified ID profile
    question: How do I delete a Verified ID profile I no longer need?
  phrasing_ops: 9
  slug: azure-ad-identity-identityverifiedidroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.riskPreventionContainer API from Microsoft Entra ID (formerly Azure AD) — 12 operation(s) for identity.riskpreventioncontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity.risk Prevention Container API
  phrasing_intents:
  - id: identity_GetRiskPrevention
    intent: Get fraud and risk prevention settings
    question: Where do I see my tenant's fraud and risk prevention configuration for External ID?
  - id: identity_UpdateRiskPrevention
    intent: Update the risk prevention configuration
    question: How do I change the fraud protection and firewall providers in one update to the risk prevention container?
  - id: identity_DeleteRiskPrevention
    intent: Delete the risk prevention configuration
    question: Can I wipe the whole risk prevention configuration from my tenant?
  - id: identity.riskPrevention_ListFraudProtectionProvider
    intent: List fraud protection providers
    question: Which fraud protection providers are connected to my External ID tenant?
  - id: identity.riskPrevention_CreateFraudProtectionProvider
    intent: Add a fraud protection provider
    question: How do I connect a new fraud protection provider to my sign-up flows?
  - id: identity.riskPrevention_GetFraudProtectionProvider
    intent: Get a fraud protection provider
    question: How do I look up the settings of one fraud protection provider by ID?
  - id: identity.riskPrevention_UpdateFraudProtectionProvider
    intent: Update a fraud protection provider
    question: How do I rename or reconfigure an existing fraud protection provider?
  - id: identity.riskPrevention_DeleteFraudProtectionProvider
    intent: Delete a fraud protection provider
    question: How do I disconnect a fraud protection provider I no longer use?
  phrasing_ops: 23
  slug: azure-ad-identity-riskpreventioncontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.accessPackageCatalog API from Microsoft Entra ID (formerly Azure AD) — 146 operation(s) for identitygovernance.accesspackagecatalog.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.access Package Catalog API
  phrasing_intents:
  - id: identityGovernance_ListCatalog
    intent: List access package catalogs
    question: Which access package catalogs exist in my Entra ID tenant?
  - id: identityGovernance_CreateCatalog
    intent: Create an access package catalog
    question: How do I set up a new catalog to hold access packages?
  - id: identityGovernance_GetCatalog
    intent: Get one access package catalog
    question: What are the settings of a specific access package catalog?
  - id: identityGovernance_UpdateCatalog
    intent: Update an access package catalog
    question: How do I rename an existing access package catalog?
  - id: identityGovernance_DeleteCatalog
    intent: Delete an access package catalog
    question: Can I remove an access package catalog I no longer use?
  - id: identityGovernance.catalog_ListAccessPackage
    intent: List the access packages in a catalog
    question: Which access packages live inside a given catalog?
  - id: identityGovernance.catalog_GetAccessPackage
    intent: Get an access package from a catalog
    question: How can I look up one access package through its catalog?
  - id: identityGovernance.catalog.accessPackage_GetCount
    intent: Count the access packages in a catalog
    question: How many access packages does a catalog contain?
  phrasing_ops: 252
  slug: azure-ad-identitygovernance-accesspackagecatalog-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.accessReviewSet API from Microsoft Entra ID (formerly Azure AD) — 45 operation(s) for identitygovernance.accessreviewset.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.access Review Set API
  phrasing_intents:
  - id: identityGovernance_GetAccessReview
    intent: Get the tenant's access review container
    question: What does the top-level access reviews object in identity governance contain?
  - id: identityGovernance_UpdateAccessReview
    intent: Update the access review container
    question: Can I patch the access review set root in one call instead of each definition?
  - id: identityGovernance_DeleteAccessReview
    intent: Delete the access review container
    question: Is it possible to remove the whole access reviews navigation property from identity governance?
  - id: identityGovernance.accessReview_ListDefinition
    intent: List access review schedule definitions
    question: Which access review series are set up in our Entra tenant?
  - id: identityGovernance.accessReview_CreateDefinition
    intent: Create a new access review series
    question: How do I schedule a recurring access review of a group's members?
  - id: identityGovernance.accessReview_GetDefinition
    intent: Get one access review schedule definition
    question: How can I see the scope, reviewers and settings of a specific access review series?
  - id: identityGovernance.accessReview_SetDefinition
    intent: Replace an access review schedule definition
    question: Can I change the reviewers or recurrence of an access review series that already exists?
  - id: identityGovernance.accessReview_DeleteDefinition
    intent: Delete an access review series
    question: How do I permanently remove an access review series from Entra?
  phrasing_ops: 77
  slug: azure-ad-identitygovernance-accessreviewset-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.appConsentApprovalRoute API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for identitygovernance.appconsentapprovalroute.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.app Consent Approval Route API
  phrasing_intents:
  - id: identityGovernance_GetAppConsent
    intent: Get the app consent approval container
    question: What sits under the app consent section of identity governance?
  - id: identityGovernance_UpdateAppConsent
    intent: Update the app consent approval container
    question: How do I patch the appConsent root under identity governance?
  - id: identityGovernance_DeleteAppConsent
    intent: Delete the app consent approval container
    question: Is it possible to remove the whole appConsent navigation property from identity governance?
  - id: identityGovernance.appConsent_ListAppConsentRequest
    intent: List admin consent requests for apps
    question: Which apps have users asked an admin to approve access for?
  - id: identityGovernance.appConsent_CreateAppConsentRequest
    intent: Create an app consent request
    question: How do I open a new admin consent request for an app?
  - id: identityGovernance.appConsent_GetAppConsentRequest
    intent: Get an app consent request
    question: Which scopes are pending on one specific app consent request?
  - id: identityGovernance.appConsent_UpdateAppConsentRequest
    intent: Update an app consent request
    question: How do I change the pending scopes on an existing app consent request?
  - id: identityGovernance.appConsent_DeleteAppConsentRequest
    intent: Delete an app consent request
    question: How do I get rid of an app consent request that's no longer needed?
  phrasing_ops: 26
  slug: azure-ad-identitygovernance-appconsentapprovalroute-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.entitlementManagement API from Microsoft Entra ID (formerly Azure AD) — 737 operation(s) for identitygovernance.entitlementmanagement.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.entitlement Management API
  phrasing_intents:
  - id: identityGovernance_GetEntitlementManagement
    intent: Read the entitlement management container
    question: What does the entitlement management root object in Microsoft Entra identity governance contain?
  - id: identityGovernance_UpdateEntitlementManagement
    intent: Update the entitlement management container
    question: Can I patch the entitlement management root object directly?
  - id: identityGovernance_DeleteEntitlementManagement
    intent: Delete the entitlement management container
    question: Is it possible to remove the whole entitlement management navigation property from identity governance?
  - id: identityGovernance.entitlementManagement_ListAccessPackageAssignmentApproval
    intent: List access package assignment approvals
    question: Which access package assignment approvals exist in entitlement management?
  - id: identityGovernance.entitlementManagement_CreateAccessPackageAssignmentApproval
    intent: Create an assignment approval record
    question: Can I add a new approval object under access package assignment approvals?
  - id: identityGovernance.entitlementManagement_GetAccessPackageAssignmentApproval
    intent: Get an assignment approval by ID
    question: How do I look up one approval using the ID of an access package assignment request?
  - id: identityGovernance.entitlementManagement_UpdateAccessPackageAssignmentApproval
    intent: Update an assignment approval
    question: Can I patch an existing assignment approval object, for example its stages?
  - id: identityGovernance.entitlementManagement_DeleteAccessPackageAssignmentApproval
    intent: Delete an assignment approval
    question: Can an access package assignment approval object be deleted?
  phrasing_ops: 1265
  slug: azure-ad-identitygovernance-entitlementmanagement-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.identityGovernance API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identitygovernance.identitygovernance.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.identity Governance API
  phrasing_intents:
  - id: identityGovernance_GetIdentityGovernance
    intent: Get the identity governance container
    question: What identity governance features, like access reviews and lifecycle workflows, are available in my tenant?
  - id: identityGovernance_UpdateIdentityGovernance
    intent: Update the identity governance container
    question: Can I patch terms of use or entitlement management settings through the top-level governance object?
  phrasing_ops: 2
  slug: azure-ad-identitygovernance-identitygovernance-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.lifecycleWorkflowsContainer API from Microsoft Entra ID (formerly Azure AD) — 311 operation(s) for identitygovernance.lifecycleworkflowscontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.lifecycle Workflows Container API
  phrasing_intents:
  - id: identityGovernance_GetLifecycleWorkflow
    intent: Get the lifecycle workflows container
    question: What does the lifecycle workflows container in Microsoft Entra ID Governance hold?
  - id: identityGovernance_UpdateLifecycleWorkflow
    intent: Update the lifecycle workflows container
    question: Can I patch the lifecycle workflows container's settings in one request?
  - id: identityGovernance_DeleteLifecycleWorkflow
    intent: Delete the lifecycle workflows container
    question: Is it possible to remove the whole lifecycle workflows navigation property from identity governance?
  - id: identityGovernance.lifecycleWorkflow_ListCustomTaskExtension
    intent: List custom task extensions
    question: Which custom task extensions are configured for my lifecycle workflows?
  - id: identityGovernance.lifecycleWorkflow_CreateCustomTaskExtension
    intent: Create a custom task extension
    question: How do I create a new custom task extension for lifecycle workflows?
  - id: identityGovernance.lifecycleWorkflow_GetCustomTaskExtension
    intent: Get a custom task extension
    question: What are the properties of a specific custom task extension?
  - id: identityGovernance.lifecycleWorkflow_UpdateCustomTaskExtension
    intent: Update a custom task extension
    question: How do I change the callback configuration on an existing custom task extension?
  - id: identityGovernance.lifecycleWorkflow_DeleteCustomTaskExtension
    intent: Delete a custom task extension
    question: Can I delete a custom task extension that tasks still reference?
  phrasing_ops: 363
  slug: azure-ad-identitygovernance-lifecycleworkflowscontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.privilegedAccessRoot API from Microsoft Entra ID (formerly Azure AD) — 64 operation(s) for identitygovernance.privilegedaccessroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.privileged Access Root API
  phrasing_intents:
  - id: identityGovernance_GetPrivilegedAccess
    intent: Get the privileged access root
    question: What does the privileged access root in identity governance expose?
  - id: identityGovernance_UpdatePrivilegedAccess
    intent: Update the privileged access root
    question: Can I patch the privileged access root object?
  - id: identityGovernance_DeletePrivilegedAccess
    intent: Delete the privileged access root
    question: Can I remove the privilegedAccess navigation property from identity governance?
  - id: identityGovernance.privilegedAccess_GetGroup
    intent: Get the PIM for Groups container
    question: Where do I find the groups governed by Privileged Identity Management?
  - id: identityGovernance.privilegedAccess_UpdateGroup
    intent: Update the PIM for Groups container
    question: Can I patch the PIM for Groups container in one request?
  - id: identityGovernance.privilegedAccess_DeleteGroup
    intent: Delete the PIM for Groups container
    question: Can I delete the PIM for Groups navigation property?
  - id: identityGovernance.privilegedAccess.group_ListAssignmentApproval
    intent: List PIM group assignment approvals
    question: Which approvals exist for PIM group assignment requests?
  - id: identityGovernance.privilegedAccess.group_CreateAssignmentApproval
    intent: Create a PIM group assignment approval
    question: Can I create a new approval object for PIM group assignments?
  phrasing_ops: 92
  slug: azure-ad-identitygovernance-privilegedaccessroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.termsOfUseContainer API from Microsoft Entra ID (formerly Azure AD) — 23 operation(s) for identitygovernance.termsofusecontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.terms Of Use Container API
  phrasing_intents:
  - id: identityGovernance_GetTermsGraphOPreUse
    intent: Get the terms of use container
    question: How do I read the top-level terms of use container in identity governance?
  - id: identityGovernance_UpdateTermsGraphOPreUse
    intent: Update the terms of use container
    question: How do I update the terms of use container itself rather than a single agreement?
  - id: identityGovernance_DeleteTermsGraphOPreUse
    intent: Delete the terms of use container
    question: What happens if I delete the whole terms of use container from identity governance?
  - id: identityGovernance.termsGraphOPreUse_ListAgreementAcceptance
    intent: List all terms of use acceptances tenant-wide
    question: Which users have accepted or declined any terms of use across the whole tenant?
  - id: identityGovernance.termsGraphOPreUse_CreateAgreementAcceptance
    intent: Record a tenant-level agreement acceptance
    question: Can I add an acceptance record to the tenant-wide agreement acceptances collection?
  - id: identityGovernance.termsGraphOPreUse_GetAgreementAcceptance
    intent: Get a tenant-level agreement acceptance
    question: How do I look up one acceptance record from the tenant-wide terms of use acceptances?
  - id: identityGovernance.termsGraphOPreUse_UpdateAgreementAcceptance
    intent: Update a tenant-level agreement acceptance
    question: Is it possible to change the state of an acceptance in the tenant-wide acceptances collection?
  - id: identityGovernance.termsGraphOPreUse_DeleteAgreementAcceptance
    intent: Delete a tenant-level agreement acceptance
    question: Can I remove a record from the tenant-wide agreement acceptances collection?
  phrasing_ops: 48
  slug: azure-ad-identitygovernance-termsofusecontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.identityProtectionRoot API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identityprotection.identityprotectionroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.identity Protection Root API
  phrasing_intents:
  - id: identityProtection.identityProtectionRoot_GetIdentityProtectionRoot
    intent: Get the identity protection root
    question: What risk data does Entra ID Protection expose at its top level?
  - id: identityProtection.identityProtectionRoot_UpdateIdentityProtectionRoot
    intent: Update the identity protection root
    question: How do I patch the identity protection root object?
  phrasing_ops: 2
  slug: azure-ad-identityprotection-identityprotectionroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.riskDetection API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identityprotection.riskdetection.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.risk Detection API
  phrasing_intents:
  - id: identityProtection_ListRiskDetection
    intent: List identity risk detections
    question: What risky sign-in and user risk detections has Identity Protection flagged?
  - id: identityProtection_CreateRiskDetection
    intent: Add a risk detection record
    question: Can I create a risk detection entry for a user?
  - id: identityProtection_GetRiskDetection
    intent: Get one risk detection
    question: What location, IP and risk type are behind a particular risk detection?
  - id: identityProtection_UpdateRiskDetection
    intent: Update a risk detection
    question: Can I change the risk state or risk level recorded on a detection?
  - id: identityProtection_DeleteRiskDetection
    intent: Delete a risk detection
    question: Can I remove a risk detection record?
  - id: identityProtection.riskDetection_GetCount
    intent: Count identity risk detections
    question: How many risk detections has Identity Protection recorded?
  phrasing_ops: 6
  slug: azure-ad-identityprotection-riskdetection-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.riskyServicePrincipal API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for identityprotection.riskyserviceprincipal.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.risky Service Principal API
  phrasing_intents:
  - id: identityProtection_ListRiskyServicePrincipal
    intent: List risky service principals
    question: Which service principals has Identity Protection flagged as risky in my tenant?
  - id: identityProtection_CreateRiskyServicePrincipal
    intent: Add a risky service principal record
    question: Is it possible to create a new riskyServicePrincipal entry directly in Identity Protection?
  - id: identityProtection_GetRiskyServicePrincipal
    intent: Get a risky service principal
    question: What is the current risk level and risk detail for one specific risky service principal?
  - id: identityProtection_UpdateRiskyServicePrincipal
    intent: Update a risky service principal record
    question: Can I change the risk state or risk level stored on one risky service principal record?
  - id: identityProtection_DeleteRiskyServicePrincipal
    intent: Delete a risky service principal record
    question: Can I remove a riskyServicePrincipal object from Identity Protection entirely?
  - id: identityProtection.riskyServicePrincipal_ListHistory
    intent: List a risky service principal's risk history
    question: What is the risk history of a flagged service principal over time?
  - id: identityProtection.riskyServicePrincipal_CreateHistory
    intent: Add a risk history item to a service principal
    question: Can I append a new entry to a risky service principal's risk history?
  - id: identityProtection.riskyServicePrincipal_GetHistory
    intent: Get one risk history item for a service principal
    question: How do I read a single entry from a risky service principal's risk history?
  phrasing_ops: 14
  slug: azure-ad-identityprotection-riskyserviceprincipal-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.riskyUser API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for identityprotection.riskyuser.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.risky User API
  phrasing_intents:
  - id: identityProtection_ListRiskyUser
    intent: List users flagged as risky
    question: Which users in my tenant has Identity Protection flagged as risky?
  - id: identityProtection_CreateRiskyUser
    intent: Create a risky user record
    question: Can I add a new riskyUser entry to Identity Protection myself?
  - id: identityProtection_GetRiskyUser
    intent: Get one risky user's risk details
    question: What is a specific user's current risk level and why were they flagged?
  - id: identityProtection_UpdateRiskyUser
    intent: Update a risky user record's properties
    question: Can I edit the properties on an existing risky user record directly?
  - id: identityProtection_DeleteRiskyUser
    intent: Delete a risky user record
    question: Can I remove a user's riskyUser record from Identity Protection entirely?
  - id: identityProtection.riskyUser_ListHistory
    intent: List a risky user's risk history
    question: How has a user's risk level changed over time?
  - id: identityProtection.riskyUser_CreateHistory
    intent: Add an entry to a risky user's history
    question: Can I append a history item to a risky user's record?
  - id: identityProtection.riskyUser_GetHistory
    intent: Get one entry from a risky user's history
    question: What happened in one specific risk-change event for a user?
  phrasing_ops: 15
  slug: azure-ad-identityprotection-riskyuser-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.servicePrincipalRiskDetection API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identityprotection.serviceprincipalriskdetection.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.service Principal Risk Detection API
  phrasing_intents:
  - id: identityProtection_ListServicePrincipalRiskDetection
    intent: List service principal risk detections
    question: Which risky activities has Identity Protection detected for my apps' service principals?
  - id: identityProtection_CreateServicePrincipalRiskDetection
    intent: Create a service principal risk detection
    question: Can I record a new risk detection against a service principal?
  - id: identityProtection_GetServicePrincipalRiskDetection
    intent: Get a service principal risk detection
    question: What details, like location and detection time, does one service principal risk detection hold?
  - id: identityProtection_UpdateServicePrincipalRiskDetection
    intent: Update a service principal risk detection
    question: Can I change the risk state of a service principal risk detection after review?
  - id: identityProtection_DeleteServicePrincipalRiskDetection
    intent: Delete a service principal risk detection
    question: Can I delete a risk detection recorded against a service principal?
  - id: identityProtection.servicePrincipalRiskDetection_GetCount
    intent: Count service principal risk detections
    question: How many risk detections are there for service principals in my tenant?
  phrasing_ops: 6
  slug: azure-ad-identityprotection-serviceprincipalriskdetection-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProviders.identityProvider API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identityproviders.identityprovider.
  name: Microsoft Entra ID (formerly Azure AD) Identity Providers.identity Provider API
  phrasing_intents:
  - id: identityProvider_ListIdentityProvider
    intent: List identity providers (deprecated endpoint)
    question: Which external identity providers are configured in my directory on the deprecated endpoint?
  - id: identityProvider_CreateIdentityProvider
    intent: Add an identity provider (deprecated endpoint)
    question: Can I register a new social identity provider with a client ID and secret?
  - id: identityProvider_GetIdentityProvider
    intent: Get one identity provider (deprecated endpoint)
    question: How can I read the settings of one existing identity provider?
  - id: identityProvider_UpdateIdentityProvider
    intent: Update an identity provider (deprecated endpoint)
    question: How do I rotate the client secret on an existing identity provider?
  - id: identityProvider_DeleteIdentityProvider
    intent: Delete an identity provider (deprecated endpoint)
    question: Can I remove an identity provider users no longer sign in with?
  - id: identityProvider_GetCount
    intent: Count identity providers
    question: How many identity providers are configured in the tenant?
  phrasing_ops: 6
  slug: azure-ad-identityproviders-identityprovider-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProviders.identityProvider.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identityproviders.identityprovider.functions.
  name: Microsoft Entra ID (formerly Azure AD) Identity Providers.identity Provider.Functions API
  phrasing_intents:
  - id: identityProvider_availableProviderType
    intent: List available identity provider types
    question: Which identity provider types are available in my directory?
  phrasing_ops: 1
  slug: azure-ad-identityproviders-identityprovider-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The informationProtection.bitlocker API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for informationprotection.bitlocker.
  name: Microsoft Entra ID (formerly Azure AD) Information Protection.bitlocker API
  phrasing_intents:
  - id: informationProtection_GetBitlocker
    intent: Get the BitLocker information protection root
    question: Where does Microsoft Graph expose BitLocker data under information protection?
  - id: informationProtection.bitlocker_ListRecoveryKey
    intent: List BitLocker recovery keys
    question: Which BitLocker recovery keys are stored in my tenant, and for which devices?
  - id: informationProtection.bitlocker_GetRecoveryKey
    intent: Get a BitLocker recovery key
    question: How do I retrieve the BitLocker recovery key for a locked-out drive?
  - id: informationProtection.bitlocker.recoveryKey_GetCount
    intent: Count BitLocker recovery keys
    question: How many BitLocker recovery keys are escrowed in my directory?
  phrasing_ops: 4
  slug: azure-ad-informationprotection-bitlocker-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The informationProtection.informationProtection API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for informationprotection.informationprotection.
  name: Microsoft Entra ID (formerly Azure AD) Information Protection.information Protection API
  phrasing_intents:
  - id: informationProtection_GetInformationProtection
    intent: Get the information protection settings
    question: Where do I read the tenant's information protection resource, including BitLocker?
  - id: informationProtection_UpdateInformationProtection
    intent: Update the information protection settings
    question: How do I change the information protection resource for my tenant?
  phrasing_ops: 2
  slug: azure-ad-informationprotection-informationprotection-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The informationProtection.threatAssessmentRequest API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for informationprotection.threatassessmentrequest.
  name: Microsoft Entra ID (formerly Azure AD) Information Protection.threat Assessment Request API
  phrasing_intents:
  - id: informationProtection_ListThreatAssessmentRequest
    intent: List threat assessment requests
    question: Which threat assessment requests have been submitted in our tenant?
  - id: informationProtection_CreateThreatAssessmentRequest
    intent: Submit a threat assessment request
    question: How do I report a suspicious email, URL or file for a threat assessment?
  - id: informationProtection_GetThreatAssessmentRequest
    intent: Get a threat assessment request
    question: What is the status of a threat assessment I submitted?
  - id: informationProtection_UpdateThreatAssessmentRequest
    intent: Update a threat assessment request
    question: Is it possible to change the category or expected verdict on a threat assessment I already filed?
  - id: informationProtection_DeleteThreatAssessmentRequest
    intent: Delete a threat assessment request
    question: Can I withdraw a threat assessment request I no longer need?
  - id: informationProtection.threatAssessmentRequest_ListResult
    intent: List results of a threat assessment
    question: What did the threat assessment conclude for my submission?
  - id: informationProtection.threatAssessmentRequest_CreateResult
    intent: Add a result to a threat assessment
    question: How do I attach a new result message to a threat assessment request?
  - id: informationProtection.threatAssessmentRequest_GetResult
    intent: Get one threat assessment result
    question: How do I read one specific result from a threat assessment?
  phrasing_ops: 12
  slug: azure-ad-informationprotection-threatassessmentrequest-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The invitations.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for invitations.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Invitations.directory Object API
  phrasing_intents:
  - id: invitation_ListInvitedUserSponsor
    intent: List sponsors of invited guest users
    question: Which users or groups are sponsoring the guests we've invited?
  - id: invitation_GetInvitedUserSponsor
    intent: Get one sponsor of an invited user
    question: How do I look up the details of a single guest sponsor by its object id?
  - id: invitation.invitedUserSponsor_GetCount
    intent: Count invited-user sponsors
    question: How many sponsors are assigned to invited guest users?
  phrasing_ops: 3
  slug: azure-ad-invitations-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The invitations.invitation API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for invitations.invitation.
  name: Microsoft Entra ID (formerly Azure AD) Invitations.invitation API
  phrasing_intents:
  - id: invitation_ListInvitation
    intent: List guest invitations
    question: Which guest invitations has my tenant sent?
  - id: invitation_CreateInvitation
    intent: Invite an external guest user
    question: How do I invite a partner to our tenant as a guest?
  - id: invitation_GetCount
    intent: Count guest invitations
    question: How many guest invitations exist?
  phrasing_ops: 3
  slug: azure-ad-invitations-invitation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The invitations.user API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for invitations.user.
  name: Microsoft Entra ID (formerly Azure AD) Invitations.user API
  phrasing_intents:
  - id: invitation_GetInvitedUser
    intent: Get the user created by an invitation
    question: Which user was created when an invitation was sent?
  - id: invitation.invitedUser_GetMailboxSetting
    intent: Get the invited user's mailbox settings
    question: What mailbox settings does the invited user have?
  - id: invitation.invitedUser_UpdateMailboxSetting
    intent: Update the invited user's mailbox settings
    question: How do I change the invited user's mailbox time zone?
  - id: invitation.invitedUser_ListServiceProvisioningError
    intent: List the invited user's provisioning errors
    question: What provisioning errors has a federated service reported for the invited user?
  - id: invitation.invitedUser.ServiceProvisioningError_GetCount
    intent: Count the invited user's provisioning errors
    question: How many service provisioning errors does the invited user have?
  phrasing_ops: 5
  slug: azure-ad-invitations-user-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on the signed-in user
  name: Azure Active Directory Me API
  phrasing_intents:
  - id: getMe
    intent: Get the signed-in user's profile
    question: How do I find out who is signed in with the current access token?
  - id: getMyPhoto
    intent: Download the signed-in user's profile photo
    question: How can I download my own profile picture as image bytes?
  phrasing_ops: 2
  slug: azure-ad-me-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The oauth2PermissionGrants.oAuth2PermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for oauth2permissiongrants.oauth2permissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Oauth2 Permission Grants.o Auth2 Permission Grant API
  phrasing_intents:
  - id: oauth2PermissionGrant_ListOAuth2PermissionGrant
    intent: List delegated permission grants
    question: Which client apps have been granted delegated permissions to call APIs for signed-in users?
  - id: oauth2PermissionGrant_CreateOAuth2PermissionGrant
    intent: Grant delegated permissions to a client app
    question: How do I programmatically consent to delegated scopes for an app on behalf of all users?
  - id: oauth2PermissionGrant_GetOAuth2PermissionGrant
    intent: Get one delegated permission grant
    question: What scopes does a specific delegated permission grant cover?
  - id: oauth2PermissionGrant_UpdateOAuth2PermissionGrant
    intent: Change the scopes on a delegated grant
    question: Can I add or remove scopes on a consent grant that already exists?
  - id: oauth2PermissionGrant_DeleteOAuth2PermissionGrant
    intent: Revoke a delegated permission grant
    question: How do I revoke consent an app was given to act on users' behalf?
  - id: oauth2PermissionGrant_GetCount
    intent: Count delegated permission grants
    question: How many delegated permission grants exist across my tenant?
  phrasing_ops: 6
  slug: azure-ad-oauth2permissiongrants-oauth2permissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The oauth2PermissionGrants.oAuth2PermissionGrant.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for oauth2permissiongrants.oauth2permissiongrant.functions.
  name: Microsoft Entra ID (formerly Azure AD) Oauth2 Permission Grants.o Auth2 Permission Grant.Functions API
  phrasing_intents:
  - id: oauth2PermissionGrant_delta
    intent: Track changes to delegated permission grants
    question: Which delegated permission grants were added, changed or removed since my last sync?
  phrasing_ops: 1
  slug: azure-ad-oauth2permissiongrants-oauth2permissiongrant-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.certificateBasedAuthConfiguration API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for organization.certificatebasedauthconfiguration.
  name: Microsoft Entra ID (formerly Azure AD) Organization.certificate Based Auth Configuration API
  phrasing_intents:
  - id: organization_ListCertificateBasedAuthConfiguration
    intent: List certificate-based auth configurations
    question: Which certificate authorities are trusted for certificate-based sign-in in my organization?
  - id: organization_CreateCertificateBasedAuthConfiguration
    intent: Create a certificate-based auth configuration
    question: How do I upload my certificate authorities to enable certificate-based authentication in Entra ID?
  - id: organization_GetCertificateBasedAuthConfiguration
    intent: Get one certificate-based auth configuration
    question: What certificate authorities are in a specific certificate-based auth configuration?
  - id: organization_DeleteCertificateBasedAuthConfiguration
    intent: Delete a certificate-based auth configuration
    question: How do I remove the trusted CA configuration for certificate sign-in?
  - id: organization.certificateBasedAuthConfiguration_GetCount
    intent: Count certificate-based auth configurations
    question: How many certificate-based auth configurations does my organization have?
  phrasing_ops: 5
  slug: azure-ad-organization-certificatebasedauthconfiguration-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for organization.extension.
  name: Microsoft Entra ID (formerly Azure AD) Organization.extension API
  phrasing_intents:
  - id: organization_ListExtension
    intent: List open extensions on the organization
    question: What custom open extensions have been added to our organization object?
  - id: organization_CreateExtension
    intent: Add an open extension to the organization
    question: How do I attach custom data to my tenant's organization object?
  - id: organization_GetExtension
    intent: Get one open extension on the organization
    question: How do I read back the custom data stored in one particular organization extension?
  - id: organization_UpdateExtension
    intent: Update an existing organization extension
    question: How do I change the data in an open extension that already exists on the organization?
  - id: organization_DeleteExtension
    intent: Delete an open extension from the organization
    question: Can I remove a custom extension I no longer need from the organization object?
  - id: organization.extension_GetCount
    intent: Count the organization's open extensions
    question: How many open extensions are defined on our organization?
  phrasing_ops: 6
  slug: azure-ad-organization-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.organization.Actions API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for organization.organization.actions.
  name: Microsoft Entra ID (formerly Azure AD) Organization.organization.Actions API
  phrasing_intents:
  - id: organization_checkMemberGroup
    intent: Check an organization's membership in groups
    question: Is this directory object a member of any of these specific groups?
  - id: organization_checkMemberObject
    intent: Check an organization's membership in objects
    question: Can I check membership against a mixed list of groups, roles and administrative units?
  - id: organization_getMemberGroup
    intent: Get all groups an organization belongs to
    question: What groups does an organization object belong to, including transitive membership?
  - id: organization_getMemberObject
    intent: Get groups, units and roles an org belongs to
    question: Which groups, administrative units and directory roles is an organization object a member of?
  - id: organization_restore
    intent: Restore a deleted directory object
    question: How do I restore a recently deleted user, group or application from deleted items?
  - id: organization_setMobileDeviceManagementAuthority
    intent: Set the mobile device management authority
    question: How do I set the mobile device management authority for my organization?
  - id: organization_getAvailableExtensionProperty
    intent: List available directory extension properties
    question: Which directory extension properties are registered in my tenant, including from multitenant apps?
  - id: organization_getGraphBPreId
    intent: Get directory objects by their IDs
    question: How do I resolve a batch of object IDs to users, groups and devices in one call?
  phrasing_ops: 9
  slug: azure-ad-organization-organization-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.organization API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for organization.organization.
  name: Microsoft Entra ID (formerly Azure AD) Organization.organization API
  phrasing_intents:
  - id: organization_ListOrganization
    intent: List the tenant's organization
    question: What organization details are on record for my Microsoft Entra tenant?
  - id: organization_CreateOrganization
    intent: Add an organization entity
    question: Is there an endpoint to add a new organization entity?
  - id: organization_GetOrganization
    intent: Get the organization's properties
    question: What address, phone and technical contacts does my organization have on file?
  - id: organization_UpdateOrganization
    intent: Update the organization's settings
    question: How do I change who gets technical notification emails for my tenant?
  - id: organization_DeleteOrganization
    intent: Delete an organization entity
    question: Can the organization entity be deleted through this endpoint?
  - id: organization_GetCount
    intent: Count organization entities
    question: How many organization objects does the tenant return?
  phrasing_ops: 6
  slug: azure-ad-organization-organization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.organizationalBranding API from Microsoft Entra ID (formerly Azure AD) — 18 operation(s) for organization.organizationalbranding.
  name: Microsoft Entra ID (formerly Azure AD) Organization.organizational Branding API
  phrasing_intents:
  - id: organization_GetBranding
    intent: Get the organization's default sign-in branding
    question: What sign-in page text and username hint does our default company branding use?
  - id: organization_UpdateBranding
    intent: Update the default organizational branding
    question: How do I change our default sign-in branding properties?
  - id: organization_DeleteBranding
    intent: Delete the default organizational branding
    question: Can I wipe out our default company branding entirely?
  - id: organization_GetBrandingBackgroundImage
    intent: Download the default sign-in background image
    question: What background picture is shown behind our default sign-in page?
  - id: organization_SetBrandingBackgroundImage
    intent: Upload the default sign-in background image
    question: What size limits apply to a sign-in background image, like the 1920 × 1080 maximum?
  - id: organization_DeleteBrandingBackgroundImage
    intent: Remove the default sign-in background image
    question: Can I get rid of the custom background on our default sign-in page?
  - id: organization_GetBrandingBannerLogo
    intent: Download the default banner logo
    question: Which banner version of our company logo appears on the default sign-in page?
  - id: organization_SetBrandingBannerLogo
    intent: Upload the default banner logo
    question: What dimensions are allowed for a sign-in banner logo, like the 36 × 245 limit?
  phrasing_ops: 51
  slug: azure-ad-organization-organizationalbranding-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.activityBasedTimeoutPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.activitybasedtimeoutpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.activity Based Timeout Policy API
  phrasing_intents:
  - id: policy_ListActivityBasedTimeoutPolicy
    intent: List activity-based timeout policies
    question: Which idle session timeout policies are defined in my tenant?
  - id: policy_CreateActivityBasedTimeoutPolicy
    intent: Create an activity-based timeout policy
    question: How do I set up automatic sign-out after inactivity for web apps?
  - id: policy_GetActivityBasedTimeoutPolicy
    intent: Get an activity-based timeout policy
    question: What are the settings of one idle session timeout policy?
  - id: policy_UpdateActivityBasedTimeoutPolicy
    intent: Update an activity-based timeout policy
    question: How do I change an existing idle session timeout policy?
  - id: policy_DeleteActivityBasedTimeoutPolicy
    intent: Delete an activity-based timeout policy
    question: How do I remove an idle session timeout policy?
  - id: policy.activityBasedTimeoutPolicy_ListAppliesTo
    intent: List objects a timeout policy applies to
    question: Which directory objects is an idle timeout policy applied to?
  - id: policy.activityBasedTimeoutPolicy_GetAppliesTo
    intent: Get one object a timeout policy applies to
    question: Is a specific directory object covered by an idle timeout policy?
  - id: policy.activityBasedTimeoutPolicy.appliesTo_GetCount
    intent: Count objects a timeout policy applies to
    question: How many objects is an idle timeout policy applied to?
  phrasing_ops: 9
  slug: azure-ad-policies-activitybasedtimeoutpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.adminConsentRequestPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.adminconsentrequestpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.admin Consent Request Policy API
  phrasing_intents:
  - id: policy_GetAdminConsentRequestPolicy
    intent: Get the admin consent request policy
    question: Is the admin consent request workflow turned on in my tenant?
  - id: policy_UpdateAdminConsentRequestPolicy
    intent: Configure admin consent requests
    question: How do I turn on admin consent requests so users can ask for app approval?
  - id: policy_DeleteAdminConsentRequestPolicy
    intent: Delete the admin consent request policy
    question: Can I delete the admin consent request policy object?
  phrasing_ops: 3
  slug: azure-ad-policies-adminconsentrequestpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.appManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.appmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.app Management Policy API
  phrasing_intents:
  - id: policy_ListAppManagementPolicy
    intent: List app management policies
    question: Which app management policies exist in my Entra tenant?
  - id: policy_CreateAppManagementPolicy
    intent: Create an app management policy
    question: How do I create a policy that limits password lifetimes on specific apps?
  - id: policy_GetAppManagementPolicy
    intent: Get an app management policy
    question: What credential restrictions does a particular app management policy enforce?
  - id: policy_UpdateAppManagementPolicy
    intent: Update an app management policy
    question: Can I switch off an existing app management policy without deleting it?
  - id: policy_DeleteAppManagementPolicy
    intent: Delete an app management policy
    question: Can I delete an app management policy I no longer need?
  - id: policy.appManagementPolicy_ListAppliesTo
    intent: List apps an app management policy applies to
    question: Which applications and service principals are assigned a given app management policy?
  - id: policy.appManagementPolicy_GetAppliesTo
    intent: Get one object an app management policy applies to
    question: Can I fetch a single app or service principal from a policy's applied-to list?
  - id: policy.appManagementPolicy.appliesTo_GetCount
    intent: Count objects an app management policy covers
    question: How many apps and service principals is an app management policy applied to?
  phrasing_ops: 9
  slug: azure-ad-policies-appmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authenticationFlowsPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.authenticationflowspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authentication Flows Policy API
  phrasing_intents:
  - id: policy_GetAuthenticationFlowsPolicy
    intent: Get the authentication flows policy
    question: Is self-service sign-up enabled for guest users in my tenant?
  - id: policy_UpdateAuthenticationFlowsPolicy
    intent: Turn self-service sign-up on or off
    question: How do I enable self-service sign-up for external users?
  - id: policy_DeleteAuthenticationFlowsPolicy
    intent: Delete the authentication flows policy
    question: Can I delete the authentication flows policy navigation property?
  phrasing_ops: 3
  slug: azure-ad-policies-authenticationflowspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authenticationMethodsPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for policies.authenticationmethodspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authentication Methods Policy API
  phrasing_intents:
  - id: policy_GetAuthenticationMethodsPolicy
    intent: Get the tenant authentication methods policy
    question: Which authentication methods are enabled for users in my tenant?
  - id: policy_UpdateAuthenticationMethodsPolicy
    intent: Update the authentication methods policy
    question: How do I change how often users must reconfirm their authentication methods?
  - id: policy_DeleteAuthenticationMethodsPolicy
    intent: Delete the authentication methods policy
    question: Can I delete the authentication methods policy object entirely?
  - id: policy.authenticationMethodsPolicy_ListAuthenticationMethodConfiguration
    intent: List authentication method configurations
    question: What's the configuration of each authentication method, like FIDO2 or SMS, in my tenant?
  - id: policy.authenticationMethodsPolicy_CreateAuthenticationMethodConfiguration
    intent: Add an authentication method configuration
    question: How do I add a new external authentication method configuration to the policy?
  - id: policy.authenticationMethodsPolicy_GetAuthenticationMethodConfiguration
    intent: Get one authentication method configuration
    question: Is a specific authentication method enabled, and who is excluded from it?
  - id: policy.authenticationMethodsPolicy_UpdateAuthenticationMethodConfiguration
    intent: Enable, disable or scope an authentication method
    question: How do I disable a specific authentication method for the whole tenant?
  - id: policy.authenticationMethodsPolicy_DeleteAuthenticationMethodConfiguration
    intent: Delete an authentication method configuration
    question: How do I remove an external authentication method from my tenant?
  phrasing_ops: 9
  slug: azure-ad-policies-authenticationmethodspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authenticationStrengthPolicy API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for policies.authenticationstrengthpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authentication Strength Policy API
  phrasing_intents:
  - id: policy_ListAuthenticationStrengthPolicy
    intent: List authentication strength policies
    question: Which authentication strengths, built-in and custom, are available in my tenant?
  - id: policy_CreateAuthenticationStrengthPolicy
    intent: Create a custom authentication strength
    question: How do I define a custom authentication strength that only allows phishing-resistant methods?
  - id: policy_GetAuthenticationStrengthPolicy
    intent: Get an authentication strength policy
    question: Which method combinations does a specific authentication strength allow?
  - id: policy_UpdateAuthenticationStrengthPolicy
    intent: Update an authentication strength's name or description
    question: How do I rename a custom authentication strength?
  - id: policy_DeleteAuthenticationStrengthPolicy
    intent: Delete a custom authentication strength
    question: How do I delete a custom authentication strength I created?
  - id: policy.authenticationStrengthPolicy_ListCombinationConfiguration
    intent: List combination configurations of a strength
    question: What extra restrictions, like specific FIDO2 key models, are set on an authentication strength?
  - id: policy.authenticationStrengthPolicy_CreateCombinationConfiguration
    intent: Add a combination configuration to a strength
    question: How do I require a specific kind of authenticator for one combination in an authentication strength?
  - id: policy.authenticationStrengthPolicy_GetCombinationConfiguration
    intent: Get one combination configuration of a strength
    question: How do I read a single combination configuration on an authentication strength?
  phrasing_ops: 14
  slug: azure-ad-policies-authenticationstrengthpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authorizationPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.authorizationpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authorization Policy API
  phrasing_intents:
  - id: policy_GetAuthorizationPolicy
    intent: Get the tenant authorization policy
    question: Who is allowed to invite guests into my Entra tenant?
  - id: policy_UpdateAuthorizationPolicy
    intent: Update the tenant authorization policy
    question: How do I restrict guest invitations to admins only?
  - id: policy_DeleteAuthorizationPolicy
    intent: Delete the authorization policy
    question: Is there a way to delete the authorization policy navigation property?
  phrasing_ops: 3
  slug: azure-ad-policies-authorizationpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.claimsMappingPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.claimsmappingpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.claims Mapping Policy API
  phrasing_intents:
  - id: policy_ListClaimsMappingPolicy
    intent: List claims-mapping policies
    question: Which claims-mapping policies are defined in our Entra tenant?
  - id: policy_CreateClaimsMappingPolicy
    intent: Create a claims-mapping policy
    question: How do I customize the claims emitted in tokens for an application?
  - id: policy_GetClaimsMappingPolicy
    intent: Get a claims-mapping policy
    question: What does a specific claims-mapping policy's definition look like?
  - id: policy_UpdateClaimsMappingPolicy
    intent: Update a claims-mapping policy
    question: Can I change the claims an existing claims-mapping policy emits?
  - id: policy_DeleteClaimsMappingPolicy
    intent: Delete a claims-mapping policy
    question: How do I remove a claims-mapping policy I no longer use?
  - id: policy.claimsMappingPolicy_ListAppliesTo
    intent: List what a claims-mapping policy applies to
    question: Which service principals is a claims-mapping policy assigned to?
  - id: policy.claimsMappingPolicy_GetAppliesTo
    intent: Get one object a claims-mapping policy targets
    question: How do I check a single directory object that a claims-mapping policy is applied to?
  - id: policy.claimsMappingPolicy.appliesTo_GetCount
    intent: Count objects a claims-mapping policy applies to
    question: How many apps or service principals use a given claims-mapping policy?
  phrasing_ops: 9
  slug: azure-ad-policies-claimsmappingpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.conditionalAccessPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for policies.conditionalaccesspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.conditional Access Policy API
  phrasing_intents:
  - id: policy_ListConditionalAccessPolicy
    intent: List conditional access policies
    question: Which conditional access policies are configured in our Microsoft Entra tenant?
  - id: policy_CreateConditionalAccessPolicy
    intent: Create a conditional access policy
    question: How do I require MFA for a set of users with a new conditional access policy?
  - id: policy_GetConditionalAccessPolicy
    intent: Get a conditional access policy
    question: What conditions and grant controls does a specific conditional access policy use?
  - id: policy_UpdateConditionalAccessPolicy
    intent: Update a conditional access policy
    question: Can I switch an existing conditional access policy from report-only to enabled?
  - id: policy_DeleteConditionalAccessPolicy
    intent: Delete a conditional access policy
    question: How do I remove a conditional access policy from the tenant?
  - id: policy.conditionalAccessPolicy_restore
    intent: Restore a deleted conditional access policy
    question: Can I bring back a conditional access policy that was deleted?
  - id: policy.conditionalAccessPolicy_GetCount
    intent: Count conditional access policies
    question: How many conditional access policies do we have?
  phrasing_ops: 7
  slug: azure-ad-policies-conditionalaccesspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.crossTenantAccessPolicy API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for policies.crosstenantaccesspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.cross Tenant Access Policy API
  phrasing_intents:
  - id: policy_GetCrossTenantAccessPolicy
    intent: View the tenant's cross-tenant access policy
    question: How do I see my tenant's overall cross-tenant access policy in Microsoft Entra ID?
  - id: policy_UpdateCrossTenantAccessPolicy
    intent: Update the top-level cross-tenant access policy
    question: Can I change which cloud endpoints are allowed for cross-tenant collaboration?
  - id: policy_DeleteCrossTenantAccessPolicy
    intent: Delete the cross-tenant access policy object
    question: Can the whole cross-tenant access policy object be deleted from the policies root?
  - id: policy.crossTenantAccessPolicy_GetDefault
    intent: View the default cross-tenant access settings
    question: What are the default inbound and outbound B2B settings that apply to tenants without a partner config?
  - id: policy.crossTenantAccessPolicy_UpdateDefault
    intent: Change default cross-tenant access settings
    question: How can I block outbound B2B collaboration by default for every external tenant?
  - id: policy.crossTenantAccessPolicy_DeleteDefault
    intent: Delete the default cross-tenant configuration
    question: Can I delete the default configuration object under the cross-tenant access policy?
  - id: policy.crossTenantAccessPolicy.default_resetToSystemDefault
    intent: Reset default cross-tenant settings to system default
    question: How do I undo all my customizations to the default cross-tenant access settings?
  - id: policy.crossTenantAccessPolicy_ListPartner
    intent: List partner-specific cross-tenant configurations
    question: Which external tenants have their own partner configuration in our cross-tenant access policy?
  phrasing_ops: 30
  slug: azure-ad-policies-crosstenantaccesspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.deviceRegistrationPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.deviceregistrationpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.device Registration Policy API
  phrasing_intents:
  - id: policy_GetDeviceRegistrationPolicy
    intent: View the device registration policy
    question: What is the device quota per user in our Microsoft Entra device registration policy?
  phrasing_ops: 1
  slug: azure-ad-policies-deviceregistrationpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.featureRolloutPolicy API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for policies.featurerolloutpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.feature Rollout Policy API
  phrasing_intents:
  - id: policy_ListFeatureRolloutPolicy
    intent: List feature rollout policies
    question: Which staged rollout policies are set up in my Entra tenant?
  - id: policy_CreateFeatureRolloutPolicy
    intent: Create a feature rollout policy
    question: How do I start a staged rollout of a feature like passthrough authentication to some users?
  - id: policy_GetFeatureRolloutPolicy
    intent: Get a feature rollout policy
    question: What feature and settings does one staged rollout policy have?
  - id: policy_UpdateFeatureRolloutPolicy
    intent: Update a feature rollout policy
    question: How do I turn off an existing staged rollout policy?
  - id: policy_DeleteFeatureRolloutPolicy
    intent: Delete a feature rollout policy
    question: How do I delete a staged rollout policy I'm finished with?
  - id: policy.featureRolloutPolicy_ListAppliesTo
    intent: List who a feature rollout applies to
    question: Which groups or objects is a staged rollout feature enabled for?
  - id: policy.featureRolloutPolicy_CreateAppliesTo
    intent: Add a directory object to a feature rollout
    question: How do I add a group to a staged rollout by posting the directory object?
  - id: policy.featureRolloutPolicy.appliesTo_DeleteDirectoryObjectGraphBPreRef
    intent: Remove one object from a feature rollout
    question: How do I take a specific group out of a staged rollout by its ID?
  phrasing_ops: 13
  slug: azure-ad-policies-featurerolloutpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.federatedTokenValidationPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.federatedtokenvalidationpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.federated Token Validation Policy API
  phrasing_intents:
  - id: policy_GetFederatedTokenValidationPolicy
    intent: Get the federated token validation policy
    question: What is the federated token validation policy set to in my tenant?
  - id: policy_UpdateFederatedTokenValidationPolicy
    intent: Update the federated token validation policy
    question: How do I change which domains are validated for federated tokens?
  - id: policy_DeleteFederatedTokenValidationPolicy
    intent: Delete the federated token validation policy
    question: Can I delete the federated token validation policy altogether?
  phrasing_ops: 3
  slug: azure-ad-policies-federatedtokenvalidationpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.homeRealmDiscoveryPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.homerealmdiscoverypolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.home Realm Discovery Policy API
  phrasing_intents:
  - id: policy_ListHomeRealmDiscoveryPolicy
    intent: List home realm discovery policies
    question: Which home realm discovery policies exist in my tenant?
  - id: policy_CreateHomeRealmDiscoveryPolicy
    intent: Create a home realm discovery policy
    question: How do I create a new home realm discovery policy?
  - id: policy_GetHomeRealmDiscoveryPolicy
    intent: Get a home realm discovery policy
    question: What are the properties and definition of one home realm discovery policy?
  - id: policy_UpdateHomeRealmDiscoveryPolicy
    intent: Update a home realm discovery policy
    question: Can I change the settings of an existing home realm discovery policy?
  - id: policy_DeleteHomeRealmDiscoveryPolicy
    intent: Delete a home realm discovery policy
    question: Can I remove a home realm discovery policy I no longer need?
  - id: policy.homeRealmDiscoveryPolicy_ListAppliesTo
    intent: List objects a home realm discovery policy applies to
    question: Which applications or service principals is a home realm discovery policy assigned to?
  - id: policy.homeRealmDiscoveryPolicy_GetAppliesTo
    intent: Get one object a home realm discovery policy applies to
    question: Can I check a single object that a home realm discovery policy has been applied to?
  - id: policy.homeRealmDiscoveryPolicy.appliesTo_GetCount
    intent: Count objects a home realm discovery policy applies to
    question: How many objects is a home realm discovery policy applied to?
  phrasing_ops: 9
  slug: azure-ad-policies-homerealmdiscoverypolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.identitySecurityDefaultsEnforcementPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.identitysecuritydefaultsenforcementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.identity Security Defaults Enforcement Policy API
  phrasing_intents:
  - id: policy_GetIdentitySecurityDefaultsEnforcementPolicy
    intent: Check whether security defaults are enabled
    question: Are security defaults turned on in my Entra tenant?
  - id: policy_UpdateIdentitySecurityDefaultsEnforcementPolicy
    intent: Turn security defaults on or off
    question: How do I enable security defaults for my tenant?
  - id: policy_DeleteIdentitySecurityDefaultsEnforcementPolicy
    intent: Delete the security defaults enforcement policy
    question: Can I delete the security defaults enforcement policy object itself?
  phrasing_ops: 3
  slug: azure-ad-policies-identitysecuritydefaultsenforcementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.ownerlessGroupPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.ownerlessgrouppolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.ownerless Group Policy API
  phrasing_intents:
  - id: policy_GetOwnerlessGroupPolicy
    intent: View the tenant's ownerless group policy
    question: What is our current policy for Microsoft 365 groups that have no owner?
  - id: policy_UpdateOwnerlessGroupPolicy
    intent: Create or update the ownerless group policy
    question: How do I set up notifications asking members to take ownership of groups that lost their owner?
  phrasing_ops: 2
  slug: azure-ad-policies-ownerlessgrouppolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.permissionGrantPolicy API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for policies.permissiongrantpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.permission Grant Policy API
  phrasing_intents:
  - id: policy_ListPermissionGrantPolicy
    intent: List permission grant policies
    question: Which permission grant policies control app consent in my tenant?
  - id: policy_CreatePermissionGrantPolicy
    intent: Create a permission grant policy
    question: How do I define a custom policy for when users may consent to apps?
  - id: policy_GetPermissionGrantPolicy
    intent: Get a permission grant policy
    question: What conditions does a particular consent policy include and exclude?
  - id: policy_UpdatePermissionGrantPolicy
    intent: Update a permission grant policy
    question: How do I replace the include and exclude conditions on an existing consent policy in one update?
  - id: policy_DeletePermissionGrantPolicy
    intent: Delete a permission grant policy
    question: Can I remove a custom consent policy I no longer need?
  - id: policy.permissionGrantPolicy_ListExclude
    intent: List a consent policy's exclude conditions
    question: Which condition sets are excluded from a permission grant policy?
  - id: policy.permissionGrantPolicy_CreateExclude
    intent: Add an exclude condition to a consent policy
    question: How do I exclude a specific client app from a permission grant policy?
  - id: policy.permissionGrantPolicy_GetExclude
    intent: Get one exclude condition set of a policy
    question: What exactly does a single exclusion rule in a consent policy match?
  phrasing_ops: 18
  slug: azure-ad-policies-permissiongrantpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.policyRoot API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.policyroot.
  name: Microsoft Entra ID (formerly Azure AD) Policies.policy Root API
  phrasing_intents:
  - id: policy.policyRoot_GetPolicyRoot
    intent: Get the tenant's policy root
    question: What policies are configured in my Microsoft Entra tenant overall?
  - id: policy.policyRoot_UpdatePolicyRoot
    intent: Update the tenant's policy root
    question: How do I update the policy root to change the authorization policy?
  phrasing_ops: 2
  slug: azure-ad-policies-policyroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.tenantAppManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.tenantappmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.tenant App Management Policy API
  phrasing_intents:
  - id: policy_GetDefaultAppManagementPolicy
    intent: Get the tenant default app management policy
    question: What credential restrictions does my tenant enforce on apps by default?
  - id: policy_UpdateDefaultAppManagementPolicy
    intent: Update the tenant default app management policy
    question: How do I turn on tenant-wide restrictions for app secrets and certificates?
  - id: policy_DeleteDefaultAppManagementPolicy
    intent: Delete the tenant default app management policy
    question: Can I delete the tenant-wide default app management policy?
  phrasing_ops: 3
  slug: azure-ad-policies-tenantappmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.tokenIssuancePolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.tokenissuancepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.token Issuance Policy API
  phrasing_intents:
  - id: policy_ListTokenIssuancePolicy
    intent: List token issuance policies
    question: Which token issuance policies are defined in my tenant?
  - id: policy_CreateTokenIssuancePolicy
    intent: Create a token issuance policy
    question: How do I define a new policy that controls the SAML tokens Entra ID issues?
  - id: policy_GetTokenIssuancePolicy
    intent: Get a token issuance policy
    question: What SAML token characteristics does one specific token issuance policy define?
  - id: policy_UpdateTokenIssuancePolicy
    intent: Update a token issuance policy
    question: How do I change the settings of an existing token issuance policy?
  - id: policy_DeleteTokenIssuancePolicy
    intent: Delete a token issuance policy
    question: Can I remove a token issuance policy we no longer use?
  - id: policy.tokenIssuancePolicy_ListAppliesTo
    intent: List apps a token issuance policy applies to
    question: Which applications is a given token issuance policy assigned to?
  - id: policy.tokenIssuancePolicy_GetAppliesTo
    intent: Get one object a token policy applies to
    question: Is a specific application among the objects a token issuance policy is applied to?
  - id: policy.tokenIssuancePolicy.appliesTo_GetCount
    intent: Count objects a token issuance policy covers
    question: How many applications is one token issuance policy applied to?
  phrasing_ops: 9
  slug: azure-ad-policies-tokenissuancepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.tokenLifetimePolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.tokenlifetimepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.token Lifetime Policy API
  phrasing_intents:
  - id: policy_ListTokenLifetimePolicy
    intent: List token lifetime policies
    question: What token lifetime policies are defined in my tenant?
  - id: policy_CreateTokenLifetimePolicy
    intent: Create a token lifetime policy
    question: How do I create a policy that shortens access token lifetime?
  - id: policy_GetTokenLifetimePolicy
    intent: Get a token lifetime policy
    question: What token lifetime does a particular policy define?
  - id: policy_UpdateTokenLifetimePolicy
    intent: Update a token lifetime policy
    question: How do I change the lifetime set in an existing token lifetime policy?
  - id: policy_DeleteTokenLifetimePolicy
    intent: Delete a token lifetime policy
    question: How do I remove a token lifetime policy we no longer want?
  - id: policy.tokenLifetimePolicy_ListAppliesTo
    intent: List apps a token lifetime policy applies to
    question: Which applications or service principals is a token lifetime policy applied to?
  - id: policy.tokenLifetimePolicy_GetAppliesTo
    intent: Get one object a token lifetime policy applies to
    question: Is a specific application covered by a given token lifetime policy?
  - id: policy.tokenLifetimePolicy.appliesTo_GetCount
    intent: Count objects a token lifetime policy applies to
    question: How many apps is a token lifetime policy applied to?
  phrasing_ops: 9
  slug: azure-ad-policies-tokenlifetimepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.unifiedRoleManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for policies.unifiedrolemanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.unified Role Management Policy API
  phrasing_intents:
  - id: policy_ListRoleManagementPolicy
    intent: List PIM role management policies
    question: Which PIM policies apply to Microsoft Entra roles or group membership in my tenant?
  - id: policy_CreateRoleManagementPolicy
    intent: Create a role management policy
    question: Is it possible to add a new role management policy for a scope?
  - id: policy_GetRoleManagementPolicy
    intent: Get one role management policy
    question: What are the details of a specific PIM role management policy?
  - id: policy_UpdateRoleManagementPolicy
    intent: Update a role management policy
    question: How do I rename or re-describe an existing PIM policy?
  - id: policy_DeleteRoleManagementPolicy
    intent: Delete a role management policy
    question: Can I delete a role management policy I created?
  - id: policy.roleManagementPolicy_ListEffectiveRule
    intent: List a policy's effective rules
    question: Which approval and expiration rules actually take effect after inherited tenant-wide rules are applied?
  - id: policy.roleManagementPolicy_CreateEffectiveRule
    intent: Add an effective rule to a policy
    question: Can I create an effective rule entry on a role management policy?
  - id: policy.roleManagementPolicy_GetEffectiveRule
    intent: Get one effective rule of a policy
    question: What is the effective, inheritance-evaluated value of one specific rule on a PIM policy?
  phrasing_ops: 18
  slug: azure-ad-policies-unifiedrolemanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.unifiedRoleManagementPolicyAssignment API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for policies.unifiedrolemanagementpolicyassignment.
  name: Microsoft Entra ID (formerly Azure AD) Policies.unified Role Management Policy Assignment API
  phrasing_intents:
  - id: policy_ListRoleManagementPolicyAssignment
    intent: List PIM role management policy assignments
    question: Which role management policies are assigned to Entra roles and groups in PIM?
  - id: policy_CreateRoleManagementPolicyAssignment
    intent: Create a role management policy assignment
    question: Can I link a role management policy to a role definition at a given scope?
  - id: policy_GetRoleManagementPolicyAssignment
    intent: Get a PIM role management policy assignment
    question: What are the details of one PIM policy assignment for a role or group?
  - id: policy_UpdateRoleManagementPolicyAssignment
    intent: Update a role management policy assignment
    question: Can I point an existing PIM policy assignment at a different policy?
  - id: policy_DeleteRoleManagementPolicyAssignment
    intent: Delete a role management policy assignment
    question: Can I remove a PIM policy assignment from a role?
  - id: policy.roleManagementPolicyAssignment_GetPolicy
    intent: Get the policy behind a PIM policy assignment
    question: Which role management policy and rules does a PIM assignment actually enforce?
  - id: policy.roleManagementPolicyAssignment_GetCount
    intent: Count role management policy assignments
    question: How many role management policy assignments exist in PIM?
  phrasing_ops: 7
  slug: azure-ad-policies-unifiedrolemanagementpolicyassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The roleManagement.rbacApplication API from Microsoft Entra ID (formerly Azure AD) — 150 operation(s) for rolemanagement.rbacapplication.
  name: Microsoft Entra ID (formerly Azure AD) Role Management.rbac Application API
  phrasing_intents:
  - id: roleManagement_GetDirectory
    intent: Get the directory role management container
    question: What does the role management directory container expose in Entra ID?
  - id: roleManagement_UpdateDirectory
    intent: Update the directory role management container
    question: Can I patch the directory RBAC provider object itself rather than one role?
  - id: roleManagement_DeleteDirectory
    intent: Delete the directory role management container
    question: Is it possible to delete the whole directory RBAC provider navigation property?
  - id: roleManagement.directory_ListResourceNamespace
    intent: List directory resource namespaces
    question: Which resource namespaces exist for directory role permissions?
  - id: roleManagement.directory_CreateResourceNamespace
    intent: Create a directory resource namespace
    question: Can I add a new resource namespace to the directory RBAC provider?
  - id: roleManagement.directory_GetResourceNamespace
    intent: Get a directory resource namespace
    question: How can I look up a single directory resource namespace by its ID?
  - id: roleManagement.directory_UpdateResourceNamespace
    intent: Update a directory resource namespace
    question: Can I rename a directory resource namespace?
  - id: roleManagement.directory_DeleteResourceNamespace
    intent: Delete a directory resource namespace
    question: Can I remove a resource namespace from the directory RBAC provider?
  phrasing_ops: 224
  slug: azure-ad-rolemanagement-rbacapplication-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.appManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.appmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.app Management Policy API
  phrasing_intents:
  - id: servicePrincipal_ListAppManagementPolicy
    intent: List app management policies on a service principal
    question: Which app management policies are applied to a particular service principal?
  - id: servicePrincipal_GetAppManagementPolicy
    intent: Get one app management policy on a service principal
    question: Can I read a specific app management policy through the service principal it applies to?
  - id: servicePrincipal.appManagementPolicy_GetCount
    intent: Count app management policies on a service principal
    question: How many app management policies apply to a service principal?
  phrasing_ops: 3
  slug: azure-ad-serviceprincipals-appmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.appRoleAssignment API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for serviceprincipals.approleassignment.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.app Role Assignment API
  phrasing_intents:
  - id: servicePrincipal_ListAppRoleAssignedTo
    intent: List who has been granted an app's roles
    question: Which users, groups and apps have been granted roles on my API's service principal?
  - id: servicePrincipal_CreateAppRoleAssignedTo
    intent: Grant a user, group or app a role on a resource app
    question: How do I give a user or group an app role on an enterprise application?
  - id: servicePrincipal_GetAppRoleAssignedTo
    intent: Get one grant of a resource app's role
    question: Who received a specific role assignment on my resource app, and which role was it?
  - id: servicePrincipal_UpdateAppRoleAssignedTo
    intent: Update a role grant on a resource app
    question: Can I change which role a user holds on my resource app without deleting the grant?
  - id: servicePrincipal_DeleteAppRoleAssignedTo
    intent: Revoke a user, group or app's role on a resource app
    question: How do I remove a user's access to an enterprise application?
  - id: servicePrincipal.appRoleAssignedTo_GetCount
    intent: Count grants of a resource app's roles
    question: How many users, groups and apps have been granted roles on my resource app?
  - id: servicePrincipal_ListAppRoleAssignment
    intent: List app roles a service principal holds
    question: Which application permissions has a client app's service principal been granted on other APIs?
  - id: servicePrincipal_CreateAppRoleAssignment
    intent: Grant an application permission to a client app
    question: How do I grant an application permission to a client app's service principal?
  phrasing_ops: 12
  slug: azure-ad-serviceprincipals-approleassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.claimsMappingPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.claimsmappingpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.claims Mapping Policy API
  phrasing_intents:
  - id: servicePrincipal_ListClaimsMappingPolicy
    intent: List claims mapping policies on a service principal
    question: Which claims mapping policies are assigned to this service principal?
  - id: servicePrincipal.claimsMappingPolicy_DeleteClaimsMappingPolicyGraphBPreRef
    intent: Unassign a claims mapping policy by id
    question: How do I remove a specific claims mapping policy from a service principal using the policy id in the path?
  - id: servicePrincipal.claimsMappingPolicy_GetCount
    intent: Count claims mapping policies on a service principal
    question: How many claims mapping policies are assigned to one service principal?
  - id: servicePrincipal_ListClaimsMappingPolicyGraphBPreRef
    intent: List claims mapping policy references
    question: Can I get just the references (@odata.id links) for claims mapping policies on a service principal?
  - id: servicePrincipal_CreateClaimsMappingPolicyGraphBPreRef
    intent: Assign a claims mapping policy to a service principal
    question: How do I assign a claims mapping policy to an enterprise app?
  - id: servicePrincipal_DeleteClaimsMappingPolicyGraphBPreRef
    intent: Unassign a claims mapping policy by reference
    question: Can I remove a claims mapping policy by passing its @id reference as a query parameter?
  phrasing_ops: 6
  slug: azure-ad-serviceprincipals-claimsmappingpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.delegatedPermissionClassification API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.delegatedpermissionclassification.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.delegated Permission Classification API
  phrasing_intents:
  - id: servicePrincipal_ListDelegatedPermissionClassification
    intent: List delegated permission classifications
    question: Which delegated permissions exposed by my API have been classified?
  - id: servicePrincipal_CreateDelegatedPermissionClassification
    intent: Classify a delegated permission
    question: How do I classify a delegated permission as low impact?
  - id: servicePrincipal_GetDelegatedPermissionClassification
    intent: Get a delegated permission classification
    question: Can I read a single delegated permission classification?
  - id: servicePrincipal_UpdateDelegatedPermissionClassification
    intent: Update a delegated permission classification
    question: Can I change a delegated permission's classification after setting it?
  - id: servicePrincipal_DeleteDelegatedPermissionClassification
    intent: Remove a delegated permission classification
    question: How do I remove a classification from a delegated permission?
  - id: servicePrincipal.delegatedPermissionClassification_GetCount
    intent: Count delegated permission classifications
    question: How many delegated permission classifications does a service principal have?
  phrasing_ops: 6
  slug: azure-ad-serviceprincipals-delegatedpermissionclassification-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 64 operation(s) for serviceprincipals.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.directory Object API
  phrasing_intents:
  - id: servicePrincipal_ListCreatedObject
    intent: List objects a service principal created
    question: Which directory objects were created by a particular service principal?
  - id: servicePrincipal_GetCreatedObject
    intent: Get one object a service principal created
    question: What are the details of a single object that a service principal created?
  - id: servicePrincipal_GetCreatedObjectAsServicePrincipal
    intent: Get a created object typed as a service principal
    question: Can I read a created object with its service principal properties rather than generic directory fields?
  - id: servicePrincipal.createdObject_GetCount
    intent: Count objects a service principal created
    question: How many directory objects has a given service principal created?
  - id: servicePrincipal_ListCreatedObjectAsServicePrincipal
    intent: List service principals a service principal created
    question: Which service principals were created by another service principal?
  - id: servicePrincipal.CreatedObject_GetCountAsServicePrincipal
    intent: Count service principals a service principal created
    question: How many service principals has one service principal created?
  - id: servicePrincipal_ListMemberGraphOPre
    intent: List a service principal's direct memberships
    question: Which groups and directory roles is a service principal directly a member of?
  - id: servicePrincipal_GetMemberGraphOPre
    intent: Get one direct membership of a service principal
    question: Can I fetch a single group or role that a service principal is directly a member of?
  phrasing_ops: 66
  slug: azure-ad-serviceprincipals-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.endpoint API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.endpoint.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.endpoint API
  phrasing_intents:
  - id: servicePrincipal_ListEndpoint
    intent: List a service principal's endpoints
    question: Which endpoints are registered on a given service principal?
  - id: servicePrincipal_CreateEndpoint
    intent: Add an endpoint to a service principal
    question: How do I register a new endpoint URI on a service principal?
  - id: servicePrincipal_GetEndpoint
    intent: Get one service principal endpoint
    question: What URI and capability does a specific service principal endpoint have?
  - id: servicePrincipal_UpdateEndpoint
    intent: Update a service principal endpoint
    question: How do I change the URI of an existing service principal endpoint?
  - id: servicePrincipal_DeleteEndpoint
    intent: Remove an endpoint from a service principal
    question: How do I delete an endpoint from a service principal?
  - id: servicePrincipal.endpoint_GetCount
    intent: Count a service principal's endpoints
    question: How many endpoints does a given service principal have?
  phrasing_ops: 6
  slug: azure-ad-serviceprincipals-endpoint-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.federatedIdentityCredential API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.federatedidentitycredential.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.federated Identity Credential API
  phrasing_intents:
  - id: servicePrincipal_ListFederatedIdentityCredential
    intent: List a service principal's federated credentials
    question: Which federated identity credentials are configured on a managed identity's service principal?
  - id: servicePrincipal_CreateFederatedIdentityCredential
    intent: Add a federated credential to a service principal
    question: How do I let an external CI pipeline or workload sign in as a managed identity without a secret?
  - id: servicePrincipal_GetFederatedIdentityCredential
    intent: Get a federated credential by ID
    question: What issuer and subject does a specific federated credential on a service principal trust?
  - id: servicePrincipal_UpdateFederatedIdentityCredential
    intent: Update a federated credential by ID
    question: Can I change the subject on an existing federated credential using its ID?
  - id: servicePrincipal_DeleteFederatedIdentityCredential
    intent: Delete a federated credential by ID
    question: How do I revoke a workload's federated trust on a service principal using the credential ID?
  - id: servicePrincipal.federatedIdentityCredential_GetGraphBPreName
    intent: Get a federated credential by name
    question: Can I look up a federated identity credential on a service principal by its name instead of its ID?
  - id: servicePrincipal.federatedIdentityCredential_UpdateGraphBPreName
    intent: Update a federated credential by name
    question: Can I update a federated identity credential by addressing it with its name?
  - id: servicePrincipal.federatedIdentityCredential_DeleteGraphBPreName
    intent: Delete a federated credential by name
    question: Can I delete a federated identity credential by its name rather than its ID?
  phrasing_ops: 9
  slug: azure-ad-serviceprincipals-federatedidentitycredential-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.homeRealmDiscoveryPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.homerealmdiscoverypolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.home Realm Discovery Policy API
  phrasing_intents:
  - id: servicePrincipal_ListHomeRealmDiscoveryPolicy
    intent: List home realm discovery policies on an app
    question: Which home realm discovery policies are assigned to a service principal?
  - id: servicePrincipal.homeRealmDiscoveryPolicy_DeleteHomeRealmDiscoveryPolicyGraphBPreRef
    intent: Remove an HRD policy from an app by policy ID
    question: How do I unassign a specific home realm discovery policy from a service principal by its ID?
  - id: servicePrincipal.homeRealmDiscoveryPolicy_GetCount
    intent: Count HRD policies on a service principal
    question: How many home realm discovery policies are assigned to one service principal?
  - id: servicePrincipal_ListHomeRealmDiscoveryPolicyGraphBPreRef
    intent: List references to an app's HRD policies
    question: Can I get just the $ref links of HRD policies assigned to a service principal?
  - id: servicePrincipal_CreateHomeRealmDiscoveryPolicyGraphBPreRef
    intent: Assign an HRD policy to a service principal
    question: How do I assign a home realm discovery policy to an enterprise app?
  - id: servicePrincipal_DeleteHomeRealmDiscoveryPolicyGraphBPreRef
    intent: Remove an HRD policy from an app by reference
    question: How do I unassign an HRD policy from a service principal using its @id reference?
  phrasing_ops: 6
  slug: azure-ad-serviceprincipals-homerealmdiscoverypolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.oAuth2PermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.oauth2permissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.o Auth2 Permission Grant API
  phrasing_intents:
  - id: servicePrincipal_ListOauth2PermissionGrant
    intent: List delegated permission grants for an app
    question: Which delegated permissions have users or admins consented to for a client app?
  - id: servicePrincipal_GetOauth2PermissionGrant
    intent: Get one delegated permission grant for an app
    question: How do I read a single OAuth2 permission grant on a service principal?
  - id: servicePrincipal.oauth2PermissionGrant_GetCount
    intent: Count delegated permission grants for an app
    question: How many delegated permission grants does a service principal have?
  phrasing_ops: 3
  slug: azure-ad-serviceprincipals-oauth2permissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.remoteDesktopSecurityConfiguration API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for serviceprincipals.remotedesktopsecurityconfiguration.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.remote Desktop Security Configuration API
  phrasing_intents:
  - id: servicePrincipal_GetRemoteDesktopSecurityConfiguration
    intent: View an app's Remote Desktop security configuration
    question: Is Entra ID authentication for Remote Desktop turned on for this service principal?
  - id: servicePrincipal_UpdateRemoteDesktopSecurityConfiguration
    intent: Enable or disable Entra RDP auth on an app
    question: How do I turn on Microsoft Entra ID authentication for Remote Desktop Protocol?
  - id: servicePrincipal_DeleteRemoteDesktopSecurityConfiguration
    intent: Remove an app's Remote Desktop security configuration
    question: What happens to RDP sign-in if I delete the remote desktop security configuration?
  - id: servicePrincipal.remoteDesktopSecurityConfiguration_ListApprovedClientApp
    intent: List approved Remote Desktop client apps
    question: Which client apps are approved for Remote Desktop connections on this app?
  - id: servicePrincipal.remoteDesktopSecurityConfiguration_CreateApprovedClientApp
    intent: Approve a client app for Remote Desktop
    question: How do I add a new approved client app to the RDP security configuration?
  - id: servicePrincipal.remoteDesktopSecurityConfiguration_GetApprovedClientApp
    intent: Get one approved Remote Desktop client app
    question: What are the details of a specific approved RDP client app?
  - id: servicePrincipal.remoteDesktopSecurityConfiguration_UpdateApprovedClientApp
    intent: Rename an approved Remote Desktop client app
    question: Can I change the display name of an approved RDP client app?
  - id: servicePrincipal.remoteDesktopSecurityConfiguration_DeleteApprovedClientApp
    intent: Revoke an approved Remote Desktop client app
    question: How do I stop a client app from being approved for RDP?
  phrasing_ops: 15
  slug: azure-ad-serviceprincipals-remotedesktopsecurityconfiguration-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.servicePrincipal.Actions API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for serviceprincipals.serviceprincipal.actions.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.service Principal.Actions API
  phrasing_intents:
  - id: servicePrincipal_addKey
    intent: Add a key credential to a service principal
    question: How do I roll an expiring certificate key on a service principal?
  - id: servicePrincipal_addPassword
    intent: Add a client secret to a service principal
    question: Can I generate a new client secret for a service principal?
  - id: servicePrincipal_addTokenSigningCertificate
    intent: Create a token signing certificate for a service principal
    question: How do I create a self-signed SAML token signing certificate for an enterprise app?
  - id: servicePrincipal_checkMemberGroup
    intent: Check a service principal's membership in given groups
    question: Is a service principal a member of any of these specific groups?
  - id: servicePrincipal_checkMemberObject
    intent: Check a service principal's membership in given objects
    question: Can I test whether a service principal is a member of specific groups, roles or administrative units?
  - id: servicePrincipal_getMemberGroup
    intent: Get all groups a service principal belongs to
    question: Which groups is a service principal a member of, including nested ones?
  - id: servicePrincipal_getMemberObject
    intent: Get all groups, roles and units a service principal is in
    question: What groups, administrative units and directory roles does a service principal belong to?
  - id: servicePrincipal_removeKey
    intent: Remove a key credential from a service principal
    question: How do I retire an old certificate key from a service principal?
  phrasing_ops: 13
  slug: azure-ad-serviceprincipals-serviceprincipal-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.servicePrincipal API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.serviceprincipal.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.service Principal API
  phrasing_intents:
  - id: servicePrincipal_ListServicePrincipal
    intent: List service principals
    question: Which enterprise apps and service principals exist in my tenant?
  - id: servicePrincipal_CreateServicePrincipal
    intent: Create a service principal
    question: How do I create a service principal for an app registration?
  - id: servicePrincipal_GetServicePrincipal
    intent: Get a service principal by object ID
    question: How can I read a service principal when I have its object ID?
  - id: servicePrincipal_UpdateServicePrincipal
    intent: Upsert a service principal by object ID
    question: How do I update a service principal's settings given its object ID?
  - id: servicePrincipal_DeleteServicePrincipal
    intent: Delete a service principal by object ID
    question: Can I delete an enterprise app's service principal using its object ID?
  - id: servicePrincipal_GetServicePrincipalGraphBPreAppId
    intent: Get a service principal by its app ID
    question: Can I look up a service principal using the application (client) ID instead of the object ID?
  - id: servicePrincipal_UpdateServicePrincipalGraphBPreAppId
    intent: Upsert a service principal by its app ID
    question: Can I create a service principal if missing, or update it, addressed by appId?
  - id: servicePrincipal_DeleteServicePrincipalGraphBPreAppId
    intent: Delete a service principal by its app ID
    question: Can I delete a service principal knowing only its application client ID?
  phrasing_ops: 9
  slug: azure-ad-serviceprincipals-serviceprincipal-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.servicePrincipal.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for serviceprincipals.serviceprincipal.functions.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.service Principal.Functions API
  phrasing_intents:
  - id: servicePrincipal_delta
    intent: Track changes to service principals
    question: How do I get only the service principals that were created, updated or deleted since my last sync?
  phrasing_ops: 1
  slug: azure-ad-serviceprincipals-serviceprincipal-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.synchronization API from Microsoft Entra ID (formerly Azure AD) — 34 operation(s) for serviceprincipals.synchronization.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.synchronization API
  phrasing_intents:
  - id: servicePrincipal_GetSynchronization
    intent: Get an app's provisioning synchronization setup
    question: What does the overall provisioning synchronization resource look like for one enterprise app?
  - id: servicePrincipal_SetSynchronization
    intent: Replace an app's whole synchronization resource
    question: Can I overwrite a service principal's entire synchronization resource in a single PUT?
  - id: servicePrincipal_DeleteSynchronization
    intent: Remove an app's entire synchronization resource
    question: How do I tear down all provisioning synchronization for an enterprise app?
  - id: servicePrincipal.synchronization_ListJob
    intent: List an app's provisioning sync jobs
    question: Which provisioning synchronization jobs exist for an enterprise app?
  - id: servicePrincipal.synchronization_CreateJob
    intent: Create a provisioning sync job for an app
    question: How do I set up a new user provisioning job for an enterprise app?
  - id: servicePrincipal.synchronization_GetJob
    intent: Get one provisioning sync job
    question: What is the current status and schedule of a specific provisioning job?
  - id: servicePrincipal.synchronization_UpdateJob
    intent: Update a provisioning sync job's settings
    question: Can I change the run schedule of an existing provisioning job?
  - id: servicePrincipal.synchronization_DeleteJob
    intent: Stop and delete a provisioning sync job
    question: What happens to already-synced accounts when I delete a provisioning job?
  phrasing_ops: 56
  slug: azure-ad-serviceprincipals-synchronization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.tokenIssuancePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.tokenissuancepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.token Issuance Policy API
  phrasing_intents:
  - id: servicePrincipal_ListTokenIssuancePolicy
    intent: List a service principal's token issuance policies
    question: Which token issuance policies are assigned to a service principal?
  - id: servicePrincipal.tokenIssuancePolicy_DeleteTokenIssuancePolicyGraphBPreRef
    intent: Unassign a token issuance policy by its ID
    question: Can I unassign a specific token issuance policy from a service principal using the policy ID in the path?
  - id: servicePrincipal.tokenIssuancePolicy_GetCount
    intent: Count a service principal's token issuance policies
    question: How many token issuance policies are assigned to a service principal?
  - id: servicePrincipal_ListTokenIssuancePolicyGraphBPreRef
    intent: List token issuance policy references
    question: Can I get just the reference links of the token issuance policies on a service principal?
  - id: servicePrincipal_CreateTokenIssuancePolicyGraphBPreRef
    intent: Assign a token issuance policy to a service principal
    question: How do I apply a token issuance policy to an enterprise app's service principal?
  - id: servicePrincipal_DeleteTokenIssuancePolicyGraphBPreRef
    intent: Unassign a token issuance policy by @id reference
    question: Can I remove a token issuance policy link by passing its reference as an @id query value?
  phrasing_ops: 6
  slug: azure-ad-serviceprincipals-tokenissuancepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.tokenLifetimePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.tokenlifetimepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.token Lifetime Policy API
  phrasing_intents:
  - id: servicePrincipal_ListTokenLifetimePolicy
    intent: List token lifetime policies on a service principal
    question: Which token lifetime policy is assigned to an enterprise app's service principal?
  - id: servicePrincipal.tokenLifetimePolicy_DeleteTokenLifetimePolicyGraphBPreRef
    intent: Unassign a token lifetime policy by id
    question: How do I remove a specific token lifetime policy from a service principal?
  - id: servicePrincipal.tokenLifetimePolicy_GetCount
    intent: Count token lifetime policies on a service principal
    question: Does this service principal have a token lifetime policy, going by the count?
  - id: servicePrincipal_ListTokenLifetimePolicyGraphBPreRef
    intent: List token lifetime policy references
    question: Can I get just the reference link of a service principal's token lifetime policy?
  - id: servicePrincipal_CreateTokenLifetimePolicyGraphBPreRef
    intent: Assign a token lifetime policy to a service principal
    question: How do I apply a token lifetime policy to a service principal?
  - id: servicePrincipal_DeleteTokenLifetimePolicyGraphBPreRef
    intent: Unassign a token lifetime policy by reference query
    question: Can I remove a token lifetime policy from a service principal by passing its @id as a query parameter?
  phrasing_ops: 6
  slug: azure-ad-serviceprincipals-tokenlifetimepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The subscribedSkus.subscribedSku API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for subscribedskus.subscribedsku.
  name: Microsoft Entra ID (formerly Azure AD) Subscribed Skus.subscribed Sku API
  phrasing_intents:
  - id: subscribedSku_ListSubscribedSku
    intent: List the organization's license subscriptions
    question: Which commercial subscriptions and licenses has my organization acquired?
  - id: subscribedSku_CreateSubscribedSku
    intent: Add a subscribed SKU entity
    question: Can I add a subscribed SKU record with a SKU id and part number?
  - id: subscribedSku_GetSubscribedSku
    intent: Get one license subscription
    question: What are the details of one specific commercial subscription my organization owns?
  - id: subscribedSku_UpdateSubscribedSku
    intent: Update a subscribed SKU entity
    question: Can I change the capability status of a subscribed SKU?
  - id: subscribedSku_DeleteSubscribedSku
    intent: Delete a subscribed SKU entity
    question: Can I delete a subscribed SKU record from the directory?
  phrasing_ops: 5
  slug: azure-ad-subscribedskus-subscribedsku-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The subscriptions.subscription.Actions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for subscriptions.subscription.actions.
  name: Microsoft Entra ID (formerly Azure AD) Subscriptions.subscription.Actions API
  phrasing_intents:
  - id: subscription_reauthorize
    intent: Reauthorize a change notification subscription
    question: What do I do when a Graph subscription gets a reauthorizationRequired challenge?
  phrasing_ops: 1
  slug: azure-ad-subscriptions-subscription-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The subscriptions.subscription API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for subscriptions.subscription.
  name: Microsoft Entra ID (formerly Azure AD) Subscriptions.subscription API
  phrasing_intents:
  - id: subscription_ListSubscription
    intent: List change notification subscriptions
    question: Which webhook subscriptions for change notifications are active for my app?
  - id: subscription_CreateSubscription
    intent: Subscribe to change notifications on a resource
    question: How do I get notified at my webhook when users or groups change?
  - id: subscription_GetSubscription
    intent: Get one change notification subscription
    question: What resource and notification URL is a specific subscription set up for?
  - id: subscription_UpdateSubscription
    intent: Renew a change notification subscription
    question: How do I renew a change notification subscription before it expires?
  - id: subscription_DeleteSubscription
    intent: Stop a change notification subscription
    question: How do I stop receiving change notifications for a subscription?
  phrasing_ops: 5
  slug: azure-ad-subscriptions-subscription-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The tenantRelationships.multiTenantOrganization API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for tenantrelationships.multitenantorganization.
  name: Microsoft Entra ID (formerly Azure AD) Tenant Relationships.multi Tenant Organization API
  phrasing_intents:
  - id: tenantRelationship_GetMultiTenantOrganization
    intent: Get the multitenant organization
    question: What are the properties of the multitenant organization my tenant belongs to?
  - id: tenantRelationship_UpdateMultiTenantOrganization
    intent: Update the multitenant organization
    question: How do I rename our multitenant organization?
  - id: tenantRelationship.multiTenantOrganization_GetJoinRequest
    intent: Check my tenant's join request status
    question: Has my tenant finished joining the multitenant organization yet?
  - id: tenantRelationship.multiTenantOrganization_UpdateJoinRequest
    intent: Join a multitenant organization
    question: My tenant was added as pending to a multitenant organization; how do I actually join it?
  - id: tenantRelationship.multiTenantOrganization_ListTenant
    intent: List tenants in the multitenant organization
    question: Which tenants are members of our multitenant organization?
  - id: tenantRelationship.multiTenantOrganization_CreateTenant
    intent: Add a tenant to the multitenant organization
    question: How do I invite another tenant into our multitenant organization?
  - id: tenantRelationship.multiTenantOrganization_GetTenant
    intent: Get one member tenant
    question: What role and state does a specific member tenant have in the multitenant organization?
  - id: tenantRelationship.multiTenantOrganization_UpdateTenant
    intent: Update a member tenant
    question: How do I promote a member tenant to an owner in the multitenant organization?
  phrasing_ops: 10
  slug: azure-ad-tenantrelationships-multitenantorganization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The tenantRelationships.tenantRelationship.Functions API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for tenantrelationships.tenantrelationship.functions.
  name: Microsoft Entra ID (formerly Azure AD) Tenant Relationships.tenant Relationship.Functions API
  phrasing_intents:
  - id: tenantRelationship_findTenantInformationGraphBPreDomainName
    intent: Find a tenant by domain name
    question: Which tenant owns a given domain name?
  - id: tenantRelationship_findTenantInformationGraphBPreTenantId
    intent: Find a tenant by tenant ID
    question: Can I validate a tenant ID and read its tenant information?
  phrasing_ops: 2
  slug: azure-ad-tenantrelationships-tenantrelationship-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.agreementAcceptance API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.agreementacceptance.
  name: Microsoft Entra ID (formerly Azure AD) Users.agreement Acceptance API
  phrasing_intents:
  - id: user_ListAgreementAcceptance
    intent: List a user's terms of use acceptances
    question: Which terms of use agreements has a user accepted or declined?
  - id: user_GetAgreementAcceptance
    intent: Get one terms of use acceptance for a user
    question: How do I read a single agreement acceptance record for a user?
  - id: user.agreementAcceptance_GetCount
    intent: Count a user's terms of use acceptances
    question: How many terms of use acceptances does a user have on record?
  phrasing_ops: 3
  slug: azure-ad-users-agreementacceptance-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: User accounts in the directory
  name: Microsoft Entra ID (formerly Azure AD) Users API
  phrasing_intents:
  - id: listUsers
    intent: List users in the directory
    question: How do I get a list of all the users in my Entra ID tenant?
  - id: createUser
    intent: Create a new user account
    question: How do I add a new employee account to Microsoft Entra ID through Graph?
  - id: getUser
    intent: Look up a single user's profile
    question: How can I look up one user's profile by their sign-in name?
  - id: updateUser
    intent: Update an existing user's profile
    question: How do I change an existing user's job title or display name?
  - id: deleteUser
    intent: Delete a user account
    question: How do I remove a departed employee's account from the directory?
  - id: getUserManager
    intent: Find a user's manager
    question: Who does a particular employee report to?
  - id: listDirectReports
    intent: List a user's direct reports
    question: Which people report directly to a given manager?
  phrasing_ops: 7
  slug: azure-ad-users-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.appRoleAssignment API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.approleassignment.
  name: Microsoft Entra ID (formerly Azure AD) Users.app Role Assignment API
  phrasing_intents:
  - id: user_ListAppRoleAssignment
    intent: List a user's app role assignments
    question: Which application roles has a particular user been granted?
  - id: user_CreateAppRoleAssignment
    intent: Assign an app role to a user
    question: How do I give a user a specific role in an enterprise application?
  - id: user_GetAppRoleAssignment
    intent: Get one of a user's app role assignments
    question: How do I read the details of one specific app role assignment for a user?
  - id: user_UpdateAppRoleAssignment
    intent: Update a user's app role assignment
    question: Can I change the role on an existing app role assignment for a user?
  - id: user_DeleteAppRoleAssignment
    intent: Remove an app role from a user
    question: How do I revoke a user's access to an application role?
  - id: user.appRoleAssignment_GetCount
    intent: Count a user's app role assignments
    question: How many applications is a user assigned to?
  phrasing_ops: 6
  slug: azure-ad-users-approleassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.authentication API from Microsoft Entra ID (formerly Azure AD) — 44 operation(s) for users.authentication.
  name: Microsoft Entra ID (formerly Azure AD) Users.authentication API
  phrasing_intents:
  - id: user_GetAuthentication
    intent: Get a user's authentication root
    question: Where do I see the authentication object that holds all of a user's sign-in method collections?
  - id: user_UpdateAuthentication
    intent: Update a user's authentication root
    question: Can I patch the authentication object on a user to replace several method collections at once?
  - id: user_DeleteAuthentication
    intent: Delete a user's authentication root
    question: Is it possible to delete the whole authentication navigation property on a user?
  - id: user.authentication_ListEmailMethod
    intent: List a user's email authentication methods
    question: Which email address has a user registered for self-service password reset?
  - id: user.authentication_CreateEmailMethod
    intent: Register an email authentication method
    question: How do I add a password reset email address to a user in Entra ID?
  - id: user.authentication_GetEmailMethod
    intent: Get one email authentication method
    question: What email address is stored on a specific email authentication method for a user?
  - id: user.authentication_UpdateEmailMethod
    intent: Change a user's authentication email address
    question: Can I change the email address on an existing email authentication method for a user?
  - id: user.authentication_DeleteEmailMethod
    intent: Remove a user's email authentication method
    question: How do I remove a user's password reset email address?
  phrasing_ops: 68
  slug: azure-ad-users-authentication-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 84 operation(s) for users.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Users.directory Object API
  phrasing_intents:
  - id: user_ListCreatedObject
    intent: List directory objects a user created
    question: Which directory objects did a particular user create?
  - id: user_GetCreatedObject
    intent: Get one object a user created
    question: How do I look up a single object from a user's created objects?
  - id: user_GetCreatedObjectAsServicePrincipal
    intent: Get a user-created object as a service principal
    question: Can I read an object a user created cast as a service principal?
  - id: user.createdObject_GetCount
    intent: Count the objects a user created
    question: How many directory objects has a given user created?
  - id: user_ListCreatedObjectAsServicePrincipal
    intent: List service principals a user created
    question: Which service principals were created by a specific user?
  - id: user.CreatedObject_GetCountAsServicePrincipal
    intent: Count service principals a user created
    question: How many service principals has one user created?
  - id: user_ListDirectReport
    intent: List a user's direct reports
    question: Who reports directly to a given user or agent user?
  - id: user_GetDirectReport
    intent: Get one direct report of a user
    question: How do I fetch a single person from someone's direct reports?
  phrasing_ops: 88
  slug: azure-ad-users-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.extension.
  name: Microsoft Entra ID (formerly Azure AD) Users.extension API
  phrasing_intents:
  - id: user_ListExtension
    intent: List open extensions on a user
    question: What custom open extensions have been stored on a user's profile?
  - id: user_CreateExtension
    intent: Add an open extension to a user
    question: How do I attach custom data to a user with an open extension?
  - id: user_GetExtension
    intent: Get one open extension on a user
    question: How do I read a specific custom extension stored on a user?
  - id: user_UpdateExtension
    intent: Update an open extension on a user
    question: Can I change the custom values in a user's existing open extension?
  - id: user_DeleteExtension
    intent: Delete an open extension from a user
    question: Can I remove custom data I stored on a user as an open extension?
  - id: user.extension_GetCount
    intent: Count open extensions on a user
    question: How many open extensions does a user have?
  phrasing_ops: 6
  slug: azure-ad-users-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.itemInsights API from Microsoft Entra ID (formerly Azure AD) — 14 operation(s) for users.iteminsights.
  name: Microsoft Entra ID (formerly Azure AD) Users.item Insights API
  phrasing_intents:
  - id: user_GetInsight
    intent: Get a user's item insights
    question: How do I see the document insights Microsoft Graph has calculated for a user?
  - id: user_UpdateInsight
    intent: Update a user's item insights container
    question: Is there a patch call for a user's top-level insights object?
  - id: user_DeleteInsight
    intent: Delete a user's item insights
    question: Can I wipe the calculated document insights for a user?
  - id: user.insight_ListShared
    intent: List documents shared with or by a user
    question: Which files have been shared with or by a particular user recently?
  - id: user.insight_CreateShared
    intent: Add a shared-document insight for a user
    question: Can I add a shared insight record to a user's insights?
  - id: user.insight_GetShared
    intent: Get one shared-document insight
    question: What details are stored for one specific shared-document insight?
  - id: user.insight_UpdateShared
    intent: Update a shared-document insight
    question: Can I change the visualization details on an existing shared insight?
  - id: user.insight_DeleteShared
    intent: Delete a shared-document insight
    question: Can I remove one shared-document insight from a user's list?
  phrasing_ops: 25
  slug: azure-ad-users-iteminsights-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.licenseDetails API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for users.licensedetails.
  name: Microsoft Entra ID (formerly Azure AD) Users.license Details API
  phrasing_intents:
  - id: user_ListLicenseDetail
    intent: List a user's license details
    question: Which licenses and service plans does a user have?
  - id: user_CreateLicenseDetail
    intent: Add a license detail record to a user
    question: Can I create a licenseDetails entry on a user through this endpoint?
  - id: user_GetLicenseDetail
    intent: Get one license detail of a user
    question: Which service plans are included in one specific license a user holds?
  - id: user_UpdateLicenseDetail
    intent: Update a license detail record on a user
    question: Can I change the service plans recorded on a user's existing license detail?
  - id: user_DeleteLicenseDetail
    intent: Delete a license detail record from a user
    question: Can I delete a licenseDetails record from a user?
  - id: user.licenseDetail_GetCount
    intent: Count a user's licenses
    question: How many licenses does a user have?
  - id: user.licenseDetail_getTeamsLicensingDetail
    intent: Check a user's Microsoft Teams license status
    question: Does a user have a Teams license?
  phrasing_ops: 7
  slug: azure-ad-users-licensedetails-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.mailboxSettings API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for users.mailboxsettings.
  name: Microsoft Entra ID (formerly Azure AD) Users.mailbox Settings API
  phrasing_intents:
  - id: user_GetMailboxSetting
    intent: Get a user's mailbox settings
    question: What are a user's mailbox settings like time zone and language?
  - id: user_UpdateMailboxSetting
    intent: Update a user's mailbox settings
    question: How do I change a user's mailbox time zone?
  phrasing_ops: 2
  slug: azure-ad-users-mailboxsettings-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.oAuth2PermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.oauth2permissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Users.o Auth2 Permission Grant API
  phrasing_intents:
  - id: user_ListOauth2PermissionGrant
    intent: List a user's delegated permission grants
    question: Which apps has a user granted delegated permissions to act on their behalf?
  - id: user_GetOauth2PermissionGrant
    intent: Get one of a user's delegated permission grants
    question: What scopes does a specific delegated permission grant give an app for a user?
  - id: user.oauth2PermissionGrant_GetCount
    intent: Count a user's delegated permission grants
    question: How many delegated permission grants does a given user have?
  phrasing_ops: 3
  slug: azure-ad-users-oauth2permissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.onPremisesSyncBehavior API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for users.onpremisessyncbehavior.
  name: Microsoft Entra ID (formerly Azure AD) Users.on Premises Sync Behavior API
  phrasing_intents:
  - id: user_GetOnPremisesSyncBehavior
    intent: Get a user's on-premises sync behavior
    question: Is this user managed in the cloud or still synced from on-premises?
  - id: user_UpdateOnPremisesSyncBehavior
    intent: Switch a user between cloud and on-premises management
    question: How do I make a synced user cloud managed instead of on-premises managed?
  - id: user_DeleteOnPremisesSyncBehavior
    intent: Remove a user's on-premises sync behavior
    question: Can I delete the on-premises sync behavior object on a user?
  phrasing_ops: 3
  slug: azure-ad-users-onpremisessyncbehavior-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.outlookUser API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for users.outlookuser.
  name: Microsoft Entra ID (formerly Azure AD) Users.outlook User API
  phrasing_intents:
  - id: user_GetOutlook
    intent: Get a user's Outlook settings container
    question: Can I read the Outlook services object for a user in Microsoft Graph?
  - id: user.outlook_ListMasterCategory
    intent: List a user's Outlook categories
    question: Which color categories has a user defined in Outlook?
  - id: user.outlook_CreateMasterCategory
    intent: Create an Outlook category for a user
    question: Can I add a new color category to a user's Outlook master list?
  - id: user.outlook_GetMasterCategory
    intent: Get one of a user's Outlook categories
    question: What name and color does a specific Outlook category of a user have?
  - id: user.outlook_UpdateMasterCategory
    intent: Change an existing Outlook category
    question: Can I change the color of an Outlook category a user already has?
  - id: user.outlook_DeleteMasterCategory
    intent: Delete one of a user's Outlook categories
    question: Can I remove a category from a user's Outlook master list?
  - id: user.outlook.masterCategory_GetCount
    intent: Count a user's Outlook categories
    question: How many Outlook categories has a user defined?
  - id: user.outlook_supportedLanguage
    intent: List languages supported for a user's mailbox
    question: Which locales and languages does a user's mailbox server support?
  phrasing_ops: 10
  slug: azure-ad-users-outlookuser-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.profilePhoto API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for users.profilephoto.
  name: Microsoft Entra ID (formerly Azure AD) Users.profile Photo API
  phrasing_intents:
  - id: user_GetPhoto
    intent: Get a user's main profile photo metadata
    question: Does this user have a profile photo set, and what size is their main one?
  - id: user_UpdatePhoto
    intent: Update a user's profile photo properties
    question: Can I change the recorded height and width on a user's photo metadata?
  - id: user_DeletePhoto
    intent: Remove a user's profile photo record
    question: Can I delete the profile photo object for a user altogether?
  - id: user_GetPhotoContent
    intent: Download a user's profile picture
    question: How do I download the actual image bytes of a colleague's profile picture?
  - id: user_SetPhotoContent
    intent: Upload a new profile picture for a user
    question: How do I upload a new profile picture for someone in my organization?
  - id: user_DeletePhotoContent
    intent: Delete a user's profile picture image
    question: How do I clear a user's profile picture so the default initials show again?
  - id: user_ListPhoto
    intent: List a user's profile photo sizes
    question: Which sizes of a user's profile photo are available?
  - id: getUsersByUserIdPhotosByProfilePhotoId
    intent: Get details of one photo size for a user
    question: What are the height and width of one specific photo size a user has?
  phrasing_ops: 11
  slug: azure-ad-users-profilephoto-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.scopedRoleMembership API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.scopedrolemembership.
  name: Microsoft Entra ID (formerly Azure AD) Users.scoped Role Membership API
  phrasing_intents:
  - id: user_ListScopedRoleMemberGraphOPre
    intent: List a user's admin-unit scoped role assignments
    question: Which administrative units does a user hold an admin role in?
  - id: user_CreateScopedRoleMemberGraphOPre
    intent: Give a user a role scoped to an admin unit
    question: How do I make someone a helpdesk admin for just one administrative unit?
  - id: user_GetScopedRoleMemberGraphOPre
    intent: Get one scoped role membership of a user
    question: What role and administrative unit does a specific scoped membership grant?
  - id: user_UpdateScopedRoleMemberGraphOPre
    intent: Update a user's scoped role membership
    question: How do I move a user's scoped admin role to a different administrative unit?
  - id: user_DeleteScopedRoleMemberGraphOPre
    intent: Remove a user's admin-unit scoped role
    question: How do I revoke a user's admin role over one administrative unit?
  - id: user.scopedRoleMemberOf_GetCount
    intent: Count a user's scoped role memberships
    question: How many admin-unit scoped roles does a user hold?
  phrasing_ops: 6
  slug: azure-ad-users-scopedrolemembership-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.todo API from Microsoft Entra ID (formerly Azure AD) — 30 operation(s) for users.todo.
  name: Microsoft Entra ID (formerly Azure AD) Users.todo API
  phrasing_intents:
  - id: user_GetTodo
    intent: Get a user's To Do service
    question: What does the To Do root object for a user contain?
  - id: user_UpdateTodo
    intent: Update a user's To Do service object
    question: Can I patch the To Do root object of a user directly?
  - id: user_DeleteTodo
    intent: Delete a user's To Do service object
    question: Is it possible to delete the whole To Do navigation property for a user?
  - id: user.todo_ListList
    intent: List a user's To Do task lists
    question: Which task lists does a user have in Microsoft To Do?
  - id: user.todo_CreateList
    intent: Create a To Do task list
    question: How do I create a new task list in someone's Microsoft To Do?
  - id: user.todo_GetList
    intent: Get a To Do task list
    question: What are the details of one specific To Do task list?
  - id: user.todo_UpdateList
    intent: Rename or update a To Do task list
    question: How do I rename an existing To Do task list?
  - id: user.todo_DeleteList
    intent: Delete a To Do task list
    question: Can I delete an entire To Do list along with its tasks?
  phrasing_ops: 58
  slug: azure-ad-users-todo-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.user API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for users.user.
  name: Microsoft Entra ID (formerly Azure AD) Users.user API
  phrasing_intents:
  - id: user_ListUser
    intent: List users in the directory
    question: How do I pull a list of every user account in my Entra ID tenant?
  - id: user_CreateUser
    intent: Create a new user account
    question: What's the minimum I need to supply to create a new employee account?
  - id: user_GetUser
    intent: Get a user by object id
    question: How do I look up a single user's properties from their object id?
  - id: user_UpdateUser
    intent: Update a user by object id
    question: How do I change a user's job title or department using their object id?
  - id: user_DeleteUser
    intent: Delete a user by object id
    question: What happens to a user's mailbox and licenses when I delete their account?
  - id: user_GetUserGraphBPreUserPrincipalName
    intent: Get a user by sign-in name
    question: Can I fetch a user directly by their userPrincipalName instead of the object id?
  - id: user_UpdateUserGraphBPreUserPrincipalName
    intent: Update a user by sign-in name
    question: Can I patch a user's profile when I only have their userPrincipalName?
  - id: user_DeleteUserGraphBPreUserPrincipalName
    intent: Delete a user by sign-in name
    question: Is it possible to delete an account addressed by userPrincipalName rather than id?
  phrasing_ops: 9
  slug: azure-ad-users-user-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.userSettings API from Microsoft Entra ID (formerly Azure AD) — 24 operation(s) for users.usersettings.
  name: Microsoft Entra ID (formerly Azure AD) Users.user Settings API
  phrasing_intents:
  - id: user_GetSetting
    intent: Get a user's settings
    question: How do I see all of a user's settings, like content discovery and work hours, in one place?
  - id: user_UpdateSetting
    intent: Update a user's settings
    question: Can I stop a user's activity from feeding content discovery in Microsoft 365?
  - id: user_DeleteSetting
    intent: Delete a user's settings object
    question: Can I remove the whole settings object from a user account?
  - id: user.setting_GetExchange
    intent: List a user's Exchange mailboxes
    question: Which Exchange mailboxes belong to a user, including shared ones?
  - id: user.setting_GetItemInsight
    intent: Get a user's item insights privacy setting
    question: Is item insights turned on for this user?
  - id: user.setting_UpdateItemInsight
    intent: Turn a user's item insights on or off
    question: How do I disable item and meeting hour insights for a privacy-sensitive user?
  - id: user.setting_DeleteItemInsight
    intent: Delete a user's item insights setting
    question: Can I remove the item insights settings object from someone's account?
  - id: user.setting_GetShiftPreference
    intent: Get a user's shift availability preferences
    question: When is a shift worker available according to their shift preferences?
  phrasing_ops: 50
  slug: azure-ad-users-usersettings-api
artifact_total: 223
asyncapis:
- description: ''
  name: Azure Ad Change Notifications Webhooks
  slug: azure-ad-change-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications API
  slug: open-azure-ad-applications-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Directory API
  slug: open-azure-ad-directory-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Groups API
  slug: open-azure-ad-groups-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Me API
  slug: open-azure-ad-me-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Users API
  slug: open-azure-ad-users-api
- collection_type: open
  name: Microsoft Graph API (Azure AD)
  slug: open-azure-ad
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-applications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-applications-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-identity-directorymanagement-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-identity-directorymanagement-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-groups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-groups-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-users-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-identity-signins-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-identity-signins-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-identity-governance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-identity-governance-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-directoryobjects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-directoryobjects-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/overlays/azure-ad-graph-changenotifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/azure-ad-graph-changenotifications-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/packages/azure-ad-packages.yml
  title: ''
  type: SDKs
  url: packages/azure-ad-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/security/azure-ad-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/azure-ad-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/lifecycle/azure-ad-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/azure-ad-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/conventions/azure-ad-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/azure-ad-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/security/azure-ad-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/azure-ad-trust-center.yml
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/asyncapi/azure-ad-change-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/azure-ad-change-notifications-webhooks.yml
- group: start
  title: ''
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/microsoftgraph
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.microsoft.com/en-us/microsoft-365/roadmap
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/rate-limits/azure-ad-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/azure-ad-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/plans/azure-ad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azure-ad-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/sandbox/azure-ad-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/azure-ad-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/data-model/azure-ad-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azure-ad-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/components/azure-ad-components.yml
  title: ''
  type: Components
  url: components/azure-ad-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/cli/azure-ad-cli.yml
  title: ''
  type: CLI
  url: cli/azure-ad-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/changelog/azure-ad-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/azure-ad-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/conventions/azure-ad-conventions.yml
  title: ''
  type: Conventions
  url: conventions/azure-ad-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/lifecycle/azure-ad-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/azure-ad-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/errors/azure-ad-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/azure-ad-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/security/azure-ad-trust-center.yml
  title: ''
  type: Compliance
  url: security/azure-ad-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/conformance/azure-ad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azure-ad-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/llms/azure-ad-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azure-ad-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/mcp/azure-ad-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/azure-ad-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/mcp/azure-ad-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/azure-ad-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/well-known/azure-ad-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/azure-ad-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/well-known/azure-ad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azure-ad-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/packages/azure-ad-packages.yml
  title: ''
  type: Packages
  url: packages/azure-ad-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/security/azure-ad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-ad-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/agentic-access/azure-ad-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-ad-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/security/azure-ad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azure-ad-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/authentication/azure-ad-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azure-ad-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/scopes/azure-ad-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/azure-ad-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureAD
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/active-directory/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/security/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.microsoft.com/en-us/security/blog/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/get-started-azure-ad
created: '2024-01-01'
description: Microsoft's cloud-based identity and access management service that helps employees sign in and access resources. Azure AD provides OAuth, OpenID Connect, SAML, and other identity protocols for securing applications and managing user identities.
features:
- description: Enable users to sign in once and access all connected apps without re-authenticating.
  name: Single Sign-On
- description: Enforce MFA to add an extra layer of security beyond passwords.
  name: Multi-Factor Authentication
- description: Define access policies based on user, device, location, and risk signals.
  name: Conditional Access
- description: Industry-standard protocols for authorization and authentication.
  name: OAuth 2.0 and OpenID Connect
- description: Federate with thousands of SAML-based SaaS applications.
  name: SAML 2.0 Support
- description: Detect and respond to identity-based risks with AI-powered signals.
  name: Identity Protection
- description: Just-in-time privileged access with approval workflows and audit.
  name: Privileged Identity Management
- description: Invite external users from partner organizations to access your resources.
  name: B2B Collaboration
- description: Enable customer and partner identity management with Azure AD B2C and B2B.
  name: External Identities
finops:
- name: Azure Ad Finops
  service_category: API
  slug: azure-ad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-ad.png
integrations:
- description: Provides identity and access management for all Microsoft 365 applications.
  name: Microsoft 365
- description: SAML-based SSO integration with Salesforce CRM and Platform.
  name: Salesforce
- description: Federated SSO and user provisioning for ServiceNow via SAML and SCIM.
  name: ServiceNow
- description: SAML SSO and SCIM provisioning for GitHub Enterprise organizations.
  name: GitHub Enterprise
- description: Federate Azure AD with AWS IAM Identity Center for cross-cloud SSO.
  name: AWS
layout: provider
mcp_servers:
- description: Microsoft's own hosted MCP server for querying enterprise identity and directory data in a Microsoft Entra tenant with natural language. Rather than projecting one tool per Graph operation, it ships t
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-09-16'
name: Microsoft Entra ID (formerly Azure AD)
nav: Providers
network: true
overview: 'Microsoft Entra ID (formerly Azure AD) publishes 186 APIs on the [APIs.io](https://apis.io/) network, including Admin.people Admin Settings API, Agreements.agreement API, Agreements.agreement Acceptance API, and 183 more. Tagged areas include Authentication, Authorization, Identity, OpenID Connect, and SSO.


  The Microsoft Entra ID (formerly Azure AD) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Microsoft Entra ID (formerly Azure AD)''s developer surface includes API reference, developer console, signup flow, support, sandbox, CLI, changelog, and 49 more developer resources.'
plans:
- name: Azure Ad Plans Pricing
  plan_count: 10
  slug: azure-ad-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 8
  name: Azure Ad Rate Limits
  slug: azure-ad-rate-limits
scopes:
- name: Azure Ad Scopes
  scope_count: 39
  slug: azure-ad-scopes
  summary_line: 39 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: exemplar
  composite: 83.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 56.3
    developer_ergonomics: 82.7
    discoverability: 80.0
    operational_transparency: 97.4
  previous_composite: 82.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 185
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
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/screenshots/azure-ad-2026-06-20T172836.png
security:
- kind: authentication
  name: Azure Ad Authentication
  slug: azure-ad-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Azure Ad Domain Security
  slug: azure-ad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Ad Vulnerability Disclosure
  slug: azure-ad-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Azure Ad Trust Center
  slug: azure-ad-trust-center
  summary_line: FedRAMP, NIST SP 800-53, HIPAA / HITECH, SOX
slug: azure-ad
tags:
- Authentication
- Authorization
- Identity
- OpenID Connect
- SSO
- Identity Federation
use_cases:
- description: Provide single sign-on for employees across thousands of SaaS applications.
  name: Enterprise SSO
- description: Implement zero trust architecture with identity as the control plane.
  name: Zero Trust Security
- description: Build customer-facing login with Azure AD B2C supporting social identities.
  name: Consumer Identity
- description: Secure APIs with OAuth 2.0 tokens issued by Azure AD.
  name: API Security
- description: Extend on-premises Active Directory to the cloud with Azure AD Connect.
  name: Hybrid Identity
website: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
---
