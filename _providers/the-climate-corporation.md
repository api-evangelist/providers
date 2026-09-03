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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: The Climate Corporation Agentic Access
  operation_count: 28
  slug: the-climate-corporation-agentic-access
  summary_line: 28 operations · 6 acting
api_count: 1
apis:
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: Field Boundary data endpoints.
  name: The Climate Corporation Boundaries API
  slug: the-climate-corporation-boundaries-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: General data export endpoints.
  name: The Climate Corporation Exports API
  slug: the-climate-corporation-exports-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: Farm organization data endpoints.
  name: The Climate Corporation FarmOrganizations API
  slug: the-climate-corporation-farmorganizations-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: Field data endpoints.
  name: The Climate Corporation Fields API
  slug: the-climate-corporation-fields-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: General data retrieval endpoints.
  name: The Climate Corporation Layers API
  slug: the-climate-corporation-layers-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: Operation data endpoints.
  name: The Climate Corporation Operations API
  slug: the-climate-corporation-operations-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: Resource Owner data endpoints.
  name: The Climate Corporation ResourceOwners API
  slug: the-climate-corporation-resourceowners-api
- baseURL: https://platform.climate.com
  baseurl_source: declared
  description: General data upload endpoints.
  name: The Climate Corporation Uploads API
  slug: the-climate-corporation-uploads-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries API
  slug: open-the-climate-corporation-boundaries-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries Exports API
  slug: open-the-climate-corporation-exports-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries FarmOrganizations API
  slug: open-the-climate-corporation-farmorganizations-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries Fields API
  slug: open-the-climate-corporation-fields-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries Layers API
  slug: open-the-climate-corporation-layers-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries Operations API
  slug: open-the-climate-corporation-operations-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries ResourceOwners API
  slug: open-the-climate-corporation-resourceowners-api
- collection_type: open
  name: Climate FieldView Platform APIs Boundaries Uploads API
  slug: open-the-climate-corporation-uploads-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/the-climate-corporation-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/the-climate-corporation-platform-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.fieldview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fieldview.com/technical-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.fieldview.com/technical-documentation/
- group: start
  title: ''
  type: SignUp
  url: https://dev.fieldview.com/join-us
- group: operate
  title: ''
  type: Support
  url: https://support.climate.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheClimateCorporation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://climate.com/legal/end-user-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://climate.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-climate-corporation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-climate-corporation-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-climate-corporation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-climate-corporation-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-climate-corporation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-climate-corporation-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-climate-corporation-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-climate-corporation-agentic-access.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/the-climate-corporation-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/the-climate-corporation-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-climate-corporation-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-climate-corporation-llms.txt
created: '2026-07-17'
description: 'The Climate Corporation (Climate LLC, a Bayer company) operates Climate FieldView, one of the world''s largest digital agriculture platforms, spanning 120M+ acres and 100,000+ farmers. Its FieldView Platform APIs let approved partners read and write growers'' data with OAuth2 consent: field boundaries (GeoJSON), farm organizations, operations, resource owners, and agronomic layers (as-planted, as-applied, as-harvested, scouting), plus asynchronous bulk uploads and exports of planting, application, harvest, imagery, seeding prescription (rx), and soil-sample data. Every call requires both a Bearer access token and a partner X-Api-Key. A v5 API surface is in preview.'
image: https://s3-us-west-2.amazonaws.com/climate-com/favicons/android-chrome-192x192.png
layout: provider
modified: '2026-07-21'
name: The Climate Corporation
nav: Providers
network: true
overview: 'The Climate Corporation publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Boundaries API, Exports API, FarmOrganizations API, and 5 more. Tagged areas include Company, Climate, Agriculture, AgTech, and Digital Agriculture.


  The Climate Corporation''s developer surface includes documentation, API reference, signup flow, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 15
scopes:
- name: The Climate Corporation Scopes
  scope_count: 24
  slug: the-climate-corporation-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 56.7
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-climate-corporation/refs/heads/main/screenshots/the-climate-corporation-2026-08-17T082334.png
security:
- kind: authentication
  name: The Climate Corporation Authentication
  slug: the-climate-corporation-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: The Climate Corporation Domain Security
  slug: the-climate-corporation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: the-climate-corporation
tags:
- Company
- Climate
- Agriculture
- AgTech
- Digital Agriculture
- Farm Management
- Geospatial
website: https://dev.fieldview.com/
---
