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
- description: API for Virtual Assistant International services (no public machine‑readable contract found)
  name: Virtual Assistant International API
  slug: virtual-assistant-international-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/virtualassistantinternational-com/llms/virtualassistantinternational-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/virtualassistantinternational-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/virtualassistantinternational-com/well-known/virtualassistantinternational-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/virtualassistantinternational-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/virtualassistantinternational-com/hosts/virtualassistantinternational-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/virtualassistantinternational-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/virtualassistantinternational-com/vendors/virtualassistantinternational-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/virtualassistantinternational-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtualassistantinternational.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.virtualassistantinternational.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtualassistantinternational.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://support.virtualassistantinternational.com/hc/documentation/articles/pricing-and-billing
- group: docs
  title: ''
  type: Documentation
  url: https://support.virtualassistantinternational.com/hc/documentation/en
- group: start
  title: ''
  type: GettingStarted
  url: https://support.virtualassistantinternational.com/hc/documentation/articles/1786097787-how-can-i-make-onboarding-easier
- group: auth
  href: https://artifacts.apis.io/virtualassistantinternational-com/security/virtualassistantinternational-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virtualassistantinternational-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://virtualassistantinternational.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are public but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://support.virtualassistantinternational.com/hc/documentation/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: VA International trains virtual assistants and connects graduates with employers directly. Founded in 2017 and based in the Netherlands, the company operates across 50+ countries, offering AI‑powered virtual assistant training, placement, and management services for remote workforces.
image: https://bxcgzcibtpvvoybtrbms.supabase.co/storage/v1/object/public/company-logos/DO-NOT-DELETE/vai-favicon.png
layout: provider
modified: '2026-10-30'
name: virtualassistantinternational-com
nav: Providers
network: true
overview: 'virtualassistantinternational-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Virtual Assistant, Remote Work, and Netherlands.


  virtualassistantinternational-com''s developer surface includes support, pricing, documentation, getting-started guide, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/virtualassistantinternational-com/virtualassistantinternational-com-2026-11-03T145832.png
security:
- kind: domain-security
  name: Virtualassistantinternational Com Domain Security
  slug: virtualassistantinternational-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virtualassistantinternational-com
tags:
- Company
- Artificial Intelligence
- Virtual Assistant
- Remote Work
- Netherlands
website: https://virtualassistantinternational.com/
---
