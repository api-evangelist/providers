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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Datastream Agentic Access
  operation_count: 11
  slug: google-cloud-datastream-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://datastream.googleapis.com
  baseurl_source: declared
  description: Operations for managing connection profiles
  name: Google Cloud Datastream ConnectionProfiles API
  slug: google-cloud-datastream-connectionprofiles-api
- baseURL: https://datastream.googleapis.com
  baseurl_source: declared
  description: Long-running operation management
  name: Google Cloud Datastream Operations API
  slug: google-cloud-datastream-operations-api
- baseURL: https://datastream.googleapis.com
  baseurl_source: declared
  description: Operations for managing replication streams
  name: Google Cloud Datastream Streams API
  slug: google-cloud-datastream-streams-api
artifact_total: 24
asyncapis:
- description: Google Cloud Datastream is a serverless change data capture (CDC) and replication service that streams change events from supported source databases and applications into Google Cloud destinations. Th
  name: Google Cloud Datastream CDC Events
  slug: google-cloud-datastream-asyncapi
collections:
- collection_type: postman
  name: Google Cloud Datastream ConnectionProfiles API
  slug: postman-google-cloud-datastream-connectionprofiles-api
- collection_type: postman
  name: Google Cloud Datastream ConnectionProfiles Operations API
  slug: postman-google-cloud-datastream-operations-api
- collection_type: postman
  name: Google Cloud Datastream ConnectionProfiles Streams API
  slug: postman-google-cloud-datastream-streams-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Datastream ConnectionProfiles API
  slug: open-google-cloud-datastream-connectionprofiles-api
- collection_type: open
  name: Google Cloud Datastream ConnectionProfiles Operations API
  slug: open-google-cloud-datastream-operations-api
- collection_type: open
  name: Google Cloud Datastream ConnectionProfiles Streams API
  slug: open-google-cloud-datastream-streams-api
- collection_type: open
  name: Google Cloud Datastream API
  slug: open-google-cloud-datastream
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-datastream/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-datastream-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-datastream-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-datastream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-datastream-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-datastream-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/datastream
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/datastream/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/datastream/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/datastream/pricing
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
  url: https://cloud.google.com/datastream/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-datastream-context.jsonld
created: '2026-03-13'
description: Google Cloud Datastream is a serverless change data capture (CDC) and replication service that allows you to synchronize data across heterogeneous databases, storage systems, and applications reliably and with minimal latency.
finops:
- name: Google Cloud Datastream Finops
  service_category: API
  slug: google-cloud-datastream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-datastream.png
json_schemas:
- name: Google Cloud Datastream Stream
  property_count: 9
  slug: google-cloud-datastream-stream
jsonld:
- class_count: 13
  name: Google Cloud Datastream Context
  property_count: 2
  slug: google-cloud-datastream-context
layout: provider
modified: '2026-05-30'
name: Google Cloud Datastream
nav: Providers
network: true
overview: 'Google Cloud Datastream publishes 3 APIs on the [APIs.io](https://apis.io/) network: ConnectionProfiles API, Operations API, and Streams API. Tagged areas include Change Data Capture, Data Replication, Google Cloud, and Streaming.


  The Google Cloud Datastream catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Google Cloud Datastream''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Datastream Plans Pricing
  plan_count: 3
  slug: google-cloud-datastream-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google Cloud Datastream Rate Limits
  slug: google-cloud-datastream-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Google Cloud Datastream API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: google-cloud-datastream-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Google Cloud Datastream API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-datastream-jsonschema-spectral-rules
scopes:
- name: Google Cloud Datastream Scopes
  scope_count: 1
  slug: google-cloud-datastream-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 59.5
    catalog_earned_first_party: 0.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 71.1
    developer_ergonomics: 48.8
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 48.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-datastream/refs/heads/main/screenshots/google-cloud-datastream-2026-06-20T182105.png
security:
- kind: authentication
  name: Google Cloud Datastream Authentication
  slug: google-cloud-datastream-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Datastream Domain Security
  slug: google-cloud-datastream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Datastream Vulnerability Disclosure
  slug: google-cloud-datastream-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-datastream
tags:
- Change Data Capture
- Data Replication
- Google Cloud
- Streaming
website: https://cloud.google.com/datastream
---
