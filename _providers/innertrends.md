---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.innertrends.com
- group: company
  title: ''
  type: Blog
  url: https://www.innertrends.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.innertrends.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.innertrends.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.innertrends.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.innertrends.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.innertrends.com/security
- group: auth
  title: ''
  type: Security
  url: https://www.innertrends.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/innertrends-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/innertrends-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/innertrends-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InnerTrends
- group: commercial
  title: ''
  type: Plans
  url: plans/innertrends-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/innertrends-llms.txt
coverage:
  checked: '2026-08-13'
  detail: InnerTrends now sells data-warehouse and analysis services rather than software — its old product-analytics SaaS and its developer surface are gone (support.innertrends.com, api., app., docs. and developers.innertrends.com no longer resolve in DNS), the marketing site is WordPress with the REST API disabled, and the only public code is a deployment script that stands a data pipeline up inside the CUSTOMER'S own Google Cloud project.
  evidence:
  - status: 404
    url: https://www.innertrends.com/openapi.json
  - status: 404
    url: https://www.innertrends.com/wp-json/
  - status: 404
    url: https://www.innertrends.com/.well-known/agent-card.json
  - status: 404
    url: https://www.innertrends.com/api
  - status: 200
    url: https://www.innertrends.com/pricing
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: InnerTrends is a UK-based analytics and data consultancy that operates as a fractional data department for SaaS marketing and growth teams. Founded in 2015 and based in Norwich, England, it builds a marketing and growth data warehouse that consolidates customer and attribution data, delivers custom reports and customer-journey deep-dive analyses, and provides tracking and measurement consulting for product-led and subscription businesses. The company is ISO 27001 certified and GDPR compliant. It was surfaced as a portfolio company of 500 Global and added to the API Evangelist network for enrichment. As of this pass it does not publish a public developer API, documentation, or SDKs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/innertrends.png
layout: provider
modified: '2026-08-13'
name: Innertrends
nav: Providers
network: true
overview: 'Innertrends is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Product Analytics, Marketing, and Growth.


  Innertrends'' developer surface includes engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Innertrends Plans Pricing
  plan_count: 5
  slug: innertrends-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 24.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/innertrends/refs/heads/main/screenshots/innertrends-2026-07-25T222456.png
security:
- kind: domain-security
  name: Innertrends Domain Security
  slug: innertrends-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Innertrends Vulnerability Disclosure
  slug: innertrends-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Innertrends Trust Center
  slug: innertrends-trust-center
  summary_line: ISO 27001, GDPR
slug: innertrends
tags:
- Company
- Analytics
- Product Analytics
- Marketing
- Growth
- Data
- Software-as-a-Service
- Consulting
- Attribution
website: https://www.innertrends.com
---
