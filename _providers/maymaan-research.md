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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maymaan-research-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maymaan.com/
- group: operate
  title: ''
  type: Support
  url: https://maymaan.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://maymaan.com/stories
- group: company
  title: ''
  type: Press
  url: https://maymaan.com/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maymaan.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maymaan.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maymaan-research-llc/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maymaan-research-llms.txt
coverage:
  checked: '2026-08-25'
  detail: MayMaan Research manufactures water-and-bio-alcohol internal combustion engines and generator sets (the AquaStroke A35 and AV2); its entire public site is product marketing plus a quote-request form, and the apex host returns a genuine 404 for /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and every /.well-known/ path, with a control probe confirming it is not a soft-404 catch-all.
  evidence:
  - status: 404
    url: https://maymaan.com/openapi.json
  - status: 404
    url: https://maymaan.com/graphql
  - status: 404
    url: https://maymaan.com/.well-known/agent-card.json
  - status: 404
    url: https://maymaan.com/this-path-should-not-exist-xyz123
  - status: 200
    url: https://maymaan.com/
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'MayMaan Research is a clean-energy engineering company that redesigns the internal combustion engine around its patented AquaStroke platform, a piston engine that runs on a blend of roughly 70% water and 30% bio-alcohol (ethanol or methanol) instead of gasoline or diesel. The company builds modular generator sets and powertrains that scale from a 35 kW unit (A35) through the AV2 to multi-megawatt installations, and it positions them as drop-in replacements for diesel gensets in power generation, EV charging infrastructure, data centers, telecommunications, marine, construction, agriculture, defense and off-grid deployments, with near-zero NOx, SOx, CO2 and particulate output. MayMaan is headquartered in Hollywood, Florida with a European office in Paris, holds engine and fuel-system patents internationally, and raised a $30 million Series A led by WAVE Equity Partners. It is a hardware manufacturer: as of this profile it publishes no public API, developer portal, SDK or machine-readable
  interface of any kind.'
image: https://maymaan.b-cdn.net/assets/frontend/img/footer-logo.webp
layout: provider
modified: '2026-08-25'
name: MayMaan Research
nav: Providers
network: true
overview: 'MayMaan Research is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Clean Energy, Power Generation, and Engines.


  MayMaan Research''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Maymaan Research Domain Security
  slug: maymaan-research-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maymaan-research
tags:
- Company
- Energy
- Clean Energy
- Power Generation
- Engines
- Manufacturing
- Hardware
- Sustainability
- Data Centers
- Automotive
website: https://maymaan.com/
---
