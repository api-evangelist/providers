---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: AI Platform provides AI model deployment, monitoring, and management services.
  name: AI Platform
  slug: ai-platform
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bespinglobal/refs/heads/main/plans/bespinglobal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bespinglobal-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bespinglobal/refs/heads/main/mcp/bespinglobal-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bespinglobal-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bespinglobal/refs/heads/main/hosts/bespinglobal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bespinglobal-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bespinglobal/refs/heads/main/vendors/bespinglobal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bespinglobal-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://blog.bespinglobal.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.bespinglobal.com/category/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bespinglobal/refs/heads/main/security/bespinglobal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bespinglobal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bespinglobal.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bespinglobal.com/helpnow
- group: company
  title: ''
  type: Blog
  url: https://www.bespinglobal.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bespinglobal.com/helpnow
- group: operate
  title: ''
  type: Support
  url: https://www.bespinglobal.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bespinglobal.com/privacy
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API or documentation sites.
  evidence:
  - status: 0
    url: https://api.bespinglobal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bespinglobal (베스핀글로벌) is a global AI‑enabled cloud services and consulting company offering end‑to‑end AI platforms, data‑ops, cloud infrastructure, and managed services. It helps enterprises accelerate AI adoption, optimize cloud operations, and modernize digital workflows through its AI Platform, DataOps, Cloud MSP, and automation solutions.
image: https://img.bespinglobal.com/wp-content/uploads/2026/04/bespinglobal_og.jpg
layout: provider
mcp_servers:
- description: ''
  name: Bespinglobal MCP Server
  slug: bespinglobal-mcp-server
modified: '2026-09-27'
name: Bespinglobal
nav: Providers
network: true
overview: 'Bespinglobal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Artificial Intelligence, Consulting, Services, and Global.


  Bespinglobal''s developer surface includes documentation, engineering blog, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Bespinglobal Plans Pricing
  plan_count: 1
  slug: bespinglobal-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 61.7
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bespinglobal Domain Security
  slug: bespinglobal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bespinglobal
tags:
- Cloud
- Artificial Intelligence
- Consulting
- Services
- Global
website: https://www.bespinglobal.com
---
