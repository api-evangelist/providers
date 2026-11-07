---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 73.8
  scored_at: '2026-11-06'
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
artifact_total: 28
asyncapis:
- description: ''
  name: Closedloop Webhooks
  slug: closedloop-webhooks
common:
- group: other
  href: https://artifacts.apis.io/closedloop/capabilities/closedloop-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/closedloop-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/closedloop/overlays/closedloop-public-api-overlay.yaml
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
  href: https://artifacts.apis.io/closedloop/a2a/closedloop-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/closedloop-a2a.yml
- group: agent
  href: https://artifacts.apis.io/closedloop/well-known/closedloop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/closedloop-well-known.yml
- group: build
  href: https://artifacts.apis.io/closedloop/packages/closedloop-packages.yml
  title: ''
  type: Packages
  url: packages/closedloop-packages.yml
- group: build
  href: https://artifacts.apis.io/closedloop/cli/closedloop-cli.yml
  title: ''
  type: CLI
  url: cli/closedloop-cli.yml
- group: design
  href: https://artifacts.apis.io/closedloop/conventions/closedloop-conventions.yml
  title: ''
  type: Conventions
  url: conventions/closedloop-conventions.yml
- group: design
  href: https://artifacts.apis.io/closedloop/errors/closedloop-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/closedloop-problem-types.yml
- group: design
  href: https://artifacts.apis.io/closedloop/data-model/closedloop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/closedloop-data-model.yml
- group: auth
  href: https://artifacts.apis.io/closedloop/authentication/closedloop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/closedloop-authentication.yml
- group: auth
  href: https://artifacts.apis.io/closedloop/scopes/closedloop-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/closedloop-scopes.yml
- group: operate
  href: https://artifacts.apis.io/closedloop/rate-limits/closedloop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/closedloop-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/closedloop/plans/closedloop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/closedloop-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/closedloop/lifecycle/closedloop-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/closedloop-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/closedloop/conformance/closedloop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/closedloop-conformance.yml
- group: auth
  href: https://artifacts.apis.io/closedloop/security/closedloop-trust-center.yml
  title: ''
  type: Compliance
  url: security/closedloop-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/closedloop/security/closedloop-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/closedloop-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/closedloop/security/closedloop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/closedloop-domain-security.yml
- group: design
  href: https://artifacts.apis.io/closedloop/asyncapi/closedloop-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/closedloop-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/closedloop/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/closedloop/llms/closedloop-llms.txt
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
finops:
- has_sources: true
  method: derived
  name: Closedloop Finops
  primary_unit: ''
  service_category: ''
  slug: closedloop-finops
  template: true
image: https://closedloop.sh/assets/images/og-image.png
layout: provider
mcp_servers:
- description: 'Hosted remote MCP over Streamable HTTP with OAuth 2.1. deployment.mode=remote, endpoint https://mcp.closedloop.sh (EU: https://eu.mcp.closedloop.sh). Verified by probe 2026-08-30: POST tools/list retu'
  name: ClosedLoop AI MCP Server
  slug: closedloop-ai-mcp-server
- description: EU regional MCP endpoint. Verified 2026-08-30, same 401 OAuth challenge.
  name: ClosedLoop AI MCP Server
  slug: https-eu-mcp-closedloop-sh
modified: '2026-08-30'
name: ClosedLoop AI
nav: Providers
network: true
overview: 'ClosedLoop AI publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Competitors API, Context API, and 10 more. Tagged areas include Product Intelligence, Customer Feedback, Voice of Customer, Product Management, and AI Agents.


  The ClosedLoop AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ClosedLoop AI''s developer surface includes documentation, API reference, quickstart, pricing, engineering blog, signup flow, support, and 29 more developer resources.'
plans:
- name: Closedloop Plans Pricing
  plan_count: 1
  slug: closedloop-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Closedloop Rate Limits
  slug: closedloop-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: ClosedLoop AI API Rules
  rule_count: 65
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 8
  slug: closedloop-rules
scopes:
- name: Closedloop Scopes
  scope_count: 2
  slug: closedloop-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 57.5
    catalog_earned_first_party: 16.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 75.0
    contract_governance: 31.8
    contract_quality: 65.6
    developer_ergonomics: 67.5
    discoverability: 75.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 62.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/closedloop/closedloop-2026-09-02T145114.png
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
skill_count: 4
skills:
- name: Closedloopai
  slug: closedloop-closedloopai-published-skill
- name: closedloop-competitive-and-churn-signals
  slug: closedloop-competitive-and-churn-signals
- name: closedloop-incremental-insight-export
  slug: closedloop-incremental-insight-export
- name: closedloop-theme-to-roadmap-evidence
  slug: closedloop-theme-to-roadmap-evidence
slug: closedloop
tags:
- Product Intelligence
- Customer Feedback
- Voice of Customer
- Product Management
- AI Agents
- MCP
- SaaS Analytics
- A2A
- SCIM
- Product Discovery
website: https://www.closedloop.sh/
---
