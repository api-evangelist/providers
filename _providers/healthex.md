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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for patient outreach, consent checking and auditing, record-location search, test-patient creation, and usage reporting, plus a FHIR R4 server ($everything) for standards-based access to a co
  name: HealthEx API
  slug: healthex-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.healthex.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.healthex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.healthex.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.healthex.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.healthex.io/authentication
- group: operate
  title: ''
  type: Support
  url: https://support.healthex.io/kb
- group: start
  title: ''
  type: SignUp
  url: https://app.healthex.io/
- group: start
  title: ''
  type: Login
  url: https://app.healthex.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.healthex.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.healthex.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.healthex.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/healthex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/healthex-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/healthex-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/healthex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthex-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/healthex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/healthex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthex-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/healthex-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/healthex-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/healthex-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/healthex-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/healthex-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: HealthEx is a patient-centric health-data-rights platform that securely unifies an individual's medical records across places of care into one connected history, and lets them share that record — under explicit, patient-initiated consent — with providers, apps, and AI services. It operates as an Information Access Services (IAS) Provider on the TEFCA network, complies with HIPAA privacy rules, and reaches records across more than 80% of U.S. care providers. For developers HealthEx exposes a REST admin API (patient outreach, consent checking and auditing, record-location search, usage), a FHIR R4 server ($everything, USCDIv3), and a hosted Model Context Protocol server that gives AI agents governed, consent-scoped access to a patient's health record.
image: https://framerusercontent.com/assets/91Fl8WPMZvfgNsG45g8tmHf88w.png
layout: provider
mcp_servers:
- description: 'Hosted Model Context Protocol server exposing a consented patient''s FHIR-based health record to AI agents through standardized tools, with per-patient data isolation and natural-language search. Also '
  name: HealthEx MCP Server
  slug: healthex-mcp-server
modified: '2026-07-19'
name: HealthEx
nav: Providers
network: true
overview: 'HealthEx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Records, FHIR, and Patient Consent.


  HealthEx''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, changelog, and 20 more developer resources.'
random_paper: 11
scopes:
- name: Healthex Scopes
  scope_count: 5
  slug: healthex-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 39.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 63.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 39.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthex/refs/heads/main/screenshots/healthex-2026-07-25T220838.png
security:
- kind: authentication
  name: Healthex Authentication
  slug: healthex-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Healthex Domain Security
  slug: healthex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Healthex Trust Center
  slug: healthex-trust-center
  summary_line: HIPAA, TEFCA
slug: healthex
tags:
- Company
- Healthcare
- Health Records
- FHIR
- Patient Consent
- Data Sharing
- Interoperability
- TEFCA
- MCP
- Agents
website: https://www.healthex.io/
---
