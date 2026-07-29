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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
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
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Wistia Agentic Access
  operation_count: 48
  slug: wistia-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 13
apis:
- description: REST API providing programmatic access to medias, projects, accounts, customizations, captions, and statistics in a Wistia account. Data is returned in JSON over HTTPS. Authentication uses Bearer Toke
  name: Wistia Data API
  slug: data-api
- description: Endpoint for uploading video files directly to a Wistia account, typically used in conjunction with the Data API to manage uploaded media. Authentication uses the same API access token.
  name: Wistia Upload API
  slug: upload-api
- description: Real-time webhook deliveries from Wistia for documented media lifecycle events. Deliveries are HTTP POST with a JSON body and are signed via HMAC-SHA256 using the consumer's configured webhook secret,
  name: Wistia Webhooks
  slug: webhooks
- description: The Account API from Wistia — 1 operation(s) for account.
  name: Wistia Account API
  slug: wistia-account-api
- description: The AllowedDomains API from Wistia — 2 operation(s) for alloweddomains.
  name: Wistia AllowedDomains API
  slug: wistia-alloweddomains-api
- description: The Captions API from Wistia — 3 operation(s) for captions.
  name: Wistia Captions API
  slug: wistia-captions-api
- description: The Channels API from Wistia — 2 operation(s) for channels.
  name: Wistia Channels API
  slug: wistia-channels-api
- description: The Customizations API from Wistia — 1 operation(s) for customizations.
  name: Wistia Customizations API
  slug: wistia-customizations-api
- description: The Folders API from Wistia — 3 operation(s) for folders.
  name: Wistia Folders API
  slug: wistia-folders-api
- description: The Medias API from Wistia — 8 operation(s) for medias.
  name: Wistia Medias API
  slug: wistia-medias-api
- description: The Tags API from Wistia — 3 operation(s) for tags.
  name: Wistia Tags API
  slug: wistia-tags-api
- description: The Tokens API from Wistia — 1 operation(s) for tokens.
  name: Wistia Tokens API
  slug: wistia-tokens-api
- description: The Webinars API from Wistia — 3 operation(s) for webinars.
  name: Wistia Webinars API
  slug: wistia-webinars-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of Wistia's webhook surface. Wistia delivers real-time notifications about media lifecycle events to a consumer endpoint configured in your Wistia account. All webhooks are de
  name: Wistia Webhooks API
  slug: wistia-asyncapi
collections:
- collection_type: open
  name: Wistia Data API
  slug: open-wistia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wistia-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wistia-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wistia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wistia-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wistia
- group: company
  title: ''
  type: Website
  url: https://wistia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wistia.com
- group: commercial
  title: ''
  type: Pricing
  url: https://wistia.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://wistia.com/signup
- group: operate
  title: ''
  type: Support
  url: https://wistia.com/support
- group: other
  title: ''
  type: Developers
  url: https://docs.wistia.com
- group: company
  title: ''
  type: Blog
  url: https://wistia.com/learn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wistia
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.wistia.com/llms.txt
created: '2026-05-11'
description: Wistia is an all-in-one video marketing platform for businesses that combines branded video hosting, webinars, video editing, webcam and screen recording, and deep viewer analytics for B2B marketing teams focused on lead generation, brand control, and content performance. Founded in 2006, Wistia is used by more than 425,000 businesses and integrates with major marketing automation and CRM platforms. Wistia exposes a Data API at https://api.wistia.com/v1 for programmatic access to medias, projects, customizations, accounts, and analytics, with authentication via Bearer Token or HTTP Basic using an API access token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wistia.png
layout: provider
modified: '2026-05-30'
name: Wistia
nav: Providers
network: true
overview: 'Wistia publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, AllowedDomains API, and 8 more. Tagged areas include Video Hosting, Video Marketing, Video Analytics, Lead Generation, and Webinars.


  The Wistia catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Wistia''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 17
rules:
- name: Wistia API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: wistia-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.9
  delta: -3.5
  facets:
    commercial_clarity: 18.4
    contract_quality: 63.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 5.3
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wistia/refs/heads/main/screenshots/wistia-2026-06-20T201532.png
security:
- kind: authentication
  name: Wistia Authentication
  slug: wistia-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Wistia Domain Security
  slug: wistia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wistia Trust Center
  slug: wistia-trust-center
  summary_line: SOC 2, PCI DSS, FedRAMP, GDPR
slug: wistia
tags:
- Video Hosting
- Video Marketing
- Video Analytics
- Lead Generation
- Webinars
- B2B Marketing
website: https://wistia.com
---
