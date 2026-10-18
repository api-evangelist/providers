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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Klover offers a cash‑advance and budgeting API accessible via its developer portal.
  name: Klover API
  slug: klover-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.joinklover.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/klover/refs/heads/main/plans/klover-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/klover-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/klover/refs/heads/main/hosts/klover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/klover-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/klover/refs/heads/main/vendors/klover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/klover-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/klover/refs/heads/main/security/klover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinklover.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.joinklover.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.joinklover.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.joinklover.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joinklover.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinklover.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinklover.com/privacy-policy
coverage:
  checked: '2026-10-12'
  detail: Developer portal https://dev.joinklover.com returns a static S3 bucket listing with no API spec.
  evidence:
  - status: 200
    url: https://dev.joinklover.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Klover provides cash advance and budgeting tools via its mobile app, offering users up to $750 in advances with zero interest or fees. The platform includes point-earning features, financial education, and a seamless sign‑up process, targeting consumers seeking flexible short‑term financing and budgeting assistance.
image: https://cdn.prod.website-files.com/5e9f09041565a624c0bf8ad3/69ceadc14c64a453538db87a_Website%20Open%20Graph-april26.png
layout: provider
modified: '2026-10-12'
name: Klover
nav: Providers
network: true
overview: 'Klover is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, CashAdvance, Budgeting, and Mobile App.


  Klover''s developer surface includes documentation, support, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Klover Plans Pricing
  plan_count: 1
  slug: klover-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Klover Domain Security
  slug: klover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klover
tags:
- Company
- Fintech
- CashAdvance
- Budgeting
- Mobile App
website: https://joinklover.com
---
