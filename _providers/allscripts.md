---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The Veradigm FHIR R4 API provides RESTful access to clinical, demographic, and facility data using the HL7 FHIR R4 standard. It supports 28 FHIR resources including Patient, Condition, Observation, Me
  name: Veradigm FHIR R4 API
  slug: veradigm-fhir-r4-api
- description: The Veradigm Unity API exposes clinical, scheduling, demographic, and practice management functions across Allscripts EHR product lines including Touchworks, Professional EHR, and acute care solutions
  name: Veradigm Unity API
  slug: veradigm-unity-api
- description: 'The Paragon Open API provides FHIR-compliant access to data from the Veradigm Paragon acute care EHR platform. It enables third-party applications to integrate with Paragon to access patient clinical '
  name: Veradigm Paragon Open API
  slug: veradigm-paragon-open-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allscripts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allscripts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allscripts-scopes.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: conformance/allscripts-fhir-r4-capabilitystatement.json
- group: design
  title: ''
  type: Conformance
  url: conformance/allscripts-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allscripts-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/allscripts-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allscripts-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allscripts-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allscripts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allscripts-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/allscripts-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/allscripts-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allscripts-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/allscripts-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/allscripts-fhir-patient-summary.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veradigm
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.veradigm.com/
- group: start
  title: ''
  type: DeveloperPortalLegacy
  url: https://developer.allscripts.com/
- group: other
  title: ''
  type: AppExpo
  url: https://expo.veradigm.com/apps
- group: start
  title: ''
  type: Signup
  url: https://developer.veradigm.com/Content/fhir/content/Developer_Signup/
- group: commercial
  title: ''
  type: Plans
  url: https://developer.veradigm.com/Home/LearnMore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veradigm.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veradigm.com/legal/privacy-notice/
- group: build
  title: ''
  type: MasterClientAgreement
  url: https://veradigm.com/img/legal/Client-Master-Agreement.pdf
- group: auth
  title: ''
  type: SecurityProgram
  url: https://veradigm.com/legal/privacy-and-security-program/
- group: auth
  title: ''
  type: ComplianceONC
  url: https://veradigm.com/legal/onc-reg-compliance/
- group: company
  title: ''
  type: Blog
  url: https://veradigm.com/blog/
- group: learn
  title: ''
  type: APIWorkshop
  url: https://lp.veradigm.com/api-workshop-registration-april
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/allscripts/refs/heads/main/finops/allscripts-finops.yml
created: '2026-06-13'
description: Allscripts, now operating as Veradigm, is a healthcare IT company providing REST and FHIR APIs for EHR data exchange, clinical workflows, patient portal, and practice management integrations. The Veradigm Developer Program (formerly Allscripts Developer Program) offers FHIR R4 APIs covering 28 clinical resources as well as a Unity API for clinical, scheduling, demographic, and practice management functions across Allscripts EHR products.
finops:
- name: Allscripts Finops
  service_category: ''
  slug: allscripts-finops
graphqls:
- description: This conceptual GraphQL schema represents the Allscripts (Veradigm) healthcare EHR APIs, covering the Veradigm FHIR R4 API and the Veradigm Unity API. Allscripts, now operating under the Veradigm bran
  name: Allscripts (Veradigm) GraphQL Schema
  slug: allscripts-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allscripts.png
jsonld:
- class_count: 0
  name: Allscripts Context
  property_count: 19
  slug: allscripts-context
layout: provider
mcp_servers:
- description: 'No official/hosted MCP server was found for Veradigm/Allscripts. Probed open.platform.veradigm.com/mcp (404, real 404 page) and developer.veradigm.com/mcp (200, but confirmed soft-404 HTML catch-all, '
  name: Allscripts MCP Server
  slug: allscripts-mcp-server
modified: '2026-08-14'
name: Allscripts
nav: Providers
network: true
overview: 'Allscripts publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare IT, EHR, FHIR, Clinical Data, and Practice Management.


  The Allscripts catalog on APIs.io includes 1 JSON-LD context.


  Allscripts'' developer surface includes authentication, sandbox, signup flow, engineering blog, and 26 more developer resources.'
plans:
- name: Unity Api Plans
  plan_count: 3
  slug: unity-api-plans
- name: Veradigm Fhir Plans
  plan_count: 6
  slug: veradigm-fhir-plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Unity Api Rate Limits
  slug: unity-api-rate-limits
- limit_count: 0
  name: Veradigm Fhir Rate Limits
  slug: veradigm-fhir-rate-limits
scopes:
- name: Allscripts Scopes
  scope_count: 0
  slug: allscripts-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.6
  delta: 4.3
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 52.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allscripts/refs/heads/main/screenshots/allscripts-2026-06-20T171537.png
security:
- kind: authentication
  name: Allscripts Authentication
  slug: allscripts-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Allscripts Domain Security
  slug: allscripts-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: allscripts
tags:
- Healthcare IT
- EHR
- FHIR
- Clinical Data
- Practice Management
- HL7
website: https://developer.veradigm.com/
---
