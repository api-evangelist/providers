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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Data Catalog Agentic Access
  operation_count: 10
  slug: google-cloud-data-catalog-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Search operations across the catalog
  name: Google Cloud Data Catalog Catalog API
  slug: google-cloud-data-catalog-catalog-api
- description: Operations for managing catalog entries
  name: Google Cloud Data Catalog Entries API
  slug: google-cloud-data-catalog-entries-api
- description: Operations for managing entry groups
  name: Google Cloud Data Catalog EntryGroups API
  slug: google-cloud-data-catalog-entrygroups-api
- description: Operations for managing tag templates
  name: Google Cloud Data Catalog TagTemplates API
  slug: google-cloud-data-catalog-tagtemplates-api
artifact_total: 25
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-data-catalog/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-data-catalog-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-data-catalog-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-data-catalog-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-data-catalog-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-data-catalog-context.jsonld
created: '2026-03-13'
description: Google Cloud Data Catalog is a fully managed, scalable metadata management service that helps organizations discover, understand, and manage their data. It provides a unified view of data assets across Google Cloud and allows users to search, tag, and classify data resources.
finops:
- name: Google Cloud Data Catalog Finops
  service_category: API
  slug: google-cloud-data-catalog-finops
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
modified: '2026-05-19'
name: Google Cloud Data Catalog
nav: Providers
network: true
overview: 'Google Cloud Data Catalog publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Entries API, EntryGroups API, and 1 more. Tagged areas include Data Catalog, Data Governance, Google Cloud, and Metadata.


  The Google Cloud Data Catalog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Data Catalog''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Data Catalog Plans Pricing
  plan_count: 3
  slug: google-cloud-data-catalog-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Google Cloud Data Catalog Rate Limits
  slug: google-cloud-data-catalog-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Data Catalog API Rules
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
  composite: 44.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-data-catalog/refs/heads/main/screenshots/google-cloud-data-catalog-2026-06-20T182058.png
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
website: https://cloud.google.com/data-catalog
---
