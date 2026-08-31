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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ebbo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ebbo.com
- group: company
  title: ''
  type: Blog
  url: https://www.ebbo.com/insights/
- group: operate
  title: ''
  type: Support
  url: https://www.ebbo.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ebbo.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ebbo.com/terms-of-use/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ebbo.com/feed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ebbo-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Ebbo's Integration Management page markets "an advanced API framework" and lists "API documentation", "Permission-based access" and "Permission Throttling" as API resources, but links none of them — api., docs. and developer.ebbo.com do not resolve, every spec path 404s on www.ebbo.com, and the only route to the reference is the "Get in touch" contact form.
  evidence:
  - status: 200
    url: https://www.ebbo.com/solutions/technology/integration/
  - status: 404
    url: https://www.ebbo.com/openapi.json
  - status: 404
    url: https://www.ebbo.com/.well-known/api-catalog
  - status: 404
    url: https://www.ebbo.com/pricing/
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Ebbo is an enterprise loyalty and promotional marketing technology company that helps brands build lasting customer relationships and grow revenue through engagement. Its platform powers paid, tiered, and engagement-based loyalty programs alongside promotional overlays such as sweepstakes, instant wins, contests, and user-generated-content campaigns, supported by real-time performance dashboards, purchase validation, and advanced privacy and security controls. Ebbo pairs this technology with full-service program design, creative, program management, data analytics, rewards sourcing, and customer service for brands including T-Mobile, Lowe's, and FULLBEAUTY Brands. Backed by Norwest Venture Partners.
image: https://www.ebbo.com/wp-content/themes/_ws/logo.svg
layout: provider
modified: '2026-08-13'
name: Ebbo
nav: Providers
network: true
overview: 'Ebbo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loyalty, Marketing Technology, Promotions, and Customer Engagement.


  Ebbo''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Ebbo Plans Pricing
  plan_count: 0
  slug: ebbo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ebbo Rate Limits
  slug: ebbo-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ebbo/refs/heads/main/screenshots/ebbo-2026-07-25T212725.png
security:
- kind: domain-security
  name: Ebbo Domain Security
  slug: ebbo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ebbo
tags:
- Company
- Loyalty
- Marketing Technology
- Promotions
- Customer Engagement
- Rewards
- Sweepstakes
website: https://ebbo.com
---
