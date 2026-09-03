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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hithium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hithium.com/
- group: operate
  title: ''
  type: Support
  url: https://www.hithium.com/support/services.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hithium.com/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.hithium.com/about/IndustryNews.html
- group: auth
  title: ''
  type: Security
  url: https://www.hithium.com/support/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.hithium.com/about/anti_corruption.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hithium-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hithium-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hithium-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/hithium-plans-pricing.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/hithium-stock
coverage:
  detail: 'HiTHIUM sells battery cells and containerised storage systems, not software: there is no developer surface anywhere on its estate - eleven candidate API/docs subdomains of hithium.com fail to resolve, every /.well-known/* path 404s on all three live hosts, the HeroEE brand site answers 200 with the same Next.js HTML shell for /openapi.json and /llms.txt (a soft-200, not a document), there is no GitHub organisation, and the only integration documentation that exists - the Modbus/CAN datasheets and manuals - sits behind the download centre''s "Please login to download this datasheet" account gate.'
  evidence:
  - status: 404
    url: https://www.hithium.com/openapi.json
  - status: 404
    url: https://www.hithium.com/llms.txt
  - status: 404
    url: https://www.hithium.com/.well-known/agent-card.json
  - status: 404
    url: https://www.hithium.com/.well-known/api-catalog
  - status: 404
    url: https://en.hithium.com/.well-known/security.txt
  - status: 200
    url: https://www.hero-ee.com/openapi.json
  - status: 404
    url: https://www.hero-ee.com/.well-known/agent-card.json
  - status: 200
    url: https://www.hithium.com/support/download_center.html
  - status: 200
    url: https://www.hithium.com/support/security.html
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: HiTHIUM (Xiamen Hithium Energy Storage Technology Co., Ltd.) is a Chinese energy storage company founded in 2019 that designs and manufactures lithium iron phosphate (LFP) cells, modules and complete battery energy storage systems (BESS) for utility-scale, commercial and industrial, and residential applications. The product line runs from large-format prismatic ESS cells through liquid-cooled multi-megawatt-hour container systems to the HeroEE residential and portable range marketed at hero-ee.com. Company material reports roughly 8,000 staff, more than 1,100 R&D engineers and over 3,900 patents. Product pages publish named certifications including UL 1973, UL 9540, UL 9540A, NFPA 855, IEC 62619, IEC 62477, IEC 63056, IEC 61000 and UN 38.3. HiTHIUM operates a Product Security Incident Response Team (PSIRT) running an IEC 62443-aligned vulnerability management process, and publishes numbered cybersecurity bulletins with CVE references and remediation guidance at hithium.com/support/security.html.
  HiTHIUM publishes no developer portal, no API reference, no OpenAPI, AsyncAPI, GraphQL or Postman contract, no SDKs, no CLI, no webhook catalog and no MCP or A2A agent surface; third-party integration happens over Modbus/CAN interfaces described in datasheets and manuals that sit behind the download-center account gate, and the HeroEE consumer app's backend is undocumented.
image: https://www.hithium.com/favicon.ico
layout: provider
modified: '2026-08-22'
name: Hithium
nav: Providers
network: true
overview: 'Hithium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy Storage, Battery, Lithium Iron Phosphate, and Renewable Energy.


  Hithium''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Hithium Plans Pricing
  plan_count: 0
  slug: hithium-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hithium/refs/heads/main/screenshots/hithium-2026-09-02T145801.png
security:
- kind: domain-security
  name: Hithium Domain Security
  slug: hithium-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hithium Vulnerability Disclosure
  slug: hithium-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hithium
tags:
- Company
- Energy Storage
- Battery
- Lithium Iron Phosphate
- Renewable Energy
- Utilities
- Manufacturing
- Hardware
- Industrial Control Systems
website: https://www.hithium.com/
---
