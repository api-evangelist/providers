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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3d-glass-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.3dgsinc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.3dgsinc.com/blogs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3dgsinc.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.3dgsinc.com/supplier-terms-and-conditions
- group: operate
  title: ''
  type: ContactUs
  url: https://www.3dgsinc.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3dgsinc
coverage:
  checked: '2026-08-05'
  detail: 3DGS is a glass-substrate semiconductor foundry whose only "design enablement" surface is an EDA process design kit handed off to the AWR software group — the site has no developer, API or documentation section at all, and every spec and .well-known discovery path on 3dgsinc.com returns the Squarespace 404.
  evidence:
  - status: 404
    url: https://3dgsinc.com/openapi.json
  - status: 404
    url: https://3dgsinc.com/.well-known/api-catalog
  - status: 404
    url: https://3dgsinc.com/.well-known/agent-card.json
  - status: 404
    url: https://3dgsinc.com/llms.txt
  - status: 200
    url: https://www.3dgsinc.com/process-design-kit
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 3D Glass Solutions (3DGS) is a US-based pure-play glass foundry in Albuquerque, New Mexico that manufactures photo-definable glass-ceramic substrates for advanced semiconductor packaging. Its patented APEX Glass material supports through-glass vias (TGV), high-density interconnect, integrated passive devices, RF substrates, micro-cavities and 3D heterogeneous integration for wireless communications, aerospace and defense, photonics, HPC/AI and sensor markets. The company sells wafer processing, custom fabrication and design-enablement services — including process design kits (PDKs) delivered through EDA partners such as the AWR software group — rather than software, and publishes no public API, SDK, developer portal or machine-readable specification.
image: http://static1.squarespace.com/static/65e8b2455ebce721208a3f82/t/66160e433996332e807c5c47/1712721475580/Final+1+%281%29.png?format=1500w
layout: provider
modified: '2026-08-05'
name: 3D Glass Solutions
nav: Providers
network: true
overview: '3D Glass Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductors, Advanced Packaging, Glass Substrates, RF Components, and Photonics.


  3D Glass Solutions'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/3d-glass-solutions/refs/heads/main/screenshots/3d-glass-solutions-2026-08-07T160700.png
security:
- kind: domain-security
  name: 3D Glass Solutions Domain Security
  slug: 3d-glass-solutions-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 3d-glass-solutions
tags:
- Semiconductors
- Advanced Packaging
- Glass Substrates
- RF Components
- Photonics
- Manufacturing
- Hardware
- Company
website: https://www.3dgsinc.com/
---
