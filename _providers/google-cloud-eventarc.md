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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
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
artifact_total: 9
collections:
- collection_type: open
  name: Google Cloud Eventarc API
  slug: open-openapi
common:
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


  Google Cloud Eventarc''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 8 more developer resources.'
plans:
- name: Google Cloud Eventarc Plans Pricing
  plan_count: 3
  slug: google-cloud-eventarc-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Google Cloud Eventarc Rate Limits
  slug: google-cloud-eventarc-rate-limits
rules:
- name: Google Cloud Eventarc API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-eventarc-jsonschema-spectral-rules
score:
  band: developing
  composite: 57.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 50.4
    developer_ergonomics: 43.5
    discoverability: 60.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 57.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
