---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Delos Agentic Access
  operation_count: 39
  slug: delos-agentic-access
  summary_line: 39 operations · 23 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The actions API from Delos — 1 operation(s) for actions.
  name: Delos Actions API
  slug: delos-actions-api
- description: The admin/installations API from Delos — 3 operation(s) for admin/installations.
  name: Delos Admin/installations API
  slug: delos-admin-installations-api
- description: The admin/products API from Delos — 3 operation(s) for admin/products.
  name: Delos Admin/products API
  slug: delos-admin-products-api
- description: The admin/products-bundles API from Delos — 1 operation(s) for admin/products-bundles.
  name: Delos Admin/products Bundles API
  slug: delos-admin-products-bundles-api
- description: The admin/users API from Delos — 4 operation(s) for admin/users.
  name: Delos Admin/users API
  slug: delos-admin-users-api
- description: The global API from Delos — 3 operation(s) for global.
  name: Delos Global API
  slug: delos-global-api
- description: The installations API from Delos — 1 operation(s) for installations.
  name: Delos Installations API
  slug: delos-installations-api
- description: The local-accounts API from Delos — 6 operation(s) for local-accounts.
  name: Delos Local Accounts API
  slug: delos-local-accounts-api
- description: The products API from Delos — 1 operation(s) for products.
  name: Delos Products API
  slug: delos-products-api
- description: The sessions API from Delos — 4 operation(s) for sessions.
  name: Delos Sessions API
  slug: delos-sessions-api
- description: The users API from Delos — 6 operation(s) for users.
  name: Delos Users API
  slug: delos-users-api
artifact_total: 19
asyncapis:
- description: ''
  name: Delos Events
  slug: delos-events
collections:
- collection_type: open
  name: Cloud BE
  slug: open-delos-wellcube-cloud-be
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/delos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delos.com/
- group: company
  title: ''
  type: Website
  url: https://wellcube.io/
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.wellcube.io/api/v1/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.wellcube.io/api/v1/docs/
- group: operate
  title: ''
  type: Support
  url: https://support.wellcube.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://delos.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Delos-tech
- group: start
  title: ''
  type: Login
  url: https://app.wellcube.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wellcube.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wellcube.io/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/delos-wellcube-cloud-be-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/delos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/delos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/delos-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/delos-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/delos-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/delos-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/delos-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/delos-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/delos-wellcube-cloud-be-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/delos-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/delos-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/delos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/delos-rate-limits.yml
created: '2026-08-12'
description: Delos Living LLC is a New York-based wellness real estate and technology company that applies building science and evidence-based research to indoor environments across commercial, residential, hospitality, education, senior living and transportation. Delos is the founder of the WELL Building Standard (now administered by the International WELL Building Institute) and co-founder of the Well Living Lab with Mayo Clinic. Its product line spans Intellipure advanced air purification, indoor environmental quality (IEQ) sensing, the Stay Well hospitality program, and WellCube — a connected system of localized air purifiers and multi-sensor devices for the modern office, backed by the "Cloud BE" / Darwin Cloud platform that handles installations, products, device actions and account federation.
image: https://a-us.storyblok.com/f/1016757/200x62/8b73c5475d/logo_delos_layer_1.svg
layout: provider
mcp_servers:
- description: ''
  name: Delos MCP Server
  slug: delos-mcp-server
modified: '2026-08-12'
name: Delos
nav: Providers
network: true
overview: 'Delos publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Admin/installations API, Admin/products API, and 8 more. Tagged areas include wellness-real-estate, indoor-air-quality, indoor-environmental-quality, iot, and smart-buildings.


  The Delos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Delos'' developer surface includes documentation, API reference, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Delos Plans Pricing
  plan_count: 0
  slug: delos-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Delos Rate Limits
  slug: delos-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delos/refs/heads/main/screenshots/delos-2026-08-17T080906.png
security:
- kind: authentication
  name: Delos Authentication
  slug: delos-authentication
  summary_line: apiKey/openIdConnect · 1 scheme
- kind: domain-security
  name: Delos Domain Security
  slug: delos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: delos
tags:
- wellness-real-estate
- indoor-air-quality
- indoor-environmental-quality
- iot
- smart-buildings
- building-automation
- air-purification
- environmental-sensors
- commercial-real-estate
- healthy-buildings
- hospitality
- ESG
website: https://delos.com/
---
