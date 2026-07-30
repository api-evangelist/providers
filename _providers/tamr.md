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
api_count: 2
apis:
- description: The Tamr Core REST API allows programmatic access to Tamr's on-premise master data management application. It supports dataset management, project workflows, machine learning model training, classific
  name: Tamr Core REST API
  slug: core-rest-api
- description: The Tamr Cloud SaaS platform exposes APIs for managing tenants, data products, enrichment, and AI-driven mastering and classification workflows. Documented via the Tamr Developer Hub.
  name: Tamr Cloud API
  slug: cloud-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tamr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tamr-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tamrinc
- group: company
  title: ''
  type: Website
  url: https://www.tamr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tamr.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Datatamer
- group: company
  title: ''
  type: Blog
  url: https://www.tamr.com/blog
- group: company
  title: ''
  type: About
  url: https://www.tamr.com/about/
- group: company
  title: ''
  type: Careers
  url: https://www.tamr.com/careers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tamr.com/pricing
created: '2026-05-05'
description: An enterprise data management company that uses machine learning to automate the mastering, enrichment, and classification of messy data across disparate sources. Helps large organizations unify customer, supplier, and product data to power analytics and AI initiatives.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tamr.png
layout: provider
modified: '2026-05-16'
name: Tamr
nav: Providers
network: true
overview: 'Tamr publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Management, Machine Learning, Enterprise Software, and Master Data Management.


  Tamr''s developer surface includes documentation, GitHub presence, engineering blog, pricing, and 6 more developer resources.'
random_paper: 26
score:
  band: minimal
  composite: 12.5
  delta: -2.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tamr/refs/heads/main/screenshots/tamr-2026-06-20T194913.png
security:
- kind: domain-security
  name: Tamr Domain Security
  slug: tamr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tamr Trust Center
  slug: tamr-trust-center
  summary_line: SOC 2, GDPR
slug: tamr
tags:
- Data Management
- Machine Learning
- Enterprise Software
- Master Data Management
website: https://www.tamr.com/
---
