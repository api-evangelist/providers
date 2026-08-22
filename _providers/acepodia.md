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
- group: company
  title: ''
  type: Website
  url: https://www.acepodia.com/
- group: company
  title: ''
  type: About
  url: https://www.acepodia.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.acepodia.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.acepodia.com/careers/
- group: other
  title: ''
  type: Leadership
  url: https://www.acepodia.com/leadership/
- group: other
  title: ''
  type: Technology
  url: https://www.acepodia.com/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://www.acepodia.com/pipeline/
- group: company
  title: ''
  type: Partnerships
  url: https://www.acepodia.com/partnerships/
- group: company
  title: ''
  type: News
  url: https://www.acepodia.com/newsroom/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.acepodia.com/newsroom/press-releases/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acepodia.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acepodia.com/legal/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acepodia/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acepodia-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acepodia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acepodia-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/acepodia_stock/
coverage:
  checked: '2026-08-06'
  detail: Acepodia is a clinical-stage cell-therapy developer whose published sitemap.xml lists 38 URLs, every one of them corporate (about, leadership, technology, pipeline, newsroom, partnerships, careers, legal) — no api., developer., docs., portal., app., status. or trust. host resolves for acepodia.com, no acepodia GitHub organisation exists, and every /.well-known/ and conventional spec path on www.acepodia.com returns the site's own HTML 404 page.
  evidence:
  - status: 200
    url: https://www.acepodia.com/sitemap.xml
  - status: 404
    url: https://www.acepodia.com/openapi.json
  - status: 404
    url: https://www.acepodia.com/.well-known/agent-card.json
  - status: 404
    url: https://www.acepodia.com/.well-known/security.txt
  - status: 404
    url: https://www.acepodia.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/acepodia
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Acepodia is a clinical-stage biotechnology company founded in 2017 by Dr. Patrick Y. Yang and Dr. Sonny Hsiao, headquartered in Alameda, California with operations in Taipei, Taiwan. It develops off-the-shelf allogeneic cell therapies for cancer and autoimmune disease built on two proprietary platforms: Antibody-Cell Conjugation (ACC), which uses bioorthogonal click chemistry from Carolyn Bertozzi''s Nobel Prize-winning work to attach tumor-targeting antibodies to gamma delta 2 T cells and natural killer cells without genetic engineering, and Antibody-Dual-Drugs Conjugation (AD2C). Its clinical pipeline includes ACE1831, an anti-CD20 gamma delta T cell therapy, and ACE2016, an anti-EGFR gamma delta T cell therapy. Acepodia is a therapeutics developer rather than a software vendor, and publishes no public API, developer portal, or machine-readable specification.'
image: https://www.acepodia.com/upload/base_fb_img/enL_01ns_web_base_20K06_uiwbgs3abs.png
layout: provider
modified: '2026-08-06'
name: Acepodia
nav: Providers
network: true
overview: 'Acepodia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Oncology, and Immunotherapy.


  Acepodia''s developer surface includes product news and 16 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.8
  delta: -1.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acepodia/refs/heads/main/screenshots/acepodia-2026-08-07T160823.png
security:
- kind: domain-security
  name: Acepodia Domain Security
  slug: acepodia-domain-security
  summary_line: TLSv1.2
slug: acepodia
tags:
- Company
- Biotechnology
- Cell Therapy
- Oncology
- Immunotherapy
- Life Sciences
- Clinical Stage
- Healthcare
website: https://www.acepodia.com/
---
