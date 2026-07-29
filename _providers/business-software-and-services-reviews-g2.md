---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The G2 API V2 provides programmatic access to G2's software reviews, buyer intent signals, competitive intelligence, and product data. Uses OAuth 2.0 for authentication. Enables integration of G2 buye
  name: G2 API V2
  slug: g2-api-v2
- description: 'G2 Buyer Intent Data provides signals about companies actively researching software categories, products, and competitors on G2. Tracks nine signal types including profile views, pricing page visits, '
  name: G2 Buyer Intent Data API
  slug: g2-buyer-intent-data
- description: The G2 MCP (Model Context Protocol) Server enables AI assistants like Claude to access G2 data. Uses OAuth for authentication via browser sign-in. Provides access to buyer intent intelligence, competi
  name: G2 MCP Server
  slug: g2-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/business-software-and-services-reviews-g2-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/business-software-and-services-reviews-g2-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/g2dotcom
- group: company
  title: ''
  type: Website
  url: https://www.g2.com/
- group: start
  title: ''
  type: Portal
  url: https://documentation.g2.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.g2.com/static/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.g2.com/docs/integrations
created: '2025-07-11'
description: G2 is the world's largest and most trusted software marketplace. More than 90 million people annually use G2 to make smarter software decisions based on authentic peer reviews. Find the right software and services based on real user reviews.
finops:
- name: Business Software And Services Reviews G2 Finops
  service_category: API
  slug: business-software-and-services-reviews-g2-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/business-software-and-services-reviews-g2.png
layout: provider
modified: '2026-04-23'
name: Business Software and Services Reviews | G2
nav: Providers
network: true
overview: 'Business Software and Services Reviews | G2 publishes 1 API on the [APIs.io](https://apis.io/) network: G2 API V2. Tagged areas include B2B, SaaS, Software Reviews, Buyer Intent, and Competitive Intelligence.


  Business Software and Services Reviews | G2''s developer surface includes developer portal, documentation, and 5 more developer resources.'
plans:
- name: Business Software And Services Reviews G2 Plans Pricing
  plan_count: 3
  slug: business-software-and-services-reviews-g2-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Business Software And Services Reviews G2 Rate Limits
  slug: business-software-and-services-reviews-g2-rate-limits
score:
  band: thin
  composite: 35.7
  delta: -1.6
  facets:
    commercial_clarity: 57.9
    contract_quality: 40.3
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/business-software-and-services-reviews-g2/refs/heads/main/screenshots/business-software-and-services-reviews-g2-2026-06-20T173819.png
security:
- kind: domain-security
  name: Business Software And Services Reviews G2 Domain Security
  slug: business-software-and-services-reviews-g2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Business Software And Services Reviews G2 Trust Center
  slug: business-software-and-services-reviews-g2-trust-center
  summary_line: SOC 2, GDPR, CSA STAR
slug: business-software-and-services-reviews-g2
tags:
- B2B
- SaaS
- Software Reviews
- Buyer Intent
- Competitive Intelligence
website: https://www.g2.com/
---
