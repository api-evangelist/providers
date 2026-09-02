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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.sealedair.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sit-developer.sealedair.com/
- group: operate
  title: ''
  type: Support
  url: https://www.sealedair.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.sealedair.com/resources?tab=blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sealedair.com/company/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sealed-air-corporation
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/SealedAirCorp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sealed-air-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/sealed-air-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sealed-air-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sealed-air-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sealed-air-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: Sealed Air's production Azure API Management portal at developer.sealedair.com has never had its content published — every path returns the default 514-byte "content hasn't been published yet" placeholder — and the one portal that is published, sit-developer.sealedair.com ("We provide industry-leading APIs for Sealed Air"), shows nothing but Sign up / Sign In, with its developer-portal data API refusing anonymous listing of the API catalog.
  evidence:
  - status: 200
    url: https://sit-developer.sealedair.com/
  - status: 401
    url: https://sit-apim-manage.sealedair.com/subscriptions/000/resourceGroups/000/providers/Microsoft.ApiManagement/service/apim-sit-eus2-seeint-001/apis?api-version=2022-04-01-preview
  - status: 200
    url: https://developer.sealedair.com/apis
  - status: 401
    url: https://see-link-cloud-gateway-demo.digital.sealedair.com/V1/API
  - status: 404
    url: https://www.sealedair.com/llms.txt
  reason: partner-login
  state: gated
created: '2026-03-24'
description: Sealed Air Corporation (SEE) is a global packaging company headquartered in Charlotte, North Carolina, now privately held following its acquisition by Clayton, Dubilier & Rice. It designs and manufactures food packaging, protective packaging and automated packaging equipment under the Bubble Wrap, Cryovac, AutoBag, Liquibox and NexCel brands, and pairs them with digital services including SEE Smart Service Link for connected-equipment monitoring and prismiq for digital printing and smart packaging. Its developer surface is an Azure API Management program at developer.sealedair.com whose API catalog requires a portal account, so no public OpenAPI, reference or SDK is available to an unauthenticated integrator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sealed-air.png
layout: provider
modified: '2026-08-28'
name: Sealed Air
nav: Providers
network: true
overview: 'Sealed Air is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Packaging, Food Packaging, Protective Packaging, and Manufacturing.


  Sealed Air''s developer surface includes support, engineering blog, YouTube channel, and 9 more developer resources.'
plans:
- name: Sealed Air Plans Pricing
  plan_count: 0
  slug: sealed-air-plans-pricing
press:
- date: '2026-05-25'
  title: Sealed Air Announces Expiration of "Go-Shop" Period
  url: https://www.prnewswire.com/news-releases/sealed-air-announces-expiration-of-go-shop-period-302644234.html
- date: '2026-05-25'
  title: 'Research Update: Sealed Air Corp. Placed On Credi'
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3481462
- date: '2026-05-25'
  title: Sealed Air Announces Completion of Acquisition by CD&R
  url: https://www.prnewswire.com/news-releases/sealed-air-announces-completion-of-acquisition-by-cdr-302738274.html
- date: '2026-05-25'
  title: Sealed Air Acquires Assets from Intellibot Robotics
  url: https://ir.sealedair.com/node/11006/pdf
- date: '2026-05-25'
  title: Are You Ready for Intelligent Automation Solutions?
  url: https://www.sealedair.com/uk/resources/blog/automated-ecommerce-fulfillment-services-solution
random_paper: 17
rate_limits:
- limit_count: 0
  name: Sealed Air Rate Limits
  slug: sealed-air-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sealed Air Domain Security
  slug: sealed-air-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sealed-air
tags:
- Fortune 500
- Packaging
- Food Packaging
- Protective Packaging
- Manufacturing
- Industrial Automation
- Materials
- Smart Packaging
website: https://www.sealedair.com
---
