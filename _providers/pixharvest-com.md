---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/pixharvest-com/plans/pixharvest-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pixharvest-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/pixharvest-com/hosts/pixharvest-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pixharvest-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pixharvest-com/vendors/pixharvest-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pixharvest-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/pixharvest-com/security/pixharvest-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixharvest-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pixharvest.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://pixharvest.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://pixharvest.com/
- group: company
  title: ''
  type: Blog
  url: https://pixharvest.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pixharvest.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pixharvest.com/
created: '2026-10-29'
description: PixHarvest provides a WhatsApp‑based quoting solution for printing shops in Singapore and Malaysia. By loading a price table once, the service automatically generates finished quotations for every WhatsApp enquiry within minutes, streamlining order handling and reducing manual effort. The platform targets small‑to‑medium print businesses seeking fast, automated price responses via a popular messaging channel.
image: data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%2315140f'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia' fill='%23f7f5f0' text-anchor='middle'%3EP%3C/text%3E%3C/svg%3E
layout: provider
modified: '2026-10-29'
name: pixharvest-com
nav: Providers
network: true
overview: 'pixharvest-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Printing, WhatsApp, Quoting, and Software-as-a-Service.


  pixharvest-com''s developer surface includes pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Pixharvest Com Plans Pricing
  plan_count: 3
  slug: pixharvest-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Pixharvest Com Rate Limits
  slug: pixharvest-com-rate-limits
scopes:
- name: Pixharvest Com Scopes
  scope_count: 0
  slug: pixharvest-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - malaysia
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pixharvest-com/pixharvest-com-2026-11-03T141247.png
security:
- kind: authentication
  name: Pixharvest Com Authentication
  slug: pixharvest-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pixharvest Com Domain Security
  slug: pixharvest-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pixharvest-com
tags:
- Company
- Printing
- WhatsApp
- Quoting
- Software-as-a-Service
- Singapore
- Malaysia
website: https://pixharvest.com/
---
