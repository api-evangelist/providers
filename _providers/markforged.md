---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Markforged Agentic Access
  operation_count: 30
  slug: markforged-agentic-access
  summary_line: 30 operations · 9 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Secure, licensed distribution of manufacturer-certified parts for distributed (point-of-need) manufacturing. Built on the Markforged platform (ISO 27001 certified); no separate public developer API is
  name: Markforged Digital Source
  slug: digital-source
- description: The Builds API from Markforged — 5 operation(s) for builds.
  name: Markforged Builds API
  slug: markforged-builds-api
- description: The Devices API from Markforged — 4 operation(s) for devices.
  name: Markforged Devices API
  slug: markforged-devices-api
- description: The Organizations API from Markforged — 3 operation(s) for organizations.
  name: Markforged Organizations API
  slug: markforged-organizations-api
- description: The Parts API from Markforged — 6 operation(s) for parts.
  name: Markforged Parts API
  slug: markforged-parts-api
- description: The Print Jobs API from Markforged — 3 operation(s) for print jobs.
  name: Markforged Print Jobs API
  slug: markforged-print-jobs-api
- description: The Printed Parts API from Markforged — 3 operation(s) for printed parts.
  name: Markforged Printed Parts API
  slug: markforged-printed-parts-api
artifact_total: 14
collections:
- collection_type: open
  name: Eiger API V3
  slug: open-markforged
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/markforged-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/markforged-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/markforged-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarkForged
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/markforged
- group: company
  title: ''
  type: Website
  url: https://markforged.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.eiger.io/developer
- group: commercial
  title: ''
  type: Plans
  url: plans/markforged-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/markforged-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/markforged-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://markforged.com/resources/blog
created: '2026-06-20'
description: Markforged builds industrial additive manufacturing systems - composite (FX, Onyx, X-series) and metal (Metal X, PX100) 3D printers - managed through the Eiger cloud software platform. The Eiger API (V3) exposes a REST interface over HTTP Basic Auth for managing devices, builds, print jobs, and parts, letting customers integrate Markforged additive workflows into ERP, MES, PLM, and other factory systems. Digital Source extends the platform with secure, licensed distribution of manufacturer-certified parts for distributed manufacturing.
finops:
- name: Markforged Finops
  service_category: Manufacturing and Additive Manufacturing
  slug: markforged-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/markforged.png
layout: provider
modified: '2026-06-20'
name: Markforged
nav: Providers
network: true
overview: 'Markforged publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Devices API, Organizations API, and 3 more. Tagged areas include 3D Printing, Additive Manufacturing, Industrial, Eiger, and Fleet Management.


  Markforged''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Markforged Plans Pricing
  plan_count: 4
  slug: markforged-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Markforged Rate Limits
  slug: markforged-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/markforged/refs/heads/main/screenshots/markforged-2026-06-20T184959.png
security:
- kind: authentication
  name: Markforged Authentication
  slug: markforged-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Markforged Domain Security
  slug: markforged-domain-security
  summary_line: TLSv1.3 · DMARC
slug: markforged
tags:
- 3D Printing
- Additive Manufacturing
- Industrial
- Eiger
- Fleet Management
website: https://markforged.com
---
