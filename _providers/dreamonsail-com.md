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
- description: API for Dream On Sail charter service (no public spec discovered)
  name: DreamOnSail API
  slug: dreamonsail-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dreamonsail-com/llms/dreamonsail-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamonsail-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dreamonsail-com/hosts/dreamonsail-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamonsail-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreamonsail-com/vendors/dreamonsail-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamonsail-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dreamonsail.com/privacy/
- group: auth
  href: https://artifacts.apis.io/dreamonsail-com/security/dreamonsail-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamonsail-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamonsail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dreamonsail.com/llms.txt
- group: other
  title: ''
  type: Data
  url: https://dreamonsail.com/data/dream-on.json
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing known hosts.
  evidence:
  - status: 405
    url: https://dreamonsail.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dream On Charter offers luxury crewed catamaran charters in the British Virgin Islands aboard the first flagship Bali 5.8 catamaran. The all‑inclusive service includes a captain, chef, premium open bar, fuel, and a suite of water toys such as sea scooters, wakeboard and water skis. Guests enjoy upscale accommodations for up to eight guests, with bespoke itineraries across Tortola, Virgin Gorda, Norman Island and more.
layout: provider
modified: '2026-11-05'
name: Dream On Charter
nav: Providers
network: true
overview: 'Dream On Charter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Charter, Luxury, Catamaran, BVI, and Travel.


  Dream On Charter''s developer surface includes documentation and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreamonsail Com Domain Security
  slug: dreamonsail-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dreamonsail-com
tags:
- Charter
- Luxury
- Catamaran
- BVI
- Travel
website: https://dreamonsail.com/
---
