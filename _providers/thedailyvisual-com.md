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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to JSON datasets listed at the data index.
  name: The Daily Visual Data API
  slug: the-daily-visual-data-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/thedailyvisual-com/llms/thedailyvisual-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thedailyvisual-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/thedailyvisual-com/well-known/thedailyvisual-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thedailyvisual-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/thedailyvisual-com/hosts/thedailyvisual-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thedailyvisual-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/thedailyvisual-com/vendors/thedailyvisual-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thedailyvisual-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/thedailyvisual-com/security/thedailyvisual-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thedailyvisual-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thedailyvisual.com
- group: docs
  title: ''
  type: APIReference
  url: https://thedailyvisual.com/data/index.json
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.thedailyvisual.com/openapi.json
  - status: 404
    url: https://thedailyvisual.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The Daily Visual creates data-driven visual stories about the world, covering topics such as climate, food, markets, energy, money, economy, health, and work. They publish interactive charts and accompanying JSON datasets that are openly accessible via CORS, allowing developers to integrate the data into applications and analyses. The site offers a rich collection of datasets behind each chart, with clear provenance, licensing, and regular updates.
image: https://thedailyvisual.com/og-default.png
layout: provider
modified: '2026-10-28'
name: The Daily Visual
nav: Providers
network: true
overview: 'The Daily Visual is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Visualization, Climate, and Economics.


  The Daily Visual''s developer surface includes API reference and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 6.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thedailyvisual-com/thedailyvisual-com-2026-11-03T144616.png
security:
- kind: domain-security
  name: Thedailyvisual Com Domain Security
  slug: thedailyvisual-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thedailyvisual-com
tags:
- Company
- Data
- Visualization
- Climate
- Economics
website: https://thedailyvisual.com
---
