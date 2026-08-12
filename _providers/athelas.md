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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Athelas Agentic Access
  operation_count: 18
  slug: athelas-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 6
apis:
- description: ONC (g)(10)-certified, US Core 6.1.0-compliant FHIR R4B server exposing patient health data from Air to authorized third-party apps. Secured with SMART on FHIR v2 / OAuth2 (AWS Cognito), supporting st
  name: Commure EHR FHIR API
  slug: commure-ehr-fhir-api
- description: The Auth API from Athelas — 1 operation(s) for auth.
  name: Athelas Auth API
  slug: athelas-auth-api
- description: The Patients API from Athelas — 8 operation(s) for patients.
  name: Athelas Patients API
  slug: athelas-patients-api
- description: The Prescribers API from Athelas — 3 operation(s) for prescribers.
  name: Athelas Prescribers API
  slug: athelas-prescribers-api
- description: The Sites API from Athelas — 5 operation(s) for sites.
  name: Athelas Sites API
  slug: athelas-sites-api
- description: The Test Types API from Athelas — 1 operation(s) for test types.
  name: Athelas Test Types API
  slug: athelas-test-types-api
artifact_total: 12
asyncapis:
- description: ''
  name: Athelas Webhooks
  slug: athelas-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://athelas.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://athelas.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athelas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://athelas.readme.io/reference/login
- group: start
  title: ''
  type: GettingStarted
  url: https://athelas.readme.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/athelas-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/athelas-scopes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/athelas-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.athelas.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/athelas-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/athelas-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/athelas-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/athelas-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/athelas-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.athelas.com/air_developer/onc_certification/mandatory_disclosure
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/athelas-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/athelas-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/athelas-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/athelas-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/athelas-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/athelas-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/athelas-enterprise-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athelas-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.athelas.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.athelas.com/legal/privacy-policy-current
- group: company
  title: ''
  type: Blog
  url: https://www.athelas.com/tbh
- group: operate
  title: ''
  type: Support
  url: https://athelas.readme.io/discuss
created: '2026-07-17'
description: 'Athelas (Commure d/b/a Athelas) is a healthcare technology company building AI-powered infrastructure for provider organizations, spanning remote patient monitoring (RPM), an AI-native EHR ("Air"), ambient AI scribing, and revenue cycle management (RCM / "Insights"). Its developer surface exposes two public APIs: the Athelas Enterprise RPM API (Bearer-token REST over api.athelas.com/enterprise/v1) for enrolling patients, managing sites and prescribers, shipping cellular-connected monitoring devices, and streaming device test results via webhook; and the Commure EHR FHIR API, an ONC (g)(10)-certified, US Core 6.1.0-compliant FHIR R4B server secured with SMART on FHIR v2 / OAuth2 for third-party app integrations with Air. Backed by General Catalyst and Initialized Capital; Athelas and Commure merged to form a multi-billion-dollar healthcare infrastructure company.'
image: https://www.athelas.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: athelas-mcp.yml
  slug: athelas-mcpyml
modified: '2026-07-18'
name: Athelas
nav: Providers
network: true
overview: 'Athelas publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Patients API, Prescribers API, and 2 more. Tagged areas include Company, Healthcare, Remote Patient Monitoring, Electronic Health Records, and FHIR.


  The Athelas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Athelas'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 21 more developer resources.'
random_paper: 42
scopes:
- name: Athelas Scopes
  scope_count: 31
  slug: athelas-scopes
  summary_line: 31 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 54.0
  delta: -5.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/athelas/refs/heads/main/screenshots/athelas-2026-07-25T201527.png
security:
- kind: authentication
  name: Athelas Authentication
  slug: athelas-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Athelas Domain Security
  slug: athelas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: athelas
tags:
- Company
- Healthcare
- Remote Patient Monitoring
- Electronic Health Records
- FHIR
- Revenue Cycle Management
- Medical Devices
- SMART on FHIR
- Interoperability
- AI
website: https://athelas.com/
---
