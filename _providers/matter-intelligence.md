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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.matter.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matter.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matter-intelligence
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matter-intelligence-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matter-intelligence-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matter-intelligence-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Matter Intelligence is a pre-launch ultraspectral sensing company whose entire public surface is a seven-page Webflow marketing site plus an Early Access Typeform; no api./docs./developer. subdomain of matter.com resolves at all and every spec and /.well-known/ path on www.matter.com returns 404.
  evidence:
  - status: 404
    url: https://www.matter.com/openapi.json
  - status: 404
    url: https://www.matter.com/.well-known/api-catalog
  - status: 404
    url: https://www.matter.com/.well-known/agent-card.json
  - status: 200
    url: https://www.matter.com/sitemap.xml
  - status: 200
    url: https://github.com/matter-intelligence
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Matter Intelligence is a California-based remote sensing and physical-AI company founded in 2024 by former NASA Jet Propulsion Laboratory engineers Vishnu Sridhar and Thomas Chrien with former Caltech scientist Nathan Stein. The company builds ultraspectral imaging sensors that capture roughly 2,000 spectral bands from deep ultraviolet through thermal infrared — enough to read the molecular chemistry of a surface rather than only its color — and pairs them with Large Geospatial Models that reason over that data. Its sensors are designed for satellites, aircraft, drones and robots, and its first satellite, EARTH-1, is intended to deliver sub-meter hyperspectral and thermal imaging and to build a global encyclopedia of Earth''s material composition. Target applications named on its site include mining and mineral exploration, agriculture, insurance and risk, infrastructure monitoring, emissions and methane detection, and defense ISR. The company emerged from stealth in October
  2024 with a $12M seed round led by Lowercarbon Capital, with Toyota Ventures, Pear VC, E2MC and Mark Cuban participating. As of this profile it is pre-launch and pre-product: matter.com is a marketing site with an Early Access request form, and Matter Intelligence publishes no public API, developer portal, documentation, SDK or machine-readable contract of any kind.'
image: https://www.matter.com/images/cdn/opengraph.jpg
layout: provider
modified: '2026-08-25'
name: Matter Intelligence
nav: Providers
network: true
overview: Matter Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Remote Sensing, Earth Observation, Hyperspectral Imaging, and Geospatial.
plans:
- name: Matter Intelligence Plans Pricing
  plan_count: 0
  slug: matter-intelligence-plans-pricing
random_paper: 12
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Matter Intelligence Domain Security
  slug: matter-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matter-intelligence
tags:
- Company
- Remote Sensing
- Earth Observation
- Hyperspectral Imaging
- Geospatial
- Satellite Imagery
- Sensors
- Artificial Intelligence
- Climate
- Aerospace
website: https://www.matter.com/
---
