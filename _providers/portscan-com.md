---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Portscan Com Agentic Access
  operation_count: 6
  slug: portscan-com-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.portscan.com
  baseurl_source: declared
  description: The Deep API from portscan-com — 2 operation(s) for deep.
  name: portscan-com Deep API
  slug: portscan-com-deep-api
- baseURL: https://api.portscan.com
  baseurl_source: declared
  description: The Fast API from portscan-com — 2 operation(s) for fast.
  name: portscan-com Fast API
  slug: portscan-com-fast-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/portscan-com/agentic-access/portscan-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/portscan-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/portscan-com/rate-limits/portscan-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/portscan-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/portscan-com/rules/portscan-com-rules.yml
  title: ''
  type: Spectral
  url: rules/portscan-com-rules.yml
- group: design
  href: https://artifacts.apis.io/portscan-com/json-ld/portscan-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/portscan-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/portscan-com/vocabulary/portscan-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/portscan-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/portscan-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/portscan-com/data-model/portscan-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/portscan-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/portscan-com/security/portscan-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/portscan-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/portscan-com/errors/portscan-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/portscan-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/portscan-com/conformance/portscan-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/portscan-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/portscan-com/llms/portscan-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/portscan-com-llms.txt
- group: build
  href: https://artifacts.apis.io/portscan-com/mcp/portscan-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/portscan-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/portscan-com/mcp/portscan-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/portscan-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/portscan-com/well-known/portscan-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/portscan-com-security.txt
- group: auth
  href: https://artifacts.apis.io/portscan-com/well-known/portscan-com-a-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/portscan-com-a-security.txt
- group: agent
  href: https://artifacts.apis.io/portscan-com/well-known/portscan-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/portscan-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/portscan-com/hosts/portscan-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/portscan-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/portscan-com/vendors/portscan-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/portscan-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://portscan.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://portscan.com/privacy
- group: auth
  href: https://artifacts.apis.io/portscan-com/security/portscan-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/portscan-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/portscan-com/security/portscan-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portscan-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portscan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.portscan.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.portscan.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.portscan.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.portscan.com/
created: '2026-10-31'
description: portscan.com provides a free online port scanner and a public HTTP API that lets anyone scan TCP ports on an IP address without requiring an account, API key, or signup. The service offers fast scans of common ports (about 20 seconds) and deep scans of all 65,535 ports (60‑300 seconds), includes service and version detection via nmap, reverse DNS lookup, and supports both IPv4 and IPv6. Documentation is available at https://api.portscan.com/, and a developer portal at https://mcp.portscan.com/. The website https://portscan.com/ describes the offering and provides links to the API and terms of service.
image: https://portscan.com/og-image.png
json_schemas:
- name: ScanQueued
  property_count: 6
  slug: portscan-com-scan-queued
- name: ScanResult
  property_count: 15
  slug: portscan-com-scan-result
jsonld:
- class_count: 4
  name: Portscan Com Context
  property_count: 23
  slug: portscan-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.portscan.com.
  name: portscan-com MCP Server
  slug: portscan-com-mcp-yml
modified: '2026-10-31'
name: portscan-com
nav: Providers
network: true
overview: 'portscan-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Deep API and Fast API. Tagged areas include Networking, Security, and Port Scanning.


  The portscan-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  portscan-com''s developer surface includes documentation, API reference, getting-started guide, and 24 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 4
  name: Portscan Com Rate Limits
  slug: portscan-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: portscan-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: portscan-com-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 52.6
    developer_ergonomics: 25.5
    discoverability: 56.7
    operational_transparency: 42.1
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/portscan-com/portscan-com-2026-11-03T141413.png
security:
- kind: authentication
  name: Portscan Com Authentication
  slug: portscan-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Portscan Com Domain Security
  slug: portscan-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Portscan Com Vulnerability Disclosure
  slug: portscan-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: deep-scan
  slug: portscan-com-deep-scan
- name: fast-scan
  slug: portscan-com-fast-scan
slug: portscan-com
tags:
- Networking
- Security
- Port Scanning
website: https://portscan.com/
---
