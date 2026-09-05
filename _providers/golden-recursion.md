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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Golden Recursion Agentic Access
  operation_count: 8
  slug: golden-recursion-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://golden.com/api/v2/public
  baseurl_source: declared
  description: The Entity API API from Golden Recursion — 2 operation(s) for entity api.
  name: Golden Recursion Entity API API
  slug: golden-recursion-entity-api-api
- baseURL: https://golden.com/api/v2/public
  baseurl_source: declared
  description: The Query API API from Golden Recursion — 2 operation(s) for query api.
  name: Golden Recursion Query API API
  slug: golden-recursion-query-api-api
- baseURL: https://golden.com/api/v2/public
  baseurl_source: declared
  description: The Schema API API from Golden Recursion — 4 operation(s) for schema api.
  name: Golden Recursion Schema API API
  slug: golden-recursion-schema-api-api
arazzos:
- description: Introspect the predicate schema, search entities by type, then retrieve the full cited entity.
  name: Golden — discover schema then enrich an entity
  slug: golden-recursion-enrich-entity
- description: Resolve a saved Golden query by its permalink and page through its entity results.
  name: Golden — run a saved query by permalink
  slug: golden-recursion-saved-query
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Golden API v2 Entity API API
  slug: open-golden-recursion-entity-api-api
- collection_type: open
  name: Golden API v2 Entity API Query API API
  slug: open-golden-recursion-query-api-api
- collection_type: open
  name: Golden API v2 Entity API Schema API API
  slug: open-golden-recursion-schema-api-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://golden.com/product/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.golden.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.golden.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://golden.com/product/api
- group: operate
  title: ''
  type: Support
  url: https://goldenhq.notion.site/goldenhq/Golden-Guide-1eef7518f3ca43da8d6ee4d54307801b
- group: operate
  title: ''
  type: HelpCenter
  url: https://goldenhq.notion.site/goldenhq/Golden-Guide-1eef7518f3ca43da8d6ee4d54307801b
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goldenrecursion
- group: commercial
  title: ''
  type: Pricing
  url: https://golden.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://golden.com/signup
- group: start
  title: ''
  type: Login
  url: https://golden.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://golden.com/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://golden.com/about/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/golden-recursion-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/golden-recursion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/golden-recursion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/golden-recursion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/golden-recursion-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/golden-recursion-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/golden-recursion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/golden-recursion-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/golden-recursion-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/golden-recursion-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/golden-recursion-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/golden-recursion-enrich-entity.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/golden-recursion-saved-query.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/golden-recursion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golden-recursion-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/golden-recursion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/golden-recursion-rate-limits.yml
created: '2026-07-17'
description: 'Golden Recursion Inc. builds Golden, a San Francisco company using machine intelligence to construct a self-building knowledge graph of millions of connected entities — companies, people, venture-capital firms and products — each described by structured, cited properties. The Golden API v2 gives developers read-only, programmatic access to the same data that powers the Golden Query Tool: retrieve entities and their cited properties, pull the results of saved queries by ID or permalink, and introspect the entity-type and predicate schema. Responses are structured JSON with underlying source citations so every value can be traced. Authentication is a simple apikey header. Golden also published godel, an open-source Python SDK for its separate golden.xyz protocol GraphQL API. Backed by a16z ($59.5M raised); Golden was acquired by ComplyAdvantage on 2024-04-24 and golden.com now serves an acquisition notice, though the API v2 endpoints and the Scalar API reference at docs.golden.com
  remain live and were re-verified 2026-08-14.'
image: https://golden.com/static/images/38d57130206f78fb48c9.png
layout: provider
modified: '2026-08-14'
name: Golden Recursion
nav: Providers
network: true
overview: 'Golden Recursion publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entity API API, Query API API, and Schema API API. Tagged areas include Company, Knowledge Graph, Data Enrichment, Entity Data, and Company Data.


  Golden Recursion''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Golden Recursion Plans Pricing
  plan_count: 4
  slug: golden-recursion-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Golden Recursion Rate Limits
  slug: golden-recursion-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/golden-recursion/refs/heads/main/screenshots/golden-recursion-2026-07-25T220029.png
security:
- kind: authentication
  name: Golden Recursion Authentication
  slug: golden-recursion-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Golden Recursion Domain Security
  slug: golden-recursion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: golden-recursion
tags:
- Company
- Knowledge Graph
- Data Enrichment
- Entity Data
- Company Data
- Artificial Intelligence
- Semantic Web
- Data
website: https://golden.com/product/api
---
