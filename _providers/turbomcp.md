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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Turbo MCP provides a self‑hosted Management Control Plane API. Documentation is not publicly available.
  name: Turbo MCP API
  slug: turbo-mcp-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/turbomcp/hosts/turbomcp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/turbomcp-hosts.yml
- group: auth
  href: https://artifacts.apis.io/turbomcp/security/turbomcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/turbomcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://turbomcp.ai/
- group: company
  title: ''
  type: Blog
  url: https://turbomcp.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://turbomcp.ai/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://turbomcp.ai/book-a-demo
created: '2026-10-19'
description: Turbo MCP provides a standards‑compliant, self‑hosted Management Control Plane (MCP) gateway and platform that lets enterprises connect their applications to AI on their own terms. It offers features such as OIDC‑compatible identity integration, granular audit and control, data loss prevention, and a kill‑switch for AI workloads, all deployable via a single‑container image on Kubernetes, VMs, or PaaS environments.
layout: provider
modified: '2026-10-19'
name: Turbo MCP
nav: Providers
network: true
overview: 'Turbo MCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Management, Control Plane, and Self-Hosted.


  Turbo MCP''s developer surface includes engineering blog, support, getting-started guide, and 3 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Turbomcp Domain Security
  slug: turbomcp-domain-security
  summary_line: TLSv1.3 · HSTS
slug: turbomcp
tags:
- Company
- Artificial Intelligence
- Management
- Control Plane
- Self-Hosted
website: https://turbomcp.ai/
---
