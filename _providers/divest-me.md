---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DivestMe provides a private‑position acquisition service accessed via its web interface. No public machine‑readable API contract was found; only web guides are available.
  name: DivestMe API
  slug: divestme-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/divest-me/llms/divest-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/divest-me-llms.txt
- group: other
  href: https://artifacts.apis.io/divest-me/hosts/divest-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/divest-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/divest-me/vendors/divest-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/divest-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.divest.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.divest.me/privacy
- group: start
  title: ''
  type: Login
  url: https://www.divest.me/login
- group: auth
  href: https://artifacts.apis.io/divest-me/security/divest-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divest-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://divest.me/
- group: docs
  title: ''
  type: Documentation
  url: https://www.divest.me/how-it-works
- group: start
  title: ''
  type: GettingStarted
  url: https://www.divest.me/guides
- group: other
  title: ''
  type: WhitePaper
  url: https://www.divest.me/white-paper
- group: other
  title: ''
  type: Advisors
  url: https://www.divest.me/advisors
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or gRPC spec was discovered despite documentation pages.
  evidence:
  - status: 200
    url: https://www.divest.me/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: DivestMe buys stuck private positions for $1 under a counter‑signed sale agreement. A flat $150 covers the documentation, providing a dated sale your accountant can work with. The service documents a real, counter‑signed sale of a defunct private position, offering Asset Sale Agreements and Certificates of Completion with SHA‑256 integrity hashes. It does not determine tax eligibility or provide legal advice, leaving those decisions to the holder and their advisors.
layout: provider
modified: '2026-11-06'
name: DivestMe
nav: Providers
network: true
overview: 'DivestMe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Documentation, Private Equity, and Software-as-a-Service.


  DivestMe''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Divest Me Domain Security
  slug: divest-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: divest-me
tags:
- Company
- Finance
- Documentation
- Private Equity
- Software-as-a-Service
website: https://divest.me/
---
