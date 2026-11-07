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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/autoprintstudio-com/llms/autoprintstudio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoprintstudio-com-llms.txt
- group: other
  href: https://artifacts.apis.io/autoprintstudio-com/hosts/autoprintstudio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoprintstudio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoprintstudio-com/vendors/autoprintstudio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoprintstudio-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://autoprintstudio.com/sign-in
- group: other
  title: ''
  type: Leadership
  url: https://autoprintstudio.com/team
- group: auth
  href: https://artifacts.apis.io/autoprintstudio-com/security/autoprintstudio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoprintstudio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoprintstudio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://autoprintstudio.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://autoprintstudio.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://autoprintstudio.com/guides
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoprintstudio.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoprintstudio.com/legal/terms
coverage:
  checked: '2026-11-02'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://autoprintstudio.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AutoPrint Studio is an on-demand custom printing service that turns user‑provided text or image prompts into physical products such as posters, canvas prints, mugs, stickers, and apparel. Users describe what they want in a sentence, choose a product type, and the studio creates and ships the item, typically within a week, with a 30‑day reprint or refund guarantee.
image: https://autoprintstudio.com/og-04b.jpg
layout: provider
modified: '2026-11-02'
name: AutoPrint Studio
nav: Providers
network: true
overview: 'AutoPrint Studio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Printing, On-Demand, Custom, E-Commerce, and Art.


  AutoPrint Studio''s developer surface includes documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoprintstudio Com Domain Security
  slug: autoprintstudio-com-domain-security
  summary_line: TLSv1.3
slug: autoprintstudio-com
tags:
- Printing
- On-Demand
- Custom
- E-Commerce
- Art
website: https://autoprintstudio.com/
---
