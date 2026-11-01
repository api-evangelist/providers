---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Trytruffle Agentic Access
  operation_count: 1
  slug: trytruffle-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://www.trytruffle.ai/api
  baseurl_source: declared
  description: The Agents API from Truffle AI — 1 operation(s) for agents.
  name: Truffle AI Agents API
  slug: trytruffle-agents-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/trytruffle/agentic-access/trytruffle-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trytruffle-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/trytruffle/rules/trytruffle-rules.yml
  title: ''
  type: Spectral
  url: rules/trytruffle-rules.yml
- group: auth
  href: https://artifacts.apis.io/trytruffle/authentication/trytruffle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trytruffle-authentication.yml
- group: design
  href: https://artifacts.apis.io/trytruffle/conformance/trytruffle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trytruffle-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trytruffle/llms/trytruffle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trytruffle-llms.txt
- group: other
  href: https://artifacts.apis.io/trytruffle/a2a/trytruffle-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/trytruffle-a2a.yml
- group: agent
  href: https://artifacts.apis.io/trytruffle/well-known/trytruffle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trytruffle-well-known.yml
- group: other
  href: https://artifacts.apis.io/trytruffle/hosts/trytruffle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trytruffle-hosts.yml
- group: other
  href: https://artifacts.apis.io/trytruffle/vendors/trytruffle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trytruffle-vendors.yml
- group: build
  href: https://artifacts.apis.io/trytruffle/packages/trytruffle-packages.yml
  title: ''
  type: SDKs
  url: packages/trytruffle-packages.yml
- group: build
  href: https://artifacts.apis.io/trytruffle/packages/trytruffle-packages.yml
  title: ''
  type: Packages
  url: packages/trytruffle-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://www.trytruffle.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trytruffle.ai/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trytruffle.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trytruffle.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/trytruffle/security/trytruffle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trytruffle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trytruffle.ai/
created: '2026-10-19'
description: 'Truffle AI is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-19'
name: Truffle AI
nav: Providers
network: true
overview: 'Truffle AI publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agents API. Tagged areas include Company.


  The Truffle AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Truffle AI''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Truffle AI API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: trytruffle-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 29.5
    catalog_earned_first_party: 0.0
    catalog_gap: 85.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 34.3
    developer_ergonomics: 50.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Trytruffle Authentication
  slug: trytruffle-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trytruffle Domain Security
  slug: trytruffle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trytruffle
tags:
- Company
website: https://trytruffle.ai/
---
