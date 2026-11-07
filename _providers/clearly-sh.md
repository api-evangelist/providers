---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Clearly's AI workspace platform, documented at https://www.clearly.sh/docs
  name: Clearly API
  slug: clearly-api
- baseURL: https://clearly.sh
  baseurl_source: declared
  description: 'Clearly API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Clearly API
  slug: clearly-sh-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/clearly-sh/plans/clearly-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearly-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clearly-sh/rules/clearly-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/clearly-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/clearly-sh/vocabulary/clearly-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearly-sh-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/clearly-sh/cli/clearly-sh-cli.yml
  title: ''
  type: CLI
  url: cli/clearly-sh-cli.yml
- group: auth
  href: https://artifacts.apis.io/clearly-sh/authentication/clearly-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearly-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/clearly-sh/conformance/clearly-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearly-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clearly-sh/llms/clearly-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearly-sh-llms.txt
- group: auth
  href: https://artifacts.apis.io/clearly-sh/well-known/clearly-sh-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearly-sh-www-security.txt
- group: auth
  href: https://artifacts.apis.io/clearly-sh/well-known/clearly-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearly-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/clearly-sh/well-known/clearly-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearly-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearly-sh/hosts/clearly-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearly-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearly-sh/vendors/clearly-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearly-sh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearly.sh/terms
- group: operate
  title: ''
  type: Support
  url: https://www.clearly.sh/help
- group: operate
  title: ''
  type: StatusPage
  url: https://www.clearly.sh/status
- group: auth
  title: ''
  type: Security
  url: https://www.clearly.sh/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearly.sh/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clearly.sh/pricing
- group: start
  title: ''
  type: Login
  url: https://www.clearly.sh/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.clearly.sh/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.clearly.sh/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.clearly.sh/blog
- group: auth
  href: https://artifacts.apis.io/clearly-sh/security/clearly-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearly-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clearly-sh/security/clearly-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearly-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearly.sh/
coverage:
  checked: '2026-11-04'
  detail: Documentation is a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.clearly.sh/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Clearly provides a collaborative AI workspace where agents like Claude, ChatGPT, and Cursor get dedicated spaces for documents, tickets, and designs, separate from personal files and accounts. The platform offers free usage for up to three agents, focusing on productivity and secure AI memory across conversations.
image: https://www.clearly.sh/landing/workspace/og.png
layout: provider
modified: '2026-11-03'
name: Clearly
nav: Providers
network: true
overview: 'Clearly is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Workspace, and Design Tools.


  The Clearly catalog on APIs.io includes 1 Spectral governance ruleset.


  Clearly''s developer surface includes CLI, authentication, support, pricing, documentation, changelog, engineering blog, and 18 more developer resources.'
plans:
- name: Clearly Sh Plans Pricing
  plan_count: 2
  slug: clearly-sh-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Clearly API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: clearly-sh-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.8
    catalog_earned_first_party: 8.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 11.7
    developer_ergonomics: 27.4
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clearly Sh Authentication
  slug: clearly-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Clearly Sh Domain Security
  slug: clearly-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clearly Sh Vulnerability Disclosure
  slug: clearly-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clearly-sh
tags:
- AI Agents
- Workspace
- Design Tools
website: https://clearly.sh/
---
