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
- description: Capture6 provides water-positive carbon removal services; API documentation is listed under Technology.
  name: Capture6 API
  slug: capture6-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capture6/refs/heads/main/hosts/capture6-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capture6-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capture6/refs/heads/main/security/capture6-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capture6-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capture6.com
- group: docs
  title: ''
  type: Documentation
  url: https://capture6.com/technology/
- group: start
  title: ''
  type: GettingStarted
  url: https://capture6.com/get-in-touch/
- group: company
  title: ''
  type: Careers
  url: https://capture6.com/careers/
- group: company
  title: ''
  type: News
  url: https://capture6.com/news-page/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capture6.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capture6.com/terms-of-use/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://capture6.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Capture6 is a water-positive carbon removal company based in California and New Zealand. It turns saltwater into fresh water while capturing atmospheric CO₂, creating fresh water and valuable by‑products. The integrated system reduces brine disposal costs, generates commercial value, and supports climate resilience for industrial partners. Capture6 partners with governments and corporations to deliver scalable water security and carbon removal solutions.
layout: provider
modified: '2026-10-06'
name: Capture6
nav: Providers
network: true
overview: 'Capture6 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Water, CarbonRemoval, Climate Tech, Cleantech, and Company.


  Capture6''s developer surface includes documentation, getting-started guide, product news, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capture6 Domain Security
  slug: capture6-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capture6
tags:
- Water
- CarbonRemoval
- Climate Tech
- Cleantech
- Company
website: https://capture6.com
---
