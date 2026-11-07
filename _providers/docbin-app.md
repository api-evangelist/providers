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
api_count: 1
apis:
- description: Upload and version HTML or Markdown docs via REST.
  name: docbin API
  slug: docbin-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/docbin-app/plans/docbin-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docbin-app-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/docbin-app/cli/docbin-app-cli.yml
  title: ''
  type: CLI
  url: cli/docbin-app-cli.yml
- group: design
  href: https://artifacts.apis.io/docbin-app/conformance/docbin-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docbin-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docbin-app/well-known/docbin-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docbin-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/docbin-app/hosts/docbin-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docbin-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/docbin-app/vendors/docbin-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docbin-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docbin.app/terms
- group: operate
  title: ''
  type: Support
  url: https://docbin.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docbin.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://docbin.app/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docbin.app/docs
- group: auth
  href: https://artifacts.apis.io/docbin-app/authentication/docbin-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docbin-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/docbin-app/security/docbin-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docbin-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docbin.app/
created: '2026-11-05'
description: Docbin is a markdown pastebin service that offers version history, up to 5 MB free storage per paste, and optional paid plans for larger files and additional features. Users can create, share, and embed markdown or HTML documents, with support for callouts, directives, and front‑matter. The platform provides a REST API for programmatic access, a CLI tool, and integrates with MCP for AI‑assisted editing.
image: https://docbin.app/og/landing.png?b=479bcbb740e08037d65c7e66412fb12b1b92967e
layout: provider
modified: '2026-11-05'
name: docbin
nav: Providers
network: true
overview: 'docbin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pastebin, Markdown, CLI, and Documentation.


  docbin''s developer surface includes CLI, support, pricing, documentation, authentication, and 9 more developer resources.'
plans:
- name: Docbin App Plans Pricing
  plan_count: 2
  slug: docbin-app-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
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
- kind: authentication
  name: Docbin App Authentication
  slug: docbin-app-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Docbin App Domain Security
  slug: docbin-app-domain-security
  summary_line: TLSv1.3
slug: docbin-app
tags:
- Pastebin
- Markdown
- CLI
- Documentation
website: https://docbin.app/
---
