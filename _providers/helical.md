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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Helical MCP API provides endpoints for model listing, dataset upload, job execution, and more.
  name: Helical MCP API
  slug: mcp-api
artifact_total: 6
common:
- group: build
  href: https://artifacts.apis.io/helical/cli/helical-cli.yml
  title: ''
  type: CLI
  url: cli/helical-cli.yml
- group: agent
  href: https://artifacts.apis.io/helical/well-known/helical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/helical-well-known.yml
- group: other
  href: https://artifacts.apis.io/helical/hosts/helical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/helical-hosts.yml
- group: other
  href: https://artifacts.apis.io/helical/vendors/helical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/helical-vendors.yml
- group: auth
  href: https://artifacts.apis.io/helical/security/helical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/helical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.helical.bio/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.helical.bio/plugin
- group: docs
  title: ''
  type: Documentation
  url: https://www.helical.bio/plugin/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.helical.bio/plugin/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.helical.bio/plugin/cookbooks/getting-started-with-helical-mcp
- group: operate
  title: ''
  type: Support
  url: https://console.helical.bio/contact
- group: company
  title: ''
  type: Blog
  url: https://www.helical.bio/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helicalAI/helical
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.helical.bio/plugin/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helical.bio/plugin/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.helical.bio/mcp
  - status: 200
    url: https://www.helical.bio/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Helical turns your data into biological intelligence for target identification and biomarker discovery. Your models and the intelligence they capture stay yours. Helical provides a virtual AI lab for drug discovery, enabling users to teach biological foundation models with proprietary data, run target and biomarker workflows, and assess cross-species translation with evidence to prioritize experiments.
image: https://www.helical.bio/brand/og.jpg
layout: provider
modified: '2026-10-29'
name: Helical
nav: Providers
network: true
overview: 'Helical is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Artificial Intelligence, Drug Discovery, and Bioinformatics.


  Helical''s developer surface includes CLI, documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Helical Plans Pricing
  plan_count: 0
  slug: helical-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Helical Rate Limits
  slug: helical-rate-limits
scopes:
- name: Helical Scopes
  scope_count: 0
  slug: helical-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.8
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
screenshot: https://apis.io/screenshots/helical/helical-2026-11-03T133335.png
security:
- kind: authentication
  name: Helical Authentication
  slug: helical-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Helical Domain Security
  slug: helical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helical
tags:
- Company
- Biotechnology
- Artificial Intelligence
- Drug Discovery
- Bioinformatics
- Platform
website: https://www.helical.bio/
---
