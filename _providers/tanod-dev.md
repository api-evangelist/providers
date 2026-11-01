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
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 288
  human_in_the_loop: 7
  name: Tanod Dev Agentic Access
  operation_count: 376
  slug: tanod-dev-agentic-access
  summary_line: 376 operations · 288 acting · 7 human-in-the-loop
api_count: 11
apis:
- baseURL: https://agents.tanod.dev
  baseurl_source: declared
  description: agentscan, the agent-economy index. Query, history, export and bulk access to a daily cross-registry index of x402 endpoints and MCP servers (aggregated public-registry data, not an endorsement).
  name: tanod-dev Agentscan API
  slug: tanod-dev-agentscan-api
- baseURL: https://agents.tanod.dev
  baseurl_source: declared
  description: chainpeek, the on-chain read. Read-only ENS resolution and records, EVM calldata and event-log decoding, ERC-20 token metadata, proxy detection, block-at-time lookup, ETH and BTC price candles (OHLCV)
  name: tanod-dev Chainpeek API
  slug: tanod-dev-chainpeek-api
- baseURL: https://security.tanod.dev
  baseurl_source: declared
  description: dnspeek, the domain, email and IP lookups. Domain inspection (DNS, SPF/DMARC/DKIM/MTA-STS, TLS cert), RDAP (whois) registration lookup for a domain, IP or AS number, DNS-only email address verificatio
  name: tanod-dev Dnspeek API
  slug: tanod-dev-dnspeek-api
- baseURL: https://text.tanod.dev
  baseurl_source: declared
  description: 'findpeek, the web search. Pay-per-call web search over an independent index (Mojeek): title, URL and snippet per result. Results are third-party web content, treated as untrusted.'
  name: tanod-dev Findpeek API
  slug: tanod-dev-findpeek-api
- baseURL: https://images.tanod.dev
  baseurl_source: declared
  description: imagepeek, the image toolkit. Resize, convert (PNG, JPEG, WebP, GIF, TIFF, BMP, ICO, AVIF), compress, crop, rotate, thumbnail, read or strip metadata (EXIF, GPS, XMP, IPTC), watermark, dominant colour
  name: tanod-dev Imagepeek API
  slug: tanod-dev-imagepeek-api
- baseURL: https://ml.tanod.dev
  baseurl_source: declared
  description: mlpeek, the local ML inference. Text embeddings (English or multilingual, 384 dimensions), multimodal embeddings (texts and images in one 768-dimension space, EmbeddingGemma 2), reranking, semantic si
  name: tanod-dev Mlpeek API
  slug: tanod-dev-mlpeek-api
- baseURL: https://security.tanod.dev
  baseurl_source: declared
  description: pactlint, the contract scan. Static security analysis of Solidity source or a verified contract on Ethereum or Base.
  name: tanod-dev Pactlint API
  slug: tanod-dev-pactlint-api
- baseURL: https://docs.tanod.dev
  baseurl_source: declared
  description: pdfpeek, the PDF toolkit. Merge, split, extract or remove pages, rotate, compress, convert pages to images and images to PDF, watermark, number pages, password-protect or unlock, read or edit metadata
  name: tanod-dev Pdfpeek API
  slug: tanod-dev-pdfpeek-api
- baseURL: https://agents.tanod.dev
  baseurl_source: declared
  description: sitepeek, the web page, document reader. Fetch a public web page to clean Markdown (static or JS-rendered) or a PNG screenshot, extract the text of a PDF, read a page's metadata (title, Open Graph, fe
  name: tanod-dev Sitepeek API
  slug: tanod-dev-sitepeek-api
- baseURL: https://sky.tanod.dev
  baseurl_source: declared
  description: skypeek, the aviation and space data. Aviation weather (METAR and TAF, raw and decoded), airport lookup and great-circle distances, space weather, aurora nowcasts, asteroid close approaches, sun and m
  name: tanod-dev Skypeek API
  slug: tanod-dev-skypeek-api
- baseURL: https://agents.tanod.dev
  baseurl_source: declared
  description: toolsniff, the skill, MCP server scanner. Static security scan of an AI-agent skill or MCP server package before it is installed.
  name: tanod-dev Toolsniff API
  slug: tanod-dev-toolsniff-api
- baseURL: https://chain.tanod.dev
  baseurl_source: declared
  description: txpeek, the pre-transaction check. Risk verdict for an address in about a second, before an agent sends a transaction, approves or buys.
  name: tanod-dev Txpeek API
  slug: tanod-dev-txpeek-api
- baseURL: https://finance.tanod.dev
  baseurl_source: declared
  description: 'utilpeek, the data and text utilities. Everyday deterministic utilities: ECB foreign-exchange reference rates, SEC EDGAR company lookups (profile, latest filings, headline financials), the US Treasury'
  name: tanod-dev Utilpeek API
  slug: tanod-dev-utilpeek-api
- baseURL: https://sky.tanod.dev
  baseurl_source: declared
  description: 'weatherpeek, the weather forecast. Hourly weather forecast (up to 48 h) for coordinates or a city name: temperature, humidity, wind, cloud, precipitation. Data: MET Norway (CC BY 4.0) and GeoNames (CC'
  name: tanod-dev Weatherpeek API
  slug: tanod-dev-weatherpeek-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/tanod-dev/agentic-access/tanod-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tanod-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/tanod-dev/rules/tanod-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/tanod-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/tanod-dev/vocabulary/tanod-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tanod-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tanod-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/tanod-dev/changelog/tanod-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tanod-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/tanod-dev/security/tanod-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tanod-dev-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/tanod-dev/errors/tanod-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tanod-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tanod-dev/conformance/tanod-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tanod-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tanod-dev/llms/tanod-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tanod-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/tanod-dev/mcp/tanod-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tanod-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tanod-dev/mcp/tanod-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tanod-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/tanod-dev/well-known/tanod-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tanod-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/tanod-dev/well-known/tanod-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tanod-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/tanod-dev/hosts/tanod-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tanod-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/tanod-dev/vendors/tanod-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tanod-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/tanod-dev/packages/tanod-dev-packages.yml
  title: ''
  type: Packages
  url: packages/tanod-dev-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tanod.dev/status
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tanod-labs/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://tanod.dev/changelog/
- group: auth
  href: https://artifacts.apis.io/tanod-dev/security/tanod-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tanod-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tanod-dev/security/tanod-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tanod-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tanod.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tanod.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://tanod.dev/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://tanod.dev/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tanod
- group: commercial
  title: ''
  type: Pricing
  url: https://tanod.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tanod.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tanod.dev/privacy/
created: '2026-10-29'
description: Tanod provides a pay‑per‑call MCP server and HTTP API offering over 300 tools for AI agents, including security checks, market data, aviation information, document conversion, and more. It operates without signup, offering a free daily tier and paid usage via USDC on multiple blockchains. The service is run by an AI and aims to simplify integration of diverse data and utilities for developers.
image: https://tanod.dev/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at tanod.dev.
  name: tanod-dev MCP Server
  slug: tanod-dev-mcp-yml
modified: '2026-10-29'
name: tanod-dev
nav: Providers
network: true
overview: 'tanod-dev publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agentscan API, Chainpeek API, Dnspeek API, and 11 more. Tagged areas include AI, MCP, Tools, Finance, and Monitoring.


  The tanod-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  tanod-dev''s developer surface includes changelog, documentation, API reference, support, pricing, and 24 more developer resources.'
plans:
- name: Tanod Dev Plans Pricing
  plan_count: 0
  slug: tanod-dev-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Tanod Dev Rate Limits
  slug: tanod-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: tanod-dev API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: tanod-dev-rules
scopes:
- name: Tanod Dev Scopes
  scope_count: 0
  slug: tanod-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 49.6
    developer_ergonomics: 35.0
    discoverability: 70.0
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
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
  name: Tanod Dev Authentication
  slug: tanod-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tanod Dev Domain Security
  slug: tanod-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tanod Dev Vulnerability Disclosure
  slug: tanod-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: pdf-processing
  slug: tanod-dev-pdf-processing
slug: tanod-dev
tags:
- AI
- MCP
- Tools
- Finance
- Monitoring
website: https://tanod.dev/
---
