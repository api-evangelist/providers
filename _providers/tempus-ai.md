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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
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
- description: Tempus integrates genomic test ordering and results into clinical workflows using near real-time connections (HL7, FHIR) and batch data exchange, including an integration with Epic. These interfaces a
  name: Tempus EHR Integration
  slug: tempus-ehr-integration
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: company
  title: ''
  type: About
  url: https://www.tempus.com/about-us/tempus-tech/next/
- group: company
  title: ''
  type: Investors
  url: https://www.tempus.com/oncology/genomic-profiling/
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
  url: llms/tempus-ai-llms.txt
created: '2026-06-20'
description: 'Tempus AI (NASDAQ: TEM) is a precision medicine company that has built one of the world''s largest libraries of de-identified clinical and molecular data, paired with an operating system to make that data accessible for diagnostics and research, starting with cancer. Its products span genomic profiling (xT / xR), AI-enabled clinical tools (Hub, One, Next), the Lens real-world data and agentic AI platform for life sciences, cardiology and radiology AI (ECG-AI, Pixel), and a consumer health app (Olivia). Tempus does not currently publish a self-serve, documented public developer API; integrations are delivered through enterprise and EHR channels (HL7 / FHIR, e.g. Epic) under partner agreements.'
finops:
- name: Tempus Ai Finops
  service_category: Healthcare and Life Sciences
  slug: tempus-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tempus-ai.png
layout: provider
modified: '2026-08-08'
name: Tempus AI
nav: Providers
network: true
overview: 'Tempus AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Precision Medicine, Genomics, Healthcare, Molecular Diagnostics, and Oncology.


  Tempus AI''s developer surface includes documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Tempus Ai Plans Pricing
  plan_count: 1
  slug: tempus-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Tempus Ai Rate Limits
  slug: tempus-ai-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
website: https://www.tempus.com/
---
