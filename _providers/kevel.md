---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Kevel Agentic Access
  operation_count: 33
  slug: kevel-agentic-access
  summary_line: 33 operations · 17 acting
api_count: 1
apis:
- description: The Decision API enables ad requests without using ad code. By posting to a RESTful endpoint, Kevel's ad engine returns decision data and creative contents for serving ads in your application across w
  name: Kevel Decision API
  slug: decision-api
- description: 'The Management API provides programmatic access to manage advertisers, campaigns, flights, ads, creatives, channels, sites, zones, and other platform resources. It is the system-of-record API used to '
  name: Kevel Management API
  slug: management-api
- description: The Reporting API exposes ad serving performance data, allowing customers to pull impressions, clicks, conversions, revenue, and other metrics by advertiser, campaign, flight, ad, creative, site, zone
  name: Kevel Reporting API
  slug: reporting-api
- description: The UserDB API provides first-party audience and user data management, enabling customers to read and write user keys, custom properties, interests, and audience segment membership for targeting in th
  name: Kevel UserDB API
  slug: userdb-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Ad API from Kevel — 5 operation(s) for ad.
  name: Kevel Ad API
  slug: kevel-ad-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Adtypes API from Kevel — 2 operation(s) for adtypes.
  name: Kevel Adtypes API
  slug: kevel-adtypes-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Advertiser API from Kevel — 8 operation(s) for advertiser.
  name: Kevel Advertiser API
  slug: kevel-advertiser-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Campaign API from Kevel — 4 operation(s) for campaign.
  name: Kevel Campaign API
  slug: kevel-campaign-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Categories API from Kevel — 1 operation(s) for categories.
  name: Kevel Categories API
  slug: kevel-categories-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Category Catalog API from Kevel — 1 operation(s) for category catalog.
  name: Kevel Category Catalog API
  slug: kevel-category-catalog-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Channel API from Kevel — 8 operation(s) for channel.
  name: Kevel Channel API
  slug: kevel-channel-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The ChannelsInSite API from Kevel — 1 operation(s) for channelsinsite.
  name: Kevel Channels In Site API
  slug: kevel-channelsinsite-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The ChannelSite API from Kevel — 1 operation(s) for channelsite.
  name: Kevel Channel Site API
  slug: kevel-channelsite-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Countries API from Kevel — 1 operation(s) for countries.
  name: Kevel Countries API
  slug: kevel-countries-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Country API from Kevel — 2 operation(s) for country.
  name: Kevel Country API
  slug: kevel-country-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Creative API from Kevel — 3 operation(s) for creative.
  name: Kevel Creative API
  slug: kevel-creative-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Creative Templates API from Kevel — 3 operation(s) for creative templates.
  name: Kevel Creative Templates API
  slug: kevel-creative-templates-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Entitycounts API from Kevel — 1 operation(s) for entitycounts.
  name: Kevel Entitycounts API
  slug: kevel-entitycounts-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Fast API from Kevel — 2 operation(s) for fast.
  name: Kevel Fast API
  slug: kevel-fast-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Flight API from Kevel — 20 operation(s) for flight.
  name: Kevel Flight API
  slug: kevel-flight-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Instantcounts API from Kevel — 6 operation(s) for instantcounts.
  name: Kevel Instantcounts API
  slug: kevel-instantcounts-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Itemdb API from Kevel — 2 operation(s) for itemdb.
  name: Kevel Itemdb API
  slug: kevel-itemdb-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Login API from Kevel — 2 operation(s) for login.
  name: Kevel Login API
  slug: kevel-login-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Priority API from Kevel — 3 operation(s) for priority.
  name: Kevel Priority API
  slug: kevel-priority-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Region API from Kevel — 1 operation(s) for region.
  name: Kevel Region API
  slug: kevel-region-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Segment API from Kevel — 3 operation(s) for segment.
  name: Kevel Segment API
  slug: kevel-segment-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Site API from Kevel — 2 operation(s) for site.
  name: Kevel Site API
  slug: kevel-site-api
- baseURL: https://api.kevel.co
  baseurl_source: spec
  description: The Zone API from Kevel — 2 operation(s) for zone.
  name: Kevel Zone API
  slug: kevel-zone-api
artifact_total: 48
collections:
- collection_type: open
  name: Kevel APIs Ads API
  slug: open-kevel-ads-api
- collection_type: open
  name: Kevel APIs Ads Advertisers API
  slug: open-kevel-advertisers-api
- collection_type: open
  name: Kevel APIs Ads Campaigns API
  slug: open-kevel-campaigns-api
- collection_type: open
  name: Kevel APIs Ads Channels API
  slug: open-kevel-channels-api
- collection_type: open
  name: Kevel APIs Ads Creatives API
  slug: open-kevel-creatives-api
- collection_type: open
  name: Kevel APIs Ads Decision API
  slug: open-kevel-decision-api
- collection_type: open
  name: Kevel APIs Ads Flights API
  slug: open-kevel-flights-api
- collection_type: open
  name: Kevel APIs Ads Reporting API
  slug: open-kevel-reporting-api
- collection_type: open
  name: Kevel APIs Ads Sites API
  slug: open-kevel-sites-api
- collection_type: open
  name: Kevel APIs Ads Zones API
  slug: open-kevel-zones-api
- collection_type: open
  name: Kevel APIs
  slug: open-kevel
common:
- group: commercial
  href: https://artifacts.apis.io/kevel/plans/kevel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kevel-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kevel/rate-limits/kevel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kevel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kevel/finops/kevel-finops.yml
  title: ''
  type: FinOps
  url: finops/kevel-finops.yml
- group: other
  href: https://artifacts.apis.io/kevel/capabilities/kevel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kevel-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kevel/agentic-access/kevel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kevel-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kevel/security/kevel-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kevel-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kevel/security/kevel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kevel-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kevel/authentication/kevel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kevel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kevelapi
- group: company
  title: ''
  type: Website
  url: https://www.kevel.com
- group: start
  title: ''
  type: Portal
  url: https://dev.kevel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.kevel.com/docs/understanding-kevel
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.kevel.com/reference/getting-started-with-kevel
- group: docs
  title: ''
  type: Reference
  url: https://dev.kevel.com/reference
- group: build
  title: ''
  type: SDKs
  url: https://dev.kevel.com/docs/sdks
- group: company
  title: ''
  type: Blog
  url: https://www.kevel.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kevel.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.kevel.com/llms.txt
created: '2026-03-16'
description: Kevel is an API-first ad serving platform that lets brands and publishers build unified, fully customized ad systems supporting any ad format, any creative, and multiple demand sources. Kevel exposes a Decision API for ad requests, a Management API for campaign and creative operations, a Reporting API for performance analytics, and a UserDB API for first-party audience and user data.
finops:
- has_sources: false
  method: generated
  name: Kevel Finops
  primary_unit: request
  service_category: API
  slug: kevel-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kevel.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.kevel.com over HTTP.
  name: Kevel MCP Server
  slug: kevel
modified: '2026-04-28'
name: Kevel
nav: Providers
network: true
overview: 'Kevel publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad API, Adtypes API, Advertiser API, and 25 more. Tagged areas include Ad Serving, Advertising, API-First, Audiences, and Monetization.


  The Kevel catalog on APIs.io includes 1 Spectral governance ruleset.


  Kevel''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Kevel Plans Pricing
  plan_count: 3
  slug: kevel-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Kevel Rate Limits
  slug: kevel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Kevel API Rules
  rule_count: 44
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 10
  slug: kevel-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 49.1
    developer_ergonomics: 59.5
    discoverability: 66.7
    operational_transparency: 7.9
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 31.4
      derived: 0
      marker_coverage: 68.6
      total: 35
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/kevel/kevel-2026-06-20T184002.png
security:
- kind: authentication
  name: Kevel Authentication
  slug: kevel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kevel Domain Security
  slug: kevel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kevel Trust Center
  slug: kevel-trust-center
  summary_line: SOC 2, GDPR
slug: kevel
tags:
- Ad Serving
- Advertising
- API-First
- Audiences
- Monetization
- Reporting
website: https://www.kevel.com
---
