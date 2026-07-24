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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: The Authentication API from VOA Health — 1 operation(s) for authentication.
  name: VOA Health Authentication API
  slug: voa-health-authentication-api
- description: Submit, query, replace, and delete clinical records on the RNDS national bus.
  name: VOA Health RNDS API
  slug: voa-health-rnds-api
artifact_total: 5
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
  url: openapi/voa-health-rnds-openapi.yml
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
- description: ''
  name: voa-health-mcp.yml
  slug: voa-health-mcpyml
modified: '2026-07-21'
name: VOA Health
nav: Providers
network: true
overview: 'VOA Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and RNDS API. Tagged areas include Company, Health, Healthcare, Clinical Documentation, and EHR.


  VOA Health''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 44.1
  delta: 0.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 60.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 43.4
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 47.8
  schema_version: 0.5
  scored_at: '2026-07-23'
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
