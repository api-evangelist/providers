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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercy-bioanalytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mercybio.com/
- group: operate
  title: ''
  type: Support
  url: https://mercybio.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mercybio.com/privacy-policy/
coverage:
  checked: '2026-08-25'
  detail: Mercy BioAnalytics sells a lab-run blood test (the Mercy Halo extracellular-vesicle liquid biopsy), not software — no api/developer/docs/portal/app subdomain of mercybio.com resolves in DNS, no GitHub org exists under mercybio or mercy-bioanalytics, no package is published to npm or PyPI, and every /openapi, /graphql and /.well-known path on mercybio.com is answered by a 169-byte SiteGround `sg-captcha` interstitial (HTTP 202) rather than a document.
  evidence:
  - status: 202
    url: https://mercybio.com/openapi.json
  - status: 202
    url: https://mercybio.com/.well-known/api-catalog
  - status: 202
    url: https://mercybio.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/mercybio
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Mercy BioAnalytics, Inc. is a Waltham, Massachusetts clinical-stage cancer diagnostics company, founded in 2018, developing extracellular-vesicle (EV) based liquid biopsy tests for the early detection of cancer. Its patented Mercy Halo platform uses biomarker co-localization — the simultaneous detection of multiple cancer-related biomarkers on the surface of individual tumor-derived extracellular vesicles — to read a small volume of serum or plasma with a simple PCR-based readout. The company''s initial programs target ovarian cancer screening in asymptomatic post-menopausal women and lung cancer detection in average and high-risk individuals; the Mercy Halo Ovarian Cancer Screening Test received FDA Breakthrough Device Designation in May 2024. Mercy BioAnalytics raised a $41M Series A in April 2023 led by Novalis LifeSciences and a $59M Series B in September 2025. The product is a laboratory-developed blood test, not software: as of this profile the company publishes no public
  developer program, API, SDK, or machine-readable API contract of any kind.'
layout: provider
modified: '2026-08-25'
name: Mercy BioAnalytics
nav: Providers
network: true
overview: 'Mercy BioAnalytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health, Diagnostics, and Biotechnology.


  Mercy BioAnalytics'' developer surface includes support and 3 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 4.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Mercy Bioanalytics Domain Security
  slug: mercy-bioanalytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mercy-bioanalytics
tags:
- Company
- Healthcare
- Health
- Diagnostics
- Biotechnology
- Life Sciences
- Cancer Screening
- Liquid Biopsy
- Laboratory
website: https://mercybio.com/
---
