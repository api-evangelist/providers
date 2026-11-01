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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/meecrogate/plans/meecrogate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meecrogate-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/meecrogate/hosts/meecrogate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meecrogate-hosts.yml
- group: other
  href: https://artifacts.apis.io/meecrogate/vendors/meecrogate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meecrogate-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meecrogate
- group: auth
  href: https://artifacts.apis.io/meecrogate/security/meecrogate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meecrogate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meecrogate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meecrogate.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meecrogate.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meecrogate.com/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meecrogate.com/politique-confidentialite
coverage:
  checked: '2026-10-18'
  detail: The documentation site loads content via JavaScript, providing no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.meecrogate.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Meecrogate is a French‑based sovereign cloud API platform offering low‑code, modular, composable solutions for API exposure, security, orchestration and governance. The platform provides an API gateway, identity server, orchestrator and process executor, all configurable without code, targeting European data‑privacy standards and offering a single‑price annual edition covering all components.
image: https://www.meecrogate.com/og-image.png
layout: provider
modified: '2026-10-18'
name: Meecrogate
nav: Providers
network: true
overview: 'Meecrogate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Platform, Low-Code, Sovereign Cloud, and European.


  Meecrogate''s developer surface includes documentation, pricing, and 8 more developer resources.'
plans:
- name: Meecrogate Plans Pricing
  plan_count: 1
  slug: meecrogate-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 17.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Meecrogate Domain Security
  slug: meecrogate-domain-security
  summary_line: TLSv1.3
slug: meecrogate
tags:
- Company
- API Platform
- Low-Code
- Sovereign Cloud
- European
website: https://meecrogate.com/
---
