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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rakuten-medical-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rakuten-medical-llms.txt
- group: company
  title: ''
  type: Website
  url: https://rakuten-med.com/us/
- group: company
  title: ''
  type: About
  url: https://rakuten-med.com/us/about/
- group: company
  title: ''
  type: Blog
  url: https://rakuten-med.com/us/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://rakuten-med.com/us/feed/
- group: company
  title: ''
  type: News
  url: https://rakuten-med.com/us/news/press-releases/
- group: operate
  title: ''
  type: Support
  url: https://rakuten-med.com/us/contact/
- group: company
  title: ''
  type: Careers
  url: https://rakuten-med.com/us/recruitment/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rakuten-med.com/us/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rakuten-medical/
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/rakuten-medical_stock/
coverage:
  checked: '2026-08-05'
  detail: Rakuten Medical is a clinical-stage biotechnology company whose product is a drug-device cancer therapy (an IRDye 700DX antibody conjugate plus a 690nm laser), sold to hospitals and regulated by PMDA and FDA rather than integrated by developers; its only web property is a WordPress corporate site, and the sole non-www host that resolves, portal.rakuten-med.com, is an F5 BIG-IP employee VPN that answers 200 with the same HTML logout page for every path.
  evidence:
  - status: 404
    url: https://rakuten-med.com/us/openapi.json
  - status: 404
    url: https://rakuten-med.com/us/.well-known/api-catalog
  - status: 404
    url: https://rakuten-med.com/us/.well-known/agent-card.json
  - status: 404
    url: https://rakuten-med.com/us/llms.txt
  - status: 404
    url: https://rakuten-med.com/us/developers
  - status: 200
    url: https://portal.rakuten-med.com/.well-known/agent-card.json
  - status: 200
    url: https://rakuten-med.com/us/pipeline/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Rakuten Medical, Inc. is a global biotechnology company headquartered in San Diego, California, developing precision, cell-targeting investigational cancer therapies on its proprietary Alluminox platform — a drug-device combination pairing an IRDye 700DX light-activated dye conjugated to a cell-targeting antibody with local illumination by 690nm red light. Founded in 2010 as Aspyrian Therapeutics and renamed following investment from Rakuten Group, the company operates in the United States, Japan, Taiwan, Switzerland and India. Its lead asset ASP-1929, an EGFR-targeting antibody-dye conjugate, received marketing approval in Japan in 2021 as Akalux for unresectable locally advanced or recurrent head and neck cancer and is in global Phase 3 development alone and in combination with anti-PD-1 therapy; RM-1995 and RM-0256 follow in earlier-stage programs. As a clinical-stage therapeutics and drug-device company, Rakuten Medical publishes no public developer API, SDK, webhook, or
  machine-readable specification; this profile captures its corporate identity and public web properties in the API Evangelist network.
image: https://rakuten-med.com/us/wp-content/uploads/sites/6/2021/02/RakutenMedical_KV.png
layout: provider
modified: '2026-08-05'
name: Rakuten Medical
nav: Providers
network: true
overview: 'Rakuten Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Healthcare.


  Rakuten Medical''s developer surface includes engineering blog, product news, support, and 9 more developer resources.'
random_paper: 36
score:
  band: minimal
  composite: 8.3
  delta: -1.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
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
  name: Rakuten Medical Domain Security
  slug: rakuten-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rakuten-medical
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Healthcare
- Life Sciences
- Photoimmunotherapy
- Medical Devices
- Clinical Trials
- Cancer
website: https://rakuten-med.com/us/
---
