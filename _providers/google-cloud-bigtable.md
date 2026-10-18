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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Bigtable Agentic Access
  operation_count: 10
  slug: google-cloud-bigtable-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://bigtableadmin.googleapis.com/v2
  baseurl_source: declared
  description: Operations on Bigtable clusters within instances
  name: Google Cloud Bigtable Clusters API
  slug: google-cloud-bigtable-clusters-api
- baseURL: https://bigtableadmin.googleapis.com/v2
  baseurl_source: declared
  description: Operations on Bigtable instances
  name: Google Cloud Bigtable Instances API
  slug: google-cloud-bigtable-instances-api
- baseURL: https://bigtableadmin.googleapis.com/v2
  baseurl_source: declared
  description: Operations on Bigtable tables
  name: Google Cloud Bigtable Tables API
  slug: google-cloud-bigtable-tables-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Cloud Bigtable Admin Clusters API
  slug: postman-google-cloud-bigtable-clusters-api
- collection_type: postman
  name: Google Cloud Bigtable Admin Clusters Instances API
  slug: postman-google-cloud-bigtable-instances-api
- collection_type: postman
  name: Google Cloud Bigtable Admin Clusters Tables API
  slug: postman-google-cloud-bigtable-tables-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Bigtable Admin API
  slug: open-cloud-bigtable
- collection_type: open
  name: Google Cloud Bigtable Admin Clusters API
  slug: open-google-cloud-bigtable-clusters-api
- collection_type: open
  name: Google Cloud Bigtable Admin Clusters Instances API
  slug: open-google-cloud-bigtable-instances-api
- collection_type: open
  name: Google Cloud Bigtable Admin Clusters Tables API
  slug: open-google-cloud-bigtable-tables-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/plans/google-cloud-bigtable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-bigtable-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/rate-limits/google-cloud-bigtable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-bigtable-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/finops/google-cloud-bigtable-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-bigtable-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/capabilities/google-cloud-bigtable-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-bigtable-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-bigtable/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/agentic-access/google-cloud-bigtable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-bigtable-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/security/google-cloud-bigtable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-bigtable-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/security/google-cloud-bigtable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-bigtable-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/authentication/google-cloud-bigtable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-bigtable-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/scopes/google-cloud-bigtable-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-bigtable-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/bigtable
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/bigtable/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/bigtable/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/bigtable/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/bigtable/pricing
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
  url: https://cloud.google.com/bigtable/docs/support
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/json-ld/google-cloud-bigtable-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-bigtable-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/bigtable-release-notes.xml
created: '2026-03-13'
description: Google Cloud Bigtable is a fully managed, scalable NoSQL database service designed for large analytical and operational workloads. It offers consistent sub-10ms latency and seamless scalability, making it ideal for time-series data, IoT, ad tech, fintech, and machine learning applications. Bigtable integrates with popular big data tools like Hadoop, Dataflow, and Dataproc.
finops:
- has_sources: false
  method: generated
  name: Google Cloud Bigtable Finops
  primary_unit: ''
  service_category: API
  slug: google-cloud-bigtable-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-bigtable.png
json_schemas:
- name: Google Cloud Bigtable Instance
  property_count: 7
  slug: instance
jsonld:
- class_count: 16
  name: Google Cloud Bigtable Context
  property_count: 0
  slug: google-cloud-bigtable-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Bigtable
nav: Providers
network: true
overview: 'Google Cloud Bigtable publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Clusters API, Instances API, and Tables API. Tagged areas include Bigtable, Database, Google Cloud, NoSQL, and Wide Column.


  The Google Cloud Bigtable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Bigtable''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Google Cloud Bigtable Plans Pricing
  plan_count: 3
  slug: google-cloud-bigtable-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Google Cloud Bigtable Rate Limits
  slug: google-cloud-bigtable-rate-limits
rules:
- authorship: generated
  effective_rule_count: 4
  extends: []
  name: Google Cloud Bigtable — jsonschema rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-cloud-bigtable-jsonschema-spectral-rules
scopes:
- name: Google Cloud Bigtable Scopes
  scope_count: 3
  slug: google-cloud-bigtable-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.7
    catalog_earned_first_party: 0.0
    catalog_gap: 55.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 59.3
    developer_ergonomics: 51.2
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/screenshots/google-cloud-bigtable-2026-06-20T182046.png
security:
- kind: authentication
  name: Google Cloud Bigtable Authentication
  slug: google-cloud-bigtable-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Bigtable Domain Security
  slug: google-cloud-bigtable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Bigtable Vulnerability Disclosure
  slug: google-cloud-bigtable-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-bigtable
tags:
- Bigtable
- Database
- Google Cloud
- NoSQL
- Wide Column
website: https://www.google.com/
---
