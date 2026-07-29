---
access_model:
  confidence: high
  label: Enterprise · Partner onboarding
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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datavant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datavant.com/
- group: company
  title: ''
  type: Blog
  url: https://www.datavant.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.datavant.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datavant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datavant.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datavant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datavant
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datavant-llms.txt
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/connect-linkage
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/connect-privacy
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/connect-retrieval
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/insights-and-evidence-generation
created: '2026-07-24'
description: Datavant is a United States health-data logistics company, formed from the 2021 merger of Datavant and Ciox Health, that connects and de-identifies healthcare data across a "network of networks" spanning 350+ real-world data partners, 80,000+ hospitals and clinics, and a majority of the largest US health systems. Its core capabilities are privacy-preserving record linkage using Datavant tokens, HIPAA Expert Determination and de-identification, medical record retrieval / release of information, and real-world evidence generation for life sciences, payers, providers, and government. Datavant's integration surface is enterprise and partner/contract gated - an access-controlled API host exists at api.datavant.com (returns HTTP 403 to anonymous callers) but Datavant does not publish a self-serve public developer portal, a downloadable OpenAPI specification, or a FHIR CapabilityStatement. Home market is the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Datavant
nav: Providers
network: true
overview: 'Datavant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Interoperability, Health Data, and De-Identification.


  Datavant''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 61
score:
  band: emerging
  composite: 13.5
  delta: -3.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datavant/refs/heads/main/screenshots/datavant-2026-07-25T211401.png
security:
- kind: domain-security
  name: Datavant Domain Security
  slug: datavant-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: datavant
tags:
- Healthcare
- United States
- Interoperability
- Health Data
- De-Identification
- Tokenization
- Real-World Data
- Record Retrieval
- Data Connectivity
- Life Sciences
- HIPAA
website: https://www.datavant.com/
---
