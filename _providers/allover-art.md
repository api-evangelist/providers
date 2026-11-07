---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 31.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/allover-art/llms/allover-art-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allover-art-llms.txt
- group: other
  href: https://artifacts.apis.io/allover-art/a2a/allover-art-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/allover-art-a2a.yml
- group: agent
  href: https://artifacts.apis.io/allover-art/well-known/allover-art-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allover-art-well-known.yml
- group: other
  href: https://artifacts.apis.io/allover-art/hosts/allover-art-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allover-art-hosts.yml
- group: other
  href: https://artifacts.apis.io/allover-art/vendors/allover-art-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allover-art-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allover.art/info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allover.art/info/privacy
- group: company
  title: ''
  type: Blog
  url: https://allover.art/blog
- group: auth
  href: https://artifacts.apis.io/allover-art/security/allover-art-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allover-art-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allover.art/
coverage:
  checked: '2026-11-01'
  detail: No public developer program or API documentation is available on the site.
  evidence:
  - status: 200
    url: https://allover.art/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: All-Over Print Tees is an online retailer offering over 2,800 custom designs printed on 100% cotton apparel. Customers can choose from a wide range of themes including skulls, cats, galaxy, florals, and more, with vibrant, durable dye that won't crack or peel. The platform provides a seamless shopping experience, detailed product information, and worldwide shipping, catering to both individual consumers and bulk orders for events or merchandise.
layout: provider
modified: '2026-11-01'
name: All-Over Print Tees
nav: Providers
network: true
overview: 'All-Over Print Tees is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Print on Demand, Graphic Tees, and Worldwide Shipping.


  All-Over Print Tees'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 8.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Allover Art Domain Security
  slug: allover-art-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allover-art
tags:
- Print on Demand
- Graphic Tees
- Worldwide Shipping
website: https://allover.art/
---
