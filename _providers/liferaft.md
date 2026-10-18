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
- description: Liferaft provides a health benefits platform; documentation is available at the Guides page.
  name: Liferaft API
  slug: liferaft-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/liferaft/refs/heads/main/plans/liferaft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/liferaft-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/liferaft/refs/heads/main/hosts/liferaft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/liferaft-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/liferaft/refs/heads/main/vendors/liferaft-vendors.yml
  title: ''
  type: Vendors
  url: vendors/liferaft-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.liferaft.co/user/login/
- group: docs
  title: ''
  type: Documentation
  url: https://blog.liferaft.co/guides
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/liferaft/refs/heads/main/security/liferaft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liferaft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liferaft.co/
- group: company
  title: ''
  type: Blog
  url: https://blog.liferaft.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.liferaft.co/company/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liferaft.co/company/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liferaft.co/company/privacy/
coverage:
  checked: '2026-10-12'
  detail: Guides page renders via JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://blog.liferaft.co/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Liferaft provides flexible and affordable health benefits for individuals and employers, supplementing existing coverage with affordable options. Their platform offers easy enrollment, comprehensive plan options, and tools to manage health benefits, aiming to protect users when they need it most. Liferaft aims to simplify health benefit administration and improve access to care.
image: https://www.liferaft.co/static/img/logos/liferaft_horizontallogo_pink.svg
layout: provider
modified: '2026-10-12'
name: Liferaft
nav: Providers
network: true
overview: 'Liferaft is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Benefits, Insurance, and Software-as-a-Service.


  Liferaft''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Liferaft Plans Pricing
  plan_count: 4
  slug: liferaft-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Liferaft Domain Security
  slug: liferaft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liferaft
tags:
- Company
- Health
- Benefits
- Insurance
- Software-as-a-Service
website: https://www.liferaft.co/
---
