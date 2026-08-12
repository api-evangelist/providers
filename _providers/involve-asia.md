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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Involve Asia Agentic Access
  operation_count: 9
  slug: involve-asia-agentic-access
  summary_line: 9 operations · 9 acting
api_count: 6
apis:
- description: The Auth API from Involve Asia — 1 operation(s) for auth.
  name: Involve Asia Auth API
  slug: involve-asia-auth-api
- description: The Campaigns API from Involve Asia — 1 operation(s) for campaigns.
  name: Involve Asia Campaigns API
  slug: involve-asia-campaigns-api
- description: The Conversions API from Involve Asia — 3 operation(s) for conversions.
  name: Involve Asia Conversions API
  slug: involve-asia-conversions-api
- description: The Deeplink API from Involve Asia — 1 operation(s) for deeplink.
  name: Involve Asia Deeplink API
  slug: involve-asia-deeplink-api
- description: The Offers API from Involve Asia — 2 operation(s) for offers.
  name: Involve Asia Offers API
  slug: involve-asia-offers-api
- description: The Shopee API from Involve Asia — 1 operation(s) for shopee.
  name: Involve Asia Shopee API
  slug: involve-asia-shopee-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, resolve an offer, and mint a trackable affiliate deeplink.
  name: Involve Asia Generate Deeplink
  slug: involve-asia-generate-deeplink-workflow
- description: Authenticate and pull attributed conversions for a date range.
  name: Involve Asia Sync Conversions
  slug: involve-asia-sync-conversions-workflow
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://involve.asia
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.involve.asia/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://involve.asia/partners/api-overview/
- group: docs
  title: ''
  type: APIReference
  url: https://api.involve.asia/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.involve.asia/docs/#quickstart
- group: operate
  title: ''
  type: Support
  url: https://helpcentre.involve.asia/
- group: company
  title: ''
  type: Blog
  url: https://involve.asia/publisher-blog/
- group: start
  title: ''
  type: SignUp
  url: https://involve.asia/publisher/
- group: start
  title: ''
  type: Login
  url: https://app.involve.asia/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://involve.asia/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.involve.asia/publisher/privacypolicy
- group: build
  title: ''
  type: Postman
  url: https://api.involve.asia/docs/collection.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/involve-asia-publisher-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/involve-asia-publisher-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/involve-asia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/involve-asia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/involve-asia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/involve-asia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/involve-asia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/involve-asia-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/involve-asia-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/involve-asia-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/involve-asia-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/involve-asia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/involve-asia-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/involve-asia-generate-deeplink-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/involve-asia-sync-conversions-workflow.yml
created: '2026-07-17'
description: 'Involve Asia (Involve Asia Technologies Sdn. Bhd.) is a leading affiliate and partnership-marketing network across Southeast Asia and Taiwan, connecting advertisers with publishers and creators to grow revenue through performance marketing. Its public Publisher API lets publishers programmatically pull conversion (commission) data, browse offers and campaigns, generate trackable affiliate deeplinks, and access Shopee Commission Xtra boosted-payout brands — without logging into the dashboard. The API is REST over HTTPS with bearer-JWT auth (2-hour token TTL), form-urlencoded requests, page-number pagination, a 60 requests/minute throttle, and a 1,000-link rolling 30-day deeplink cap. Involve Asia publishes first-party machine-readable artifacts: an OpenAPI 3.1 spec, a Claude Skill, an llms.txt, and a Postman collection.'
image: https://api.involve.asia/docs/assets/f4c704c9-e5f3-4fea-8ccd-89209c3f2451.svg
layout: provider
mcp_servers:
- description: ''
  name: involve-asia-mcp.yml
  slug: involve-asia-mcpyml
modified: '2026-07-19'
name: Involve Asia
nav: Providers
network: true
overview: 'Involve Asia publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Campaigns API, Conversions API, and 3 more. Tagged areas include Affiliate Marketing, Performance Marketing, Partnership Marketing, Publishers, and Creators.


  Involve Asia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 46.4
  delta: -1.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 59.7
    developer_ergonomics: 65.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/involve-asia/refs/heads/main/screenshots/involve-asia-2026-07-25T222801.png
security:
- kind: authentication
  name: Involve Asia Authentication
  slug: involve-asia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Involve Asia Domain Security
  slug: involve-asia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: involve-asia
tags:
- Affiliate Marketing
- Performance Marketing
- Partnership Marketing
- Publishers
- Creators
- Conversions
- Deeplinks
- Commissions
- Ecommerce
- Southeast Asia
- Shopee
- Company
website: https://involve.asia
---
