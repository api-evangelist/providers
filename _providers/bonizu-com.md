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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Semantic product search and comparison across beauty, personal care, supplements, vitamins, and wellness products. Benelux market focus.
  name: Bonizu Product Intelligence API
  slug: bonizu-product-intelligence-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bonizu-com/llms/bonizu-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bonizu-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bonizu-com/well-known/bonizu-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bonizu-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bonizu-com/hosts/bonizu-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonizu-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bonizu-com/security/bonizu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonizu-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonizu.com/
created: '2026-11-02'
description: Bonizu provides an AI‑powered product intelligence API that enables developers to access comprehensive product data, comparisons, and analytics. The platform offers sandbox access with free tier limits, integrates with various data sources, and presents a modern web interface for exploring APIs, pricing, and integrations.
layout: provider
modified: '2026-11-02'
name: Bonizu
nav: Providers
network: true
overview: Bonizu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Product Data, Software-as-a-Service, and Analytics.
random_paper: 19
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: first-party
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
  name: Bonizu Com Domain Security
  slug: bonizu-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bonizu-com
tags:
- Artificial Intelligence
- Product Data
- Software-as-a-Service
- Analytics
website: https://bonizu.com/
---
