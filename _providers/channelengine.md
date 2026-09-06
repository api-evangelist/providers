---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: 'Integrate the system of your choice (ERP, PIM, WMS, or webstore) with ChannelEngine. Synchronize product content and offers; retrieve, acknowledge and update orders, shipments, returns, cancellations '
  name: ChannelEngine Merchant API
  slug: channelengine-merchant-api
- description: Set up your own marketplace on ChannelEngine with automated connections between your marketplace and partnering merchants. Synchronize product data and offer changes, create and invoice orders, and ha
  name: ChannelEngine Channel API
  slug: channelengine-channel-api
- description: Export the categories and product data attributes of your marketplace to ChannelEngine via a unified approach, so merchants can map and list against your channel's taxonomy.
  name: ChannelEngine Channel Management API
  slug: channelengine-channel-management-api
artifact_total: 8
asyncapis:
- description: ''
  name: Channelengine Webhooks
  slug: channelengine-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/channelengine-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/channelengine-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/channelengine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.channelengine.com/security
- group: company
  title: ''
  type: Website
  url: https://www.channelengine.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.channelengine.com/developer-hub
- group: docs
  title: ''
  type: Documentation
  url: https://support.channelengine.com/hc/en-us/categories/4419833201937-APIs
- group: docs
  title: ''
  type: APIReference
  url: https://support.channelengine.com/hc/en-us/articles/25437375786013-ChannelEngine-API-references
- group: start
  title: ''
  type: GettingStarted
  url: https://support.channelengine.com/hc/en-us/articles/10023835402397-Merchant-API-getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.channelengine.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.channelengine.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.channelengine.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/channelengine
- group: commercial
  title: ''
  type: Pricing
  url: https://www.channelengine.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.channelengine.net/login
- group: start
  title: ''
  type: Login
  url: https://www.channelengine.net/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.channelengine.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.channelengine.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.channelengine.com/hc/en-us/articles/4409484849309-ChannelEngine-release-notes
- group: auth
  title: ''
  type: Authentication
  url: authentication/channelengine-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/channelengine-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/channelengine-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/channelengine-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/channelengine-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/channelengine-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/channelengine-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/channelengine-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/channelengine-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/channelengine-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/channelengine-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/channelengine-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/channelengine-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/channelengine-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.channelengine.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.channelengine.com/security
- group: design
  title: ''
  type: DataModel
  url: data-model/channelengine-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/channelengine-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/channelengine-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'ChannelEngine is a marketplace integration and multichannel e-commerce platform, founded in Leiden, Netherlands and backed by General Catalyst, that lets brands, retailers, and manufacturers connect their ERP, PIM, WMS, or webstore once and sell across 1,300+ global marketplaces, social platforms, and emerging AI commerce channels. It centralizes product listing, inventory and offer synchronization, order and fulfillment management, returns, and dynamic repricing from a single dashboard, and exposes three REST APIs: the Merchant API (integrate your own systems with ChannelEngine), the Channel API (build your own marketplace on ChannelEngine), and the Channel Management API (export marketplace categories and product attributes). The APIs use API-key authentication, JSON response envelopes, page-based pagination, header-based rate limiting, and webhooks for near-real-time events.'
image: https://www.channelengine.com/hubfs/ChannelEngine-Logomark.png
layout: provider
modified: '2026-07-18'
name: ChannelEngine
nav: Providers
network: true
overview: 'ChannelEngine publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace Integration, Multi-Channel Commerce, and Order Management.


  The ChannelEngine catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ChannelEngine''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 53.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/channelengine/refs/heads/main/screenshots/channelengine-2026-07-25T205043.png
security:
- kind: authentication
  name: Channelengine Authentication
  slug: channelengine-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Channelengine Domain Security
  slug: channelengine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Channelengine Vulnerability Disclosure
  slug: channelengine-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Channelengine Trust Center
  slug: channelengine-trust-center
  summary_line: ISO 27001, GDPR
slug: channelengine
tags:
- Company
- E-Commerce
- Marketplace Integration
- Multi-Channel Commerce
- Order Management
- Inventory Management
- Product Information
- Retail
- Webhook
- Netherlands
website: https://www.channelengine.com/
---
