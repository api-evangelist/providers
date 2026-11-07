---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Cognee Agentic Access
  operation_count: 22
  slug: cognee-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Knowledge graph construction pipeline
  name: Cognee Cognify API
  slug: cognee-cognify-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Dataset management and introspection
  name: Cognee Datasets API
  slug: cognee-datasets-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Service health probes
  name: Cognee Health API
  slug: cognee-health-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Semantic and graph search queries
  name: Cognee Search API
  slug: cognee-search-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: System configuration (LLM and vector DB)
  name: Cognee Settings API
  slug: cognee-settings-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Activity endpoints for inspecting pipeline runs, traced spans, tenant users, agents, and dataset exports.
  name: Cognee Activity API
  slug: cognee-activity-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Data ingestion endpoints for adding text, files, and structured data.
  name: Cognee Add API
  slug: cognee-add-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for registering, unregistering, and inspecting agent connections to the instance.
  name: Cognee agent connections API
  slug: cognee-agent-connections-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for creating, listing, retrieving, and deleting agents.
  name: Cognee agent management API
  slug: cognee-agent-management-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Authentication endpoints for user registration, login, and token management.
  name: Cognee Auth API
  slug: cognee-auth-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Diagnostic endpoint for validating a Cognee Cloud API key supplied in the X-Api-Key header.
  name: Cognee Checks API
  slug: cognee-checks-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for storing, retrieving, and listing a user's saved configurations.
  name: Cognee Configuration API
  slug: cognee-configuration-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Data deletion endpoints (deprecated — use datasets endpoints instead).
  name: Cognee Delete API
  slug: cognee-delete-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoint for removing data from the knowledge graph.
  name: Cognee Forget API
  slug: cognee-forget-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoint for enriching and improving an existing knowledge graph.
  name: Cognee Improve API
  slug: cognee-improve-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for connecting, provisioning, and disconnecting OAuth providers and plugins.
  name: Cognee Integrations API
  slug: cognee-integrations-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: LLM-backed endpoints for inferring graph schemas and generating custom extraction prompts.
  name: Cognee Llm API
  slug: cognee-llm-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoint for running enrichment pipelines over existing graphs or supplied data.
  name: Cognee Memify API
  slug: cognee-memify-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for uploading, listing, and deleting ontology files used during cognify.
  name: Cognee Ontologies API
  slug: cognee-ontologies-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Permission management for multi-user access control.
  name: Cognee Permissions API
  slug: cognee-permissions-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for querying the knowledge graph and reviewing past recall history.
  name: Cognee Recall API
  slug: cognee-recall-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for ingesting data into the knowledge graph and storing session memory entries.
  name: Cognee Remember API
  slug: cognee-remember-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Response generation endpoints using the knowledge graph.
  name: Cognee Responses API
  slug: cognee-responses-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Schema inspection endpoints for a dataset's derived schema inventory and the caller-wide memory provenance graph.
  name: Cognee Schema API
  slug: cognee-schema-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for listing sessions and reporting usage, cost, and token statistics.
  name: Cognee Sessions API
  slug: cognee-sessions-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Skill management endpoints for ingesting, listing, retrieving, and deleting dataset skills, plus read-only retrieval of improvement proposals.
  name: Cognee Skills API
  slug: cognee-skills-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for listing workspace channels, setting channel allowlists, and linking Slack accounts.
  name: Cognee Slack API
  slug: cognee-slack-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoints for syncing local data to Cognee Cloud and checking sync status.
  name: Cognee Sync API
  slug: cognee-sync-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Endpoint for updating existing data in a dataset.
  name: Cognee Update API
  slug: cognee-update-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: User management endpoints.
  name: Cognee Users API
  slug: cognee-users-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Diagnostic endpoint for checking consistency between a dataset's graph and vector stores.
  name: Cognee Validate API
  slug: cognee-validate-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Graph visualization endpoints.
  name: Cognee Visualize API
  slug: cognee-visualize-api
artifact_total: 51
collections:
- collection_type: open
  name: Cognee REST agents API
  slug: open-cognee-agents-api
- collection_type: open
  name: Cognee REST agents cognify API
  slug: open-cognee-cognify-api
- collection_type: open
  name: Cognee REST agents data API
  slug: open-cognee-data-api
- collection_type: open
  name: Cognee REST agents datasets API
  slug: open-cognee-datasets-api
- collection_type: open
  name: Cognee REST agents health API
  slug: open-cognee-health-api
- collection_type: open
  name: Cognee REST agents search API
  slug: open-cognee-search-api
- collection_type: open
  name: Cognee REST agents settings API
  slug: open-cognee-settings-api
common:
- group: other
  href: https://artifacts.apis.io/cognee/capabilities/cognee-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cognee-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/topoteretes/cognee/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/topoteretes/cognee/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/topoteretes/cognee/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/topoteretes/cognee/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/topoteretes/cognee/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/topoteretes/cognee/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/cognee/agentic-access/cognee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cognee-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cognee/security/cognee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognee-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cognee/authentication/cognee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cognee-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cognee.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cognee.ai/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topoteretes
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/topoteretes/cognee
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognee-ai
- group: company
  title: ''
  type: Blog
  url: https://www.cognee.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cognee.ai/pricing
- group: commercial
  title: ''
  type: CostCalculator
  url: https://www.cognee.ai/cost-calculator
- group: other
  title: ''
  type: X
  url: https://x.com/cognee_
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/m63hxKsp4p
- group: commercial
  href: https://artifacts.apis.io/cognee/plans/cognee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cognee-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cognee/rate-limits/cognee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cognee-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cognee/finops/cognee-finops.yml
  title: ''
  type: FinOps
  url: finops/cognee-finops.yml
- group: design
  href: https://artifacts.apis.io/cognee/vocabulary/cognee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cognee-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cognee/json-ld/cognee-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/cognee-context.jsonld
created: '2026-06-12'
description: Cognee is an open-source AI memory and knowledge graph platform that enables developers to build persistent, structured memory for AI agents and LLM applications. The platform provides a REST API and Python/TypeScript SDKs for ingesting documents and data from 28+ sources, processing them through a six-stage ECL (Extract, Cognify, Load) pipeline, and storing the resulting entities and relationships in a hybrid graph-vector-relational store. Developers can query the knowledge graph using 13+ search modes including semantic graph completion, RAG completion, and temporal search. Cognee is available as a managed cloud service on AWS, GCP, and Azure, or as a self-hosted deployment via Docker, Modal, Railway, Fly.io, and Render.
examples:
- key_count: 3
  name: Cognee Search Example
  slug: cognee-search-example
finops:
- has_sources: true
  method: derived
  name: Cognee Finops
  primary_unit: 1m tokens
  service_category: ''
  slug: cognee-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognee.png
json_schemas:
- name: Cognee Dataset
  property_count: 5
  slug: cognee-dataset
- name: Cognee Search Payload
  property_count: 12
  slug: cognee-search-payload
jsonld:
- class_count: 1
  name: Cognee Context
  property_count: 42
  slug: cognee-context
layout: provider
modified: '2026-06-12'
name: Cognee
nav: Providers
network: true
overview: 'Cognee publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cognify API, Datasets API, Health API, and 29 more. Tagged areas include Artificial Intelligence, Memory, Knowledge Graph, RAG, and Agents.


  The Cognee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cognee''s developer surface includes authentication, documentation, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Cognee Plans Pricing
  plan_count: 3
  slug: cognee-plans-pricing
- name: Cognee Price Estimates
  plan_count: 0
  slug: cognee-price-estimates
random_paper: 1
rate_limits:
- limit_count: 2
  name: Cognee Rate Limits
  slug: cognee-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Cognee — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cognee-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 50.0
    contract_governance: 23.5
    contract_quality: 57.5
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.0
      total: 40
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/cognee/cognee-2026-06-20T174711.png
security:
- kind: authentication
  name: Cognee Authentication
  slug: cognee-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cognee Domain Security
  slug: cognee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cognee
tags:
- Artificial Intelligence
- Memory
- Knowledge Graph
- RAG
- Agents
- Graph Database
- Vector Search
- LLM
- Open Source
website: https://www.cognee.ai/
---
