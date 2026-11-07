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
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 5
  name: Chatrail Dev Agentic Access
  operation_count: 104
  slug: chatrail-dev-agentic-access
  summary_line: 104 operations · 63 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Optional, per connection, off by default.
  name: chatrail-dev AI API
  slug: chatrail-dev-ai-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Dashboard sign-in. Not used by API clients.
  name: chatrail-dev Auth API
  slug: chatrail-dev-auth-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Checkout, the customer portal and Creem webhooks.
  name: chatrail-dev Billing API
  slug: chatrail-dev-billing-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: WhatsApp numbers and their pairing lifecycle.
  name: chatrail-dev Connections API
  slug: chatrail-dev-connections-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Creating and running WhatsApp groups from a connected number.
  name: chatrail-dev Groups API
  slug: chatrail-dev-groups-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Called by the transport, not by you.
  name: chatrail-dev Internal API
  slug: chatrail-dev-internal-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Workspace tools for a coding assistant.
  name: chatrail-dev MCP API
  slug: chatrail-dev-mcp-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Sending, delivery state and export.
  name: chatrail-dev Messages API
  slug: chatrail-dev-messages-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Health and metrics.
  name: chatrail-dev Operational API
  slug: chatrail-dev-operational-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: People who asked not to be messaged. Sends to them are refused.
  name: chatrail-dev Opt Outs API
  slug: chatrail-dev-opt-outs-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Recurring sends.
  name: chatrail-dev Schedules API
  slug: chatrail-dev-schedules-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Membership and invitations. Dashboard sessions only.
  name: chatrail-dev Team API
  slug: chatrail-dev-team-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Where inbound events and delivery updates are sent.
  name: chatrail-dev Webhooks API
  slug: chatrail-dev-webhooks-api
- baseURL: https://www.chatrail.dev
  baseurl_source: declared
  description: Identity, credentials, plan and usage.
  name: chatrail-dev Workspace API
  slug: chatrail-dev-workspace-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/chatrail-dev/agentic-access/chatrail-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chatrail-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/chatrail-dev/rate-limits/chatrail-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chatrail-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/chatrail-dev/rules/chatrail-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/chatrail-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/chatrail-dev/vocabulary/chatrail-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chatrail-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/chatrail-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/chatrail-dev/changelog/chatrail-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chatrail-dev-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.chatrail.dev/security
- group: auth
  href: https://artifacts.apis.io/chatrail-dev/authentication/chatrail-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chatrail-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/chatrail-dev/errors/chatrail-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chatrail-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chatrail-dev/conformance/chatrail-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chatrail-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chatrail-dev/llms/chatrail-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatrail-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/chatrail-dev/mcp/chatrail-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chatrail-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/chatrail-dev/well-known/chatrail-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chatrail-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/chatrail-dev/well-known/chatrail-dev-chatrail-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chatrail-dev-chatrail-security.txt
- group: agent
  href: https://artifacts.apis.io/chatrail-dev/well-known/chatrail-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatrail-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/chatrail-dev/hosts/chatrail-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatrail-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatrail-dev/vendors/chatrail-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatrail-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/chatrail-dev/packages/chatrail-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/chatrail-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/chatrail-dev/packages/chatrail-dev-packages.yml
  title: ''
  type: Packages
  url: packages/chatrail-dev-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.chatrail.dev/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://www.chatrail.dev/status
- group: auth
  title: ''
  type: Security
  url: https://www.chatrail.dev/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.chatrail.dev/changelog
- group: auth
  href: https://artifacts.apis.io/chatrail-dev/security/chatrail-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chatrail-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chatrail-dev/security/chatrail-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chatrail-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chatrail-dev/security/chatrail-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatrail-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatrail.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.chatrail.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chatrail.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.chatrail.dev/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chatrail.dev/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.chatrail.dev/help
- group: company
  title: ''
  type: Blog
  url: https://www.chatrail.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatrail
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chatrail.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chatrail.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chatrail.dev/privacy
created: '2026-10-30'
description: ChatRail provides a context‑aware WhatsApp API for developers, enabling them to send alerts, receive replies, and enrich messages with AI‑generated answers based on attached data. The service uses WhatsApp Linked Devices (the same connection as WhatsApp Web) and does not require Meta Business Platform approval. ChatRail is published by Cortex Software Services Ltd and offers webhooks, a free sandbox, pricing plans, and extensive documentation.
image: https://www.chatrail.dev/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.chatrail.dev.
  name: chatrail-dev MCP Server
  slug: chatrail-dev-mcp-yml
modified: '2026-10-30'
name: chatrail-dev
nav: Providers
network: true
overview: 'chatrail-dev publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Auth API, Billing API, and 11 more. Tagged areas include WhatsApp, Messaging, Artificial Intelligence, and Developers.


  The chatrail-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  chatrail-dev''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 30 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Chatrail Dev Rate Limits
  slug: chatrail-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: chatrail-dev API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: chatrail-dev-rules
scopes:
- name: Chatrail Dev Scopes
  scope_count: 0
  slug: chatrail-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.7
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 49.4
    developer_ergonomics: 48.1
    discoverability: 56.7
    operational_transparency: 48.7
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chatrail-dev/chatrail-dev-2026-11-03T123916.png
security:
- kind: authentication
  name: Chatrail Dev Authentication
  slug: chatrail-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chatrail Dev Domain Security
  slug: chatrail-dev-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Chatrail Dev Vulnerability Disclosure
  slug: chatrail-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Chatrail Dev Trust Center
  slug: chatrail-dev-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: send-message
  slug: chatrail-dev-send_message
slug: chatrail-dev
tags:
- WhatsApp
- Messaging
- Artificial Intelligence
- Developers
website: https://chatrail.dev/
---
