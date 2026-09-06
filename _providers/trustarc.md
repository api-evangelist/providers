---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 132
  human_in_the_loop: 17
  name: Trustarc Agentic Access
  operation_count: 276
  slug: trustarc-agentic-access
  summary_line: 276 operations · 132 acting · 17 human-in-the-loop
api_count: 2
apis:
- description: Manage the website inventory of a Cookie Consent Manager instance and queue tracker scans. Version v1.0, released 2025-04-23, with a published versioning policy (URI versioning, 12-month support for s
  name: TrustArc Cookie Consent Manager External API
  slug: trustarc-cookie-consent-manager-external-api
- description: Create, label, search and close data subject requests (DSR/DSAR) in Individual Rights Manager, and register callbacks for request status changes. Request bodies are keyed by per-form field IDs discove
  name: TrustArc Individual Rights Manager External API
  slug: trustarc-individual-rights-manager-external-api
- description: Read and write consent records, consent forms, data subjects and their callbacks in Consent & Preference Manager, with a matching EU data-residency deployment at cpm.trustarc.eu. Exposes external cons
  name: TrustArc Consent & Preference Manager External API
  slug: trustarc-consent-preference-manager-external-api
- description: Synchronize the privacy data inventory — Business Processes, IT Systems, Company Affiliates and Third Parties — between a customer system of record and TrustArc's Data Mapping & Risk Manager. Every re
  name: TrustArc Data Mapping Hub External Integration API
  slug: trustarc-data-mapping-hub-external-integration-api
- description: Pull consent analytics out of Cookie Consent Manager — analytics reports, consent locations and GDPR reports, in JSON and CSV. Version 1.4 of the guide, last updated 2026-01-07. Auth server login.trus
  name: TrustArc Cookie Consent Manager Reporting API
  slug: trustarc-cookie-consent-manager-reporting-api
- description: Create Assessment Manager projects (PIA/DPIA/TIA) programmatically over a RESTful surface, plus an external-integration project answer endpoint and packaged Salesforce and ServiceNow connectors. Docum
  name: TrustArc Assessment Manager API
  slug: trustarc-assessment-manager-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts API from TrustArc — 14 operation(s) for accounts.
  name: TrustArc Accounts API
  slug: trustarc-accounts-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-CustomMetaTags API from TrustArc — 7 operation(s) for accounts-custommetatags.
  name: TrustArc Accounts Custom Meta Tags API
  slug: trustarc-accounts-custommetatags-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-Extension API from TrustArc — 6 operation(s) for accounts-extension.
  name: TrustArc Accounts Extension API
  slug: trustarc-accounts-extension-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-fieldtypes API from TrustArc — 3 operation(s) for accounts-fieldtypes.
  name: TrustArc Accounts Fieldtypes API
  slug: trustarc-accounts-fieldtypes-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-MetaTags API from TrustArc — 3 operation(s) for accounts-metatags.
  name: TrustArc Accounts Meta Tags API
  slug: trustarc-accounts-metatags-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-OrganizationalStructure API from TrustArc — 6 operation(s) for accounts-organizationalstructure.
  name: TrustArc Accounts Organizational Structure API
  slug: trustarc-accounts-organizationalstructure-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-PickTags API from TrustArc — 4 operation(s) for accounts-picktags.
  name: TrustArc Accounts Pick Tags API
  slug: trustarc-accounts-picktags-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-Prefaces API from TrustArc — 3 operation(s) for accounts-prefaces.
  name: TrustArc Accounts Prefaces API
  slug: trustarc-accounts-prefaces-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-ReportConfigs API from TrustArc — 3 operation(s) for accounts-reportconfigs.
  name: TrustArc Accounts Report Configs API
  slug: trustarc-accounts-reportconfigs-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-SubAccount API from TrustArc — 2 operation(s) for accounts-subaccount.
  name: TrustArc Accounts Sub Account API
  slug: trustarc-accounts-subaccount-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-Tokens API from TrustArc — 3 operation(s) for accounts-tokens.
  name: TrustArc Accounts Tokens API
  slug: trustarc-accounts-tokens-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Accounts-UserGroups API from TrustArc — 1 operation(s) for accounts-usergroups.
  name: TrustArc Accounts User Groups API
  slug: trustarc-accounts-usergroups-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: Monitor and interact
  name: TrustArc Actuator API
  slug: trustarc-actuator-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The anon-credential-resource API from TrustArc — 2 operation(s) for anon-credential-resource.
  name: TrustArc Anon Credential Resource API
  slug: trustarc-anon-credential-resource-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The anon-session-controller API from TrustArc — 1 operation(s) for anon-session-controller.
  name: TrustArc Anon Session Controller API
  slug: trustarc-anon-session-controller-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Clients API from TrustArc — 13 operation(s) for clients.
  name: TrustArc Clients API
  slug: trustarc-clients-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Clients-Extension API from TrustArc — 1 operation(s) for clients-extension.
  name: TrustArc Clients Extension API
  slug: trustarc-clients-extension-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Clients-Extension-License API from TrustArc — 3 operation(s) for clients-extension-license.
  name: TrustArc Clients Extension License API
  slug: trustarc-clients-extension-license-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Clients-Roles API from TrustArc — 2 operation(s) for clients-roles.
  name: TrustArc Clients Roles API
  slug: trustarc-clients-roles-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Clients-UserGroups API from TrustArc — 3 operation(s) for clients-usergroups.
  name: TrustArc Clients User Groups API
  slug: trustarc-clients-usergroups-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Email Templates API from TrustArc — 4 operation(s) for email templates.
  name: TrustArc Email Templates API
  slug: trustarc-email-templates-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Entity Configs API from TrustArc — 4 operation(s) for entity configs.
  name: TrustArc Entity Configs API
  slug: trustarc-entity-configs-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Groups API from TrustArc — 2 operation(s) for groups.
  name: TrustArc Groups API
  slug: trustarc-groups-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The History API from TrustArc — 3 operation(s) for history.
  name: TrustArc History API
  slug: trustarc-history-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Jobs API from TrustArc — 3 operation(s) for jobs.
  name: TrustArc Jobs API
  slug: trustarc-jobs-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Navigation-Menus API from TrustArc — 4 operation(s) for navigation-menus.
  name: TrustArc Navigation Menus API
  slug: trustarc-navigation-menus-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Nymity API from TrustArc — 2 operation(s) for nymity.
  name: TrustArc Nymity API
  slug: trustarc-nymity-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The PermissionProfiles API from TrustArc — 5 operation(s) for permissionprofiles.
  name: TrustArc Permission Profiles API
  slug: trustarc-permissionprofiles-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Preface API from TrustArc — 3 operation(s) for preface.
  name: TrustArc Preface API
  slug: trustarc-preface-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Reports API from TrustArc — 2 operation(s) for reports.
  name: TrustArc Reports API
  slug: trustarc-reports-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Schedules API from TrustArc — 3 operation(s) for schedules.
  name: TrustArc Schedules API
  slug: trustarc-schedules-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Scim API from TrustArc — 5 operation(s) for scim.
  name: TrustArc SCIM API
  slug: trustarc-scim-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Sessions API from TrustArc — 5 operation(s) for sessions.
  name: TrustArc Sessions API
  slug: trustarc-sessions-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The sso-login-controller API from TrustArc — 1 operation(s) for sso-login-controller.
  name: TrustArc SSO Login Controller API
  slug: trustarc-sso-login-controller-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Storage API from TrustArc — 1 operation(s) for storage.
  name: TrustArc Storage API
  slug: trustarc-storage-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Sysinfo API from TrustArc — 1 operation(s) for sysinfo.
  name: TrustArc Sysinfo API
  slug: trustarc-sysinfo-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Translations API from TrustArc — 2 operation(s) for translations.
  name: TrustArc Translations API
  slug: trustarc-translations-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The user-info-resource API from TrustArc — 1 operation(s) for user-info-resource.
  name: TrustArc User Info Resource API
  slug: trustarc-user-info-resource-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The UserProfiles-Activations API from TrustArc — 2 operation(s) for userprofiles-activations.
  name: TrustArc User Profiles Activations API
  slug: trustarc-userprofiles-activations-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The UserProfiles API from TrustArc — 11 operation(s) for userprofiles.
  name: TrustArc User Profiles API
  slug: trustarc-userprofiles-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The UserProfiles-Users API from TrustArc — 4 operation(s) for userprofiles-users.
  name: TrustArc User Profiles Users API
  slug: trustarc-userprofiles-users-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users API from TrustArc — 34 operation(s) for users.
  name: TrustArc Users API
  slug: trustarc-users-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-Audits API from TrustArc — 1 operation(s) for users-audits.
  name: TrustArc Users Audits API
  slug: trustarc-users-audits-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-Extension API from TrustArc — 1 operation(s) for users-extension.
  name: TrustArc Users Extension API
  slug: trustarc-users-extension-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-fieldtypes API from TrustArc — 2 operation(s) for users-fieldtypes.
  name: TrustArc Users Fieldtypes API
  slug: trustarc-users-fieldtypes-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-History API from TrustArc — 3 operation(s) for users-history.
  name: TrustArc Users History API
  slug: trustarc-users-history-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-MetaTags API from TrustArc — 4 operation(s) for users-metatags.
  name: TrustArc Users Meta Tags API
  slug: trustarc-users-metatags-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-Simple API from TrustArc — 1 operation(s) for users-simple.
  name: TrustArc Users Simple API
  slug: trustarc-users-simple-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Users-Switch API from TrustArc — 1 operation(s) for users-switch.
  name: TrustArc Users Switch API
  slug: trustarc-users-switch-api
- baseURL: https://login.truste.com
  baseurl_source: declared
  description: The Xauths API from TrustArc — 4 operation(s) for xauths.
  name: TrustArc Xauths API
  slug: trustarc-xauths-api
artifact_total: 64
asyncapis:
- description: ''
  name: Trustarc Webhooks
  slug: trustarc-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/trustarc-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/trustarc-scim-user-provisioning.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trustarc-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trustarc-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustarc-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trustarc-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustarc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trustarc.com
- group: other
  title: ''
  type: Company
  url: https://trustarc.com/company/
- group: other
  title: ''
  type: Products
  url: https://trustarc.com/products/
- group: commercial
  title: ''
  type: PrivacyStudio
  url: https://trustarc.com/products/consent-consumer-rights/
- group: other
  title: ''
  type: CookieConsentManager
  url: https://trustarc.com/products/consent-consumer-rights/cookie-consent-manager/
- group: docs
  title: ''
  type: ConsentPreferenceManager
  url: https://trustarc.com/products/consent-consumer-rights/consent-preference-manager/
- group: other
  title: ''
  type: IndividualRightsManager
  url: https://trustarc.com/products/consent-consumer-rights/individual-rights-manager/
- group: auth
  title: ''
  type: UnifiedTrustCenter
  url: https://trustarc.com/products/consent-consumer-rights/trust-center/
- group: other
  title: ''
  type: GovernanceSuite
  url: https://trustarc.com/products/privacy-data-governance/
- group: commercial
  title: ''
  type: PrivacyCentral
  url: https://trustarc.com/products/privacy-data-governance/privacycentral/
- group: other
  title: ''
  type: DataMappingRiskManager
  url: https://trustarc.com/products/privacy-data-governance/data-inventory-mapping/
- group: other
  title: ''
  type: AssessmentManager
  url: https://trustarc.com/products/privacy-data-governance/assessment-manager/
- group: other
  title: ''
  type: NymityResearch
  url: https://trustarc.com/products/privacy-data-governance/nymity-research/
- group: other
  title: ''
  type: AssuranceServices
  url: https://trustarc.com/products/assurance-certifications/
- group: operate
  title: ''
  type: HelpCenter
  url: https://trustarchelp.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIGuides
  url: https://trustarchelp.zendesk.com/hc/en-us/sections/36115648969363-API-Guides
- group: build
  title: ''
  type: MobileSDKiOS
  url: https://trustarchelp.zendesk.com/hc/en-us/articles/32900734257939-iOS
- group: other
  title: ''
  type: Resources
  url: https://trustarc.com/resources/
- group: start
  title: ''
  type: Login
  url: https://login.truste.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/trustarc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TrustArc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustarc
- group: build
  title: ''
  type: Packages
  url: packages/trustarc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trustarc-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trustarc-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trustarc-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/trustarc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.trustarc.com/en-US/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.trustarc.com/en-US/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trustarc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trustarc-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trustarc.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://trustarchelp.zendesk.com/hc/en-us/articles/53518189041043-API-Versioning-Changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/trustarc-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trustarc-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/trustarc-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trustarc-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trustarc-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trustarc-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trustarc-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trustarc-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/trustarc-guardian-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://trustarchelp.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://trustarchelp.zendesk.com/hc/en-us/articles/53517557106963-API-Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://trustarchelp.zendesk.com/hc/en-us/articles/53517235461651-Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://trustarc.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://trustarc.com/resources/?action=resources&type=blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trustarc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.trustarc.com/en-US/policies/site-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.trustarc.com/en-US/policies/trustarc-privacy-notice
- group: start
  title: ''
  type: SignUp
  url: https://trustarc.com/demo-request/
created: '2026-05-25'
description: 'TrustArc is a Walnut Creek, California enterprise privacy management platform that helps organizations operationalize global data privacy programs. Its product portfolio spans three suites. Privacy Studio covers consumer-facing consent and rights with Cookie Consent Manager, Consent & Preference Manager, Individual Rights Manager (DSR automation), and the Unified Trust Center. The Governance Suite covers internal privacy program operations with PrivacyCentral, Data Mapping & Risk Manager, Assessment Manager (PIA/DPIA/TIA), and Nymity Research for regulatory intelligence. Assurance Services delivers third-party attestations including Data Privacy Framework verification, GDPR and CCPA/CPRA validation, APEC CBPR/PRP, and TRUSTe Responsible AI Certification. TrustArc exposes a developer surface through gated APIs documented in the customer help center — including the Gateway API, Individual Rights Manager Rapid/Client APIs, Cookie Consent Manager Reporting API, Consent & Preference
  Manager Rapid/Standard APIs, and Assessment Manager Internal API — plus a Mobile Consent SDK (iOS), 300+ prebuilt connectors to platforms such as Salesforce, HubSpot, Marketo, Adobe Experience Manager, Microsoft Dynamics, Jira, and Google Workspace, and a Google Consent Mode v2 template published on GitHub. The developer surface is larger than it looks: TrustArc serves one machine-readable contract openly — the Guardian identity API at login.truste.com/v3/api-docs, an OpenAPI 3.1.0 document with 205 paths, 276 operations and 158 schemas that includes a standards-compliant SCIM 2.0 provisioning surface — plus OpenID Connect and RFC 8414 discovery documents advertising PKCE, mTLS-bound tokens, DPoP and token exchange. Six further external APIs (Cookie Consent Manager External v1, CCM Reporting, Individual Rights Manager, Consent & Preference Manager, the Data Mapping Hub external-integration API and Assessment Manager) are fully documented in the public help center with endpoints, payloads,
  status codes and a versioning and deprecation policy, but publish no OpenAPI. Founded over 28 years ago and serving 1,500+ enterprises including Abbott, ADP, GE, Nike, and Starbucks, TrustArc operates on a commercial SaaS model with no published pricing; API credentials are issued by an account administrator rather than self-service.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustarc.png
layout: provider
modified: '2026-08-27'
name: TrustArc
nav: Providers
network: true
overview: 'TrustArc publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Accounts Custom Meta Tags API, Accounts Extension API, and 47 more. Tagged areas include Privacy, Data Privacy, SCIM, Identity, and Authentication.


  The TrustArc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TrustArc''s developer surface includes authentication, GitHub presence, changelog, sandbox, documentation, API reference, getting-started guide, and 52 more developer resources.'
plans:
- name: Trustarc Plans Pricing
  plan_count: 0
  slug: trustarc-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Trustarc Rate Limits
  slug: trustarc-rate-limits
scopes:
- name: Trustarc Scopes
  scope_count: 1
  slug: trustarc-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 63.7
    discoverability: 63.0
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustarc/refs/heads/main/screenshots/trustarc-2026-06-20T195803.png
security:
- kind: authentication
  name: Trustarc Authentication
  slug: trustarc-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Trustarc Domain Security
  slug: trustarc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trustarc Trust Center
  slug: trustarc-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: trustarc
tags:
- Privacy
- Data Privacy
- SCIM
- Identity
- Authentication
- OpenID Connect
- User Provisioning
- Privacy Management
- Consent Management
- Cookie Consent
- Preference Management
- Data Subject Rights
- DSR
- Privacy Governance
- Data Mapping
- Privacy Assessments
- PIA
- DPIA
- GDPR
- CCPA
- CPRA
- Data Privacy Framework
- TRUSTe
- AI Governance
- Responsible AI
- Compliance
- Certifications
- RegTech
- Trust Center
- Enterprise Saas
website: https://trustarc.com
---
