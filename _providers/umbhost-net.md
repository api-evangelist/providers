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
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 15.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'UmbHost provides a developer portal with API documentation for its hosting services. The portal lists endpoints for managing hosting, email, and DevOps resources, but no machine‑readable contract was '
  name: UmbHost API
  slug: umbhost-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/umbhost-net/plans/umbhost-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/umbhost-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/umbhost-net/llms/umbhost-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/umbhost-net-llms.txt
- group: other
  href: https://artifacts.apis.io/umbhost-net/a2a/umbhost-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/umbhost-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/umbhost-net/mcp/umbhost-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/umbhost-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/umbhost-net/well-known/umbhost-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/umbhost-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/umbhost-net/hosts/umbhost-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/umbhost-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/umbhost-net/vendors/umbhost-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/umbhost-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/umbhost-net/security/umbhost-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/umbhost-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://umbhost.net/
- group: company
  title: ''
  type: Blog
  url: https://umbhost.net/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.umbhost.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UmbHost
- group: commercial
  title: ''
  type: Pricing
  url: https://umbhost.net/gb/pricing-calculator
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://umbhost.net/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.umbhost.net
- group: commercial
  title: ''
  type: TermsOfService
  url: https://umbhost.net/legal/terms-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://umbhost.net/media/ngvg34vf/scot_terms_and_condition.pdf
coverage:
  checked: '2026-10-30'
  detail: Developer portal pages are static HTML without OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://dev.umbhost.net/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: UmbHost.net provides sustainable cloud hosting solutions, focusing on Umbraco, WordPress, and custom web applications. Their platform offers Linux and Windows servers, managed email, and DevOps services, targeting developers and enterprises seeking reliable, eco‑friendly infrastructure. The company emphasizes green data centers, automated scaling, and comprehensive support, positioning itself as a modern alternative to traditional hosting providers.
image: https://umbhost.net/media/trpayeh1/social-share.png?width=1200&height=630&v=1dc36a4c22f79e0&hmac=1d487009a3d4023bd0d40c2a29a479a6d5e81bbf0c53682f5a667ef4746f1169&bgcolor=white
layout: provider
mcp_servers:
- description: Remote MCP server at kb.umbhost.net.
  name: umbhost-net MCP Server
  slug: umbhost-net-mcp-yml
modified: '2026-10-30'
name: umbhost-net
nav: Providers
network: true
overview: 'umbhost-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Cloud, Sustainable, and DevOps.


  umbhost-net''s developer surface includes engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Umbhost Net Plans Pricing
  plan_count: 12
  slug: umbhost-net-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 67.5
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/umbhost-net/umbhost-net-2026-11-03T145420.png
security:
- kind: domain-security
  name: Umbhost Net Domain Security
  slug: umbhost-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: umbhost-net
tags:
- Company
- Hosting
- Cloud
- Sustainable
- DevOps
website: https://umbhost.net/
---
