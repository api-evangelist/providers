---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nanoparse Agentic Access
  operation_count: 1
  slug: nanoparse-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Web parsing service converting URLs to clean Markdown with Litmus signals.
  name: NanoParse API
  slug: nanoparse-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/agentic-access/nanoparse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nanoparse-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/rules/nanoparse-rules.yml
  title: ''
  type: Spectral
  url: rules/nanoparse-rules.yml
- group: auth
  title: ''
  type: Security
  url: https://nanoparse.app/privacy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/errors/nanoparse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nanoparse-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/conformance/nanoparse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nanoparse-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/llms/nanoparse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nanoparse-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/a2a/nanoparse-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nanoparse-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/mcp/nanoparse-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nanoparse-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/mcp/nanoparse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nanoparse-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/well-known/nanoparse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nanoparse-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/well-known/nanoparse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nanoparse-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/hosts/nanoparse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nanoparse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/vendors/nanoparse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nanoparse-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/security/nanoparse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nanoparse-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nanoparse/refs/heads/main/security/nanoparse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nanoparse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nanoparse.app
- group: docs
  title: ''
  type: Documentation
  url: https://nanoparse.app/quickstart
- group: company
  title: ''
  type: Blog
  url: https://nanoparse.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nanoparse.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nanoparse.app/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://nanoparse.app/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nanoparse-dev
created: '2026-10-15'
description: NanoParse offers a web parsing service that converts any URL into clean Markdown, targeting AI agents. It provides deterministic Litmus signals to assess content freshness, authority, and citability. Users can parse for $0.005 per request using USDC on Base, with a free tier of 10 parses. The platform includes features like Litmus scoring, quickstart guides, and a blog for updates.
layout: provider
mcp_servers:
- description: Remote MCP server at nanoparse.app.
  name: NanoParse MCP Server
  slug: nanoparse-mcp-yml
modified: '2026-10-15'
name: NanoParse
nav: Providers
network: true
overview: 'NanoParse is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Parsing, AI Agents, Markdown Conversion, Litmus Scoring, and Crypto Payments.


  The NanoParse catalog on APIs.io includes 1 Spectral governance ruleset.


  NanoParse''s developer surface includes documentation, engineering blog, API reference, and 19 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: NanoParse API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: nanoparse-rules
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 71.7
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nanoparse Domain Security
  slug: nanoparse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nanoparse Vulnerability Disclosure
  slug: nanoparse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nanoparse
tags:
- Web Parsing
- AI Agents
- Markdown Conversion
- Litmus Scoring
- Crypto Payments
website: https://nanoparse.app
---
