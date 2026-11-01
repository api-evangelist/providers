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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: Config, Log export, and IP APIs plus SCIM 2.0 user/group provisioning for Forcepoint ONE / Data Security Cloud (SSE). OAuth 2.0 bearer authentication with configurable permission scopes.
  name: Forcepoint Data Security Cloud | SSE REST API
  slug: forcepoint-data-security-cloud-sse-rest-api
- baseURL: https://{dlpManagerHost}:{dlpManagerPort}/dlp/rest/v1
  baseurl_source: declared
  description: REST API for Forcepoint Data Loss Prevention policy management; JSON over HTTP(S).
  name: Forcepoint DLP REST API
  slug: forcepoint-dlp-rest-api
- description: RESTful Security Management Center (SMC) API for Forcepoint Next-Generation Firewall — engines, network elements, and policy automation (JSON/XML). API-key authentication via an SMC API Client.
  name: Forcepoint NGFW SMC API
  slug: forcepoint-ngfw-smc-api
- description: REST API for managing Forcepoint appliances (basic auth over HTTP(S)).
  name: Forcepoint Appliance REST API
  slug: forcepoint-appliance-rest-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/forcepoint/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/forcepoint/rules/forcepoint-rules.yml
  title: ''
  type: Spectral
  url: rules/forcepoint-rules.yml
- group: design
  href: https://artifacts.apis.io/forcepoint/vocabulary/forcepoint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/forcepoint-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/forcepoint/well-known/forcepoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/forcepoint-well-known.yml
- group: other
  href: https://artifacts.apis.io/forcepoint/hosts/forcepoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/forcepoint-hosts.yml
- group: build
  href: https://artifacts.apis.io/forcepoint/integrations/forcepoint-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/forcepoint-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/forcepoint/vendors/forcepoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/forcepoint-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.forcepoint.com/security/cloud
- group: company
  title: ''
  type: Newsroom
  url: https://www.forcepoint.com/newsroom
- group: start
  title: ''
  type: GettingStarted
  url: https://help.forcepoint.com/fpone/Interoperability/Getting_started_guide/index.html
- group: company
  title: ''
  type: Website
  url: https://forcepoint.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.forcepoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.forcepoint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.forcepoint.com/dlp/90/restapi/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Forcepoint
- group: operate
  title: ''
  type: Support
  url: https://support.forcepoint.com/
- group: company
  title: ''
  type: Blog
  url: https://www.forcepoint.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forcepoint.com/legal/website-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forcepoint.com/company/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forcepoint.com/
- group: auth
  href: https://artifacts.apis.io/forcepoint/security/forcepoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/forcepoint-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.forcepoint.com/
- group: auth
  href: https://artifacts.apis.io/forcepoint/authentication/forcepoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/forcepoint-authentication.yml
- group: build
  href: https://artifacts.apis.io/forcepoint/packages/forcepoint-packages.yml
  title: ''
  type: Packages
  url: packages/forcepoint-packages.yml
- group: build
  href: https://artifacts.apis.io/forcepoint/packages/forcepoint-packages.yml
  title: ''
  type: SDKs
  url: packages/forcepoint-packages.yml
- group: design
  href: https://artifacts.apis.io/forcepoint/conformance/forcepoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forcepoint-conformance.yml
- group: design
  href: https://artifacts.apis.io/forcepoint/lifecycle/forcepoint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/forcepoint-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/forcepoint/security/forcepoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forcepoint-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/forcepoint/llms/forcepoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/forcepoint-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forcepoint.com/form/pricing-request
- group: start
  title: ''
  type: Login
  url: https://education.forcepoint.com/account/Login
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://support.forcepoint.com/mcp/v1
  - status: 200
    url: https://forcepoint.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: 'Forcepoint is a data-first cybersecurity vendor whose platform spans Data Loss Prevention (DLP), Security Service Edge / SASE (Forcepoint ONE and Data Security Cloud | SSE), Next-Generation Firewall (NGFW), and web, email, and data security. For developers and security engineers Forcepoint exposes several product REST APIs — DLP policy management, SSE Config/Log/IP and SCIM 2.0 provisioning, the NGFW Security Management Center (SMC) API, and an Appliance management API — documented on help.forcepoint.com. Auth varies by product: OAuth 2.0 bearer tokens for SSE, API-key clients for the NGFW SMC, and basic/session auth for DLP and appliances. Forcepoint publishes official automation tooling including the fp-NGFW-SMC-python SDK (PyPI), Ansible modules, and a Terraform provider, and runs a public status portal and trust center (SOC 2, ISO 27001/27017/27018, CSA STAR, FIPS 140, GDPR).'
image: https://logo.clearbit.com/forcepoint.com
layout: provider
modified: '2026-10-20'
name: Forcepoint
nav: Providers
network: true
overview: 'Forcepoint is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including DLP REST API, and 3 more. Tagged areas include Company, Cybersecurity, Security, Data Loss Prevention, and SASE.


  The Forcepoint catalog on APIs.io includes 1 Spectral governance ruleset.


  Forcepoint''s developer surface includes getting-started guide, documentation, API reference, support, engineering blog, authentication, pricing, and 24 more developer resources.'
plans:
- name: Forcepoint Plans Pricing
  plan_count: 0
  slug: forcepoint-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Forcepoint Rate Limits
  slug: forcepoint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Forcepoint API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: forcepoint-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 11.1
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 45.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/forcepoint/forcepoint-2026-07-25T214926.png
security:
- kind: authentication
  name: Forcepoint Authentication
  slug: forcepoint-authentication
  summary_line: oauth2/apiKey/http · 4 schemes
- kind: domain-security
  name: Forcepoint Domain Security
  slug: forcepoint-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Forcepoint Trust Center
  slug: forcepoint-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR, FIPS 140
skill_count: 1
skills:
- name: manage-dlp-policy-rules
  slug: forcepoint-manage-dlp-policy-rules
slug: forcepoint
tags:
- Company
- Cybersecurity
- Security
- Data Loss Prevention
- SASE
- Security Service Edge
- Firewall
- Data Security
- Cloud Security
website: https://forcepoint.com
---
