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
    dynamic_client_registration: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/responsibid/plans/responsibid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/responsibid-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/responsibid/well-known/responsibid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/responsibid-well-known.yml
- group: other
  href: https://artifacts.apis.io/responsibid/hosts/responsibid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/responsibid-hosts.yml
- group: other
  href: https://artifacts.apis.io/responsibid/vendors/responsibid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/responsibid-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://responsibid.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://responsibid.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://responsibid.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://bids.responsibid.com/Login
- group: company
  title: ''
  type: Blog
  url: https://blog.responsibid.com/
- group: auth
  href: https://artifacts.apis.io/responsibid/security/responsibid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/responsibid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://responsibid.com/
coverage:
  checked: '2026-10-28'
  detail: ResponsiBid's website provides no developer portal or API documentation, indicating no public API program.
  evidence:
  - status: 200
    url: https://responsibid.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: ResponsiBid provides a modern pricing and sales software platform designed for home service businesses. Their solution streamlines the sales process, offering tools for quoting, invoicing, and customer management, helping companies improve efficiency and close deals faster. The platform emphasizes ease of use, integration capabilities, and tailored features for service‑oriented enterprises.
layout: provider
modified: '2026-10-28'
name: ResponsiBid
nav: Providers
network: true
overview: 'ResponsiBid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pricing, SalesSoftware, HomeServices, and SaaS.


  ResponsiBid''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Responsibid Plans Pricing
  plan_count: 3
  slug: responsibid-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 20.9
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
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Responsibid Domain Security
  slug: responsibid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: responsibid
tags:
- Company
- Pricing
- SalesSoftware
- HomeServices
- SaaS
website: https://responsibid.com/
---
