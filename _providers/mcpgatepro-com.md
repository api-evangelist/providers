---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mcpgatepro Com Agentic Access
  operation_count: 2
  slug: mcpgatepro-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Hosted MCP servers for Claude Desktop and Claude Code.
  name: MCPGatePro API
  slug: mcpgatepro-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/mcpgatepro-com/agentic-access/mcpgatepro-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mcpgatepro-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mcpgatepro-com/rules/mcpgatepro-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mcpgatepro-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mcpgatepro-com/errors/mcpgatepro-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mcpgatepro-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mcpgatepro-com/conformance/mcpgatepro-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcpgatepro-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/mcpgatepro-com/hosts/mcpgatepro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpgatepro-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mcpgatepro-com/security/mcpgatepro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpgatepro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpgatepro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcpgatepro.com/docs
- group: operate
  title: ''
  type: Support
  url: https://mcpgatepro.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/innodigital-io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcpgatepro.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcpgatepro.com/privacy
created: '2026-10-30'
description: 'MCPGatePro provides hosted MCP (Model Context Protocol) servers that integrate with Claude Desktop and Claude Code, enabling users to quickly connect AI tools for cloud cost analysis, PostgreSQL performance auditing, and other infrastructure insights. The platform offers a simple three-step setup: subscribe for an API key, add the provided configuration to Claude, and start querying AI for actionable recommendations on AWS spending, database optimization, and more. With plans starting at 79 zł per month, MCPGatePro targets teams seeking hassle‑free AI‑driven operations without self‑hosting or complex infrastructure.'
image: https://mcpgatepro.com/og-image.png
layout: provider
modified: '2026-10-30'
name: mcpgatepro-com
nav: Providers
network: true
overview: 'mcpgatepro-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Cloud, Cost-Management, and Database.


  The mcpgatepro-com catalog on APIs.io includes 1 Spectral governance ruleset.


  mcpgatepro-com''s developer surface includes documentation, support, and 10 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: mcpgatepro-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: mcpgatepro-com-rules
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mcpgatepro Com Domain Security
  slug: mcpgatepro-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mcpgatepro-com
tags:
- Company
- AI
- Cloud
- Cost-Management
- Database
- Monitoring
website: https://mcpgatepro.com/
---
