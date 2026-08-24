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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halo-precision-diagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.halodx.com/
- group: company
  title: ''
  type: Blog
  url: https://www.halodx.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.halodx.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.halodx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.halodx.com/privacy/
- group: company
  title: ''
  type: Careers
  url: https://www.halodx.com/careers/
- group: other
  title: ''
  type: Team
  url: https://www.halodx.com/team/
- group: other
  title: ''
  type: Locations
  url: https://www.halodx.com/locations/
- group: company
  title: ''
  type: Partners
  url: https://www.halodx.com/partner-with-us/
- group: other
  title: ''
  type: ProviderResources
  url: https://www.halodx.com/provider-resources/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.halodx.com/knowledge-center/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/halo-dx
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/HaloDx/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCQudju8UU6L9-Fz27A6bH5Q
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/halo-precision-diagnostics-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/halo-precision-diagnostics-llms.txt
coverage:
  checked: '2026-08-22'
  detail: HALO Precision Diagnostics is a clinical imaging-center operator whose referring-physician integration is delivered by third-party vendor products — a RoyalMD provider portal and the eUnity image viewer — so halodx.com carries no developer, docs or API hostname, api.halodx.com resolves in DNS but answers every path with a bare empty 404, and the only machine-readable JSON on the site is the marketing CMS's stock WordPress core REST API at /wp-json/.
  evidence:
  - status: 404
    url: https://www.halodx.com/openapi.json
  - status: 404
    url: https://www.halodx.com/llms.txt
  - status: 404
    url: https://www.halodx.com/graphql
  - status: 404
    url: https://www.halodx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.halodx.com/.well-known/security.txt
  - status: 404
    url: https://www.halodx.com/.well-known/api-catalog
  - status: 404
    url: https://api.halodx.com/openapi.json
  - status: 404
    url: https://api.halodx.com/graphql
  - status: 404
    url: https://www.halodx.com/fhir/metadata
  - status: 200
    url: https://www.halodx.com/wp-json/
  - status: 200
    url: https://www.halodx.com/provider-resources/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: HALO Precision Diagnostics (HALO Dx) is a Menlo Park, California precision-diagnostics company that acquires community imaging centers and rebuilds them as what it calls Imaging Center 2.0 — next-generation diagnostic hubs where advanced imaging, genomics and biomarker testing are all performed under one roof. Its diagnostic ensemble combines whole-body and multiparametric MRI, PSMA-targeted PET (PYLARIFY), digital pathology, polygenic risk scoring, hereditary and proteomic testing, and AI-assisted interpretation, applied first to cancer — the prostate program adds MRI-guided targeted biopsy and MRI-guided TULSA-PRO focal ablation — and expanding into cardiovascular disease and dementia. The company is led by CEO Michael Uhl with co-founder Brian Axe as Chief Product Officer and Dr. John Feller as Chief Medical Officer. Clinical delivery happens in HALO's own centers; referring physicians reach orders, results and images through a vendor-operated provider portal (RoyalMD) and
  the eUnity enterprise image viewer, and HALO advertises EMR integration for pushing orders and pulling results as a service its vendors deliver rather than as an interface it publishes. HALO operates no public developer program, publishes no API documentation, ships no SDK, and serves no machine-readable API contract; the only JSON on halodx.com is the marketing site's stock WordPress core REST API.
image: https://www.halodx.com/wp-content/uploads/2025/05/HALO-Precision-Diagnostics_Logo.svg
layout: provider
modified: '2026-08-22'
name: HALO Precision Diagnostics
nav: Providers
network: true
overview: 'HALO Precision Diagnostics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Medical Imaging, and Radiology.


  HALO Precision Diagnostics'' developer surface includes engineering blog, support, YouTube channel, and 14 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: domain-security
  name: Halo Precision Diagnostics Domain Security
  slug: halo-precision-diagnostics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: halo-precision-diagnostics
tags:
- Company
- Healthcare
- Diagnostics
- Medical Imaging
- Radiology
- Cancer
- Precision Medicine
- Genomics
- Early Detection
- Artificial Intelligence
website: https://www.halodx.com/
---
