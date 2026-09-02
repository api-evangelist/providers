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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ready-robotics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ready-robotics
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ready-robotics-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ready-robotics-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ready-robotics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ready-robotics-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ready-robotics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ready-robotics-plans-pricing.yml
coverage:
  checked: '2026-08-26'
  detail: READY Robotics ceased operations in August 2024 and withdrew every developer host from DNS — developer.ready-robotics.com, which carried the Forge Edge REST API reference and its OpenAPI description, is NXDOMAIN, as are docs., market., portal. and support.ready-robotics.com, leaving only a Cloudflare-challenged marketing site and the intact GitHub organization.
  evidence:
  - status: 0
    url: https://developer.ready-robotics.com/
  - status: 0
    url: https://docs.ready-robotics.com/
  - status: 403
    url: https://www.ready-robotics.com/
  - status: 200
    url: https://github.com/ready-robotics
  reason: defunct
  state: none
created: '2026-08-26'
description: READY Robotics was a Columbus, Ohio industrial-automation software company, founded in 2016 out of Johns Hopkins University, that built Forge/OS — a universal operating system for industrial robots. Forge/OS presented one low-code programming and control surface across hundreds of robot models from ABB, Epson, FANUC, Kawasaki, Stäubli, Universal Robots and Yaskawa, and its Forge Edge product advertised a REST API with an OpenAPI/Swagger description plus client tooling for Python, JavaScript and C++, alongside the RAL2 (Robot Abstraction Layer 2) C++/Qt plugin interface used to write new robot drivers. The company ceased operations in August 2024 after a funding round collapsed, and its assets were liquidated through an assignment for the benefit of creditors. Every developer-facing host it operated — developer., docs., portal., market. and support.ready-robotics.com — no longer resolves in DNS, so no live machine-readable contract remains. What survives publicly is the marketing
  site behind a Cloudflare challenge and the GitHub organization, which still carries the RAL2 sample driver and the vendored C++ dependencies Forge/OS was built on.
layout: provider
modified: '2026-08-26'
name: Ready Robotics
nav: Providers
network: true
overview: Ready Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Industrial Automation, Manufacturing, Operating Systems, and Industrial IoT.
plans:
- name: Ready Robotics Plans Pricing
  plan_count: 0
  slug: ready-robotics-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Ready Robotics Rate Limits
  slug: ready-robotics-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Ready Robotics Domain Security
  slug: ready-robotics-domain-security
  summary_line: TLSv1.3
slug: ready-robotics
tags:
- Robotics
- Industrial Automation
- Manufacturing
- Operating Systems
- Industrial IoT
- Robot Operating System
- Defunct
- Company
website: https://www.ready-robotics.com/
---
