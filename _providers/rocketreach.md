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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-08-11'
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
artifact_total: 24
collections:
- collection_type: open
  name: RocketReach Account API
  slug: open-rocketreach-account-api
- collection_type: open
  name: RocketReach Company Lookup API
  slug: open-rocketreach-company-lookup-api
- collection_type: open
  name: RocketReach Company Search API
  slug: open-rocketreach-company-search-api
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
  url: https://rocketreach.co/api
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
  url: https://rocketreach.co/about
- group: company
  title: ''
  type: Careers
  url: https://rocketreach.co/careers
- group: company
  title: ''
  type: Press
  url: https://rocketreach.co/press
- group: auth
  title: ''
  type: TrustCenter
  url: https://rocketreach.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rocketreach.co/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rocketreach.co/legal/terms-of-use
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
modified: '2026-05-25'
name: RocketReach
nav: Providers
network: true
overview: 'RocketReach publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Company Data API API, and People Data API API. Tagged areas include B2B, Contact Data, Email Lookup, Phone Lookup, and Sales Intelligence.


  RocketReach''s developer surface includes authentication, developer portal, documentation, getting-started guide, FAQ, pricing, signup flow, and 23 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 42.8
  delta: -0.6
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.7
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rocketreach/refs/heads/main/screenshots/rocketreach-2026-06-20T193159.png
security:
- kind: authentication
  name: Rocketreach Authentication
  slug: rocketreach-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rocketreach Domain Security
  slug: rocketreach-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rocketreach Vulnerability Disclosure
  slug: rocketreach-vulnerability-disclosure
  summary_line: security.txt · contact published
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
- Webhooks
website: https://rocketreach.co
---
