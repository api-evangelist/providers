---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Agentgates Ai Agentic Access
  operation_count: 17
  slug: agentgates-ai-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 1
apis:
- baseURL: https://agentgates.ai
  baseurl_source: declared
  description: The Compute API from Agentgates — 4 operation(s) for compute.
  name: Agentgates Compute API
  slug: agentgates-ai-compute-api
- baseURL: https://agentgates.ai
  baseurl_source: declared
  description: The Directory API from Agentgates — 7 operation(s) for directory.
  name: Agentgates Directory API
  slug: agentgates-ai-directory-api
- baseURL: https://agentgates.ai
  baseurl_source: declared
  description: The Inference API from Agentgates — 4 operation(s) for inference.
  name: Agentgates Inference API
  slug: agentgates-ai-inference-api
- baseURL: https://agentgates.ai
  baseurl_source: declared
  description: The Llms.txt API from Agentgates — 1 operation(s) for llms.txt.
  name: Agentgates Llms.txt API
  slug: agentgates-ai-llms-txt-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/agentgates-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/agentgates-ai/agentic-access/agentgates-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentgates-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentgates-ai/rules/agentgates-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agentgates-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agentgates-ai/json-ld/agentgates-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentgates-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentgates-ai/vocabulary/agentgates-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentgates-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentgates-ai/data-model/agentgates-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentgates-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentgates-ai/authentication/agentgates-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentgates-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentgates-ai/errors/agentgates-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentgates-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentgates-ai/conformance/agentgates-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentgates-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentgates-ai/llms/agentgates-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentgates-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agentgates-ai/a2a/agentgates-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentgates-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentgates-ai/well-known/agentgates-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentgates-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentgates-ai/hosts/agentgates-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentgates-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentgates-ai/vendors/agentgates-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentgates-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentgates-ai/security/agentgates-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentgates-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentgates.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agentgates.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentgates.ai/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentgates.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Carlos-Sotop/agentgates
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agentgates.ai/openapi.json
  - status: 401
    url: https://agentgates.ai/mcp
  - status: 200
    url: https://agentgates.ai/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 'Agentgates provides compute and inference for AI agents: a confidential virtual machine billed by the hour and an open model billed per request. Both services quote a real price over HTTP and accept payment in USDC. No account is required; users simply connect a wallet to start using the platform.'
image: https://agentgates.ai/brand/icon.svg
jsonld:
- class_count: 1
  name: Agentgates Ai Context
  property_count: 2
  slug: agentgates-ai-context
layout: provider
modified: '2026-10-31'
name: Agentgates
nav: Providers
network: true
overview: 'Agentgates publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Compute API, Directory API, Inference API, and 1 more. Tagged areas include Artificial Intelligence, Compute, Inference, Blockchain, and Payments.


  The Agentgates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentgates'' developer surface includes authentication, documentation, API reference, and 17 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Agentgates API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: agentgates-ai-rules
scopes:
- name: Agentgates Ai Scopes
  scope_count: 0
  slug: agentgates-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 5.3
    contract_governance: 19.7
    contract_quality: 42.6
    developer_ergonomics: 26.7
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentgates Ai Authentication
  slug: agentgates-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agentgates Ai Domain Security
  slug: agentgates-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentgates-ai
tags:
- Artificial Intelligence
- Compute
- Inference
- Blockchain
- Payments
website: https://agentgates.ai/
---
