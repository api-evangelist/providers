---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: true
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: 9Bot Com Br Agentic Access
  operation_count: 6
  slug: 9bot-com-br-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://mcp.9bot.com.br
  baseurl_source: declared
  description: Public MCP, OAuth, and registry metadata.
  name: 9bot Discovery API
  slug: 9bot-com-br-discovery-api
- baseURL: https://mcp.9bot.com.br
  baseurl_source: declared
  description: Public service health information.
  name: 9bot Health API
  slug: 9bot-com-br-health-api
- baseURL: https://mcp.9bot.com.br
  baseurl_source: declared
  description: OAuth-protected Model Context Protocol transport.
  name: 9bot MCP API
  slug: 9bot-com-br-mcp-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/9bot-com-br/agentic-access/9bot-com-br-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/9bot-com-br-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/9bot-com-br/plans/9bot-com-br-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/9bot-com-br-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/rules/9bot-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/9bot-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/json-ld/9bot-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/9bot-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/9bot-com-br/vocabulary/9bot-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/9bot-com-br-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/9bot-com-br/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/data-model/9bot-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/9bot-com-br-data-model.yml
- group: operate
  href: https://artifacts.apis.io/9bot-com-br/changelog/9bot-com-br-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/9bot-com-br-changelog.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/conventions/9bot-com-br-conventions.yml
  title: ''
  type: Conventions
  url: conventions/9bot-com-br-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://9bot.com.br/en/bot-policy/
- group: auth
  href: https://artifacts.apis.io/9bot-com-br/authentication/9bot-com-br-authentication.yml
  title: ''
  type: Authentication
  url: authentication/9bot-com-br-authentication.yml
- group: auth
  href: https://artifacts.apis.io/9bot-com-br/scopes/9bot-com-br-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/9bot-com-br-scopes.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/lifecycle/9bot-com-br-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/9bot-com-br-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/errors/9bot-com-br-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/9bot-com-br-problem-types.yml
- group: design
  href: https://artifacts.apis.io/9bot-com-br/conformance/9bot-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/9bot-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/9bot-com-br/llms/9bot-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/9bot-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/9bot-com-br/a2a/9bot-com-br-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/9bot-com-br-a2a.yml
- group: auth
  href: https://artifacts.apis.io/9bot-com-br/well-known/9bot-com-br-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/9bot-com-br-security.txt
- group: agent
  href: https://artifacts.apis.io/9bot-com-br/well-known/9bot-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/9bot-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/9bot-com-br/hosts/9bot-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/9bot-com-br-hosts.yml
- group: auth
  href: https://artifacts.apis.io/9bot-com-br/security/9bot-com-br-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/9bot-com-br-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/9bot-com-br/security/9bot-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/9bot-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://9bot.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://9bot.com.br/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://9bot.com.br/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://9bot.com.br/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://9bot.com.br/en/start-now/
- group: company
  title: ''
  type: Blog
  url: https://9bot.com.br/en/articles/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://9bot.com.br/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://9bot.com.br/en/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://9bot.com.br/en/start-now/
created: '2026-10-31'
description: 9bot provides a platform to automate WhatsApp group management, enabling scheduled messages, alerts, integrations, moderation, and reporting through a programmable API. It empowers businesses and communities to streamline communications, connect AI assistants, and integrate external systems, delivering a unified control panel for WhatsApp operations.
image: https://9bot.com.br/wp-content/uploads/2025/11/logo-9bot2.png.webp
json_schemas:
- name: HealthResponse
  property_count: 4
  slug: 9bot-com-br-health-response
- name: JsonRpcClientPayload
  property_count: 0
  slug: 9bot-com-br-json-rpc-client-payload
- name: McpMetadata
  property_count: 6
  slug: 9bot-com-br-mcp-metadata
- name: McpServerManifest
  property_count: 7
  slug: 9bot-com-br-mcp-server-manifest
- name: OAuthAuthorizationServerMetadata
  property_count: 8
  slug: 9bot-com-br-oauth-authorization-server-metadata
- name: OAuthProtectedResourceMetadata
  property_count: 5
  slug: 9bot-com-br-oauth-protected-resource-metadata
jsonld:
- class_count: 11
  name: 9Bot Com Br Context
  property_count: 34
  slug: 9bot-com-br-context
layout: provider
modified: '2026-10-31'
name: 9bot
nav: Providers
network: true
overview: '9bot publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Health API, and MCP API. Tagged areas include WhatsApp, Automation, Bot, Messaging, and Integration.


  The 9bot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  9bot''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: 9Bot Com Br Plans Pricing
  plan_count: 2
  slug: 9bot-com-br-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: 9Bot Com Br Rate Limits
  slug: 9bot-com-br-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 9bot API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: 9bot-com-br-rules
scopes:
- name: 9Bot Com Br Scopes
  scope_count: 2
  slug: 9bot-com-br-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 38.2
    contract_governance: 35.6
    contract_quality: 64.2
    developer_ergonomics: 38.6
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 9Bot Com Br Authentication
  slug: 9bot-com-br-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 9Bot Com Br Domain Security
  slug: 9bot-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 9Bot Com Br Vulnerability Disclosure
  slug: 9bot-com-br-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-mcp-health
  slug: 9bot-com-br-get-mcp-health
slug: 9bot-com-br
tags:
- WhatsApp
- Automation
- Bot
- Messaging
- Integration
website: https://9bot.com.br/
---
