---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
asyncapis:
- description: ''
  name: Coefficient Works Webhooks
  slug: coefficient-works-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/coefficient-works/security/coefficient-works-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coefficient-works-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coefficient.io/
- group: other
  title: ''
  type: Product
  url: https://coefficient.io/product
- group: docs
  title: ''
  type: Documentation
  url: https://help.coefficient.io/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://help.coefficient.io/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://coefficient.io/get-started
- group: company
  title: ''
  type: Blog
  url: https://coefficient.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://coefficient.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coefficient.io/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coefficient.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coefficient.io/privacy-policy
- group: operate
  title: ''
  type: Community
  url: https://coefficient.io/community
- group: company
  title: ''
  type: About
  url: https://coefficient.io/about
- group: operate
  title: ''
  type: ContactUs
  url: https://coefficient.io/contact
- group: company
  title: ''
  type: Careers
  url: https://coefficient.io/careers
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.atlassian.com/vendors/1220522/coefficient-works-inc
- group: other
  title: ''
  type: Templates
  url: https://coefficient.io/templates
- group: agent
  href: https://artifacts.apis.io/coefficient-works/llms/coefficient-works-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coefficient-works-llms.txt
- group: design
  href: https://artifacts.apis.io/coefficient-works/asyncapi/coefficient-works-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coefficient-works-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/coefficient-works/rate-limits/coefficient-works-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coefficient-works-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coefficient-works/plans/coefficient-works-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coefficient-works-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coefficient-works/conformance/coefficient-works-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coefficient-works-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coefficient.io/data-security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coeff
created: '2026-07-17'
description: 'Coefficient Works, Inc. (operating as Coefficient) is a San Mateo, California no-code data platform that connects live business data to Google Sheets and Microsoft Excel. Founded in 2019 by Navneet Loiwal and Tommy Tsai, the company provides point-and-click connectors to 60+ business systems including Salesforce, HubSpot, NetSuite, QuickBooks, Snowflake, MySQL, Stripe, Looker, Tableau and Google Ads, with scheduled two-way sync, spreadsheet-native alerting through Slack and email, live web dashboards, and an AI assistant that builds pivot tables, formulas, charts and data-cleaning steps from natural language. Coefficient is a consumer of other providers'' APIs rather than a producer: as of this enrichment pass it publishes no public developer API, no OpenAPI or AsyncAPI description, no client SDKs, and no developer portal, and its "Connect Any API" feature is a consumer-side HTTP client (GET/POST, bearer token / API key / basic auth, cursor, offset and page-number pagination)
  that writes third-party API responses into a sheet. The one programmatic surface Coefficient serves is an inbound webhook trigger URL, issued per import on the Pro and Enterprise plans, that an external system calls to force an immediate refresh — capped at 12 calls per hour with a five-minute minimum interval. Coefficient states it is SOC 2 compliant and provides the audit report on request. Distribution is through the Google Workspace Marketplace and Microsoft AppSource. The company is backed by Battery Ventures, Foundation Capital and S28 Capital.'
finops:
- has_sources: true
  method: derived
  name: Coefficient Works Finops
  primary_unit: user
  service_category: ''
  slug: coefficient-works-finops
  template: false
image: https://coefficient.io/wp-content/uploads/2026/02/homepage-meta-image-v2.png
layout: provider
modified: '2026-08-14'
name: Coefficient Works
nav: Providers
network: true
overview: 'Coefficient Works is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spreadsheets, Google Sheets, Microsoft Excel, and Data Integration.


  The Coefficient Works catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coefficient Works'' developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Coefficient Works Plans Pricing
  plan_count: 4
  slug: coefficient-works-plans-pricing
- name: Coefficient Works Price Estimates
  plan_count: 0
  slug: coefficient-works-price-estimates
random_paper: 10
rate_limits:
- limit_count: 2
  name: Coefficient Works Rate Limits
  slug: coefficient-works-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.0
    catalog_earned_first_party: 20.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 31.6
  previous_composite: 47.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coefficient-works/coefficient-works-2026-07-25T205946.png
security:
- kind: domain-security
  name: Coefficient Works Domain Security
  slug: coefficient-works-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coefficient-works
tags:
- Company
- Spreadsheets
- Google Sheets
- Microsoft Excel
- Data Integration
- No-Code
- Business Intelligence
- Reporting
- Revenue Operations
- Software-as-a-Service
website: https://coefficient.io/
---
