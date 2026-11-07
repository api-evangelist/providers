---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/mable-com-au/plans/mable-com-au-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mable-com-au-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/mable-com-au/hosts/mable-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mable-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/mable-com-au/vendors/mable-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mable-com-au-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://mable.com.au/discover/support-at-home/registered-supporter/
- group: company
  title: ''
  type: Website
  url: https://mable.com.au/
- group: auth
  href: https://artifacts.apis.io/mable-com-au/security/mable-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mable-com-au-domain-security.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://mable.com.au/help_centre/
- group: operate
  title: ''
  type: FAQ
  url: https://mable.com.au/faqs/
- group: operate
  title: ''
  type: Support
  url: https://mable.com.au/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://mable.com.au/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://mable.com.au/newsroom/
- group: commercial
  title: ''
  type: Legal
  url: https://mable.com.au/legal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mable.com.au/legal/terms/site-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mable.com.au/legal/policies/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://mable.com.au/about-us/leadership-team/
- group: company
  title: ''
  type: Careers
  url: https://mable.com.au/about-us/careers-at-mable/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mableaustralia/
created: '2026-10-22'
description: Mable is an Australian online platform (mable.com.au) that connects people seeking disability (NDIS) and aged care support, including Support at Home and self-funded or out-of-hospital care, with verified independent support workers in their local community, letting clients search, book and build their own support team. Support workers, NDIS support coordinators and aged care managers also use the platform, which handles payments, support notes and safeguards. No public developer API or documentation was found on its site.
image: https://res.cloudinary.com/Mable-EU/image/upload/c_crop,h_880,w_1173,x_103,y_0/c_scale,h_880,w_1173/aged-care-clay-workshop-1280x854-1_1_ouncob
layout: provider
modified: '2026-10-22'
name: Mable
nav: Providers
network: true
overview: 'Mable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aged Care, Disability Support, NDIS, and Healthcare.


  Mable''s developer surface includes signup flow, FAQ, support, pricing, legal docs, and 12 more developer resources.'
plans:
- name: Mable Com Au Plans Pricing
  plan_count: 3
  slug: mable-com-au-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Mable Com Au Rate Limits
  slug: mable-com-au-rate-limits
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mable-com-au/mable-com-au-2026-11-03T135203.png
security:
- kind: domain-security
  name: Mable Com Au Domain Security
  slug: mable-com-au-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mable-com-au
tags:
- Company
- Aged Care
- Disability Support
- NDIS
- Healthcare
- Marketplace
- Australia
- Care Workers
website: https://mable.com.au/
---
