---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/polopan-com/plans/polopan-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/polopan-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/polopan-com/llms/polopan-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/polopan-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/polopan-com/mcp/polopan-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/polopan-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/polopan-com/hosts/polopan-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polopan-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://polopan.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://polopan.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://polopan.com/pricing/
- group: auth
  href: https://artifacts.apis.io/polopan-com/security/polopan-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polopan-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polopan.com/
coverage:
  checked: '2026-10-30'
  detail: Polopan offers a consumer AI styling service but provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://polopan.com/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: Polopan offers a free AI-powered personal stylist platform that curates a discovery-first fashion experience. Leveraging advanced machine learning, the service provides users with a personalized feed of clothing recommendations, helping them discover items they want to wear before they even know what to search for. The platform aims to democratize fashion advice, making AI-driven styling accessible to everyone, and integrates with e‑commerce partners to facilitate seamless shopping.
image: https://polopan.com/wp-content/uploads/2025/11/cropped-logo1024.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp-server.polopan.com.
  name: polopan-com MCP Server
  slug: polopan-com-mcp-yml
modified: '2026-10-30'
name: polopan-com
nav: Providers
network: true
overview: 'polopan-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Fashion, PersonalStylist, and E-commerce.


  polopan-com''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Polopan Com Plans Pricing
  plan_count: 2
  slug: polopan-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Polopan Com Rate Limits
  slug: polopan-com-rate-limits
scopes:
- name: Polopan Com Scopes
  scope_count: 0
  slug: polopan-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Polopan Com Authentication
  slug: polopan-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Polopan Com Domain Security
  slug: polopan-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: polopan-com
tags:
- Company
- AI
- Fashion
- PersonalStylist
- E-commerce
website: https://polopan.com/
---
