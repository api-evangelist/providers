---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Similarweb Agentic Access
  operation_count: 27
  slug: similarweb-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 14
apis:
- description: The SimilarWeb Batch API is optimized for large-scale bulk data extraction, supporting jobs of up to one million domains per request. It delivers data asynchronously to cloud storage destinations incl
  name: SimilarWeb Batch API
  slug: similarweb-batch-api
- description: Account credits, capabilities, and usage information
  name: SimilarWeb Account API
  slug: similarweb-account-api
- description: Mobile app downloads, active users, sessions, and demographics
  name: SimilarWeb App Intelligence API
  slug: similarweb-app-intelligence-api
- description: Batch API credit management
  name: SimilarWeb Credits API
  slug: similarweb-credits-api
- description: Geographic distribution of website traffic
  name: SimilarWeb Geography API
  slug: similarweb-geography-api
- description: Manage cloud storage integrations (S3, GCS, Snowflake)
  name: SimilarWeb Integrations API
  slug: similarweb-integrations-api
- description: Keyword analytics including organic and paid keyword data
  name: SimilarWeb Keywords API
  slug: similarweb-keywords-api
- description: Lead enrichment combining firmographics and web analytics
  name: SimilarWeb Lead Enrichment API
  slug: similarweb-lead-enrichment-api
- description: Global, country, and industry rank data
  name: SimilarWeb Rankings API
  slug: similarweb-rankings-api
- description: Submit, track, and retrieve bulk data report requests
  name: SimilarWeb Reports API
  slug: similarweb-reports-api
- description: Similar website discovery
  name: SimilarWeb Similar Sites API
  slug: similarweb-similar-sites-api
- description: Website traffic visits, bounce rate, pages per visit, visit duration
  name: SimilarWeb Traffic and Engagement API
  slug: similarweb-traffic-and-engagement-api
- description: Marketing channel traffic breakdown including organic, paid, referral, social, and display
  name: SimilarWeb Traffic Sources API
  slug: similarweb-traffic-sources-api
- description: Webhook subscription management for data-ready notifications
  name: SimilarWeb Webhooks API
  slug: similarweb-webhooks-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/similarweb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/similarweb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/similarweb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.similarweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.similarweb.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/similarweb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/similarweb
- group: company
  title: ''
  type: Blog
  url: https://www.similarweb.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.similarweb.com/corp/daas/api/
- group: other
  title: ''
  type: X
  url: https://x.com/similarweb
- group: commercial
  title: ''
  type: Plans
  url: plans/similarweb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/similarweb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/similarweb-finops.yml
created: '2026-06-13'
description: SimilarWeb is a digital intelligence platform offering a REST API for accessing website traffic estimates, audience demographics, keyword analytics, competitive benchmarking, app intelligence data, and lead generation insights. The API provides real-time and historical data covering traffic sources, search behavior, technographics, e-commerce shopper intelligence, and firmographic company data, enabling developers to integrate market intelligence into applications, dashboards, and data pipelines.
examples:
- key_count: 2
  name: Similarweb Batch Request Example
  slug: similarweb-batch-request-example
- key_count: 2
  name: Similarweb Geography Example
  slug: similarweb-geography-example
- key_count: 2
  name: Similarweb Visits Desktop Example
  slug: similarweb-visits-desktop-example
finops:
- name: Similarweb Finops
  service_category: ''
  slug: similarweb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/similarweb.png
json_schemas:
- name: SimilarWeb Geography Response
  property_count: 2
  slug: similarweb-geography
- name: SimilarWeb Traffic and Engagement Response
  property_count: 6
  slug: similarweb-traffic-engagement
jsonld:
- class_count: 7
  name: Similarweb Context
  property_count: 49
  slug: similarweb-context
layout: provider
modified: '2026-06-13'
name: SimilarWeb
nav: Providers
network: true
overview: 'SimilarWeb publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, App Intelligence API, Credits API, and 10 more. Tagged areas include Digital Intelligence, Web Analytics, Traffic Analytics, Competitive Intelligence, and Keyword Analytics.


  The SimilarWeb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SimilarWeb''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Similarweb Plans Pricing
  plan_count: 3
  slug: similarweb-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 3
  name: Similarweb Rate Limits
  slug: similarweb-rate-limits
rules:
- name: SimilarWeb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: similarweb-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/similarweb/refs/heads/main/screenshots/similarweb-2026-06-20T193927.png
security:
- kind: authentication
  name: Similarweb Authentication
  slug: similarweb-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Similarweb Domain Security
  slug: similarweb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: similarweb
tags:
- Digital Intelligence
- Web Analytics
- Traffic Analytics
- Competitive Intelligence
- Keyword Analytics
- Audience Demographics
- App Intelligence
- Market Research
- E-commerce
- SEO
website: https://www.similarweb.com/
---
