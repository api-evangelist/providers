---
access_model:
  confidence: medium
  label: Enterprise · Partner onboarding · US-only
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Vim Agentic Access
  operation_count: 4
  slug: vim-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 6
apis:
- description: The Vim Canvas developer platform and VimOS.js JavaScript SDK for embedding applications at the point of care. Reads EHR state (Patient, Encounter, Orders, Referral, Claim, plus problem/medication/all
  name: Vim Canvas SDK (VimOS.js)
  slug: vim-canvas-sdk
- description: REST endpoints for retrieving the organizations connected to an application and the users within an organization application. OAuth 2.0 client-credentials authenticated.
  name: Vim Applications & Organizations API
  slug: vim-applications-api
- description: REST endpoint for inviting users to access applications on Vim. OAuth 2.0 client-credentials authenticated.
  name: Vim Invitations API
  slug: vim-invitations-api
- description: REST endpoint returning future appointment data (a 10-day lookahead) for a Vim organization. OAuth 2.0 client-credentials authenticated.
  name: Vim Appointments API
  slug: vim-appointments-api
- description: REST endpoint for obtaining a download URL for a chart-retrieval request. OAuth 2.0 client-credentials authenticated.
  name: Vim Chart Retrieval API
  slug: vim-chart-retrieval-api
- description: 'Ingestion surface for pushing patient-specific clinical insights and gaps (Diagnosis Gaps, Risk, Quality, Social Determinants of Health) into Vim for surfacing at the point of care, via either API or '
  name: Vim Data Source
  slug: vim-data-source
artifact_total: 12
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/vim-data-source-openapi-original.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vim-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vim-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/vim-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vim-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vim-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vim-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vim-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vim-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vim-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://getvim.com/technology-security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance-self-service.getvim.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vim-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vim-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vim-data-source-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vim-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vim-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vim-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vim-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://getvim.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getvim.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getvim.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getvim.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getvim.com/vim-os-js/setting-up
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/vim-openid-configuration.json
- group: design
  title: ''
  type: OAuthMetadata
  url: well-known/vim-oauth-authorization-server.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getvim
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getvim.com
- group: company
  title: ''
  type: Blog
  url: https://getvim.com/blog
- group: auth
  title: ''
  type: Security
  url: https://getvim.com/technology-security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getvim.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getvim.com/legal/privacy/
created: '2026-07-24'
description: Vim is a United States healthcare technology company (getvim.com) that operates a clinical workflow and point-of-care integration platform connecting health plans, provider organizations, and digital-health applications to physicians inside their existing electronic health records. Through the Vim Canvas developer platform and the VimOS.js JavaScript SDK, applications embed actionable clinical insights - diagnosis gaps, risk, quality, and social determinants of health - directly into supported ambulatory EHR workflows and can read and write EHR resources (Patient, Encounter, Orders, Referral, Claim) at the point of care. Vim also exposes a REST API at api.getvim.com/v1 for provisioning applications, organizations, invitations, appointment lookups, and chart retrieval, authenticated with OAuth 2.0 client credentials via an Auth0-backed authorization server (auth.getvim.com). Vim is HIPAA, SOC 2, and HITRUST certified. The platform is proprietary REST and SDK based; it is not
  an HL7 FHIR API and publishes no FHIR CapabilityStatement. The API is available only to application servers hosted within the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: vim-mcp.yml
  slug: vim-mcpyml
modified: '2026-07-24'
name: Vim
nav: Providers
network: true
overview: 'Vim publishes 1 API on the [APIs.io](https://apis.io/) network: Data Source. Tagged areas include Healthcare, United States, Clinical AI, EHR Integration, and Point of Care.


  Vim''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 28 more developer resources.'
random_paper: 16
scopes:
- name: Vim Scopes
  scope_count: 4
  slug: vim-scopes
  summary_line: 4 scopes · implicit/clientCredentials
score:
  band: developing
  composite: 44.5
  delta: -5.6
  facets:
    commercial_clarity: 36.8
    contract_quality: 32.3
    developer_ergonomics: 58.2
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Vim Authentication
  slug: vim-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vim Domain Security
  slug: vim-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vim Trust Center
  slug: vim-trust-center
  summary_line: HITRUST CSF, SOC 2 Type II, HIPAA
slug: vim
tags:
- Healthcare
- United States
- Clinical AI
- EHR Integration
- Point of Care
- Interoperability
- Value-Based Care
- Care Gaps
- OAuth
website: https://getvim.com/
---
