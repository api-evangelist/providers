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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'LatchBio API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: LatchBio API
  slug: latchbio-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/latchbio/rules/latchbio-rules.yml
  title: ''
  type: Spectral
  url: rules/latchbio-rules.yml
- group: design
  href: https://artifacts.apis.io/latchbio/vocabulary/latchbio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/latchbio-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/latchbio/cli/latchbio-cli.yml
  title: ''
  type: CLI
  url: cli/latchbio-cli.yml
- group: design
  href: https://artifacts.apis.io/latchbio/conformance/latchbio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/latchbio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/latchbio/llms/latchbio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/latchbio-llms.txt
- group: other
  href: https://artifacts.apis.io/latchbio/a2a/latchbio-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/latchbio-a2a.yml
- group: agent
  href: https://artifacts.apis.io/latchbio/mcp/latchbio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/latchbio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/latchbio/well-known/latchbio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/latchbio-well-known.yml
- group: other
  href: https://artifacts.apis.io/latchbio/hosts/latchbio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/latchbio-hosts.yml
- group: other
  href: https://artifacts.apis.io/latchbio/vendors/latchbio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/latchbio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://latch.bio/security
- group: company
  title: ''
  type: Blog
  url: https://blog.latch.bio/
- group: start
  title: ''
  type: GettingStarted
  url: https://wiki.latch.bio/start/quickstart
- group: auth
  href: https://artifacts.apis.io/latchbio/security/latchbio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latchbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latch.bio/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.latch.bio/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.latch.bio/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wiki.latch.bio/wiki/resources/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wiki.latch.bio/wiki/resources/privacy-policy
created: '2026-10-22'
description: LatchBio provides a platform that harmonizes wet and dry lab workflows, enabling high‑throughput biological experiments, data capture, and analysis. By integrating laboratory automation, assay management, and machine‑learning driven insights, LatchBio helps researchers accelerate discovery and improve reproducibility across biotech and pharmaceutical research.
image: https://latch.bio/_next/static/media/open_graph.0fb8911c.png
layout: provider
mcp_servers:
- description: Remote MCP server at wiki.latch.bio.
  name: LatchBio MCP Server
  slug: latchbio-mcp-yml
modified: '2026-10-22'
name: LatchBio
nav: Providers
network: true
overview: 'LatchBio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, LabAutomation, DataAnalytics, MachineLearning, and Platform.


  The LatchBio catalog on APIs.io includes 1 Spectral governance ruleset.


  LatchBio''s developer surface includes CLI, engineering blog, getting-started guide, documentation, API reference, and 14 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: LatchBio API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: latchbio-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Latchbio Domain Security
  slug: latchbio-domain-security
  summary_line: TLSv1.2 · DMARC
slug: latchbio
tags:
- Biotechnology
- LabAutomation
- DataAnalytics
- MachineLearning
- Platform
- Company
website: https://latch.bio/
---
