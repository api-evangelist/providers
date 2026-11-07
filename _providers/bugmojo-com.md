---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: BugMojo provides an AI-native bug tracking platform with an MCP server for AI agents.
  name: BugMojo API
  slug: bugmojo-api
- description: 'BugMojo API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BugMojo API
  slug: bugmojo-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/bugmojo-com/plans/bugmojo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bugmojo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bugmojo-com/rules/bugmojo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bugmojo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bugmojo-com/vocabulary/bugmojo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bugmojo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bugmojo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/bugmojo-com/cli/bugmojo-com-cli.yml
  title: ''
  type: CLI
  url: cli/bugmojo-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/bugmojo-com/changelog/bugmojo-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bugmojo-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bugmojo.com/security
- group: auth
  href: https://artifacts.apis.io/bugmojo-com/authentication/bugmojo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bugmojo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bugmojo-com/conformance/bugmojo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bugmojo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bugmojo-com/llms/bugmojo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bugmojo-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/bugmojo-com/well-known/bugmojo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bugmojo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/bugmojo-com/well-known/bugmojo-com-bugmojo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bugmojo-com-bugmojo-security.txt
- group: agent
  href: https://artifacts.apis.io/bugmojo-com/well-known/bugmojo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bugmojo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bugmojo-com/hosts/bugmojo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bugmojo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bugmojo-com/vendors/bugmojo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bugmojo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bugmojo.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.bugmojo.com/help
- group: auth
  title: ''
  type: Security
  url: https://www.bugmojo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bugmojo.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bugmojo.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.bugmojo.com/blog/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bugmojo.com/solutions/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bugmojo.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.bugmojo.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bugmojo.com/help/getting-started/what-is-bugmojo
- group: auth
  href: https://artifacts.apis.io/bugmojo-com/security/bugmojo-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bugmojo-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bugmojo-com/security/bugmojo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bugmojo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bugmojo-com/security/bugmojo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugmojo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bugmojo.com/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documented hosts.
  evidence:
  - status: 200
    url: https://www.bugmojo.com/solutions/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BugMojo provides an AI-native bug tracking platform that captures bugs with a single click via a browser extension, offers session replay, console and network logs, and generates failing tests for developers. It integrates with MCP for coding agents, aiming to make bug reports human‑readable and machine‑readable, accelerating AI‑assisted debugging and code fixing.
image: https://www.bugmojo.com/og
layout: provider
modified: '2026-11-03'
name: BugMojo
nav: Providers
network: true
overview: 'BugMojo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bug Tracking, Artificial Intelligence, Developer Tools, Session Replay, and Open Source.


  The BugMojo catalog on APIs.io includes 1 Spectral governance ruleset.


  BugMojo''s developer surface includes CLI, changelog, authentication, support, pricing, documentation, engineering blog, and 22 more developer resources.'
plans:
- name: Bugmojo Com Plans Pricing
  plan_count: 3
  slug: bugmojo-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: BugMojo API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: bugmojo-com-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 44.5
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bugmojo Com Authentication
  slug: bugmojo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bugmojo Com Domain Security
  slug: bugmojo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Bugmojo Com Vulnerability Disclosure
  slug: bugmojo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bugmojo Com Trust Center
  slug: bugmojo-com-trust-center
  summary_line: SOC 2
slug: bugmojo-com
tags:
- Bug Tracking
- Artificial Intelligence
- Developer Tools
- Session Replay
- Open Source
website: https://www.bugmojo.com/
---
