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
- description: Swedish payment clearing house API (no public documentation found).
  name: Bankgirot API
  slug: bankgirot-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bankgirot/hosts/bankgirot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankgirot-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://nyhetsrum.bankgirot.se/posts/news/bankgirot-vinnare-i-tech-excellence-awards
- group: auth
  href: https://artifacts.apis.io/bankgirot/security/bankgirot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankgirot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankgirot.se/
- group: operate
  title: ''
  type: Support
  url: https://www.bankgirot.se/kundservice/
- group: company
  title: ''
  type: About
  url: https://www.bankgirot.se/om-bankgirot/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on the API host.
  evidence:
  - status: 0
    url: https://api.bankgirot.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Bankgirot is Sweden’s central clearing house for bank payments, operating a nationwide payment infrastructure that connects banks, businesses and public sector entities. It provides services such as BGC Invoice validation, automated payroll, direct debits, and electronic invoicing, supporting both private and corporate customers. The organization focuses on modernising payment flows, ensuring security, and offering APIs for integration with banking systems and third‑party providers.
image: https://www.bankgirot.se/globalassets/bilder/bankgirot_open_graph.jpg
layout: provider
modified: '2026-10-15'
name: Bankgirot
nav: Providers
network: true
overview: 'Bankgirot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Banking, and Sweden.


  Bankgirot''s developer surface includes support and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 3.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bankgirot/bankgirot-2026-11-03T121540.png
security:
- kind: domain-security
  name: Bankgirot Domain Security
  slug: bankgirot-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: bankgirot
tags:
- Company
- Payments
- Banking
- Sweden
website: https://bankgirot.se/
---
