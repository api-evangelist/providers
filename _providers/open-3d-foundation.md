---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: Programmatic access to O3DE engine APIs, 3D rendering tools, and game development resources.
  name: Open 3D Foundation API
  slug: open-3d-foundation-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-3d-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-3d-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/o3de
- group: docs
  title: ''
  type: Documentation
  url: https://www.o3de.org/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/o3de
- group: company
  title: ''
  type: Blog
  url: https://o3de.org/news-blogs/feed/
created: '2026-03-16'
description: The Open 3D Foundation is a Linux Foundation project supporting the Open 3D Engine (O3DE), an open source, real-time 3D engine for building games, simulations, and other 3D applications. With Microsoft as a premier member, it provides a modular, cross-platform engine with advanced rendering capabilities.
finops:
- name: Open 3D Foundation Finops
  service_category: API
  slug: open-3d-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-3d-foundation.png
layout: provider
modified: '2026-04-28'
name: Open 3D Foundation
nav: Providers
network: true
overview: 'Open 3D Foundation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Engine, Gaming, Linux Foundation, and Simulation.


  Open 3D Foundation''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Open 3D Foundation Plans Pricing
  plan_count: 3
  slug: open-3d-foundation-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Open 3D Foundation Rate Limits
  slug: open-3d-foundation-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-3d-foundation/refs/heads/main/screenshots/open-3d-foundation-2026-06-20T190730.png
security:
- kind: domain-security
  name: Open 3D Foundation Domain Security
  slug: open-3d-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Open 3D Foundation Vulnerability Disclosure
  slug: open-3d-foundation-vulnerability-disclosure
  summary_line: disclosure policy published
slug: open-3d-foundation
tags:
- 3D Engine
- Gaming
- Linux Foundation
- Simulation
---
