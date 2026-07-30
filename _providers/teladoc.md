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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for the Teladoc Health Solo virtual-care platform. Manages patients, appointments, waiting rooms, appointment slots, visit notes, attachments, patient documents, episodes of care, encounter r
  name: Teladoc Health Solo External API
  slug: teladoc-health-solo-external-api
artifact_total: 5
asyncapis:
- description: ''
  name: Teladoc Webhooks
  slug: teladoc-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.teladochealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-documentation.teladochealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://intouchhealth.github.io/solo-slate/
- group: docs
  title: ''
  type: APIReference
  url: https://intouchhealth.github.io/solo-slate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IntouchHealth
- group: auth
  title: ''
  type: Authentication
  url: authentication/teladoc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teladoc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teladoc-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/teladoc-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/teladoc-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teladoc-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teladoc-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teladoc-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/teladoc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/teladoc-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teladoc-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teladoc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teladoc-llms.txt
created: '2026-07-17'
description: 'Teladoc Health is a global virtual-care company providing telehealth, mental and behavioral health, chronic-condition management, and expert medical opinion services. Its developer surface is the Solo platform: a partner-gated REST API (the Solo External API, served under /qapi/v1 on visitnow.org) for patients, appointments, waiting rooms, visit notes, episodes of care, encounter reports, virtual nursing, and webhooks, plus native iOS and Android Mobile SDKs for embedding virtual care into partner applications. Access is granted under a partner agreement and Business Associate Agreement (BAA); requests authenticate with a static Api-Key header. Sector: healthtech.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teladoc.png
layout: provider
mcp_servers:
- description: ''
  name: teladoc-mcp.yml
  slug: teladoc-mcpyml
modified: '2026-07-21'
name: Teladoc
nav: Providers
network: true
overview: 'Teladoc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Telehealth, Telemedicine, and Virtual Care.


  The Teladoc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teladoc''s developer surface includes documentation, API reference, authentication, sandbox, and 14 more developer resources.'
random_paper: 76
score:
  band: thin
  composite: 31.8
  delta: 2.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 29.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Teladoc Authentication
  slug: teladoc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Teladoc Domain Security
  slug: teladoc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: teladoc
tags:
- Company
- Healthtech
- Telehealth
- Telemedicine
- Virtual Care
- Healthcare
- Behavioral Health
- Webhooks
- API
website: https://www.teladochealth.com
---
