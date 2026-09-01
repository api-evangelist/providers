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
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Standards-based FHIR R4 (4.0.1) Patient Access API published for CMS-9115-F / ONC 21st Century Cures Act compliance. Lets Medicare Advantage members authorize third-party applications via OAuth 2.0 to
  name: Curana Health Interoperability API
  slug: curana-health-interoperability-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://curanahealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://curanahealth.com/interoperability-api/
- group: docs
  title: ''
  type: Documentation
  url: https://curanahealth.com/interoperability-api/
- group: docs
  title: ''
  type: APIReference
  url: https://curanahealth.com/wp-content/uploads/2026/04/3rd_PARTY_CMS_APIS_v2.2.pdf
- group: start
  title: ''
  type: SignUp
  url: https://curanahealth.com/patient-api-access-form/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curanahealtstg.wpenginepowered.com/wp-content/uploads/CuranaCMSAPI-Terms-of-Service-Clean-and-Final.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curanahealth.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://curanahealth.com/interoperability-api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/curana-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/curana-health-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curana-health-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curana-health-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curana-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curana-health-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://curanahealth.com/wp-content/uploads/2025/11/CuranaCMSAPI-Release-Policy-Clean-and-Final.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/curana-health-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/curana-health-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curana-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curana-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curana-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curana-health-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curana-health-domain-security.yml
created: '2026-07-17'
description: Curana Health is a value-based senior-living healthcare company delivering on-site primary care, behavioral health, palliative care, integrated care management, and chronic-condition management to 250,000+ residents across 2,000+ senior living and skilled-nursing communities in more than 30 states, supported by 1,400+ providers, a national medical group, Accountable Care Organizations (ACOs), and Medicare Advantage Special Needs Plans. In support of the CMS Interoperability and Patient Access final rule (CMS-9115-F) and the ONC 21st Century Cures Act final rule (45 CFR 170.213 / 170.215), Curana Health publishes a standards-based FHIR R4 Interoperability (Patient Access) API at fhir.curanahealth.com that lets Medicare Advantage members authorize third-party apps to access their claims, encounter, and clinical data using OAuth 2.0, alongside a public provider-directory surface.
image: https://curanahealth.com/wp-content/uploads/2025/04/Curana-Health-Logo-Full-Color-1000px-300x84.webp
layout: provider
mcp_servers:
- description: ''
  name: Curana Health MCP Server
  slug: curana-health-mcp-server
modified: '2026-07-18'
name: Curana Health
nav: Providers
network: true
overview: 'Curana Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Healthcare, FHIR, and Interoperability.


  Curana Health''s developer surface includes documentation, API reference, signup flow, authentication, changelog, sandbox, and 16 more developer resources.'
random_paper: 7
scopes:
- name: Curana Health Scopes
  scope_count: 0
  slug: curana-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 36.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: us-core
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 71.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curana-health/refs/heads/main/screenshots/curana-health-2026-07-25T210929.png
security:
- kind: authentication
  name: Curana Health Authentication
  slug: curana-health-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Curana Health Domain Security
  slug: curana-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curana-health
tags:
- Company
- Digital Health
- Healthcare
- FHIR
- Interoperability
- Medicare Advantage
- Senior Living
- Patient Access
- Value-Based Care
- CMS-9115-F
website: https://curanahealth.com
---
