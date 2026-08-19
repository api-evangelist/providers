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
  url: security/caidya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caidya.com/
- group: company
  title: ''
  type: Blog
  url: https://www.caidya.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.caidya.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.caidya.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caidya.com/privacy-notices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caidya.com/disclaimer/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caidya-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/caidya-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.caidya.com/privacy-notices/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/caidya-stock
coverage:
  checked: '2026-08-08'
  detail: Caidya is a clinical research organization that explicitly positions itself as an integrator of the sponsor's preferred EDC, eCOA, IRT, CTMS, eTMF and safety platforms rather than a publisher of its own — there is no developer portal, no api./developer. subdomain (both NXDOMAIN), and the only machine-readable file on the whole estate is a Yoast-generated marketing llms.txt.
  evidence:
  - status: 200
    url: https://www.caidya.com/llms.txt
  - status: 404
    url: https://www.caidya.com/openapi.json
  - status: 404
    url: https://www.caidya.com/.well-known/agent-card.json
  - status: 404
    url: https://www.caidya.com/.well-known/security.txt
  - status: 200
    url: https://www.caidya.com/about/clinical-technology-ecosystem/
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: 'Caidya is a full-service, global clinical research organization (CRO) formed from the April 2021 merger of dMed and Clinipace, rebranded to Caidya in October 2022. It runs clinical development programs end to end — pre-IND and regulatory strategy, early phase, Phase II/III delivery, study start-up, trial feasibility, clinical operations, risk-based quality management, medical monitoring, clinical data management, biometrics, medical writing, pharmacovigilance, quality assurance and post-marketing surveillance — across oncology and hematology, cardiovascular-metabolic, rare disease, pediatrics, gastroenterology, nephrology, dermatology, ophthalmology, cell and gene therapy, neurology, immunology and infectious disease. The company took a $165M strategic growth investment from Rubicon Founders and announced a strategic combination with Simbec-Orion. Caidya is a clinical services provider rather than a software vendor: it integrates with sponsor-preferred EDC, eCOA, IRT, CTMS,
  eTMF and safety platforms rather than publishing a developer program or a public API of its own.'
image: https://www.caidya.com/wp-content/uploads/2026/06/og-image.png
layout: provider
modified: '2026-08-08'
name: Caidya
nav: Providers
network: true
overview: 'Caidya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clinical Research, Contract Research Organization, Healthcare, and Life Sciences.


  Caidya''s developer surface includes engineering blog, product news, support, and 8 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 16.8
  delta: 0.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Caidya Domain Security
  slug: caidya-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caidya
tags:
- Company
- Clinical Research
- Contract Research Organization
- Healthcare
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Clinical Data Management
- Pharmacovigilance
- Regulatory Affairs
- Biometrics
- Oncology
website: https://www.caidya.com/
---
