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
    agentic_commerce: self
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
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Dubai Table venue listings, availability and bookings.
  name: Dubai Table API
  slug: dubai-table-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dubaitable-com/llms/dubaitable-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dubaitable-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dubaitable-com/well-known/dubaitable-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dubaitable-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dubaitable-com/hosts/dubaitable-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dubaitable-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dubaitable-com/vendors/dubaitable-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dubaitable-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dubaitable-com/security/dubaitable-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dubaitable-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dubaitable.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dubaitable.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dubaitable.com/privacy
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found despite probing known hosts.
  evidence:
  - status: 404
    url: https://dubaitable.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Dubai Table is a platform that aggregates Dubai’s luxury dinner parties, beach clubs, and nightlife events, allowing users to compare options, plan evenings, and request table reservations confirmed via WhatsApp. Operated by The Rize Group FZ‑LLE, it serves the Dubai market with multilingual support and a comprehensive event calendar.
image: https://dubaitable.com/assets/hero-poster.jpg
layout: provider
modified: '2026-11-06'
name: Dubai Table
nav: Providers
network: true
overview: Dubai Table is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Event, Hospitality, Dubai, and Nightlife.
random_paper: 9
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
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
  name: Dubaitable Com Domain Security
  slug: dubaitable-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dubaitable-com
tags:
- Company
- Event
- Hospitality
- Dubai
- Nightlife
website: https://dubaitable.com/
---
