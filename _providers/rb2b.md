---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Credit-metered Identification endpoints that convert anonymous web signals (IP addresses and user agents) into business identifiers, including IP → HEM (hashed email), IP → MAID (mobile ad ID), and IP
  name: RB2B Identification API
  slug: rb2b-identification-api
- description: Credit-metered Enrichment endpoints that take a known identifier (hashed email, LinkedIn URL, plaintext email, MAID, or company domain) and return additional B2B attributes — LinkedIn URL, full busine
  name: RB2B Enrichment API
  slug: rb2b-enrichment-api
- description: The RB2B JavaScript pixel installed in a site header (or via Google Tag Manager / Segment / RudderStack / Shopify / Webflow / WordPress / HubSpot CMS / Wix) is the primary data ingestion surface for R
  name: RB2B Pixel and Destination Webhooks
  slug: rb2b-pixel-webhooks
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/rb2b-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rb2b-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rb2b.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rb2b.com/pricing
- group: company
  title: ''
  type: Partner
  url: https://www.rb2b.com/partner
- group: operate
  title: ''
  type: Support
  url: https://support.rb2b.com/en/
- group: other
  title: ''
  type: APIs
  url: https://www.rb2b.com/apis
- group: start
  title: ''
  type: APIPortal
  url: https://ui.api.rb2b.com/login
- group: docs
  title: ''
  type: APIDocumentation
  url: https://postman.api.rb2b.com/
- group: company
  title: ''
  type: APIPartnerProgram
  url: https://support.rb2b.com/en/articles/12579420-rb2b-s-api-partner-program
- group: build
  title: ''
  type: APICollections
  url: https://support.rb2b.com/en/collections/16023167-api-partner-program
- group: operate
  title: ''
  type: Contact
  url: mailto:support@rb2b.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RetentionAdam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rb2b
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/retentiondotcom/
created: '2026-05-25'
description: RB2B is a US-focused B2B website visitor identification platform that resolves anonymous web traffic into person-level leads — names, LinkedIn profiles, hashed and plaintext business emails, mobile ad IDs, and full business profiles — and pushes them to sales, marketing, and ad-tech systems. The product is delivered as a JavaScript pixel plus a knowledge- base and pipeline of 50+ destination integrations (Slack, Microsoft Teams, Salesforce, HubSpot, Clay, Zapier, Apollo, Customer.io, Demandbase, and others), with global company-level identification and US-only person- level resolution. RB2B operates a separate API Partner Program at api.rb2b.com that exposes credit-metered Identification endpoints (IP → HEM, IP → MAID, IP → Company Domain) and Enrichment endpoints (HEM → LinkedIn, HEM → Business Profile, HEM → MAID, LinkedIn → Email, LinkedIn → Phone, Email → LinkedIn, Email → MAID) for SaaS developers, GTM engineers, retailers, and ad-tech platforms that want to embed identity
  resolution into their own apps and identity graphs. The platform is SOC 2 Type II certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rb2b.png
layout: provider
modified: '2026-05-25'
name: RB2B
nav: Providers
network: true
overview: 'RB2B publishes 2 APIs on the [APIs.io](https://apis.io/) network: Identification API and Enrichment API. Tagged areas include Identity Resolution, Visitor Identification, B2B Data, Lead Generation, and Sales Intelligence.


  RB2B''s developer surface includes pricing, support, and 13 more developer resources.'
random_paper: 40
score:
  band: minimal
  composite: 12.3
  delta: -2.3
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rb2b/refs/heads/main/screenshots/rb2b-2026-06-20T192625.png
security:
- kind: domain-security
  name: Rb2B Domain Security
  slug: rb2b-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rb2B Trust Center
  slug: rb2b-trust-center
  summary_line: SOC 2, GDPR
slug: rb2b
tags:
- Identity Resolution
- Visitor Identification
- B2B Data
- Lead Generation
- Sales Intelligence
- Marketing
- Data Enrichment
- LinkedIn Enrichment
- Hashed Email
- Mobile Ad ID
- Firmographics
- Webhooks
- Pixel
- Adtech
- Identity Graph
website: https://www.rb2b.com
---
