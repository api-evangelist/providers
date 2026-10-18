---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.centrify.com/'', ''status'': 301, ''note'': ''declared website redirects to https://delinea.com/centrify — a different registrable domain (centrify.com -> delinea.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 658
  human_in_the_loop: 16
  name: Centrify Agentic Access
  operation_count: 799
  slug: centrify-agentic-access
  summary_line: 799 operations · 658 acting · 16 human-in-the-loop
api_count: 15
apis:
- description: REST API for the Centrify Identity Platform / Cloud Suite (PAS). Programmatic access to authentication profiles, users, directories, roles, sets, resources, secrets, privileged access requests, connec
  name: Centrify Identity Services API
  slug: centrify-identity-services-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The Apis API from Centrify — 5 operation(s) for apis.
  name: Centrify APIs API
  slug: centrify-apis-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage applications and SaaS
  name: Centrify Application Management API
  slug: centrify-application-management-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Authenticate to cloud service, MFA
  name: Centrify Authentication API
  slug: centrify-authentication-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage users for the Centrify Cloud Directory Service
  name: Centrify Cloud User Management API
  slug: centrify-cloud-user-management-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Utility functions and basic ops
  name: Centrify Core Services API
  slug: centrify-core-services-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The Dataset API from Centrify — 1 operation(s) for dataset.
  name: Centrify Dataset API
  slug: centrify-dataset-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage devices
  name: Centrify Device Management API
  slug: centrify-device-management-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage directory services
  name: Centrify Directory Services API
  slug: centrify-directory-services-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The File API from Centrify — 2 operation(s) for file.
  name: Centrify File API
  slug: centrify-file-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The GetDiscoveryProfiles API from Centrify — 1 operation(s) for getdiscoveryprofiles.
  name: Centrify Get Discovery Profiles API
  slug: centrify-getdiscoveryprofiles-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The GetDiscoveryStatus API from Centrify — 1 operation(s) for getdiscoverystatus.
  name: Centrify Get Discovery Status API
  slug: centrify-getdiscoverystatus-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The GetRoleApps API from Centrify — 1 operation(s) for getroleapps.
  name: Centrify Get Role Apps API
  slug: centrify-getroleapps-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The GetScript API from Centrify — 1 operation(s) for getscript.
  name: Centrify Get Script API
  slug: centrify-getscript-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The GetSSOToken API from Centrify — 1 operation(s) for getssotoken.
  name: Centrify Get SSO Token API
  slug: centrify-getssotoken-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The HandleAppClick API from Centrify — 1 operation(s) for handleappclick.
  name: Centrify Handle App Click API
  slug: centrify-handleappclick-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The Jumpterm API from Centrify — 1 operation(s) for jumpterm.
  name: Centrify Jumpterm API
  slug: centrify-jumpterm-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Access Cloud Service database
  name: Centrify Reports API
  slug: centrify-reports-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage resources and accounts for CPS
  name: Centrify Resource Management API
  slug: centrify-resource-management-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage roles and admin rights
  name: Centrify Role Management API
  slug: centrify-role-management-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The Rules API from Centrify — 5 operation(s) for rules.
  name: Centrify Rules API
  slug: centrify-rules-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The RunDiscovery API from Centrify — 1 operation(s) for rundiscovery.
  name: Centrify Run Discovery API
  slug: centrify-rundiscovery-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The ServerAgent API from Centrify — 1 operation(s) for serveragent.
  name: Centrify Server Agent API
  slug: centrify-serveragent-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: The SetApplicationPermissions API from Centrify — 1 operation(s) for setapplicationpermissions.
  name: Centrify Set Application Permissions API
  slug: centrify-setapplicationpermissions-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage users for all Directory Services (AD, Cloud, LDAP, etc)
  name: Centrify User Management API
  slug: centrify-user-management-api
- baseURL: https://developer.delinea.com/reference
  baseurl_source: declared
  description: Manage workflows
  name: Centrify Workflow Management API
  slug: centrify-workflow-management-api
artifact_total: 39
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/agentic-access/centrify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/centrify-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/rules/centrify-rules.yml
  title: ''
  type: Spectral
  url: rules/centrify-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/json-ld/centrify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centrify-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/vocabulary/centrify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centrify-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/data-model/centrify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/centrify-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/errors/centrify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/centrify-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/hosts/centrify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centrify-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/vendors/centrify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centrify-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://delinea.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.delinea.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://delinea.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://delinea.com/news
- group: other
  title: ''
  type: Leadership
  url: https://delinea.com/leadership
- group: company
  title: ''
  type: Website
  url: https://www.centrify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.delinea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.delinea.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.delinea.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.delinea.com/docs/getting-access-to-the-api
- group: docs
  title: ''
  type: DocumentationLibrary
  url: https://docs.centrify.com/
- group: operate
  title: ''
  type: Support
  url: https://support.delinea.com/s/
- group: company
  title: ''
  type: Blog
  url: https://delinea.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://delinea.com/centrify
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DelineaXPM
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/authentication/centrify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/centrify-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/packages/centrify-packages.yml
  title: ''
  type: SDKs
  url: packages/centrify-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/packages/centrify-packages.yml
  title: ''
  type: Packages
  url: packages/centrify-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/cli/centrify-cli.yml
  title: ''
  type: CLI
  url: cli/centrify-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/well-known/centrify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centrify-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/well-known/centrify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/centrify-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/security/centrify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centrify-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/security/centrify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/centrify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.delinea.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/security/centrify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/centrify-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/conformance/centrify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centrify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.delinea.com/
created: '2026-07-17'
description: Centrify is an identity and privileged access management (PAM) platform now delivered as part of Delinea (the company formed from the Centrify + Thycotic merger). The Centrify Identity Platform / Cloud Suite / Privileged Access Service secures access to applications, servers, network infrastructure, and privileged accounts with adaptive multi-factor authentication, single sign-on, least-privilege enforcement, session auditing, and analytics. The Centrify REST API exposes the full platform programmatically — authentication profiles, users and directories, roles and sets, resources and secrets, privileged access requests, connectors, webhooks, and audit/reporting — authenticated via OAuth2, bearer tokens, or MFA-aware session cookies. centrify.com now redirects to delinea.com and the developer documentation is served at developer.delinea.com.
image: https://delinea.com/hubfs/Delinea/images/logos/delinea-logo.svg
json_schemas:
- name: CoreGetAdTopology
  property_count: 4
  slug: centrify-core-get-ad-topology
- name: SaasManageGetApplication
  property_count: 4
  slug: centrify-saas-manage-get-application
- name: ServerManageGetDiscoveryProfiles
  property_count: 4
  slug: centrify-server-manage-get-discovery-profiles
- name: ServerManageGetMyWorkspaceAccounts
  property_count: 4
  slug: centrify-server-manage-get-my-workspace-accounts
- name: UPRestGetResultantAppsForUser
  property_count: 4
  slug: centrify-uprest-get-resultant-apps-for-user
- name: UserMgmtGetUserInfo
  property_count: 4
  slug: centrify-user-mgmt-get-user-info
jsonld:
- class_count: 120
  name: Centrify Context
  property_count: 4
  slug: centrify-context
layout: provider
modified: '2026-07-18'
name: Centrify
nav: Providers
network: true
overview: 'Centrify publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including APIs API, Application Management API, Authentication API, and 23 more. Tagged areas include Company, Identity, Privileged Access Management, Identity and Access Management, and Authentication.


  The Centrify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Centrify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 28 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Centrify API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: centrify-rules
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 28.9
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 54.7
    developer_ergonomics: 52.4
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 25
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/screenshots/centrify-2026-07-25T204934.png
security:
- kind: authentication
  name: Centrify Authentication
  slug: centrify-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Centrify Domain Security
  slug: centrify-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Centrify Vulnerability Disclosure
  slug: centrify-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Centrify Trust Center
  slug: centrify-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001:2022, PCI DSS v4.0.1, GDPR, EU-US Data Privacy Framework, CCPA, FedRAMP, DESC Cloud Service Provider
slug: centrify
tags:
- Company
- Identity
- Privileged Access Management
- Identity and Access Management
- Authentication
- SSO
- Multi-Factor Authentication
- Security
- Zero Trust
website: https://www.centrify.com/
---
