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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Free MCP server providing deposit‑insurance limits. Endpoint: https://bankrolled.ai/mcp'
  name: Bankrolled AI MCP
  slug: bankrolled-ai-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bankrolled-ai/llms/bankrolled-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankrolled-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bankrolled-ai/mcp/bankrolled-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bankrolled-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bankrolled-ai/well-known/bankrolled-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankrolled-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bankrolled-ai/hosts/bankrolled-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankrolled-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bankrolled-ai/vendors/bankrolled-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankrolled-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bankrolled-ai/security/bankrolled-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankrolled-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankrolled.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bankrolled.ai/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://bankrolled.ai/wp-json/bankrolled-ai/v1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bankrolled.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bankrolled.ai/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/Bankrolled/bankrolled-ai-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bankrolled
created: '2026-11-02'
description: Bankrolled.ai provides a free, regulator‑sourced API hub for AI agents to access deposit‑insurance limits, savings, retirement and related financial limits across multiple jurisdictions. It offers a Machine‑Callable Protocol (MCP) endpoint and a REST API that return up‑to‑date limits with citations to official regulator sources. The service is open, requires no API key, and includes tools for money‑fact queries, scheme lookups, cross‑border checks, and pricing lists. Documentation is available via llms.txt and a GitHub docs repository.
image: https://bankrolled.ai/wp-content/uploads/2026/08/cropped-mark-cropped-192x192.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at bankrolled.ai.
  name: Bankrolled.ai MCP Server
  slug: bankrolled-ai-mcp-yml
modified: '2026-11-02'
name: Bankrolled.ai
nav: Providers
network: true
overview: 'Bankrolled.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, Deposit-Insurance, Agents, and Regulatory.


  Bankrolled.ai''s developer surface includes documentation, API reference, and 11 more developer resources.'
plans:
- name: Bankrolled Ai Plans Pricing
  plan_count: 0
  slug: bankrolled-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Bankrolled Ai Rate Limits
  slug: bankrolled-ai-rate-limits
scopes:
- name: Bankrolled Ai Scopes
  scope_count: 0
  slug: bankrolled-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 18.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bankrolled Ai Authentication
  slug: bankrolled-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bankrolled Ai Domain Security
  slug: bankrolled-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bankrolled-ai
tags:
- Finance
- Artificial Intelligence
- Deposit-Insurance
- Agents
- Regulatory
website: https://bankrolled.ai/
---
