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
    mcp_server: false
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/flex-com/llms/flex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flex-com-llms.txt
- group: other
  href: https://artifacts.apis.io/flex-com/hosts/flex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/flex-com/vendors/flex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flex-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://flex.com/solutions-and-services/supply-chain/supplier-information/register
- group: company
  title: ''
  type: Newsroom
  url: https://flex.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://flex.com/leadership/hooi-tan
- group: auth
  href: https://artifacts.apis.io/flex-com/security/flex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flex.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flex.com/company/policies/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Flex is a manufacturing services company and does not expose a public API.
  evidence:
  - status: 200
    url: https://flex.com/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Flex is the manufacturing partner of choice for streamlined product lifecycles. From design to end of life, its end‑to‑end services optimize efficiency. Advanced Manufacturing with End‑to‑End Solutions. Flex is honored to be ranked among Forbes’ 500 top‑performing U.S. companies and recognized as a Most Preferred Workplace for Women (2025‑2026).
image: https://flex.com/wp-content/uploads/2023/03/logo-sq.png
layout: provider
modified: '2026-10-28'
name: Flex
nav: Providers
network: true
overview: 'Flex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Hardware, Supply Chain, and Technology.


  Flex''s developer surface includes signup flow and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flex-com/flex-com-2026-11-03T132138.png
security:
- kind: domain-security
  name: Flex Com Domain Security
  slug: flex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flex-com
tags:
- Company
- Manufacturing
- Hardware
- Supply Chain
- Technology
website: https://www.flex.com
---
