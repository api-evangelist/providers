---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Snowplow Agentic Access
  operation_count: 13
  slug: snowplow-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: 'Snowplow provides tracker SDKs for all major platforms including JavaScript (web), iOS, Android, Python, Java, Go, Ruby, .NET, PHP, and Rust. Trackers generate self-describing events and send them to '
  name: Snowplow Tracker SDKs
  slug: snowplow-trackers
- baseURL: https://console.snowplowanalytics.com/api/msc/v1
  baseurl_source: spec
  description: Credentials API for obtaining JWT access tokens from API key credentials.
  name: Snowplow Authentication API
  slug: snowplow-authentication-api
- baseURL: https://console.snowplowanalytics.com/api/msc/v1
  baseurl_source: spec
  description: Manage data products (tracking plans) which organize event specifications and define the behavioral data strategy for a product or feature.
  name: Snowplow Data Products API
  slug: snowplow-data-products-api
- baseURL: https://console.snowplowanalytics.com/api/msc/v1
  baseurl_source: spec
  description: Manage JSON Schema data structures (event schemas) in Snowplow. Data structures define the shape of events tracked in your pipeline. Supports versioning, validation, and deployment to dev/prod registr
  name: Snowplow Data Structures API
  slug: snowplow-data-structures-api
artifact_total: 27
collections:
- collection_type: postman
  name: Snowplow Console Authentication API
  slug: postman-snowplow-authentication-api
- collection_type: postman
  name: Snowplow Console Authentication Data Products API
  slug: postman-snowplow-data-products-api
- collection_type: postman
  name: Snowplow Console Authentication Data Structures API
  slug: postman-snowplow-data-structures-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snowplow Console Authentication API
  slug: open-snowplow-authentication-api
- collection_type: open
  name: Snowplow Console API
  slug: open-snowplow-console-api
- collection_type: open
  name: Snowplow Console Authentication Data Products API
  slug: open-snowplow-data-products-api
- collection_type: open
  name: Snowplow Console Authentication Data Structures API
  slug: open-snowplow-data-structures-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/snowplow/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snowplow-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/snowplow-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snowplow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snowplow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snowplow
- group: company
  title: ''
  type: Website
  url: https://snowplow.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snowplow.io
- group: company
  title: ''
  type: Blog
  url: https://snowplow.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://snowplow.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/snowplow
- group: start
  title: ''
  type: Login
  url: https://console.snowplowanalytics.com
- group: start
  title: ''
  type: Signup
  url: https://snowplow.io/get-started
- group: operate
  title: ''
  type: Support
  url: https://snowplow.io/support
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snowplow.io/docs/getting-started-on-snowplow-open-source
- group: operate
  title: ''
  type: Community
  url: https://discourse.snowplow.io
- group: other
  title: ''
  type: DataStructuresAPI
  url: https://docs.snowplow.io/docs/data-product-studio/data-structures/manage/api/
- group: commercial
  title: ''
  type: TrackingPlansAPI
  url: https://docs.snowplow.io/docs/data-product-studio/data-products/api/
- group: other
  title: ''
  type: CredentialsAPI
  url: https://docs.snowplow.io/docs/account-management/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.snowplow.io/llms.txt
created: '2026-03-26'
description: Snowplow is a behavioral data platform that enables organizations to collect, process, and model granular event-level data from web, mobile, and server-side sources, providing a data pipeline for analytics and AI use cases. The platform uses a schema-first approach with self-describing JSON events validated against the Iglu schema registry. The Snowplow Console API provides programmatic governance of data structures (schemas), data products (tracking plans), and event specifications.
examples:
- key_count: 4
  name: Snowplow Deploy Data Structure Example
  slug: snowplow-deploy-data-structure-example
- key_count: 4
  name: Snowplow List Data Structures Example
  slug: snowplow-list-data-structures-example
finops:
- name: Snowplow Finops
  service_category: API
  slug: snowplow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snowplow.png
json_schemas:
- name: Snowplow Data Structure
  property_count: 9
  slug: snowplow-data-structure
- name: Snowplow Event
  property_count: 30
  slug: snowplow-event
json_structures:
- name: Snowplow Pipeline Structure
  property_count: 0
  slug: snowplow-pipeline-structure
jsonld:
- class_count: 6
  name: Snowplow Context
  property_count: 30
  slug: snowplow-context
layout: provider
modified: '2026-05-19'
name: Snowplow
nav: Providers
network: true
overview: 'Snowplow publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Data Products API, and Data Structures API. Tagged areas include Analytics Platform, Behavioral Data, Data Collection, Data Engineering, and Data Pipeline.


  The Snowplow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Snowplow''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 13 more developer resources.'
plans:
- name: Snowplow Plans Pricing
  plan_count: 3
  slug: snowplow-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Snowplow Rate Limits
  slug: snowplow-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Snowplow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: snowplow-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Snowplow API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: snowplow-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 13.6
    contract_quality: 65.3
    developer_ergonomics: 39.3
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snowplow/refs/heads/main/screenshots/snowplow-2026-06-20T194113.png
security:
- kind: authentication
  name: Snowplow Authentication
  slug: snowplow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Snowplow Domain Security
  slug: snowplow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Snowplow Trust Center
  slug: snowplow-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: snowplow
tags:
- Analytics Platform
- Behavioral Data
- Data Collection
- Data Engineering
- Data Pipeline
- Event Tracking
- Open-Source
website: https://snowplow.io
---
