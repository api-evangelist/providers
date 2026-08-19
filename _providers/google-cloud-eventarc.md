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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Eventarc Agentic Access
  operation_count: 10
  slug: google-cloud-eventarc-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Eventarc — 5 operation(s) for projects.
  name: Google Cloud Eventarc Projects API
  slug: google-cloud-eventarc-projects-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud Eventarc Projects API
  slug: postman-google-cloud-eventarc-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Eventarc Projects API
  slug: open-google-cloud-eventarc-projects-api
- collection_type: open
  name: Google Cloud Eventarc API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-eventarc/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-eventarc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-eventarc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-eventarc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/eventarc
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/eventarc/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/eventarc/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/eventarc/pricing
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
  url: https://cloud.google.com/eventarc/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.json
created: '2026-03-13'
description: Google Cloud Eventarc is a fully managed eventing service that allows you to build event-driven architectures by routing events from Google Cloud services, SaaS applications, and custom sources to target destinations. Eventarc supports both standard and advanced editions, providing scalable, serverless event routing with built-in security, authorization, observability, and error handling.
finops:
- name: Google Cloud Eventarc Finops
  service_category: API
  slug: google-cloud-eventarc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-eventarc.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Eventarc
nav: Providers
network: true
overview: 'Google Cloud Eventarc publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Event-Driven, Events, Google Cloud, Messaging, and Serverless.


  The Google Cloud Eventarc catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Eventarc''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 9 more developer resources.'
plans:
- name: Google Cloud Eventarc Plans Pricing
  plan_count: 3
  slug: google-cloud-eventarc-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Google Cloud Eventarc Rate Limits
  slug: google-cloud-eventarc-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Cloud Eventarc API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-eventarc-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: -5.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 57.3
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-eventarc/refs/heads/main/screenshots/google-cloud-eventarc-2026-06-20T182110.png
security:
- kind: domain-security
  name: Google Cloud Eventarc Domain Security
  slug: google-cloud-eventarc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Eventarc Vulnerability Disclosure
  slug: google-cloud-eventarc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-eventarc
tags:
- Event-Driven
- Events
- Google Cloud
- Messaging
- Serverless
- Triggers
website: https://cloud.google.com/eventarc
---
