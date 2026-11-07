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
- description: Provides access to Blast Radius AI data and analysis.
  name: Blast Radius API
  slug: blast-radius-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/blast-radius-ai/hosts/blast-radius-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blast-radius-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/blast-radius-ai/vendors/blast-radius-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blast-radius-ai-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://blast-radius.ai/signup
- group: company
  title: ''
  type: Newsroom
  url: https://blast-radius.ai/news
- group: auth
  href: https://artifacts.apis.io/blast-radius-ai/security/blast-radius-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blast-radius-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blast-radius.ai/
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires POST which is not allowed, and no OpenAPI or other spec is published.
  evidence:
  - status: 405
    url: https://blast-radius.ai/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Blast Radius is a living investment memo by Kip McClanahan that tracks the AI capability surge. It publishes a weekly analysis of the five forces reshaping AI, covering frontier models, enterprise readiness, agents, harnesses, open‑weight vs owned stacks, economics and capital, providing evidence‑based insights for investors and technologists.
image: https://blast-radius.ai/og-blast-radius.jpg
layout: provider
modified: '2026-11-02'
name: Blast Radius
nav: Providers
network: true
overview: 'Blast Radius is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Investment, Memo, and Weekly.


  Blast Radius'' developer surface includes signup flow and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blast Radius Ai Domain Security
  slug: blast-radius-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blast-radius-ai
tags:
- Company
- Artificial Intelligence
- Investment
- Memo
- Weekly
- Analysis
website: https://blast-radius.ai/
---
