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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Leadiq Agentic Access
  operation_count: 1
  slug: leadiq-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Model Context Protocol server that exposes LeadIQ's verified B2B contact and company intelligence to AI agents (Claude Desktop, Claude Code, Cursor, and any MCP-compatible client). Provides conversati
  name: LeadIQ MCP Server
  slug: leadiq-mcp-server
- description: Single GraphQL endpoint exposing all LeadIQ queries and mutations.
  name: LeadIQ GraphQL API
  slug: leadiq-graphql-api
artifact_total: 7
collections:
- collection_type: open
  name: LeadIQ Data API
  slug: open-leadiq-data-api
common:
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
- group: commercial
  title: ''
  type: Pricing
  url: https://leadiq.com/pricing
- group: start
  title: ''
  type: Signup
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
- group: auth
  title: ''
  type: Security
  url: https://leadiq.com/security
- group: commercial
  title: ''
  type: Privacy
  url: https://leadiq.com/privacy
- group: commercial
  title: ''
  type: Terms
  url: https://leadiq.com/terms
- group: company
  title: ''
  type: Careers
  url: https://leadiq.com/careers
- group: company
  title: ''
  type: About
  url: https://leadiq.com/about
- group: operate
  title: ''
  type: Contact
  url: https://leadiq.com/contact
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
description: LeadIQ is a B2B sales intelligence and contact data platform headquartered in Santa Clara, California (with engineering in Singapore and Brisbane) that helps outbound sales teams identify, capture, enrich, and engage prospects across Salesforce, HubSpot, Outreach, Salesloft, Gong, and other revenue tools. The product portfolio includes Prospector (Chrome extension for contact capture with verified work emails and direct-dial mobile phones), Scribe (AI message writer), Refresh / CRM Enrichment (continuous contact and account hygiene for Salesforce and HubSpot), Champion Tracking (job-change alerts on existing contacts), AI Account Prospecting (ICP-fit account and persona discovery), and Lando — an agentic AI assistant that fuses first-party CRM data with LeadIQ's third-party intelligence behind a conversational interface. LeadIQ exposes a public GraphQL Data API at https://api.leadiq.com/graphql for programmatic people search, company search, advanced grouped search, prospect-list
  management, usage reporting, and data-feedback submission, authenticated via HTTP Basic auth with an API key issued in the LeadIQ dashboard. The same API surface is also reachable through a Model Context Protocol (MCP) server so AI agents (including Claude) can query verified contact and account data conversationally. Rate limits default to 10 requests/minute on Free and 60 requests/minute on paid plans, with credit-based metering where an email costs 1 credit, a phone 10 credits, and account enrichment 3 credits.
graphqls:
- description: Public GraphQL Data API exposing LeadIQ's verified B2B contact and company intelligence. Supports people search by name + company / domain / LinkedIn URL / email, company search by name or domain, gro
  name: LeadIQ GraphQL API
  slug: leadiq-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadiq.png
layout: provider
modified: '2026-05-25'
name: LeadIQ
nav: Providers
network: true
overview: 'LeadIQ publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Sales Intelligence, B2B Data, Contact Data, Lead Generation, and Prospecting.


  LeadIQ''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, status page, and 21 more developer resources.'
random_paper: 59
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.7
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leadiq/refs/heads/main/screenshots/leadiq-2026-06-20T184350.png
security:
- kind: authentication
  name: Leadiq Authentication
  slug: leadiq-authentication
  summary_line: http · 1 scheme
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
