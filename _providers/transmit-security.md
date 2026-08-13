---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Transmit Security Agentic Access
  operation_count: 78
  slug: transmit-security-agentic-access
  summary_line: 78 operations · 49 acting
api_count: 9
apis:
- description: 'No-code identity orchestration API and policy engine enabling dynamic identity flow composition, adaptive access control, and integration with third-party services through pre-built journey templates '
  name: Mosaic Orchestration API
  slug: mosaic-orchestration-api
- description: The Applications API from Transmit Security — 14 operation(s) for applications.
  name: Transmit Security Applications API
  slug: transmit-security-applications-api
- description: The Auth API from Transmit Security — 10 operation(s) for auth.
  name: Transmit Security Auth API
  slug: transmit-security-auth-api
- description: The Manage API from Transmit Security — 1 operation(s) for manage.
  name: Transmit Security Manage API
  slug: transmit-security-manage-api
- description: The Organizations API from Transmit Security — 6 operation(s) for organizations.
  name: Transmit Security Organizations API
  slug: transmit-security-organizations-api
- description: The Recommendation API from Transmit Security — 3 operation(s) for recommendation.
  name: Transmit Security Recommendation API
  slug: transmit-security-recommendation-api
- description: The Token API from Transmit Security — 1 operation(s) for token.
  name: Transmit Security Token API
  slug: transmit-security-token-api
- description: The Users API from Transmit Security — 18 operation(s) for users.
  name: Transmit Security Users API
  slug: transmit-security-users-api
- description: The Verification API from Transmit Security — 6 operation(s) for verification.
  name: Transmit Security Verification API
  slug: transmit-security-verification-api
artifact_total: 38
collections:
- collection_type: postman
  name: One-Time Login Applications API
  slug: postman-transmit-security-applications-api
- collection_type: postman
  name: One-Time Login Applications Auth API
  slug: postman-transmit-security-auth-api
- collection_type: postman
  name: One-Time Login Applications Manage API
  slug: postman-transmit-security-manage-api
- collection_type: postman
  name: One-Time Login Applications Organizations API
  slug: postman-transmit-security-organizations-api
- collection_type: postman
  name: One-Time Login Applications Recommendation API
  slug: postman-transmit-security-recommendation-api
- collection_type: postman
  name: One-Time Login Applications Token API
  slug: postman-transmit-security-token-api
- collection_type: postman
  name: One-Time Login Applications Users API
  slug: postman-transmit-security-users-api
- collection_type: postman
  name: One-Time Login Applications Verification API
  slug: postman-transmit-security-verification-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/transmit-security/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transmit-security-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transmit-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transmit-security-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/transmit-security-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://transmitsecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.transmitsecurity.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TransmitSecurity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transmit-security
- group: other
  title: ''
  type: X
  url: https://x.com/transmitsec
- group: company
  title: ''
  type: Blog
  url: https://transmitsecurity.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://transmitsecurity.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.transmitsecurity.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.transmitsecurity.com/sdk-ref/platform/changelog
- group: build
  title: ''
  type: SDKs
  url: https://developer.transmitsecurity.com/sdk-ref/sdk_ref_intro
- group: commercial
  title: ''
  type: Plans
  url: plans/transmit-security-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transmit-security-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/transmit-security-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/transmit-security-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/transmit-security-context.jsonld
created: '2026-06-12'
description: Transmit Security provides the Mosaic platform, a comprehensive CIAM (Customer Identity and Access Management) solution offering REST APIs for passkey and WebAuthn authentication, fraud detection and risk-based access control, identity orchestration, identity verification, and user journey management. The platform delivers unified identity management across customer, business, and workforce contexts through an API-first architecture with OAuth2 and JWT authentication. Mosaic serves leading banks, insurers, and retailers worldwide with region-specific deployments across the US, EU, Canada, and Australia, backed by a 99.99% uptime SLA.
examples:
- key_count: 4
  name: Transmit Security Fraud Prevention Recommendation Request Example
  slug: transmit-security-fraud-prevention-recommendation-request-example
- key_count: 6
  name: Transmit Security Identity Management Create User Example
  slug: transmit-security-identity-management-create-user-example
- key_count: 4
  name: Transmit Security Identity Verification Create Session Example
  slug: transmit-security-identity-verification-create-session-example
- key_count: 4
  name: Transmit Security Organizations Create Org Example
  slug: transmit-security-organizations-create-org-example
- key_count: 5
  name: Transmit Security Platform Administration Create App Example
  slug: transmit-security-platform-administration-create-app-example
finops:
- name: Transmit Security Finops
  service_category: ''
  slug: transmit-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transmit-security.png
json_schemas:
- name: Transmit Security One-Time Login Schemas
  property_count: 0
  slug: transmit-security-backend-authentication
- name: Transmit Security Recommendations Schemas
  property_count: 0
  slug: transmit-security-fraud-prevention
- name: Transmit Security Users Schemas
  property_count: 0
  slug: transmit-security-identity-management
- name: Transmit Security Document Verification Schemas
  property_count: 0
  slug: transmit-security-identity-verification
- name: Transmit Security One-Time Login Schemas
  property_count: 0
  slug: transmit-security-oidc-authentication
- name: Transmit Security Organizations Schemas
  property_count: 0
  slug: transmit-security-organizations
- name: Transmit Security Applications Schemas
  property_count: 0
  slug: transmit-security-platform-administration
jsonld:
- class_count: 204
  name: Transmit Security Context
  property_count: 0
  slug: transmit-security-context
layout: provider
modified: '2026-06-12'
name: Transmit Security
nav: Providers
network: true
overview: 'Transmit Security publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Auth API, Manage API, and 5 more. Tagged areas include CIAM, Identity, Authentication, Passkeys, and WebAuthn.


  The Transmit Security catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Transmit Security''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 15 more developer resources.'
plans:
- name: Transmit Security Plans Pricing
  plan_count: 4
  slug: transmit-security-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Transmit Security Rate Limits
  slug: transmit-security-rate-limits
rules:
- name: Transmit Security API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: transmit-security-jsonschema-spectral-rules
scopes:
- name: Transmit Security Scopes
  scope_count: 4
  slug: transmit-security-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: strong
  composite: 58.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.6
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transmit-security/refs/heads/main/screenshots/transmit-security-2026-06-20T195547.png
security:
- kind: authentication
  name: Transmit Security Authentication
  slug: transmit-security-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Transmit Security Domain Security
  slug: transmit-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transmit-security
tags:
- CIAM
- Identity
- Authentication
- Passkeys
- WebAuthn
- Fraud Detection
- Risk Management
- Identity Verification
- Orchestration
- OAuth2
- Security
- SSO
website: https://transmitsecurity.com/
---
