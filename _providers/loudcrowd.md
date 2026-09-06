---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-05'
api_count: 4
apis:
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The Attribution Events API API from LoudCrowd — 1 operation(s) for attribution events api.
  name: LoudCrowd Attribution Events API
  slug: loudcrowd-attribution-events-api-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The Brand API API from LoudCrowd — 1 operation(s) for brand api.
  name: LoudCrowd Brand API
  slug: loudcrowd-brand-api-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The Product Data API from LoudCrowd — 1 operation(s) for product data.
  name: LoudCrowd Product Data API
  slug: loudcrowd-product-data-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The StorefrontAmbassador API from LoudCrowd — 1 operation(s) for storefrontambassador.
  name: LoudCrowd Storefront Ambassador API
  slug: loudcrowd-storefrontambassador-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The StorefrontCollections API from LoudCrowd — 1 operation(s) for storefrontcollections.
  name: LoudCrowd Storefront Collections API
  slug: loudcrowd-storefrontcollections-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The StorefrontFeedItems API from LoudCrowd — 1 operation(s) for storefrontfeeditems.
  name: LoudCrowd Storefront Feed Items API
  slug: loudcrowd-storefrontfeeditems-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The StorefrontMediaDetails API from LoudCrowd — 1 operation(s) for storefrontmediadetails.
  name: LoudCrowd Storefront Media Details API
  slug: loudcrowd-storefrontmediadetails-api
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The StorefrontProductDetails API from LoudCrowd — 1 operation(s) for storefrontproductdetails.
  name: LoudCrowd Storefront Product Details API
  slug: loudcrowd-storefrontproductdetails-api
artifact_total: 13
asyncapis:
- description: ''
  name: Loudcrowd Attribution Events
  slug: loudcrowd-attribution-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loudcrowd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loudcrowd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loudcrowd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.loudcrowd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.loudcrowd.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.loudcrowd.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.loudcrowd.com/docs/implementation-overview-custom-ecommerce
- group: operate
  title: ''
  type: Support
  url: https://help.loudcrowd.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.loudcrowd.com/en/
- group: company
  title: ''
  type: Blog
  url: https://loudcrowd.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://loudcrowd.com/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://loudcrowd.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://loudcrowd.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.loudcrowd.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loudcrowd.com/legal/platform-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loudcrowd.com/legal/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://loudcrowd.com/legal/dpa/
- group: build
  title: ''
  type: Packages
  url: packages/loudcrowd-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/loudcrowd-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loudcrowd-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/loudcrowd-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/loudcrowd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loudcrowd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loudcrowd-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loudcrowd-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loudcrowd-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/loudcrowd-components.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/loudcrowd-tool-crosswalk.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/loudcrowd-attribution-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loudcrowd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loudcrowd-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/loudcrowd-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/loudcrowd-creator-storefronts-overlay.yaml
- group: agent
  title: ''
  type: WellKnown-Probe
  url: well-known/loudcrowd-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/loudcrowd-mcp.yml
created: '2026-08-25'
description: 'LoudCrowd is a creator-commerce platform for consumer brands, combining an influencer/ambassador and affiliate marketing platform, on-domain Creator Storefronts, a ShopWith AI shopping concierge for product detail pages, AI Influencer Agents for discovery, outreach and moderation, and Creator GEO for turning earned creator content into AI-recommendable assets. For developers it publishes a small, purpose-built OpenAPI 3.0 surface across three services: a read-only account-scoped Brand API for pulling program-attributed orders, an HMAC-SHA256-signed Attribution Events API for pushing order create/update/cancel and refund events plus product-catalog batches from custom and headless commerce stacks, and a Creator Storefronts data API used in place of the hosted storefront web components. A browser SDK loaded from pub.loudcrowd.com renders storefront and influencer-list app blocks and performs first-party affiliate attribution on Shopify, Salesforce Commerce Cloud and custom sites.'
image: https://loudcrowd.com/og-default.png
layout: provider
modified: '2026-08-25'
name: LoudCrowd
nav: Providers
network: true
overview: 'LoudCrowd publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attribution Events API, Brand API, Product Data API, and 5 more. Tagged areas include Creator Marketing, Influencer Marketing, Affiliate Marketing, E-Commerce, and Creator Commerce.


  The LoudCrowd catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LoudCrowd''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Loudcrowd Plans Pricing
  plan_count: 5
  slug: loudcrowd-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Loudcrowd Rate Limits
  slug: loudcrowd-rate-limits
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 61.7
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 52.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loudcrowd/refs/heads/main/screenshots/loudcrowd-2026-09-02T150320.png
security:
- kind: authentication
  name: Loudcrowd Authentication
  slug: loudcrowd-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Loudcrowd Domain Security
  slug: loudcrowd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: loudcrowd
tags:
- Creator Marketing
- Influencer Marketing
- Affiliate Marketing
- E-Commerce
- Creator Commerce
- Attribution
- Social Commerce
- Shopify
- User Generated Content
- Commissions
- Retail
- Marketing
website: https://loudcrowd.com/
---
