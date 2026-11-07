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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/8b-com/plans/8b-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/8b-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/8b-com/llms/8b-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/8b-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/8b-com/mcp/8b-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/8b-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/8b-com/hosts/8b-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/8b-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/8b-com/vendors/8b-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/8b-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://8b.com/tos.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://8b.com/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://8b.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.8b.com/start/
- group: docs
  title: ''
  type: Documentation
  url: https://help.8b.com/
- group: auth
  href: https://artifacts.apis.io/8b-com/security/8b-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/8b-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://8b.com/
coverage:
  checked: '2026-10-31'
  detail: 8B provides a website builder with no public API documented.
  evidence:
  - status: 200
    url: https://help.8b.com/start/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: 8B provides a free website builder that requires no sign‑up, allowing users to create real websites from a single sentence. The platform offers an easy‑to‑use interface, multilingual support, and a variety of themes, all hosted on a fast CDN. It targets individuals and small businesses seeking a quick online presence without the hassle of accounts or templates, emphasizing privacy and simplicity.
image: https://8b.com/demos/shots/design-studio.webp
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.8b.com.
  name: 8B MCP Server
  slug: 8b-com-mcp-yml
modified: '2026-10-31'
name: 8B
nav: Providers
network: true
overview: '8B is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Website Builder, Free, and Small Business.


  8B''s developer surface includes pricing, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: 8B Com Plans Pricing
  plan_count: 2
  slug: 8b-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 40.0
    operational_transparency: 0.0
  previous_composite: 19.4
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
security:
- kind: domain-security
  name: 8B Com Domain Security
  slug: 8b-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 8b-com
tags:
- Company
- Website Builder
- Free
- Small Business
website: https://8b.com/
---
