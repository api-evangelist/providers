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
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Property Capsule''s Developer API, announced live on 2020-06-18 in the company''s public release notes: "Our robust API is now live! Now your developers can access PropertyCapsule data outside of our pl'
  name: Property Capsule Developer API
  slug: property-capsule-developer-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/property-capsule-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://propertycapsule.com/
- group: docs
  title: ''
  type: Documentation
  url: https://propertycapsule.com/details
- group: operate
  title: ''
  type: Support
  url: http://support.propertycapsule.com/
- group: operate
  title: ''
  type: Contact
  url: https://propertycapsule.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://propertycapsule.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/property-capsule-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/property-capsule-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/property-capsule-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/property-capsule-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/property-capsule-llms.txt
- group: start
  title: ''
  type: Login
  url: https://admin.propertycapsule.com
- group: start
  title: ''
  type: SignUp
  url: https://maps.propertycapsule.com/map/sign-up
coverage:
  checked: '2026-08-13'
  detail: Property Capsule announced a Developer API live on 2020-06-18 and told developers to "contact our support team" for it, and api.propertycapsule.com is up and serving two path-versioned majors — but every path on that host answers with the plain-text body "You must authenticate.", and the 62-article public help center has no developer section at all, so the reference only exists for signed customers.
  evidence:
  - status: 200
    url: https://api.propertycapsule.com/api/v1/
  - status: 200
    url: https://api.propertycapsule.com/api
  - status: 200
    url: https://propertycapsule.zendesk.com/hc/en-us/articles/360050724134-Release-Notes-June-18th-2020
  - status: 200
    url: https://propertycapsule.com/openapi.json
  - status: 301
    url: https://propertycapsule.com/pricing
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Property Capsule (PropertyCapsule) is a retail and commercial real estate marketing automation and prospecting platform for landlords and brokers. It centralizes property, tenant, and availability data in one place and automatically publishes it as flyers, tourbooks, interactive site plans, aerials, demographics, and competition maps across web and iPad leasing apps. Founded around 2014, the company was acquired by VTS in October 2019 and its capabilities were folded into the VTS Market product. This profile was surfaced as a portfolio company of trinity-ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/property-capsule.png
layout: provider
modified: '2026-08-13'
name: Property Capsule
nav: Providers
network: true
overview: 'Property Capsule publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, PropTech, Commercial Real Estate, and Retail.


  Property Capsule''s developer surface includes documentation, support, changelog, signup flow, and 9 more developer resources.'
plans:
- name: Property Capsule Plans Pricing
  plan_count: 0
  slug: property-capsule-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Property Capsule Rate Limits
  slug: property-capsule-rate-limits
score:
  band: emerging
  composite: 16.3
  delta: 0.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 16.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Property Capsule Domain Security
  slug: property-capsule-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: property-capsule
tags:
- Company
- Real Estate
- PropTech
- Commercial Real Estate
- Retail
- Marketing Automation
- Leasing
website: https://propertycapsule.com/
---
