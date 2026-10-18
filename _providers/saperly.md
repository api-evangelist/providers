---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 3
  name: Saperly Agentic Access
  operation_count: 48
  slug: saperly-agentic-access
  summary_line: 48 operations · 24 acting · 3 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Manage the scoped `sk_` API keys agents use to call Saperly. Each key carries a set of scopes, an optional number allow-list, and an optional spend cap; revoke a key when it is no longer needed.
  name: Saperly API Token Registry API
  slug: saperly-api-token-registry-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Ask the built-in workspace assistant a natural-language question and get a text answer back. Backed by an in-network model; availability depends on the operator configuration.
  name: Saperly Assistant API
  slug: saperly-assistant-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Connections — the handler bound to a phone number that answers and talks. Hosted lines run an in-network voice assistant (pick the model, voice, language, and MCP tools); manual lines forward turns to
  name: Saperly Connections API
  slug: saperly-connections-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Track opt-in consent for contacts on your numbers. Record, revoke, list, and check the consent that backs your outbound messaging compliance. (Inbound STOP/START opt-out is handled automatically by th
  name: Saperly Consent API
  slug: saperly-consent-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: The customVoices API from Saperly — 2 operation(s) for customvoices.
  name: Saperly Custom Voices API
  slug: saperly-customvoices-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Service liveness. A lightweight, unauthenticated probe for uptime checks and load balancers.
  name: Saperly Health API
  slug: saperly-health-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: 'Provision and manage scoped `sk_` API keys for the workspace. The workspace is always read from the calling key, never from client input. A key holding the `keys:admin` scope can mint child keys (and '
  name: Saperly Keys API
  slug: saperly-keys-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: 'Discover the spoken languages a connection can use (its `language` field). The list is derived from the voice catalogue — every language here has at least one voice that speaks it (see `GET /voices`) '
  name: Saperly Languages API
  slug: saperly-languages-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Send and list SMS messages on your numbers. Outbound sends are billed per segment and pass through opt-out (STOP) and spend-limit enforcement before reaching the carrier; inbound messages are recorded
  name: Saperly Messaging API
  slug: saperly-messaging-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: 'Phone numbers — provision, list, release, and configure the lines in your workspace. Bind a connection to a number to make it answer calls and messages, set a per-number webhook, and override the SMS '
  name: Saperly Numbers API
  slug: saperly-numbers-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Pricing — get a live quote for what a phone number will cost before you provision it. Returns the customer-facing monthly and upfront prices for a given country and number type, so you can confirm the
  name: Saperly Pricing API
  slug: saperly-pricing-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Read metered usage for the workspace — call and message counts, total call cost and duration, and the current prepaid balance. Aggregated over an optional time window; the balance is point-in-time.
  name: Saperly Usage API
  slug: saperly-usage-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Place and control outbound calls and fetch call records. Audio always stays in-network — there is no live media-control surface here by design. Funds are reserved on start and settled from the carrier
  name: Saperly Voice API
  slug: saperly-voice-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Discover the in-network text-to-speech voices a hosted connection can speak with. Each voice carries its language, so this endpoint also doubles as the catalogue of supported spoken languages (use a v
  name: Saperly Voices API
  slug: saperly-voices-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Workspace administration — read the members, API tokens, webhook endpoints, and audit log for a workspace. Dashboard/management routes keyed by the workspace slug in the path.
  name: Saperly Workspace API
  slug: saperly-workspace-api
- baseURL: https://api.saperly.com
  baseurl_source: declared
  description: Invite teammates to a workspace by email address.
  name: Saperly Workspace Invitations API
  slug: saperly-workspace-invitations-api
artifact_total: 27
asyncapis:
- description: ''
  name: Saperly Webhooks
  slug: saperly-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/rate-limits/saperly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/saperly-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.saperly.com</code
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/agentic-access/saperly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/saperly-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/plans/saperly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/saperly-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/rules/saperly-rules.yml
  title: ''
  type: Spectral
  url: rules/saperly-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/json-ld/saperly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/saperly-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/vocabulary/saperly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/saperly-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/asyncapi/saperly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/saperly-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/data-model/saperly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/saperly-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/conventions/saperly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/saperly-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/conventions/saperly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/saperly-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/authentication/saperly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/saperly-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/scopes/saperly-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/saperly-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/lifecycle/saperly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/saperly-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/errors/saperly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/saperly-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/conformance/saperly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/saperly-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/overlays/saperly-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/saperly-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/llms/saperly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/saperly-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/mcp/saperly-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/saperly-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/mcp/saperly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/saperly-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/well-known/saperly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/saperly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/hosts/saperly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saperly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/vendors/saperly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saperly-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/packages/saperly-packages.yml
  title: ''
  type: SDKs
  url: packages/saperly-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/packages/saperly-packages.yml
  title: ''
  type: Packages
  url: packages/saperly-packages.yml
- group: company
  title: ''
  type: Website
  url: https://saperly.com
- group: docs
  title: ''
  type: Documentation
  url: https://saperly.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://saperly.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://saperly.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://saperly.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Saperly
- group: start
  title: ''
  type: SignUp
  url: https://saperly.com/sign-in
- group: start
  title: ''
  type: Login
  url: https://saperly.com/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://saperly.com/#pricing
- group: auth
  title: ''
  type: Security
  url: https://saperly.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saperly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saperly.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/security/saperly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/saperly-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/security/saperly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saperly-domain-security.yml
created: '2026-10-07'
description: 'Saperly is the phone carrier for AI agents: one API call gives an agent a real phone number with inbound and outbound voice and SMS, routing to a hosted in-network voice agent or to your own runtime (manual mode), and TCPA compliance enforced in the carrier layer — AI disclosure, consent records, 10DLC brand/campaign registration and an append-only audit trail. The v2 REST API at api.saperly.com (48 operations, OpenAPI 3.2) covers numbers, connections, messaging, voice, voices, consent, pricing quotes, usage and ceiling-bounded scoped API keys; a remote MCP server at api.saperly.com/mcp (Streamable HTTP, OAuth 2.1 or sap_sk_ bearer) exposes the same surface as tools, with official Node and Python SDKs, signed webhooks and prepaid usage-based pricing.'
image: https://saperly.com/saperly-flower-hero.jpg
jsonld:
- class_count: 32
  name: Saperly Context
  property_count: 30
  slug: saperly-context
layout: provider
mcp_servers:
- description: Saperly operates a remote MCP server at https://api.saperly.com/mcp (Streamable HTTP, JSON-RPC 2.0) authenticated with a scoped sap_sk_ bearer key or an MCP OAuth 2.1 access token issued by https://sa
  name: Saperly MCP Server
  slug: saperly-mcp-yml
modified: '2026-10-07'
name: Saperly
nav: Providers
network: true
overview: 'Saperly publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Token Registry API, Assistant API, Connections API, and 13 more. Tagged areas include Telephony, Voice, SMS, Phone Numbers, and AI Agents.


  The Saperly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Saperly''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, and 33 more developer resources.'
plans:
- name: Saperly Plans Pricing
  plan_count: 2
  slug: saperly-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Saperly Rate Limits
  slug: saperly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Saperly API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 4
  slug: saperly-rules
scopes:
- name: Saperly Scopes
  scope_count: 7
  slug: saperly-scopes
  summary_line: 7 scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 58.0
    developer_ergonomics: 61.3
    discoverability: 80.0
    operational_transparency: 23.7
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 40.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/saperly/refs/heads/main/screenshots/saperly-2026-10-11T125628.png
security:
- kind: authentication
  name: Saperly Authentication
  slug: saperly-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Saperly Domain Security
  slug: saperly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Saperly Vulnerability Disclosure
  slug: saperly-vulnerability-disclosure
  summary_line: no policy recorded
slug: saperly
tags:
- Telephony
- Voice
- SMS
- Phone Numbers
- AI Agents
- Consent
- Compliance
- MCP
- Messaging
- Communications
website: https://saperly.com
---
