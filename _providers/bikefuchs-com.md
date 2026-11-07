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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bikefuchs-com/llms/bikefuchs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bikefuchs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bikefuchs-com/well-known/bikefuchs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bikefuchs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bikefuchs-com/hosts/bikefuchs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bikefuchs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bikefuchs-com/vendors/bikefuchs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bikefuchs-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bikefuchs-com/security/bikefuchs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bikefuchs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bikefuchs.com/
- group: commercial
  title: ''
  type: Legal
  url: https://bikefuchs.com/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bikefuchs.com/datenschutz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bikefuchs.com/nutzungsbedingungen
- group: start
  title: ''
  type: GettingStarted
  url: https://bikefuchs.com/ki
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host or documentation pages.
  evidence:
  - status: 0
    url: https://api.bikefuchs.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bikefuchs offers AI‑driven price comparison across 11 bike‑shop partners, optimizing shopping carts for bicycle parts, components, accessories and apparel. The service calculates the cheapest combination of shops, shows real‑time availability and includes shipping costs, helping cyclists save money and time when ordering bike‑related products.
layout: provider
modified: '2026-11-02'
name: Bikefuchs
nav: Providers
network: true
overview: 'Bikefuchs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, E-Commerce, Price Comparison, Bicycles, and Shopping.


  Bikefuchs'' developer surface includes legal docs, getting-started guide, and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bikefuchs Com Domain Security
  slug: bikefuchs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bikefuchs-com
tags:
- Artificial Intelligence
- E-Commerce
- Price Comparison
- Bicycles
- Shopping
website: https://bikefuchs.com/
---
