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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bitcoinyield Agentic Access
  operation_count: 3
  slug: bitcoinyield-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://bitcoinyield.co
  baseurl_source: declared
  description: The Offers API from BitcoinYield — 1 operation(s) for offers.
  name: BitcoinYield Offers API
  slug: bitcoinyield-offers-api
- baseURL: https://bitcoinyield.co
  baseurl_source: declared
  description: The Prices API from BitcoinYield — 1 operation(s) for prices.
  name: BitcoinYield Prices API
  slug: bitcoinyield-prices-api
- baseURL: https://bitcoinyield.co
  baseurl_source: declared
  description: The Yields API from BitcoinYield — 1 operation(s) for yields.
  name: BitcoinYield Yields API
  slug: bitcoinyield-yields-api
artifact_total: 7
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/errors/bitcoinyield-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitcoinyield-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/well-known/bitcoinyield-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitcoinyield-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/agentic-access/bitcoinyield-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitcoinyield-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/rules/bitcoinyield-rules.yml
  title: ''
  type: Spectral
  url: rules/bitcoinyield-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/conformance/bitcoinyield-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitcoinyield-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/llms/bitcoinyield-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitcoinyield-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/hosts/bitcoinyield-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcoinyield-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/vendors/bitcoinyield-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitcoinyield-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/security/bitcoinyield-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcoinyield-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitcoinyield.co
- group: docs
  title: ''
  type: Documentation
  url: https://bitcoinyield.co/docs
- group: company
  title: ''
  type: Blog
  url: https://bitcoinyield.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitcoinyield.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitcoinyield.co/legal/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinyield/refs/heads/main/mcp/bitcoinyield-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bitcoinyield-mcp.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://bitcoinyield.co/openapi.json
created: '2026-10-06'
description: BitcoinYield publishes live crypto yields (BTC, ETH, SOL and stablecoins) from about 220 platforms, each with an A-D risk grade, refreshed every three hours. The REST API (GET /api/v1/yields, /api/v1/offers, /api/v1/prices) and a remote Model Context Protocol (MCP) server for AI agents (https://bitcoinyield.co/api/mcp, tools list_yields and list_offers) need no key, account or sign-up.
image: https://bitcoinyield.co/opengraph-image?v=165863
layout: provider
mcp_servers:
- description: BitcoinYield serves a remote Model Context Protocol server for AI agents on its own host. No key, account or sign-up; an anonymous tools/list returns two tools.
  name: BitcoinYield MCP Server
  slug: bitcoinyield-mcp-yml
modified: '2026-10-12'
name: BitcoinYield
nav: Providers
network: true
overview: 'BitcoinYield publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Offers API, Prices API, and Yields API. Tagged areas include Company, Cryptocurrency, Yield, and Finance.


  The BitcoinYield catalog on APIs.io includes 1 Spectral governance ruleset.


  BitcoinYield''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: BitcoinYield API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: bitcoinyield-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 11.9
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Bitcoinyield Domain Security
  slug: bitcoinyield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitcoinyield
tags:
- Company
- Cryptocurrency
- Yield
- Finance
website: https://bitcoinyield.co
---
