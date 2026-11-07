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
- description: Dynaboard provides a collaborative low-code IDE with a REST API documented at the developer docs.
  name: Dynaboard API
  slug: dynaboard-api-2
- description: 'Dynaboard API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Dynaboard API
  slug: dynaboard-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/dynaboard/plans/dynaboard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynaboard-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dynaboard/rules/dynaboard-rules.yml
  title: ''
  type: Spectral
  url: rules/dynaboard-rules.yml
- group: design
  href: https://artifacts.apis.io/dynaboard/vocabulary/dynaboard-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dynaboard-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/dynaboard/authentication/dynaboard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynaboard-authentication.yml
- group: design
  href: https://artifacts.apis.io/dynaboard/conformance/dynaboard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynaboard-conformance.yml
- group: other
  href: https://artifacts.apis.io/dynaboard/hosts/dynaboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynaboard-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynaboard/vendors/dynaboard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynaboard-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dynaboard.com/docs/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://dynaboard.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://dynaboard.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynaboard
- group: docs
  title: ''
  type: Documentation
  url: https://dynaboard.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://dynaboard.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://dynaboard.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://dynaboard.com/docs/reference/hotkeys
- group: start
  title: ''
  type: GettingStarted
  url: https://dynaboard.com/docs/getting-started/quick-start
- group: auth
  href: https://artifacts.apis.io/dynaboard/security/dynaboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynaboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dynaboard.com
created: '2026-10-24'
description: Dynaboard provides a collaborative low-code IDE for developers, enabling real‑time, multiplayer web app development with a drag‑and‑drop builder, code‑first UI framework, and generative AI assistance. It supports TypeScript, AI‑generated components, and a WebAssembly‑powered VM for custom logic, targeting full‑stack applications.
image: https://images.ctfassets.net/b0wn34vnc1k8/UnmzMMHv5u02RJcDhhFSA/e78b60d6f86e26247b6b581c62b55353/dynaboard.png
layout: provider
modified: '2026-10-24'
name: Dynaboard
nav: Providers
network: true
overview: 'Dynaboard is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Low-Code, Collaboration, Real-Time, Artificial Intelligence, and Web Development.


  The Dynaboard catalog on APIs.io includes 1 Spectral governance ruleset.


  Dynaboard''s developer surface includes authentication, pricing, documentation, changelog, engineering blog, API reference, getting-started guide, and 11 more developer resources.'
plans:
- name: Dynaboard Plans Pricing
  plan_count: 5
  slug: dynaboard-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dynaboard API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dynaboard-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 27.4
    discoverability: 58.0
    operational_transparency: 10.5
  previous_composite: 34.2
  provenance:
    conformance: first-party
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
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dynaboard/dynaboard-2026-11-03T131141.png
security:
- kind: authentication
  name: Dynaboard Authentication
  slug: dynaboard-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Dynaboard Domain Security
  slug: dynaboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dynaboard
tags:
- Low-Code
- Collaboration
- Real-Time
- Artificial Intelligence
- Web Development
website: https://dynaboard.com
---
