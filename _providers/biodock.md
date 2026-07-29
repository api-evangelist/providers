---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Submitting, tracking, and downloading analysis jobs
  name: Biodock Analysis Jobs API
  slug: biodock-analysis-jobs-api
- description: API key verification
  name: Biodock Auth API
  slug: biodock-auth-api
- description: Uploading and listing Biodock Filesystem items
  name: Biodock Files API
  slug: biodock-files-api
- description: Listing published analysis pipelines
  name: Biodock Pipelines API
  slug: biodock-pipelines-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.biodock.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biodock.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.biodock.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.biodock.ai/
- group: company
  title: ''
  type: Blog
  url: https://blog.biodock.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://biodock.statuspage.io/
- group: operate
  title: ''
  type: Support
  url: https://www.biodock.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biodock.ai/termsprivacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biodock.ai/termsprivacy
- group: auth
  title: ''
  type: Security
  url: https://www.biodock.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.biodock.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.biodock.ai/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biodock-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/biodock-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/biodock-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/biodock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biodock-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Biodock is an AI platform that makes deep learning easy to train, run, and interpret on biological and microscopy images, dramatically accelerating R&D image analysis. Researchers upload microscopy images, label and train fully-automated deep AI models in a visual labeler (no code required), and run those models across large datasets to segment, classify, and quantify objects such as cells - producing results comparable to flow cytometry along with downloadable object-level and aggregate data. Biodock is used by academic labs and Fortune 500 biopharma and life-science organizations, and is SOC 2 Type II and ISO 27001 certified. Beyond the visual app, Biodock exposes a public REST API (beta) for uploading files to the Biodock Filesystem, submitting analysis jobs against published pipelines, tracking job progress, and downloading results and segmentation masks - so analysis can be scripted and integrated into internal tools and imaging pipelines.
image: https://cdn.prod.website-files.com/63213d26df394911486f698e/637bb41c1cac3a4ded2e9f23_SEOImage.jpg
layout: provider
modified: '2026-07-18'
name: Biodock
nav: Providers
network: true
overview: 'Biodock publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analysis Jobs API, Auth API, Files API, and 1 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Image Analysis, and Microscopy.


  Biodock''s developer surface includes documentation, signup flow, engineering blog, support, and 14 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 43.6
  delta: -3.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.6
    developer_ergonomics: 25.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 47.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biodock/refs/heads/main/screenshots/biodock-2026-07-25T203036.png
security:
- kind: authentication
  name: Biodock Authentication
  slug: biodock-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Biodock Domain Security
  slug: biodock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Biodock Vulnerability Disclosure
  slug: biodock-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Biodock Trust Center
  slug: biodock-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001
slug: biodock
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Image Analysis
- Microscopy
- Life Sciences
- Biotechnology
- Computer Vision
- Cell Analysis
- Research
website: https://docs.biodock.ai/
---
