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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Athelas Agentic Access
  operation_count: 18
  slug: athelas-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 1
apis:
- description: ONC (g)(10)-certified, US Core 6.1.0-compliant FHIR R4B server exposing patient health data from Air to authorized third-party apps. Secured with SMART on FHIR v2 / OAuth2 (AWS Cognito), supporting st
  name: Commure EHR FHIR API
  slug: commure-ehr-fhir-api
- baseURL: https://api.athelas.com/enterprise/v1
  baseurl_source: declared
  description: The Auth API from Athelas — 1 operation(s) for auth.
  name: Athelas Auth API
  slug: athelas-auth-api
- baseURL: https://api.athelas.com/enterprise/v1
  baseurl_source: declared
  description: The Patients API from Athelas — 8 operation(s) for patients.
  name: Athelas Patients API
  slug: athelas-patients-api
- baseURL: https://api.athelas.com/enterprise/v1
  baseurl_source: declared
  description: The Prescribers API from Athelas — 3 operation(s) for prescribers.
  name: Athelas Prescribers API
  slug: athelas-prescribers-api
- baseURL: https://api.athelas.com/enterprise/v1
  baseurl_source: declared
  description: The Sites API from Athelas — 5 operation(s) for sites.
  name: Athelas Sites API
  slug: athelas-sites-api
- baseURL: https://api.athelas.com/enterprise/v1
  baseurl_source: declared
  description: The Test Types API from Athelas — 1 operation(s) for test types.
  name: Athelas Test Types API
  slug: athelas-test-types-api
artifact_total: 18
asyncapis:
- description: ''
  name: Athelas Webhooks
  slug: athelas-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Athelas Enterprise Auth API
  slug: open-athelas-auth-api
- collection_type: open
  name: Athelas Enterprise Auth Patients API
  slug: open-athelas-patients-api
- collection_type: open
  name: Athelas Enterprise Auth Prescribers API
  slug: open-athelas-prescribers-api
- collection_type: open
  name: Athelas Enterprise Auth Sites API
  slug: open-athelas-sites-api
- collection_type: open
  name: Athelas Enterprise Auth Test Types API
  slug: open-athelas-test-types-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/athelas-capability-edges.yml
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
  name: Athelas MCP Server
  slug: athelas-mcp-server
modified: '2026-07-18'
name: Athelas
nav: Providers
network: true
overview: 'Athelas publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Patients API, Prescribers API, and 2 more. Tagged areas include Company, Healthcare, Remote Patient Monitoring, Electronic Health Records, and FHIR.


  The Athelas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Athelas'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 22 more developer resources.'
random_paper: 3
scopes:
- name: Athelas Scopes
  scope_count: 31
  slug: athelas-scopes
  summary_line: 31 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 63.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 54.3
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
    jurisdictions:
    - jurisdiction: US
      standard: uscdi
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 87.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Artificial Intelligence
website: https://athelas.com/
---
