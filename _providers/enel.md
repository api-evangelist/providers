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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/enel/refs/heads/main/plans/enel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/enel-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/enel/refs/heads/main/hosts/enel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enel-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/enel/refs/heads/main/vendors/enel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enel-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enel.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.enel.com/media/explore/search-press-releases/press/2016/09/price-set-for-public-tender-offer-that-enel-subsidiary-enersis-americas-will-launch-for-endesa-americas-free-float
- group: company
  title: ''
  type: Newsroom
  url: https://www.enel.com/media/explore/search-news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/enel/refs/heads/main/security/enel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enel.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.enel.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Enel is a multinational energy company and one of the world’s leading integrated electricity and gas operators. It focuses on renewable energy, digital innovation, and sustainability, providing electricity and gas to millions of customers worldwide. Enel operates in over 30 countries, invests heavily in clean energy projects, and drives digital transformation across its services.
layout: provider
modified: '2026-10-13'
name: Enel
nav: Providers
network: true
overview: 'Enel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Renewables, and Technology.


  Enel''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Enel Plans Pricing
  plan_count: 1
  slug: enel-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Enel Domain Security
  slug: enel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enel
tags:
- Company
- Energy
- Utilities
- Renewables
- Technology
- Italy
website: https://www.enel.com
---
