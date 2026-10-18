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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conapto/refs/heads/main/hosts/conapto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conapto-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.conapto.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conapto.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.conapto.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conapto/refs/heads/main/security/conapto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conapto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.conapto.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.conapto.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Conapto provides scalable, secure and sustainable data center colocation and cloud connectivity services. Based in Sweden, Conapto offers flexible colocation solutions, interconnect, cloud‑connect, and sale‑leaseback options for enterprises seeking reliable infrastructure with low carbon footprint. The company emphasizes climate‑responsible operations, high availability, and competitive electricity costs, serving customers across Europe and globally.
image: https://www.conapto.com/wp-content/uploads/2018/09/slide_front_1.jpg
layout: provider
modified: '2026-10-15'
name: Conapto
nav: Providers
network: true
overview: 'Conapto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DataCenter, Colocation, CloudConnectivity, and Sustainability.


  Conapto''s developer surface includes support and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
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
  name: Conapto Domain Security
  slug: conapto-domain-security
  summary_line: TLSv1.3 · HSTS
slug: conapto
tags:
- Company
- DataCenter
- Colocation
- CloudConnectivity
- Sustainability
website: https://www.conapto.com/
---
