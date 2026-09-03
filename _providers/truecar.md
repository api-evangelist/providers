---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truecar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truecar.com/
- group: company
  title: ''
  type: Blog
  url: https://www.truecar.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.truecar.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrueCar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truecar.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truecar.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.truecar.com/contact-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truecar-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/truecar-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/truecar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truecar-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truecar-lifecycle.yml
coverage:
  checked: '2026-08-30'
  detail: developer.truecar.com and docs.truecar.com resolve only to TrueCar's wildcard CloudFront origin and answer a bare 404, and no TrueCar host serves an OpenAPI, GraphQL SDL, WSDL, MCP manifest or any /.well-known document - TrueCar ships an end-user car-buying marketplace, and its only integration surface is bespoke dealer/DMS wiring arranged privately through dealerportal.truecar.com.
  evidence:
  - status: 404
    url: https://developer.truecar.com/
  - status: 404
    url: https://api.truecar.com/openapi.json
  - status: 404
    url: https://www.truecar.com/.well-known/api-catalog
  - status: 0
    url: https://status.truecar.com/
  reason: no-developer-program
  state: none
created: '2026-08-30'
description: TrueCar is a Santa Monica, California based online automotive marketplace that connects car buyers with a nationwide network of certified dealers, publishing upfront, transparent pricing on new and used vehicles alongside what other buyers in the same area actually paid. The company operates truecar.com, the TrueCar+ end-to-end digital retail experience, a sell-your-car / instant cash offer service, and white-label car-buying programs for affinity partners such as credit unions, insurers and large employers. Founded in 2005 by Scott Painter, TrueCar traded on NASDAQ as TRUE until January 2026, when Fair Holdings, Inc. - led by Painter, with PenFed Credit Union, Zurich North America, AutoNation and Atlantic Coast Automotive - completed a $227 million take-private acquisition. TrueCar publishes no public developer program, API reference, or machine-readable contract; its dealer, DMS and OEM integrations are arranged privately through the dealer portal under commercial agreement.
image: https://tcblogprod.wpengine.com/wp-content/themes/truecar/img/TrueCar-black.png
layout: provider
modified: '2026-08-30'
name: TrueCar
nav: Providers
network: true
overview: 'TrueCar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Marketplace, Car Buying, and Vehicle Pricing.


  TrueCar''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Truecar Plans Pricing
  plan_count: 0
  slug: truecar-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Truecar Rate Limits
  slug: truecar-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Truecar Domain Security
  slug: truecar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truecar
tags:
- Company
- Automotive
- Marketplace
- Car Buying
- Vehicle Pricing
- Dealers
- Consumer
- E-Commerce
website: https://www.truecar.com/
---
