---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 8.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/virohanalife-com/plans/virohanalife-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/virohanalife-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.virohanalife.com/trust.html
- group: agent
  href: https://artifacts.apis.io/virohanalife-com/llms/virohanalife-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/virohanalife-com-llms.txt
- group: other
  href: https://artifacts.apis.io/virohanalife-com/a2a/virohanalife-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/virohanalife-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/virohanalife-com/well-known/virohanalife-com-virohanalife-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/virohanalife-com-virohanalife-security.txt
- group: auth
  href: https://artifacts.apis.io/virohanalife-com/well-known/virohanalife-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/virohanalife-com-security.txt
- group: agent
  href: https://artifacts.apis.io/virohanalife-com/well-known/virohanalife-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/virohanalife-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/virohanalife-com/hosts/virohanalife-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/virohanalife-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/virohanalife-com/vendors/virohanalife-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/virohanalife-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.virohanalife.com/trust
- group: auth
  href: https://artifacts.apis.io/virohanalife-com/security/virohanalife-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/virohanalife-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/virohanalife-com/security/virohanalife-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virohanalife-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.virohanalife.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.virohanalife.com/services.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.virohanalife.com/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://www.virohanalife.com/blog.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.virohanalife.com/engine-room.html
- group: agent
  title: ''
  type: llms
  url: https://www.virohanalife.com/llms.txt
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://www.virohanalife.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Virohanalife OÜ builds sovereign, humanity‑first AI systems that work for your life, not for platforms watching it. Their bi‑temporal memory APIs let AI agents discover, pay for, and verify work, settled in USDC over x402, with Ed25519‑signed receipts. They offer paid skills, memory storage, and a stack for AI agents to own their data and interactions, emphasizing privacy, ownership, and decentralized finance.
image: https://www.virohanalife.com/og-image.png
layout: provider
modified: '2026-10-29'
name: virohanalife-com
nav: Providers
network: true
overview: 'virohanalife-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sovereign, Memory, and Finance.


  virohanalife-com''s developer surface includes documentation, pricing, engineering blog, API reference, and 14 more developer resources.'
plans:
- name: Virohanalife Com Plans Pricing
  plan_count: 11
  slug: virohanalife-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/virohanalife-com/virohanalife-com-2026-11-03T145833.png
security:
- kind: domain-security
  name: Virohanalife Com Domain Security
  slug: virohanalife-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Virohanalife Com Vulnerability Disclosure
  slug: virohanalife-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: virohanalife-com
tags:
- Company
- Artificial Intelligence
- Sovereign
- Memory
- Finance
website: https://www.virohanalife.com/
---
