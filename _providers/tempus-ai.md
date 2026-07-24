---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: Lens is Tempus' real-world multimodal data and agentic AI platform for life sciences and oncology drug development, providing exploration of one of the world's largest de-identified clinical and molec
  name: Tempus Lens
  slug: tempus-lens
- description: Tempus One is an AI clinical assistant giving oncology providers voice and text access to patient data, clinical-trial options, and treatment guidelines at the point of care. It is surfaced inside Tem
  name: Tempus One
  slug: tempus-one
- description: 'Tempus Hub is the smart physician platform where providers order diagnostic tests, get clinical context on a patient, and receive and review testing results. Access is via the Hub web application and '
  name: Tempus Hub
  slug: tempus-hub
- description: Tempus Next ingests patient data and applies AI to unstructured elements, evaluating it against care guidelines to identify in near real time patients who have deviated from the standard of care. It i
  name: Tempus Next
  slug: tempus-next
- description: Tempus integrates genomic test ordering and results into clinical workflows using near real-time connections (HL7, FHIR) and batch data exchange, including an integration with Epic. These interfaces a
  name: Tempus EHR Integration
  slug: tempus-ehr-integration
- description: Tempus xT and xR are DNA and RNA next-generation sequencing assays for oncology. Results are returned through Tempus Hub and EHR integrations rather than a documented public API.
  name: Tempus Genomic Profiling (xT / xR)
  slug: tempus-genomic-profiling
artifact_total: 11
collections:
- collection_type: open
  name: Tempus AI
  slug: open-tempus-ai
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tempus-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tempuslabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tempuslabs
- group: company
  title: ''
  type: Website
  url: https://www.tempus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tempus.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tempus-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tempus-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tempus-ai-finops.yml
created: '2026-06-20'
description: 'Tempus AI (NASDAQ: TEM) is a precision medicine company that has built one of the world''s largest libraries of de-identified clinical and molecular data, paired with an operating system to make that data accessible for diagnostics and research, starting with cancer. Its products span genomic profiling (xT / xR), AI-enabled clinical tools (Hub, One, Next), the Lens real-world data and agentic AI platform for life sciences, cardiology and radiology AI (ECG-AI, Pixel), and a consumer health app (Olivia). Tempus does not currently publish a self-serve, documented public developer API; integrations are delivered through enterprise and EHR channels (HL7 / FHIR, e.g. Epic) under partner agreements.'
finops:
- name: Tempus Ai Finops
  service_category: Healthcare and Life Sciences
  slug: tempus-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tempus-ai.png
layout: provider
modified: '2026-06-20'
name: Tempus AI
nav: Providers
network: true
overview: 'Tempus AI publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Precision Medicine, Genomics, Healthcare, Molecular Diagnostics, and Oncology.


  Tempus AI''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Tempus Ai Plans Pricing
  plan_count: 1
  slug: tempus-ai-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Tempus Ai Rate Limits
  slug: tempus-ai-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: -0.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.7
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Tempus Ai Domain Security
  slug: tempus-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tempus-ai
tags:
- Precision Medicine
- Genomics
- Healthcare
- Molecular Diagnostics
- Oncology
- Real-World Data
- AI
website: https://www.tempus.com/
---
