---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The first-party Python client library for LeapYear Core. The Client class opens an authenticated connection to a self-hosted LeapYear server and exposes administrative resources (databases, tables, co
  name: LeapYear Python Client
  slug: leapyear-python-client
artifact_total: 3
common:
- group: docs
  title: ''
  type: Documentation
  url: https://leapyear-python-docs.readthedocs-hosted.com/en/4.1.1/
- group: docs
  title: ''
  type: APIReference
  url: https://leapyear-python-docs.readthedocs-hosted.com/en/4.1.1/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://leapyear-python-docs.readthedocs-hosted.com/en/4.1.1/tutorial.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/leapyear-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/leapyear-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leapyear-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leapyear-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leapyear-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leapyear-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leapyear-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leapyear-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leapyear-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leapyear-llms.txt
created: '2026-07-17'
description: 'LeapYear Technologies built an enterprise platform for differentially private analytics and machine learning, letting organizations run statistics, SQL-style queries, feature engineering, and supervised and unsupervised model training against their most sensitive data while a mathematically provable privacy guarantee bounds what any single record can leak. The product shipped as a self-hosted server, LeapYear Core, driven by a first-party Python client library that exposes databases, tables, views, users, groups, permissions, privacy profiles, and per-database privacy budgets as programmable resources. Snowflake announced its intent to acquire LeapYear in February 2023 and closed the acquisition for $62.0 million in cash, folding the differential privacy technology and team into the Snowflake Data Cloud clean-room capabilities. The standalone company surface is now retired: leapyear.io no longer answers on HTTPS. The surviving public developer surface is the hosted LeapYear
  Python client reference for version 4.1.1.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leapyear.png
layout: provider
modified: '2026-07-19'
name: LeapYear
nav: Providers
network: true
overview: 'LeapYear publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Privacy, Differential Privacy, Machine Learning, and Analytics.


  LeapYear''s developer surface includes documentation, API reference, getting-started guide, authentication, and 9 more developer resources.'
random_paper: 91
score:
  band: emerging
  composite: 16.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 77.8
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 16.9
  provenance:
    conformance: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leapyear/refs/heads/main/screenshots/leapyear-2026-07-25T224754.png
security:
- kind: authentication
  name: Leapyear Authentication
  slug: leapyear-authentication
  summary_line: password/public-key · 3 schemes
- kind: domain-security
  name: Leapyear Domain Security
  slug: leapyear-domain-security
  summary_line: TLSv1.3 · HSTS
slug: leapyear
tags:
- Company
- Data Privacy
- Differential Privacy
- Machine Learning
- Analytics
- Data Clean Rooms
- Privacy Enhancing Technologies
- Python
- Acquired
---
