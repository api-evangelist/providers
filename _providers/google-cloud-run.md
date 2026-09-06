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
- acting_count: 8
  human_in_the_loop: 0
  name: Google Cloud Run Agentic Access
  operation_count: 14
  slug: google-cloud-run-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://run.googleapis.com
  baseurl_source: declared
  description: Operations for managing Cloud Run jobs
  name: Google Cloud Run Jobs API
  slug: google-cloud-run-jobs-api
- baseURL: https://run.googleapis.com
  baseurl_source: declared
  description: The Projects API from Google Cloud Run — 2 operation(s) for projects.
  name: Google Cloud Run Projects API
  slug: google-cloud-run-projects-api
- baseURL: https://run.googleapis.com
  baseurl_source: declared
  description: Operations for managing service revisions
  name: Google Cloud Run Revisions API
  slug: google-cloud-run-revisions-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Cloud Run Admin Jobs API
  slug: postman-google-cloud-run-jobs-api
- collection_type: postman
  name: Google Cloud Run Admin Jobs Projects API
  slug: postman-google-cloud-run-projects-api
- collection_type: postman
  name: Google Cloud Run Admin Jobs Revisions API
  slug: postman-google-cloud-run-revisions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Run Admin Jobs API
  slug: open-google-cloud-run-jobs-api
- collection_type: open
  name: Google Cloud Run Admin Jobs Projects API
  slug: open-google-cloud-run-projects-api
- collection_type: open
  name: Google Cloud Run Admin Jobs Revisions API
  slug: open-google-cloud-run-revisions-api
- collection_type: open
  name: Google Cloud Run Admin API
  slug: open-google-cloud-run
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-run/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-run-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-run-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-run-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-run-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-run-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/run
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/run/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/run/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/run/pricing
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
  url: https://cloud.google.com/run/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-run-context.jsonld
created: '2026-03-13'
description: Google Cloud Run is a fully managed serverless platform that enables you to run stateless containers that are invocable via HTTP requests. It abstracts away infrastructure management so you can focus on building applications.
finops:
- name: Google Cloud Run Finops
  service_category: API
  slug: google-cloud-run-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-run.png
json_schemas:
- name: Google Cloud Run Service
  property_count: 15
  slug: google-cloud-run-service
jsonld:
- class_count: 17
  name: Google Cloud Run Context
  property_count: 2
  slug: google-cloud-run-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Run
nav: Providers
network: true
overview: 'Google Cloud Run publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jobs API, Projects API, and Revisions API. Tagged areas include Cloud Run, Containers, Google Cloud, and Serverless.


  The Google Cloud Run catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Run''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Run Plans Pricing
  plan_count: 3
  slug: google-cloud-run-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Cloud Run Rate Limits
  slug: google-cloud-run-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Run API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-run-jsonschema-spectral-rules
scopes:
- name: Google Cloud Run Scopes
  scope_count: 2
  slug: google-cloud-run-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 58.3
    catalog_earned_first_party: 0.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 48.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-run/refs/heads/main/screenshots/google-cloud-run-2026-06-20T182136.png
security:
- kind: authentication
  name: Google Cloud Run Authentication
  slug: google-cloud-run-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Run Domain Security
  slug: google-cloud-run-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Run Vulnerability Disclosure
  slug: google-cloud-run-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-run
tags:
- Cloud Run
- Containers
- Google Cloud
- Serverless
website: https://cloud.google.com/run
---
