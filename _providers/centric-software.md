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
  href: https://raw.githubusercontent.com/api-evangelist/centric-software/refs/heads/main/hosts/centric-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centric-software-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centric-software/refs/heads/main/vendors/centric-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centric-software-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.centricsoftware.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.centricsoftware.com/pricing-optimization
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.centricsoftware.com/WebAccess/home.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.centricsoftware.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centric-software/refs/heads/main/security/centric-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centric-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.centricsoftware.com
- group: company
  title: ''
  type: Blog
  url: https://www.centricsoftware.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centricsoftware.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centricsoftware.com/legal
coverage:
  checked: '2026-10-13'
  detail: Developer portal at https://dev.centricsoftware.com/WebAccess/home.html provides no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://dev.centricsoftware.com/WebAccess/home.html
  - status: 0
    url: https://api.centricsoftware.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Centric Software provides award‑winning product lifecycle management (PLM), planning and pricing solutions. Their platform supports end‑to‑end product development from concept through commercialization, leveraging AI‑driven insights to accelerate time‑to‑market, reduce excess inventory, and improve operating margins. Serving industries such as fashion, food & beverage, outdoor sports, and consumer electronics, Centric Software helps teams collaborate, plan, price, and sell products efficiently while promoting sustainability.
image: https://images.ctfassets.net/32vxorm5v0vi/7bXx9b6XiM3hH8gtGSd1Gj/6993666b31316036efb834c128eb1ce1/og-image.jpg
layout: provider
modified: '2026-10-13'
name: Centric Software
nav: Providers
network: true
overview: 'Centric Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PLM, Planning, Pricing, and Artificial Intelligence.


  Centric Software''s developer surface includes support, pricing, documentation, engineering blog, and 7 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Centric Software Domain Security
  slug: centric-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centric-software
tags:
- PLM
- Planning
- Pricing
- Artificial Intelligence
website: https://www.centricsoftware.com
---
