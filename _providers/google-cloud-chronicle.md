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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Chronicle Agentic Access
  operation_count: 9
  slug: google-cloud-chronicle-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 4
apis:
- description: Operations for managing security alerts
  name: Google Cloud Chronicle Alerts API
  slug: google-cloud-chronicle-alerts-api
- description: Operations for managing data ingestion feeds
  name: Google Cloud Chronicle Feeds API
  slug: google-cloud-chronicle-feeds-api
- description: Operations for managing reference lists
  name: Google Cloud Chronicle ReferenceLists API
  slug: google-cloud-chronicle-referencelists-api
- description: Operations for managing detection rules
  name: Google Cloud Chronicle Rules API
  slug: google-cloud-chronicle-rules-api
artifact_total: 16
collections:
- collection_type: open
  name: Google Cloud Chronicle API
  slug: open-chronicle-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-chronicle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-chronicle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-chronicle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-chronicle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-chronicle-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chronicle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chroniclesec
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/chronicle
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/chronicle/docs/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/chronicle/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/chronicle/docs/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/chronicle/pricing
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
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/chronicle/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-chronicle-context.jsonld
created: '2026-03-13'
description: Google Cloud Chronicle is a cloud-native security information and event management (SIEM) platform that enables enterprises to store, search, and analyze massive volumes of security telemetry data. Built on Google infrastructure, Chronicle provides sub-second search across petabytes of security data, threat detection using rules and intelligence, and investigation tools for security operations teams.
finops:
- name: Google Cloud Chronicle Finops
  service_category: API
  slug: google-cloud-chronicle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-chronicle.png
json_schemas:
- name: Google Cloud Chronicle UDM Event
  property_count: 7
  slug: google-cloud-chronicle-event
jsonld:
- class_count: 0
  name: Google Cloud Chronicle Context
  property_count: 4
  slug: google-cloud-chronicle-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Chronicle
nav: Providers
network: true
overview: 'Google Cloud Chronicle publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Feeds API, ReferenceLists API, and 1 more. Tagged areas include Incident Response, Log Management, Security Analytics, Security Operations, and SIEM.


  The Google Cloud Chronicle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Chronicle''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Chronicle Plans Pricing
  plan_count: 3
  slug: google-cloud-chronicle-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Google Cloud Chronicle Rate Limits
  slug: google-cloud-chronicle-rate-limits
rules:
- name: Google Cloud Chronicle API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-chronicle-jsonschema-spectral-rules
scopes:
- name: Google Cloud Chronicle Scopes
  scope_count: 1
  slug: google-cloud-chronicle-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 65.2
  delta: 4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.4
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 60.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-chronicle/refs/heads/main/screenshots/google-cloud-chronicle-2026-06-20T182100.png
security:
- kind: authentication
  name: Google Cloud Chronicle Authentication
  slug: google-cloud-chronicle-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Chronicle Domain Security
  slug: google-cloud-chronicle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Chronicle Vulnerability Disclosure
  slug: google-cloud-chronicle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-chronicle
tags:
- Incident Response
- Log Management
- Security Analytics
- Security Operations
- SIEM
- Threat Detection
website: https://cloud.google.com/chronicle
---
