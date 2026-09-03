---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperlight-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyperlight-llms.txt
- group: company
  title: ''
  type: Website
  url: https://hyperlightcorp.com/
- group: company
  title: ''
  type: About
  url: https://hyperlightcorp.com/company
- group: other
  title: ''
  type: Applications
  url: https://hyperlightcorp.com/applications
- group: other
  title: ''
  type: Product
  url: https://hyperlightcorp.com/products/imdd-tx-pics
- group: other
  title: ''
  type: Product
  url: https://hyperlightcorp.com/products/dpiq-tx-pics
- group: other
  title: ''
  type: Product
  url: https://hyperlightcorp.com/products/packaged-modulators
- group: other
  title: ''
  type: Custom Development
  url: https://hyperlightcorp.com/custom
- group: other
  title: ''
  type: Patents
  url: https://hyperlightcorp.com/patents
- group: operate
  title: ''
  type: Contact
  url: https://hyperlightcorp.com/contact
- group: company
  title: ''
  type: Careers
  url: https://apply.workable.com/hyperlight/
- group: other
  title: ''
  type: CookiePolicy
  url: https://hyperlightcorp.com/cookie_policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperlight-corporation/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/hyperlight_stock/
coverage:
  checked: '2026-08-22'
  detail: HyperLight makes thin-film lithium niobate photonic chips, not software — hyperlightcorp.com is a nine-page marketing and sales site (company, applications, custom, three product pages, patents, contact, shopping cart) where /openapi.json, /swagger.json, /api-docs, /docs, /graphql and /llms.txt all return a real 404, every /.well-known/* path returns the same 404 page, and api./docs./developer.hyperlightcorp.com do not resolve in DNS; the only "hyperlight" packages on npm, PyPI and crates.io belong to the unrelated hyperlight-dev sandboxing project.
  evidence:
  - status: 200
    url: https://hyperlightcorp.com/
  - status: 404
    url: https://hyperlightcorp.com/openapi.json
  - status: 404
    url: https://hyperlightcorp.com/api-docs
  - status: 404
    url: https://hyperlightcorp.com/graphql
  - status: 404
    url: https://hyperlightcorp.com/llms.txt
  - status: 404
    url: https://hyperlightcorp.com/.well-known/agent-card.json
  - status: 404
    url: https://hyperlightcorp.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'HyperLight Corporation is a Cambridge, Massachusetts photonics company founded by Mian Zhang out of Harvard University that designs and manufactures thin-film lithium niobate (TFLN) photonic integrated circuits. Its patented TFLN Chiplet platform pairs the electro-optic properties of thin-film lithium niobate with CMOS-like, high-volume wafer fabrication to produce IMDD transmitter PICs at up to 448 Gbps per lane, dual-polarization IQ transmitter PICs for 130/200/260 Gbaud coherent links, and packaged standalone modulators with up to 145 GHz bandwidth, aimed at AI and hyperscale data center interconnect, DCI and telecom transport, test and measurement, and emerging quantum and sensing applications. The company manufactures through tier-1 foundry and OSAT partners including UMC and its compound semiconductor subsidiary Wavetek on 6-inch and 8-inch wafers, is ISO 9001:2015 certified as of September 2025, and raised an $80M Series C led by MediaTek with participation from UMC
  Capital, Jabil, Foxconn, EDBI, CDIB-TEN Capital and the Qatar Investment Authority, following a $37M Series B in September 2024. HyperLight is a semiconductor hardware business: its public site covers company, applications, custom development, three product lines, patents, careers and a sales contact, and it publishes no developer program, API, SDK, webhook surface or machine-readable specification of any kind.'
image: https://hyperlightcorp.com/img/logo.webp
layout: provider
modified: '2026-08-22'
name: HyperLight
nav: Providers
network: true
overview: HyperLight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photonics, Integrated Photonics, Semiconductors, and Optical Networking.
random_paper: 17
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperlight/refs/heads/main/screenshots/hyperlight-2026-09-02T145805.png
security:
- kind: domain-security
  name: Hyperlight Domain Security
  slug: hyperlight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hyperlight
tags:
- Company
- Photonics
- Integrated Photonics
- Semiconductors
- Optical Networking
- Data-Center
- Telecommunications
- Hardware
- AI Infrastructure
website: https://hyperlightcorp.com/
---
