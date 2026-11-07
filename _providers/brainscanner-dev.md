---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/brainscanner-dev/plans/brainscanner-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brainscanner-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brainscanner-dev/conformance/brainscanner-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainscanner-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brainscanner-dev/well-known/brainscanner-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainscanner-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/brainscanner-dev/hosts/brainscanner-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainscanner-dev-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://brainscanner.dev/pricing
- group: auth
  href: https://artifacts.apis.io/brainscanner-dev/security/brainscanner-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainscanner-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainscanner.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://brainscanner.dev/guides/first-project-handoff
- group: start
  title: ''
  type: GettingStarted
  url: https://brainscanner.dev/guides/first-project-handoff
- group: start
  title: ''
  type: SignUp
  url: https://brainscanner.dev/signup
- group: operate
  title: ''
  type: Support
  url: mailto:support@brainscanner.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brainscanner.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainscanner.dev/privacy
coverage:
  checked: '2026-11-03'
  detail: Documentation is publicly available but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://brainscanner.dev/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Brain Scanner is a web application that helps developers review, pivot, and manage AI coding agent decisions. It records change histories, decision trails, and provides a workspace to connect coding agents like Claude Code or Codex. Users can sign up for a free account, explore project graphs, view change reports, and integrate with MCP settings to streamline AI agent workflows.
image: https://brainscanner.dev/brain-scanner-logo.png
layout: provider
modified: '2026-11-02'
name: Brain Scanner
nav: Providers
network: true
overview: 'Brain Scanner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Coding, Code Review, Session Replay, and Task Queue.


  Brain Scanner''s developer surface includes pricing, documentation, getting-started guide, signup flow, support, and 8 more developer resources.'
plans:
- name: Brainscanner Dev Plans Pricing
  plan_count: 2
  slug: brainscanner-dev-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainscanner Dev Domain Security
  slug: brainscanner-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: brainscanner-dev
tags:
- AI Coding
- Code Review
- Session Replay
- Task Queue
website: https://brainscanner.dev/
---
