---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Karada Agentic Access
  operation_count: 74
  slug: karada-agentic-access
  summary_line: 74 operations · 43 acting
api_count: 1
apis:
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The admin API from Karada AI — 9 operation(s) for admin.
  name: Karada AI Admin API
  slug: karada-admin-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The auth API from Karada AI — 4 operation(s) for auth.
  name: Karada AI Auth API
  slug: karada-auth-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The billing API from Karada AI — 10 operation(s) for billing.
  name: Karada AI Billing API
  slug: karada-billing-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The deployments API from Karada AI — 5 operation(s) for deployments.
  name: Karada AI Deployments API
  slug: karada-deployments-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The feedback API from Karada AI — 1 operation(s) for feedback.
  name: Karada AI Feedback API
  slug: karada-feedback-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The gateway API from Karada AI — 11 operation(s) for gateway.
  name: Karada AI Gateway API
  slug: karada-gateway-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The marketplace API from Karada AI — 5 operation(s) for marketplace.
  name: Karada AI Marketplace API
  slug: karada-marketplace-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The mcp API from Karada AI — 2 operation(s) for mcp.
  name: Karada AI MCP API
  slug: karada-mcp-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The newsletter API from Karada AI — 1 operation(s) for newsletter.
  name: Karada AI Newsletter API
  slug: karada-newsletter-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The pricing API from Karada AI — 1 operation(s) for pricing.
  name: Karada AI Pricing API
  slug: karada-pricing-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The projects API from Karada AI — 6 operation(s) for projects.
  name: Karada AI Projects API
  slug: karada-projects-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The registry API from Karada AI — 4 operation(s) for registry.
  name: Karada AI Registry API
  slug: karada-registry-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The system API from Karada AI — 1 operation(s) for system.
  name: Karada AI System API
  slug: karada-system-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The teams API from Karada AI — 2 operation(s) for teams.
  name: Karada AI Teams API
  slug: karada-teams-api
- baseURL: https://api.karada.ai
  baseurl_source: declared
  description: The user API from Karada AI — 1 operation(s) for user.
  name: Karada AI User API
  slug: karada-user-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/karada/agentic-access/karada-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/karada-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/karada/plans/karada-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/karada-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/karada/rules/karada-rules.yml
  title: ''
  type: Spectral
  url: rules/karada-rules.yml
- group: design
  href: https://artifacts.apis.io/karada/vocabulary/karada-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/karada-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/karada/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/karada/authentication/karada-authentication.yml
  title: ''
  type: Authentication
  url: authentication/karada-authentication.yml
- group: design
  href: https://artifacts.apis.io/karada/errors/karada-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/karada-problem-types.yml
- group: design
  href: https://artifacts.apis.io/karada/conformance/karada-conformance.yml
  title: ''
  type: Conformance
  url: conformance/karada-conformance.yml
- group: agent
  href: https://artifacts.apis.io/karada/llms/karada-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/karada-llms.txt
- group: other
  href: https://artifacts.apis.io/karada/a2a/karada-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/karada-a2a.yml
- group: agent
  href: https://artifacts.apis.io/karada/mcp/karada-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/karada-mcp.yml
- group: agent
  href: https://artifacts.apis.io/karada/well-known/karada-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/karada-well-known.yml
- group: other
  href: https://artifacts.apis.io/karada/hosts/karada-hosts.yml
  title: ''
  type: Hosts
  url: hosts/karada-hosts.yml
- group: other
  href: https://artifacts.apis.io/karada/vendors/karada-vendors.yml
  title: ''
  type: Vendors
  url: vendors/karada-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://karada.ai/help
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.karada.ai/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.karada.ai/playbooks/stripe-api-to-mcp.md
- group: auth
  href: https://artifacts.apis.io/karada/security/karada-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/karada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://karada.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.karada.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://karada.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://karada.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karada.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karada.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://karada.ai/login
created: '2026-10-17'
description: Karada AI provides an infrastructure platform that turns APIs into Go MCP (Model Context Protocol) servers with one‑click plugins and gateways. It offers tools to auto‑compile APIs into MCP servers, keep them in sync via CI/CD, and publish to a registry for use across AI assistants like Claude, Cursor, and others. The platform includes a free starter tier, detailed documentation, pricing plans, a blog, and community support via Discord.
image: https://karada.ai/og.png?v=20260917
layout: provider
mcp_servers:
- description: Remote MCP server at gateway.karada.ai requiring OAuth.
  name: Karada AI MCP Server
  slug: karada-mcp-yml
modified: '2026-10-17'
name: Karada AI
nav: Providers
network: true
overview: 'Karada AI publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, Billing API, and 12 more. Tagged areas include Company, Artificial Intelligence, Platform, MCP, and Automation.


  The Karada AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Karada AI''s developer surface includes authentication, support, getting-started guide, API reference, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Karada Plans Pricing
  plan_count: 4
  slug: karada-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Karada AI API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: karada-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 39.3
    developer_ergonomics: 49.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Karada Authentication
  slug: karada-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Karada Domain Security
  slug: karada-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: karada-auth-login-flow
  slug: karada-auth-login-flow
- name: karada-billing-checkout
  slug: karada-billing-checkout
slug: karada
tags:
- Company
- Artificial Intelligence
- Platform
- MCP
- Automation
website: https://karada.ai/
---
