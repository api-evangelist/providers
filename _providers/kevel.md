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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Kevel Agentic Access
  operation_count: 33
  slug: kevel-agentic-access
  summary_line: 33 operations · 17 acting
api_count: 14
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
- description: Manage ads.
  name: Kevel Ads API
  slug: kevel-ads-api
- description: Manage advertiser accounts.
  name: Kevel Advertisers API
  slug: kevel-advertisers-api
- description: Manage campaigns.
  name: Kevel Campaigns API
  slug: kevel-campaigns-api
- description: Manage channels.
  name: Kevel Channels API
  slug: kevel-channels-api
- description: Manage creatives.
  name: Kevel Creatives API
  slug: kevel-creatives-api
- description: Request ad decisions and creatives.
  name: Kevel Decision API
  slug: kevel-decision-api
- description: Manage flights (line items).
  name: Kevel Flights API
  slug: kevel-flights-api
- description: Queue and retrieve performance reports.
  name: Kevel Reporting API
  slug: kevel-reporting-api
- description: Manage sites.
  name: Kevel Sites API
  slug: kevel-sites-api
- description: Manage zones.
  name: Kevel Zones API
  slug: kevel-zones-api
artifact_total: 22
collections:
- collection_type: open
  name: Kevel APIs
  slug: open-kevel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kevel-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kevel-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kevel-domain-security.yml
- group: auth
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
- name: Kevel Finops
  service_category: API
  slug: kevel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kevel.png
layout: provider
modified: '2026-04-28'
name: Kevel
nav: Providers
network: true
overview: 'Kevel publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Advertisers API, Campaigns API, and 7 more. Tagged areas include Ad Serving, Advertising, API-First, Audience, and Monetization.


  Kevel''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Kevel Plans Pricing
  plan_count: 3
  slug: kevel-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Kevel Rate Limits
  slug: kevel-rate-limits
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 57.4
    developer_ergonomics: 54.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kevel/refs/heads/main/screenshots/kevel-2026-06-20T184002.png
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
- Audience
- Monetization
- Reporting
website: https://www.kevel.com
---
