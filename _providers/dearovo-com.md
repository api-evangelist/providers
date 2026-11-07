---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 1
apis:
- description: Dearovo provides a developer guide at https://www.dearovo.com/guides/.
  name: Dearovo API
  slug: dearovo-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dearovo-com/plans/dearovo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dearovo-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dearovo-com/llms/dearovo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dearovo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dearovo-com/mcp/dearovo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dearovo-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dearovo-com/hosts/dearovo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dearovo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dearovo-com/vendors/dearovo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dearovo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dearovo.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dearovo.com/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dearovo.com/pricing.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.dearovo.com/guides/
- group: auth
  href: https://artifacts.apis.io/dearovo-com/security/dearovo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dearovo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dearovo.com/
created: '2026-11-05'
description: 'dearovo-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://www.dearovo.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at dearovo.com.
  name: dearovo-com MCP Server
  slug: dearovo-com-mcp-yml
modified: '2026-11-05'
name: dearovo-com
nav: Providers
network: true
overview: 'dearovo-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Romance and Relationship.


  dearovo-com''s developer surface includes pricing, documentation, and 9 more developer resources.'
plans:
- name: Dearovo Com Plans Pricing
  plan_count: 2
  slug: dearovo-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dearovo Com Domain Security
  slug: dearovo-com-domain-security
  summary_line: TLSv1.3
slug: dearovo-com
tags:
- Romance
- Relationship
website: https://dearovo.com/
---
