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
  scored_at: '2026-09-16'
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
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on the signed-in user
  name: Azure Active Directory Me API
  slug: azure-ad-me-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The admin.peopleAdminSettings API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for admin.peopleadminsettings.
  name: Microsoft Entra ID (formerly Azure AD) Admin.people Admin Settings API
  slug: azure-ad-admin-peopleadminsettings-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreement API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for agreements.agreement.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement API
  slug: azure-ad-agreements-agreement-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreementAcceptance API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for agreements.agreementacceptance.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement Acceptance API
  slug: azure-ad-agreements-agreementacceptance-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreementFile API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for agreements.agreementfile.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement File API
  slug: azure-ad-agreements-agreementfile-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The agreements.agreementFileLocalization API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for agreements.agreementfilelocalization.
  name: Microsoft Entra ID (formerly Azure AD) Agreements.agreement File Localization API
  slug: azure-ad-agreements-agreementfilelocalization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Application registrations in Entra ID
  name: Microsoft Entra ID (formerly Azure AD) Applications API
  slug: azure-ad-applications-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.application.Actions API from Microsoft Entra ID (formerly Azure AD) — 14 operation(s) for applications.application.actions.
  name: Microsoft Entra ID (formerly Azure AD) Applications.application.Actions API
  slug: azure-ad-applications-application-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.application API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for applications.application.
  name: Microsoft Entra ID (formerly Azure AD) Applications.application API
  slug: azure-ad-applications-application-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.application.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for applications.application.functions.
  name: Microsoft Entra ID (formerly Azure AD) Applications.application.Functions API
  slug: azure-ad-applications-application-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.appManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.appmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.app Management Policy API
  slug: azure-ad-applications-appmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 17 operation(s) for applications.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Applications.directory Object API
  slug: azure-ad-applications-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.extensionProperty API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for applications.extensionproperty.
  name: Microsoft Entra ID (formerly Azure AD) Applications.extension Property API
  slug: azure-ad-applications-extensionproperty-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.federatedIdentityCredential API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.federatedidentitycredential.
  name: Microsoft Entra ID (formerly Azure AD) Applications.federated Identity Credential API
  slug: azure-ad-applications-federatedidentitycredential-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.homeRealmDiscoveryPolicy API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for applications.homerealmdiscoverypolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.home Realm Discovery Policy API
  slug: azure-ad-applications-homerealmdiscoverypolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.synchronization API from Microsoft Entra ID (formerly Azure AD) — 34 operation(s) for applications.synchronization.
  name: Microsoft Entra ID (formerly Azure AD) Applications.synchronization API
  slug: azure-ad-applications-synchronization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.tokenIssuancePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.tokenissuancepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.token Issuance Policy API
  slug: azure-ad-applications-tokenissuancepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applications.tokenLifetimePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for applications.tokenlifetimepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Applications.token Lifetime Policy API
  slug: azure-ad-applications-tokenlifetimepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applicationTemplates.applicationTemplate.Actions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for applicationtemplates.applicationtemplate.actions.
  name: Microsoft Entra ID (formerly Azure AD) Application Templates.application Template.Actions API
  slug: azure-ad-applicationtemplates-applicationtemplate-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The applicationTemplates.applicationTemplate API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for applicationtemplates.applicationtemplate.
  name: Microsoft Entra ID (formerly Azure AD) Application Templates.application Template API
  slug: azure-ad-applicationtemplates-applicationtemplate-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 28 operation(s) for contacts.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.directory Object API
  slug: azure-ad-contacts-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.onPremisesSyncBehavior API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for contacts.onpremisessyncbehavior.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.on Premises Sync Behavior API
  slug: azure-ad-contacts-onpremisessyncbehavior-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.orgContact.Actions API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for contacts.orgcontact.actions.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.org Contact.Actions API
  slug: azure-ad-contacts-orgcontact-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.orgContact API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for contacts.orgcontact.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.org Contact API
  slug: azure-ad-contacts-orgcontact-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.orgContact.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for contacts.orgcontact.functions.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.org Contact.Functions API
  slug: azure-ad-contacts-orgcontact-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contacts.serviceProvisioningError API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for contacts.serviceprovisioningerror.
  name: Microsoft Entra ID (formerly Azure AD) Contacts.service Provisioning Error API
  slug: azure-ad-contacts-serviceprovisioningerror-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contracts.contract.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for contracts.contract.actions.
  name: Microsoft Entra ID (formerly Azure AD) Contracts.contract.Actions API
  slug: azure-ad-contracts-contract-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contracts.contract API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for contracts.contract.
  name: Microsoft Entra ID (formerly Azure AD) Contracts.contract API
  slug: azure-ad-contracts-contract-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The contracts.contract.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for contracts.contract.functions.
  name: Microsoft Entra ID (formerly Azure AD) Contracts.contract.Functions API
  slug: azure-ad-contracts-contract-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The dataPolicyOperations.dataPolicyOperation API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for datapolicyoperations.datapolicyoperation.
  name: Microsoft Entra ID (formerly Azure AD) Data Policy Operations.data Policy Operation API
  slug: azure-ad-datapolicyoperations-datapolicyoperation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.device.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for devices.device.actions.
  name: Microsoft Entra ID (formerly Azure AD) Devices.device.Actions API
  slug: azure-ad-devices-device-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.device API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for devices.device.
  name: Microsoft Entra ID (formerly Azure AD) Devices.device API
  slug: azure-ad-devices-device-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.device.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for devices.device.functions.
  name: Microsoft Entra ID (formerly Azure AD) Devices.device.Functions API
  slug: azure-ad-devices-device-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 50 operation(s) for devices.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Devices.directory Object API
  slug: azure-ad-devices-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The devices.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for devices.extension.
  name: Microsoft Entra ID (formerly Azure AD) Devices.extension API
  slug: azure-ad-devices-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.administrativeUnit API from Microsoft Entra ID (formerly Azure AD) — 32 operation(s) for directory.administrativeunit.
  name: Microsoft Entra ID (formerly Azure AD) Directory.administrative Unit API
  slug: azure-ad-directory-administrativeunit-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Directory roles and objects
  name: Microsoft Entra ID (formerly Azure AD) Directory API
  slug: azure-ad-directory-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.attributeSet API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.attributeset.
  name: Microsoft Entra ID (formerly Azure AD) Directory.attribute Set API
  slug: azure-ad-directory-attributeset-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.companySubscription API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for directory.companysubscription.
  name: Microsoft Entra ID (formerly Azure AD) Directory.company Subscription API
  slug: azure-ad-directory-companysubscription-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.customSecurityAttributeDefinition API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for directory.customsecurityattributedefinition.
  name: Microsoft Entra ID (formerly Azure AD) Directory.custom Security Attribute Definition API
  slug: azure-ad-directory-customsecurityattributedefinition-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.deviceLocalCredentialInfo API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.devicelocalcredentialinfo.
  name: Microsoft Entra ID (formerly Azure AD) Directory.device Local Credential Info API
  slug: azure-ad-directory-devicelocalcredentialinfo-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.directory API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directory.directory.
  name: Microsoft Entra ID (formerly Azure AD) Directory.directory API
  slug: azure-ad-directory-directory-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 29 operation(s) for directory.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Directory.directory Object API
  slug: azure-ad-directory-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.identityProviderBase API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for directory.identityproviderbase.
  name: Microsoft Entra ID (formerly Azure AD) Directory.identity Provider Base API
  slug: azure-ad-directory-identityproviderbase-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.onPremisesDirectorySynchronization API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.onpremisesdirectorysynchronization.
  name: Microsoft Entra ID (formerly Azure AD) Directory.on Premises Directory Synchronization API
  slug: azure-ad-directory-onpremisesdirectorysynchronization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.publicKeyInfrastructureRoot API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directory.publickeyinfrastructureroot.
  name: Microsoft Entra ID (formerly Azure AD) Directory.public Key Infrastructure Root API
  slug: azure-ad-directory-publickeyinfrastructureroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.recovery API from Microsoft Entra ID (formerly Azure AD) — 14 operation(s) for directory.recovery.
  name: Microsoft Entra ID (formerly Azure AD) Directory.recovery API
  slug: azure-ad-directory-recovery-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directory.remoteTenantGroup API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directory.remotetenantgroup.
  name: Microsoft Entra ID (formerly Azure AD) Directory.remote Tenant Group API
  slug: azure-ad-directory-remotetenantgroup-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryObjects.directoryObject.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directoryobjects.directoryobject.actions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Objects.directory Object.Actions API
  slug: azure-ad-directoryobjects-directoryobject-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryObjects.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directoryobjects.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Directory Objects.directory Object API
  slug: azure-ad-directoryobjects-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryObjects.directoryObject.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directoryobjects.directoryobject.functions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Objects.directory Object.Functions API
  slug: azure-ad-directoryobjects-directoryobject-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 22 operation(s) for directoryroles.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Object API
  slug: azure-ad-directoryroles-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryRole.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directoryroles.directoryrole.actions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Role.Actions API
  slug: azure-ad-directoryroles-directoryrole-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryRole API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for directoryroles.directoryrole.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Role API
  slug: azure-ad-directoryroles-directoryrole-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.directoryRole.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directoryroles.directoryrole.functions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.directory Role.Functions API
  slug: azure-ad-directoryroles-directoryrole-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoles.scopedRoleMembership API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directoryroles.scopedrolemembership.
  name: Microsoft Entra ID (formerly Azure AD) Directory Roles.scoped Role Membership API
  slug: azure-ad-directoryroles-scopedrolemembership-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoleTemplates.directoryRoleTemplate.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for directoryroletemplates.directoryroletemplate.actions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Role Templates.directory Role Template.Actions API
  slug: azure-ad-directoryroletemplates-directoryroletemplate-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoleTemplates.directoryRoleTemplate API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for directoryroletemplates.directoryroletemplate.
  name: Microsoft Entra ID (formerly Azure AD) Directory Role Templates.directory Role Template API
  slug: azure-ad-directoryroletemplates-directoryroletemplate-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The directoryRoleTemplates.directoryRoleTemplate.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for directoryroletemplates.directoryroletemplate.functions.
  name: Microsoft Entra ID (formerly Azure AD) Directory Role Templates.directory Role Template.Functions API
  slug: azure-ad-directoryroletemplates-directoryroletemplate-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for domains.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Domains.directory Object API
  slug: azure-ad-domains-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.domain.Actions API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for domains.domain.actions.
  name: Microsoft Entra ID (formerly Azure AD) Domains.domain.Actions API
  slug: azure-ad-domains-domain-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.domain API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for domains.domain.
  name: Microsoft Entra ID (formerly Azure AD) Domains.domain API
  slug: azure-ad-domains-domain-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.domainDnsRecord API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for domains.domaindnsrecord.
  name: Microsoft Entra ID (formerly Azure AD) Domains.domain Dns Record API
  slug: azure-ad-domains-domaindnsrecord-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The domains.internalDomainFederation API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for domains.internaldomainfederation.
  name: Microsoft Entra ID (formerly Azure AD) Domains.internal Domain Federation API
  slug: azure-ad-domains-internaldomainfederation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupLifecyclePolicies.groupLifecyclePolicy.Actions API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for grouplifecyclepolicies.grouplifecyclepolicy.actions.
  name: Microsoft Entra ID (formerly Azure AD) Group Lifecycle Policies.group Lifecycle Policy.Actions API
  slug: azure-ad-grouplifecyclepolicies-grouplifecyclepolicy-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupLifecyclePolicies.groupLifecyclePolicy API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for grouplifecyclepolicies.grouplifecyclepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Group Lifecycle Policies.group Lifecycle Policy API
  slug: azure-ad-grouplifecyclepolicies-grouplifecyclepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Microsoft 365 and security groups
  name: Microsoft Entra ID (formerly Azure AD) Groups API
  slug: azure-ad-groups-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.appRoleAssignment API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.approleassignment.
  name: Microsoft Entra ID (formerly Azure AD) Groups.app Role Assignment API
  slug: azure-ad-groups-approleassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.conversation API from Microsoft Entra ID (formerly Azure AD) — 29 operation(s) for groups.conversation.
  name: Microsoft Entra ID (formerly Azure AD) Groups.conversation API
  slug: azure-ad-groups-conversation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.conversationThread API from Microsoft Entra ID (formerly Azure AD) — 26 operation(s) for groups.conversationthread.
  name: Microsoft Entra ID (formerly Azure AD) Groups.conversation Thread API
  slug: azure-ad-groups-conversationthread-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 113 operation(s) for groups.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Groups.directory Object API
  slug: azure-ad-groups-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.extension.
  name: Microsoft Entra ID (formerly Azure AD) Groups.extension API
  slug: azure-ad-groups-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.group.Actions API from Microsoft Entra ID (formerly Azure AD) — 18 operation(s) for groups.group.actions.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group.Actions API
  slug: azure-ad-groups-group-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.group API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for groups.group.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group API
  slug: azure-ad-groups-group-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.group.Functions API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for groups.group.functions.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group.Functions API
  slug: azure-ad-groups-group-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.groupLifecyclePolicy API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for groups.grouplifecyclepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group Lifecycle Policy API
  slug: azure-ad-groups-grouplifecyclepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.groupSetting API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.groupsetting.
  name: Microsoft Entra ID (formerly Azure AD) Groups.group Setting API
  slug: azure-ad-groups-groupsetting-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.onPremisesSyncBehavior API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for groups.onpremisessyncbehavior.
  name: Microsoft Entra ID (formerly Azure AD) Groups.on Premises Sync Behavior API
  slug: azure-ad-groups-onpremisessyncbehavior-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.profilePhoto API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for groups.profilephoto.
  name: Microsoft Entra ID (formerly Azure AD) Groups.profile Photo API
  slug: azure-ad-groups-profilephoto-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groups.resourceSpecificPermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groups.resourcespecificpermissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Groups.resource Specific Permission Grant API
  slug: azure-ad-groups-resourcespecificpermissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettings.groupSetting API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groupsettings.groupsetting.
  name: Microsoft Entra ID (formerly Azure AD) Group Settings.group Setting API
  slug: azure-ad-groupsettings-groupsetting-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate.Actions API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for groupsettingtemplates.groupsettingtemplate.actions.
  name: Microsoft Entra ID (formerly Azure AD) Group Setting Templates.group Setting Template.Actions API
  slug: azure-ad-groupsettingtemplates-groupsettingtemplate-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for groupsettingtemplates.groupsettingtemplate.
  name: Microsoft Entra ID (formerly Azure AD) Group Setting Templates.group Setting Template API
  slug: azure-ad-groupsettingtemplates-groupsettingtemplate-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for groupsettingtemplates.groupsettingtemplate.functions.
  name: Microsoft Entra ID (formerly Azure AD) Group Setting Templates.group Setting Template.Functions API
  slug: azure-ad-groupsettingtemplates-groupsettingtemplate-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.authenticationEventListener API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identity.authenticationeventlistener.
  name: Microsoft Entra ID (formerly Azure AD) Identity.authentication Event Listener API
  slug: azure-ad-identity-authenticationeventlistener-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.authenticationEventsFlow API from Microsoft Entra ID (formerly Azure AD) — 26 operation(s) for identity.authenticationeventsflow.
  name: Microsoft Entra ID (formerly Azure AD) Identity.authentication Events Flow API
  slug: azure-ad-identity-authenticationeventsflow-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.b2xIdentityUserFlow API from Microsoft Entra ID (formerly Azure AD) — 34 operation(s) for identity.b2xidentityuserflow.
  name: Microsoft Entra ID (formerly Azure AD) Identity.b2x Identity User Flow API
  slug: azure-ad-identity-b2xidentityuserflow-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.conditionalAccessRoot API from Microsoft Entra ID (formerly Azure AD) — 36 operation(s) for identity.conditionalaccessroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity.conditional Access Root API
  slug: azure-ad-identity-conditionalaccessroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.customAuthenticationExtension API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for identity.customauthenticationextension.
  name: Microsoft Entra ID (formerly Azure AD) Identity.custom Authentication Extension API
  slug: azure-ad-identity-customauthenticationextension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityApiConnector API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for identity.identityapiconnector.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity API Connector API
  slug: azure-ad-identity-identityapiconnector-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityContainer API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identity.identitycontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity Container API
  slug: azure-ad-identity-identitycontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityProviderBase API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for identity.identityproviderbase.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity Provider Base API
  slug: azure-ad-identity-identityproviderbase-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityUserFlowAttribute API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identity.identityuserflowattribute.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity User Flow Attribute API
  slug: azure-ad-identity-identityuserflowattribute-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.identityVerifiedIdRoot API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for identity.identityverifiedidroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity.identity Verified ID Root API
  slug: azure-ad-identity-identityverifiedidroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identity.riskPreventionContainer API from Microsoft Entra ID (formerly Azure AD) — 12 operation(s) for identity.riskpreventioncontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity.risk Prevention Container API
  slug: azure-ad-identity-riskpreventioncontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.accessPackageCatalog API from Microsoft Entra ID (formerly Azure AD) — 146 operation(s) for identitygovernance.accesspackagecatalog.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.access Package Catalog API
  slug: azure-ad-identitygovernance-accesspackagecatalog-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.accessReviewSet API from Microsoft Entra ID (formerly Azure AD) — 45 operation(s) for identitygovernance.accessreviewset.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.access Review Set API
  slug: azure-ad-identitygovernance-accessreviewset-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.appConsentApprovalRoute API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for identitygovernance.appconsentapprovalroute.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.app Consent Approval Route API
  slug: azure-ad-identitygovernance-appconsentapprovalroute-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.entitlementManagement API from Microsoft Entra ID (formerly Azure AD) — 737 operation(s) for identitygovernance.entitlementmanagement.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.entitlement Management API
  slug: azure-ad-identitygovernance-entitlementmanagement-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.identityGovernance API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identitygovernance.identitygovernance.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.identity Governance API
  slug: azure-ad-identitygovernance-identitygovernance-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.lifecycleWorkflowsContainer API from Microsoft Entra ID (formerly Azure AD) — 311 operation(s) for identitygovernance.lifecycleworkflowscontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.lifecycle Workflows Container API
  slug: azure-ad-identitygovernance-lifecycleworkflowscontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.privilegedAccessRoot API from Microsoft Entra ID (formerly Azure AD) — 64 operation(s) for identitygovernance.privilegedaccessroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.privileged Access Root API
  slug: azure-ad-identitygovernance-privilegedaccessroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityGovernance.termsOfUseContainer API from Microsoft Entra ID (formerly Azure AD) — 23 operation(s) for identitygovernance.termsofusecontainer.
  name: Microsoft Entra ID (formerly Azure AD) Identity Governance.terms Of Use Container API
  slug: azure-ad-identitygovernance-termsofusecontainer-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.identityProtectionRoot API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identityprotection.identityprotectionroot.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.identity Protection Root API
  slug: azure-ad-identityprotection-identityprotectionroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.riskDetection API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identityprotection.riskdetection.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.risk Detection API
  slug: azure-ad-identityprotection-riskdetection-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.riskyServicePrincipal API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for identityprotection.riskyserviceprincipal.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.risky Service Principal API
  slug: azure-ad-identityprotection-riskyserviceprincipal-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.riskyUser API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for identityprotection.riskyuser.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.risky User API
  slug: azure-ad-identityprotection-riskyuser-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProtection.servicePrincipalRiskDetection API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identityprotection.serviceprincipalriskdetection.
  name: Microsoft Entra ID (formerly Azure AD) Identity Protection.service Principal Risk Detection API
  slug: azure-ad-identityprotection-serviceprincipalriskdetection-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProviders.identityProvider API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for identityproviders.identityprovider.
  name: Microsoft Entra ID (formerly Azure AD) Identity Providers.identity Provider API
  slug: azure-ad-identityproviders-identityprovider-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The identityProviders.identityProvider.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for identityproviders.identityprovider.functions.
  name: Microsoft Entra ID (formerly Azure AD) Identity Providers.identity Provider.Functions API
  slug: azure-ad-identityproviders-identityprovider-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The informationProtection.bitlocker API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for informationprotection.bitlocker.
  name: Microsoft Entra ID (formerly Azure AD) Information Protection.bitlocker API
  slug: azure-ad-informationprotection-bitlocker-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The informationProtection.informationProtection API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for informationprotection.informationprotection.
  name: Microsoft Entra ID (formerly Azure AD) Information Protection.information Protection API
  slug: azure-ad-informationprotection-informationprotection-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The informationProtection.threatAssessmentRequest API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for informationprotection.threatassessmentrequest.
  name: Microsoft Entra ID (formerly Azure AD) Information Protection.threat Assessment Request API
  slug: azure-ad-informationprotection-threatassessmentrequest-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The invitations.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for invitations.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Invitations.directory Object API
  slug: azure-ad-invitations-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The invitations.invitation API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for invitations.invitation.
  name: Microsoft Entra ID (formerly Azure AD) Invitations.invitation API
  slug: azure-ad-invitations-invitation-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The invitations.user API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for invitations.user.
  name: Microsoft Entra ID (formerly Azure AD) Invitations.user API
  slug: azure-ad-invitations-user-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: Operations on the signed-in user
  name: Microsoft Entra ID (formerly Azure AD) Me API
  slug: azure-ad-me-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The oauth2PermissionGrants.oAuth2PermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for oauth2permissiongrants.oauth2permissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Oauth2 Permission Grants.o Auth2 Permission Grant API
  slug: azure-ad-oauth2permissiongrants-oauth2permissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The oauth2PermissionGrants.oAuth2PermissionGrant.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for oauth2permissiongrants.oauth2permissiongrant.functions.
  name: Microsoft Entra ID (formerly Azure AD) Oauth2 Permission Grants.o Auth2 Permission Grant.Functions API
  slug: azure-ad-oauth2permissiongrants-oauth2permissiongrant-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.certificateBasedAuthConfiguration API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for organization.certificatebasedauthconfiguration.
  name: Microsoft Entra ID (formerly Azure AD) Organization.certificate Based Auth Configuration API
  slug: azure-ad-organization-certificatebasedauthconfiguration-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for organization.extension.
  name: Microsoft Entra ID (formerly Azure AD) Organization.extension API
  slug: azure-ad-organization-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.organization.Actions API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for organization.organization.actions.
  name: Microsoft Entra ID (formerly Azure AD) Organization.organization.Actions API
  slug: azure-ad-organization-organization-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.organization API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for organization.organization.
  name: Microsoft Entra ID (formerly Azure AD) Organization.organization API
  slug: azure-ad-organization-organization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The organization.organizationalBranding API from Microsoft Entra ID (formerly Azure AD) — 18 operation(s) for organization.organizationalbranding.
  name: Microsoft Entra ID (formerly Azure AD) Organization.organizational Branding API
  slug: azure-ad-organization-organizationalbranding-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.activityBasedTimeoutPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.activitybasedtimeoutpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.activity Based Timeout Policy API
  slug: azure-ad-policies-activitybasedtimeoutpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.adminConsentRequestPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.adminconsentrequestpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.admin Consent Request Policy API
  slug: azure-ad-policies-adminconsentrequestpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.appManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.appmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.app Management Policy API
  slug: azure-ad-policies-appmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authenticationFlowsPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.authenticationflowspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authentication Flows Policy API
  slug: azure-ad-policies-authenticationflowspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authenticationMethodsPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for policies.authenticationmethodspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authentication Methods Policy API
  slug: azure-ad-policies-authenticationmethodspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authenticationStrengthPolicy API from Microsoft Entra ID (formerly Azure AD) — 8 operation(s) for policies.authenticationstrengthpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authentication Strength Policy API
  slug: azure-ad-policies-authenticationstrengthpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.authorizationPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.authorizationpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.authorization Policy API
  slug: azure-ad-policies-authorizationpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.claimsMappingPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.claimsmappingpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.claims Mapping Policy API
  slug: azure-ad-policies-claimsmappingpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.conditionalAccessPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for policies.conditionalaccesspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.conditional Access Policy API
  slug: azure-ad-policies-conditionalaccesspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.crossTenantAccessPolicy API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for policies.crosstenantaccesspolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.cross Tenant Access Policy API
  slug: azure-ad-policies-crosstenantaccesspolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.deviceRegistrationPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.deviceregistrationpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.device Registration Policy API
  slug: azure-ad-policies-deviceregistrationpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.featureRolloutPolicy API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for policies.featurerolloutpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.feature Rollout Policy API
  slug: azure-ad-policies-featurerolloutpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.federatedTokenValidationPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.federatedtokenvalidationpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.federated Token Validation Policy API
  slug: azure-ad-policies-federatedtokenvalidationpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.homeRealmDiscoveryPolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.homerealmdiscoverypolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.home Realm Discovery Policy API
  slug: azure-ad-policies-homerealmdiscoverypolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.identitySecurityDefaultsEnforcementPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.identitysecuritydefaultsenforcementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.identity Security Defaults Enforcement Policy API
  slug: azure-ad-policies-identitysecuritydefaultsenforcementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.ownerlessGroupPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.ownerlessgrouppolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.ownerless Group Policy API
  slug: azure-ad-policies-ownerlessgrouppolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.permissionGrantPolicy API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for policies.permissiongrantpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.permission Grant Policy API
  slug: azure-ad-policies-permissiongrantpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.policyRoot API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.policyroot.
  name: Microsoft Entra ID (formerly Azure AD) Policies.policy Root API
  slug: azure-ad-policies-policyroot-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.tenantAppManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for policies.tenantappmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.tenant App Management Policy API
  slug: azure-ad-policies-tenantappmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.tokenIssuancePolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.tokenissuancepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.token Issuance Policy API
  slug: azure-ad-policies-tokenissuancepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.tokenLifetimePolicy API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for policies.tokenlifetimepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.token Lifetime Policy API
  slug: azure-ad-policies-tokenlifetimepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.unifiedRoleManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 9 operation(s) for policies.unifiedrolemanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Policies.unified Role Management Policy API
  slug: azure-ad-policies-unifiedrolemanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The policies.unifiedRoleManagementPolicyAssignment API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for policies.unifiedrolemanagementpolicyassignment.
  name: Microsoft Entra ID (formerly Azure AD) Policies.unified Role Management Policy Assignment API
  slug: azure-ad-policies-unifiedrolemanagementpolicyassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The roleManagement.rbacApplication API from Microsoft Entra ID (formerly Azure AD) — 150 operation(s) for rolemanagement.rbacapplication.
  name: Microsoft Entra ID (formerly Azure AD) Role Management.rbac Application API
  slug: azure-ad-rolemanagement-rbacapplication-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.appManagementPolicy API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.appmanagementpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.app Management Policy API
  slug: azure-ad-serviceprincipals-appmanagementpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.appRoleAssignment API from Microsoft Entra ID (formerly Azure AD) — 6 operation(s) for serviceprincipals.approleassignment.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.app Role Assignment API
  slug: azure-ad-serviceprincipals-approleassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.claimsMappingPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.claimsmappingpolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.claims Mapping Policy API
  slug: azure-ad-serviceprincipals-claimsmappingpolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.delegatedPermissionClassification API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.delegatedpermissionclassification.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.delegated Permission Classification API
  slug: azure-ad-serviceprincipals-delegatedpermissionclassification-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 64 operation(s) for serviceprincipals.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.directory Object API
  slug: azure-ad-serviceprincipals-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.endpoint API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.endpoint.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.endpoint API
  slug: azure-ad-serviceprincipals-endpoint-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.federatedIdentityCredential API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.federatedidentitycredential.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.federated Identity Credential API
  slug: azure-ad-serviceprincipals-federatedidentitycredential-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.homeRealmDiscoveryPolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.homerealmdiscoverypolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.home Realm Discovery Policy API
  slug: azure-ad-serviceprincipals-homerealmdiscoverypolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.oAuth2PermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for serviceprincipals.oauth2permissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.o Auth2 Permission Grant API
  slug: azure-ad-serviceprincipals-oauth2permissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.remoteDesktopSecurityConfiguration API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for serviceprincipals.remotedesktopsecurityconfiguration.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.remote Desktop Security Configuration API
  slug: azure-ad-serviceprincipals-remotedesktopsecurityconfiguration-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.servicePrincipal.Actions API from Microsoft Entra ID (formerly Azure AD) — 13 operation(s) for serviceprincipals.serviceprincipal.actions.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.service Principal.Actions API
  slug: azure-ad-serviceprincipals-serviceprincipal-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.servicePrincipal API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.serviceprincipal.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.service Principal API
  slug: azure-ad-serviceprincipals-serviceprincipal-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.servicePrincipal.Functions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for serviceprincipals.serviceprincipal.functions.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.service Principal.Functions API
  slug: azure-ad-serviceprincipals-serviceprincipal-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.synchronization API from Microsoft Entra ID (formerly Azure AD) — 34 operation(s) for serviceprincipals.synchronization.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.synchronization API
  slug: azure-ad-serviceprincipals-synchronization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.tokenIssuancePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.tokenissuancepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.token Issuance Policy API
  slug: azure-ad-serviceprincipals-tokenissuancepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The servicePrincipals.tokenLifetimePolicy API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for serviceprincipals.tokenlifetimepolicy.
  name: Microsoft Entra ID (formerly Azure AD) Service Principals.token Lifetime Policy API
  slug: azure-ad-serviceprincipals-tokenlifetimepolicy-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The subscribedSkus.subscribedSku API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for subscribedskus.subscribedsku.
  name: Microsoft Entra ID (formerly Azure AD) Subscribed Skus.subscribed Sku API
  slug: azure-ad-subscribedskus-subscribedsku-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The subscriptions.subscription.Actions API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for subscriptions.subscription.actions.
  name: Microsoft Entra ID (formerly Azure AD) Subscriptions.subscription.Actions API
  slug: azure-ad-subscriptions-subscription-actions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The subscriptions.subscription API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for subscriptions.subscription.
  name: Microsoft Entra ID (formerly Azure AD) Subscriptions.subscription API
  slug: azure-ad-subscriptions-subscription-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The tenantRelationships.multiTenantOrganization API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for tenantrelationships.multitenantorganization.
  name: Microsoft Entra ID (formerly Azure AD) Tenant Relationships.multi Tenant Organization API
  slug: azure-ad-tenantrelationships-multitenantorganization-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The tenantRelationships.tenantRelationship.Functions API from Microsoft Entra ID (formerly Azure AD) — 2 operation(s) for tenantrelationships.tenantrelationship.functions.
  name: Microsoft Entra ID (formerly Azure AD) Tenant Relationships.tenant Relationship.Functions API
  slug: azure-ad-tenantrelationships-tenantrelationship-functions-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.agreementAcceptance API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.agreementacceptance.
  name: Microsoft Entra ID (formerly Azure AD) Users.agreement Acceptance API
  slug: azure-ad-users-agreementacceptance-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: User accounts in the directory
  name: Microsoft Entra ID (formerly Azure AD) Users API
  slug: azure-ad-users-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.appRoleAssignment API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.approleassignment.
  name: Microsoft Entra ID (formerly Azure AD) Users.app Role Assignment API
  slug: azure-ad-users-approleassignment-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.authentication API from Microsoft Entra ID (formerly Azure AD) — 44 operation(s) for users.authentication.
  name: Microsoft Entra ID (formerly Azure AD) Users.authentication API
  slug: azure-ad-users-authentication-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.directoryObject API from Microsoft Entra ID (formerly Azure AD) — 84 operation(s) for users.directoryobject.
  name: Microsoft Entra ID (formerly Azure AD) Users.directory Object API
  slug: azure-ad-users-directoryobject-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.extension API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.extension.
  name: Microsoft Entra ID (formerly Azure AD) Users.extension API
  slug: azure-ad-users-extension-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.itemInsights API from Microsoft Entra ID (formerly Azure AD) — 14 operation(s) for users.iteminsights.
  name: Microsoft Entra ID (formerly Azure AD) Users.item Insights API
  slug: azure-ad-users-iteminsights-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.licenseDetails API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for users.licensedetails.
  name: Microsoft Entra ID (formerly Azure AD) Users.license Details API
  slug: azure-ad-users-licensedetails-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.mailboxSettings API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for users.mailboxsettings.
  name: Microsoft Entra ID (formerly Azure AD) Users.mailbox Settings API
  slug: azure-ad-users-mailboxsettings-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.oAuth2PermissionGrant API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.oauth2permissiongrant.
  name: Microsoft Entra ID (formerly Azure AD) Users.o Auth2 Permission Grant API
  slug: azure-ad-users-oauth2permissiongrant-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.onPremisesSyncBehavior API from Microsoft Entra ID (formerly Azure AD) — 1 operation(s) for users.onpremisessyncbehavior.
  name: Microsoft Entra ID (formerly Azure AD) Users.on Premises Sync Behavior API
  slug: azure-ad-users-onpremisessyncbehavior-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.outlookUser API from Microsoft Entra ID (formerly Azure AD) — 7 operation(s) for users.outlookuser.
  name: Microsoft Entra ID (formerly Azure AD) Users.outlook User API
  slug: azure-ad-users-outlookuser-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.profilePhoto API from Microsoft Entra ID (formerly Azure AD) — 5 operation(s) for users.profilephoto.
  name: Microsoft Entra ID (formerly Azure AD) Users.profile Photo API
  slug: azure-ad-users-profilephoto-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.scopedRoleMembership API from Microsoft Entra ID (formerly Azure AD) — 3 operation(s) for users.scopedrolemembership.
  name: Microsoft Entra ID (formerly Azure AD) Users.scoped Role Membership API
  slug: azure-ad-users-scopedrolemembership-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.todo API from Microsoft Entra ID (formerly Azure AD) — 30 operation(s) for users.todo.
  name: Microsoft Entra ID (formerly Azure AD) Users.todo API
  slug: azure-ad-users-todo-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.user API from Microsoft Entra ID (formerly Azure AD) — 4 operation(s) for users.user.
  name: Microsoft Entra ID (formerly Azure AD) Users.user API
  slug: azure-ad-users-user-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The users.userSettings API from Microsoft Entra ID (formerly Azure AD) — 24 operation(s) for users.usersettings.
  name: Microsoft Entra ID (formerly Azure AD) Users.user Settings API
  slug: azure-ad-users-usersettings-api
artifact_total: 224
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
overview: 'Microsoft Entra ID (formerly Azure AD) publishes 186 APIs on the [APIs.io](https://apis.io/) network, including Azure Active Directory Me API, Admin.people Admin Settings API, Agreements.agreement API, and 183 more. Tagged areas include Authentication, Authorization, Identity, OpenID Connect, and SSO.


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
  composite: 79.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 82.7
    discoverability: 75.9
    operational_transparency: 97.4
  previous_composite: 77.9
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
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
