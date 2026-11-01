---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/verified-first/vendors/verified-first-vendors.yml
  title: ''
  type: Vendors
  url: vendors/verified-first-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/verified-first/plans/verified-first-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/verified-first-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://verifiedfirst.com/compliance/
- group: agent
  href: https://artifacts.apis.io/verified-first/llms/verified-first-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verified-first-llms.txt
- group: agent
  href: https://artifacts.apis.io/verified-first/well-known/verified-first-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/verified-first-well-known.yml
- group: other
  href: https://artifacts.apis.io/verified-first/hosts/verified-first-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verified-first-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.verifiedfirst.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.verifiedfirst.com/status/verifiedfirst
- group: commercial
  title: ''
  type: Pricing
  url: https://verifiedfirst.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://verifiedfirst.com/get-started/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.verifiedfirst.com
- group: company
  title: ''
  type: Blog
  url: https://verifiedfirst.com/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.verifiedfirst.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VerifiedFirst
- group: auth
  href: https://artifacts.apis.io/verified-first/security/verified-first-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/verified-first-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/verified-first/security/verified-first-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verified-first-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verifiedfirst.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.verifiedfirst.com/mcp
  - status: 403
    url: https://dev.verifiedfirst.com/mcp
  - status: 403
    url: https://drift.verifiedfirst.com/mcp
  - status: 401
    url: https://go.verifiedfirst.com/api/mcp
  - status: 200
    url: https://verifiedfirst.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Verified First provides quality pre‑employment screening, criminal background checks, verifications, and drug testing for businesses. Their platform helps companies ensure safe hiring practices by offering comprehensive background check services, including identity verification, employment history, education validation, and drug testing, all delivered through an easy‑to‑use online portal.
image: https://i0.wp.com/verifiedfirst.com/wp-content/uploads/2019/01/VF-Logo-Color-Horizontal.pngngelist/verified-first/refs/heads/main/apis.yml
layout: provider
modified: '2026-10-27'
name: Verified First
nav: Providers
network: true
overview: 'Verified First is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Background-Checks, Screening, Verification, and Employment.


  Verified First''s developer surface includes support, pricing, getting-started guide, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Verified First Plans Pricing
  plan_count: 4
  slug: verified-first-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Verified First Domain Security
  slug: verified-first-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Verified First Trust Center
  slug: verified-first-trust-center
  summary_line: SOC 2
slug: verified-first
tags:
- Company
- Background-Checks
- Screening
- Verification
- Employment
website: https://verifiedfirst.com/
---
