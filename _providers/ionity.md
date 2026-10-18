---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides access to charging station data, pricing and transaction services.
  name: IONITY API
  slug: ionity-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ionity/refs/heads/main/hosts/ionity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ionity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ionity/refs/heads/main/vendors/ionity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ionity-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.ionity.eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ionity.eu/policies/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ionity.eu/hr/price
- group: company
  title: ''
  type: Newsroom
  url: https://www.ionity.eu/ionity/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ionity/refs/heads/main/security/ionity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ionity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ionity.eu
coverage:
  checked: '2026-10-13'
  detail: The developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.ionity.eu/hr/price
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: IONITY operates a high-power electric vehicle (EV) charging network across Europe, offering fast, reliable charging stations in 24 countries. The company focuses on seamless mobility, providing drivers with subscription plans, fleet solutions, and a mobile app to locate and pay for charging. IONITY aims to accelerate the transition to electric transportation by expanding its infrastructure and delivering transparent pricing.
image: https://cdn.prod.website-files.com/66e197644ead7b648dbae27d/673c3eb7bac9f80df03d2969_IONITY_OG_IMG.jpg
layout: provider
modified: '2026-10-13'
name: IONITY
nav: Providers
network: true
overview: 'IONITY is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EVCharging, Infrastructure, Europe, and Mobility.


  IONITY''s developer surface includes support, pricing, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ionity Domain Security
  slug: ionity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ionity
tags:
- Company
- EVCharging
- Infrastructure
- Europe
- Mobility
website: https://ionity.eu
---
