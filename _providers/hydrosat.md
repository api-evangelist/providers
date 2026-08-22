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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.8
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The Catalog API from Hydrosat — 2 operation(s) for catalog.
  name: Hydrosat Catalog API
  slug: hydrosat-catalog-api
- description: The Collections API from Hydrosat — 2 operation(s) for collections.
  name: Hydrosat Collections API
  slug: hydrosat-collections-api
- description: The Items API from Hydrosat — 2 operation(s) for items.
  name: Hydrosat Items API
  slug: hydrosat-items-api
- description: The Queryables API from Hydrosat — 2 operation(s) for queryables.
  name: Hydrosat Queryables API
  slug: hydrosat-queryables-api
- description: The Search API from Hydrosat — 1 operation(s) for search.
  name: Hydrosat Search API
  slug: hydrosat-search-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hydrosat STAC Catalog API
  slug: open-hydrosat-catalog-api
- collection_type: open
  name: Hydrosat STAC Catalog Collections API
  slug: open-hydrosat-collections-api
- collection_type: open
  name: Hydrosat STAC Catalog Items API
  slug: open-hydrosat-items-api
- collection_type: open
  name: Hydrosat STAC Catalog Queryables API
  slug: open-hydrosat-queryables-api
- collection_type: open
  name: Hydrosat STAC Catalog Search API
  slug: open-hydrosat-search-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hydrosat-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hydrosat-stac-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://discover.hydrosat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://satdocs.hydrosat.com/
- group: docs
  title: ''
  type: APIReference
  url: https://satdocs.hydrosat.com/stac-api-reference-and-specification
- group: start
  title: ''
  type: GettingStarted
  url: https://satdocs.hydrosat.com/stac-api-how-to-guides
- group: auth
  title: ''
  type: Authentication
  url: authentication/hydrosat-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydrosat-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydrosat-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hydrosat.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hydrosat-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://hydrosat.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://hydrosat.com/stories-blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hydrosat
- group: start
  title: ''
  type: SignUp
  url: https://discover.hydrosat.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydrosat.com/privacy-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydrosat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hydrosat.com/
created: '2026-07-17'
description: Hydrosat delivers thermal infrared satellite data and analytics for monitoring resources and detecting change, combining thermal-infrared imaging, proprietary algorithms, and field-tested expertise to support food security, water security, and industrial monitoring across 60+ countries. Its Discovery platform exposes a STAC-compliant (SpatioTemporal Asset Catalog) API at stac.hydrosat.com serving VZ-1 (Van Zyl-01) thermal and VNIR imagery at processing levels L1A, L1B, and L2, accessible via the Discovery Portal web app, direct download, or the OAuth2-protected STAC API. Products include the IrriWatch irrigation-planning tool and water/crop management solutions.
image: https://hydrosat.com/wp-content/uploads/2024/06/Field-Irrigation-Planning-2.png
layout: provider
mcp_servers:
- description: ''
  name: hydrosat-mcp.yml
  slug: hydrosat-mcpyml
modified: '2026-07-19'
name: Hydrosat
nav: Providers
network: true
overview: 'Hydrosat publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Collections API, Items API, and 2 more. Tagged areas include Company, Satellite Imagery, Thermal Infrared, Geospatial, and Earth Observation.


  Hydrosat''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 12 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 40.5
  delta: -1.9
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 47.1
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 42.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hydrosat/refs/heads/main/screenshots/hydrosat-2026-07-25T221835.png
security:
- kind: authentication
  name: Hydrosat Authentication
  slug: hydrosat-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hydrosat Domain Security
  slug: hydrosat-domain-security
  summary_line: TLSv1.2 · DMARC
slug: hydrosat
tags:
- Company
- Satellite Imagery
- Thermal Infrared
- Geospatial
- Earth Observation
- Remote Sensing
- STAC
- Agriculture
- Water Management
- Data
website: https://hydrosat.com/
---
