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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Platform Gcp Agentic Access
  operation_count: 10
  slug: google-cloud-platform-gcp-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- description: Unified AI platform for building, deploying, and scaling ML models.
  name: Vertex AI API
  slug: vertex-ai-api
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: spec
  description: The Projects API from Google Cloud Platform — 6 operation(s) for projects.
  name: Google Cloud Platform Projects API
  slug: google-cloud-platform-gcp-projects-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Compute Engine Projects API
  slug: open-google-cloud-platform-gcp-projects-api
- collection_type: open
  name: Google Compute Engine API
  slug: open-google-cloud-platform-gcp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-platform-gcp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-platform-gcp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-platform-gcp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-platform-gcp-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-cloud
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/apis/docs/client-libraries
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.google.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/docs
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com
- group: commercial
  title: ''
  type: Pricing Calculator
  url: https://cloud.google.com/products/calculator
created: '2024-01-15'
description: Google Cloud Platform provides a comprehensive suite of cloud computing services including compute, storage, databases, machine learning, networking, and more.
finops:
- name: Google Cloud Platform Gcp Finops
  service_category: API
  slug: google-cloud-platform-gcp-finops
layout: provider
modified: '2026-04-28'
name: Google Cloud Platform
nav: Providers
network: true
overview: 'Google Cloud Platform publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Cloud Computing, Data Analytics, Infrastructure-as-a-Service, Machine-Learning, and Platform-as-a-Service.


  Google Cloud Platform''s developer surface includes authentication, support, getting-started guide, developer console, and 11 more developer resources.'
plans:
- name: Google Cloud Platform Gcp Plans Pricing
  plan_count: 3
  slug: google-cloud-platform-gcp-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Google Cloud Platform Gcp Rate Limits
  slug: google-cloud-platform-gcp-rate-limits
scopes:
- name: Google Cloud Platform Gcp Scopes
  scope_count: 2
  slug: google-cloud-platform-gcp-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 29.0
    catalog_earned_first_party: 0.0
    catalog_gap: 86.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 48.8
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-platform-gcp/refs/heads/main/screenshots/google-cloud-platform-gcp-2026-06-20T182127.png
security:
- kind: authentication
  name: Google Cloud Platform Gcp Authentication
  slug: google-cloud-platform-gcp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Platform Gcp Domain Security
  slug: google-cloud-platform-gcp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: google-cloud-platform-gcp
tags:
- Cloud Computing
- Data Analytics
- Infrastructure-as-a-Service
- Machine-Learning
- Platform-as-a-Service
- Software-as-a-Service
- Serverless
website: https://cloud.google.com
---
