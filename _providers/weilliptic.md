---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for the WeilChain platform, covering collections, tokens, and streaming.
  name: WeilChain API
  slug: weilchain-api
- description: 'Weilliptic API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Weilliptic API
  slug: weilliptic-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/weilliptic/rules/weilliptic-rules.yml
  title: ''
  type: Spectral
  url: rules/weilliptic-rules.yml
- group: design
  href: https://artifacts.apis.io/weilliptic/vocabulary/weilliptic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weilliptic-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/weilliptic/conformance/weilliptic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weilliptic-conformance.yml
- group: other
  href: https://artifacts.apis.io/weilliptic/hosts/weilliptic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weilliptic-hosts.yml
- group: other
  href: https://artifacts.apis.io/weilliptic/vendors/weilliptic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weilliptic-vendors.yml
- group: build
  href: https://artifacts.apis.io/weilliptic/packages/weilliptic-packages.yml
  title: ''
  type: SDKs
  url: packages/weilliptic-packages.yml
- group: build
  href: https://artifacts.apis.io/weilliptic/packages/weilliptic-packages.yml
  title: ''
  type: Packages
  url: packages/weilliptic-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weilliptic.ai/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/weilliptic/security/weilliptic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weilliptic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weilliptic.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.weilliptic.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.weilliptic.ai/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://weilliptic.ai/get-started/
- group: company
  title: ''
  type: Blog
  url: https://weilliptic.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weilliptic-public
coverage:
  checked: '2026-10-29'
  detail: Public documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 200
    url: https://docs.weilliptic.ai/docs/reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Weilliptic provides infrastructure for autonomous systems, offering a stack of primitives such as WeilChain, Autos, Writ, Pensieve, WeilStream, and Receipts. The platform enables secure identity, scoped authority, tamper‑evident memory, event streaming, and verifiable receipts for AI agents and decentralized applications.
image: https://weilliptic.ai/img/weilliptic-logo.svg
layout: provider
modified: '2026-10-29'
name: Weilliptic
nav: Providers
network: true
overview: 'Weilliptic is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Autonomous Systems, Blockchain, Platform, and Developer Tools.


  The Weilliptic catalog on APIs.io includes 1 Spectral governance ruleset.


  Weilliptic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 11 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Weilliptic Rate Limits
  slug: weilliptic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Weilliptic API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: weilliptic-rules
scopes:
- name: Weilliptic Scopes
  scope_count: 0
  slug: weilliptic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Weilliptic Authentication
  slug: weilliptic-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Weilliptic Domain Security
  slug: weilliptic-domain-security
  summary_line: TLSv1.3 · HSTS
slug: weilliptic
tags:
- AI
- Autonomous Systems
- Blockchain
- Platform
- Developer Tools
website: https://weilliptic.ai
---
