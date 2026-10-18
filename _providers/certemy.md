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
- description: API for Certemy workforce compliance platform, documented at the developer portal.
  name: Certemy API
  slug: certemy-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/certemy/refs/heads/main/plans/certemy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/certemy-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/certemy/refs/heads/main/conformance/certemy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/certemy-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certemy/refs/heads/main/hosts/certemy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certemy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certemy/refs/heads/main/vendors/certemy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certemy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://certemy.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://certemy.com/contact-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certemy.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://certemy.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://certemy.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://certemy.com/solutions/developer-portal/
- group: company
  title: ''
  type: Blog
  url: https://certemy.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://certemy.com/solutions/onboard/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/certemy/refs/heads/main/security/certemy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certemy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certemy.com
coverage:
  checked: '2026-10-08'
  detail: The OpenAPI endpoint returns a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://api.certemy.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Certemy provides workforce compliance software that automates license tracking, primary source verification, and employee onboarding. Their platform helps large US employers manage regulatory compliance, reduce risk, and improve staff utilization across multiple industries such as healthcare, real estate, and field services.
image: https://certemy.com/wp-content/uploads/2023/01/dashboard.jpg
layout: provider
modified: '2026-10-07'
name: Certemy
nav: Providers
network: true
overview: 'Certemy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Workforce Compliance, License Management, Credential Verification, Employee Onboarding, and HRIS Integration.


  Certemy''s developer surface includes support, pricing, engineering blog, getting-started guide, and 10 more developer resources.'
plans:
- name: Certemy Plans Pricing
  plan_count: 5
  slug: certemy-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Certemy Domain Security
  slug: certemy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: certemy
tags:
- Workforce Compliance
- License Management
- Credential Verification
- Employee Onboarding
- HRIS Integration
- Enterprise Software
website: https://certemy.com
---
