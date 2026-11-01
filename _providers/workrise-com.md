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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/workrise-com/hosts/workrise-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/workrise-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/workrise-com/vendors/workrise-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/workrise-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rigup.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workrise.com/security/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.rigup.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workrise.com/policies/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rigup.com/solutions/vendor-management/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.rigup.com/guides/how-to-navigate-regional-expansion-in-oil-gas
- group: company
  title: ''
  type: Blog
  url: https://www.rigup.com/blog
- group: auth
  href: https://artifacts.apis.io/workrise-com/security/workrise-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workrise-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rigup.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.workrise.com/mcp
  - status: 200
    url: https://www.workrise.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Workrise, now operating as RigUp, provides a source‑to‑pay platform for the energy industry, offering workforce management, vendor onboarding, compliance, and financial tools to streamline non‑core supplier operations and project ROI for energy companies.
layout: provider
modified: '2026-10-25'
name: Workrise
nav: Providers
network: true
overview: 'Workrise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Workforce, SaaS, and Procurement.


  Workrise''s developer surface includes support, pricing, documentation, engineering blog, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Workrise Com Domain Security
  slug: workrise-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workrise-com
tags:
- Company
- Energy
- Workforce
- SaaS
- Procurement
website: https://www.rigup.com
---
