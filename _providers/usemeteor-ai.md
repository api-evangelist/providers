---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/usemeteor-ai/plans/usemeteor-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usemeteor-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/usemeteor-ai/llms/usemeteor-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usemeteor-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/usemeteor-ai/mcp/usemeteor-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usemeteor-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/usemeteor-ai/well-known/usemeteor-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usemeteor-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/usemeteor-ai/hosts/usemeteor-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usemeteor-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/usemeteor-ai/vendors/usemeteor-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usemeteor-ai-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://usemeteor.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://usemeteor.ai/signin
- group: auth
  href: https://artifacts.apis.io/usemeteor-ai/security/usemeteor-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usemeteor-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usemeteor.ai
- group: docs
  title: ''
  type: Documentation
  url: https://usemeteor.ai/connect
- group: company
  title: ''
  type: Blog
  url: https://usemeteor.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usemeteor.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usemeteor.ai/terms
coverage:
  checked: '2026-10-18'
  detail: The provider's documentation at /connect is HTML without a machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://usemeteor.ai/connect
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Meteor (usemeteor.ai) provides an AI-driven job application platform that automatically matches users with relevant job openings, tailors resumes, and submits applications through supported job portals. Leveraging large language models, it streamlines the job search process for immigrants and international students, offering a free tier and paid credits for advanced features.
image: https://usemeteor.ai/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at usemeteor.ai requiring OAuth.
  name: Meteor (usemeteor.ai) MCP Server
  slug: usemeteor-ai-mcp-yml
modified: '2026-10-17'
name: Meteor (usemeteor.ai)
nav: Providers
network: true
overview: 'Meteor (usemeteor.ai) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Job Search, Automation, Immigration, and Resume.


  Meteor (usemeteor.ai)''s developer surface includes pricing, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Usemeteor Ai Plans Pricing
  plan_count: 1
  slug: usemeteor-ai-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 20.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usemeteor Ai Domain Security
  slug: usemeteor-ai-domain-security
  summary_line: TLSv1.3
slug: usemeteor-ai
tags:
- Artificial Intelligence
- Job Search
- Automation
- Immigration
- Resume
- Company
website: https://usemeteor.ai
---
