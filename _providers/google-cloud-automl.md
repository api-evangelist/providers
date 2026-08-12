---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Automl Agentic Access
  operation_count: 7
  slug: google-cloud-automl-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud AutoML — 4 operation(s) for projects.
  name: Google Cloud AutoML Projects API
  slug: google-cloud-automl-projects-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud AutoML Projects API
  slug: postman-google-cloud-automl-projects-api
- collection_type: open
  name: Google Cloud AutoML API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-automl/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-automl-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-automl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-automl-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/automl
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/automl/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/automl/docs/reference/rest
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/automl/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/automl/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/automl-natural-language-release-notes.xml
created: '2026-03-13'
description: Google Cloud AutoML enables developers with limited machine learning expertise to train high-quality custom models. It provides a suite of products for training custom ML models for translation, natural language, vision, video intelligence, and tabular data using transfer learning and neural architecture search.
finops:
- name: Google Cloud Automl Finops
  service_category: API
  slug: google-cloud-automl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-automl.png
json_schemas:
- name: AutoML Model
  property_count: 7
  slug: model
jsonld:
- class_count: 12
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud AutoML
nav: Providers
network: true
overview: 'Google Cloud AutoML publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include AutoML, Custom Models, Google Cloud, Machine Learning, and Training.


  The Google Cloud AutoML catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud AutoML''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Automl Plans Pricing
  plan_count: 3
  slug: google-cloud-automl-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Google Cloud Automl Rate Limits
  slug: google-cloud-automl-rate-limits
rules:
- name: Google Cloud AutoML API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-cloud-automl-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.3
  delta: -8.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.9
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-automl/refs/heads/main/screenshots/google-cloud-automl-2026-06-20T182043.png
security:
- kind: domain-security
  name: Google Cloud Automl Domain Security
  slug: google-cloud-automl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Automl Vulnerability Disclosure
  slug: google-cloud-automl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-automl
tags:
- AutoML
- Custom Models
- Google Cloud
- Machine Learning
- Training
website: https://cloud.google.com/automl
---
