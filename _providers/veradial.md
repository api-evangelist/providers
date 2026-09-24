---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: Remote, read-only Model Context Protocol server (Streamable HTTP) that lets a customer's own AI assistant - Claude, ChatGPT, Codex or any MCP client - read that customer's VeraDial account - calls wit
  name: VeraDial MCP Server
  slug: mcp
- baseURL: https://api.veradial.com/api/v1/integrations/zapier
  baseurl_source: declared
  description: 'REST Hooks integration API used by VeraDial''s native Zapier app and documented for direct callers - test a vdk_ API key, list selectable phone lines, fetch event samples, and subscribe or unsubscribe '
  name: VeraDial Zapier Integration API
  slug: zapier-integration-api
artifact_total: 17
asyncapis:
- description: ''
  name: Veradial Webhooks
  slug: veradial-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/rate-limits/veradial-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/veradial-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/plans/veradial-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veradial-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/rules/veradial-rules.yml
  title: ''
  type: Spectral
  url: rules/veradial-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/json-ld/veradial-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veradial-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/vocabulary/veradial-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veradial-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/asyncapi/veradial-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/veradial-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/data-model/veradial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veradial-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/changelog/veradial-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/veradial-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/conventions/veradial-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/veradial-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/conventions/veradial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veradial-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/authentication/veradial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veradial-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/scopes/veradial-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/veradial-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/lifecycle/veradial-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/veradial-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/errors/veradial-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/veradial-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/conformance/veradial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veradial-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/overlays/veradial-zapier-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/veradial-zapier-integration-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/llms/veradial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veradial-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/mcp/veradial-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/veradial-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/mcp/veradial-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/veradial-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/well-known/veradial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/veradial-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/hosts/veradial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veradial-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/vendors/veradial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veradial-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/veradial/refs/heads/main/security/veradial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veradial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://veradial.com/
- group: docs
  title: ''
  type: Documentation
  url: https://veradial.com/help
- group: start
  title: ''
  type: DeveloperPortal
  url: https://veradial.com/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://veradial.com/help/zapier-integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://veradial.com/help/setup-veradial-first-screened-call
- group: operate
  title: ''
  type: Support
  url: https://veradial.com/faq
- group: company
  title: ''
  type: Blog
  url: https://veradial.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://veradial.com/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://veradial.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.veradial.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.veradial.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veradial.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veradial.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VeraDial
- group: other
  title: ''
  type: X
  url: https://x.com/VeraDialApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/112327687/
created: '2026-09-23'
description: VeraDial is an AI receptionist and business phone app for small businesses in the United States and Canada, built by Graham Thomson in Toronto. It gives a business a dedicated US or Canadian number with Vera, an AI receptionist that answers calls and texts 24/7, screens callers, takes messages, books appointments and places outbound AI calls. Developers and agents reach an account three ways - a read-only remote MCP server at api.veradial.com/mcp secured with OAuth 2.1, a Zapier REST Hooks integration API authenticated with vdk_ API keys, and signed HMAC event webhooks for Make, n8n or your own service.
image: https://veradial.com/opengraph-image
json_schemas:
- name: GetKeysResponse
  property_count: 3
  slug: veradial-get-keys-response
- name: GetLinesResponse
  property_count: 1
  slug: veradial-get-lines-response
- name: GetSamplesResponse
  property_count: 9
  slug: veradial-get-samples-response
- name: PostHooksRequest
  property_count: 3
  slug: veradial-post-hooks-request
- name: PostKeysRequest
  property_count: 1
  slug: veradial-post-keys-request
- name: PostKeysResponse
  property_count: 1
  slug: veradial-post-keys-response
jsonld:
- class_count: 9
  name: Veradial Context
  property_count: 17
  slug: veradial-context
layout: provider
mcp_servers:
- description: ''
  name: VeraDial MCP Server
  slug: veradial-mcp-server
modified: '2026-09-23'
name: VeraDial
nav: Providers
network: true
overview: 'VeraDial publishes 1 API on the [APIs.io](https://apis.io/) network: Zapier Integration API. Tagged areas include AI Receptionist, Business Phone, Telephony, Voice AI, and SMS.


  The VeraDial catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  VeraDial''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Veradial Plans Pricing
  plan_count: 4
  slug: veradial-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Veradial Rate Limits
  slug: veradial-rate-limits
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: VeraDial API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: veradial-rules
scopes:
- name: Veradial Scopes
  scope_count: 3
  slug: veradial-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 83.8
    catalog_earned_first_party: 20.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 34.4
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Veradial Authentication
  slug: veradial-authentication
  summary_line: http-bearer/oauth2 · 4 schemes
- kind: domain-security
  name: Veradial Domain Security
  slug: veradial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veradial
tags:
- AI Receptionist
- Business Phone
- Telephony
- Voice AI
- SMS
- Webhook
- MCP
- Small Business
website: https://veradial.com/
---
