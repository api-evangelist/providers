---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Vocus next-gen APIs for Vocus Wholesale customers, providing connectivity, real-time data access and automated network solutions (quote-to-delivery, provisioning, on-demand service changes), designed '
  name: Vocus Wholesale APIs
  slug: wholesale-apis
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/vocus/conformance/vocus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vocus-conformance.yml
- group: auth
  href: https://artifacts.apis.io/vocus/well-known/vocus-internal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vocus-internal-security.txt
- group: agent
  href: https://artifacts.apis.io/vocus/well-known/vocus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vocus-well-known.yml
- group: other
  href: https://artifacts.apis.io/vocus/hosts/vocus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vocus-hosts.yml
- group: other
  href: https://artifacts.apis.io/vocus/vendors/vocus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vocus-vendors.yml
- group: auth
  href: https://artifacts.apis.io/vocus/security/vocus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vocus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vocus.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.vocus.com.au/s/
- group: docs
  title: ''
  type: Documentation
  url: https://www.vocus.com.au/wholesale/wholesale-apis
- group: operate
  title: ''
  type: Support
  url: https://support.vocus.com.au/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.vocus.com.au/help-and-support
- group: operate
  title: ''
  type: Contact
  url: https://www.vocus.com.au/help-and-support/contact-us
- group: start
  title: ''
  type: Login
  url: https://www.vocus.com.au/login
- group: company
  title: ''
  type: Newsroom
  url: https://www.vocus.com.au/news
- group: company
  title: ''
  type: About
  url: https://www.vocus.com.au/about-vocus
- group: other
  title: ''
  type: Leadership
  url: https://www.vocus.com.au/about-vocus/social-impact/team
- group: company
  title: ''
  type: Careers
  url: https://www.vocus.com.au/about-vocus/careers
- group: other
  title: ''
  type: Outages
  url: https://www.vocus.com.au/help-and-support/outages
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vocus.com.au/help-and-support/legal-contracts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vocus.com.au/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vocus-communications
created: '2026-10-22'
description: Vocus is Australia's specialist provider of fibre, network, and business solutions for businesses, government, and wholesale customers, operating an Australian and international fibre network. Its wholesale arm publishes Wholesale APIs for connectivity, real-time data access and automated network solutions, served through the Vocus Developer Portal (developer.vocus.com.au), where the full API catalogue is visible only after login and access is granted to customers with an active agreement via their Vocus Account Manager.
image: https://www.vocus.com.au/globalassets/global-media/brand/logos/logo---vocus-blue-rgb.svg
layout: provider
modified: '2026-10-22'
name: Vocus
nav: Providers
network: true
overview: 'Vocus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Fibre, Networking, and Wholesale.


  Vocus'' developer surface includes documentation, support, and 19 more developer resources.'
plans:
- name: Vocus Plans Pricing
  plan_count: 0
  slug: vocus-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Vocus Rate Limits
  slug: vocus-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 10.5
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
  previous_composite: 19.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vocus/vocus-2026-11-03T145919.png
security:
- kind: domain-security
  name: Vocus Domain Security
  slug: vocus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vocus
tags:
- Company
- Telecommunications
- Fibre
- Networking
- Wholesale
- Internet Service Provider
- Australia
website: https://www.vocus.com.au/
---
