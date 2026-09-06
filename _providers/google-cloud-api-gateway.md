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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Api Gateway Agentic Access
  operation_count: 11
  slug: google-cloud-api-gateway-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://apigateway.googleapis.com
  baseurl_source: declared
  description: The Projects API from Google Cloud API Gateway — 5 operation(s) for projects.
  name: Google Cloud API Gateway Projects API
  slug: google-cloud-api-gateway-projects-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud API Gateway Projects API
  slug: postman-google-cloud-api-gateway-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud API Gateway Projects API
  slug: open-google-cloud-api-gateway-projects-api
- collection_type: open
  name: Google Cloud API Gateway API
  slug: open-openapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: https://cloud.google.com/trust-center
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cloud.google.com/release-notes
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-api-gateway/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-api-gateway-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-api-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-api-gateway-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/api-gateway
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/api-gateway/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/api-gateway/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/api-gateway/docs/authentication-method
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/api-gateway/pricing
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
  url: https://cloud.google.com/api-gateway/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.json
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/apigateway-release-notes.xml
created: '2026-03-13'
description: Google Cloud API Gateway enables you to provide secure access to your backend services through a well-defined REST API that is consistent across all of your services. It is a fully managed, pay-per-use gateway designed for serverless workloads, supporting Cloud Functions, Cloud Run, and App Engine backends. API Gateway includes security features like authentication and API key validation, as well as monitoring, logging, and tracing capabilities.
finops:
- name: Google Cloud Api Gateway Finops
  service_category: API
  slug: google-cloud-api-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-api-gateway.png
layout: provider
modified: '2026-05-19'
name: Google Cloud API Gateway
nav: Providers
network: true
overview: 'Google Cloud API Gateway publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include API Gateway, API Management, Authentication, Google Cloud, and Security.


  The Google Cloud API Gateway catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud API Gateway''s developer surface includes changelog, developer portal, getting-started guide, documentation, authentication, pricing, support, and 12 more developer resources.'
plans:
- name: Google Cloud Api Gateway Plans Pricing
  plan_count: 3
  slug: google-cloud-api-gateway-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Google Cloud Api Gateway Rate Limits
  slug: google-cloud-api-gateway-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud API Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-api-gateway-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 55.3
    catalog_earned_first_party: 0.0
    catalog_gap: 59.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 9.8
    contract_quality: 55.8
    developer_ergonomics: 58.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-api-gateway/refs/heads/main/screenshots/google-cloud-api-gateway-2026-06-20T182038.png
security:
- kind: domain-security
  name: Google Cloud Api Gateway Domain Security
  slug: google-cloud-api-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Api Gateway Vulnerability Disclosure
  slug: google-cloud-api-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-api-gateway
tags:
- API Gateway
- API Management
- Authentication
- Google Cloud
- Security
- Serverless
website: https://cloud.google.com/api-gateway
---
