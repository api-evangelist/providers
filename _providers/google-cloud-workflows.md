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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Workflows Agentic Access
  operation_count: 9
  slug: google-cloud-workflows-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Workflows — 5 operation(s) for projects.
  name: Google Cloud Workflows Projects API
  slug: google-cloud-workflows-projects-api
artifact_total: 10
collections:
- collection_type: postman
  name: Google Cloud Workflows Projects API
  slug: postman-google-cloud-workflows-projects-api
- collection_type: open
  name: Google Cloud Workflows API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-workflows/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-workflows-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-workflows-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-workflows-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/workflows
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/workflows/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/workflows/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/workflows/pricing
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
  url: https://cloud.google.com/workflows/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.json
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/workflows-release-notes.xml
created: '2026-03-13'
description: Google Cloud Workflows is a serverless orchestration service that lets you combine Google Cloud services and APIs into flexible, automated workflows. Workflows manages the order of execution, including handling retries, waiting, and polling, and ensures reliable execution despite hardware and networking interruptions. It supports conditional logic, subworkflows, and connectors to integrate with other Google Cloud products.
finops:
- name: Google Cloud Workflows Finops
  service_category: API
  slug: google-cloud-workflows-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-workflows.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Workflows
nav: Providers
network: true
overview: 'Google Cloud Workflows publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Automation, Google Cloud, Integration, Orchestration, and Serverless.


  The Google Cloud Workflows catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Workflows'' developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Workflows Plans Pricing
  plan_count: 3
  slug: google-cloud-workflows-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Google Cloud Workflows Rate Limits
  slug: google-cloud-workflows-rate-limits
rules:
- name: Google Cloud Workflows API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-workflows-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.3
  delta: -2.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 57.6
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-workflows/refs/heads/main/screenshots/google-cloud-workflows-2026-06-20T182150.png
security:
- kind: domain-security
  name: Google Cloud Workflows Domain Security
  slug: google-cloud-workflows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Workflows Vulnerability Disclosure
  slug: google-cloud-workflows-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-workflows
tags:
- Automation
- Google Cloud
- Integration
- Orchestration
- Serverless
- Workflows
website: https://cloud.google.com/workflows
---
