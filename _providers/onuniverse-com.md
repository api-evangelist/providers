---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/onuniverse-com/plans/onuniverse-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onuniverse-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/onuniverse-com/hosts/onuniverse-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onuniverse-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/onuniverse-com/vendors/onuniverse-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onuniverse-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.onuniverse.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onuniverse.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://support.onuniverse.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onuniverse.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onuniverse.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onuniverse.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.onuniverse.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.onuniverse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.onuniverse.com/
- group: auth
  href: https://artifacts.apis.io/onuniverse-com/security/onuniverse-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onuniverse-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onuniverse.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.onuniverse.com/mcp
  - status: 200
    url: https://onuniverse.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Universe provides a visual, no‑code website builder that lets users create custom sites, online stores, portfolios, event pages, blogs, and fan sites from any device. Users drag and drop blocks on a grid without writing HTML or CSS, and can add commerce features such as selling physical goods or digital downloads, with optional shipping label discounts. The platform includes built‑in analytics, mailing‑list tools, SEO tools, and integrations with social media advertising.
image: https://universeapp.com/_assets/9081508d-60a7-4b26-a8e6-8bcb93b06d12?w=1200&h=630&crop=top&fit=crop
layout: provider
modified: '2026-10-24'
name: Universe
nav: Providers
network: true
overview: 'Universe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Website Builder, No-code, E-commerce, Templates, and Analytics.


  Universe''s developer surface includes support, pricing, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Onuniverse Com Plans Pricing
  plan_count: 4
  slug: onuniverse-com-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Onuniverse Com Domain Security
  slug: onuniverse-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: onuniverse-com
tags:
- Website Builder
- No-code
- E-commerce
- Templates
- Analytics
- Integrations
website: https://onuniverse.com/
---
