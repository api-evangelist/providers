---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Istock Agentic Access
  operation_count: 12
  slug: istock-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: Reference data
  name: iStock Countries API
  slug: istock-countries-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: License and download assets
  name: iStock Downloads API
  slug: istock-downloads-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: Image metadata retrieval
  name: iStock Images API
  slug: istock-images-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: Search creative and editorial assets
  name: iStock Search API
  slug: istock-search-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: Video metadata retrieval
  name: iStock Videos API
  slug: istock-videos-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The AffiliateSearch API from iStock — 2 operation(s) for affiliatesearch.
  name: iStock Affiliate Search API
  slug: istock-affiliatesearch-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The AiGenerator API from iStock — 18 operation(s) for aigenerator.
  name: iStock AI Generator API
  slug: istock-aigenerator-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Artists API from iStock — 2 operation(s) for artists.
  name: iStock Artists API
  slug: istock-artists-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The AssetChanges API from iStock — 3 operation(s) for assetchanges.
  name: iStock Asset Changes API
  slug: istock-assetchanges-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The AssetLicensing API from iStock — 1 operation(s) for assetlicensing.
  name: iStock Asset Licensing API
  slug: istock-assetlicensing-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Boards API from iStock — 8 operation(s) for boards.
  name: iStock Boards API
  slug: istock-boards-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Collections API from iStock — 1 operation(s) for collections.
  name: iStock Collections API
  slug: istock-collections-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Customers API from iStock — 1 operation(s) for customers.
  name: iStock Customers API
  slug: istock-customers-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Events API from iStock — 2 operation(s) for events.
  name: iStock Events API
  slug: istock-events-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The ImageMatch API from iStock — 1 operation(s) for imagematch.
  name: iStock Image Match API
  slug: istock-imagematch-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Orders API from iStock — 1 operation(s) for orders.
  name: iStock Orders API
  slug: istock-orders-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Products API from iStock — 1 operation(s) for products.
  name: iStock Products API
  slug: istock-products-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Purchases API from iStock — 1 operation(s) for purchases.
  name: iStock Purchases API
  slug: istock-purchases-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Usage API from iStock — 1 operation(s) for usage.
  name: iStock Usage API
  slug: istock-usage-api
artifact_total: 34
collections:
- collection_type: open
  name: iStock API (Getty Images Platform) Countries API
  slug: open-istock-countries-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries Downloads API
  slug: open-istock-downloads-api
- collection_type: open
  name: iStock API (Getty Platform) Countries Images API
  slug: open-istock-images-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries OAuth API
  slug: open-istock-oauth-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries Search API
  slug: open-istock-search-api
- collection_type: open
  name: iStock API (Getty Images Platform) Countries Videos API
  slug: open-istock-videos-api
- collection_type: open
  name: iStock API (Getty Images Platform)
  slug: open-istock
common:
- group: company
  title: ''
  type: Blog
  url: https://www.istockphoto.com/blog
- group: other
  href: https://artifacts.apis.io/istock/capabilities/istock-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/istock-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/istock/agentic-access/istock-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/istock-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/istock/security/istock-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/istock-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/istock/security/istock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/istock-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/istock/authentication/istock-authentication.yml
  title: ''
  type: Authentication
  url: authentication/istock-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/istockphoto
- group: company
  title: ''
  type: Website
  url: https://www.istockphoto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gettyimages.com/
- group: commercial
  href: https://artifacts.apis.io/istock/plans/istock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/istock-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/istock/rate-limits/istock-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/istock-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/istock/finops/istock-finops.yml
  title: ''
  type: FinOps
  url: finops/istock-finops.yml
created: '2026-05-08'
description: iStock is Getty Images' royalty-free stock media brand for affordable, subscription-based image, video, illustration, and audio licensing. iStock shares Getty's underlying API platform; partner API access is gated and tied to a commercial licensing agreement.
finops:
- has_sources: true
  method: generated
  name: Istock Finops
  primary_unit: ''
  service_category: Stock Media
  slug: istock-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/istock.png
layout: provider
modified: '2026-10-06'
name: iStock
nav: Providers
network: true
overview: 'iStock publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Countries API, Downloads API, Images API, and 16 more. Tagged areas include Stock Media, Image, Video, Illustrations, and Royalty-Free.


  The iStock catalog on APIs.io includes 1 Spectral governance ruleset.


  iStock''s developer surface includes engineering blog, authentication, and 10 more developer resources.'
plans:
- name: Istock Plans Pricing
  plan_count: 3
  slug: istock-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Istock Rate Limits
  slug: istock-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: iStock API Rules
  rule_count: 52
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 10
  slug: istock-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 42.9
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 26.9
      derived: 0
      marker_coverage: 73.1
      total: 26
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/istock/istock-2026-06-20T183628.png
security:
- kind: authentication
  name: Istock Authentication
  slug: istock-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Istock Domain Security
  slug: istock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Istock Vulnerability Disclosure
  slug: istock-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: istock
tags:
- Stock Media
- Image
- Video
- Illustrations
- Royalty-Free
- Getty
website: https://www.istockphoto.com/
---
