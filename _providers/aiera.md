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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-09-17'
api_count: 5
apis:
- description: Aiera's hosted remote Model Context Protocol server, exposing the financial research corpus to LLMs and agentic workflows as roughly three dozen specialized tools across equities and financials, index
  name: Aiera MCP Server
  slug: aiera-mcp-server
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Calendar API from Aiera — 3 operation(s) for calendar.
  name: Aiera Calendar API
  slug: aiera-calendar-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Event calendar, coverage, and estimates
  name: Aiera Calendar v2 API
  slug: aiera-calendar-v2-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: iCal calendar subscriptions
  name: Aiera Calendars v1 API
  slug: aiera-calendars-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: AieraChat
  name: Aiera Chat v1 API
  slug: aiera-chat-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Company information and lookup
  name: Aiera Companies v1 API
  slug: aiera-companies-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Company-published documents
  name: Aiera Company Docs v1 API
  slug: aiera-company-docs-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Content API from Aiera — 2 operation(s) for content.
  name: Aiera Content API
  slug: aiera-content-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Corporate Activity API from Aiera — 4 operation(s) for corporate activity.
  name: Aiera Corporate Activity API
  slug: aiera-corporate-activity-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Dashboards API from Aiera — 1 operation(s) for dashboards.
  name: Aiera Dashboards API
  slug: aiera-dashboards-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Equities V2 API from Aiera — 7 operation(s) for equities v2.
  name: Aiera Equities V2 API
  slug: aiera-equities-v2-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Events API from Aiera — 3 operation(s) for events.
  name: Aiera Events API
  slug: aiera-events-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Event data and transcripts
  name: Aiera Events v2 API
  slug: aiera-events-v2-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Third-party expert insights content
  name: Aiera Expert Access v1 API
  slug: aiera-expert-access-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: SEC regulatory filings
  name: Aiera Filings v1 API
  slug: aiera-filings-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: People and speaker lookup
  name: Aiera People v1 API
  slug: aiera-people-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Summaries API from Aiera — 3 operation(s) for summaries.
  name: Aiera Summaries API
  slug: aiera-summaries-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Topics API from Aiera — 6 operation(s) for topics.
  name: Aiera Topics API
  slug: aiera-topics-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: The Transcrippets API from Aiera — 1 operation(s) for transcrippets.
  name: Aiera Transcrippets API
  slug: aiera-transcrippets-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Shareable transcript snippets
  name: Aiera Transcrippets v1 API
  slug: aiera-transcrippets-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Organization user management
  name: Aiera User Admin v1 API
  slug: aiera-user-admin-v1-api
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: User entitlements and permissions
  name: Aiera Users v1 API
  slug: aiera-users-v1-api
artifact_total: 29
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/overlays/aiera-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aiera-rest-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://aiera.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rest.aiera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rest.aiera.com/
- group: docs
  title: ''
  type: APIReference
  url: https://rest.aiera.com/docs/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://rest.aiera.com/#quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.aiera.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://aiera.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiera-inc
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.aiera.com/auth
- group: start
  title: ''
  type: Login
  url: https://dashboard.aiera.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiera.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiera.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aiera.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/mcp/aiera-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiera-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/llms/aiera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiera-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/well-known/aiera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiera-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/authentication/aiera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiera-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/scopes/aiera-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aiera-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/conventions/aiera-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiera-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/lifecycle/aiera-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aiera-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/conformance/aiera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiera-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/security/aiera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiera-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/packages/aiera-packages.yml
  title: ''
  type: Packages
  url: packages/aiera-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/packages/aiera-packages.yml
  title: ''
  type: SDKs
  url: packages/aiera-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/components/aiera-components.yml
  title: ''
  type: Components
  url: components/aiera-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/rate-limits/aiera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiera-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/plans/aiera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiera-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/errors/aiera-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiera-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/data-model/aiera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiera-data-model.yml
created: '2026-09-14'
description: Aiera is a New York-based financial research technology company that provides real-time and historical intelligence on public-company events. Its platform covers earnings calls, investor days, conferences and shareholder meetings with live AI transcription plus human-edited transcripts, and layers on AI-generated summaries, topic and tonal-sentiment analysis, SEC filings, company-published documents, broker research, expert-insight content (including Third Bridge) and financial news. Aiera exposes that corpus to buy-side and sell-side institutions through an entitlement-aware REST API, a hosted remote MCP server for LLM and agentic workflows, embeddable web components (AieraChat, Aieracast, EventList), and an open-source Python MCP package.
image: https://aiera.com/wp-content/uploads/2025/09/aiera-default-feature.jpg
layout: provider
mcp_servers:
- description: Aiera ships a hosted remote MCP server exposing its financial research corpus — earnings calls and transcripts, calendars, equities and financials, SEC filings, company-published documents, Third Brid
  name: Aiera MCP Server
  slug: aiera-mcp-server
- description: ''
  name: Aiera MCP Server
  slug: aiera-mcp-server-2
modified: '2026-09-14'
name: Aiera
nav: Providers
network: true
overview: 'Aiera publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Calendar v2 API, Calendars v1 API, and 18 more. Tagged areas include Financial Research, Earnings Calls, Transcripts, SEC Filings, and Market Data.


  Aiera''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Aiera Plans Pricing
  plan_count: 0
  slug: aiera-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Aiera Rate Limits
  slug: aiera-rate-limits
scopes:
- name: Aiera Scopes
  scope_count: 0
  slug: aiera-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 56.8
    developer_ergonomics: 66.1
    discoverability: 81.5
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aiera Authentication
  slug: aiera-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Aiera Domain Security
  slug: aiera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiera
tags:
- Financial Research
- Earnings Calls
- Transcripts
- SEC Filings
- Market Data
- Financial Data
- Broker Research
- Expert Networks
- Speech-to-Text
- Financial-Services
- MCP
- agent-native
website: https://aiera.com/
---
