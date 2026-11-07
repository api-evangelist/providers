---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 59 endpoints across 7 resource families. Every one is a GET, takes your API key in the Authorization header, and answers with data and meta.
  name: EnvoAPI
  slug: envoapi
- baseURL: https://api.envoapi.com
  baseurl_source: declared
  description: 'envoapi-com API as documented publicly: 59 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: envoapi-com API
  slug: envoapi-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/envoapi-com/rules/envoapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/envoapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/envoapi-com/vocabulary/envoapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/envoapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/envoapi-com/conventions/envoapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/envoapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/envoapi-com/authentication/envoapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/envoapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/envoapi-com/errors/envoapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/envoapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/envoapi-com/conformance/envoapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/envoapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/envoapi-com/llms/envoapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/envoapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/envoapi-com/hosts/envoapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/envoapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/envoapi-com/vendors/envoapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/envoapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/envoapi-com/packages/envoapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/envoapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/envoapi-com/packages/envoapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/envoapi-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://envoapi.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.envoapi.com
- group: start
  title: ''
  type: Login
  url: https://envoapi.com/signin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.envoapi.com\
- group: auth
  href: https://artifacts.apis.io/envoapi-com/security/envoapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/envoapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://envoapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.envoapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.envoapi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.envoapi.com/index.md
- group: company
  title: ''
  type: Blog
  url: https://envoapi.com/blog
- group: operate
  title: ''
  type: Support
  url: https://envoapi.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://envoapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://envoapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://envoapi.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envoapi-official
- group: operate
  title: ''
  type: Roadmap
  url: https://envoapi.com/changelog
coverage:
  checked: '2026-10-30'
  detail: API reference page lists endpoints but provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.envoapi.com/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: EnvoAPI provides a suite of B2B data enrichment APIs that allow developers to retrieve professional profile information, company details, LinkedIn data, email verification, and website scraping. The platform offers endpoints for LinkedIn profiles, companies, jobs, search, as well as email finder and disposable email checks. Users can start with 100 free credits and access comprehensive data through a clean RESTful API.
image: https://envoapi.com/og/logo.png
layout: provider
modified: '2026-10-30'
name: envoapi-com
nav: Providers
network: true
overview: 'envoapi-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Enrichment, B2B, LinkedIn, and Email Verification.


  The envoapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  envoapi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 20 more developer resources.'
plans:
- name: Envoapi Com Plans Pricing
  plan_count: 0
  slug: envoapi-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Envoapi Com Rate Limits
  slug: envoapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: envoapi-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: envoapi-com-rules
scopes:
- name: Envoapi Com Scopes
  scope_count: 0
  slug: envoapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.3
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 41.7
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 41.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/envoapi-com/envoapi-com-2026-11-03T131551.png
security:
- kind: authentication
  name: Envoapi Com Authentication
  slug: envoapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Envoapi Com Domain Security
  slug: envoapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: envoapi-com
tags:
- Data Enrichment
- B2B
- LinkedIn
- Email Verification
website: https://envoapi.com/
---
