---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Datacite Agentic Access
  operation_count: 42
  slug: datacite-agentic-access
  summary_line: 42 operations · 14 acting
api_count: 16
apis:
- description: 'An alternative query interface for DOI metadata retrieval using the GraphQL query language. Currently supports queries only (no mutations or subscriptions). Publicly accessible without authentication '
  name: DataCite GraphQL API
  slug: datacite-graphql-api
- description: Tracks mentions, citations, and scholarly events related to registered DOIs. Enables discovery of how research outputs are referenced and linked across the scholarly web.
  name: DataCite Event Data API
  slug: datacite-event-data-api
- description: Activities
  name: DataCite activities API
  slug: datacite-activities-api
- description: Client Prefixes
  name: DataCite client-prefixes API
  slug: datacite-client-prefixes-api
- description: Clients
  name: DataCite clients API
  slug: datacite-clients-api
- description: DOIs
  name: DataCite dois API
  slug: datacite-dois-api
- description: Events
  name: DataCite events API
  slug: datacite-events-api
- description: Heartbeat
  name: DataCite heartbeat API
  slug: datacite-heartbeat-api
- description: Prefixes
  name: DataCite prefixes API
  slug: datacite-prefixes-api
- description: Provider Prefixes
  name: DataCite provider-prefixes API
  slug: datacite-provider-prefixes-api
- description: Providers
  name: DataCite providers API
  slug: datacite-providers-api
- description: The publishers API from DataCite — 2 operation(s) for publishers.
  name: DataCite publishers API
  slug: datacite-publishers-api
- description: The report_types API from DataCite — 1 operation(s) for report_types.
  name: DataCite report_types API
  slug: datacite-report-types-api
- description: Reports
  name: DataCite reports API
  slug: datacite-reports-api
- description: The repositories API from DataCite — 2 operation(s) for repositories.
  name: DataCite repositories API
  slug: datacite-repositories-api
- description: The status API from DataCite — 1 operation(s) for status.
  name: DataCite status API
  slug: datacite-status-api
artifact_total: 24
common:
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


  DataCite''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Datacite Plans Pricing
  plan_count: 6
  slug: datacite-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Datacite Rate Limits
  slug: datacite-rate-limits
score:
  band: developing
  composite: 44.0
  delta: -1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.6
  scored_at: '2026-07-28'
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
