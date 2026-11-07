---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: true
  try_now: true
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Event planning API documented at https://doodates.com/docs
  name: DooDates API
  slug: doodates-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/doodates-com/plans/doodates-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doodates-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://doodates.com/privacy
- group: design
  href: https://artifacts.apis.io/doodates-com/conformance/doodates-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doodates-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doodates-com/llms/doodates-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doodates-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/doodates-com/mcp/doodates-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doodates-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/doodates-com/well-known/doodates-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doodates-com-security.txt
- group: agent
  href: https://artifacts.apis.io/doodates-com/well-known/doodates-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doodates-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doodates-com/hosts/doodates-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doodates-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doodates-com/vendors/doodates-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doodates-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/doodates-com/security/doodates-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doodates-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doodates-com/security/doodates-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doodates-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doodates.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doodates.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://doodates.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doodates.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doodates.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://doodates.com/support
- group: operate
  title: ''
  type: Roadmap
  url: https://doodates.com/roadmap
coverage:
  checked: '2026-11-05'
  detail: Docs site returns a JavaScript‑rendered React app, preventing machine‑readable specs.
  evidence:
  - status: 200
    url: https://doodates.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DooDates is an event planning tool that helps groups find a suitable date through simple polls. Users can create polls without signing up, invite participants via a link, and vote on proposed dates. The platform supports AI‑assisted date suggestions, recurring events, and export options such as PDF, JSON, and Markdown. It offers a free tier with unlimited manual polls and paid plans for AI conversations and advanced features.
image: https://doodates.com/logo-doodates.png?v=3
layout: provider
mcp_servers:
- description: Remote MCP server at doodates.com.
  name: DooDates MCP Server
  slug: doodates-com-mcp-yml
modified: '2026-11-05'
name: DooDates
nav: Providers
network: true
overview: 'DooDates is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Scheduling, Polls, Event Planning, Collaboration, and Free Tier.


  DooDates'' developer surface includes documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Doodates Com Plans Pricing
  plan_count: 3
  slug: doodates-com-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doodates Com Domain Security
  slug: doodates-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Doodates Com Vulnerability Disclosure
  slug: doodates-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: doodates-com
tags:
- Scheduling
- Polls
- Event Planning
- Collaboration
- Free Tier
website: https://doodates.com/
---
