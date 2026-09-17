---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 74.6
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'Hosted, first-class MCP server over HTTP with OAuth auth (interactive auto-registration or client_credentials for M2M). Ships MCP tools (query insights, context, customers, themes, competitors) and a '
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server
- description: 'Set of ~25 pre-built Claude Code skills distributed as the ''closedloop-skills'' plugin via the Anthropic community marketplace, grouped by team (product/eng/sales/marketing/CS/leadership). Examples: De'
  name: ClosedLoop AI Claude Code Skills
  slug: closedloop-ai-claude-code-skills
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: Trends, cohorts and facet counts over the full dataset.
  name: ClosedLoop AI Analytics API
  slug: closedloop-analytics-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: Competitive pressure derived from your customers' own words. Competitors with a **mention trend over time** (not a static total), and a searchable feed of the exact mentions, each showing the customer
  name: ClosedLoop AI Competitors API
  slug: closedloop-competitors-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: '**Customer context**, the strategic intelligence behind your customers: churn reasons, competitive mentions, satisfaction, pricing perception and more, surfaced from conversations. This is the `/conte'
  name: ClosedLoop AI Context API
  slug: closedloop-context-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: The people and accounts who gave feedback, with CRM context.
  name: ClosedLoop AI Customers API
  slug: closedloop-customers-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: '**Features**: the buildable, shippable children of a theme. Filter by `theme_id`. Same theme → features hierarchy you see on the roadmap.'
  name: ClosedLoop AI Features API
  slug: closedloop-features-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: 'Individual **product insights**: structured, AI-processed feedback items (pain point, severity, workaround, competitor gap, evidence).'
  name: ClosedLoop AI Insights API
  slug: closedloop-insights-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: Connected data sources for your team.
  name: ClosedLoop AI Integrations API
  slug: closedloop-integrations-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: Service metadata.
  name: ClosedLoop AI Meta API
  slug: closedloop-meta-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: The current product, product-area, and feature-area vocabulary for the team.
  name: ClosedLoop AI Products API
  slug: closedloop-products-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: '**Themes**: top-level problem clusters of related insights, RIC-scored. The "what should we build?" surface. Each theme rolls up one or more buildable features.'
  name: ClosedLoop AI Themes API
  slug: closedloop-themes-api
- baseURL: https://api.closedloop.sh/v1
  baseurl_source: declared
  description: Credit consumption and usage records for billing transparency.
  name: ClosedLoop AI Usage API
  slug: closedloop-usage-api
artifact_total: 23
asyncapis:
- description: ''
  name: Closedloop Webhooks
  slug: closedloop-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/overlays/closedloop-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/closedloop-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.closedloop.sh/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://closedloop.sh/docs
- group: docs
  title: ''
  type: Documentation
  url: https://closedloop.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://closedloop.sh/docs/api-reference/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://closedloop.sh/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://closedloop.sh/pricing
- group: company
  title: ''
  type: Blog
  url: https://closedloop.sh/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.closedloop.sh/signup
- group: start
  title: ''
  type: Login
  url: https://app.closedloop.sh/login
- group: operate
  title: ''
  type: Support
  url: https://closedloop.sh/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://closedloop.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://closedloop.sh/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/closed-loop-ai
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/a2a/closedloop-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/closedloop-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/well-known/closedloop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/closedloop-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/packages/closedloop-packages.yml
  title: ''
  type: Packages
  url: packages/closedloop-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/cli/closedloop-cli.yml
  title: ''
  type: CLI
  url: cli/closedloop-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/conventions/closedloop-conventions.yml
  title: ''
  type: Conventions
  url: conventions/closedloop-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/errors/closedloop-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/closedloop-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/data-model/closedloop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/closedloop-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/authentication/closedloop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/closedloop-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/scopes/closedloop-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/closedloop-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/rate-limits/closedloop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/closedloop-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/plans/closedloop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/closedloop-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/lifecycle/closedloop-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/closedloop-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/conformance/closedloop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/closedloop-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/security/closedloop-trust-center.yml
  title: ''
  type: Compliance
  url: security/closedloop-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/security/closedloop-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/closedloop-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/security/closedloop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/closedloop-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/asyncapi/closedloop-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/closedloop-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/llms/closedloop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/closedloop-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://closedloop.sh/docs/llms.txt
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@closedloop.sh
created: '2026-08-30'
description: Product-intelligence platform that turns customer conversations and feedback (Gong, Fireflies, Slack, Zendesk, Intercom, Salesforce, HubSpot, surveys, product usage; 40+ integrations) into structured, source-traceable product insights, themes, buildable features, and prioritized roadmap decisions. Exposes a read-only /v1 REST API, a hosted MCP server, an llms.txt index, and published Claude Code skills.
image: https://closedloop.sh/assets/images/og-image.png
layout: provider
mcp_servers:
- description: 'Hosted remote MCP over Streamable HTTP with OAuth 2.1. deployment.mode=remote, endpoint https://mcp.closedloop.sh (EU: https://eu.mcp.closedloop.sh). Verified by probe 2026-08-30: POST tools/list retu'
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server
- description: LIVE MCP, OAuth-gated. NOTE the path -- the endpoint is the HOST ROOT; https://mcp.closedloop.sh/mcp returns 404 ROUTE_NOT_FOUND. Verified 2026-08-30.
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server-2
- description: EU regional MCP endpoint. Verified 2026-08-30, same 401 OAuth challenge.
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server-3
modified: '2026-08-30'
name: ClosedLoop AI
nav: Providers
network: true
overview: 'ClosedLoop AI publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Competitors API, Context API, and 8 more. Tagged areas include Product Intelligence, Customer Feedback, Voice of Customer, Product Management, and Agentic AI.


  The ClosedLoop AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ClosedLoop AI''s developer surface includes documentation, API reference, quickstart, pricing, engineering blog, signup flow, support, and 28 more developer resources.'
plans:
- name: Closedloop Plans Pricing
  plan_count: 3
  slug: closedloop-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Closedloop Rate Limits
  slug: closedloop-rate-limits
scopes:
- name: Closedloop Scopes
  scope_count: 0
  slug: closedloop-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 65.6
    developer_ergonomics: 67.9
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 61.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/closedloop/refs/heads/main/screenshots/closedloop-2026-09-02T145114.png
security:
- kind: authentication
  name: Closedloop Authentication
  slug: closedloop-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Closedloop Domain Security
  slug: closedloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Closedloop Trust Center
  slug: closedloop-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, FedRAMP
slug: closedloop
tags:
- Product Intelligence
- Customer Feedback
- Voice of Customer
- Product Management
- Agentic AI
- MCP
- SaaS analytics
- A2A
- SCIM
- Product Discovery
website: https://www.closedloop.sh/
---
