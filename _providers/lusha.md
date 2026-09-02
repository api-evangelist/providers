---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · API keys gated to Scale plan
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Lusha Agentic Access
  operation_count: 58
  slug: lusha-agentic-access
  summary_line: 58 operations · 38 acting
api_count: 2
apis:
- description: Find contacts or companies from known identifiers — contact id, LinkedIn URL, email or name + company; company id, name or domain — and return a non-PII preview with `has` and `canReveal` fields descr
  name: Lusha Search API
  slug: lusha-search-api
- description: 'Reveal full contact and company profiles by Lusha id, with an explicit `reveal` list controlling which fields are unlocked and charged, and optional waterfall fall-through to enabled third-party data '
  name: Lusha Enrich API
  slug: lusha-enrichment-api
- description: Resolve an identifier and return the fully revealed contact or company record in a single call, collapsing the two-phase search-then-enrich pattern where the caller has already decided to spend credit
  name: Lusha Search & Enrich API
  slug: lusha-search-enrich-api
- description: Filter-based search across Lusha's contact and company database — job title, seniority, department, location, company size, revenue, industry, technology and intent — with paged results and a dedupe s
  name: Lusha Prospecting API
  slug: lusha-prospecting-api
- description: AI-powered similarity search that expands a seed list of contacts or companies into comparable profiles, with exclusion lists, a dedupe session id and optional persistence into a Lusha table.
  name: Lusha Lookalikes API
  slug: lusha-lookalike-api
- description: Persona classification over a fixed set of up to 25 named accounts — labels each returned contact decision_maker, potential_champion or end_user with a relevance score. Released 2026-08-12 as the repl
  name: Lusha Buying Group API
  slug: lusha-buying-group-api
- description: Real-world activity data for contacts and companies — promotions and job changes on the contact side; headcount movement, hiring surges, web traffic, IT spend, news classes and LinkedIn activity inten
  name: Lusha Signals API
  slug: lusha-signals-api
- description: Companies ranked by website-visit signals for domains you track, filtered by score band, visitor country, session counts, unique visitors, high-intent pageviews and recency.
  name: Lusha Website Visitors API
  slug: lusha-website-visits-api
- description: Filter discovery for prospecting — enumerates the available filter types and the valid values for each, so callers never guess industry labels, seniority ids or technology names. Charges no credits.
  name: Lusha Filters API
  slug: lusha-filters-api
- description: Persist, organise and enrich contacts in reusable tables with dynamic columns — create, list, read, update, delete tables; add and remove up to 500 entity ids per call; run enrichment columns over a s
  name: Lusha Contacts Tables API
  slug: lusha-contacts-tables-api
- description: The company-side twin of Contacts Tables — persist and enrich company working sets in tables with dynamic columns, capped at 50,000 entities per table and 500 tables per account.
  name: Lusha Companies Tables API
  slug: lusha-companies-tables-api
- description: Subscription management for real-time signal callbacks — bulk create and delete up to 25 items per request, account-level HMAC-SHA256 secret with rotation, delivery test, contact opt-out notifications
  name: Lusha Webhooks API
  slug: lusha-webhooks-api
- description: Credit balance, plan information, per-action credit pricing and the live rate-limit tiers for the minute, hourly and daily windows.
  name: Lusha Account API
  slug: lusha-account-api
- description: 'First-party hosted Model Context Protocol server exposing 22 Lusha tools over streamable HTTP. Authenticates with OAuth 2.1 (scope `mcp`, PKCE S256, dynamic client registration at auth.lusha.com) for '
  name: Lusha MCP Server
  slug: mcp
- description: 'Manage your account and monitor usage. Use this endpoint to: - Monitor credit usage - Understand consumption patterns - Align API usage with plan limits - Support governance and production operations '
  name: Lusha Account Management API
  slug: lusha-account-management-api
- description: Available filters for company searches
  name: Lusha Company Filters API
  slug: lusha-company-filters-api
- description: Available filters for contact searches
  name: Lusha Contact Filters API
  slug: lusha-contact-filters-api
- description: '**What is enrichment?** Enrichment is the process of adding missing or updated data to existing contact or company records. Use enrichment to: - Complete CRM records - Improve outbound accuracy and de'
  name: Lusha Enrichment API
  slug: lusha-enrichment-api
- description: With Lusha's Prospecting API, you can query Lusha's extensive database based on specific criteria (such as job title, seniority, location, and more) to retrieve detailed contact and company informatio
  name: Lusha Prospecting - Search & Enrich API
  slug: lusha-prospecting-search-enrich-api
artifact_total: 44
asyncapis:
- description: ''
  name: Lusha Webhooks
  slug: lusha-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lusha API Documentation Account API
  slug: open-lusha-account-api
- collection_type: open
  name: Lusha API Documentation Buying Group API
  slug: open-lusha-buying-group-api
- collection_type: open
  name: Lusha API Documentation Companies Tables API
  slug: open-lusha-companies-tables-api
- collection_type: open
  name: Lusha API Documentation Contacts Tables API
  slug: open-lusha-contacts-tables-api
- collection_type: open
  name: Lusha API Documentation Enrich API
  slug: open-lusha-enrich-api
- collection_type: open
  name: Lusha API Documentation Filters API
  slug: open-lusha-filters-api
- collection_type: open
  name: Lusha API Documentation Lookalikes API
  slug: open-lusha-lookalikes-api
- collection_type: open
  name: Lusha API Documentation Prospecting API
  slug: open-lusha-prospecting-api
- collection_type: open
  name: Lusha API Documentation Search API
  slug: open-lusha-search-api
- collection_type: open
  name: Lusha API Documentation Search & Enrich API
  slug: open-lusha-search-enrich-api
- collection_type: open
  name: Lusha API Documentation Signals API
  slug: open-lusha-signals-api
- collection_type: open
  name: Lusha API Documentation Webhooks API
  slug: open-lusha-webhooks-api
- collection_type: open
  name: Lusha API Documentation Website Visits API
  slug: open-lusha-website-visits-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.lusha.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lusha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lusha.com/apis/openapi
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lusha.com/apis/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lusha.com/guides/advanced-topics/new-getting-started
- group: operate
  title: ''
  type: Support
  url: https://info.lusha.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lusha.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lusha-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lushadata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lusha.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://dashboard.lusha.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lusha.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lusha.com/legal/privacy-notice/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lushateam/workspace/lusha-s-api/collection/28683568-fc849873-9ae1-47dd-8159-0d4deda04750
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.lusha.com/_spec/apis/@v3/openapi.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lusha-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lusha-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lusha-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lusha-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lusha-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lusha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lusha-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lusha-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lusha-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lusha.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.lusha.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lusha-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lusha.com/changelog
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lusha-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lusha-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lusha.com/trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/lusha-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lusha.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lusha-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lusha-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lusha-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lusha-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/lusha-packages.yml
- group: start
  title: ''
  type: Console
  url: sandbox/lusha-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lusha-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lusha-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lusha-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lusha-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.lusha.com/llms.txt
created: '2026-05-08'
description: Lusha is a B2B sales-intelligence platform that sells verified contact and company data, buying signals and AI recommendations to revenue teams. Its v3 REST API at api.lusha.com exposes 58 operations across thirteen resource families — Search, Enrich, Search & Enrich, Prospecting, Lookalikes, Buying Group, Contacts Tables, Companies Tables, Signals, Website Visits, Filters, Webhooks and Account — behind a single `api_key` header credential, on a search-then-enrich pattern where previews are free of PII and reveals spend credits. Lusha also ships a first-party hosted MCP server at mcp.lusha.com with 22 tools, OAuth 2.1 discovery and official Claude, ChatGPT and Codex connectors, plus HMAC-signed webhooks for real-time signal delivery.
finops:
- name: Lusha Finops
  service_category: Sales Intelligence
  slug: lusha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lusha.png
layout: provider
mcp_servers:
- description: Lusha ships a first-party hosted MCP server at https://mcp.lusha.com plus a local stdio package on npm (@lusha-org/mcp) and a Gemini CLI extension. The hosted endpoint accepts either an OAuth authoriz
  name: Lusha MCP Server
  slug: lusha-mcp-server
modified: '2026-08-13'
name: Lusha
nav: Providers
network: true
overview: 'Lusha publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Search API, Enrich API, Search & Enrich API, and 15 more. Tagged areas include Sales Intelligence, B2B, Enrichment, Contact Data, and Prospecting.


  The Lusha catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lusha''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 38 more developer resources.'
plans:
- name: Lusha Plans Pricing
  plan_count: 4
  slug: lusha-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 13
  name: Lusha Rate Limits
  slug: lusha-rate-limits
scopes:
- name: Lusha Scopes
  scope_count: 1
  slug: lusha-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 65.1
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 86.8
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/screenshots/lusha-2026-06-20T184813.png
security:
- kind: authentication
  name: Lusha Authentication
  slug: lusha-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Lusha Domain Security
  slug: lusha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lusha Vulnerability Disclosure
  slug: lusha-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lusha Trust Center
  slug: lusha-trust-center
  summary_line: SOC 2 Type II
slug: lusha
tags:
- Sales Intelligence
- B2B
- Enrichment
- Contact Data
- Prospecting
- Intent
- Signals
- Lookalikes
- Webhook
- MCP
website: https://www.lusha.com/
---
