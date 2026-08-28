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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Bazaarvoice Agentic Access
  operation_count: 79
  slug: bazaarvoice-agentic-access
  summary_line: 79 operations · 30 acting
api_count: 17
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
- description: The Conversations Display API returns published user-generated content for a product or catalog - reviews, review comments, questions, answers, author profiles, products, categories and aggregate stat
  name: Bazaarvoice Conversations Display API
  slug: bazaarvoice-conversations-display-api
- description: 'The Conversations Submission API accepts shopper-generated content: reviews, review comments, questions, answers and feedback, plus photo and video upload, author authentication and progressive submis'
  name: Bazaarvoice Conversations Submission API
  slug: bazaarvoice-conversations-submission-api
- description: 'The Response API lets a brand publish, edit and remove its official response to a review, and read the review and author behind a response. It authenticates with an HTTP bearer token obtained through '
  name: Bazaarvoice Response API
  slug: bazaarvoice-response-api
- description: A separately published single-operation contract that takes a list of review identifiers and returns how many brand responses each review already has - the bulk triage counterpart to the Response API.
  name: Bazaarvoice Response Count API
  slug: bazaarvoice-response-count-api
- description: The Notifications Subscriptions API manages shopper email subscription state for Bazaarvoice notification emails - paging the opt-in and opt-out lists per email type and subscribing or unsubscribing a
  name: Bazaarvoice Notifications Subscriptions API
  slug: bazaarvoice-notifications-subscriptions-api
- description: The Transactions API ingests purchase transaction records - single or bulk - so Bazaarvoice can schedule post-interaction review-request notifications, and invalidates a transaction when an order is c
  name: Bazaarvoice Transactions API
  slug: bazaarvoice-transactions-api
- description: 'The Product Sentiment API returns NLP-derived consumer insight from review text: summarised product features with best/worst weighting, the shopper quotes behind each feature, all detected features fo'
  name: Bazaarvoice Product Sentiment API
  slug: bazaarvoice-product-sentiment-api
- description: The Social Commerce Display API serves visual user-generated content - gallery media, top images, recommendations, Instagram and Facebook sourcing, media upload and reporting, and Schema.org structure
  name: Bazaarvoice Social Commerce Display (Media) API
  slug: bazaarvoice-social-commerce-media-api
- description: 'The Authentic Discovery API is Bazaarvoice''s generative-engine-optimization surface: a server-side call that returns a product''s ratings, reviews, review summaries and Q&A as Schema.org JSON-LD or Mic'
  name: Bazaarvoice Authentic Discovery API
  slug: bazaarvoice-authentic-discovery-api
- description: 'Displayable Content Export is a bulk HTTPS data interface: a client requests a manifest file list, follows redirects to the manifest and then to the data files, and downloads the full set of displayab'
  name: Bazaarvoice Displayable Content Export
  slug: bazaarvoice-displayable-content-export
- description: 'Product Sentiment Export is the bulk counterpart to the Product Sentiment API: the same manifest-then-download HTTPS flow used by Displayable Content Export, delivering sentiment insight data as files'
  name: Bazaarvoice Product Sentiment Export
  slug: bazaarvoice-product-sentiment-export
artifact_total: 45
collections:
- collection_type: postman
  name: Bazaarvoice Notifications Subscriptions API
  slug: postman-bazaarvoice-notifications-subscriptions-api
- collection_type: postman
  name: Bazaarvoice Privacy API
  slug: postman-bazaarvoice-privacy-api
- collection_type: postman
  name: Bazaarvoice Response API
  slug: postman-bazaarvoice-response-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bazaarvoice Content Search Answers API
  slug: open-bazaarvoice-answers-api
- collection_type: open
  name: SEO
  slug: open-bazaarvoice-authentic-discovery
- collection_type: open
  name: Bazaarvoice Content Search Answers Clients API
  slug: open-bazaarvoice-clients-api
- collection_type: open
  name: Bazaarvoice Content Search Answers Contributor API
  slug: open-bazaarvoice-contributor-api
- collection_type: open
  name: Conversations Display API
  slug: open-bazaarvoice-conversations-display
- collection_type: open
  name: Conversation Submission API
  slug: open-bazaarvoice-conversations-submission
- collection_type: open
  name: Step 1
  slug: open-bazaarvoice-displayable-content-export
- collection_type: open
  name: Bazaarvoice Content Search Answers Lookahead API
  slug: open-bazaarvoice-lookahead-api
- collection_type: open
  name: Notifications Subscriptions API
  slug: open-bazaarvoice-notifications-subscriptions
- collection_type: open
  name: Step 1
  slug: open-bazaarvoice-product-sentiment-export
- collection_type: open
  name: Product Sentiment API
  slug: open-bazaarvoice-product-sentiment
- collection_type: open
  name: Bazaarvoice Content Search Answers Questions API
  slug: open-bazaarvoice-questions-api
- collection_type: open
  name: Count Client Response
  slug: open-bazaarvoice-response-count
- collection_type: open
  name: Response API
  slug: open-bazaarvoice-response
- collection_type: open
  name: Media API
  slug: open-bazaarvoice-social-commerce-media
- collection_type: open
  name: Transactions API
  slug: open-bazaarvoice-transactions
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
- group: auth
  title: ''
  type: Security
  url: https://www.bazaarvoice.com/legal/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bazaarvoice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bazaarvoice-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bazaarvoice.com/company/trust/security/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bazaarvoice-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bazaarvoice-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bazaarvoice-plans-pricing.yml
- group: build
  title: ''
  type: Postman
  url: postman/_index.yml
- group: start
  title: ''
  type: Login
  url: https://portal.bazaarvoice.com
- group: operate
  title: ''
  type: Support
  url: https://support.bazaarvoice.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/_index.yml
created: '2026-07-17'
description: 'Bazaarvoice operates a retail and brand user-generated-content network that collects, moderates, syndicates and now makes machine-discoverable the ratings, reviews, questions and answers, and visual content published across thousands of brand and retailer sites. Its developer portal publishes twelve product sections and eleven distinct OpenAPI documents: the Conversations Display and Conversations Submission APIs for retrieving and posting UGC, the V2.0 Content Search API, the Response API for brand replies, the Transactions API for scheduling review requests, the Product Sentiment API for NLP-derived feature insight, the Notifications Subscriptions and Privacy APIs, the Social Commerce Display API for visual UGC, bulk Displayable Content and Product Sentiment exports, and the Authentic Discovery API, which returns Schema.org JSON-LD so AI crawlers that do not run JavaScript can read a product''s reviews. Authentication varies by product - a Portal-managed passkey (Bv-Passkey
  header or Passkey query parameter), HTTP bearer tokens from 2-legged or 3-legged OAuth2, or an X-Curalate-Api-Key header on the acquired Curalate social-commerce platform. Bazaarvoice serves a real llms.txt on every documentation section, publishes first-party Postman collections and iOS, Android, SEO, Magento and Salesforce Commerce SDKs on GitHub, and is ISO/IEC 27001 certified with a HackerOne vulnerability disclosure policy.'
image: https://github.com/bazaarvoice.png
layout: provider
mcp_servers:
- description: ''
  name: Bazaarvoice MCP Server
  slug: bazaarvoice-mcp-server
modified: '2026-08-13'
name: Bazaarvoice
nav: Providers
network: true
overview: 'Bazaarvoice publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Answers API, Clients API, Contributor API, and 14 more. Tagged areas include Company, Reviews, Ratings, User Generated Content, and Retail.


  Bazaarvoice''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 32 more developer resources.'
plans:
- name: Bazaarvoice Plans Pricing
  plan_count: 9
  slug: bazaarvoice-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Bazaarvoice Rate Limits
  slug: bazaarvoice-rate-limits
score:
  band: strong
  composite: 62.4
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 54.9
    developer_ergonomics: 67.3
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 48.7
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bazaarvoice/refs/heads/main/screenshots/bazaarvoice-2026-07-25T202455.png
security:
- kind: authentication
  name: Bazaarvoice Authentication
  slug: bazaarvoice-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Bazaarvoice Domain Security
  slug: bazaarvoice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bazaarvoice Vulnerability Disclosure
  slug: bazaarvoice-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Bazaarvoice Trust Center
  slug: bazaarvoice-trust-center
  summary_line: ISO/IEC 27001:2013, CSA CAIQ, GDPR, CCPA
slug: bazaarvoice
tags:
- Company
- Reviews
- Ratings
- User Generated Content
- Retail
- E-Commerce
- Product Reviews
- Syndication
- Social Commerce
- SEO
website: https://developers.bazaarvoice.com/
---
