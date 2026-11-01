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
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Aazzur Agentic Access
  operation_count: 1
  slug: aazzur-agentic-access
  summary_line: 1 operation · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Embedded finance API providing accounts, cards, transfers, and other banking services.
  name: AAZZUR API
  slug: aazzur-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/aazzur/agentic-access/aazzur-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aazzur-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aazzur/rules/aazzur-rules.yml
  title: ''
  type: Spectral
  url: rules/aazzur-rules.yml
- group: design
  href: https://artifacts.apis.io/aazzur/vocabulary/aazzur-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aazzur-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/aazzur/authentication/aazzur-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aazzur-authentication.yml
- group: design
  href: https://artifacts.apis.io/aazzur/errors/aazzur-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aazzur-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aazzur/conformance/aazzur-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aazzur-conformance.yml
- group: other
  href: https://artifacts.apis.io/aazzur/hosts/aazzur-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aazzur-hosts.yml
- group: other
  href: https://artifacts.apis.io/aazzur/vendors/aazzur-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aazzur-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.aazzur.com/company/team
- group: company
  title: ''
  type: Website
  url: https://www.aazzur.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aazzur.gitbook.io/api-documentations/
- group: docs
  title: ''
  type: Documentation
  url: https://aazzur.gitbook.io/api-documentations/
- group: docs
  title: ''
  type: APIReference
  url: https://aazzur.gitbook.io/api-documentations/
- group: start
  title: ''
  type: GettingStarted
  url: https://aazzur.gitbook.io/api-documentations/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:contact@aazzur.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aazzur.com/az-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aazzur.com/az-privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aazzur
- group: auth
  href: https://artifacts.apis.io/aazzur/security/aazzur-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aazzur-domain-security.yml
coverage:
  checked: '2026-10-27'
  detail: The public documentation is available as markdown on GitBook, but no owned OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://aazzur.gitbook.io/api-documentations/WeMjPT81RENPps2FDolb/api/endpoints.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: AAZZUR is a Berlin-based embedded finance and Banking-as-a-Service (BaaS) platform that lets enterprises, financial institutions, and startups embed financial services into their own products. It provides modular "Smart Finance Blocks" (pre-configured front-end screens, micro-services, and connections to underlying API providers) alongside its own developer-portal APIs and a smart marketplace of BaaS and fintech partners. Customers can consume the APIs directly, drop in AAZZUR's embeddable front-end components, or launch stand-alone apps and web frontends covering banking, payments, cards, lending, wealth management, and insurance without building the underlying financial infrastructure themselves.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aazzur.png
layout: provider
modified: '2026-07-17'
name: AAZZUR
nav: Providers
network: true
overview: 'AAZZUR is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Embedded Finance, Banking as a Service, Fintech, and Open Banking.


  The AAZZUR catalog on APIs.io includes 1 Spectral governance ruleset.


  AAZZUR''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 14 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AAZZUR API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aazzur-rules
scopes:
- name: Aazzur Scopes
  scope_count: 0
  slug: aazzur-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.9
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 58.9
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 13.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 33.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aazzur/aazzur-2026-07-25T181328.png
security:
- kind: authentication
  name: Aazzur Authentication
  slug: aazzur-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aazzur Domain Security
  slug: aazzur-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aazzur
tags:
- Company
- Embedded Finance
- Banking as a Service
- Fintech
- Open Banking
- Payments
website: https://www.aazzur.com/
---
