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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inquis-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inquismedical.com/
- group: company
  title: ''
  type: Blog
  url: https://inquismedical.com/about-us/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://inquismedical.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://inquismedical.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inquismedical.com/terms-and-conditions/
- group: operate
  title: ''
  type: FAQ
  url: https://inquismedical.com/faqs/
- group: company
  title: ''
  type: Careers
  url: https://inquismedical.com/careers/
- group: other
  title: ''
  type: Patents
  url: https://inquismedical.com/patents/
- group: other
  title: ''
  type: Technology
  url: https://inquismedical.com/technology/
- group: build
  title: ''
  type: ClinicalEvidence
  url: https://inquismedical.com/clinical-evidence/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InquisMedical
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inquis-medical/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Inquismedical
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@inquis.medical
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/inquis-medical_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inquis-medical-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Inquis Medical sells clinical hardware — the AVENTUS thrombectomy catheter system used at the point of care — and ships no software product to integrate with; inquismedical.com is a single WordPress marketing host with no api./developer./docs./dev./app./portal./partners. subdomain in DNS (all NXDOMAIN), the whole /.well-known/ directory is answered by a 403 WAF interstitial, and the only machine-readable JSON on the domain is the stock WordPress core REST API at /wp-json/, which is the CMS and not an Inquis Medical product API.
  evidence:
  - status: 404
    url: https://inquismedical.com/openapi.json
  - status: 404
    url: https://inquismedical.com/swagger.json
  - status: 404
    url: https://inquismedical.com/graphql
  - status: 404
    url: https://inquismedical.com/llms.txt
  - status: 404
    url: https://inquismedical.com/.well-known/security.txt
  - status: 403
    url: https://inquismedical.com/.well-known/agent-card.json
  - status: 403
    url: https://inquismedical.com/.well-known/api-catalog
  - status: 200
    url: https://inquismedical.com/wp-json/
  - status: 200
    url: https://github.com/InquisMedical
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'Inquis Medical is a privately funded medical device company founded in 2020 and headquartered at 1530 O''Brien Drive in Menlo Park, California, dedicated to advancing the treatment of venous thromboembolic disease (VTE). Its flagship product, the AVENTUS Precision Thrombectomy System, is a single-catheter mechanical thrombectomy platform that combines a directional intelligent tip with an integrated 5F navigation catheter and dilator, TrueClot proprietary tissue-sensing that gives the operator real-time feedback on what the catheter tip is engaging (wall latch, lollipops, clogs), and in-line filtration with autologous blood reinfusion that reduces blood loss without capital equipment. The AVENTUS Thrombectomy System received FDA 510(k) clearance for peripheral indications and, in June 2025, for the treatment of pulmonary embolism; the company also ships the AVENTUS Introducer Sheath and the AVENTUS Clot Management System. Inquis raised a $40 million Series B in 2024 and a $75
  million Series C to scale commercial adoption. Inquis Medical is a clinical hardware company: it publishes no public developer program, API documentation, SDK, or machine-readable API contract, and its public GitHub organization holds a single empty embedded-firmware repository.'
image: https://inquismedical.com/wp-content/uploads/2025/10/Inquis-Medical-logo-reverse-rgb-e1760390408126.png
layout: provider
modified: '2026-08-23'
name: Inquis Medical
nav: Providers
network: true
overview: 'Inquis Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Thrombectomy, and Interventional Radiology.


  Inquis Medical''s developer surface includes engineering blog, support, FAQ, YouTube channel, and 13 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.7
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Inquis Medical Domain Security
  slug: inquis-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inquis-medical
tags:
- Company
- Healthcare
- Medical Devices
- Thrombectomy
- Interventional Radiology
- Cardiovascular
- Pulmonary Embolism
- Catheters
- Clinical Trials
- Medical Hardware
website: https://inquismedical.com/
---
