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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bonus-homes/refs/heads/main/llms/bonus-homes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bonus-homes-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonus-homes/refs/heads/main/hosts/bonus-homes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonus-homes-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonus-homes/refs/heads/main/vendors/bonus-homes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonus-homes-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bonushomes.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bonushomes.com/media/buybox-wallpaper
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bonushomes.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bonushomes.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonus-homes/refs/heads/main/security/bonus-homes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonus-homes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bonushomes.com/
coverage:
  checked: '2026-10-02'
  detail: The Bonus Homes website provides only HTML pages with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.bonushomes.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bonus Homes offers a Home Appreciation Partnership (HAP) that lets homeowners unlock cash equity quickly, often within two weeks, while retaining a share of future home appreciation. By converting homes into rental properties and handling mortgage payments, insurance, and maintenance, Bonus Homes provides a faster, less stressful alternative to traditional home sales, targeting homeowners seeking liquidity and long‑term wealth building.
image: https://cdn.prod.website-files.com/67058e3c0a92896313156264/67a541b754c726a9380a47d0_Home.avif
layout: provider
modified: '2026-10-02'
name: Bonus Homes
nav: Providers
network: true
overview: 'Bonus Homes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Fintech, Home Equity, and Homeownership.


  Bonus Homes'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.3
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
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonus Homes Domain Security
  slug: bonus-homes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonus-homes
tags:
- Company
- Real Estate
- Fintech
- Home Equity
- Homeownership
website: https://www.bonushomes.com/
---
