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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/binx-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/binx-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://mybinxhealth.com/
- group: company
  title: ''
  type: About
  url: https://mybinxhealth.com/about/
- group: company
  title: ''
  type: Blog
  url: https://mybinxhealth.com/binxblog-2/
- group: company
  title: ''
  type: News
  url: https://mybinxhealth.com/news/
- group: operate
  title: ''
  type: Support
  url: https://help.mybinxhealth.com/s/
- group: operate
  title: ''
  type: Contact
  url: https://mybinxhealth.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://mybinxhealth.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mybinxhealth.com/toc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mybinxhealth.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/binxhealth
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/binx-health_stock/
coverage:
  checked: '2026-08-07'
  detail: binx health sells a physical point-of-care instrument through medical distributors and runs no developer program at all — /api, /developers, /docs and /integrations are honest 404s on mybinxhealth.com, no api.* or developer.* host resolves, and the only machine-readable endpoints on the host are its WordPress CMS REST API and an auth-gated WordPress MCP adapter plugin (401), neither of which is a product API.
  evidence:
  - status: 404
    url: https://mybinxhealth.com/developers
  - status: 404
    url: https://mybinxhealth.com/api-docs
  - status: 404
    url: https://mybinxhealth.com/openapi.json
  - status: 404
    url: https://mybinxhealth.com/.well-known/agent-card.json
  - status: 401
    url: https://mybinxhealth.com/wp-json/mcp/mcp-adapter-default-server
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: binx health, inc. is a Boston, Massachusetts point-of-care diagnostics company whose binx io platform is the first FDA-cleared, CLIA-waived molecular point-of-care test for chlamydia (Chlamydia trachomatis) and gonorrhea (Neisseria gonorrhoeae), returning central-lab-equivalent results in roughly thirty minutes from female vaginal swabs or male urine so a patient can be tested, diagnosed and treated in a single visit. The instrument pairs ultra-rapid PCR amplification with the company's proprietary electrochemical detection and needs no calibration, preventative maintenance or result interpretation, so it can be run by staff with no laboratory training. binx sells into urgent care, OB/GYN, pediatrics, student health, government health and other specialty settings through distributors including Cardinal Health, McKesson, Medline and Fisher Healthcare. The company divested its at-home consumer testing business to imaware in December 2023 and retained the point-of-care molecular
  diagnostics business. binx health publishes no public developer program, API reference or machine-readable specification.
image: https://mybinxhealth.com/wp-content/uploads/2025/04/cropped-binx_logo-1.webp
layout: provider
modified: '2026-08-07'
name: Binx Health
nav: Providers
network: true
overview: 'Binx Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Molecular Diagnostics.


  Binx Health''s developer surface includes engineering blog, product news, support, and 10 more developer resources.'
random_paper: 64
score:
  band: emerging
  composite: 13.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/binx-health/refs/heads/main/screenshots/binx-health-2026-08-07T162443.png
security:
- kind: domain-security
  name: Binx Health Domain Security
  slug: binx-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: binx-health
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Molecular Diagnostics
- Point of Care Testing
- Medical Devices
- Sexual Health
- Laboratory
website: https://mybinxhealth.com/
---
