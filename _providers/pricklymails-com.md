---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 74
  human_in_the_loop: 14
  name: Pricklymails Com Agentic Access
  operation_count: 132
  slug: pricklymails-com-agentic-access
  summary_line: 132 operations · 74 acting · 14 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: The authenticated user's own profile, email, password, and 2FA.
  name: pricklymails-com Account API
  slug: pricklymails-com-account-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: The AI agents allowed to act on your account, each with its own scopes.
  name: pricklymails-com Agents API
  slug: pricklymails-com-agents-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Create, list, update, and revoke API keys, and inspect the key in use.
  name: pricklymails-com API Keys API
  slug: pricklymails-com-api-keys-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Registration, login, token refresh, password reset, and 2FA.
  name: pricklymails-com Auth API
  slug: pricklymails-com-auth-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: 'Verify a list of addresses: submit, append, list, and read the results.'
  name: pricklymails-com Batches API
  slug: pricklymails-com-batches-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Checkout and billing portal sessions.
  name: pricklymails-com Billing API
  slug: pricklymails-com-billing-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Public, unauthenticated pricing and plan configuration.
  name: pricklymails-com Config API
  slug: pricklymails-com-config-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Your verification jobs and their details.
  name: pricklymails-com Jobs API
  slug: pricklymails-com-jobs-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: What happened on your account, as a read-only history.
  name: pricklymails-com Notifications API
  slug: pricklymails-com-notifications-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: 'OAuth 2.1 authorization server: dynamic client registration (RFC 7591), discovery metadata (RFC 8414), and the authorization-code-with-PKCE flow (authorize, consent, token).'
  name: pricklymails-com OAuth API
  slug: pricklymails-com-oauth-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: The authenticated user's active sessions.
  name: pricklymails-com Sessions API
  slug: pricklymails-com-sessions-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Your usage statistics, and the public service figures.
  name: pricklymails-com Stats API
  slug: pricklymails-com-stats-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: The caller's subscription plan and status.
  name: pricklymails-com Subscription API
  slug: pricklymails-com-subscription-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Verify one address and read its result.
  name: pricklymails-com Verification API
  slug: pricklymails-com-verification-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Your token balance and its ledger.
  name: pricklymails-com Wallet API
  slug: pricklymails-com-wallet-api
- baseURL: https://api.pricklymails.com
  baseurl_source: declared
  description: Webhook endpoints that receive your verification events.
  name: pricklymails-com Webhooks API
  slug: pricklymails-com-webhooks-api
artifact_total: 32
common:
- group: agent
  href: https://artifacts.apis.io/pricklymails-com/agentic-access/pricklymails-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pricklymails-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/pricklymails-com/rate-limits/pricklymails-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pricklymails-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/pricklymails-com/rules/pricklymails-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pricklymails-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pricklymails-com/json-ld/pricklymails-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pricklymails-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pricklymails-com/vocabulary/pricklymails-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pricklymails-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pricklymails-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pricklymails-com/data-model/pricklymails-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pricklymails-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pricklymails-com/changelog/pricklymails-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pricklymails-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/pricklymails-com/authentication/pricklymails-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pricklymails-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/pricklymails-com/errors/pricklymails-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pricklymails-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pricklymails-com/conformance/pricklymails-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pricklymails-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pricklymails-com/llms/pricklymails-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pricklymails-com-llms.txt
- group: build
  href: https://artifacts.apis.io/pricklymails-com/mcp/pricklymails-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pricklymails-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/pricklymails-com/mcp/pricklymails-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pricklymails-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pricklymails-com/well-known/pricklymails-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pricklymails-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pricklymails-com/hosts/pricklymails-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pricklymails-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://pricklymails.com/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://pricklymails.com/changelog
- group: auth
  href: https://artifacts.apis.io/pricklymails-com/security/pricklymails-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pricklymails-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pricklymails.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pricklymails.com/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://pricklymails.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://pricklymails.com/docs/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://pricklymails.com/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://pricklymails.com/docs/billing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pricklymails.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pricklymails.com/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://pricklymails.com/roadmap
created: '2026-10-31'
description: PricklyMails provides an EU‑hosted real‑time email verification API that checks syntax, MX records, and probes mailboxes via SMTP where allowed. It flags disposable and role addresses, returns honest verdicts, and refunds checks that cannot be completed. The service is billed per verification using a prepaid token wallet, supports OAuth 2.1 PKCE for AI agents, and offers webhooks, batch processing, and rate‑limit controls.
image: https://pricklymails.com/favicon.ico
json_schemas:
- name: ApiKeyResponse
  property_count: 13
  slug: pricklymails-com-api-key-response
- name: AuthorizationServerMetadataResponse
  property_count: 10
  slug: pricklymails-com-authorization-server-metadata-response
- name: SubmitVerificationResponse
  property_count: 8
  slug: pricklymails-com-submit-verification-response
- name: SubscriptionResponse
  property_count: 9
  slug: pricklymails-com-subscription-response
- name: TokenRequest
  property_count: 6
  slug: pricklymails-com-token-request
- name: WebhookResponse
  property_count: 10
  slug: pricklymails-com-webhook-response
jsonld:
- class_count: 98
  name: Pricklymails Com Context
  property_count: 211
  slug: pricklymails-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.pricklymails.com requiring OAuth.
  name: pricklymails-com MCP Server
  slug: pricklymails-com-mcp-yml
modified: '2026-10-31'
name: pricklymails-com
nav: Providers
network: true
overview: 'pricklymails-com publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, API Keys API, and 13 more. Tagged areas include Email Verification, Software-as-a-Service, Data Validation, and EU-hosted.


  The pricklymails-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pricklymails-com''s developer surface includes changelog, authentication, documentation, getting-started guide, API reference, pricing, and 22 more developer resources.'
plans:
- name: Pricklymails Com Plans Pricing
  plan_count: 0
  slug: pricklymails-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Pricklymails Com Rate Limits
  slug: pricklymails-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: pricklymails-com API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 4
  slug: pricklymails-com-rules
scopes:
- name: Pricklymails Com Scopes
  scope_count: 0
  slug: pricklymails-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 59.9
    developer_ergonomics: 26.7
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pricklymails-com/pricklymails-com-2026-11-03T141605.png
security:
- kind: authentication
  name: Pricklymails Com Authentication
  slug: pricklymails-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pricklymails Com Domain Security
  slug: pricklymails-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: verify-email
  slug: verify-email
slug: pricklymails-com
tags:
- Email Verification
- Software-as-a-Service
- Data Validation
- EU-hosted
website: https://pricklymails.com/
---
