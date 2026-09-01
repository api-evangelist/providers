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
  url: security/empower-semiconductor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.empowersemi.com/
- group: company
  title: ''
  type: About
  url: https://www.empowersemi.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://www.empowersemi.com/our-products/
- group: company
  title: ''
  type: Blog
  url: https://www.empowersemi.com/category/press-release/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.empowersemi.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.empowersemi.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.empowersemi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.empowersemi.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/empower-semiconductor-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Empower Semiconductor sells silicon — integrated voltage regulators, silicon capacitors and vertical power-delivery hardware, now as an Analog Devices company — and its entire public presence is a 16-page WordPress marketing site with no developer, docs, or reference section; the only design collateral it publishes sits behind a WordPress password prompt at /design-resources/, and even the CMS REST API at /wp-json/ is deliberately closed to unauthenticated callers.
  evidence:
  - status: 404
    url: https://www.empowersemi.com/developers
  - status: 404
    url: https://www.empowersemi.com/openapi.json
  - status: 404
    url: https://www.empowersemi.com/.well-known/api-catalog
  - status: 404
    url: https://www.empowersemi.com/.well-known/agent-card.json
  - status: 200
    url: https://www.empowersemi.com/design-resources/
  - status: 401
    url: https://www.empowersemi.com/wp-json/
  - status: 200
    url: https://www.empowersemi.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Empower Semiconductor is a fabless power-semiconductor company founded in 2014 and headquartered in San Jose, California, with an R&D office in Munich. It designs integrated voltage regulators (IVRs), silicon capacitors (ECAP) and vertical power-delivery platforms for AI, high-performance computing and embedded systems, built on its FinFast architecture combining FinFET-based design, advanced packaging, advanced magnetics and integrated silicon capacitors. Its Crescendo platform targets kilowatt-class vertical power delivery for AI and HPC processors and its Forte family delivers multi-domain integrated regulation up to 25W. Analog Devices completed its acquisition of Empower Semiconductor on 7 July 2026. Empower ships silicon, not software: it publishes no developer portal, no public API, and no machine-readable specification of any kind.'
image: https://www.empowersemi.com/wp-content/uploads/2025/09/EMPR-Crescendo-Hero-Image-v1-980x693-1.webp
layout: provider
modified: '2026-08-12'
name: Empower Semiconductor
nav: Providers
network: true
overview: 'Empower Semiconductor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Power Management, and Integrated Voltage Regulators.


  Empower Semiconductor''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Empower Semiconductor Domain Security
  slug: empower-semiconductor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: empower-semiconductor
tags:
- Company
- Semiconductors
- Hardware
- Power Management
- Integrated Voltage Regulators
- Silicon Capacitors
- Artificial Intelligence
- High Performance Computing
- Data Centers
- Electronics
website: https://www.empowersemi.com/
---
