---
agent_readiness:
  band: agent-aware
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
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/donordock/plans/donordock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/donordock-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/donordock/llms/donordock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/donordock-llms.txt
- group: auth
  href: https://artifacts.apis.io/donordock/well-known/donordock-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/donordock-status-security.txt
- group: agent
  href: https://artifacts.apis.io/donordock/well-known/donordock-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/donordock-well-known.yml
- group: other
  href: https://artifacts.apis.io/donordock/hosts/donordock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donordock-hosts.yml
- group: other
  href: https://artifacts.apis.io/donordock/vendors/donordock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donordock-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.donordock.com/terms-conditions-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.donordock.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.donordock.com/integrations/signupgenius
- group: commercial
  title: ''
  type: Pricing
  url: https://www.donordock.com/pricing
- group: other
  title: ''
  type: Leadership
  url: https://www.donordock.com/team/val-k
- group: auth
  href: https://artifacts.apis.io/donordock/security/donordock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donordock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donordock.com/
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://www.donordock.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: DonorDock provides a donor development platform for growing nonprofits, offering tools for donor management, online giving, fundraising, and project management. The SaaS solution integrates with thousands of apps and supports AI-driven fundraising, aiming to help nonprofit teams build relationships and increase donations.
image: https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/6532889f2379aa018d3524f7_a126195a26fa8bdb1cdca640b84f6ff1_Website%20Meta%20Description%20Image.webp
layout: provider
modified: '2026-10-27'
name: DonorDock
nav: Providers
network: true
overview: 'DonorDock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Nonprofit, SaaS, Fundraising, Donor Management, and AI.


  DonorDock''s developer surface includes signup flow, pricing, and 11 more developer resources.'
plans:
- name: Donordock Plans Pricing
  plan_count: 1
  slug: donordock-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Donordock Domain Security
  slug: donordock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donordock
tags:
- Nonprofit
- SaaS
- Fundraising
- Donor Management
- AI
website: https://donordock.com/
---
