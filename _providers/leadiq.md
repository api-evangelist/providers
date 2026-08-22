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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Leadiq Agentic Access
  operation_count: 15
  slug: leadiq-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 3
apis:
- description: Remote Model Context Protocol server at https://mcp.leadiq.com/mcp exposing LeadIQ's verified B2B contact and company intelligence to AI agents over Streamable HTTP. Seventeen tools — EnrichPeople, En
  name: LeadIQ MCP Server
  slug: leadiq-mcp-server
- description: Single GraphQL endpoint exposing all LeadIQ queries and mutations.
  name: LeadIQ GraphQL API
  slug: leadiq-graphql-api
- description: 'REST API for LeadIQ''s saved prospecting workspace — create and read prospect lists, create prospects singly or in batches of up to 100, search saved prospects, verify email deliverability, and export '
  name: LeadIQ Prospector REST API
  slug: leadiq-prospector-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LeadIQ Data API
  slug: open-leadiq-data-api
- collection_type: open
  name: LeadIQ Data GraphQL API
  slug: open-leadiq-graphql-api
- collection_type: open
  name: Prospector API
  slug: open-leadiq-prospector-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/leadiq/dataiq-api-specs/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leadiq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadiq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadiq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leadiq-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leadiq-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/leadiq-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leadiq-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leadiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leadiq-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leadiq-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leadiq-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leadiq-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadiq.com
- group: design
  title: ''
  type: Conformance
  url: conformance/leadiq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leadiq-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/leadiq-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leadiq-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/leadiq-prospector-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leadiq-graphql-api-overlay.yaml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/leadiq.graphql
- group: company
  title: ''
  type: Website
  url: https://leadiq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.leadiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://leadiqhelp.zendesk.com/hc/en-us/sections/29405194605723-API
- group: docs
  title: ''
  type: APIReference
  url: https://developer.leadiq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://leadiqhelp.zendesk.com/hc/en-us/articles/29375289152795-LeadIQ-Public-API-Guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadiq
- group: commercial
  title: ''
  type: Pricing
  url: https://leadiq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://leadiq.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://account.leadiq.com/login
- group: company
  title: ''
  type: Blog
  url: https://leadiq.com/blog
- group: other
  title: ''
  type: Podcast
  url: https://leadiq.com/podcast
- group: other
  title: ''
  type: CaseStudies
  url: https://leadiq.com/case-studies
- group: operate
  title: ''
  type: Support
  url: https://leadiqhelp.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Status
  url: https://status.leadiq.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leadiq.com/legal/privacy-policy
- group: commercial
  title: ''
  type: PrivacyCenter
  url: https://leadiq.com/privacy-center
- group: other
  title: ''
  type: CookiePolicy
  url: https://leadiq.com/legal/cookie-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leadiq.com/legal/terms-of-use
- group: company
  title: ''
  type: Careers
  url: https://leadiq.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://leadiq.com/contact
- group: other
  title: ''
  type: Product
  url: https://leadiq.com/leadiq-mcp
- group: other
  title: ''
  type: Repository
  url: https://github.com/leadiq
- group: other
  title: ''
  type: APIRepository
  url: https://github.com/leadiq/dataiq-api-specs
- group: build
  title: ''
  type: APISamples
  url: https://github.com/leadiq/api-samples
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leadiq
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/leadiq
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@LeadIQ
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/leadiq
- group: other
  title: ''
  type: G2
  url: https://www.g2.com/products/leadiq/reviews
created: '2026-05-25'
description: 'LeadIQ is a B2B sales intelligence and contact data platform headquartered in Santa Clara, California (with engineering in Singapore and Brisbane) that helps outbound sales teams identify, capture, enrich, and engage prospects across Salesforce, HubSpot, Outreach, Salesloft, Gong, and other revenue tools. The product portfolio includes Prospector (Chrome extension for contact capture with verified work emails and direct-dial mobile phones), Scribe (AI message writer), Refresh / CRM Enrichment (continuous contact and account hygiene for Salesforce and HubSpot), Champion Tracking (job-change alerts on existing contacts), AI Account Prospecting (ICP-fit account and persona discovery), and Lando — an agentic AI assistant that fuses first-party CRM data with LeadIQ''s third-party intelligence behind a conversational interface. LeadIQ exposes a public GraphQL Data API at https://api.leadiq.com/graphql for programmatic people search, company search, advanced grouped search, prospect-list
  management, usage reporting, and data-feedback submission, authenticated via HTTP Basic auth with an API key issued in the LeadIQ dashboard. The same API surface is also reachable through a Model Context Protocol (MCP) server so AI agents (including Claude) can query verified contact and account data conversationally. LeadIQ actually runs three programmable surfaces over one data core: the GraphQL Data API, a REST Prospector API at https://prospector.leadiq.com described by an OpenAPI 3.1.0 document LeadIQ serves publicly (14 operations for lists, prospects, email verification, Salesforce export and caller identity), and a remote MCP connector at https://mcp.leadiq.com/mcp with seventeen tools behind OAuth 2.0 and dynamic client registration. The published rate limit is 60 requests/minute (Standard), with credit-based metering in Universal Credits where a verified work email costs 1 UC, a direct phone 10 UC, company firmographics 3 UC and a profile 0.1 UC. All plans get 50 one-off test
  calls; sustained API access is sales-gated.'
graphqls:
- description: Public GraphQL Data API exposing LeadIQ's verified B2B contact and company intelligence. Supports people search by name + company / domain / LinkedIn URL / email, company search by name or domain, gro
  name: LeadIQ GraphQL API
  slug: leadiq-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadiq.png
layout: provider
mcp_servers:
- description: ''
  name: leadiq-mcp.yml
  slug: leadiq-mcpyml
modified: '2026-08-13'
name: LeadIQ
nav: Providers
network: true
overview: 'LeadIQ publishes 2 APIs on the [APIs.io](https://apis.io/) network: GraphQL API and Prospector REST API. Tagged areas include Sales Intelligence, B2B Data, Contact Data, Lead Generation, and Prospecting.


  LeadIQ''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 44 more developer resources.'
plans:
- name: Leadiq Plans Pricing
  plan_count: 3
  slug: leadiq-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Leadiq Rate Limits
  slug: leadiq-rate-limits
scopes:
- name: Leadiq Scopes
  scope_count: 2
  slug: leadiq-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: strong
  composite: 58.2
  delta: -3.1
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 59.0
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leadiq/refs/heads/main/screenshots/leadiq-2026-06-20T184350.png
security:
- kind: authentication
  name: Leadiq Authentication
  slug: leadiq-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Leadiq Domain Security
  slug: leadiq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: leadiq
tags:
- Sales Intelligence
- B2B Data
- Contact Data
- Lead Generation
- Prospecting
- CRM Enrichment
- Sales Engagement
- GraphQL
- Model Context Protocol
- Revenue Operations
- Go To Market
website: https://leadiq.com
---
