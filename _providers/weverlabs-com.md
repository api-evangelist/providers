---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Weverlabs Com Agentic Access
  operation_count: 6
  slug: weverlabs-com-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://weverlabs.com
  baseurl_source: declared
  description: Agentic commerce and OS public API
  name: Wever Labs Agent API
  slug: wever-labs-agent-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: Security
  url: https://weverlabs.com/support/#security
- group: agent
  href: https://artifacts.apis.io/weverlabs-com/llms/weverlabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weverlabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/weverlabs-com/a2a/weverlabs-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/weverlabs-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/weverlabs-com/mcp/weverlabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/weverlabs-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/weverlabs-com/well-known/weverlabs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/weverlabs-com-security.txt
- group: agent
  href: https://artifacts.apis.io/weverlabs-com/well-known/weverlabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/weverlabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/weverlabs-com/hosts/weverlabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weverlabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/weverlabs-com/vendors/weverlabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weverlabs-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://weverlabs.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weverlabs.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://weverlabs.com/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weverlabs.com/privacy/
- group: auth
  href: https://artifacts.apis.io/weverlabs-com/security/weverlabs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/weverlabs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/weverlabs-com/security/weverlabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weverlabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weverlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://weverlabs.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://weverlabs.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://weverlabs.com/agent-integration-kit/
- group: operate
  title: ''
  type: Support
  url: https://weverlabs.com/support/
created: '2026-10-30'
description: Wever Labs is a founder‑led product company building the infrastructure for agentic work. It offers Wever Pay, an autonomous commerce exchange, and a suite of tools including Market Thesis AI, Tokenization Atlas, Agent Store, and Integration Kit, enabling humans and AI agents to discover, transact, and verify services across a unified platform.
image: https://weverlabs.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at agents.weverlabs.com.
  name: weverlabs-com MCP Server
  slug: weverlabs-com-mcp-yml
modified: '2026-10-30'
name: weverlabs-com
nav: Providers
network: true
overview: 'weverlabs-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Wever Labs Agent API. Tagged areas include Company, Artificial Intelligence, Payments, Infrastructure, and Platform.


  The weverlabs-com catalog on APIs.io includes 1 Spectral governance ruleset.


  weverlabs-com''s developer surface includes documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: weverlabs-com API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: weverlabs-com-rules
scopes:
- name: Weverlabs Com Scopes
  scope_count: 0
  slug: weverlabs-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 14.5
    contract_governance: 18.2
    contract_quality: 34.4
    developer_ergonomics: 16.7
    discoverability: 75.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/weverlabs-com/weverlabs-com-2026-11-03T150129.png
security:
- kind: authentication
  name: Weverlabs Com Authentication
  slug: weverlabs-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Weverlabs Com Domain Security
  slug: weverlabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Weverlabs Com Vulnerability Disclosure
  slug: weverlabs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: weverlabs-com
tags:
- Company
- Artificial Intelligence
- Payments
- Infrastructure
- Platform
website: https://weverlabs.com/
---
