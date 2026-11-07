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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/blackcarservice-co/llms/blackcarservice-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackcarservice-co-llms.txt
- group: other
  href: https://artifacts.apis.io/blackcarservice-co/hosts/blackcarservice-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackcarservice-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/blackcarservice-co/vendors/blackcarservice-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackcarservice-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackcarservice.co/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackcarservice.co/privacy
- group: auth
  href: https://artifacts.apis.io/blackcarservice-co/security/blackcarservice-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackcarservice-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackcarservice.co/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing the documented API reference URL.
  evidence:
  - status: 405
    url: https://www.blackcarservice.co/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Black Car Service provides private black car transportation in San Francisco and the Bay Area, offering airport transfers, hourly chauffeur services, and Napa trips. The company emphasizes personalized service, safety, and flexibility, allowing customers to specify passenger counts, luggage, and special requests. Their online platform enables route quotes and bookings, with support in English and Spanish.
image: https://www.blackcarservice.co/opengraph-image
layout: provider
modified: '2026-11-02'
name: Black Car Service
nav: Providers
network: true
overview: Black Car Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chauffeur, Airport Transfer, Hourly Service, Napa Transportation, and Corporate Travel.
random_paper: 3
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
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
  name: Blackcarservice Co Domain Security
  slug: blackcarservice-co-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blackcarservice-co
tags:
- Chauffeur
- Airport Transfer
- Hourly Service
- Napa Transportation
- Corporate Travel
- Private Car Service
website: https://blackcarservice.co/
---
