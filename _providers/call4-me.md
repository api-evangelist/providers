---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Call4 Me Agentic Access
  operation_count: 22
  slug: call4-me-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 1
apis:
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Balance API from call4me — 1 operation(s) for balance.
  name: call4me Balance API
  slug: call4-me-balance-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Call4me API API from call4me — 1 operation(s) for call4me api.
  name: call4me Call4me API
  slug: call4-me-call4me-api-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Calls API from call4me — 6 operation(s) for calls.
  name: call4me Calls API
  slug: call4-me-calls-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Numbers API from call4me — 5 operation(s) for numbers.
  name: call4me Numbers API
  slug: call4-me-numbers-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Profile API from call4me — 1 operation(s) for profile.
  name: call4me Profile API
  slug: call4-me-profile-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Requirements API from call4me — 2 operation(s) for requirements.
  name: call4me Requirements API
  slug: call4-me-requirements-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The Scheduled Calls API from call4me — 2 operation(s) for scheduled calls.
  name: call4me Scheduled Calls API
  slug: call4-me-scheduled-calls-api
- baseURL: https://call4.me
  baseurl_source: declared
  description: The X402 API from call4me — 1 operation(s) for x402.
  name: call4me X402 API
  slug: call4-me-x402-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/call4-me/agentic-access/call4-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/call4-me-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/call4-me/plans/call4-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/call4-me-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/call4-me/rules/call4-me-rules.yml
  title: ''
  type: Spectral
  url: rules/call4-me-rules.yml
- group: agent
  href: https://artifacts.apis.io/call4-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/call4-me/conventions/call4-me-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/call4-me-conventions.yml
- group: design
  href: https://artifacts.apis.io/call4-me/conventions/call4-me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/call4-me-conventions.yml
- group: auth
  href: https://artifacts.apis.io/call4-me/authentication/call4-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/call4-me-authentication.yml
- group: design
  href: https://artifacts.apis.io/call4-me/errors/call4-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/call4-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/call4-me/conformance/call4-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/call4-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/call4-me/llms/call4-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/call4-me-llms.txt
- group: other
  href: https://artifacts.apis.io/call4-me/a2a/call4-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/call4-me-a2a.yml
- group: agent
  href: https://artifacts.apis.io/call4-me/well-known/call4-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/call4-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/call4-me/hosts/call4-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/call4-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/call4-me/vendors/call4-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/call4-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://call4.me/terms
- group: operate
  title: ''
  type: Support
  url: https://call4.me/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://call4.me/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://call4.me/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skeptrunedev
- group: company
  title: ''
  type: Blog
  url: https://call4.me/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://call4.me/blog/paradox-hotel-vancouver
- group: docs
  title: ''
  type: APIReference
  url: https://call4.me/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/call4-me/security/call4-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/call4-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://call4.me/
created: '2026-11-03'
description: Call4me (Skeptrune LLC) provides an AI-powered phone call service that lets AI agents place calls, book appointments, and wait on hold, then patch the user into the conversation. Integrated with ChatGPT, Claude, and other LLMs, it offers a developer-friendly API and SDKs for seamless automation.
image: https://call4.me/og/site.png?v=3
layout: provider
modified: '2026-11-03'
name: call4me
nav: Providers
network: true
overview: 'call4me publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Call4me API, Calls API, and 5 more. Tagged areas include Artificial Intelligence, Telephony, Automation, Software-as-a-Service, and Call4me.


  The call4me catalog on APIs.io includes 1 Spectral governance ruleset.


  call4me''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, API reference, and 18 more developer resources.'
plans:
- name: Call4 Me Plans Pricing
  plan_count: 1
  slug: call4-me-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: call4me API Rules
  rule_count: 51
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 4
  slug: call4-me-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 26.8
    discoverability: 66.1
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Call4 Me Authentication
  slug: call4-me-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Call4 Me Domain Security
  slug: call4-me-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 1
skills:
- name: call4-me-place-call
  slug: call4-me-place-call
slug: call4-me
tags:
- Artificial Intelligence
- Telephony
- Automation
- Software-as-a-Service
- Call4me
website: https://call4.me/
---
