---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/micron/refs/heads/main/well-known/micron-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/micron-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/micron/refs/heads/main/hosts/micron-hosts.yml
  title: ''
  type: Hosts
  url: hosts/micron-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/micron/refs/heads/main/vendors/micron-vendors.yml
  title: ''
  type: Vendors
  url: vendors/micron-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.micron.com/legal/terms-of-sale
- group: start
  title: ''
  type: SignUp
  url: https://www.micron.com/about/company/suppliers/registered-suppliers
- group: auth
  title: ''
  type: Security
  url: https://www.micron.com/about/company/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.micron.com/Privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.micron.com/about/press
- group: other
  title: ''
  type: Leadership
  url: https://www.micron.com/about/company/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/micron/refs/heads/main/security/micron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/micron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.micron.com
- group: company
  title: ''
  type: Blog
  url: https://www.micron.com/about/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.micron.com/products
- group: operate
  title: ''
  type: Support
  url: https://www.micron.com/sales-support/design-tools
- group: company
  title: ''
  type: Careers
  url: https://www.micron.com/about/careers
- group: company
  title: ''
  type: Investors
  url: https://investors.micron.com/
coverage:
  checked: '2026-10-13'
  detail: Micron Technology's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.micron.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Micron Technology is a global leader in memory and storage solutions, designing and manufacturing DRAM, NAND, and SSD products for a wide range of markets including data centers, mobile devices, automotive, and industrial applications. The company provides extensive technical documentation, design tools, and developer resources to support integration of its memory technologies into customer products.
image: https://www.micron.com/content/dam/micron/global/favicon/og-image.png
layout: provider
modified: '2026-10-13'
name: Micron Technology
nav: Providers
network: true
overview: 'Micron Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Memory, Storage, Semiconductors, and Technology.


  Micron Technology''s developer surface includes signup flow, engineering blog, documentation, support, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Micron Domain Security
  slug: micron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: micron
tags:
- Company
- Memory
- Storage
- Semiconductors
- Technology
- Hardware
website: https://www.micron.com
---
