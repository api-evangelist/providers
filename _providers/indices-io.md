---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Indices Io Agentic Access
  operation_count: 26
  slug: indices-io-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 1
apis:
- description: The Indices REST API providing AI agent data services.
  name: Indices API
  slug: indices-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/indices-io/conformance/indices-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/indices-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/indices-io/llms/indices-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/indices-io-llms.txt
- group: other
  href: https://artifacts.apis.io/indices-io/hosts/indices-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/indices-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/indices-io/vendors/indices-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/indices-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/indices-io/packages/indices-io-packages.yml
  title: ''
  type: SDKs
  url: packages/indices-io-packages.yml
- group: build
  href: https://artifacts.apis.io/indices-io/packages/indices-io-packages.yml
  title: ''
  type: Packages
  url: packages/indices-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.indices.io/
- group: auth
  href: https://artifacts.apis.io/indices-io/security/indices-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/indices-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://indices.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indicesio
created: '2026-10-30'
description: Indices is building the infrastructure that enables AI agents to act across the web in real time, securely and reliably. The team brings decades of experience in large‑scale distributed systems, security, and low‑latency engineering, having built battle‑hardened platforms for finance and cloud services. Their platform aims to provide usable, trustworthy data and tooling for AI agents, supporting use‑cases from data retrieval to autonomous actions on the internet.
json_schemas:
- name: CaptureSession
  property_count: 6
  slug: indices-io-capture-session
- name: Connector
  property_count: 9
  slug: indices-io-connector
- name: CreateRunRequest
  property_count: 7
  slug: indices-io-create-run-request
- name: CreateSecretRequest
  property_count: 6
  slug: indices-io-create-secret-request
- name: File
  property_count: 8
  slug: indices-io-file
- name: Run
  property_count: 13
  slug: indices-io-run
jsonld:
- class_count: 40
  name: Indices Io Context
  property_count: 72
  slug: indices-io-context
layout: provider
modified: '2026-10-30'
name: indices-io
nav: Providers
network: true
overview: 'indices-io is listed with 1 API on the [APIs.io](https://apis.io/) network: Indices API. Tagged areas include Company, AI, Infrastructure, Real-time, and Security.


  The indices-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Indices Io Plans Pricing
  plan_count: 0
  slug: indices-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Indices Io Rate Limits
  slug: indices-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: indices-io API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 3
  slug: indices-io-rules
scopes:
- name: Indices Io Scopes
  scope_count: 0
  slug: indices-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.2
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 53.6
    contract_quality: 52.2
    developer_ergonomics: 7.1
    discoverability: 62.5
    operational_transparency: 21.1
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Indices Io Authentication
  slug: indices-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Indices Io Domain Security
  slug: indices-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: capture-sessions
  slug: indices-io-capture-sessions
- name: runs
  slug: indices-io-runs
slug: indices-io
tags:
- Company
- AI
- Infrastructure
- Real-time
- Security
website: https://indices.io/
---
