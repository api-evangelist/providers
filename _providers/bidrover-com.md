---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BidRover provides government procurement data and bidding opportunities. Documentation is at https://bidrover.com/guides but no machine‑readable contract was found.
  name: BidRover API
  slug: bidrover-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bidrover-com/plans/bidrover-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidrover-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bidrover-com/llms/bidrover-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidrover-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bidrover-com/well-known/bidrover-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bidrover-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bidrover-com/hosts/bidrover-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidrover-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidrover-com/vendors/bidrover-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidrover-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://bidrover.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidrover.com/terms
- group: start
  title: ''
  type: Sandbox
  url: https://bidrover.com/bids/topic/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidrover.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bidrover.com/pricing
- group: start
  title: ''
  type: Login
  url: https://bidrover.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://bidrover.com/guides
- group: auth
  href: https://artifacts.apis.io/bidrover-com/security/bidrover-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidrover-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidrover.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://bidrover.com/mcp
  - status: 200
    url: https://bidrover.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BidRover provides a searchable directory of public government contracts, RFPs, grants, subcontracting notices and international tenders, matching them to the services a business sells. It aggregates data from 137 official sources across the United States, 47 countries and multiple international organizations, and offers free browsing and weekly email alerts, with a paid Team plan for deeper match scoring and collaboration tools.
image: https://bidrover.com/bidrover-dark-og.png
layout: provider
modified: '2026-11-02'
name: bidrover-com
nav: Providers
network: true
overview: 'bidrover-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government Procurement, Grant Search, International Tenders, and Public Contracts.


  bidrover-com''s developer surface includes sandbox, pricing, documentation, and 11 more developer resources.'
plans:
- name: Bidrover Com Plans Pricing
  plan_count: 4
  slug: bidrover-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 18.8
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
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidrover Com Domain Security
  slug: bidrover-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bidrover-com
tags:
- Government Procurement
- Grant Search
- International Tenders
- Public Contracts
website: https://bidrover.com/
---
