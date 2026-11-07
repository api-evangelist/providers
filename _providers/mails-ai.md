---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 64.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 3
  name: Mails Ai Agentic Access
  operation_count: 74
  slug: mails-ai-agentic-access
  summary_line: 74 operations · 38 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Identify the current API key.
  name: mails-ai Account API
  slug: mails-ai-account-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Per-agent email identities and their sending policy.
  name: mails-ai Agents API
  slug: mails-ai-agents-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Create, list, and revoke API keys.
  name: mails-ai API Keys API
  slug: mails-ai-api-keys-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Usage metering and the Stripe billing portal.
  name: mails-ai Billing API
  slug: mails-ai-billing-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: 'The apps connected by signing in (the mails CLI, Claude, ChatGPT …): list and revoke them.'
  name: mails-ai Connected Apps API
  slug: mails-ai-connected-apps-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Bring-your-own custom sending domains (records-only DNS verification).
  name: mails-ai Domains API
  slug: mails-ai-domains-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Compose, edit, schedule, and send drafts.
  name: mails-ai Drafts API
  slug: mails-ai-drafts-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Typed events (incl. classifier output) and the SSE live stream.
  name: mails-ai Events API
  slug: mails-ai-events-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Received messages and the test-key inbound simulator.
  name: mails-ai Inbound API
  slug: mails-ai-inbound-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: 'Label objects: a name and a colour, applied to threads.'
  name: mails-ai Labels API
  slug: mails-ai-labels-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Audit trail of state-changing operations.
  name: mails-ai Logs API
  slug: mails-ai-logs-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Send, list, retrieve, reply, forward, schedule, and cancel email.
  name: mails-ai Messages API
  slug: mails-ai-messages-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Sent, delivered, bounced, complained, received and reply counts over time.
  name: mails-ai Metrics API
  slug: mails-ai-metrics-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Unauthenticated endpoints (health, unsubscribe link targets).
  name: mails-ai Public API
  slug: mails-ai-public-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Workspace- and agent-level deliverability reputation.
  name: mails-ai Reputation API
  slug: mails-ai-reputation-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Full-text search over received and sent mail.
  name: mails-ai Search API
  slug: mails-ai-search-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Suppression lookups and the consent allowlist.
  name: mails-ai Suppression API
  slug: mails-ai-suppression-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Conversation threads grouping inbound + outbound messages, with read state, folders and labels.
  name: mails-ai Threads API
  slug: mails-ai-threads-api
- baseURL: https://api.mails.ai
  baseurl_source: declared
  description: Endpoint registration, delivery history, test, and replay.
  name: mails-ai Webhooks API
  slug: mails-ai-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Mails Ai Webhooks
  slug: mails-ai-webhooks
common:
- group: other
  href: https://artifacts.apis.io/mails-ai/vendors/mails-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mails-ai-vendors.yml
- group: agent
  href: https://artifacts.apis.io/mails-ai/agentic-access/mails-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mails-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mails-ai/plans/mails-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mails-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/rules/mails-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/mails-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/json-ld/mails-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mails-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/mails-ai/vocabulary/mails-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mails-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mails-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/asyncapi/mails-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mails-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/data-model/mails-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mails-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/conventions/mails-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mails-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/conventions/mails-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mails-ai-conventions.yml
- group: start
  href: https://artifacts.apis.io/mails-ai/sandbox/mails-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mails-ai-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://mails.ai/trust
- group: auth
  href: https://artifacts.apis.io/mails-ai/authentication/mails-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mails-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/errors/mails-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mails-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mails-ai/conformance/mails-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mails-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mails-ai/llms/mails-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mails-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/mails-ai/mcp/mails-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mails-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/mails-ai/well-known/mails-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mails-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/mails-ai/well-known/mails-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mails-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/mails-ai/hosts/mails-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mails-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/mails-ai/packages/mails-ai-packages.yml
  title: ''
  type: Packages
  url: packages/mails-ai-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://mails.ai/features/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mails.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://mails.ai/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@mailsai/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mails.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://mails.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.mails.ai/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://mails.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://mails.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://mails.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://mails.ai/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://help.mails.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.mails.ai</code
- group: auth
  href: https://artifacts.apis.io/mails-ai/security/mails-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mails-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mails-ai/security/mails-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mails-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mails-ai/security/mails-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mails-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mails.ai/
coverage:
  checked: '2026-10-31'
  detail: Provider docs are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://mails.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Mails.ai provides a self‑serve AI email API designed for artificial‑intelligence agents. It offers programmatic email addresses with built‑in parsing, identity verification, and reputation scoring, enabling agents to send, receive, and process emails as a core primitive. The platform includes free tier access, scalable pricing, and features like structured reply events and prompt‑injection scanning, targeting developers building AI‑driven communication workflows.
image: https://mails.ai/opengraph-image?0a8355ca24bf13de
jsonld:
- class_count: 58
  name: Mails Ai Context
  property_count: 202
  slug: mails-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at help.mails.ai.
  name: mails-ai MCP Server
  slug: mails-ai-mcp-yml
modified: '2026-10-30'
name: mails-ai
nav: Providers
network: true
overview: 'mails-ai publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, API Keys API, and 16 more. Tagged areas include Company, Artificial Intelligence, Email, Infrastructure, and Agents.


  The mails-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  mails-ai''s developer surface includes sandbox, authentication, pricing, changelog, engineering blog, API reference, getting-started guide, and 32 more developer resources.'
plans:
- name: Mails Ai Plans Pricing
  plan_count: 3
  slug: mails-ai-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: mails-ai API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: mails-ai-rules
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 67.7
    developer_ergonomics: 48.2
    discoverability: 56.7
    operational_transparency: 17.1
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: unknown
    skills: derived
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
screenshot: https://apis.io/screenshots/mails-ai/mails-ai-2026-11-03T135251.png
security:
- kind: authentication
  name: Mails Ai Authentication
  slug: mails-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mails Ai Domain Security
  slug: mails-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mails Ai Vulnerability Disclosure
  slug: mails-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mails Ai Trust Center
  slug: mails-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 4
skills:
- name: mails-ai-create-and-retrieve-label
  slug: mails-ai-create-and-retrieve-label
- name: mails-ai-create-and-send-draft
  slug: mails-ai-create-and-send-draft
- name: mails-ai-manage-webhook
  slug: mails-ai-manage-webhook
- name: mails-ai-simulate-and-retrieve
  slug: mails-ai-simulate-and-retrieve
slug: mails-ai
tags:
- Company
- Artificial Intelligence
- Email
- Infrastructure
- Agents
website: https://mails.ai/
---
