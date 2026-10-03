---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Synthient Agentic Access
  operation_count: 53
  slug: synthient-agentic-access
  summary_line: 53 operations
api_count: 1
apis:
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: Account info, quota, and the public health probe.
  name: Synthient API Account API
  slug: synthient-account-api
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: VPN, Tor, and relay-class anonymizer IP ranges. One real-time stream and one parquet export.
  name: Synthient API Anonymizers API
  slug: synthient-anonymizers-api
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: Honeypot capture streams. Helios sensors record HTTP requests, TLS ClientHellos, and ADB shell commands from inbound traffic to our honeypot tunnels. Each protocol has its own real-time stream and par
  name: Synthient API Helios API
  slug: synthient-helios-api
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: JA4T TCP-layer fingerprint sightings attributed to source IPs with provider, country, and ASN enrichment. One real-time stream and one parquet export.
  name: Synthient API JA4T API
  slug: synthient-ja4t-api
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: Single-IP, batch-IP, and domain enrichment endpoints.
  name: Synthient API Lookup API
  slug: synthient-lookup-api
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: Residential, datacenter, mobile, Tor, and VPN proxy IPs. One real-time stream and one parquet export.
  name: Synthient API Proxies API
  slug: synthient-proxies-api
- baseURL: https://api.synthient.com/api/v4
  baseurl_source: declared
  description: DHT and tracker peer observations. One real-time stream and one parquet export.
  name: Synthient API Torrents API
  slug: synthient-torrents-api
artifact_total: 22
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/agentic-access/synthient-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/synthient-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/rate-limits/synthient-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/synthient-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/plans/synthient-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synthient-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/rules/synthient-rules.yml
  title: ''
  type: Spectral
  url: rules/synthient-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/json-ld/synthient-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/synthient-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/vocabulary/synthient-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/synthient-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/data-model/synthient-data-model.yml
  title: ''
  type: DataModel
  url: data-model/synthient-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/cli/synthient-cli.yml
  title: ''
  type: CLI
  url: cli/synthient-cli.yml
- group: auth
  title: ''
  type: Security
  url: https://synthient.com/terms
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/authentication/synthient-authentication.yml
  title: ''
  type: Authentication
  url: authentication/synthient-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/errors/synthient-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/synthient-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/conformance/synthient-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synthient-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/llms/synthient-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synthient-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/mcp/synthient-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/synthient-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/mcp/synthient-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/synthient-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/well-known/synthient-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/synthient-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/well-known/synthient-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synthient-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/hosts/synthient-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synthient-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/vendors/synthient-vendors.yml
  title: ''
  type: Vendors
  url: vendors/synthient-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://synthient.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://synthient.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://synthient.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://synthient.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://synthient.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/security/synthient-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/synthient-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/synthient/refs/heads/main/security/synthient-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synthient-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://synthient.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synthient.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synthient.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.synthient.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synthient.com/sdk
- group: build
  title: ''
  type: SDK
  url: https://docs.synthient.com/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synthient
- group: other
  title: ''
  type: SocialX
  url: https://x.com/synthient
created: '2026-09-28'
description: Synthient provides IP enrichment, account management, and real-time data feeds for cybersecurity and fraud prevention. The platform offers residential proxies, VPNs, and anonymized IP data with streaming capabilities, usage limits, and comprehensive authentication via API keys.
image: https://synthient.com/og-image.png?v=20260624
json_schemas:
- name: AnonymizerStreamEntry
  property_count: 7
  slug: synthient-anonymizer-stream-entry
- name: DomainLookupResponse
  property_count: 12
  slug: synthient-domain-lookup-response
- name: HoneypotHTTPSStreamEntry
  property_count: 7
  slug: synthient-honeypot-httpsstream-entry
- name: JA4TStreamEntry
  property_count: 7
  slug: synthient-ja4-tstream-entry
- name: ProxyStreamEntry
  property_count: 6
  slug: synthient-proxy-stream-entry
- name: TorrentStreamEntry
  property_count: 9
  slug: synthient-torrent-stream-entry
jsonld:
- class_count: 42
  name: Synthient Context
  property_count: 128
  slug: synthient-context
layout: provider
mcp_servers:
- description: ''
  name: Synthient API MCP Server
  slug: synthient-api-mcp-server
modified: '2026-09-28'
name: Synthient API
nav: Providers
network: true
overview: 'Synthient API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Anonymizers API, Helios API, and 4 more. Tagged areas include Company, IP, Enrichment, Cybersecurity, and Data.


  The Synthient API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Synthient API''s developer surface includes CLI, authentication, pricing, engineering blog, documentation, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Synthient Plans Pricing
  plan_count: 4
  slug: synthient-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 14
  name: Synthient Rate Limits
  slug: synthient-rate-limits
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Synthient API API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: synthient-rules
score:
  band: strong
  composite: 60.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 68.5
    discoverability: 71.7
    operational_transparency: 63.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Synthient Authentication
  slug: synthient-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Synthient Domain Security
  slug: synthient-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Synthient Vulnerability Disclosure
  slug: synthient-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: synthient
tags:
- Company
- IP
- Enrichment
- Cybersecurity
- Data
website: https://synthient.com/
---
