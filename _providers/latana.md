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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.latana.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.latana.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.latana.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.latana.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.latana.com/legal-terms/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.latana.com/legal-terms/privacy-policy
- group: company
  title: ''
  type: Impressum
  url: https://www.latana.com/legal-terms/impressum
- group: company
  title: ''
  type: About
  url: https://www.latana.com/about-us
- group: other
  title: ''
  type: Team
  url: https://www.latana.com/our-team
- group: company
  title: ''
  type: Careers
  url: https://www.latana.com/careers
- group: company
  title: ''
  type: PressRoom
  url: https://www.latana.com/press-room
- group: other
  title: ''
  type: CaseStudies
  url: https://www.latana.com/case-studies
- group: auth
  title: ''
  type: DomainSecurity
  url: security/latana-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/latana-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/latana-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/latana-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/latana-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/latana-conformance.yml
coverage:
  checked: '2026-08-12'
  detail: 'Latana ships brand tracking only as an end-user product — a dashboard, a CSV export and a Slack bot the Customer Success team provisions by email — with no developer program of any kind: /developers, /api and /integrations all 404, and the sitemap has no developer page. A private Rails backend does exist at back.latana.com and mounts an API reference at /api-docs, but it is protected by HTTP Basic authentication and is never offered, priced or documented as a customer-facing API, so it is an internal application backend rather than a withheld API product.'
  evidence:
  - status: 404
    url: https://www.latana.com/developers
  - status: 401
    url: https://back.latana.com/api-docs
  - status: 404
    url: https://www.latana.com/llms.txt
  - status: 404
    url: https://www.latana.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Latana is a Berlin-based brand tracking and consumer-insights platform that measures brand awareness, brand perception, purchase consideration and ad awareness for global consumer brands. Rather than buying responses from incentivized survey panels, Latana collects non-incentivized micro-surveys through advertising placements to reach everyday consumers, then applies Bayesian modelling and machine-learning quality assurance to project the sample onto real-world populations, including small and hard-to-reach markets. The product is delivered as a dashboard covering brand health tracking, competitor benchmarking, purchase funnel tracking and brand strategy planning, sold per market per year across Essential, Pro and Custom tiers. Customers include Unilever, Amazon, IKEA, Uber, PVH and Emma Sleep. Latana is backed by Balderton Capital. As of August 2026 Latana publishes no public API, developer portal, SDKs or machine-readable API description; delivery is through the app.latana.com
  dashboard, CSV export and a Latana Slack app whose access the Customer Success team provisions on request. A private Rails backend at back.latana.com serves the dashboard over /api/v2 and /api/v3 and mounts an API reference at /api-docs behind HTTP Basic authentication, and an LLM surface at llmagent.latana.com backs the in-product data assistant, but neither is documented, marketed or offered to customers as an API product.
image: https://cdn.prod.website-files.com/6475c5eea8e20ed4cd6ee36e/647d9733ae633cba5002ee6b_Favicon.png
layout: provider
modified: '2026-08-12'
name: Latana
nav: Providers
network: true
overview: 'Latana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brand Tracking, Market Research, Consumer Insights, and Brand Awareness.


  Latana''s developer surface includes pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Latana Plans Pricing
  plan_count: 3
  slug: latana-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Latana Rate Limits
  slug: latana-rate-limits
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/latana/refs/heads/main/screenshots/latana-2026-07-25T224552.png
security:
- kind: domain-security
  name: Latana Domain Security
  slug: latana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: latana
tags:
- Company
- Brand Tracking
- Market Research
- Consumer Insights
- Brand Awareness
- Marketing Analytics
- Survey Data
- Advertising
- Software-as-a-Service
website: https://www.latana.com/
---
