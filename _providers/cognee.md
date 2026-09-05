---
access_model:
  confidence: medium
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cognee Agentic Access
  operation_count: 22
  slug: cognee-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: AI agent identity management
  name: Cognee agents API
  slug: cognee-agents-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Knowledge graph construction pipeline
  name: Cognee cognify API
  slug: cognee-cognify-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Data ingestion and deletion operations
  name: Cognee data API
  slug: cognee-data-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Dataset management and introspection
  name: Cognee datasets API
  slug: cognee-datasets-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Service health probes
  name: Cognee health API
  slug: cognee-health-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: Semantic and graph search queries
  name: Cognee search API
  slug: cognee-search-api
- baseURL: https://api.cognee.ai
  baseurl_source: declared
  description: System configuration (LLM and vector DB)
  name: Cognee settings API
  slug: cognee-settings-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/cognee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognee-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/cognee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cognee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cognee-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cognee-vocabulary.yml
- group: design
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
- name: Cognee Finops
  service_category: ''
  slug: cognee-finops
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
overview: 'Cognee publishes 7 APIs on the [APIs.io](https://apis.io/) network, including agents API, cognify API, data API, and 4 more. Tagged areas include Artificial Intelligence, Memory, Knowledge Graph, RAG, and Agents.


  The Cognee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cognee''s developer surface includes authentication, documentation, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Cognee Plans Pricing
  plan_count: 4
  slug: cognee-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Cognee Rate Limits
  slug: cognee-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cognee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cognee-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 76.3
    catalog_earned_first_party: 0.0
    catalog_gap: 38.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 59.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognee/refs/heads/main/screenshots/cognee-2026-06-20T174711.png
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
- Open-Source
website: https://www.cognee.ai/
---
