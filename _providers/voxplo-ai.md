---
access_model:
  confidence: medium
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
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Voxplo Ai Agentic Access
  operation_count: 3
  slug: voxplo-ai-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.voxplo.ai/v1
  baseurl_source: declared
  description: The Agent API from Voxplo — 2 operation(s) for agent.
  name: Voxplo Agent API
  slug: voxplo-ai-agent-api
artifact_total: 13
asyncapis:
- description: ''
  name: Voxplo Ai Webhooks
  slug: voxplo-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/voxplo-ai/agentic-access/voxplo-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/voxplo-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/voxplo-ai/plans/voxplo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voxplo-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/rules/voxplo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/voxplo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/json-ld/voxplo-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/voxplo-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/voxplo-ai/vocabulary/voxplo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/voxplo-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/asyncapi/voxplo-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/voxplo-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/data-model/voxplo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/voxplo-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/voxplo-ai/changelog/voxplo-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/voxplo-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/conventions/voxplo-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/voxplo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/conventions/voxplo-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/voxplo-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.voxplo.ai/security
- group: auth
  href: https://artifacts.apis.io/voxplo-ai/authentication/voxplo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voxplo-ai-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.voxplo.ai/docs/agent-api/versioning
- group: design
  href: https://artifacts.apis.io/voxplo-ai/lifecycle/voxplo-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/voxplo-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/errors/voxplo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/voxplo-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/voxplo-ai/conformance/voxplo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voxplo-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/voxplo-ai/llms/voxplo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voxplo-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/voxplo-ai/a2a/voxplo-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/voxplo-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/voxplo-ai/well-known/voxplo-ai-voxplo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voxplo-ai-voxplo-security.txt
- group: auth
  href: https://artifacts.apis.io/voxplo-ai/well-known/voxplo-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voxplo-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/voxplo-ai/well-known/voxplo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voxplo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/voxplo-ai/hosts/voxplo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voxplo-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/voxplo-ai/vendors/voxplo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/voxplo-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.voxplo.ai/security
- group: auth
  href: https://artifacts.apis.io/voxplo-ai/security/voxplo-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/voxplo-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/voxplo-ai/security/voxplo-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/voxplo-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/voxplo-ai/security/voxplo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voxplo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voxplo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.voxplo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.voxplo.ai/docs/agent-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.voxplo.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.voxplo.ai/docs/agent-api/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voxplo.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.voxplo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.voxplo.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voxplo.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voxplo.ai/terms
created: '2026-10-31'
description: Voxplo AI provides a voice agent platform that enables developers to add AI‑driven phone call capabilities to their applications via a REST API and a proprietary MCP (Message Control Protocol). The service can place outbound calls, answer inbound calls, book meetings, qualify leads, and integrate with custom business rules. Voxplo offers SDKs for multiple languages, comprehensive documentation, webhooks for event handling, and pricing tiers for businesses of all sizes. Its platform is designed for easy integration, scalability, and secure handling of voice interactions.
image: https://www.voxplo.ai/icon.svg
json_schemas:
- name: AgentCall
  property_count: 15
  slug: voxplo-ai-agent-call
- name: AgentCallSummary
  property_count: 9
  slug: voxplo-ai-agent-call-summary
- name: PlaceCallRequest
  property_count: 8
  slug: voxplo-ai-place-call-request
jsonld:
- class_count: 4
  name: Voxplo Ai Context
  property_count: 20
  slug: voxplo-ai-context
layout: provider
modified: '2026-10-31'
name: Voxplo
nav: Providers
network: true
overview: 'Voxplo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include Company, Artificial Intelligence, Voice, and MCP.


  The Voxplo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Voxplo''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 30 more developer resources.'
plans:
- name: Voxplo Ai Plans Pricing
  plan_count: 4
  slug: voxplo-ai-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Voxplo API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: voxplo-ai-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 67.8
    developer_ergonomics: 34.5
    discoverability: 57.1
    operational_transparency: 32.9
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Voxplo Ai Authentication
  slug: voxplo-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Voxplo Ai Domain Security
  slug: voxplo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Voxplo Ai Vulnerability Disclosure
  slug: voxplo-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Voxplo Ai Trust Center
  slug: voxplo-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: voxplo-ai
tags:
- Company
- Artificial Intelligence
- Voice
- MCP
website: https://voxplo.ai/
---
