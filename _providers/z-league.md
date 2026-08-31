---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Z League Agentic Access
  operation_count: 7
  slug: z-league-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- description: The Leads API from Z League — 2 operation(s) for leads.
  name: Z League Leads API
  slug: z-league-leads-api
- description: The Webhooks API from Z League — 2 operation(s) for webhooks.
  name: Z League Webhooks API
  slug: z-league-webhooks-api
arazzos:
- description: Register a lead.created webhook, then create a lead. Real inserts fire the webhook so your endpoint is notified. Uses an Idempotency-Key so the create is retry-safe.
  name: MEGA CRM — capture lead and register webhook
  slug: z-league-capture-and-notify
- description: 'Poll the MEGA CRM for leads with stable keyset cursor pagination: fetch the first page sorted by updated_at ascending, then follow next_cursor to fetch the next page.'
  name: MEGA CRM — incremental lead sync
  slug: z-league-incremental-lead-sync
artifact_total: 14
asyncapis:
- description: Outbound webhook event surface for the MEGA public CRM Lead API. MEGA POSTs a signed `lead.created` event to a subscriber-registered public HTTPS endpoint whenever a genuine new lead is created. Deliv
  name: MEGA Public CRM Lead Webhooks
  slug: z-league-lead-webhooks-asyncapi
- description: ''
  name: Z League Lead Webhooks
  slug: z-league-lead-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MEGA Public CRM Lead Leads API
  slug: open-z-league-leads-api
- collection_type: open
  name: MEGA Public CRM Lead Leads Webhooks API
  slug: open-z-league-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/z-league-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/z-league-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/z-league-crm-lead-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gomega.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gomega.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gomega.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gomega.ai/quickstart
- group: company
  title: ''
  type: Website
  url: https://www.gomega.ai
- group: company
  title: ''
  type: Blog
  url: https://www.gomega.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gomega.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.gomega.ai/megapricing
- group: start
  title: ''
  type: Login
  url: https://app.gomega.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gomega.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gomega.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@gomega.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zleague
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/z-league-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/z-league-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/z-league-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/z-league-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/z-league-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/z-league-incremental-lead-sync.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/z-league-capture-and-notify.yml
created: '2026-07-17'
description: 'Z League is an a16z-backed startup that operates the MEGA platform (gomega.ai) — a suite of AI marketing agents that autonomously manage SEO, paid advertising, and website/growth optimization for businesses at a fraction of traditional agency cost. MEGA also ships a built-in CRM, and exposes the MEGA public CRM Lead API: a server-to-server REST API to pull/search leads with cursor pagination, push leads one-at-a-time or in bulk (up to 500) with idempotency and email/phone de-duplication, and register HMAC-signed `lead.created` webhooks. Authentication is an admin-issued, customer-locked, scoped Personal Access Token (Bearer `mega_...`) plus an `x-customer-id` header. The API is documented with an OpenAPI 3.1 spec and a Mintlify developer portal published from the company''s public GitHub org (github.com/zleague).'
image: https://raw.githubusercontent.com/api-evangelist/z-league/refs/heads/main/openapi/z-league-crm-lead-openapi.json
layout: provider
mcp_servers:
- description: ''
  name: Z League MCP Server
  slug: z-league-mcp-server
modified: '2026-07-21'
name: Z League
nav: Providers
network: true
overview: 'Z League publishes 2 APIs on the [APIs.io](https://apis.io/) network: Leads API and Webhooks API. Tagged areas include Company, CRM, Leads, Marketing, and AI Agents.


  The Z League catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Z League''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 17 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Z League Rate Limits
  slug: z-league-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 67.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/z-league/refs/heads/main/screenshots/z-league-2026-08-17T083228.png
security:
- kind: authentication
  name: Z League Authentication
  slug: z-league-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Z League Domain Security
  slug: z-league-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: z-league
tags:
- Company
- CRM
- Leads
- Marketing
- AI Agents
- SEO
- Advertising
- Webhook
- Gaming
website: https://www.gomega.ai
---
