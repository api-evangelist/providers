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
  href: https://raw.githubusercontent.com/api-evangelist/kinnevik/refs/heads/main/hosts/kinnevik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kinnevik-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kinnevik/refs/heads/main/vendors/kinnevik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kinnevik-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kinnevik.com/investor-relations/press-releases/2019/pricing-of-livongos-ipo/
- group: company
  title: ''
  type: Newsroom
  url: https://www.kinnevik.com/media/
- group: other
  title: ''
  type: Leadership
  url: https://www.kinnevik.com/who-we-are/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinnevik/refs/heads/main/security/kinnevik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinnevik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kinnevik.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://kinnevik.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Kinnevik is a Swedish investment company that builds, invests in and scales digital consumer businesses. It focuses on long‑term growth across sectors such as e‑commerce, fintech, health, and media, supporting portfolio companies with capital, expertise, and strategic guidance. The firm operates globally, managing a diversified portfolio of high‑growth ventures and public listings, and is known for its active involvement in shaping innovative business models.
layout: provider
modified: '2026-10-14'
name: Kinnevik
nav: Providers
network: true
overview: 'Kinnevik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investment, Venture, Technology, and Consumer.


  Kinnevik''s developer surface includes pricing and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.5
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
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kinnevik Domain Security
  slug: kinnevik-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kinnevik
tags:
- Company
- Investment
- Venture
- Technology
- Consumer
website: https://kinnevik.com/
---
