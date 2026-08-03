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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bazaarvoice Agentic Access
  operation_count: 15
  slug: bazaarvoice-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 6
apis:
- description: The Answers API from Bazaarvoice — 1 operation(s) for answers.
  name: Bazaarvoice Answers API
  slug: bazaarvoice-answers-api
- description: The Clients API from Bazaarvoice — 1 operation(s) for clients.
  name: Bazaarvoice Clients API
  slug: bazaarvoice-clients-api
- description: The Contributor API from Bazaarvoice — 3 operation(s) for contributor.
  name: Bazaarvoice Contributor API
  slug: bazaarvoice-contributor-api
- description: The Lookahead API from Bazaarvoice — 1 operation(s) for lookahead.
  name: Bazaarvoice Lookahead API
  slug: bazaarvoice-lookahead-api
- description: The Questions API from Bazaarvoice — 4 operation(s) for questions.
  name: Bazaarvoice Questions API
  slug: bazaarvoice-questions-api
- description: Search for reviews
  name: Bazaarvoice Reviews API
  slug: bazaarvoice-reviews-api
artifact_total: 11
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bazaarvoice.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bazaarvoice.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bazaarvoice.com/conversations-api/reference/v5.4
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bazaarvoice.com/v1.0-ConversationsAPI/docs/home
- group: operate
  title: ''
  type: Support
  url: https://developer.bazaarvoice.com/conversations-api/getting-help
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.bazaarvoice.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bazaarvoice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bazaarvoice.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bazaarvoice.com/legal/terms-of-use/api/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bazaarvoice.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bazaarvoice.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.bazaarvoice.com/v1.0-ConversationsAPI/docs/upgrade-guide
- group: auth
  title: ''
  type: Authentication
  url: authentication/bazaarvoice-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/bazaarvoice-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bazaarvoice-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bazaarvoice-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bazaarvoice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bazaarvoice-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bazaarvoice-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bazaarvoice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bazaarvoice-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bazaarvoice-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bazaarvoice-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bazaarvoice-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bazaarvoice-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bazaarvoice-content-search-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bazaarvoice-llms.txt
created: '2026-07-17'
description: Bazaarvoice operates a retail and brand user-generated-content network that collects, moderates, and syndicates ratings, reviews, questions and answers, and product-sampling content across thousands of brand and retailer sites. Its developer platform exposes a family of APIs - the flagship Conversations API for retrieving and submitting UGC, the V2.0 Content Search API for searching reviews/questions/answers/contributors and product catalog lookahead, plus the Transactions, Response, Social Commerce, and Authentic Discovery APIs, and structured-data (JSON-LD/Microdata) endpoints for SEO. APIs authenticate with a Bazaarvoice Portal-managed passkey (Bv-Passkey header) or, for the Transactions and Response APIs, 2-legged OAuth2 client credentials. Official iOS, Android, SEO, Magento, and Salesforce Commerce SDKs are published on GitHub.
image: https://github.com/bazaarvoice.png
layout: provider
mcp_servers:
- description: ''
  name: bazaarvoice-mcp.yml
  slug: bazaarvoice-mcpyml
modified: '2026-07-18'
name: Bazaarvoice
nav: Providers
network: true
overview: 'Bazaarvoice publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Answers API, Clients API, Contributor API, and 3 more. Tagged areas include Company, Reviews, Ratings, User Generated Content, and Retail.


  Bazaarvoice''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 21 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bazaarvoice Rate Limits
  slug: bazaarvoice-rate-limits
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 58.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bazaarvoice/refs/heads/main/screenshots/bazaarvoice-2026-07-25T202455.png
security:
- kind: authentication
  name: Bazaarvoice Authentication
  slug: bazaarvoice-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Bazaarvoice Domain Security
  slug: bazaarvoice-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bazaarvoice
tags:
- Company
- Reviews
- Ratings
- User Generated Content
- Retail
- eCommerce
- Product Reviews
- Syndication
- Social Commerce
- SEO
website: https://developers.bazaarvoice.com/
---
