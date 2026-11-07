---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only product catalog API compliant with ARC/1.0, exposed via the KaliCart Bridge plugin for WooCommerce.
  name: KaliCart Bridge API
  slug: kalicart-bridge-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/kalicart-com/conformance/kalicart-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kalicart-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kalicart-com/llms/kalicart-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kalicart-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/kalicart-com/mcp/kalicart-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kalicart-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/kalicart-com/hosts/kalicart-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kalicart-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/kalicart-com/security/kalicart-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kalicart-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kalicart.com/
- group: company
  title: ''
  type: Blog
  url: https://bridge.kalicart.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://bridge.kalicart.com/spec/
- group: docs
  title: ''
  type: APIReference
  url: https://bridge.kalicart.com/spec/
- group: operate
  title: ''
  type: Support
  url: https://www.kalicart.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bridge.kalicart.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kalicart.com/legal/
- group: start
  title: ''
  type: GettingStarted
  url: https://bridge.kalicart.com/
- group: start
  title: ''
  type: SignUp
  url: https://bridge.kalicart.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages exist but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://bridge.kalicart.com/spec/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: KaliCart provides an open‑agentic commerce network for WooCommerce stores, exposing product catalogs through a read‑only, ARC/1.0 compliant API. Merchants install the free KaliCart Bridge plugin to make their catalog machine‑readable, while AI agents query the federated KaliCart Global discovery service to retrieve offers without handling checkout. The platform emphasizes privacy, provenance, and UCP alignment, offering free GPL‑v2 bridge software, a specification, and MCP endpoints for AI integration.
image: https://bridge.kalicart.com/klcrt_ico.png
layout: provider
mcp_servers:
- description: Remote MCP server at global.kalicart.com.
  name: kalicart-com MCP Server
  slug: kalicart-com-mcp-yml
modified: '2026-10-30'
name: kalicart-com
nav: Providers
network: true
overview: 'kalicart-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, WooCommerce, Agentic Commerce, and Open Protocol.


  kalicart-com''s developer surface includes engineering blog, documentation, API reference, support, getting-started guide, signup flow, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kalicart-com/kalicart-com-2026-11-03T134259.png
security:
- kind: authentication
  name: Kalicart Com Authentication
  slug: kalicart-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kalicart Com Domain Security
  slug: kalicart-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kalicart-com
tags:
- Company
- E-Commerce
- WooCommerce
- Agentic Commerce
- Open Protocol
- Artificial Intelligence
website: https://www.kalicart.com/
---
