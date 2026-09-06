---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for Designer Cloud powered by Trifacta, exposing flows, wrangled recipes, imported/output datasets, jobs (jobGroups), connections, and deployment resources across the Google Cloud Dataprep, D
  name: Trifacta REST API
  slug: trifacta-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/trifacta-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trifacta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.alteryx.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://trust.alteryx.com/
- group: company
  title: ''
  type: Website
  url: https://www.alteryx.com/about-us/trifacta-is-now-alteryx-designer-cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trifacta.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.trifacta.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trifacta.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trifacta.com/terms-conditions/
- group: build
  title: ''
  type: Packages
  url: packages/trifacta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trifacta-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trifacta-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trifacta-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trifacta-domain-security.yml
created: '2026-07-17'
description: Trifacta is a data wrangling and data preparation platform that lets analysts and data engineers collaboratively profile, structure, clean, enrich, and pipeline data for analytics and machine learning. Founded in 2012 and spun out of Stanford/Berkeley research (backed by DCVC), Trifacta was acquired by Alteryx in early 2022 and the product is now marketed as Designer Cloud powered by Trifacta (and underpins Google Cloud Dataprep). Trifacta exposes a REST API across its product editions — Google Cloud Dataprep, Designer Cloud (SaaS), and self-managed Enterprise — for managing flows, wrangled recipes, datasets, jobs, and connections, along with a first-party Python SDK for automating data-preparation workflows.
image: https://api.trifacta.com/doc-logo.d2480004.svg
layout: provider
modified: '2026-07-21'
name: Trifacta
nav: Providers
network: true
overview: 'Trifacta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Preparation, Data Wrangling, Data Engineering, and ETL.


  Trifacta''s developer surface includes documentation, API reference, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trifacta/refs/heads/main/screenshots/trifacta-2026-09-02T164228.png
security:
- kind: domain-security
  name: Trifacta Domain Security
  slug: trifacta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trifacta Vulnerability Disclosure
  slug: trifacta-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Trifacta Trust Center
  slug: trifacta-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: trifacta
tags:
- Company
- Data Preparation
- Data Wrangling
- Data Engineering
- ETL
- Analytics
- Machine-Learning
- Data Quality
website: https://www.alteryx.com/about-us/trifacta-is-now-alteryx-designer-cloud
---
