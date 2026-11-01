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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/surepayroll/plans/surepayroll-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/surepayroll-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/surepayroll/llms/surepayroll-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/surepayroll-llms.txt
- group: agent
  href: https://artifacts.apis.io/surepayroll/well-known/surepayroll-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/surepayroll-well-known.yml
- group: other
  href: https://artifacts.apis.io/surepayroll/hosts/surepayroll-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surepayroll-hosts.yml
- group: other
  href: https://artifacts.apis.io/surepayroll/vendors/surepayroll-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surepayroll-vendors.yml
- group: auth
  href: https://artifacts.apis.io/surepayroll/security/surepayroll-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surepayroll-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.surepayroll.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.surepayroll.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.surepayroll.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.surepayroll.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.surepayroll.com/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.surepayroll.com/contact-us
created: '2026-10-27'
description: SurePayroll, a Paychex brand, provides online payroll and HR services for small businesses, households, and independent contractors. It offers payroll processing, tax filing, benefits administration, 401(k) plans, and compliance tools, aiming to simplify payroll management with affordable pricing and dedicated support.
image: https://cdn.prod.website-files.com/65a823bc36fc91ffafdc2c3e/65c20061319baa5342bd0874_Graph%20Image.png
layout: provider
modified: '2026-10-27'
name: SurePayroll
nav: Providers
network: true
overview: 'SurePayroll is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll, HR, Small Business, Paychex, and Cloud Services.


  SurePayroll''s developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Surepayroll Plans Pricing
  plan_count: 8
  slug: surepayroll-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Surepayroll Domain Security
  slug: surepayroll-domain-security
  summary_line: TLSv1.3 · DMARC
slug: surepayroll
tags:
- Payroll
- HR
- Small Business
- Paychex
- Cloud Services
website: https://www.surepayroll.com/
---
