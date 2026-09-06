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
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Tinybird Agentic Access
  operation_count: 38
  slug: tinybird-agentic-access
  summary_line: 38 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Analyze files to generate data source schemas
  name: Tinybird Analyze API
  slug: tinybird-analyze-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Manage data source lifecycle and data operations
  name: Tinybird Data Sources API
  slug: tinybird-data-sources-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Create and manage workspace variables
  name: Tinybird Environment Variables API
  slug: tinybird-environment-variables-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Ingest NDJSON events via HTTP POST
  name: Tinybird Events API
  slug: tinybird-events-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Retrieve job details and historical records
  name: Tinybird Jobs API
  slug: tinybird-jobs-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Handle organization management, members, workspaces, and clusters
  name: Tinybird Organizations API
  slug: tinybird-organizations-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Manage pipes, API endpoints, and materialized views
  name: Tinybird Pipes API
  slug: tinybird-pipes-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Execute SQL queries against pipes and data sources
  name: Tinybird Query API
  slug: tinybird-query-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Manage sink pipes with scheduling and triggering
  name: Tinybird Sink Pipes API
  slug: tinybird-sink-pipes-api
- baseURL: https://api.tinybird.co
  baseurl_source: declared
  description: Manage authentication tokens
  name: Tinybird Tokens API
  slug: tinybird-tokens-api
artifact_total: 54
collections:
- collection_type: postman
  name: Tinybird Analyze API
  slug: postman-tinybird-analyze-api
- collection_type: postman
  name: Tinybird Analyze Data Sources API
  slug: postman-tinybird-data-sources-api
- collection_type: postman
  name: Tinybird Analyze Environment Variables API
  slug: postman-tinybird-environment-variables-api
- collection_type: postman
  name: Tinybird Analyze Events API
  slug: postman-tinybird-events-api
- collection_type: postman
  name: Tinybird Analyze Jobs API
  slug: postman-tinybird-jobs-api
- collection_type: postman
  name: Tinybird Analyze Organizations API
  slug: postman-tinybird-organizations-api
- collection_type: postman
  name: Tinybird Analyze Pipes API
  slug: postman-tinybird-pipes-api
- collection_type: postman
  name: Tinybird Analyze Query API
  slug: postman-tinybird-query-api
- collection_type: postman
  name: Tinybird Analyze Sink Pipes API
  slug: postman-tinybird-sink-pipes-api
- collection_type: postman
  name: Tinybird Analyze Tokens API
  slug: postman-tinybird-tokens-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tinybird Analyze API
  slug: open-tinybird-analyze-api
- collection_type: open
  name: Tinybird Analyze Data Sources API
  slug: open-tinybird-data-sources-api
- collection_type: open
  name: Tinybird Analyze Environment Variables API
  slug: open-tinybird-environment-variables-api
- collection_type: open
  name: Tinybird Analyze Events API
  slug: open-tinybird-events-api
- collection_type: open
  name: Tinybird Analyze Jobs API
  slug: open-tinybird-jobs-api
- collection_type: open
  name: Tinybird Analyze Organizations API
  slug: open-tinybird-organizations-api
- collection_type: open
  name: Tinybird Analyze Pipes API
  slug: open-tinybird-pipes-api
- collection_type: open
  name: Tinybird Analyze Query API
  slug: open-tinybird-query-api
- collection_type: open
  name: Tinybird Analyze Sink Pipes API
  slug: open-tinybird-sink-pipes-api
- collection_type: open
  name: Tinybird Analyze Tokens API
  slug: open-tinybird-tokens-api
- collection_type: open
  name: Tinybird API
  slug: open-tinybird
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tinybird/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tinybird-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tinybird-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tinybird-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tinybird-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tinybird-co
- group: company
  title: ''
  type: Website
  url: https://www.tinybird.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tinybird.co/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tinybird.co/docs/get-started
- group: start
  title: ''
  type: Signup
  url: https://www.tinybird.co/signup
- group: company
  title: ''
  type: Blog
  url: https://www.tinybird.co/blog
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/openapi/tinybird-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/json-ld/tinybird-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/vocabulary/tinybird-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/rules/tinybird-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tinybirdco
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/tinybirdco/mcp-tinybird
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/tinybirdco/tinybird-agent-skills
created: '2025-01-08'
description: Tinybird is a real-time data platform that allows you to ingest, process, and expose data through low-latency, high-concurrency APIs. The platform supports real-time analytics at scale with a SQL-based transformation layer and instant REST API endpoint publishing.
examples:
- key_count: 2
  name: Tinybird Execute Sql Query Example
  slug: tinybird-execute-sql-query-example
- key_count: 2
  name: Tinybird Ingest Events Example
  slug: tinybird-ingest-events-example
- key_count: 2
  name: Tinybird List Data Sources Example
  slug: tinybird-list-data-sources-example
finops:
- name: Tinybird Finops
  service_category: API
  slug: tinybird-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tinybird.png
json_schemas:
- name: Tinybird Data Source
  property_count: 12
  slug: tinybird-data-source
- name: Tinybird Pipe
  property_count: 8
  slug: tinybird-pipe
- name: Tinybird Token
  property_count: 5
  slug: tinybird-token
json_structures:
- name: Tinybird Data Source Structure
  property_count: 0
  slug: tinybird-data-source-structure
jsonld:
- class_count: 35
  name: Tinybird Context
  property_count: 2
  slug: tinybird-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Tinybird
nav: Providers
network: true
overview: 'Tinybird publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Analyze API, Data Sources API, Environment Variables API, and 7 more. Tagged areas include Analytics, Data, Real-Time, SQL, and Streaming.


  The Tinybird catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tinybird''s developer surface includes authentication, documentation, getting-started guide, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Tinybird Plans Pricing
  plan_count: 3
  slug: tinybird-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Tinybird Rate Limits
  slug: tinybird-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tinybird API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tinybird-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Tinybird API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 2
    info: 0
    warn: 4
  slug: tinybird-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 67.2
    developer_ergonomics: 44.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/screenshots/tinybird-2026-06-20T195408.png
security:
- kind: authentication
  name: Tinybird Authentication
  slug: tinybird-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tinybird Domain Security
  slug: tinybird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tinybird Trust Center
  slug: tinybird-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 4
skills:
- name: tinybird-cli-guidelines
  slug: tinybird-cli-guidelines
- name: tinybird-python-sdk-guidelines
  slug: tinybird-python-sdk-guidelines
- name: tinybird-typescript-sdk-guidelines
  slug: tinybird-typescript-sdk-guidelines
- name: tinybird
  slug: tinybird
slug: tinybird
tags:
- Analytics
- Data
- Real-Time
- SQL
- Streaming
website: https://www.tinybird.co/
---
