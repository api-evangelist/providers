---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: 'OAuth 2.0 token endpoint that issues bearer access tokens used to authenticate calls to the rest of Bombora''s developer APIs. Clients exchange credentials for a short-lived access token via a POST to '
  name: Bombora Authentication API
  slug: bombora-authentication-api
- description: 'Streams Bombora''s Company Surge intent signals — account-level scores against 18,000+ B2B intent topics — derived from the Bombora Data Cooperative. Subscribers pull weekly Surge scores for monitored '
  name: Bombora Intent API
  slug: bombora-intent-api
- description: Reference data and taxonomy lookups for the Bombora platform — including intent topics, topic clusters, and supporting metadata needed to interpret intent and audience responses. Used by integrators t
  name: Bombora Reference API
  slug: bombora-reference-api
- description: Programmatic interface to Bombora's Digital Audience Builder for composing custom B2B audiences from intent, firmographic, and behavioral signals and activating them to downstream data exchanges, DSPs
  name: Bombora Digital Audience Builder (DAB) API
  slug: bombora-digital-audience-api
- description: Outbound webhook destinations that push Bombora events — including Surge report completions and audience activation updates — to partner endpoints. Destinations are registered and updated via PUT rout
  name: Bombora Webhooks API
  slug: bombora-webhooks-api
- description: Partner API for orchestrating Company Surge reports — create reports with topic, geography, blacklist, and AutoGen options (POST /v4/Surge/Create), list reports (GET /v4/Surge/GetList), and retrieve r
  name: Bombora Company Surge API (v4)
  slug: bombora-company-surge-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bombora-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bombora.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bombora.com
- group: other
  title: ''
  type: GetStarted
  url: https://developer.bombora.com/get-started
- group: other
  title: ''
  type: APIs
  url: https://developer.bombora.com/apis
- group: other
  title: ''
  type: APIChangePolicy
  url: https://developer.bombora.com/api-change-policy
- group: docs
  title: ''
  type: PartnerDocs
  url: https://bombora-partners.atlassian.net/wiki/spaces/DOC/overview
- group: other
  title: ''
  type: CustomerResourceCenter
  url: https://customers.bombora.com
- group: other
  title: ''
  type: CompanySurge
  url: https://bombora.com/company-surge-intent-data
- group: company
  title: ''
  type: AboutUs
  url: https://bombora.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://bombora.com/careers
- group: commercial
  title: ''
  type: Privacy
  url: https://bombora.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bombora.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bombora
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/bomboradata
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BomboraNYC
- group: company
  title: ''
  type: Blog
  url: https://bombora.com/feed/
created: '2026-05-25'
description: Bombora is a New York-based B2B data company that provides intent data and identity solutions used by marketing, sales, and ad-tech teams to identify in-market accounts and personalize outreach. Its flagship product, Company Surge, aggregates anonymous content-consumption signals from a cooperative of more than 5,000 B2B publishers and scores accounts against 18,000+ B2B intent topics to surface organizations actively researching specific products, services, and categories. Beyond Company Surge, Bombora offers Identity and Enrichment for first-party visitor resolution, Digital Audiences for activation across DSPs and walled gardens, Campaign Measurement for B2B attribution, and an Insights Suite that combines intent, visitor, and engagement signals. Bombora exposes a developer portal at developer.bombora.com with OAuth 2.0 authentication and a catalog of REST APIs covering intent feeds, reference taxonomies, digital audience activation, webhooks, and Company Surge report orchestration
  (v4 via sentry.bombora.com). The portal's API reference is gated behind login and Bombora does not publish public OpenAPI specifications; commercial access is sold via annual contracts with no public pricing, typically starting around $30K/year and scaling with topic volume and integration scope. Bombora integrates broadly with the B2B revenue stack, including Salesforce, HubSpot, LinkedIn, 6sense, Demandbase, Apollo, ZoomInfo, Dun and Bradstreet, Snowflake, and Adobe Experience Platform, and is profiled here for its role as the dominant supplier of cooperative-sourced B2B intent data.
graphqls:
- description: Bombora is the leading provider of cooperative-sourced B2B intent data. Its flagship product, Company Surge, aggregates anonymous content-consumption signals from more than 5,000 B2B publishers and sc
  name: Bombora GraphQL Schema
  slug: bombora-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bombora.png
layout: provider
modified: '2026-05-25'
name: Bombora
nav: Providers
network: true
overview: 'Bombora publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Intent Data, B2B Intent, Company Surge, Account Based Marketing, and Sales Intelligence.


  Bombora''s developer surface includes privacy policy, YouTube channel, engineering blog, and 14 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 24.9
  delta: 9.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bombora/refs/heads/main/screenshots/bombora-2026-06-20T173557.png
security:
- kind: domain-security
  name: Bombora Domain Security
  slug: bombora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bombora
tags:
- Intent Data
- B2B Intent
- Company Surge
- Account Based Marketing
- Sales Intelligence
- Marketing Intelligence
- Identity Resolution
- Audience Activation
- Data Cooperative
- Webhooks
- Reference Data
- Adtech
- Martech
- B2B
website: https://bombora.com
---
