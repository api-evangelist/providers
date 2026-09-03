---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'A live remote Model Context Protocol endpoint serving WINN.AI conversation data to agents. It is published nowhere on the company''s website — it was found by probing RFC 9728 OAuth protected-resource '
  name: WINN.AI MCP API
  slug: mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.winn.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://winn.ai/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://winn.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://winn.ai/web-terms-and-conditions/
- group: start
  title: ''
  type: Login
  url: https://app.winn.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/winnai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.winn.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/winnai-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://winn.ai/support/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/winnai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/winnai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/winnai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/winnai-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/winnai-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/winnai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/winnai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/winnai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/winnai-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/winnai-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/winnai-llms.txt
created: '2026-07-17'
description: Winn.ai is an AI-powered revenue execution platform for B2B sales teams that joins live sales calls to provide real-time playbook guidance, coach representatives on messaging and objection handling, and automate administrative work such as meeting note-taking, follow-up drafting, and CRM data entry. The product sits on top of a team's existing sales stack and reports outcomes including higher playbook adoption, dramatically higher CRM fill rates, and a large reduction in post-call admin work. Winn.ai is a privately held company backed by Insight Partners. WINN.AI sells API access as an Enterprise-plan feature ("Get conversation data and AI insights, in any tool") and runs a live, undocumented remote Model Context Protocol server at https://app.winn.ai/mcp, discovered through the RFC 9728 OAuth protected-resource metadata it publishes; the endpoint is gated by OAuth 2.0 authorization code with PKCE and advertises a single read-only scope, sessions:read. There is no developer
  portal, API reference, OpenAPI document, SDK, CLI, webhook catalog, status page or changelog, and both pricing tiers are sales-gated. The company operates a Vanta-hosted trust center covering SOC 2, ISO 27001 and GDPR.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/winnai.png
layout: provider
mcp_servers:
- description: WINN.AI publishes a remote Model Context Protocol endpoint at https://app.winn.ai/mcp. Its existence is not documented on the marketing site or in any developer portal — it was discovered by probing R
  name: WINN.AI MCP Server
  slug: winnai-mcp-server
modified: '2026-08-13'
name: Winn.ai
nav: Providers
network: true
overview: 'Winn.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Artificial Intelligence, Revenue, and CRM.


  Winn.ai''s developer surface includes pricing, support, authentication, and 17 more developer resources.'
plans:
- name: Winnai Plans Pricing
  plan_count: 2
  slug: winnai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Winnai Rate Limits
  slug: winnai-rate-limits
scopes:
- name: Winnai Scopes
  scope_count: 0
  slug: winnai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 30.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/winnai/refs/heads/main/screenshots/winnai-2026-09-02T170810.png
security:
- kind: authentication
  name: Winnai Authentication
  slug: winnai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Winnai Domain Security
  slug: winnai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Winnai Trust Center
  slug: winnai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: winnai
tags:
- Company
- Sales
- Artificial Intelligence
- Revenue
- CRM
- Sales Enablement
- Conversation Intelligence
- Productivity
website: https://www.winn.ai/
---
