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
  href: https://artifacts.apis.io/closeday/plans/closeday-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/closeday-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/closeday/hosts/closeday-hosts.yml
  title: ''
  type: Hosts
  url: hosts/closeday-hosts.yml
- group: other
  href: https://artifacts.apis.io/closeday/vendors/closeday-vendors.yml
  title: ''
  type: Vendors
  url: vendors/closeday-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.closeday.com/legal/terms-of-business
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.closeday.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.closeday.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.closeday.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Closeday
- group: auth
  href: https://artifacts.apis.io/closeday/security/closeday-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/closeday-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.closeday.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.closeday.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Closeday provides end‑to‑end company closure services for UK small and mid‑sized businesses. It combines licensed insolvency practitioners with AI‑driven software to handle solvent strike‑offs, tax‑efficient MVLs and insolvent liquidations, including asset realisation, debt settlement and filings to HMRC and Companies House. Clients receive a free tailored plan and a fixed price before the service begins.
layout: provider
modified: '2026-10-24'
name: CloseDay
nav: Providers
network: true
overview: 'CloseDay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company Closure, Insolvency Services, Business Liquidation, UK Compliance, and Asset Realisation.


  CloseDay''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Closeday Plans Pricing
  plan_count: 3
  slug: closeday-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Closeday Domain Security
  slug: closeday-domain-security
  summary_line: TLSv1.3 · DMARC
slug: closeday
tags:
- Company Closure
- Insolvency Services
- Business Liquidation
- UK Compliance
- Asset Realisation
website: https://www.closeday.com/
---
