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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Load Balancing Agentic Access
  operation_count: 7
  slug: google-cloud-load-balancing-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 4
apis:
- description: Manage backend services for load balancers
  name: Google Cloud Load Balancing BackendServices API
  slug: google-cloud-load-balancing-backendservices-api
- description: Manage forwarding rules for directing traffic
  name: Google Cloud Load Balancing ForwardingRules API
  slug: google-cloud-load-balancing-forwardingrules-api
- description: Manage health checks for backend services
  name: Google Cloud Load Balancing HealthChecks API
  slug: google-cloud-load-balancing-healthchecks-api
- description: Manage URL maps for routing traffic
  name: Google Cloud Load Balancing UrlMaps API
  slug: google-cloud-load-balancing-urlmaps-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices API
  slug: postman-google-cloud-load-balancing-backendservices-api
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices ForwardingRules API
  slug: postman-google-cloud-load-balancing-forwardingrules-api
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices HealthChecks API
  slug: postman-google-cloud-load-balancing-healthchecks-api
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices UrlMaps API
  slug: postman-google-cloud-load-balancing-urlmaps-api
- collection_type: open
  name: Google Cloud Load Balancing API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-load-balancing/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-load-balancing-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-load-balancing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-load-balancing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-load-balancing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-load-balancing-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/load-balancing
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/load-balancing/docs/how-to
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/load-balancing/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/load-balancing/pricing
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
  url: https://cloud.google.com/load-balancing/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: Google Cloud Load Balancing provides high-performance, scalable load balancing for Google Cloud Platform services, distributing traffic across multiple instances, regions, and backends to ensure reliability and low latency.
finops:
- name: Google Cloud Load Balancing Finops
  service_category: API
  slug: google-cloud-load-balancing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-load-balancing.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Load Balancing
nav: Providers
network: true
overview: 'Google Cloud Load Balancing publishes 4 APIs on the [APIs.io](https://apis.io/) network, including BackendServices API, ForwardingRules API, HealthChecks API, and 1 more. Tagged areas include Google Cloud, Infrastructure, Load Balancing, Networking, and Traffic Management.


  The Google Cloud Load Balancing catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Load Balancing''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Load Balancing Plans Pricing
  plan_count: 3
  slug: google-cloud-load-balancing-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Google Cloud Load Balancing Rate Limits
  slug: google-cloud-load-balancing-rate-limits
rules:
- name: Google Cloud Load Balancing API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-load-balancing-jsonschema-spectral-rules
scopes:
- name: Google Cloud Load Balancing Scopes
  scope_count: 2
  slug: google-cloud-load-balancing-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.2
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-load-balancing/refs/heads/main/screenshots/google-cloud-load-balancing-2026-06-20T182118.png
security:
- kind: authentication
  name: Google Cloud Load Balancing Authentication
  slug: google-cloud-load-balancing-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Load Balancing Domain Security
  slug: google-cloud-load-balancing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Load Balancing Vulnerability Disclosure
  slug: google-cloud-load-balancing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-load-balancing
tags:
- Google Cloud
- Infrastructure
- Load Balancing
- Networking
- Traffic Management
website: https://cloud.google.com/load-balancing
---
