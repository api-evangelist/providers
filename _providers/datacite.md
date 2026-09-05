---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
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
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Datacite Agentic Access
  operation_count: 42
  slug: datacite-agentic-access
  summary_line: 42 operations · 14 acting
api_count: 2
apis:
- description: 'An alternative query interface for DOI metadata retrieval using the GraphQL query language. Currently supports queries only (no mutations or subscriptions). Publicly accessible without authentication '
  name: DataCite GraphQL API
  slug: datacite-graphql-api
- description: Tracks mentions, citations, and scholarly events related to registered DOIs. Enables discovery of how research outputs are referenced and linked across the scholarly web.
  name: DataCite Event Data API
  slug: datacite-event-data-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Activities
  name: DataCite activities API
  slug: datacite-activities-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Client Prefixes
  name: DataCite client-prefixes API
  slug: datacite-client-prefixes-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Clients
  name: DataCite clients API
  slug: datacite-clients-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: DOIs
  name: DataCite dois API
  slug: datacite-dois-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Events
  name: DataCite events API
  slug: datacite-events-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Heartbeat
  name: DataCite heartbeat API
  slug: datacite-heartbeat-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Prefixes
  name: DataCite prefixes API
  slug: datacite-prefixes-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Provider Prefixes
  name: DataCite provider-prefixes API
  slug: datacite-provider-prefixes-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Providers
  name: DataCite providers API
  slug: datacite-providers-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: The publishers API from DataCite — 2 operation(s) for publishers.
  name: DataCite publishers API
  slug: datacite-publishers-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: The report_types API from DataCite — 1 operation(s) for report_types.
  name: DataCite report_types API
  slug: datacite-report-types-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: Reports
  name: DataCite reports API
  slug: datacite-reports-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: The repositories API from DataCite — 2 operation(s) for repositories.
  name: DataCite repositories API
  slug: datacite-repositories-api
- baseURL: https://api.datacite.org
  baseurl_source: declared
  description: The status API from DataCite — 1 operation(s) for status.
  name: DataCite status API
  slug: datacite-status-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REST activities API
  slug: open-datacite-activities-api
- collection_type: open
  name: REST activities client-prefixes API
  slug: open-datacite-client-prefixes-api
- collection_type: open
  name: REST activities clients API
  slug: open-datacite-clients-api
- collection_type: open
  name: REST activities dois API
  slug: open-datacite-dois-api
- collection_type: open
  name: REST activities events API
  slug: open-datacite-events-api
- collection_type: open
  name: REST activities heartbeat API
  slug: open-datacite-heartbeat-api
- collection_type: open
  name: REST activities prefixes API
  slug: open-datacite-prefixes-api
- collection_type: open
  name: REST activities provider-prefixes API
  slug: open-datacite-provider-prefixes-api
- collection_type: open
  name: REST activities providers API
  slug: open-datacite-providers-api
- collection_type: open
  name: REST activities publishers API
  slug: open-datacite-publishers-api
- collection_type: open
  name: REST activities report_types API
  slug: open-datacite-report-types-api
- collection_type: open
  name: REST activities reports API
  slug: open-datacite-reports-api
- collection_type: open
  name: REST activities repositories API
  slug: open-datacite-repositories-api
- collection_type: open
  name: REST activities status API
  slug: open-datacite-status-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/datacite-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datacite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datacite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datacite-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://datacite.org
- group: docs
  title: ''
  type: Documentation
  url: https://support.datacite.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datacite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datacite/
- group: company
  title: ''
  type: Blog
  url: https://datacite.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://datacite.org/fees/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datacite.org/
- group: other
  title: ''
  type: X
  url: https://x.com/DataCite
- group: other
  title: ''
  type: BestPractices
  url: https://support.datacite.org/docs/best-practices-for-integrators
- group: other
  title: ''
  type: UpcomingChanges
  url: https://support.datacite.org/docs/upcoming-changes
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/datacite-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/datacite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datacite-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datacite-finops.yml
created: '2026-06-12'
description: DataCite is a leading global non-profit organization that provides DOI (Digital Object Identifier) registration and persistent identifier services for research outputs, enabling researchers to cite, discover, and access scholarly data. DataCite maintains a REST API for minting and managing DOIs, querying metadata records, and accessing the global research data graph. Membership-based access allows institutions to register DOIs through APIs and the Fabrica web interface, while public metadata retrieval is freely available to anyone. DataCite also offers a GraphQL API, a legacy Metadata Store (MDS) API, usage statistics via its Usage Reports API, and scholarly event tracking via the Event Data API.
finops:
- name: Datacite Finops
  service_category: ''
  slug: datacite-finops
graphqls:
- description: The DataCite GraphQL API provides a flexible query interface for retrieving DOI metadata and the broader research knowledge graph. It exposes the full DataCite metadata model through a typed schema, e
  name: DataCite GraphQL API
  slug: datacite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datacite.png
jsonld:
- class_count: 32
  name: Datacite Context
  property_count: 9
  slug: datacite-context
layout: provider
modified: '2026-06-12'
name: DataCite
nav: Providers
network: true
overview: 'DataCite publishes 14 APIs on the [APIs.io](https://apis.io/) network, including activities API, client-prefixes API, clients API, and 11 more. Tagged areas include DOI, Persistent Identifiers, Scholarly Metadata, Research Data, and Open Science.


  The DataCite catalog on APIs.io includes 1 JSON-LD context.


  DataCite''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Datacite Plans Pricing
  plan_count: 6
  slug: datacite-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Datacite Rate Limits
  slug: datacite-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 72.0
    catalog_earned_first_party: 0.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 61.2
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datacite/refs/heads/main/screenshots/datacite-2026-06-20T175634.png
security:
- kind: authentication
  name: Datacite Authentication
  slug: datacite-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Datacite Domain Security
  slug: datacite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datacite
tags:
- DOI
- Persistent Identifiers
- Scholarly Metadata
- Research Data
- Open Science
- Linked Data
website: https://datacite.org
---
