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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
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
    mcp_server: documented
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
  score: 49.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Canarics Com Agentic Access
  operation_count: 21
  slug: canarics-com-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 1
apis:
- description: API that lets a client's AI assistant check the client's Canarics account, including usage, agents, and call history.
  name: Canarics API
  slug: canarics-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Agents API from canarics-com — 1 operation(s) for agents.
  name: canarics-com Agents API
  slug: canarics-com-agents-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Callbacks API from canarics-com — 1 operation(s) for callbacks.
  name: canarics-com Callbacks API
  slug: canarics-com-callbacks-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Calls API from canarics-com — 2 operation(s) for calls.
  name: canarics-com Calls API
  slug: canarics-com-calls-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Campaigns API from canarics-com — 1 operation(s) for campaigns.
  name: canarics-com Campaigns API
  slug: canarics-com-campaigns-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Canarics API For AI Agents API from canarics-com — 1 operation(s) for canarics api for ai agents.
  name: canarics-com Canarics API For AI Agents API
  slug: canarics-com-canarics-api-for-ai-agents-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Contacts API from canarics-com — 1 operation(s) for contacts.
  name: canarics-com Contacts API
  slug: canarics-com-contacts-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Conversations API from canarics-com — 1 operation(s) for conversations.
  name: canarics-com Conversations API
  slug: canarics-com-conversations-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Demo Call API from canarics-com — 1 operation(s) for demo call.
  name: canarics-com Demo Call API
  slug: canarics-com-demo-call-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Mcp API from canarics-com — 1 operation(s) for mcp.
  name: canarics-com MCP API
  slug: canarics-com-mcp-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Me API from canarics-com — 1 operation(s) for me.
  name: canarics-com Me API
  slug: canarics-com-me-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Signup API from canarics-com — 2 operation(s) for signup.
  name: canarics-com Signup API
  slug: canarics-com-signup-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Tools API from canarics-com — 3 operation(s) for tools.
  name: canarics-com Tools API
  slug: canarics-com-tools-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Upgrade API from canarics-com — 2 operation(s) for upgrade.
  name: canarics-com Upgrade API
  slug: canarics-com-upgrade-api
- baseURL: https://salestick-backend-647994203646.europe-central2.run.app
  baseurl_source: declared
  description: The Usage API from canarics-com — 1 operation(s) for usage.
  name: canarics-com Usage API
  slug: canarics-com-usage-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/canarics-com/agentic-access/canarics-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canarics-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/canarics-com/plans/canarics-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canarics-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/canarics-com/rules/canarics-com-rules.yml
  title: ''
  type: Spectral
  url: rules/canarics-com-rules.yml
- group: design
  href: https://artifacts.apis.io/canarics-com/json-ld/canarics-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canarics-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/canarics-com/vocabulary/canarics-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canarics-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/canarics-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/canarics-com/data-model/canarics-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canarics-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/canarics-com/authentication/canarics-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canarics-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/canarics-com/errors/canarics-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canarics-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canarics-com/conformance/canarics-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canarics-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canarics-com/llms/canarics-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canarics-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/canarics-com/mcp/canarics-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canarics-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/canarics-com/well-known/canarics-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canarics-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/canarics-com/hosts/canarics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canarics-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canarics-com/vendors/canarics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canarics-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/canarics-com/security/canarics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canarics-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canarics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://canarics.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://canarics.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://canarics.com/voice-ai-pricing-comparison
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canarics.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canarics.com/legal/privacy
created: '2026-10-29'
description: Canarics provides AI-powered sales intelligence and voice AI solutions that answer, route, and analyze every call, offering infinite memory for customer conversations without replacing telephony. Their platform delivers a zero‑UI sales ecosystem with three products, enabling enterprises to turn phone calls into decisions via an always‑on AI receptionist.
image: https://canarics.com/logo.svg
jsonld:
- class_count: 5
  name: Canarics Com Context
  property_count: 39
  slug: canarics-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at canarics.com.
  name: canarics-com MCP Server
  slug: canarics-com-mcp-yml
modified: '2026-10-29'
name: canarics-com
nav: Providers
network: true
overview: 'canarics-com publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Callbacks API, Calls API, and 12 more. Tagged areas include Company, Artificial Intelligence, Voice, Sales Intelligence, and Enterprise.


  The canarics-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  canarics-com''s developer surface includes authentication, documentation, API reference, pricing, and 18 more developer resources.'
plans:
- name: Canarics Com Plans Pricing
  plan_count: 3
  slug: canarics-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Canarics Com Rate Limits
  slug: canarics-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: canarics-com API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: canarics-com-rules
scopes:
- name: Canarics Com Scopes
  scope_count: 0
  slug: canarics-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.0
    catalog_earned_first_party: 12.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 55.2
    developer_ergonomics: 26.7
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/canarics-com/canarics-com-2026-11-03T123107.png
security:
- kind: authentication
  name: Canarics Com Authentication
  slug: canarics-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Canarics Com Domain Security
  slug: canarics-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canarics-com
tags:
- Company
- Artificial Intelligence
- Voice
- Sales Intelligence
- Enterprise
website: https://canarics.com/
---
