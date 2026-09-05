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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agent Diff Agentic Access
  operation_count: 5
  slug: agent-diff-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.agentdiff.dev/v1
  baseurl_source: declared
  description: The Diffs API from Agent Diff — 1 operation(s) for diffs.
  name: Agent Diff Diffs API
  slug: agent-diff-diffs-api
- baseURL: https://api.agentdiff.dev/v1
  baseurl_source: declared
  description: The Sandboxes API from Agent Diff — 2 operation(s) for sandboxes.
  name: Agent Diff Sandboxes API
  slug: agent-diff-sandboxes-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agent Diff Sandbox Diffs API
  slug: open-agent-diff-diffs-api
- collection_type: open
  name: Agent Diff Sandbox API
  slug: open-agent-diff-sandbox
- collection_type: open
  name: Agent Diff Sandbox Diffs Sandboxes API
  slug: open-agent-diff-sandboxes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agent-diff-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agent-diff-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agent-diff-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.agentdiff.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentdiff.dev/docs
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/rules/agent-diff-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-schema/agent-diff-sandbox-sandbox-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-schema/agent-diff-sandbox-diff-entry-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/json-ld/agent-diff-sandbox-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/vocabulary/agent-diff-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.agentdiff.dev/llms.txt
created: '2026-01-02'
description: Agent Diff creates isolated, ephemeral replicas of third-party APIs (Slack, Linear, GitHub). Agents interact with these sandboxes to produce deterministic state-change diffs without side effects, rate limits, or real API calls. Ideal for testing AI agents that interact with external APIs.
examples:
- key_count: 5
  name: Sandbox Diff Entry Example
  slug: sandbox-diff-entry-example
- key_count: 2
  name: Sandbox Diff List Example
  slug: sandbox-diff-list-example
- key_count: 4
  name: Sandbox Sandbox Create Request Example
  slug: sandbox-sandbox-create-request-example
- key_count: 7
  name: Sandbox Sandbox Example
  slug: sandbox-sandbox-example
- key_count: 2
  name: Sandbox Sandbox List Example
  slug: sandbox-sandbox-list-example
finops:
- name: Agent Diff Finops
  service_category: API
  slug: agent-diff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agent-diff.png
json_schemas:
- name: DiffEntry
  property_count: 5
  slug: sandbox-diff-entry
- name: DiffList
  property_count: 2
  slug: sandbox-diff-list
- name: SandboxCreateRequest
  property_count: 4
  slug: sandbox-sandbox-create-request
- name: SandboxList
  property_count: 2
  slug: sandbox-sandbox-list
- name: Sandbox
  property_count: 7
  slug: sandbox-sandbox
json_structures:
- name: Sandbox Diff Entry Structure
  property_count: 5
  slug: sandbox-diff-entry-structure
- name: Sandbox Diff List Structure
  property_count: 2
  slug: sandbox-diff-list-structure
- name: Sandbox Sandbox Create Request Structure
  property_count: 4
  slug: sandbox-sandbox-create-request-structure
- name: Sandbox Sandbox List Structure
  property_count: 2
  slug: sandbox-sandbox-list-structure
- name: Sandbox Sandbox Structure
  property_count: 7
  slug: sandbox-sandbox-structure
jsonld:
- class_count: 6
  name: Agent Diff Sandbox Context
  property_count: 15
  slug: agent-diff-sandbox-context
layout: provider
modified: '2026-05-19'
name: Agent Diff
nav: Providers
network: true
overview: 'Agent Diff publishes 2 APIs on the [APIs.io](https://apis.io/) network: Diffs API and Sandboxes API. Tagged areas include API Testing, AI Agents, Sandboxing, API Diffing, and Developer Tools.


  The Agent Diff catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agent Diff''s developer surface includes authentication, developer portal, getting-started guide, and 8 more developer resources.'
plans:
- name: Agent Diff Plans Pricing
  plan_count: 3
  slug: agent-diff-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Agent Diff Rate Limits
  slug: agent-diff-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agent Diff API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agent-diff-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: Agent Diff API Rules
  rule_count: 30
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 16
  slug: agent-diff-spectral-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 66.5
    catalog_earned_first_party: 0.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 66.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agent-diff/refs/heads/main/screenshots/agent-diff-2026-06-20T165854.png
security:
- kind: authentication
  name: Agent Diff Authentication
  slug: agent-diff-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agent Diff Domain Security
  slug: agent-diff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agent-diff
tags:
- API Testing
- AI Agents
- Sandboxing
- API Diffing
- Developer Tools
website: https://www.agentdiff.dev/
---
