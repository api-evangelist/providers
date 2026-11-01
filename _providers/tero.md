---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Tero API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Tero API
  slug: tero-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/tero/rules/tero-rules.yml
  title: ''
  type: Spectral
  url: rules/tero-rules.yml
- group: design
  href: https://artifacts.apis.io/tero/vocabulary/tero-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tero-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tero/conformance/tero-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tero-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tero/llms/tero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tero-llms.txt
- group: other
  href: https://artifacts.apis.io/tero/a2a/tero-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tero-a2a.yml
- group: agent
  href: https://artifacts.apis.io/tero/well-known/tero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tero-well-known.yml
- group: other
  href: https://artifacts.apis.io/tero/hosts/tero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tero-hosts.yml
- group: other
  href: https://artifacts.apis.io/tero/vendors/tero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tero-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.usetero.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usetero.com/edge/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usetero.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/tero/security/tero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usetero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usetero.com/
- group: company
  title: ''
  type: Blog
  url: https://usetero.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://usetero.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usetero.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usetero.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usetero
coverage:
  checked: '2026-10-24'
  detail: Documentation at https://docs.usetero.com/ provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 404
    url: https://docs.usetero.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Tero provides an agent‑native telemetry layer that connects read‑only to existing observability data stores. It continuously identifies costly waste, sensitive data exposure, and operational risks that traditional tools miss. By delivering actionable issue evidence, Tero helps organizations cut costs by 40‑60%, improve compliance, and enhance reliability across cloud and on‑prem environments. The platform offers a unified view of telemetry, automated issue detection, and integrated remediation actions, all without requiring changes to existing monitoring stacks.
layout: provider
modified: '2026-10-24'
name: Tero
nav: Providers
network: true
overview: 'Tero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Telemetry, Cost-Reduction, and Compliance.


  The Tero catalog on APIs.io includes 1 Spectral governance ruleset.


  Tero''s developer surface includes getting-started guide, API reference, documentation, engineering blog, pricing, and 14 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tero API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: tero-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 31.0
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tero Domain Security
  slug: tero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tero
tags:
- Company
- Observability
- Telemetry
- Cost-Reduction
- Compliance
- Reliability
website: https://www.usetero.com/
---
