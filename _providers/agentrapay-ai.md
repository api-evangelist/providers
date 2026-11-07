---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Agentrapay Ai Agentic Access
  operation_count: 7
  slug: agentrapay-ai-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.agentrapay.ai
  baseurl_source: declared
  description: The Agents API from Agentra — 2 operation(s) for agents.
  name: Agentra Agents API
  slug: agentrapay-ai-agents-api
- baseURL: https://api.agentrapay.ai
  baseurl_source: declared
  description: The Authorizations API from Agentra — 2 operation(s) for authorizations.
  name: Agentra Authorizations API
  slug: agentrapay-ai-authorizations-api
- baseURL: https://api.agentrapay.ai
  baseurl_source: declared
  description: The Health API from Agentra — 1 operation(s) for health.
  name: Agentra Health API
  slug: agentrapay-ai-health-api
- baseURL: https://api.agentrapay.ai
  baseurl_source: declared
  description: The Trust API from Agentra — 1 operation(s) for trust.
  name: Agentra Trust API
  slug: agentrapay-ai-trust-api
- baseURL: https://api.agentrapay.ai
  baseurl_source: declared
  description: The Wallets API from Agentra — 1 operation(s) for wallets.
  name: Agentra Wallets API
  slug: agentrapay-ai-wallets-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/agentrapay-ai/vocabulary/agentrapay-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentrapay-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentrapay-ai/data-model/agentrapay-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentrapay-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/agentrapay-ai/agentic-access/agentrapay-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentrapay-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentrapay-ai/rules/agentrapay-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agentrapay-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/agentrapay-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentrapay-ai/errors/agentrapay-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentrapay-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentrapay-ai/conformance/agentrapay-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentrapay-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentrapay-ai/llms/agentrapay-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentrapay-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agentrapay-ai/hosts/agentrapay-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentrapay-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentrapay-ai/vendors/agentrapay-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentrapay-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentrapay-ai/security/agentrapay-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrapay-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrapay.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agentrapay.ai/docs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentrapay.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentrapay.ai/privacy/
created: '2026-11-01'
description: Agentra provides trust infrastructure for autonomous AI agents, enabling identity verification, reputation scoring, and transaction authorization without custodial control. The platform supports MCP native integration, MPP and x402 protocols, offering a non‑custodial, tiered trust system for agents to transact safely on base mainnet. It includes features like bidirectional trust, mandate engine, and agent discovery, targeting the emerging agent economy.
json_schemas:
- name: AgentProfile
  property_count: 0
  slug: agentrapay-ai-agent-profile
- name: AgentRegistration
  property_count: 0
  slug: agentrapay-ai-agent-registration
- name: AuthorizationRequest
  property_count: 0
  slug: agentrapay-ai-authorization-request
- name: AuthorizationResponse
  property_count: 0
  slug: agentrapay-ai-authorization-response
- name: TrustScore
  property_count: 0
  slug: agentrapay-ai-trust-score
- name: WalletProvision
  property_count: 0
  slug: agentrapay-ai-wallet-provision
layout: provider
modified: '2026-11-01'
name: Agentra
nav: Providers
network: true
overview: 'Agentra publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Authorizations API, Health API, and 2 more. Tagged areas include Identity Verification, Reputation Scoring, Transaction Authorization, Non‑Custodial Wallet, and Agent Infrastructure.


  The Agentra catalog on APIs.io includes 1 Spectral governance ruleset.


  Agentra''s developer surface includes documentation and 14 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Agentra API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agentrapay-ai-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 54.5
    developer_ergonomics: 6.5
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentrapay Ai Domain Security
  slug: agentrapay-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: agentrapay-ai-payment-flow
  slug: agentrapay-ai-payment-flow
slug: agentrapay-ai
tags:
- Identity Verification
- Reputation Scoring
- Transaction Authorization
- Non‑Custodial Wallet
- Agent Infrastructure
website: https://agentrapay.ai/
---
