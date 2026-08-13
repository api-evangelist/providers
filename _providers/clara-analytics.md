---
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clara-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claraanalytics.com/
- group: company
  title: ''
  type: About
  url: https://claraanalytics.com/about/
- group: other
  title: ''
  type: Products
  url: https://claraanalytics.com/platform-products/
- group: company
  title: ''
  type: Blog
  url: https://claraanalytics.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://claraanalytics.com/feed/
- group: company
  title: ''
  type: News
  url: https://claraanalytics.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://claraanalytics.com/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://claraanalytics.com/case-studies/
- group: operate
  title: ''
  type: Support
  url: https://claraanalytics.com/contact-us/
- group: start
  title: ''
  type: Demo
  url: https://claraanalytics.com/demo/
- group: company
  title: ''
  type: Partners
  url: https://claraanalytics.com/partnerships/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.guidewire.com/product/clara-analytics-claratyai-claimcenter/01t3n00000GfLKHAA3
- group: start
  title: ''
  type: CustomerPortal
  url: https://portal.claraanalytics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claraanalytics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claraanalytics.com/privacy-policy/
- group: design
  title: ''
  type: Conformance
  url: conformance/clara-analytics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/clara-analytics-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clara-analytics-llms.txt
coverage:
  checked: '2026-08-09'
  detail: CLARA markets "pre-built APIs for simple integration" on six product pages but publishes no developer site of its own — docs.claraanalytics.com is a dangling CNAME to an unclaimed Document360 project that answers HTTP 200 with "Sorry! This project does not exist." for every path, api.claraanalytics.com answers nginx 404 for every unauthenticated path, and the only integration surface CLARA actually publishes is the Built-by-Guidewire CLARAty.ai listing inside the Guidewire Marketplace.
  evidence:
  - status: 200
    url: https://docs.claraanalytics.com/
  - status: 404
    url: https://api.claraanalytics.com/openapi.json
  - status: 404
    url: https://claraanalytics.com/llms.txt
  - status: 200
    url: https://marketplace.guidewire.com/product/clara-analytics-claratyai-claimcenter/01t3n00000GfLKHAA3
  reason: marketplace-only
  state: gated
created: '2026-08-09'
description: CLARA Analytics is an AI-as-a-service provider for casualty insurance claims, serving carriers, MGAs/MGUs, reinsurers, third-party administrators and self-insured organizations. Its CLARAty.ai platform applies document intelligence, natural language processing, image recognition and predictive models to medical notes, legal demand packages, bills and other claim documents across workers' compensation, auto and general liability, with products for triage, fraud detection, litigation risk, treatment and provider selection, Medicare Secondary Payer compliance, and industry benchmarking. CLARA markets pre-built APIs for integration with RMIS and core claims systems and ships a Built-by-Guidewire integration for ClaimCenter through the Guidewire Marketplace, but publishes no public developer portal, API reference, or machine-readable specification.
image: https://claraanalytics.com/wp-content/uploads/2023/02/cropped-clara-favicon-192x192.png
layout: provider
modified: '2026-08-09'
name: CLARA Analytics
nav: Providers
network: true
overview: 'CLARA Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Claims, and Artificial Intelligence.


  CLARA Analytics'' developer surface includes engineering blog, product news, support, and 16 more developer resources.'
random_paper: 88
score:
  band: emerging
  composite: 17.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Clara Analytics Domain Security
  slug: clara-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clara-analytics
tags:
- Company
- Insurance
- Insurtech
- Claims
- Artificial Intelligence
- Machine Learning
- Document Intelligence
- Analytics
- Fraud Detection
- Workers Compensation
- Casualty
website: https://claraanalytics.com/
---
