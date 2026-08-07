---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud App Engine Agentic Access
  operation_count: 8
  slug: google-cloud-app-engine-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 4
apis:
- description: Manage App Engine applications
  name: Google Cloud App Engine Applications API
  slug: google-cloud-app-engine-applications-api
- description: The Apps API from Google Cloud App Engine — 2 operation(s) for apps.
  name: Google Cloud App Engine Apps API
  slug: google-cloud-app-engine-apps-api
- description: Manage instances running a version
  name: Google Cloud App Engine Instances API
  slug: google-cloud-app-engine-instances-api
- description: Manage versions of a service
  name: Google Cloud App Engine Versions API
  slug: google-cloud-app-engine-versions-api
artifact_total: 20
collections:
- collection_type: postman
  name: Google Cloud App Engine Admin Applications API
  slug: postman-google-cloud-app-engine-applications-api
- collection_type: postman
  name: Google Cloud App Engine Admin Applications Apps API
  slug: postman-google-cloud-app-engine-apps-api
- collection_type: postman
  name: Google Cloud App Engine Admin Applications Instances API
  slug: postman-google-cloud-app-engine-instances-api
- collection_type: postman
  name: Google Cloud App Engine Admin Applications Versions API
  slug: postman-google-cloud-app-engine-versions-api
- collection_type: open
  name: Google Cloud App Engine Admin API
  slug: open-appengine
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-app-engine/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-app-engine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-app-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-app-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-app-engine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-app-engine-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/appengine
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/appengine/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/appengine/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/appengine/pricing
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
  url: https://cloud.google.com/appengine/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/appengine-context.jsonld
created: '2026-03-13'
description: Google Cloud App Engine is a fully managed, serverless platform for developing and hosting web applications at scale. It supports popular programming languages and provides built-in services and APIs such as NoSQL datastores, memcache, and a user authentication API, allowing developers to focus on writing code without managing the underlying infrastructure.
finops:
- name: Google Cloud App Engine Finops
  service_category: API
  slug: google-cloud-app-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-app-engine.png
json_schemas:
- name: Google Cloud App Engine Application
  property_count: 10
  slug: appengine-application
jsonld:
- class_count: 11
  name: Appengine Context
  property_count: 3
  slug: appengine-context
layout: provider
modified: '2026-05-19'
name: Google Cloud App Engine
nav: Providers
network: true
overview: 'Google Cloud App Engine publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Apps API, Instances API, and 1 more. Tagged areas include App Engine, Compute, Google Cloud, PaaS, and Serverless.


  The Google Cloud App Engine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud App Engine''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud App Engine Plans Pricing
  plan_count: 3
  slug: google-cloud-app-engine-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 5
  name: Google Cloud App Engine Rate Limits
  slug: google-cloud-app-engine-rate-limits
rules:
- name: Google Cloud App Engine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-app-engine-jsonschema-spectral-rules
scopes:
- name: Google Cloud App Engine Scopes
  scope_count: 2
  slug: google-cloud-app-engine-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 63.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.9
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-app-engine/refs/heads/main/screenshots/google-cloud-app-engine-2026-06-20T182039.png
security:
- kind: authentication
  name: Google Cloud App Engine Authentication
  slug: google-cloud-app-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud App Engine Domain Security
  slug: google-cloud-app-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud App Engine Vulnerability Disclosure
  slug: google-cloud-app-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-app-engine
tags:
- App Engine
- Compute
- Google Cloud
- PaaS
- Serverless
- Web Applications
website: https://cloud.google.com/appengine
---
