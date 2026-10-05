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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bizaway/refs/heads/main/plans/bizaway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bizaway-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bizaway.com/en/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bizaway/refs/heads/main/hosts/bizaway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizaway-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bizaway/refs/heads/main/vendors/bizaway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bizaway-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bizaway.com/en/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.bizaway.com/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bizaway.com/en/privacy-cookie-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bizaway.com/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.bizaway.com/en/news
- group: company
  title: ''
  type: Blog
  url: https://www.bizaway.com/en/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bizaway/refs/heads/main/security/bizaway-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bizaway-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bizaway/refs/heads/main/security/bizaway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizaway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bizaway.com
coverage:
  checked: '2026-09-29'
  detail: OpenAPI spec URLs on api.bizaway.com return HTTP 403, indicating authentication is required.
  evidence:
  - status: 403
    url: https://api.bizaway.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-29'
description: BizAway is a corporate travel management platform that centralizes booking, policy enforcement, and expense control for businesses. It combines powerful technology with 24/7 human support, offering multilingual assistance, automated travel policy rules, and comprehensive visibility over travel spend across teams, entities, and currencies. Trusted by over 2,000 companies, BizAway simplifies complex travel itineraries, provides real‑time support, and ensures compliance with regional regulations, making business travel efficient and cost‑effective.
image: https://cdn.prod.website-files.com/69e5de1a79f2fdb689c1d01c/6a1a4ffd81c60eedf17641aa_OG%20Image%20(1).jpg
layout: provider
modified: '2026-09-29'
name: BizAway
nav: Providers
network: true
overview: 'BizAway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Software-as-a-Service, B2B, and Platform.


  BizAway''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Bizaway Plans Pricing
  plan_count: 2
  slug: bizaway-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bizaway Domain Security
  slug: bizaway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bizaway Trust Center
  slug: bizaway-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: bizaway
tags:
- Company
- Travel
- Software-as-a-Service
- B2B
- Platform
website: https://www.bizaway.com
---
