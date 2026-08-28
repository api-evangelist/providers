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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rocketreach Agentic Access
  operation_count: 16
  slug: rocketreach-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 3
apis:
- description: Retrieve and manage RocketReach API account details, generate new API keys, and inspect plan, lookup credit balance, export credit balance, and Universal Credits usage. Provides both legacy account en
  name: RocketReach Account API
  slug: rocketreach-account-api
- description: The Company Data API API from RocketReach — 5 operation(s) for company data api.
  name: RocketReach Company Data API API
  slug: rocketreach-company-data-api-api
- description: The People Data API API from RocketReach — 9 operation(s) for people data api.
  name: RocketReach People Data API API
  slug: rocketreach-people-data-api-api
artifact_total: 33
asyncapis:
- description: ''
  name: Rocketreach Webhooks
  slug: rocketreach-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RocketReach Account API
  slug: open-rocketreach-account-api
- collection_type: open
  name: RocketReach Account Company Data API API
  slug: open-rocketreach-company-data-api-api
- collection_type: open
  name: RocketReach Company Lookup API
  slug: open-rocketreach-company-lookup-api
- collection_type: open
  name: RocketReach Company Search API
  slug: open-rocketreach-company-search-api
- collection_type: open
  name: RocketReach Account People Data API API
  slug: open-rocketreach-people-data-api-api
- collection_type: open
  name: RocketReach People Lookup API
  slug: open-rocketreach-people-lookup-api
- collection_type: open
  name: RocketReach People Search API
  slug: open-rocketreach-people-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rocketreach-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rocketreach-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rocketreach-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rocketreach-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://rocketreach.co
- group: company
  title: ''
  type: Website
  url: https://rocketreach.co
- group: start
  title: ''
  type: APIPortal
  url: https://rocketreach.co/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rocketreach.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rocketreach.co/reference/rocketreach-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rocketreach.co/reference/rocketreach-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rocketreach.co/reference/universal-credits-overview
- group: design
  title: ''
  type: Webhooks
  url: https://docs.rocketreach.co/reference/webhooks
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.rocketreach.co/reference/rate-limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.rocketreach.co/reference/responses-and-errors
- group: operate
  title: ''
  type: FAQ
  url: https://docs.rocketreach.co/reference/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://rocketreach.co/pricing
- group: start
  title: ''
  type: Signup
  url: https://rocketreach.co/signup
- group: start
  title: ''
  type: Login
  url: https://rocketreach.co/login
- group: operate
  title: ''
  type: Support
  url: mailto:api@rocketreach.co
- group: company
  title: ''
  type: Blog
  url: https://rocketreach.co/blog
- group: other
  title: ''
  type: Company
  url: https://rocketreach.co/company
- group: company
  title: ''
  type: Careers
  url: https://rocketreach.co/careers
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rocketreach.co
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rocketreach.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rocketreach.co/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rocketreach
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RocketReach
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/rocketreach
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@rocketreach
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rocketreach-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rocketreach-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rocketreach-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rocketreach-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/rocketreach-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rocketreach-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/rocketreach-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rocketreach-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rocketreach-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rocketreach-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rocketreach-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rocketreach-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rocketreach.co
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rocketreach-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rocketreach-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rocketreach-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rocketreach-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rocketreach-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rocketreach-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: security/rocketreach-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rocketreach-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rocketreach
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rocketreach.co/reference/rocketreach-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rocketreach.co/
- group: start
  title: ''
  type: SignUp
  url: https://rocketreach.co/signup
created: '2026-05-25'
description: RocketReach is a Seattle-based B2B contact data and sales intelligence provider that maintains a database of 700M+ professional profiles and 60M+ companies and exposes it through a REST API for email, phone, and social-handle discovery plus company firmographics. The platform is used for sales prospecting, recruiting, marketing enrichment, and CRM hydration, with results returned as structured profile and company objects and optional webhook delivery for asynchronous lookups.
features:
- 700M+ professional profiles and 60M+ companies in the RocketReach database
- REST API for People Lookup, People Search, Company Lookup, Company Search, and Account management
- Single, bulk (up to 100 queries), and combined person+company lookups
- Universal API surface (/api/v2/universal/*) unifying lookup and search across people and companies
- Asynchronous lookup results delivered via webhooks with signed payloads and RR-Request-ID correlation
- Status polling endpoints for in-progress lookups (/person/checkStatus, /universal/person/check_status)
- Cached and fully verified email return modes (return_cached_emails flag; default flips Sept 1, 2026)
- Premium, standard, phone, enrich, and bulk lookup types with credit-aware pricing
- LinkedIn URL, name+employer, profile id, email, and NPI number resolvers
- Tiered rate limits (Essentials, Pro, Ultimate, Custom) plus a 10-req/sec global ceiling with Retry-After headers on 429s
- API key authentication via Api-Key header; keys generated and rotated from Account Settings
- Salesforce, HubSpot, Outreach, SalesLoft, Zapier, and Chrome extension integrations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rocketreach.png
layout: provider
mcp_servers:
- description: RocketReach ships a first-party, hosted Model Context Protocol server that exposes its people and company search and lookup surface as MCP tools. The agent authenticates once via OAuth 2.1 with PKCE a
  name: RocketReach MCP Server
  slug: rocketreach-mcp-server
modified: '2026-08-13'
name: RocketReach
nav: Providers
network: true
overview: 'RocketReach publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Company Data API API, and People Data API API. Tagged areas include B2B, Contact Data, Email Lookup, Phone Lookup, and Sales Intelligence.


  The RocketReach catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RocketReach''s developer surface includes authentication, developer portal, documentation, getting-started guide, FAQ, pricing, signup flow, and 48 more developer resources.'
plans:
- name: Rocketreach Plans Pricing
  plan_count: 4
  slug: rocketreach-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Rocketreach Rate Limits
  slug: rocketreach-rate-limits
scopes:
- name: Rocketreach Scopes
  scope_count: 0
  slug: rocketreach-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.3
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 67.3
    developer_ergonomics: 57.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 40.8
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rocketreach/refs/heads/main/screenshots/rocketreach-2026-06-20T193159.png
security:
- kind: authentication
  name: Rocketreach Authentication
  slug: rocketreach-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Rocketreach Domain Security
  slug: rocketreach-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rocketreach Vulnerability Disclosure
  slug: rocketreach-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rocketreach Trust Center
  slug: rocketreach-trust-center
  summary_line: trust center published
slug: rocketreach
tags:
- B2B
- Contact Data
- Email Lookup
- Phone Lookup
- Sales Intelligence
- Lead Generation
- People Search
- Company Search
- Data Enrichment
- Prospecting
- Recruiting
- Webhook
website: https://rocketreach.co
---
