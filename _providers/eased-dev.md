---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- description: Eased UI provides a library of animated React components via a component registry and MCP. Documentation is available at the docs site.
  name: Eased UI API
  slug: eased-ui-api
- description: 'Eased UI API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Eased UI API
  slug: eased-dev-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/eased-dev/plans/eased-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eased-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eased-dev/rules/eased-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/eased-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/eased-dev/vocabulary/eased-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eased-dev-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/eased-dev/changelog/eased-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eased-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/eased-dev/conformance/eased-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eased-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eased-dev/llms/eased-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eased-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/eased-dev/hosts/eased-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eased-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/eased-dev/vendors/eased-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eased-dev-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://eased.dev/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://eased.dev/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://eased.dev/docs/agent-quickstart
- group: auth
  href: https://artifacts.apis.io/eased-dev/security/eased-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eased-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eased.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://eased.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://eased.dev/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eased-dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eased.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eased.dev/privacy
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are served as markdown via .md URLs but the site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://eased.dev/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: Eased UI provides a library of animated React components for shadcn and AI agents, built with Tailwind CSS and Motion. It offers ready‑to‑use UI elements that enhance developer productivity and enable smooth motion‑first interfaces. The project is open‑source, documented with examples, guides, and a pricing page for pro features.
image: https://eased.dev/opengraph-image?d10543269fc03e5f
layout: provider
modified: '2026-11-06'
name: Eased UI
nav: Providers
network: true
overview: 'Eased UI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include React, UI, Tailwind, Motion, and Open Source.


  The Eased UI catalog on APIs.io includes 1 Spectral governance ruleset.


  Eased UI''s developer surface includes changelog, getting-started guide, documentation, pricing, GitHub presence, and 13 more developer resources.'
plans:
- name: Eased Dev Plans Pricing
  plan_count: 6
  slug: eased-dev-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Eased UI API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: eased-dev-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eased Dev Domain Security
  slug: eased-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eased-dev
tags:
- React
- UI
- Tailwind
- Motion
- Open Source
website: https://eased.dev/
---
