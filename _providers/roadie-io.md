---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Roadie Io Agentic Access
  operation_count: 21
  slug: roadie-io-agentic-access
  summary_line: 21 operations · 7 acting
api_count: 1
apis:
- description: Six agent-native Model Context Protocol (MCP) servers over the Roadie API - api-docs-query, backend-config, catalog-decorators, rich-catalog-entity, scaffolder-use, and tech-insights-facts - letting A
  name: Roadie MCP Servers
  slug: roadie-io-mcp-servers
- baseURL: https://api.roadie.so/api/catalog
  baseurl_source: declared
  description: Read Backstage software catalog entities in your Roadie tenant.
  name: Roadie Catalog API
  slug: roadie-io-catalog-api
- baseURL: https://api.roadie.so/api/catalog
  baseurl_source: declared
  description: Create, delete, and idempotently manage Roadie-owned catalog entities and entity sets.
  name: Roadie Entity Push API
  slug: roadie-io-entity-push-api
- baseURL: https://api.roadie.so/api/catalog
  baseurl_source: declared
  description: Backstage software templates - discover, dry-run, execute, and track scaffolder tasks.
  name: Roadie Scaffolder API
  slug: roadie-io-scaffolder-api
- baseURL: https://api.roadie.so/api/catalog
  baseurl_source: declared
  description: Facts, checks, and scorecards describing entity quality and compliance.
  name: Roadie Tech Insights API
  slug: roadie-io-tech-insights-api
- baseURL: https://api.roadie.so/api/catalog
  baseurl_source: declared
  description: Technical documentation (docs-like-code) metadata and static content. Modeled from Backstage.
  name: Roadie TechDocs API
  slug: roadie-io-techdocs-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Roadie Catalog API
  slug: open-roadie-io-catalog-api
- collection_type: open
  name: Roadie Catalog Entity Push API
  slug: open-roadie-io-entity-push-api
- collection_type: open
  name: Roadie Catalog Scaffolder API
  slug: open-roadie-io-scaffolder-api
- collection_type: open
  name: Roadie Catalog Tech Insights API
  slug: open-roadie-io-tech-insights-api
- collection_type: open
  name: Roadie Catalog TechDocs API
  slug: open-roadie-io-techdocs-api
- collection_type: open
  name: Roadie API
  slug: open-roadie-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/roadie-io-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/roadie-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roadiehq
- group: company
  title: ''
  type: Website
  url: https://roadie.io
- group: docs
  title: ''
  type: Documentation
  url: https://roadie.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/roadie-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roadie-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/roadie-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://roadie.io/blog/
created: '2026-07-11'
description: Roadie is managed Backstage - a fully hosted internal developer portal (IDP) and software catalog delivered as SaaS, so teams get the Backstage software catalog, TechDocs, Scaffolder software templates, Tech Insights scorecards, and 75+ plugins without operating Backstage themselves. Roadie exposes a public REST API under https://api.roadie.so/api (Bearer-token authenticated with User or Service tokens) for reading catalog entities, pushing Roadie-managed entities and idempotent entity sets into the software catalog, running Scaffolder templates, and querying Tech Insights facts, checks, and scorecards. Roadie also ships six agent-native MCP servers over the same API base. Backstage itself is free and open source; Roadie is the commercial managed product, priced per contributing developer. Operated by Larder Software Limited.
finops:
- name: Roadie Io Finops
  service_category: Developer Tools and Platform Engineering
  slug: roadie-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roadie-io.png
layout: provider
modified: '2026-07-11'
name: Roadie
nav: Providers
network: true
overview: 'Roadie publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Entity Push API, Scaffolder API, and 2 more. Tagged areas include Software Catalog, Internal Developer Portal, Backstage, Developer Experience, and IDP.


  Roadie''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Roadie Io Plans Pricing
  plan_count: 3
  slug: roadie-io-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Roadie Io Rate Limits
  slug: roadie-io-rate-limits
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 44.6
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roadie-io/refs/heads/main/screenshots/roadie-io-2026-09-02T153952.png
security:
- kind: authentication
  name: Roadie Io Authentication
  slug: roadie-io-authentication
  summary_line: http · 1 scheme
slug: roadie-io
tags:
- Software Catalog
- Internal Developer Portal
- Backstage
- Developer Experience
- IDP
- Developer Portal
- Managed Backstage
- Scaffolder
- TechDocs
- Service Catalog
- Platform Engineering
website: https://roadie.io
---
