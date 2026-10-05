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
api_count: 1
apis:
- description: Boxhub provides an API for managing container inventory and orders.
  name: Boxhub API
  slug: boxhub-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boxhub/refs/heads/main/llms/boxhub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boxhub-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boxhub/refs/heads/main/hosts/boxhub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boxhub-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boxhub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boxhub.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://boxhub.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boxhub/refs/heads/main/security/boxhub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boxhub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boxhub.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/boxhub
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Boxhub provides new and used shipping containers for individuals and businesses, offering a wide range of container types including standard, refrigerated, and specialty containers. With a focus on fast delivery, transparent pricing, and a 30‑day money‑back guarantee, Boxhub serves industries such as agriculture, construction, logistics, and hospitality, helping customers store, move, and ship goods efficiently.
image: https://d3fl8yhsmky5y6.cloudfront.net/boxhub.com/homepage/og-image.jpg
layout: provider
modified: '2026-10-03'
name: Boxhub
nav: Providers
network: true
overview: 'Boxhub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Containers, Logistics, and E-Commerce.


  Boxhub''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boxhub Domain Security
  slug: boxhub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boxhub
tags:
- Company
- Shipping
- Containers
- Logistics
- E-Commerce
website: https://boxhub.com
---
