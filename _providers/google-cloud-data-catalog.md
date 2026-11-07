---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Data Catalog Agentic Access
  operation_count: 10
  slug: google-cloud-data-catalog-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://datacatalog.googleapis.com
  baseurl_source: declared
  description: Search operations across the catalog
  name: Google Cloud Data Catalog API
  slug: google-cloud-data-catalog-catalog-api
- baseURL: https://datacatalog.googleapis.com
  baseurl_source: declared
  description: Operations for managing catalog entries
  name: Google Cloud Data Catalog Entries API
  slug: google-cloud-data-catalog-entries-api
- baseURL: https://datacatalog.googleapis.com
  baseurl_source: declared
  description: Operations for managing entry groups
  name: Google Cloud Data Catalog EntryGroups API
  slug: google-cloud-data-catalog-entrygroups-api
- baseURL: https://datacatalog.googleapis.com
  baseurl_source: declared
  description: Operations for managing tag templates
  name: Google Cloud Data Catalog TagTemplates API
  slug: google-cloud-data-catalog-tagtemplates-api
artifact_total: 24
collections:
- collection_type: postman
  name: Google Cloud Data Catalog API
  slug: postman-google-cloud-data-catalog-catalog-api
- collection_type: postman
  name: Google Cloud Data Catalog Entries API
  slug: postman-google-cloud-data-catalog-entries-api
- collection_type: postman
  name: Google Cloud Data Catalog EntryGroups API
  slug: postman-google-cloud-data-catalog-entrygroups-api
- collection_type: postman
  name: Google Cloud Data Catalog TagTemplates API
  slug: postman-google-cloud-data-catalog-tagtemplates-api
- collection_type: open
  name: Google Cloud Data Catalog API
  slug: open-google-cloud-data-catalog-catalog-api
- collection_type: open
  name: Google Cloud Data Catalog Entries API
  slug: open-google-cloud-data-catalog-entries-api
- collection_type: open
  name: Google Cloud Data Catalog EntryGroups API
  slug: open-google-cloud-data-catalog-entrygroups-api
- collection_type: open
  name: Google Cloud Data Catalog TagTemplates API
  slug: open-google-cloud-data-catalog-tagtemplates-api
- collection_type: open
  name: Google Cloud Data Catalog API
  slug: open-google-cloud-data-catalog
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-data-catalog/plans/google-cloud-data-catalog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-data-catalog-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-data-catalog/rate-limits/google-cloud-data-catalog-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-data-catalog-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-data-catalog/finops/google-cloud-data-catalog-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-data-catalog-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-data-catalog/capabilities/google-cloud-data-catalog-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-data-catalog-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-data-catalog/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-data-catalog/agentic-access/google-cloud-data-catalog-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-data-catalog-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-data-catalog/security/google-cloud-data-catalog-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-data-catalog-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-data-catalog/security/google-cloud-data-catalog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-data-catalog-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-data-catalog/authentication/google-cloud-data-catalog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-data-catalog-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-data-catalog/scopes/google-cloud-data-catalog-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-data-catalog-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/data-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/data-catalog/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/data-catalog/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/data-catalog/docs/concepts/iam
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/data-catalog/pricing
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
  url: https://cloud.google.com/data-catalog/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-data-catalog/json-ld/google-cloud-data-catalog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-data-catalog-context.jsonld
created: '2026-03-13'
description: Google Cloud Data Catalog is a fully managed, scalable metadata management service that helps organizations discover, understand, and manage their data. It provides a unified view of data assets across Google Cloud and allows users to search, tag, and classify data resources.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Data Catalog Finops
  primary_unit: dcu per unit time
  service_category: ''
  slug: google-cloud-data-catalog-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-data-catalog.png
json_schemas:
- name: Google Cloud Data Catalog Entry
  property_count: 10
  slug: google-cloud-data-catalog-entry
jsonld:
- class_count: 12
  name: Google Cloud Data Catalog Context
  property_count: 1
  slug: google-cloud-data-catalog-context
layout: provider
modified: '2026-09-16'
name: Google Cloud Data Catalog
nav: Providers
network: true
overview: 'Google Cloud Data Catalog publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Entries API, EntryGroups API, and 2 more. Tagged areas include Data Catalog, Data Governance, Google Cloud, and Metadata.


  The Google Cloud Data Catalog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Data Catalog''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Google Cloud Data Catalog Plans Pricing
  plan_count: 8
  slug: google-cloud-data-catalog-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Google Cloud Data Catalog Rate Limits
  slug: google-cloud-data-catalog-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Data Catalog — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-data-catalog-jsonschema-spectral-rules
scopes:
- name: Google Cloud Data Catalog Scopes
  scope_count: 1
  slug: google-cloud-data-catalog-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.7
    catalog_earned_first_party: 12.0
    catalog_gap: 48.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 58.1
    developer_ergonomics: 36.9
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-data-catalog/google-cloud-data-catalog-2026-06-20T182058.png
security:
- kind: authentication
  name: Google Cloud Data Catalog Authentication
  slug: google-cloud-data-catalog-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Data Catalog Domain Security
  slug: google-cloud-data-catalog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Data Catalog Vulnerability Disclosure
  slug: google-cloud-data-catalog-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-data-catalog
tags:
- Data Catalog
- Data Governance
- Google Cloud
- Metadata
website: https://www.google.com/
---
