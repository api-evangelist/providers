---
access_model:
  confidence: medium
  label: Enterprise · Partner / provider integration (gated)
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - review
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Tempus Edge is a secure gateway that establishes bidirectional interfaces with provider EHRs using HL7, FHIR, API, and PACS connectivity so genomic test orders and results flow directly inside the cli
  name: Tempus EHR Integration (Tempus Edge)
  slug: tempus-ehr-integration
- description: Tempus Hub is a secure online portal for providers to order genomic and molecular tests, track order status, and view comprehensive patient results, available on desktop and mobile. It is an authentic
  name: Tempus Hub
  slug: tempus-hub
- description: 'Tempus Lens is an agentic-AI platform for oncology drug development that combines a large de-identified multimodal real-world dataset with Tempus oncology foundation models, AI agents, and scientific '
  name: Tempus Lens Platform
  slug: tempus-lens
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tempus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tempus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tempuslabs
- group: docs
  title: ''
  type: Documentation
  url: https://www.tempus.com/resources/document-library/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tempus.com/providers/
- group: company
  title: ''
  type: Blog
  url: https://www.tempus.com/news/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tempus-llms.txt
created: '2026-07-24'
description: 'Tempus AI, Inc. (formerly Tempus Labs) is an AI-enabled precision medicine and genomic diagnostics company founded in 2015 by Eric Lefkofsky and headquartered in Chicago, Illinois (NASDAQ: TEM). Tempus has assembled one of the world''s largest libraries of clinical and molecular data and runs a next-generation-sequencing lab offering oncology assays such as Tempus xT (solid-tumor DNA panel), xF (cell-free DNA liquid biopsy), xG (germline), and whole-transcriptome RNA, expanding from oncology into cardiology, neuropsychiatry, radiology, and infectious disease. For its United States home market its technical surface is delivered as partner and provider integrations rather than a public self-serve developer program: Tempus Hub (a provider portal to order tests and view genomic results), EHR integration via Tempus Edge (bidirectional HL7, FHIR, API, and PACS interfaces into Epic, Oracle Health / Cerner, OncoEMR, and other EHRs), the Tempus Lens agentic-AI platform for oncology
  drug development, Tempus One clinical assistant, and de-identified multimodal real-world-data collaborations for life sciences. As of this review no public developer portal, downloadable OpenAPI, or anonymously reachable FHIR CapabilityStatement was found; integration is gated behind partner and provider onboarding.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Tempus
nav: Providers
network: true
overview: 'Tempus publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Genomics, Precision Medicine, and Clinical AI.


  Tempus'' developer surface includes documentation, getting-started guide, engineering blog, and 4 more developer resources.'
random_paper: 54
score:
  band: minimal
  composite: 11.5
  delta: -2.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Tempus Domain Security
  slug: tempus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tempus
tags:
- Healthcare
- United States
- Genomics
- Precision Medicine
- Clinical AI
- Oncology
- FHIR
- HL7
- EHR
- Interoperability
- Life Sciences
- Real-World Data
website: https://www.tempus.com/
---
