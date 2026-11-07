---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bitcoincreditstack-com/plans/bitcoincreditstack-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bitcoincreditstack-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bitcoincreditstack-com/llms/bitcoincreditstack-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitcoincreditstack-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitcoincreditstack-com/mcp/bitcoincreditstack-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bitcoincreditstack-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/bitcoincreditstack-com/hosts/bitcoincreditstack-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcoincreditstack-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitcoincreditstack-com/vendors/bitcoincreditstack-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitcoincreditstack-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitcoincreditstack.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitcoincreditstack.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bitcoincreditstack.com/legal/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.bitcoincreditstack.com/news
- group: auth
  href: https://artifacts.apis.io/bitcoincreditstack-com/security/bitcoincreditstack-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcoincreditstack-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitcoincreditstack.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL spec found on any discovered host.
  evidence:
  - status: 404
    url: https://www.bitcoincreditstack.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'bitcoincreditstack-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bitcoincreditstack.com.
  name: Aletheia Analytics SASU MCP Server
  slug: bitcoincreditstack-com-mcp-yml
modified: '2026-11-02'
name: Aletheia Analytics SASU
nav: Providers
network: true
overview: 'Aletheia Analytics SASU is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Aletheia Analytics SASU''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Bitcoincreditstack Com Plans Pricing
  plan_count: 3
  slug: bitcoincreditstack-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 12.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 29.2
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitcoincreditstack Com Domain Security
  slug: bitcoincreditstack-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bitcoincreditstack-com
tags:
- Company
website: https://bitcoincreditstack.com/
---
