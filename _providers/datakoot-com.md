---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Datakoot Com Agentic Access
  operation_count: 52
  slug: datakoot-com-agentic-access
  summary_line: 52 operations · 50 acting
api_count: 1
apis:
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Base Intel API from datakoot-com — 5 operation(s) for base intel.
  name: datakoot-com Base Intel API
  slug: datakoot-com-base-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Domain Intel API from datakoot-com — 6 operation(s) for domain intel.
  name: datakoot-com Domain Intel API
  slug: datakoot-com-domain-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Economy Intel API from datakoot-com — 5 operation(s) for economy intel.
  name: datakoot-com Economy Intel API
  slug: datakoot-com-economy-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Filings Intel API from datakoot-com — 5 operation(s) for filings intel.
  name: datakoot-com Filings Intel API
  slug: datakoot-com-filings-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Koot API from datakoot-com — 4 operation(s) for koot.
  name: datakoot-com Koot API
  slug: datakoot-com-koot-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Market Intel API from datakoot-com — 5 operation(s) for market intel.
  name: datakoot-com Market Intel API
  slug: datakoot-com-market-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Package Intel API from datakoot-com — 6 operation(s) for package intel.
  name: datakoot-com Package Intel API
  slug: datakoot-com-package-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Regulatory Intel API from datakoot-com — 5 operation(s) for regulatory intel.
  name: datakoot-com Regulatory Intel API
  slug: datakoot-com-regulatory-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Security Intel API from datakoot-com — 5 operation(s) for security intel.
  name: datakoot-com Security Intel API
  slug: datakoot-com-security-intel-api
- baseURL: https://x402.datakoot.com
  baseurl_source: declared
  description: The Weather & Geo API from datakoot-com — 6 operation(s) for weather & geo.
  name: datakoot-com Weather & Geo API
  slug: datakoot-com-weather-geo-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/datakoot-com/agentic-access/datakoot-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datakoot-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/datakoot-com/rate-limits/datakoot-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datakoot-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/datakoot-com/rules/datakoot-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datakoot-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datakoot-com/vocabulary/datakoot-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datakoot-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/datakoot-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/datakoot-com/errors/datakoot-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datakoot-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datakoot-com/conformance/datakoot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datakoot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datakoot-com/llms/datakoot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datakoot-com-llms.txt
- group: build
  href: https://artifacts.apis.io/datakoot-com/mcp/datakoot-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/datakoot-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/datakoot-com/mcp/datakoot-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datakoot-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/datakoot-com/well-known/datakoot-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datakoot-com-security.txt
- group: agent
  href: https://artifacts.apis.io/datakoot-com/well-known/datakoot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datakoot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datakoot-com/hosts/datakoot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datakoot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datakoot-com/vendors/datakoot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datakoot-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datakoot.com/terms
- group: auth
  title: ''
  type: Security
  url: https://datakoot.com/security
- group: auth
  href: https://artifacts.apis.io/datakoot-com/security/datakoot-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datakoot-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datakoot-com/security/datakoot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datakoot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datakoot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datakoot.com/start
- group: docs
  title: ''
  type: Documentation
  url: https://datakoot.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://datakoot.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://datakoot.com/start
- group: operate
  title: ''
  type: Support
  url: https://datakoot.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datakoot
- group: commercial
  title: ''
  type: Pricing
  url: https://datakoot.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://datakoot.com/start
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datakoot.com/privacy
created: '2026-10-29'
description: Datakoot provides keyless, real‑time data APIs designed for AI agents. Its platform offers a suite of MCP (Machine‑Callable Procedures) servers delivering up‑to‑date information such as vulnerability CVE lookups, package intelligence, SEC filings, economic data, weather, and domain/DNS reconnaissance. All data is served without requiring authentication tokens, enabling seamless integration for autonomous agents. Datakoot emphasizes privacy, never selling lookup data, and operates from Pine Grove, Pennsylvania.
image: https://datakoot.com/og/default.png
layout: provider
mcp_servers:
- description: Remote MCP server at x402.datakoot.com.
  name: datakoot-com MCP Server
  slug: datakoot-com-mcp-yml
modified: '2026-10-29'
name: datakoot-com
nav: Providers
network: true
overview: 'datakoot-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Base Intel API, Domain Intel API, Economy Intel API, and 7 more. Tagged areas include Company, Data, AI, Real-time, and MCP.


  The datakoot-com catalog on APIs.io includes 1 Spectral governance ruleset.


  datakoot-com''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Datakoot Com Rate Limits
  slug: datakoot-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: datakoot-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: datakoot-com-rules
scopes:
- name: Datakoot Com Scopes
  scope_count: 0
  slug: datakoot-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 49.6
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datakoot Com Authentication
  slug: datakoot-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Datakoot Com Domain Security
  slug: datakoot-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datakoot Com Vulnerability Disclosure
  slug: datakoot-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: cve-lookup-skill
  slug: cve-lookup-skill
- name: package-vulnerabilities-skill
  slug: package-vulnerabilities-skill
- name: weather-forecast-skill
  slug: weather-forecast-skill
slug: datakoot-com
tags:
- Company
- Data
- AI
- Real-time
- MCP
- Security
website: https://datakoot.com/
---
