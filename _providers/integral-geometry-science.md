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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integral-geometry-science-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.igs-group.com/
- group: operate
  title: ''
  type: Support
  url: https://www.igs-group.com/en/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.igs-group.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.igs-group.com/en/news
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/integral-geometry-science-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/integral-geometry-science-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/integral-geometry-science-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: 'IGS sells microwave-imaging instruments and diagnostic systems, not software: its complete 306-URL sitemap carries no developer, docs, or API path in any of its three locales, and /openapi.json, /api-docs, /llms.txt and every /.well-known/ path return a real 404 on www.igs-group.com.'
  evidence:
  - status: 200
    url: https://www.igs-group.com/sitemap-igs-group-9rjqA-0.xml
  - status: 404
    url: https://www.igs-group.com/openapi.json
  - status: 404
    url: https://www.igs-group.com/.well-known/agent-card.json
  - status: 404
    url: https://www.igs-group.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'Integral Geometry Science Inc. (IGS) is a Kobe University deep-tech spinout founded on 2 April 2012 by Dr. Kenjiro Kimura, who published the first analytical solution to the inverse problem of wave scattering. IGS turns that mathematics into measurement hardware and imaging software that makes the inside of an object visible without cutting it open: microwave mammography for painless, radiation-free breast cancer screening (designated under Japan''s Sakigake scheme), non-destructive current-density imaging for rechargeable battery inspection, walk-through security screening for concealed hazardous materials, and rebar corrosion and fracture inspection for civil infrastructure. The company is headquartered in Kobe, Hyogo, Japan, holds patents across Japan, the United States, China and Europe, and is backed by SBI Investment and Japan''s NEDO deep-tech program. IGS sells instruments and diagnostic systems to hospitals, manufacturers and infrastructure operators; it publishes
  no public developer program, API, or SDK.'
image: https://www.igs-group.com/images/ogp.png
layout: provider
modified: '2026-08-23'
name: Integral Geometry Science
nav: Providers
network: true
overview: 'Integral Geometry Science is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Imaging, Healthcare, and Batteries.


  Integral Geometry Science''s developer surface includes support, engineering blog, and 6 more developer resources.'
plans:
- name: Integral Geometry Science Plans Pricing
  plan_count: 0
  slug: integral-geometry-science-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Integral Geometry Science Rate Limits
  slug: integral-geometry-science-rate-limits
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Integral Geometry Science Domain Security
  slug: integral-geometry-science-domain-security
  summary_line: TLSv1.3 · HSTS
slug: integral-geometry-science
tags:
- Company
- Medical Devices
- Medical Imaging
- Healthcare
- Batteries
- Non-Destructive Testing
- Security Screening
- Infrastructure
- Deep Tech
- Hardware
- Japan
website: https://www.igs-group.com/
---
