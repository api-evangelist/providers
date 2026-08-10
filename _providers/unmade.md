---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: The Design API API from Unmade — 9 operation(s) for design api.
  name: Unmade Design API API
  slug: unmade-design-api-api
- description: The Ecommerce Orders API API from Unmade — 12 operation(s) for ecommerce orders api.
  name: Unmade Ecommerce Orders API API
  slug: unmade-ecommerce-orders-api-api
- description: The Factory API API from Unmade — 15 operation(s) for factory api.
  name: Unmade Factory API API
  slug: unmade-factory-api-api
- description: The Outfit API API from Unmade — 5 operation(s) for outfit api.
  name: Unmade Outfit API API
  slug: unmade-outfit-api-api
- description: The Transfer Preview API API from Unmade — 2 operation(s) for transfer preview api.
  name: Unmade Transfer Preview API API
  slug: unmade-transfer-preview-api-api
- description: The Unmade Editor API from Unmade — 2 operation(s) for unmade editor.
  name: Unmade Unmade Editor API
  slug: unmade-unmade-editor-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://unmade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://engineering.unmade.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://engineering.unmade.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://engineering.unmade.com/api-docs/#/group-integrating-with-unmade
- group: company
  title: ''
  type: Blog
  url: https://engineering.unmade.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unmadeworks
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unmade.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/unmade-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unmade-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unmade-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unmade-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unmade-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unmade-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unmade-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unmade-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unmade-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/unmade-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unmade-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/unmade-embed-v2-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unmade-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unmade is a London fashion-tech company whose UnmadeOS platform lets apparel and sportswear brands such as New Balance and Rapha sell customised, on-demand products at scale. Its partner Integration API embeds the Unmade Editor in e-commerce product pages, captures saved designs, renders previews and 3D views, creates ecommerce orders from design IDs, and drives factory production workflows through to shipping. Founded in 2013 and Techstars-backed, Unmade was acquired by garment manufacturer Hi-Tech Apparel in July 2024.
image: https://github.com/unmadeworks.png
layout: provider
mcp_servers:
- description: ''
  name: unmade-mcp.yml
  slug: unmade-mcpyml
modified: '2026-07-21'
name: Unmade
nav: Providers
network: true
overview: 'Unmade publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Design API API, Ecommerce Orders API API, Factory API API, and 3 more. Tagged areas include Fashion, Apparel, Manufacturing, Customization, and eCommerce.


  Unmade''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 16 more developer resources.'
random_paper: 54
rate_limits:
- limit_count: 0
  name: Unmade Rate Limits
  slug: unmade-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 59.3
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Unmade Authentication
  slug: unmade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unmade Domain Security
  slug: unmade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unmade
tags:
- Fashion
- Apparel
- Manufacturing
- Customization
- eCommerce
- On-Demand Production
- Embedded Commerce
website: https://unmade.com/
---
