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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Google Cloud Logging Agentic Access
  operation_count: 15
  slug: google-cloud-logging-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 1
apis:
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Bucket API from Google Cloud Logging — 1 operation(s) for bucket.
  name: Google Cloud Logging Bucket API
  slug: google-cloud-logging-bucket-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Buckets API from Google Cloud Logging — 1 operation(s) for buckets.
  name: Google Cloud Logging Buckets API
  slug: google-cloud-logging-buckets-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:copy API from Google Cloud Logging — 1 operation(s) for entries:copy.
  name: Google Cloud Logging Entries:copy API
  slug: google-cloud-logging-entries-copy-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:list API from Google Cloud Logging — 1 operation(s) for entries:list.
  name: Google Cloud Logging Entries:list API
  slug: google-cloud-logging-entries-list-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:tail API from Google Cloud Logging — 1 operation(s) for entries:tail.
  name: Google Cloud Logging Entries:tail API
  slug: google-cloud-logging-entries-tail-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Entries:write API from Google Cloud Logging — 1 operation(s) for entries:write.
  name: Google Cloud Logging Entries:write API
  slug: google-cloud-logging-entries-write-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Exclusions API from Google Cloud Logging — 1 operation(s) for exclusions.
  name: Google Cloud Logging Exclusions API
  slug: google-cloud-logging-exclusions-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Google Cloud Logging API API from Google Cloud Logging — 1 operation(s) for google cloud logging api.
  name: Google Cloud Logging Google Cloud Logging API API
  slug: google-cloud-logging-google-cloud-logging-api-api
- baseURL: https://logging.googleapis.com
  baseurl_source: declared
  description: The Sinks API from Google Cloud Logging — 1 operation(s) for sinks.
  name: Google Cloud Logging Sinks API
  slug: google-cloud-logging-sinks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Logging Bucket API
  slug: open-google-cloud-logging-bucket-api
- collection_type: open
  name: Google Cloud Logging Bucket Buckets API
  slug: open-google-cloud-logging-buckets-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:copy API
  slug: open-google-cloud-logging-entries-copy-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:list API
  slug: open-google-cloud-logging-entries-list-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:tail API
  slug: open-google-cloud-logging-entries-tail-api
- collection_type: open
  name: Google Cloud Logging Bucket Entries:write API
  slug: open-google-cloud-logging-entries-write-api
- collection_type: open
  name: Google Cloud Logging Bucket Exclusions API
  slug: open-google-cloud-logging-exclusions-api
- collection_type: open
  name: Google Cloud Logging Bucket Google Cloud Logging API API
  slug: open-google-cloud-logging-google-cloud-logging-api-api
- collection_type: open
  name: Google Cloud Logging Bucket Sinks API
  slug: open-google-cloud-logging-sinks-api
- collection_type: open
  name: Google Cloud Logging API
  slug: open-google-cloud-logging
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-logging-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-logging-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-logging-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-logging-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-logging-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.google.com
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/logging/docs/quickstarts
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/operations
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloud.google.com/logging/docs/release-notes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/logging/docs
- group: operate
  title: ''
  type: RateLimits
  url: https://cloud.google.com/logging/quotas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/logs
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com
- group: start
  title: ''
  type: Login
  url: https://console.cloud.google.com/
- group: start
  title: ''
  type: Signup
  url: https://console.cloud.google.com/freetrial
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/logging/docs/reference/libraries
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/stackdriver/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-cloud-logging
- group: operate
  title: ''
  type: Issue Tracker
  url: https://cloud.google.com/support/docs/issue-trackers
- group: auth
  title: ''
  type: Security
  url: https://cloud.google.com/logging/docs/access-control
created: '2024-01-01'
description: Google Cloud Logging is a fully-managed service that performs at scale and can ingest application and system log data from thousands of VMs. Allows you to search, monitor, and analyze log data and events from Google Cloud and AWS.
finops:
- name: Google Cloud Logging Finops
  service_category: API
  slug: google-cloud-logging-finops
layout: provider
modified: '2026-04-28'
name: Google Cloud Logging
nav: Providers
network: true
overview: 'Google Cloud Logging publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bucket API, Buckets API, Entries:copy API, and 6 more. Tagged areas include Cloud, Logging, Monitoring, and Observability.


  Google Cloud Logging''s developer surface includes authentication, developer portal, getting-started guide, support, engineering blog, changelog, documentation, and 19 more developer resources.'
plans:
- name: Google Cloud Logging Plans Pricing
  plan_count: 3
  slug: google-cloud-logging-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Google Cloud Logging Rate Limits
  slug: google-cloud-logging-rate-limits
scopes:
- name: Google Cloud Logging Scopes
  scope_count: 4
  slug: google-cloud-logging-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 73.8
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-logging/refs/heads/main/screenshots/google-cloud-logging-2026-08-17T083131.png
security:
- kind: authentication
  name: Google Cloud Logging Authentication
  slug: google-cloud-logging-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Logging Domain Security
  slug: google-cloud-logging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Logging Vulnerability Disclosure
  slug: google-cloud-logging-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-logging
tags:
- Cloud
- Logging
- Monitoring
- Observability
website: https://cloud.google.com
---
