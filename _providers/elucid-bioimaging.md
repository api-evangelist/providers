---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://elucid.com/
- group: other
  title: ''
  type: Company
  url: https://elucid.com/about-elucid/
- group: operate
  title: ''
  type: Contact
  url: https://elucid.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://elucid.com/careers-at-elucid/
- group: company
  title: ''
  type: Blog
  url: https://elucid.com/about-elucid/#news
- group: company
  title: ''
  type: BlogRSS
  url: https://elucid.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elucid.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://elucid.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elucid-inc/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@elucidbioimaging
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ElucidBio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elucid-bioimaging-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elucid-bioimaging-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/elucid-bioimaging_stock/
coverage:
  checked: '2026-08-12'
  detail: Elucid ships Plaque-IQ as an FDA-cleared end-user clinical imaging application sold to health systems, and publishes no developer surface at all — elucid.com/api/, /developers/, /docs and /openapi.json all 404, and no api./docs./developer./app. subdomain even resolves in DNS.
  evidence:
  - status: 404
    url: https://elucid.com/developers/
  - status: 404
    url: https://elucid.com/api/
  - status: 404
    url: https://elucid.com/openapi.json
  - status: 404
    url: https://elucid.com/.well-known/agent-card.json
  - status: 200
    url: https://elucid.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Elucid Bioimaging, Inc. (operating as Elucid) is a Boston, Massachusetts medical technology company building AI-based image analysis software for cardiovascular disease. Its flagship product, Plaque-IQ, is an FDA-cleared CT-based plaque analysis platform indicated for both coronary and carotid anatomies: it applies image-restoration and segmentation algorithms to coronary CT angiography (CCTA) studies to quantify and classify lesion-level plaque morphology — including lipid-rich necrotic core — producing CAD-RADS classifications, straightened multi-planar reconstructions and a physician-validated PDF report. Elucid also offers an FFR-CT capability. The company sells to health systems, cardiologists, radiologists and vascular specialists through a clinical sales motion, and its go-to-market runs on reimbursement (Medicare Administrative Contractor, United Healthcare and EviCore coverage) rather than self-service signup. Elucid publishes no public developer program, API reference,
  SDK or machine-readable specification; the product is delivered as an end-user clinical platform.'
image: https://elucid.com/wp-content/uploads/2025/10/elucid-logo.svg
layout: provider
modified: '2026-08-12'
name: Elucid Bioimaging
nav: Providers
network: true
overview: 'Elucid Bioimaging is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Medical Imaging, Artificial Intelligence, and Cardiovascular.


  Elucid Bioimaging''s developer surface includes engineering blog, YouTube channel, and 12 more developer resources.'
plans:
- name: Elucid Bioimaging Plans Pricing
  plan_count: 0
  slug: elucid-bioimaging-plans-pricing
random_paper: 82
score:
  band: minimal
  composite: 7.4
  delta: -1.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Elucid Bioimaging Domain Security
  slug: elucid-bioimaging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elucid-bioimaging
tags:
- Company
- Health
- Medical Imaging
- Artificial Intelligence
- Cardiovascular
- Radiology
- Diagnostics
- Medical Devices
website: https://elucid.com/
---
