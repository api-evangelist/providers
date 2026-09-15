---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-09-14'
api_count: 1
apis:
- baseURL: https://secure.agree.com/api/v1
  baseurl_source: declared
  description: 'REST API for the Agree contract-to-cash platform. 56 operations across six resources: Agreements (create from templates, assign signature fields to recipients, send, fetch executed PDFs, soft delete),'
  name: Agree API
  slug: agree-api
artifact_total: 8
asyncapis:
- description: Real-time event notifications from the Agree contract-to-cash platform. Agree POSTs a signed JSON body to endpoints you register through POST /api/v1/webhooks. Twelve event types are published, coveri
  name: Agree.com Webhooks
  slug: agree-com-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://agree.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agree.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://secure.agree.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://secure.agree.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://secure.agree.com/documentation#section/Introduction/Quick-Start
- group: commercial
  title: ''
  type: Pricing
  url: https://agree.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://secure.agree.com/signup
- group: start
  title: ''
  type: Login
  url: https://secure.agree.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agree.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agree.com/privacy
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/openapi/agree-com-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/agree-com-api-openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/mcp/agree-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agree-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/well-known/agree-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agree-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/authentication/agree-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agree-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/scopes/agree-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agree-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/conventions/agree-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agree-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/errors/agree-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agree-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/data-model/agree-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agree-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/lifecycle/agree-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agree-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/conformance/agree-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agree-com-conformance.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/asyncapi/agree-com-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/agree-com-webhooks-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/asyncapi/agree-com-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/agree-com-webhooks-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/llms/agree-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agree-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/overlays/agree-com-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agree-com-api-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/plans/agree-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agree-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/rate-limits/agree-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agree-com-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/packages/agree-com-packages.yml
  title: ''
  type: Packages
  url: packages/agree-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agree-com/refs/heads/main/security/agree-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agree-com-domain-security.yml
created: '2026-09-12'
description: Agree.com is a contract-to-cash platform that combines free, unlimited e-signatures with invoicing, billing and integrated payments, positioning itself directly against DocuSign and Bill.com by giving the signature product away and monetizing the money movement that follows it. The company raised a $7.2M seed round led by Pelion Venture Partners in May 2025 after a $3M pre-seed led by Better Tomorrow Ventures. It markets an "agentic revenue operating system" built from named AI agents for contracts, billing, collections, recovery, reconciliation and insight. For developers it publishes a 56-operation REST API covering agreements, invoices, contacts, customers, cash-flow and recovery reporting, and webhooks, described by a real OpenAPI 3.0 document served anonymously at secure.agree.com/documentation/openapi, plus a hosted remote MCP server at secure.agree.com/mcp discoverable through RFC 9728 protected resource metadata and guarded by an OAuth 2.1 authorization server with PKCE
  and dynamic client registration.
image: https://agree.com/img/social/social-media-card.png
layout: provider
mcp_servers:
- description: 'Agree.com operates a hosted, remote Model Context Protocol server at https://secure.agree.com/mcp. It was discovered through RFC 9728 protected-resource metadata rather than the documentation: the res'
  name: Agree.com MCP Server
  slug: agreecom-mcp-server
modified: '2026-09-12'
name: Agree.com
nav: Providers
network: true
overview: 'Agree.com publishes 1 API on the [APIs.io](https://apis.io/) network: Agree API. Tagged areas include Agreements, Electronic Signature, Contract Management, Invoicing, and Billing.


  The Agree.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agree.com''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Agree Com Plans Pricing
  plan_count: 3
  slug: agree-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Agree Com Rate Limits
  slug: agree-com-rate-limits
scopes:
- name: Agree Com Scopes
  scope_count: 0
  slug: agree-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 51.8
    discoverability: 68.5
    operational_transparency: 7.9
  previous_composite: 50.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agree Com Authentication
  slug: agree-com-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Agree Com Domain Security
  slug: agree-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agree-com
tags:
- Agreements
- Electronic Signature
- Contract Management
- Invoicing
- Billing
- Payments
- Accounts Receivable
- Fintech
- Financial-Services
- Webhook
- MCP
- agent-native
website: https://agree.com/
---
