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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Iam Agentic Access
  operation_count: 11
  slug: google-cloud-iam-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 4
apis:
- description: The Permissions API from Google Cloud IAM — 1 operation(s) for permissions.
  name: Google Cloud IAM Permissions API
  slug: google-cloud-iam-permissions-api
- description: The Roles API from Google Cloud IAM — 2 operation(s) for roles.
  name: Google Cloud IAM Roles API
  slug: google-cloud-iam-roles-api
- description: The Service Account Keys API from Google Cloud IAM — 1 operation(s) for service account keys.
  name: Google Cloud IAM Service Account Keys API
  slug: google-cloud-iam-service-account-keys-api
- description: The Service Accounts API from Google Cloud IAM — 2 operation(s) for service accounts.
  name: Google Cloud IAM Service Accounts API
  slug: google-cloud-iam-service-accounts-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud IAM Permissions API
  slug: postman-google-cloud-iam-permissions-api
- collection_type: postman
  name: Google Cloud IAM Permissions Roles API
  slug: postman-google-cloud-iam-roles-api
- collection_type: postman
  name: Google Cloud IAM Permissions Service Account Keys API
  slug: postman-google-cloud-iam-service-account-keys-api
- collection_type: postman
  name: Google Cloud IAM Permissions Service Accounts API
  slug: postman-google-cloud-iam-service-accounts-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud IAM Permissions API
  slug: open-google-cloud-iam-permissions-api
- collection_type: open
  name: Google Cloud IAM Permissions Roles API
  slug: open-google-cloud-iam-roles-api
- collection_type: open
  name: Google Cloud IAM Permissions Service Account Keys API
  slug: open-google-cloud-iam-service-account-keys-api
- collection_type: open
  name: Google Cloud IAM Permissions Service Accounts API
  slug: open-google-cloud-iam-service-accounts-api
- collection_type: open
  name: Google Cloud IAM API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-iam/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-iam-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-iam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-iam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-iam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-iam-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/iam
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/iam/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/iam/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/iam/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/iam/pricing
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
  url: https://cloud.google.com/iam/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Identity and Access Management (IAM) enables fine-grained access control and visibility for managing cloud resources. It provides the ability to create and manage service accounts, roles, and permissions to enforce least-privilege security policies across Google Cloud resources.
finops:
- name: Google Cloud Iam Finops
  service_category: API
  slug: google-cloud-iam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-iam.png
json_schemas:
- name: ServiceAccount
  property_count: 9
  slug: service-account
jsonld:
- class_count: 3
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud IAM
nav: Providers
network: true
overview: 'Google Cloud IAM publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Permissions API, Roles API, Service Account Keys API, and 1 more. Tagged areas include Access Management, Google Cloud, IAM, Identity, and Permissions.


  The Google Cloud IAM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud IAM''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Iam Plans Pricing
  plan_count: 3
  slug: google-cloud-iam-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Google Cloud Iam Rate Limits
  slug: google-cloud-iam-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud IAM API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-iam-jsonschema-spectral-rules
scopes:
- name: Google Cloud Iam Scopes
  scope_count: 2
  slug: google-cloud-iam-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 46.4
  delta: -7.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.5
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-iam/refs/heads/main/screenshots/google-cloud-iam-2026-06-20T182117.png
security:
- kind: authentication
  name: Google Cloud Iam Authentication
  slug: google-cloud-iam-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Iam Domain Security
  slug: google-cloud-iam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Iam Vulnerability Disclosure
  slug: google-cloud-iam-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-iam
tags:
- Access Management
- Google Cloud
- IAM
- Identity
- Permissions
- Security
website: https://cloud.google.com/iam
---
