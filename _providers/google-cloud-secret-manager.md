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
  name: Google Cloud Secret Manager Agentic Access
  operation_count: 9
  slug: google-cloud-secret-manager-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 2
apis:
- description: The Secret Versions API from Google Cloud Secret Manager — 4 operation(s) for secret versions.
  name: Google Cloud Secret Manager Secret Versions API
  slug: google-cloud-secret-manager-secret-versions-api
- description: The Secrets API from Google Cloud Secret Manager — 2 operation(s) for secrets.
  name: Google Cloud Secret Manager Secrets API
  slug: google-cloud-secret-manager-secrets-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Cloud Secret Manager Secret Versions API
  slug: postman-google-cloud-secret-manager-secret-versions-api
- collection_type: postman
  name: Google Cloud Secret Manager Secret Versions Secrets API
  slug: postman-google-cloud-secret-manager-secrets-api
- collection_type: open
  name: Google Cloud Secret Manager API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-secret-manager/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-secret-manager-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-secret-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-secret-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-secret-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-secret-manager-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/secret-manager
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/secret-manager/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/secret-manager/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/secret-manager/pricing
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
  url: https://cloud.google.com/secret-manager/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/secret-manager-release-notes.xml
created: '2026-03-13'
description: Google Cloud Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. It provides a central place to manage, access, and audit secrets across Google Cloud with automatic versioning, IAM-based access control, and audit logging.
finops:
- name: Google Cloud Secret Manager Finops
  service_category: API
  slug: google-cloud-secret-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-secret-manager.png
json_schemas:
- name: Secret
  property_count: 10
  slug: secret
jsonld:
- class_count: 2
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Secret Manager
nav: Providers
network: true
overview: 'Google Cloud Secret Manager publishes 2 APIs on the [APIs.io](https://apis.io/) network: Secret Versions API and Secrets API. Tagged areas include Configuration, Credentials, Google Cloud, Key Management, and Secrets.


  The Google Cloud Secret Manager catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Secret Manager''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Secret Manager Plans Pricing
  plan_count: 3
  slug: google-cloud-secret-manager-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Google Cloud Secret Manager Rate Limits
  slug: google-cloud-secret-manager-rate-limits
rules:
- name: Google Cloud Secret Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-secret-manager-jsonschema-spectral-rules
scopes:
- name: Google Cloud Secret Manager Scopes
  scope_count: 1
  slug: google-cloud-secret-manager-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 61.2
  delta: -3.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 65.3
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-secret-manager/refs/heads/main/screenshots/google-cloud-secret-manager-2026-06-20T182131.png
security:
- kind: authentication
  name: Google Cloud Secret Manager Authentication
  slug: google-cloud-secret-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Secret Manager Domain Security
  slug: google-cloud-secret-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Secret Manager Vulnerability Disclosure
  slug: google-cloud-secret-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-secret-manager
tags:
- Configuration
- Credentials
- Google Cloud
- Key Management
- Secrets
- Security
website: https://cloud.google.com/secret-manager
---
