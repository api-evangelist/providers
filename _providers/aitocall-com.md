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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for integrating AI‑driven telephony via Aitocall, documented at the developer portal.
  name: Aitocall API
  slug: aitocall-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/aitocall-com/llms/aitocall-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aitocall-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aitocall-com/mcp/aitocall-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aitocall-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aitocall-com/well-known/aitocall-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aitocall-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aitocall-com/hosts/aitocall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aitocall-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aitocall-com/vendors/aitocall-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aitocall-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aitocall-com/security/aitocall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitocall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aitocall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aitocall.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aitocall.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aitocall.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://www.aitocall.com/#faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aitocall.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aitocall.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Documentation is publicly accessible but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://www.aitocall.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Aitocall is an AI‑powered telephony service that enables users to place phone calls simply by speaking to large language models such as Claude or ChatGPT. By connecting these AI chat agents to a telephone gateway, Aitocall translates spoken prompts into calls, records conversations, summarizes them, and provides call logs. The platform offers a web interface with pricing tiers, FAQs, and documentation for developers to integrate voice calling into AI applications. It targets Korean users but is accessible globally.
image: https://www.aitocall.com/brand/aitocall-wordmark-light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.aitocall.com.
  name: Aitocall MCP Server
  slug: aitocall-com-mcp-yml
modified: '2026-11-01'
name: Aitocall
nav: Providers
network: true
overview: 'Aitocall is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Telephony, Voice, Communications, and Korean.


  Aitocall''s developer surface includes documentation, getting-started guide, pricing, support, and 9 more developer resources.'
plans:
- name: Aitocall Com Plans Pricing
  plan_count: 0
  slug: aitocall-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aitocall Com Rate Limits
  slug: aitocall-com-rate-limits
scopes:
- name: Aitocall Com Scopes
  scope_count: 0
  slug: aitocall-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aitocall Com Authentication
  slug: aitocall-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aitocall Com Domain Security
  slug: aitocall-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aitocall-com
tags:
- Artificial Intelligence
- Telephony
- Voice
- Communications
- Korean
website: https://www.aitocall.com/
---
