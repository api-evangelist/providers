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
- group: company
  title: ''
  type: Website
  url: https://www.ohmium.com/
- group: company
  title: ''
  type: About
  url: https://www.ohmium.com/about-ohmium
- group: other
  title: ''
  type: Products
  url: https://www.ohmium.com/products
- group: company
  title: ''
  type: Blog
  url: https://www.ohmium.com/blog
- group: operate
  title: ''
  type: PressReleases
  url: https://www.ohmium.com/press-release
- group: other
  title: ''
  type: Resources
  url: https://www.ohmium.com/resources
- group: operate
  title: ''
  type: Support
  url: https://help.ohmium.com/support/home
- group: operate
  title: ''
  type: Contact
  url: https://www.ohmium.com/contact
- group: company
  title: ''
  type: Careers
  url: https://ohmium.wd12.myworkdayjobs.com/Ohmium_Careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ohmium.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ohmium.com/terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ohmium
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ohmiuminc
- group: other
  title: ''
  type: CompanyProfile
  url: https://forgeglobal.com/ohmium_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ohmium-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ohmium-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Ohmium manufactures PEM electrolyzer hardware and publishes no developer program at all; the only software on its domains is third-party SaaS on custom subdomains (Canary Labs Axiom at canary.ohmium.com, Freshworks at workspace.ohmium.com, Freshdesk at help.ohmium.com) plus an Azure Static Web App lead-time tool whose /api/* routes answer 401.
  evidence:
  - status: 404
    url: https://www.ohmium.com/openapi.json
  - status: 404
    url: https://www.ohmium.com/.well-known/api-catalog
  - status: 404
    url: https://www.ohmium.com/llms.txt
  - status: 401
    url: https://leadtime.ohmium.com/api/swagger.json
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Ohmium International designs, manufactures and deploys modular, vertically-stackable proton exchange membrane (PEM) electrolyzer systems for cost-competitive green hydrogen production. Its Lotus PEM electrolyzer platform integrates power electronics, water treatment and controls into skid-mounted modules for industrial, energy and mobility customers, and is paired with EPC and remote monitoring and maintenance (RM&M) services. Ohmium is a hardware and clean-energy engineering company: it publishes no public developer program, no API reference and no machine-readable specification, and its customer-facing monitoring and service portals are third-party SaaS products hosted on Ohmium subdomains behind login.'
image: https://cdn.prod.website-files.com/62727ad5ed2dca1929e23851/62727e583c4685117faeab2a_ohmium-webclip.png
layout: provider
modified: '2026-08-04'
name: Ohmium
nav: Providers
network: true
overview: 'Ohmium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Green Hydrogen, Hydrogen, Electrolyzers, and Clean Energy.


  Ohmium''s developer surface includes engineering blog, support, YouTube channel, and 13 more developer resources.'
random_paper: 4
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ohmium/refs/heads/main/screenshots/ohmium-2026-08-07T190035.png
security:
- kind: domain-security
  name: Ohmium Domain Security
  slug: ohmium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ohmium
tags:
- Company
- Green Hydrogen
- Hydrogen
- Electrolyzers
- Clean Energy
- Energy
- Manufacturing
- Industrial Equipment
- Decarbonization
website: https://www.ohmium.com/
---
