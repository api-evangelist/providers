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
  scored_at: '2026-09-02'
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
overview: 'Property Capsule publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, PropTech, Commercial Real Estate, and Retail.


  Property Capsule''s developer surface includes documentation, support, changelog, signup flow, and 9 more developer resources.'
plans:
- name: Property Capsule Plans Pricing
  plan_count: 0
  slug: property-capsule-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Property Capsule Rate Limits
  slug: property-capsule-rate-limits
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 14.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/property-capsule/refs/heads/main/screenshots/property-capsule-2026-09-02T152153.png
security:
- kind: domain-security
  name: Property Capsule Domain Security
  slug: property-capsule-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: property-capsule
tags:
- Company
- Real-Estate
- PropTech
- Commercial Real Estate
- Retail
- Marketing Automation
- Leasing
website: https://propertycapsule.com/
---
