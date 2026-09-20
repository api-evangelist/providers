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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: A first-party API host AgotoZ operates on its own registrable domain at openapi.agotoz.com, named for an open API surface and serving a valid wildcard *.agotoz.com TLS certificate. It is not reachable
  name: AgotoZ OpenAPI Host (gated)
  slug: agotoz-openapi
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agotoztechnology/refs/heads/main/security/agotoztechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agotoztechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agotoz.com/
- group: company
  title: ''
  type: Blog
  url: https://www.agotoz.com/views/news/list
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agotoz
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agotoztechnology/refs/heads/main/llms/agotoztechnology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agotoztechnology-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agotoztechnology/refs/heads/main/plans/agotoztechnology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agotoztechnology-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agotoztechnology/refs/heads/main/rate-limits/agotoztechnology-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agotoztechnology-rate-limits.yml
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://equityzen.com/company/agotoztechnology
coverage:
  checked: '2026-09-12'
  detail: 'AgotoZ runs a first-party API host on its own domain at openapi.agotoz.com under a valid wildcard *.agotoz.com certificate, but nginx answers every anonymous request to it — /openapi.json, /swagger.json, /v2/api-docs, /graphql, /mcp, every /.well-known/* path and a nonsense control path alike — with the same 571-byte HTTP 403 Forbidden, while the public site carries no developer section at all: its navigation runs home, products, solutions, news and about, and every product page ends at one 免费咨询 trial-request form and the sales address xiaoshou@agotoz.com.'
  evidence:
  - status: 403
    url: http://openapi.agotoz.com/openapi.json
  - status: 403
    url: http://openapi.agotoz.com/.well-known/zzz-control-probe-9182
  - status: 0
    url: https://openapi.agotoz.com/
  - status: 404
    url: https://www.agotoz.com/openapi.json
  - status: 404
    url: https://www.agotoz.com/llms.txt
  - status: 200
    url: https://www.agotoz.com/views/product/allwan
  reason: sales-gate
  state: gated
created: '2026-09-12'
description: AgotoZ Technology (观脉科技 / Agotoz Technology (Beijing) Co., Ltd.) is a Beijing-headquartered network-as-a-service provider, registered in 2016 and in commercial operation since 2017, that builds and operates ALLWAN — a self-built global SD-WAN overlay network the company says reaches more than 70 countries and regions — alongside the Linker and Linker Pro CPE intelligent access gateways, a global integrated CDN, cloud connection and one-stop public cloud services, SASE dynamic secure access, DDoS protection, worldwide data centre and co-location resources, and the Lingyin LinkTo real-time transmission service. Its stack applies layer 2 through layer 7 SD-WAN technology — VxLAN, millisecond-scale global dynamic routing, single- and bilateral TCP/UDP acceleration, efficient data compression and high-performance caching — to low-latency enterprise interconnect and application acceleration for gaming, VR/AR/MR, online education, audio and video conferencing, and internet companies.
  AgotoZ states it holds full MIIT telecommunications licences (A24-1, B11, B12, B13, B14), is a Chinese National High-tech Enterprise, and has served more than 200 global internet companies; it has raised roughly $57M from Legend Capital, SIG China, CICC Capital and NGP Capital, and runs offices in Beijing, Shanghai, Singapore and Hong Kong. The company sells through a trial-request and sales motion and publishes no developer portal, API reference, SDK or machine-readable contract of any kind, though it does operate a credential-gated API host of its own at openapi.agotoz.com.
image: https://static.agotoz.com/images/01home/black-logo.svg
layout: provider
modified: '2026-09-12'
name: AgotoZ Technology
nav: Providers
network: true
overview: 'AgotoZ Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SD-WAN, Network as a Service, Network Acceleration, Enterprise Networking, and CDN.


  AgotoZ Technology''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Agotoztechnology Plans Pricing
  plan_count: 0
  slug: agotoztechnology-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Agotoztechnology Rate Limits
  slug: agotoztechnology-rate-limits
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 4.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agotoztechnology Domain Security
  slug: agotoztechnology-domain-security
  summary_line: TLSv1.2 · DMARC
slug: agotoztechnology
tags:
- SD-WAN
- Network as a Service
- Network Acceleration
- Enterprise Networking
- CDN
- SASE
- DDoS Protection
- Cloud Connectivity
- Data-Center
- Telecommunications
website: https://www.agotoz.com/
---
