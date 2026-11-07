---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Leadiq Agentic Access
  operation_count: 15
  slug: leadiq-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 4
apis:
- description: Remote Model Context Protocol server at https://mcp.leadiq.com/mcp exposing LeadIQ's verified B2B contact and company intelligence to AI agents over Streamable HTTP. Seventeen tools — EnrichPeople, En
  name: LeadIQ MCP Server
  slug: leadiq-mcp-server
- baseURL: https://mcp.leadiq.com/mcp
  baseurl_source: declared
  description: The account API from LeadIQ — 1 operation(s) for account.
  name: LeadIQ Account API
  slug: leadiq-account-api
- baseURL: https://mcp.leadiq.com/mcp
  baseurl_source: declared
  description: The lists API from LeadIQ — 5 operation(s) for lists.
  name: LeadIQ Lists API
  slug: leadiq-lists-api
- baseURL: https://mcp.leadiq.com/mcp
  baseurl_source: declared
  description: The prospects API from LeadIQ — 5 operation(s) for prospects.
  name: LeadIQ Prospects API
  slug: leadiq-prospects-api
- baseURL: https://mcp.leadiq.com/mcp
  baseurl_source: declared
  description: Single GraphQL endpoint exposing all LeadIQ queries and mutations.
  name: LeadIQ Graph QL API
  slug: leadiq-graph-ql-api
artifact_total: 23
collections:
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
- group: other
  href: https://artifacts.apis.io/leadiq/capabilities/leadiq-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leadiq-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/leadiq/dataiq-api-specs/issues
- group: agent
  href: https://artifacts.apis.io/leadiq/agentic-access/leadiq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leadiq-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/leadiq/security/leadiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leadiq-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/leadiq/authentication/leadiq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leadiq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/leadiq/scopes/leadiq-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leadiq-scopes.yml
- group: agent
  href: https://artifacts.apis.io/leadiq/mcp/leadiq-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leadiq-mcp.yml
- group: build
  href: https://artifacts.apis.io/leadiq/mcp/leadiq-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/leadiq-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/leadiq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/leadiq/well-known/leadiq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leadiq-well-known.yml
- group: design
  href: https://artifacts.apis.io/leadiq/conventions/leadiq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leadiq-conventions.yml
- group: design
  href: https://artifacts.apis.io/leadiq/errors/leadiq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leadiq-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/leadiq/rate-limits/leadiq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leadiq-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leadiq/plans/leadiq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leadiq-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/leadiq/lifecycle/leadiq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leadiq-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadiq.com
- group: design
  href: https://artifacts.apis.io/leadiq/conformance/leadiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leadiq-conformance.yml
- group: design
  href: https://artifacts.apis.io/leadiq/data-model/leadiq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leadiq-data-model.yml
- group: build
  href: https://artifacts.apis.io/leadiq/packages/leadiq-packages.yml
  title: ''
  type: Packages
  url: packages/leadiq-packages.yml
- group: agent
  href: https://artifacts.apis.io/leadiq/llms/leadiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leadiq-llms.txt
- group: other
  href: https://artifacts.apis.io/leadiq/overlays/leadiq-prospector-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leadiq-prospector-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/leadiq/overlays/leadiq-graphql-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leadiq-graphql-api-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/leadiq/graphql/leadiq.graphql
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
finops:
- has_sources: true
  method: derived
  name: Leadiq Finops
  primary_unit: 1 user/50 credits
  service_category: ''
  slug: leadiq-finops
  template: false
graphqls:
- description: Public GraphQL Data API exposing LeadIQ's verified B2B contact and company intelligence. Supports people search by name + company / domain / LinkedIn URL / email, company search by name or domain, gro
  name: LeadIQ GraphQL API
  slug: leadiq-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadiq.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.leadiq.com over streamable HTTP requiring OAuth; 17 tools listed.
  name: LeadIQ MCP Connector
  slug: leadiq-mcp-connector
modified: '2026-08-13'
name: LeadIQ
nav: Providers
network: true
overview: 'LeadIQ publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Lists API, Prospects API, and 2 more. Tagged areas include Sales Intelligence, B2B Data, Contact Data, Lead Generation, and Prospecting.


  The LeadIQ catalog on APIs.io includes 1 Spectral governance ruleset.


  LeadIQ''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 45 more developer resources.'
plans:
- name: Leadiq Plans Pricing
  plan_count: 3
  slug: leadiq-plans-pricing
- name: Leadiq Price Estimates
  plan_count: 0
  slug: leadiq-price-estimates
random_paper: 0
rate_limits:
- limit_count: 2
  name: Leadiq Rate Limits
  slug: leadiq-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: LeadIQ API Rules
  rule_count: 62
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 5
  slug: leadiq-rules
scopes:
- name: Leadiq Scopes
  scope_count: 2
  slug: leadiq-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 58.9
    discoverability: 73.3
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 20.0
      derived: 0
      marker_coverage: 50.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/leadiq/leadiq-2026-06-20T184350.png
security:
- kind: authentication
  name: Leadiq Authentication
  slug: leadiq-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Leadiq Domain Security
  slug: leadiq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: leadiq-build-icp-prospect-list
  slug: leadiq-build-icp-prospect-list
- name: leadiq-enrich-known-contacts
  slug: leadiq-enrich-known-contacts
- name: leadiq-mcp-agent-operations
  slug: leadiq-mcp-agent-operations
- name: leadiq-save-and-export-prospects
  slug: leadiq-save-and-export-prospects
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
- MCP
- Revenue Operations
- Go-To-Market
- Data Enrichment
website: https://leadiq.com
---
