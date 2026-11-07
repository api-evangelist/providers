---
access_model:
  confidence: low
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
    mcp_server: documented
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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: build
  href: https://artifacts.apis.io/strunk-io/cli/strunk-io-cli.yml
  title: ''
  type: CLI
  url: cli/strunk-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/strunk-io/changelog/strunk-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/strunk-io-changelog.yml
- group: agent
  href: https://artifacts.apis.io/strunk-io/well-known/strunk-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/strunk-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/strunk-io/hosts/strunk-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/strunk-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/strunk-io/vendors/strunk-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/strunk-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/strunk-io/packages/strunk-io-packages.yml
  title: ''
  type: SDKs
  url: packages/strunk-io-packages.yml
- group: build
  href: https://artifacts.apis.io/strunk-io/packages/strunk-io-packages.yml
  title: ''
  type: Packages
  url: packages/strunk-io-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://strunk.io/changelog
- group: auth
  href: https://artifacts.apis.io/strunk-io/security/strunk-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strunk-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strunk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://strunk.io/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strunk.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strunk.io/terms
- group: operate
  title: ''
  type: Support
  url: https://strunk.io/help
- group: start
  title: ''
  type: SignUp
  url: https://strunk.io/account
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found on discovered hosts despite probing common locations; docs page provides only product information.
  evidence:
  - status: 404
    url: https://strunk.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Strunk is a productivity tool that bridges AI assistants like Claude, ChatGPT, and Codex with Google Docs, enabling reviewers' comments to be captured and applied back into the AI tool for seamless document revision without losing context. By connecting AI-generated drafts to Google Docs, Strunk allows users to publish documents, pull reviewer comments, and automatically apply approved edits, preserving comment threads. It supports multiple AI clients, offers a free sign‑up via Google account, and provides support through email and live chat.
image: https://strunk.io/brand/strunk-icon-plate-512.png
layout: provider
modified: '2026-10-31'
name: strunk-io
nav: Providers
network: true
overview: 'strunk-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Document Review, Google Docs, and MCP.


  strunk-io''s developer surface includes CLI, changelog, documentation, support, signup flow, and 10 more developer resources.'
plans:
- name: Strunk Io Plans Pricing
  plan_count: 0
  slug: strunk-io-plans-pricing
random_paper: 4
scopes:
- name: Strunk Io Scopes
  scope_count: 0
  slug: strunk-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 21.3
  provenance:
    conformance: unknown
    mcp: first-party
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
screenshot: https://apis.io/screenshots/strunk-io/strunk-io-2026-11-03T143938.png
security:
- kind: authentication
  name: Strunk Io Authentication
  slug: strunk-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Strunk Io Domain Security
  slug: strunk-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: strunk-io
tags:
- Artificial Intelligence
- Productivity
- Document Review
- Google Docs
- MCP
website: https://strunk.io/
---
