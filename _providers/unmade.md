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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-01'
api_count: 2
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unmade Integration Reference Design API API
  slug: open-unmade-design-api-api
- collection_type: open
  name: Unmade Integration Reference Design API Ecommerce Orders API API
  slug: open-unmade-ecommerce-orders-api-api
- collection_type: open
  name: Unmade Integration Reference Design API Factory API API
  slug: open-unmade-factory-api-api
- collection_type: open
  name: Unmade Integration Reference Design API Outfit API API
  slug: open-unmade-outfit-api-api
- collection_type: open
  name: Unmade Integration Reference Design API Unmade Editor API
  slug: open-unmade-unmade-editor-api
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
  name: Unmade MCP Server
  slug: unmade-mcp-server
modified: '2026-07-21'
name: Unmade
nav: Providers
network: true
overview: 'Unmade publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Design API API, Ecommerce Orders API API, Factory API API, and 3 more. Tagged areas include Fashion, Apparel, Manufacturing, Customization, and E-Commerce.


  Unmade''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 16 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Unmade Rate Limits
  slug: unmade-rate-limits
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 12.2
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 22.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- E-Commerce
- On-Demand Production
- Embedded Commerce
website: https://unmade.com/
---
