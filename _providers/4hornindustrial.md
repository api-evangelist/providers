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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4hornindustrial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4hornind.com/
- group: company
  title: ''
  type: About
  url: https://4hornind.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://4hornind.com/contact-us/
- group: company
  title: ''
  type: News
  url: https://4hornind.com/4-horn-industrial-expands-footprint-with-sulphur-louisiana-location/
- group: company
  title: ''
  type: Careers
  url: https://4hornind.com/careers/
- group: start
  title: ''
  type: CustomerPortal
  url: https://4hindustrial.intemposoftware.com/customerportal/login.show
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/4hornindustrial/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fourhornind
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/4hornindustrial
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4hornindustrial-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 4-Horn Industrial rents and sells industrial equipment out of four Gulf Coast branches; its only web surface is a WordPress/WooCommerce marketing catalog, and both digital services it offers customers are vendor-operated third parties (an Intempo Software rental portal at 4hindustrial.intemposoftware.com and Jack Henry ProfitStars SmartPay for invoices), so there is no 4-Horn API, developer program or machine-readable contract to profile.
  evidence:
  - status: 404
    url: https://4hornind.com/openapi.json
  - status: 404
    url: https://4hornind.com/.well-known/api-catalog
  - status: 404
    url: https://4hornind.com/.well-known/agent-card.json
  - status: 200
    url: https://4hindustrial.intemposoftware.com/customerportal/login.show
  - status: 200
    url: https://4hornind.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '4-Horn Industrial is an industrial equipment rental, sales and contractor supply company headquartered in Nederland, Texas, serving the petrochemical, refinery, pipeline and construction markets across the Gulf Coast from branches in Nederland, Pasadena and Hutto, Texas and Sulphur, Louisiana. It rents and sells manlifts, air compressors, forklifts, compaction and welding equipment, light towers, pneumatic tools and general contractor supplies on a 24/7/365 basis. It is an equipment leasing and distribution business rather than a software company: it publishes no developer program, no public API and no machine-readable API contract. Customer account access is delivered through a third-party rental-management portal (Intempo Software) and payments through Jack Henry ProfitStars SmartPay, both operated by vendors rather than by 4-Horn Industrial itself.'
image: https://4hornind.com/wp-content/uploads/2020/12/4H_Industrial_marked-small-copy.png
layout: provider
modified: '2026-09-05'
name: 4-Horn Industrial
nav: Providers
network: true
overview: '4-Horn Industrial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Equipment Rental, Industrial Equipment, Construction, and Energy.


  4-Horn Industrial''s developer surface includes support, product news, and 9 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Hornindustrial Domain Security
  slug: 4hornindustrial-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 4hornindustrial
tags:
- Company
- Equipment Rental
- Industrial Equipment
- Construction
- Energy
- Oil and Gas
- Logistics
- Texas
website: https://4hornind.com/
---
