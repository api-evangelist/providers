---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Synlake Ai Agentic Access
  operation_count: 16
  slug: synlake-ai-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.synlake.ai/api/v1
  baseurl_source: declared
  description: Agent registration and API keys
  name: synlake-ai Auth API
  slug: synlake-ai-auth-api
- baseURL: https://api.synlake.ai/api/v1
  baseurl_source: declared
  description: Usage tracking and metered billing
  name: synlake-ai Billing API
  slug: synlake-ai-billing-api
- baseURL: https://api.synlake.ai/api/v1
  baseurl_source: declared
  description: Browse providers and services
  name: synlake-ai Catalog API
  slug: synlake-ai-catalog-api
- baseURL: https://api.synlake.ai/api/v1
  baseurl_source: declared
  description: Validate execution kits (Terraform/CLI)
  name: synlake-ai Execution API
  slug: synlake-ai-execution-api
- baseURL: https://api.synlake.ai/api/v1
  baseurl_source: declared
  description: Query and estimate cloud infrastructure
  name: synlake-ai Infrastructure API
  slug: synlake-ai-infrastructure-api
- baseURL: https://api.synlake.ai/api/v1
  baseurl_source: declared
  description: Health and status
  name: synlake-ai System API
  slug: synlake-ai-system-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/synlake-ai/agentic-access/synlake-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/synlake-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/synlake-ai/rules/synlake-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/synlake-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/synlake-ai/json-ld/synlake-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/synlake-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/synlake-ai/vocabulary/synlake-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/synlake-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/synlake-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/synlake-ai/data-model/synlake-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/synlake-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/synlake-ai/authentication/synlake-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/synlake-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/synlake-ai/errors/synlake-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/synlake-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/synlake-ai/conformance/synlake-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synlake-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/synlake-ai/llms/synlake-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synlake-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/synlake-ai/well-known/synlake-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synlake-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/synlake-ai/hosts/synlake-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synlake-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/synlake-ai/vendors/synlake-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/synlake-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/synlake-ai/packages/synlake-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/synlake-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/synlake-ai/packages/synlake-ai-packages.yml
  title: ''
  type: Packages
  url: packages/synlake-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://synlake.ai/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://synlake.ai/legal/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synlake
- group: auth
  href: https://artifacts.apis.io/synlake-ai/security/synlake-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synlake-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://synlake.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://synlake.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://synlake.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://synlake.ai/docs/quickstart.html
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://synlake.ai/openapi.json
  - status: null
    url: https://api.synlake.ai/openapi.json
  - status: 401
    url: https://synlake.ai/mcp
  - status: 401
    url: https://api.synlake.ai/mcp
  - status: 200
    url: https://synlake.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Synlake provides a data infrastructure API for autonomous agents, normalizing AWS, GCP, and Azure into a single schema. It offers execution kits (Terraform + CLI), cost estimates, and deployment via API. Get your AI agent deploying cloud infrastructure in under 5 minutes.
image: https://synlake.ai/og-image.png
json_schemas:
- name: ActivateResponse
  property_count: 6
  slug: synlake-ai-activate-response
- name: EstimateRequest
  property_count: 5
  slug: synlake-ai-estimate-request
- name: EstimateResponse
  property_count: 8
  slug: synlake-ai-estimate-response
- name: QueryRequest
  property_count: 4
  slug: synlake-ai-query-request
- name: UsageResponse
  property_count: 9
  slug: synlake-ai-usage-response
- name: ValidateResponse
  property_count: 5
  slug: synlake-ai-validate-response
jsonld:
- class_count: 16
  name: Synlake Ai Context
  property_count: 54
  slug: synlake-ai-context
layout: provider
modified: '2026-10-30'
name: synlake-ai
nav: Providers
network: true
overview: 'synlake-ai publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Billing API, Catalog API, and 3 more. Tagged areas include Company, Data Infrastructure, AI Agents, Cloud, and Terraform.


  The synlake-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  synlake-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, and 19 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: synlake-ai API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: synlake-ai-rules
scopes:
- name: Synlake Ai Scopes
  scope_count: 0
  slug: synlake-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 39.8
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/synlake-ai/synlake-ai-2026-11-03T144244.png
security:
- kind: authentication
  name: Synlake Ai Authentication
  slug: synlake-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Synlake Ai Domain Security
  slug: synlake-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: estimate-cost
  slug: estimate-cost
- name: query-infrastructure
  slug: query-infrastructure
- name: validate-execution
  slug: validate-execution
slug: synlake-ai
tags:
- Company
- Data Infrastructure
- AI Agents
- Cloud
- Terraform
website: https://synlake.ai/
---
