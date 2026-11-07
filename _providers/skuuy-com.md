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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for skuuy.com utilities.
  name: skuuy API
  slug: skuuy-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/skuuy-com/llms/skuuy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skuuy-com-llms.txt
- group: build
  href: https://artifacts.apis.io/skuuy-com/mcp/skuuy-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/skuuy-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/skuuy-com/mcp/skuuy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/skuuy-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/skuuy-com/hosts/skuuy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skuuy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/skuuy-com/vendors/skuuy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skuuy-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/skuuy-com/security/skuuy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skuuy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skuuy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://skuuy.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://apis.skuuy.com
- group: start
  title: ''
  type: GettingStarted
  url: https://skuuy.com/tools
- group: operate
  title: ''
  type: Support
  url: https://skuuy.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skuuy.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skuuy.com/terms-of-service
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on the API host.
  evidence:
  - status: 404
    url: https://apis.skuuy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Skuuy.com provides a free, open-source suite of privacy, security, and developer utilities. It offers client‑side tools such as IP geolocation, WebRTC leak detection, zero‑knowledge TOTP two‑factor authentication, disposable temporary email routing, global proxy inspection, DNS benchmarking, port vulnerability auditing, and real‑time public API exploration. All tools run in the browser without sending data to a server, emphasizing zero‑log and zero‑knowledge principles.
image: https://skuuy.com/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.skuuy.com.
  name: skuuy-com MCP Server
  slug: skuuy-com-mcp-yml
modified: '2026-10-31'
name: skuuy-com
nav: Providers
network: true
overview: 'skuuy-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Security, Developer Tools, and Open Source.


  skuuy-com''s developer surface includes documentation, API reference, getting-started guide, support, and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 16.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skuuy-com/skuuy-com-2026-11-03T143311.png
security:
- kind: domain-security
  name: Skuuy Com Domain Security
  slug: skuuy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: skuuy-com
tags:
- Company
- Privacy
- Security
- Developer Tools
- Open Source
website: https://skuuy.com/
---
