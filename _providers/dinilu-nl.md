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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API referenced at the provider's site but no machine-readable contract found.
  name: Dinilu API
  slug: dinilu-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dinilu-nl/llms/dinilu-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-nl-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-nl/well-known/dinilu-nl-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-nl-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-nl/well-known/dinilu-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-nl/hosts/dinilu-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-nl-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dinilu-nl/security/dinilu-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.nl/
- group: operate
  title: ''
  type: Contact
  url: https://dinilu.nl/contact
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found despite API reference page.
  evidence:
  - status: 404
    url: https://dinilu.nl/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dinilu Reclame & Drukwerkproducten is a Dutch B2B supplier offering promotional merchandise, printed materials, and custom branding solutions. They provide online quotations for a wide range of products sourced from China and delivered across Europe, ensuring quality control, transport, and door‑to‑door delivery. The company emphasizes fast cost and lead‑time calculations for personalized promotional items.
image: https://cdn.dinilu.nl/art/dinilu-1200x1200.png
layout: provider
modified: '2026-11-05'
name: Dinilu
nav: Providers
network: true
overview: Dinilu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Promotional, Printing, Merchandise, and B2B.
random_paper: 20
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dinilu Nl Domain Security
  slug: dinilu-nl-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-nl
tags:
- Company
- Promotional
- Printing
- Merchandise
- B2B
website: https://dinilu.nl/
---
