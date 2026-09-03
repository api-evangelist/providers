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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zero-motorcycles-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zero-motorcycles-llms.txt
- group: company
  title: ''
  type: Website
  url: https://zeromotorcycles.com/
- group: other
  title: ''
  type: Company
  url: https://zeromotorcycles.com/company
- group: operate
  title: ''
  type: Support
  url: https://zeromotorcycles.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeromotorcycles.com/zero-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeromotorcycles.com/zero-privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/zero-motorcycles_stock/
coverage:
  checked: '2026-08-05'
  detail: Zero ships a real connected-vehicle stack — the Cypher OS, the NextGen app and the Cypher Store paid-upgrade backend at api-cypherstore.zeromotorcycles.com — but that host answers every path, including a nonsense control path, with the same 351-byte "Welcome to Zeromotor" HTML page, and a 4,100-URL sitemap contains no developer, API or integration page anywhere.
  evidence:
  - status: 200
    url: https://api-cypherstore.zeromotorcycles.com/openapi.json
  - status: 200
    url: https://api-cypherstore.zeromotorcycles.com/zzz-control-nonsense-9f3
  - status: 404
    url: https://zeromotorcycles.com/developers
  - status: 404
    url: https://zeromotorcycles.com/.well-known/agent-card.json
  - status: 404
    url: https://zeromotorcycles.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Zero Motorcycles is an American manufacturer of electric motorcycles and powertrains, founded in 2006 in Santa Cruz, California. It designs and builds street, dual-sport and off-road electric motorcycles across its S, DS, FX and X lines — including the SR/S, SR/F, DSR/X, FXE and XE — around a proprietary Z-Force electric powertrain and aircraft-grade aluminum frame. Its bikes run the Cypher operating system, which pairs with the Zero Motorcycles NextGen mobile app over Bluetooth and cellular telematics for ride data, remote diagnostics, over-the-air updates and performance customization, and with the Cypher Store, where owners purchase software upgrades that unlock additional power, top speed and features. Zero sells internationally through a dealer network and serves retail, fleet and authority/first-responder segments. Its connected-vehicle platform is consumer-facing only: Zero publishes no public developer program, API documentation, SDKs or machine-readable specification.'
image: https://images.prismic.io/zero-cms-disco/ZyTe6K8jQArT0HpQ_Zero_2025_XBXE_CoastLifestyle-1465-web.jpg?auto=format,compress
layout: provider
modified: '2026-08-05'
name: Zero Motorcycles
nav: Providers
network: true
overview: 'Zero Motorcycles is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Vehicles, Motorcycles, Automotive, and Manufacturing.


  Zero Motorcycles'' developer surface includes support and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.9
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zero-motorcycles/refs/heads/main/screenshots/zero-motorcycles-2026-09-02T171634.png
security:
- kind: domain-security
  name: Zero Motorcycles Domain Security
  slug: zero-motorcycles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zero-motorcycles
tags:
- Company
- Electric Vehicles
- Motorcycles
- Automotive
- Manufacturing
- Connected Vehicles
- Telematics
- Mobility
website: https://zeromotorcycles.com/
---
