---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides AI detection and response for coding agents, as documented in the public markdown docs.
  name: Golem API
  slug: golem-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/golem-team/llms/golem-team-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/golem-team-llms.txt
- group: agent
  href: https://artifacts.apis.io/golem-team/well-known/golem-team-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/golem-team-well-known.yml
- group: other
  href: https://artifacts.apis.io/golem-team/hosts/golem-team-hosts.yml
  title: ''
  type: Hosts
  url: hosts/golem-team-hosts.yml
- group: other
  href: https://artifacts.apis.io/golem-team/vendors/golem-team-vendors.yml
  title: ''
  type: Vendors
  url: vendors/golem-team-vendors.yml
- group: auth
  href: https://artifacts.apis.io/golem-team/security/golem-team-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/golem-team-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://golem.team/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.golem.team/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.golem.team/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.golem.team/install
- group: operate
  title: ''
  type: Support
  url: https://golem.team/support
- group: company
  title: ''
  type: Blog
  url: https://golem.team/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://golem.team/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://golem.team/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://golem.team/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://golem.team/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation is provided as markdown but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract was found.
  evidence:
  - status: 200
    url: https://docs.golem.team/index.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: 'Golem (golem.team), AI Detection and Response for coding agents. Golem sits in the path of every tool call: it detects hijacked agents, blocks or gates the dangerous calls before they run, contains a compromised machine, and signs the evidence so the record can’t be edited afterward. Free public preview.'
image: https://golem.team/og.png
layout: provider
modified: '2026-10-30'
name: golem-team
nav: Providers
network: true
overview: 'golem-team is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Agents, and Detection.


  golem-team''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 16
scopes:
- name: Golem Team Scopes
  scope_count: 0
  slug: golem-team-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/golem-team/golem-team-2026-11-03T132923.png
security:
- kind: authentication
  name: Golem Team Authentication
  slug: golem-team-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Golem Team Domain Security
  slug: golem-team-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: golem-team
tags:
- Company
- Artificial Intelligence
- Security
- Agents
- Detection
- Response
website: https://golem.team/
---
