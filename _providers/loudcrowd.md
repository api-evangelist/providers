---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
api_count: 2
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
- baseURL: https://api.loudcrowd.com
  baseurl_source: declared
  description: The Storefront Collections API from LoudCrowd — 1 operation(s) for storefront collections.
  name: LoudCrowd Storefront Collections API
  slug: loudcrowd-storefront-collections-api
artifact_total: 21
asyncapis:
- description: ''
  name: Loudcrowd Attribution Events
  slug: loudcrowd-attribution-events
common:
- group: other
  href: https://artifacts.apis.io/loudcrowd/capabilities/loudcrowd-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/loudcrowd-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/loudcrowd/security/loudcrowd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loudcrowd-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/loudcrowd/authentication/loudcrowd-authentication.yml
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
  href: https://artifacts.apis.io/loudcrowd/packages/loudcrowd-packages.yml
  title: ''
  type: Packages
  url: packages/loudcrowd-packages.yml
- group: build
  href: https://artifacts.apis.io/loudcrowd/packages/loudcrowd-packages.yml
  title: ''
  type: SDKs
  url: packages/loudcrowd-packages.yml
- group: agent
  href: https://artifacts.apis.io/loudcrowd/llms/loudcrowd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loudcrowd-llms.txt
- group: design
  href: https://artifacts.apis.io/loudcrowd/conventions/loudcrowd-conventions.yml
  title: ''
  type: Conventions
  url: conventions/loudcrowd-conventions.yml
- group: design
  href: https://artifacts.apis.io/loudcrowd/conventions/loudcrowd-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/loudcrowd-conventions.yml
- group: design
  href: https://artifacts.apis.io/loudcrowd/errors/loudcrowd-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loudcrowd-problem-types.yml
- group: design
  href: https://artifacts.apis.io/loudcrowd/lifecycle/loudcrowd-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/loudcrowd-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/loudcrowd/conformance/loudcrowd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loudcrowd-conformance.yml
- group: design
  href: https://artifacts.apis.io/loudcrowd/data-model/loudcrowd-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loudcrowd-data-model.yml
- group: design
  href: https://artifacts.apis.io/loudcrowd/components/loudcrowd-components.yml
  title: ''
  type: Components
  url: components/loudcrowd-components.yml
- group: build
  href: https://artifacts.apis.io/loudcrowd/mcp/loudcrowd-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/loudcrowd-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/loudcrowd/asyncapi/loudcrowd-attribution-events.yml
  title: ''
  type: EventCatalog
  url: asyncapi/loudcrowd-attribution-events.yml
- group: agent
  href: https://artifacts.apis.io/loudcrowd/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/loudcrowd/plans/loudcrowd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loudcrowd-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/loudcrowd/rate-limits/loudcrowd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loudcrowd-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/loudcrowd/overlays/loudcrowd-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/loudcrowd-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/loudcrowd/overlays/loudcrowd-creator-storefronts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/loudcrowd-creator-storefronts-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/loudcrowd/well-known/loudcrowd-well-known.yml
  title: ''
  type: WellKnown-Probe
  url: well-known/loudcrowd-well-known.yml
- group: agent
  href: https://artifacts.apis.io/loudcrowd/mcp/loudcrowd-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/loudcrowd-mcp.yml
created: '2026-08-25'
description: 'LoudCrowd is a creator-commerce platform for consumer brands, combining an influencer/ambassador and affiliate marketing platform, on-domain Creator Storefronts, a ShopWith AI shopping concierge for product detail pages, AI Influencer Agents for discovery, outreach and moderation, and Creator GEO for turning earned creator content into AI-recommendable assets. For developers it publishes a small, purpose-built OpenAPI 3.0 surface across three services: a read-only account-scoped Brand API for pulling program-attributed orders, an HMAC-SHA256-signed Attribution Events API for pushing order create/update/cancel and refund events plus product-catalog batches from custom and headless commerce stacks, and a Creator Storefronts data API used in place of the hosted storefront web components. A browser SDK loaded from pub.loudcrowd.com renders storefront and influencer-list app blocks and performs first-party affiliate attribution on Shopify, Salesforce Commerce Cloud and custom sites.'
finops:
- has_sources: true
  method: derived
  name: Loudcrowd Finops
  primary_unit: subscription
  service_category: ''
  slug: loudcrowd-finops
  template: false
image: https://loudcrowd.com/og-default.png
layout: provider
modified: '2026-08-25'
name: LoudCrowd
nav: Providers
network: true
overview: 'LoudCrowd publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attribution Events API, Brand API, Product Data API, and 5 more. Tagged areas include Creator Marketing, Influencer Marketing, Affiliate Marketing, E-Commerce, and Creator Commerce.


  The LoudCrowd catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LoudCrowd''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Loudcrowd Plans Pricing
  plan_count: 6
  slug: loudcrowd-plans-pricing
- name: Loudcrowd Price Estimates
  plan_count: 0
  slug: loudcrowd-price-estimates
random_paper: 19
rate_limits:
- limit_count: 0
  name: Loudcrowd Rate Limits
  slug: loudcrowd-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: LoudCrowd API Rules
  rule_count: 61
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 2
  slug: loudcrowd-rules
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 54.8
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 55.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/loudcrowd/loudcrowd-2026-09-02T150320.png
security:
- kind: authentication
  name: Loudcrowd Authentication
  slug: loudcrowd-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Loudcrowd Domain Security
  slug: loudcrowd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: loudcrowd-process-returns
  slug: loudcrowd-process-returns
- name: loudcrowd-pull-attributed-orders
  slug: loudcrowd-pull-attributed-orders
- name: loudcrowd-render-creator-storefront
  slug: loudcrowd-render-creator-storefront
- name: loudcrowd-submit-order-events
  slug: loudcrowd-submit-order-events
- name: loudcrowd-sync-product-catalog
  slug: loudcrowd-sync-product-catalog
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
