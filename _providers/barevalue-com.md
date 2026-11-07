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
api_count: 1
apis:
- description: AI podcast editing API providing endpoints for health, pricing, status, account management, orders and webhooks.
  name: Barevalue API
  slug: barevalue-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/barevalue-com/plans/barevalue-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/barevalue-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/barevalue-com/conformance/barevalue-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/barevalue-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/barevalue-com/llms/barevalue-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barevalue-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/barevalue-com/mcp/barevalue-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/barevalue-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/barevalue-com/well-known/barevalue-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barevalue-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/barevalue-com/hosts/barevalue-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barevalue-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/barevalue-com/packages/barevalue-com-packages.yml
  title: ''
  type: SDKs
  url: packages/barevalue-com-packages.yml
- group: build
  href: https://artifacts.apis.io/barevalue-com/packages/barevalue-com-packages.yml
  title: ''
  type: Packages
  url: packages/barevalue-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://barevalue.com/login
- group: auth
  href: https://artifacts.apis.io/barevalue-com/security/barevalue-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barevalue-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barevalue.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://barevalue.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://barevalue.com/docs/api-v1
- group: docs
  title: ''
  type: APIReference
  url: https://barevalue.com/docs/api-v1
- group: start
  title: ''
  type: GettingStarted
  url: https://barevalue.com/docs/api-v1#getting-started
- group: operate
  title: ''
  type: Support
  url: https://barevalue.com/contact
- group: company
  title: ''
  type: Blog
  url: https://barevalue.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://barevalue.com/podcasting-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://barevalue.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barevalue.com/privacy-policy
created: '2026-11-02'
description: Barevalue provides professional post‑production services for podcasts and video, offering both human‑expert and AI‑powered editing on a pay‑as‑you‑go model. Founded in 2018, the company serves over 10,000 creators, delivering fast turnaround and high‑quality results. Their platform includes a public API and MCP for developers to integrate editing workflows, retrieve pricing, and manage jobs programmatically.
image: https://d2v6enl7cgqjr1.cloudfront.net/images/logo-black.png
layout: provider
mcp_servers:
- description: Remote MCP server at barevalue.com.
  name: Barevalue MCP Server
  slug: barevalue-com-mcp-yml
modified: '2026-11-02'
name: Barevalue
nav: Providers
network: true
overview: 'Barevalue publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Video, Podcasts, Editing, and Artificial Intelligence.


  Barevalue''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Barevalue Com Plans Pricing
  plan_count: 5
  slug: barevalue-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barevalue Com Domain Security
  slug: barevalue-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barevalue-com
tags:
- Audio
- Video
- Podcasts
- Editing
- Artificial Intelligence
website: https://barevalue.com/
---
