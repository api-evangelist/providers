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
- group: company
  title: ''
  type: Website
  url: http://www.5lmeet.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/5lmeet-stock
- group: auth
  title: ''
  type: DomainSecurity
  url: security/5lmeet-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: '5Lmeet is a Beijing co-working and co-living property operator whose only shipped software is an end-user iPad visitor-management app for its own front desks — there is no developer portal, no API, and no machine-readable contract anywhere: all 22 discovery and /.well-known/ paths returned genuine IIS 404s on www.5lmeet.com (a negative-control path 404''d too, so the host does not echo), and api.5lmeet.com resolves to 101.201.52.28 but accepts no connection on port 80 or 443.'
  evidence:
  - status: 200
    url: http://www.5lmeet.com/
  - status: 404
    url: http://www.5lmeet.com/openapi.json
  - status: 404
    url: http://www.5lmeet.com/.well-known/security.txt
  - status: 404
    url: http://www.5lmeet.com/.well-known/agent-card.json
  - status: 404
    url: http://www.5lmeet.com/llms.txt
  - status: 404
    url: http://5lmeet.com/apis.json
  - status: 0
    url: http://api.5lmeet.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '5Lmeet (Chinese brand 共享际, operated by 优享创智 / UR Community) is a Beijing-based urban space operator founded in December 2015 by Dr. Mao Daqing, the former vice-chairman of China Vanke and founder of Ucommune. It runs an "urban renewal and spatial reconstruction" model that blends co-working, co-living, food and beverage, retail, fitness and cultural programming into single mixed-use compounds — the name stands for livable, linked, liberal, lively and landscape. Its Dongsi compound in Beijing pairs a basement co-working floor with a cafe and bakery, a gym, the Hatchery food incubator, the Unread bookstore, a 24-hour convenience store, residential units and a rooftop garden. The company raised roughly RMB 400 million in October 2016 and a USD 14.55 million Series B in early 2017 led by GIC, Singapore''s sovereign wealth fund, alongside Kaifeng Culture Tourism Investment Group, and is valued in the secondary market rather than publicly listed. 5Lmeet is a real-estate and hospitality
  operator, not a software vendor: the only software it has published is an end-user iPad visitor-management app for its own front desks, and it operates no developer program, public API, SDK or machine-readable contract of any kind.'
layout: provider
modified: '2026-09-05'
name: 5Lmeet
nav: Providers
network: true
overview: 5Lmeet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Coworking, Co-Living, and Workspace.
random_paper: 0
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 5Lmeet Domain Security
  slug: 5lmeet-domain-security
  summary_line: no transport/DNS hardening detected
slug: 5lmeet
tags:
- Company
- Real Estate
- Coworking
- Co-Living
- Workspace
- Property Technology
- Hospitality
- Urban Development
- China
website: http://www.5lmeet.com/
---
