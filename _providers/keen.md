---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Keen Agentic Access
  operation_count: 27
  slug: keen-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 3
apis:
- description: The Keen Cached Queries API allows developers to create, manage, and retrieve pre-defined queries that are automatically refreshed on a schedule. Cached queries improve performance for frequently acce
  name: Keen Cached Queries API
  slug: cached-queries-api
- description: The Keen Saved Queries API enables developers to create and manage reusable query definitions. Saved queries store query parameters as named resources that can be retrieved and executed later, enablin
  name: Keen Saved Queries API
  slug: saved-queries-api
- description: Inspect event collection schemas and properties for a project.
  name: Keen Collections API
  slug: keen-collections-api
- description: Record and inspect events stored in Keen event collections.
  name: Keen Events API
  slug: keen-events-api
- description: Extract raw event data from Keen event collections.
  name: Keen Extractions API
  slug: keen-extractions-api
- description: Run analytical queries against Keen event collections.
  name: Keen Queries API
  slug: keen-queries-api
artifact_total: 35
collections:
- collection_type: postman
  name: Keen Cached Queries API
  slug: postman-keen-cached-queries-api
- collection_type: postman
  name: Keen Cached Queries Collections API
  slug: postman-keen-collections-api
- collection_type: postman
  name: Keen Cached Queries Events API
  slug: postman-keen-events-api
- collection_type: postman
  name: Keen Cached Queries Extractions API
  slug: postman-keen-extractions-api
- collection_type: postman
  name: Keen Cached Queries API
  slug: postman-keen-queries-api
- collection_type: postman
  name: Keen Cached Queries Saved Queries API
  slug: postman-keen-saved-queries-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Keen Cached Queries API
  slug: open-keen-cached-queries-api
- collection_type: open
  name: Keen Cached Queries Collections API
  slug: open-keen-collections-api
- collection_type: open
  name: Keen Data Extraction API
  slug: open-keen-data-extraction-api
- collection_type: open
  name: Keen Event Collection API
  slug: open-keen-event-collection-api
- collection_type: open
  name: Keen Cached Queries Events API
  slug: open-keen-events-api
- collection_type: open
  name: Keen Cached Queries Extractions API
  slug: open-keen-extractions-api
- collection_type: open
  name: Keen Cached Queries API
  slug: open-keen-queries-api
- collection_type: open
  name: Keen Query API
  slug: open-keen-query-api
- collection_type: open
  name: Keen Cached Queries Saved Queries API
  slug: open-keen-saved-queries-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/keen/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keen-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keen-io
- group: company
  title: ''
  type: Website
  url: https://keen.io
- group: docs
  title: ''
  type: Documentation
  url: https://keen.io/docs
- group: docs
  title: ''
  type: APIDocumentation
  url: https://keen.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://keen.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://keen.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://keen.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/keen
- group: start
  title: ''
  type: Login
  url: https://keen.io/login
- group: start
  title: ''
  type: Signup
  url: https://keen.io/signup
- group: operate
  title: ''
  type: Support
  url: https://keen.io/support
- group: build
  title: ''
  type: SDKs
  url: https://keen.io/docs/sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keen.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keen.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keen.io/privacy-policy
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-03-26'
description: Keen is an event analytics platform and API that enables developers to collect, store, analyze, and visualize custom event data. It provides a flexible RESTful API for streaming events, running multi-dimensional queries, and building embedded analytics dashboards for products and internal tools.
finops:
- name: Keen Finops
  service_category: Analytics
  slug: keen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keen.png
json_schemas:
- name: CachedQuery
  property_count: 0
  slug: keen-cachedquery
- name: CachedQueryDefinition
  property_count: 2
  slug: keen-cachedquerydefinition
- name: Error
  property_count: 2
  slug: keen-error
- name: SavedQuery
  property_count: 0
  slug: keen-savedquery
- name: SavedQueryDefinition
  property_count: 2
  slug: keen-savedquerydefinition
json_structures:
- name: Keen Structure
  property_count: 0
  slug: keen-structure
layout: provider
modified: '2026-08-08'
name: Keen
nav: Providers
network: true
overview: 'Keen publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cached Queries API, Saved Queries API, Collections API, and 3 more. Tagged areas include Analytics, Custom Events, Data Collection, Embedded Analytics, and Event Analytics.


  The Keen catalog on APIs.io includes 1 Spectral governance ruleset.


  Keen''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, GitHub presence, signup flow, and 13 more developer resources.'
plans:
- name: Keen Plans Pricing
  plan_count: 4
  slug: keen-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 13
  name: Keen Rate Limits
  slug: keen-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Keen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: keen-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 67.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 59.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keen/refs/heads/main/screenshots/keen-2026-06-20T183939.png
security:
- kind: authentication
  name: Keen Authentication
  slug: keen-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keen Domain Security
  slug: keen-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: keen
tags:
- Analytics
- Custom Events
- Data Collection
- Embedded Analytics
- Event Analytics
website: https://keen.io
---
