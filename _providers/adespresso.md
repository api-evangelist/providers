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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/hootsuite/
- group: company
  title: ''
  type: Website
  url: https://adespresso.com
- group: commercial
  title: ''
  type: Pricing
  url: https://adespresso.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://adespresso.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.adespresso.com/s/
- group: start
  title: ''
  type: SignUp
  url: https://adespresso.com/join/
- group: start
  title: ''
  type: Login
  url: https://app.adespresso.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adespresso.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adespresso.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adespresso
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adespresso-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adespresso-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adespresso-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/adespresso-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adespresso-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adespresso-llms.txt
coverage:
  checked: '2026-08-12'
  detail: AdEspresso's pricing page sells "API access" as an Enterprise-tier ($259/month) entitlement, but no reference, base URL or specification for it exists on any public host — the Help Centre that would carry it, support.adespresso.com, runs on Salesforce Experience Cloud and returns 401 to an anonymous visitor.
  evidence:
  - status: 200
    url: https://adespresso.com/pricing/
  - status: 401
    url: https://support.adespresso.com/hc/en-us
  - status: 404
    url: https://app.adespresso.com/api/v1
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: AdEspresso by Hootsuite is a self-service digital advertising optimization platform for creating, managing, analyzing, and collaborating on Facebook and Instagram (and Google) ad campaigns from a single dashboard. Its tagline is "Digital Advertising Made Easy, Fast & Effective." The product lets marketers, agencies, and e-commerce teams launch split-test campaigns at scale, generate performance analytics in web/PDF/email/Excel formats, run team and client approval workflows, and learn through AdEspresso University guides, webinars, and eBooks. Originally a standalone Facebook Marketing Partner, AdEspresso was acquired by Hootsuite in 2017. It is surfaced here as a portfolio company of 500 Global. AdEspresso publishes no developer portal, API reference, OpenAPI or AsyncAPI definition, GraphQL endpoint, Postman collection, MCP server or SDK on any public host; it builds on Facebook's Marketing API rather than exposing one of its own. Its only public statement about an API is a
  single line item on the pricing page, where "API access" is listed as an Enterprise-tier ($259/month and up) entitlement with no contract, base URL or documentation attached.
image: https://adespresso.com/wp-content/uploads/2018/09/final-graphics-fb-share-img.png
layout: provider
modified: '2026-08-12'
name: AdEspresso
nav: Providers
network: true
overview: 'AdEspresso is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Facebook Ads, Instagram Ads, and Social Media Marketing.


  AdEspresso''s developer surface includes pricing, engineering blog, support, signup flow, and 12 more developer resources.'
plans:
- name: Adespresso Plans Pricing
  plan_count: 3
  slug: adespresso-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Adespresso Rate Limits
  slug: adespresso-rate-limits
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adespresso/refs/heads/main/screenshots/adespresso-2026-07-25T181626.png
security:
- kind: domain-security
  name: Adespresso Domain Security
  slug: adespresso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adespresso
tags:
- Company
- Advertising
- Facebook Ads
- Instagram Ads
- Social Media Marketing
- Ad Optimization
- Software-as-a-Service
- Marketing
website: https://adespresso.com
---
