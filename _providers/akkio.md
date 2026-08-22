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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Akkio's current public API, served and documented as "Akkio Public API (Beta)". Covers projects (including the Chat Explore custom-instruction fields), asynchronous model training, and Chat Explore na
  name: Akkio Public API (Beta)
  slug: akkio-public-api
- description: Legacy v1 datasets surface. Create a dataset, append rows, set field types, parse fields, list and delete. Authenticated with an api_key query parameter on GET and an api_key JSON body field on POST/D
  name: Akkio Datasets API
  slug: akkio-datasets-api
- description: Legacy v1 models surface. List trained models and POST rows to a model to receive predictions with per-class probabilities. Akkio's own docs describe the newer /api/v1 Training routes as a better-desi
  name: Akkio Models API
  slug: akkio-models-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Akkio Datasets API
  slug: open-akkio-datasets-api
- collection_type: open
  name: Akkio Datasets Models API
  slug: open-akkio-models-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akkio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akkio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.akkio.com/akkio-docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akkio.com/akkio-docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.akkio.com/akkio-docs/endpoints-and-schemas/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akkio.com/akkio-docs/rest-api/api-introduction/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.akkio.com/akkio-help-center
- group: company
  title: ''
  type: Blog
  url: https://www.akkio.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akkio-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.akkio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.akkio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.akkio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.akkio.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.akkio.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.akkio.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/akkio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/akkio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akkio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/akkio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/akkio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/akkio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/akkio-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/akkio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/akkio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/akkio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/akkio-api-openapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akkio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/akkio-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/akkio-problem-types.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/akkio-public-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/akkio-public-api-openapi.yaml
created: '2026-07-17'
description: 'Akkio is a no-code predictive AI and AI-workflow-automation platform built for media agencies and data providers. Teams use it to activate data across the campaign lifecycle: audience segmentation, propensity modeling, RFM analysis, media-mix modeling, performance measurement, and campaign-strategy development, all from unified intelligence. Beyond the app, Akkio ships a developer REST API on https://api.akkio.com in two generations: the legacy /v1 datasets and models routes (api_key in query or body), and the current "Akkio Public API (Beta)" at /api/v1, which covers projects, asynchronous model training and Chat Explore natural-language querying behind an X-API-Key header. Akkio publishes its own OpenAPI 3.1.0 document at /api/v1/api.yaml with a Swagger UI at /api/v1/docs and documents generating clients from it; the two first-party SDKs (PyPI and npm `akkio`) cover only the legacy surface and have not been released since 2021. The company is SOC 2 Type 2 and HIPAA compliant
  (verified via Drata).'
image: https://cdn.prod.website-files.com/5c97e8c9de94e8a3480419a5/6959836988084dcbb9ac3605_Screenshot%202026-01-03%20at%2012.58.19%E2%80%AFPM.png
layout: provider
modified: '2026-08-13'
name: Akkio
nav: Providers
network: true
overview: 'Akkio publishes 3 APIs on the [APIs.io](https://apis.io/) network: Public API (Beta), Datasets API, and Models API. Tagged areas include Company, Ai Apps, Machine Learning, Predictive Analytics, and No Code.


  Akkio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Akkio Plans Pricing
  plan_count: 0
  slug: akkio-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Akkio Rate Limits
  slug: akkio-rate-limits
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 30.3
    contract_quality: 52.2
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 53.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akkio/refs/heads/main/screenshots/akkio-2026-07-25T195516.png
security:
- kind: authentication
  name: Akkio Authentication
  slug: akkio-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Akkio Domain Security
  slug: akkio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Akkio Vulnerability Disclosure
  slug: akkio-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Akkio Trust Center
  slug: akkio-trust-center
  summary_line: SOC 2 Type 2, HIPAA
slug: akkio
tags:
- Company
- Ai Apps
- Machine Learning
- Predictive Analytics
- No Code
- Data Science
- Marketing
- Media
- Audience Modeling
- Predictions
website: https://www.akkio.com/
---
