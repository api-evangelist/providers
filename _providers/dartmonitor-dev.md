---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Monitor and manage Dart applications via the MCP documented at https://dartmonitor.dev/docs/mcp
  name: DartMonitor MCP
  slug: dartmonitor-mcp
- description: 'dartmonitor-dev API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: dartmonitor-dev API
  slug: dartmonitor-dev-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/dartmonitor-dev/rules/dartmonitor-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/dartmonitor-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/dartmonitor-dev/vocabulary/dartmonitor-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dartmonitor-dev-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/dartmonitor-dev/cli/dartmonitor-dev-cli.yml
  title: ''
  type: CLI
  url: cli/dartmonitor-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/dartmonitor-dev/conformance/dartmonitor-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dartmonitor-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dartmonitor-dev/llms/dartmonitor-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dartmonitor-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/dartmonitor-dev/mcp/dartmonitor-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dartmonitor-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/dartmonitor-dev/hosts/dartmonitor-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dartmonitor-dev-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dartmonitor.dev/docs/mcp
- group: auth
  href: https://artifacts.apis.io/dartmonitor-dev/security/dartmonitor-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dartmonitor-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dartmonitor.dev/
created: '2026-11-04'
description: DartMonitor provides a web interface, MCP server, and Python CLI for checking outdated Flutter and Dart dependencies in a pubspec.yaml file. It lists newer package versions, shows changelog entries between the used and latest versions, and can send email digests and alerts for breaking changes, security fixes, or deprecations. The service also offers an MCP endpoint that AI agents such as Claude Code can query, and the CLI can be used in CI pipelines with an exit code indicating available updates.
image: https://dartmonitor.dev/opengraph-image.png?opengraph-image.16zk1d4j-x-0x.png
layout: provider
mcp_servers:
- description: Remote MCP server at dartmonitor.dev.
  name: dartmonitor-dev MCP Server
  slug: dartmonitor-dev-mcp-yml
modified: '2026-11-04'
name: dartmonitor-dev
nav: Providers
network: true
overview: 'dartmonitor-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Flutter, Dart, CI, and Email Alerts.


  The dartmonitor-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  dartmonitor-dev''s developer surface includes CLI, documentation, and 8 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: dartmonitor-dev API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: dartmonitor-dev-rules
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.4
    developer_ergonomics: 16.7
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dartmonitor Dev Domain Security
  slug: dartmonitor-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dartmonitor-dev
tags:
- Flutter
- Dart
- CI
- Email Alerts
website: https://dartmonitor.dev/
---
