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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Authentication API from VOA Health — 1 operation(s) for authentication.
  name: VOA Health Authentication API
  slug: voa-health-authentication-api
- description: Submit, query, replace, and delete clinical records on the RNDS national bus.
  name: VOA Health RNDS API
  slug: voa-health-rnds-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voa Integration Identify Authentication API
  slug: open-voa-health-authentication-api
- collection_type: open
  name: Voa Integration Identify Authentication RNDS API
  slug: open-voa-health-rnds-api
common:
- group: company
  title: ''
  type: Website
  url: https://voa.health
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.voa.health
- group: docs
  title: ''
  type: Documentation
  url: https://docs.voa.health
- group: docs
  title: ''
  type: APIReference
  url: https://docs.voa.health/integracao/rnds/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.voa.health/inicio/quickstart
- group: company
  title: ''
  type: Blog
  url: https://voa.health/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.voa.health
- group: operate
  title: ''
  type: Support
  url: mailto:integration@voahealth.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/voa-health-rnds-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/voa-health-rnds-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voa-health-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voa-health-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voa-health-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voa-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/voa-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voa-health-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voa-health-llms.txt
- group: design
  title: ''
  type: Components
  url: components/voa-health-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/voa-health-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voa-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voa-health-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voa-health-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voa-health-domain-security.yml
created: '2026-07-17'
description: Voa is a Brazilian healthcare-technology company providing an AI clinical documentation and patient-monitoring assistant that embeds directly into electronic patient record (EHR/PEP) systems, used by 60,000+ physicians across 1M+ consultations. Voa exposes integration surfaces — an embeddable plugin, an iFrame widget, and a browser extension — plus a REST integration API and an RNDS API that submits finalized clinical records to Brazil's Rede Nacional de Dados em Saúde (national health data network) in FHIR R4 using ICP-Brasil certificate authentication. Backed by Prosus Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voa-health.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface mapped 1:1 from the documented Voa RNDS API operations. Each tool would require a Bearer JWT (see authentication/voa-health-authentication.yml). Not an official/hosted serve
  name: VOA Health MCP Server
  slug: voa-health-mcp-server
modified: '2026-07-21'
name: VOA Health
nav: Providers
network: true
overview: 'VOA Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and RNDS API. Tagged areas include Company, Health, Healthcare, Clinical Documentation, and EHR.


  VOA Health''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 14.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Voa Health Authentication
  slug: voa-health-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Voa Health Domain Security
  slug: voa-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voa-health
tags:
- Company
- Health
- Healthcare
- Clinical Documentation
- EHR
- FHIR
- RNDS
- Artificial Intelligence
- Brazil
website: https://voa.health
---
