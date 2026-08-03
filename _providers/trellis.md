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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'Programmatic access to Trellis''s state and federal trial court dataset: Smart Search over rulings, dockets and documents; docket/case data (parties, attorneys, documents, events); docket refresh; ruli'
  name: Trellis Trial Court Data API
  slug: trellis-trial-court-data-api
artifact_total: 4
asyncapis:
- description: ''
  name: Trellis Webhooks
  slug: trellis-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://trellis.law
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.trellis.law/trellis-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.trellis.law/trellis-api
- group: docs
  title: ''
  type: APIReference
  url: https://trellis.law/feature/trellis-trial-court-api
- group: operate
  title: ''
  type: Support
  url: https://support.trellis.law
- group: company
  title: ''
  type: Blog
  url: https://blog.trellis.law
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trellis-law
- group: auth
  title: ''
  type: Authentication
  url: authentication/trellis-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trellis-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trellis-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trellis-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trellis-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trellis-domain-security.yml
created: '2026-07-17'
description: Trellis (Trellis Research, Inc.) is an AI-powered state and federal trial court research and litigation analytics platform founded by former litigator Nicole Clark. It makes the fragmented U.S. state trial court system — plus federal, appellate, supreme, and bankruptcy courts via PACER — searchable through a single interface, and exposes that data programmatically through the Trellis Trial Court Data API. Law firms, financial institutions, insurers, and researchers use Trellis for case research, judge and ruling analytics, docket monitoring with alerts, document retrieval, business development, lead generation, and due diligence. API access (V2, adding federal + PACER on top of V1 state coverage) is provisioned through a sales-gated free trial.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trellis.png
layout: provider
modified: '2026-07-21'
name: Trellis
nav: Providers
network: true
overview: 'Trellis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Analytics, Court Data, and Litigation.


  The Trellis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trellis'' developer surface includes documentation, API reference, support, engineering blog, authentication, changelog, and 7 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 31.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Trellis Authentication
  slug: trellis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trellis Domain Security
  slug: trellis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trellis
tags:
- Company
- Legal
- Legal Analytics
- Court Data
- Litigation
- Legal Tech
- Judicial Analytics
- Artificial Intelligence
website: https://trellis.law
---
