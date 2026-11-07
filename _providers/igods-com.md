---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/igods-com/well-known/igods-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/igods-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/igods-com/hosts/igods-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/igods-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/igods-com/vendors/igods-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/igods-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.igods.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.igods.com/legal/privacy/
- group: auth
  href: https://artifacts.apis.io/igods-com/security/igods-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/igods-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://igods.com/
- group: operate
  title: ''
  type: Support
  url: https://www.igods.com/contact-us/
coverage:
  checked: '2026-10-30'
  detail: iGods is a boutique internet marketing agency offering consulting services and does not provide a public developer program or API.
  evidence:
  - status: 200
    url: https://www.igods.com/
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: iGods Internet Marketing Inc. is a boutique internet marketing agency founded in 1997, specializing in technical SEO, Google Analytics 4 implementation, Google Tag Manager, WordPress development, and applied AI solutions. The company offers custom dashboards, SEO audits, and consulting services to enterprise clients across automotive, entertainment, financial, healthcare, and insurance sectors. With over two decades of experience, iGods helps businesses migrate to GA4, optimize site performance, and leverage data-driven insights.
image: https://www.igods.com/wp-content/uploads/cropped-igods-logo-224x107-wp.webp
layout: provider
modified: '2026-10-30'
name: igods-com
nav: Providers
network: true
overview: 'igods-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Internet-Marketing, SEO, Analytics, and WordPress.


  igods-com''s developer surface includes support and 7 more developer resources.'
plans:
- name: Igods Com Plans Pricing
  plan_count: 0
  slug: igods-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Igods Com Rate Limits
  slug: igods-com-rate-limits
scopes:
- name: Igods Com Scopes
  scope_count: 0
  slug: igods-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/igods-com/igods-com-2026-11-03T133641.png
security:
- kind: authentication
  name: Igods Com Authentication
  slug: igods-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Igods Com Domain Security
  slug: igods-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: igods-com
tags:
- Company
- Internet-Marketing
- SEO
- Analytics
- WordPress
- Consulting
website: https://igods.com/
---
