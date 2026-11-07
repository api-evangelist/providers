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
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Aavia provides a cycle symptom relief platform with no publicly documented machine‑readable API. The website is a Shopify storefront with no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts discover
  name: Aavia API
  slug: aavia-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aavia/well-known/aavia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aavia-well-known.yml
- group: other
  href: https://artifacts.apis.io/aavia/hosts/aavia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aavia-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aavia/security/aavia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aavia-domain-security.yml
coverage:
  checked: '2026-10-22'
  detail: The provider's website is a Shopify storefront with no publicly available OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://aavia.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Aavia offers a cycle symptom relief platform that helps users track, learn, and understand their hormones to alleviate menstrual cycle symptoms. The service provides personalized insights, community support, and a marketplace for related products. It emphasizes privacy, offers a blog, and integrates with mobile apps on iOS and Android. The company positions itself as a comprehensive cycle planner and tracker, aiming to improve women's health and wellbeing throughout their menstrual cycle.
image: https://aavia.io/logo.png
layout: provider
modified: '2026-10-21'
name: Aavia
nav: Providers
network: true
overview: Aavia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Women's Health, Cycle Tracking, Wellness, and Mobile App.
random_paper: 10
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aavia Domain Security
  slug: aavia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aavia
tags:
- Health
- Women's Health
- Cycle Tracking
- Wellness
- Mobile App
---
