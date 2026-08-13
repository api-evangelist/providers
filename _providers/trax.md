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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'Partner-facing REST API for the Trax retail intelligence platform: master data (stores, products, regions, retailers, targets, audit cycle sets), visit planning (routes, visit types, tasks, assortment'
  name: Trax Retail Platform API
  slug: trax-retail-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trax-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.apidoc.traxretail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apidoc.traxretail.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.apidoc.traxretail.com/input-api
- group: company
  title: ''
  type: Website
  url: https://traxretail.com/
- group: company
  title: ''
  type: Blog
  url: https://traxretail.com/resources-content-types/blogs/
- group: operate
  title: ''
  type: Support
  url: https://traxretail.com/get-in-touch
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traxretail.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traxretail.com/terms-conditions/
- group: auth
  title: ''
  type: Authentication
  url: authentication/trax-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trax-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trax-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/trax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trax-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trax-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trax-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trax-llms.txt
created: '2026-07-17'
description: Trax (Trax Retail) is a cloud-based retail intelligence platform that uses computer vision and image recognition to turn shelf photographs into real-time, actionable in-store insights for consumer packaged goods (CPG) brands and retailers. Its platform measures on-shelf availability, planogram and pricing compliance, share of shelf, promotional execution, and competitor activity across retail locations. Trax exposes a partner API surface for master data management (stores, products, regions, retailers), visit planning (routes, tasks, assortments), in-store execution via the Scene Mobile SDK and Input API (sessions, scenes, images), and analysis output/notification services, plus SSO and a Salesforce connector. Trax merged with FORM to combine retail image recognition with task management and workflow automation, and is a portfolio company of the SoftBank Vision Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trax.png
layout: provider
modified: '2026-07-21'
name: Trax
nav: Providers
network: true
overview: 'Trax publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Retail, Computer Vision, and Image Recognition.


  Trax''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 87
score:
  band: emerging
  composite: 24.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.0
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Trax Authentication
  slug: trax-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Trax Domain Security
  slug: trax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trax
tags:
- Company
- Enterprise
- Retail
- Computer Vision
- Image Recognition
- CPG
- Retail Execution
- Merchandising
- SaaS
website: https://traxretail.com/
---
