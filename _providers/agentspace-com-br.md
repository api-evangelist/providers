---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 2
  name: Agentspace Com Br Agentic Access
  operation_count: 43
  slug: agentspace-com-br-agentic-access
  summary_line: 43 operations · 28 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The account API from AgentSpace — 12 operation(s) for account.
  name: AgentSpace Account API
  slug: agentspace-com-br-account-api
- description: The agent API from AgentSpace — 12 operation(s) for agent.
  name: AgentSpace Agent API
  slug: agentspace-com-br-agent-api
- description: The billing API from AgentSpace — 4 operation(s) for billing.
  name: AgentSpace Billing API
  slug: agentspace-com-br-billing-api
- description: The review API from AgentSpace — 7 operation(s) for review.
  name: AgentSpace Review API
  slug: agentspace-com-br-review-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/agentspace-com-br/agentic-access/agentspace-com-br-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentspace-com-br-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentspace-com-br/plans/agentspace-com-br-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentspace-com-br-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentspace-com-br/rules/agentspace-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/agentspace-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/agentspace-com-br/json-ld/agentspace-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentspace-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentspace-com-br/vocabulary/agentspace-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentspace-com-br-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentspace-com-br/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentspace-com-br/data-model/agentspace-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentspace-com-br-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentspace-com-br/errors/agentspace-com-br-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentspace-com-br-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentspace-com-br/conformance/agentspace-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentspace-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentspace-com-br/llms/agentspace-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentspace-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/agentspace-com-br/a2a/agentspace-com-br-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentspace-com-br-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentspace-com-br/well-known/agentspace-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentspace-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentspace-com-br/hosts/agentspace-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentspace-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentspace-com-br/vendors/agentspace-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentspace-com-br-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentspace-com-br/security/agentspace-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentspace-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentspace.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://agentspace.com.br/docs
- group: operate
  title: ''
  type: Support
  url: https://agentspace.com.br/suporte
- group: commercial
  title: ''
  type: Pricing
  url: https://agentspace.com.br/pricing
- group: start
  title: ''
  type: SignUp
  url: https://agentspace.com.br/register
- group: start
  title: ''
  type: Login
  url: https://agentspace.com.br/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentspace.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentspace.com.br/privacidade
- group: start
  title: ''
  type: GettingStarted
  url: https://agentspace.com.br/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agentspace.com.br/openapi.json
  - status: 401
    url: https://agentspace.com.br/mcp
  - status: 200
    url: https://agentspace.com.br/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AgentSpace provides a persistent workspace, sandbox, and hosting platform for AI agents, allowing them to store files beyond a session, run code, and publish public URLs. Access is available via MCP, REST, or A2A interfaces, with free and paid plans offering varying storage and site limits. The service includes dedicated support where users can contact the team with questions, problems, or ideas.
image: https://agentspace.com.br/static/brand/mark-96.png
json_schemas:
- name: Body_upload_file_api_v1_files_upload_post
  property_count: 3
  slug: agentspace-com-br-body-upload-file-api-v1-files-upload-post
- name: DeleteAccountBody
  property_count: 2
  slug: agentspace-com-br-delete-account-body
- name: DeployBody
  property_count: 5
  slug: agentspace-com-br-deploy-body
- name: ExecBody
  property_count: 3
  slug: agentspace-com-br-exec-body
- name: RegisterBody
  property_count: 4
  slug: agentspace-com-br-register-body
- name: WriteFileBody
  property_count: 2
  slug: agentspace-com-br-write-file-body
jsonld:
- class_count: 18
  name: Agentspace Com Br Context
  property_count: 33
  slug: agentspace-com-br-context
layout: provider
modified: '2026-11-01'
name: AgentSpace
nav: Providers
network: true
overview: 'AgentSpace publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent API, Billing API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Workspace, Sandbox, and Hosting.


  The AgentSpace catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentSpace''s developer surface includes documentation, support, pricing, signup flow, getting-started guide, and 19 more developer resources.'
plans:
- name: Agentspace Com Br Plans Pricing
  plan_count: 3
  slug: agentspace-com-br-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Agentspace Com Br Rate Limits
  slug: agentspace-com-br-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AgentSpace API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agentspace-com-br-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 19.5
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentspace Com Br Domain Security
  slug: agentspace-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: hello
  slug: agentspace-com-br-hello
slug: agentspace-com-br
tags:
- Artificial Intelligence
- Agents
- Workspace
- Sandbox
- Hosting
website: https://agentspace.com.br/
---
