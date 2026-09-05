---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.allscripts.com'', ''status'': 301, ''note'': ''declared website redirects to https://veradigm.com:443/?modal=allscripts — a different registrable domain (allscripts.com -> veradigm.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  score: 30.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: HL7 FHIR R4 (4.0.1) REST API for Veradigm EHR, aligned to USCDI for 21st Century Cures Act patient and provider access. The live CapabilityStatement declares 31 resource types (Patient, Encounter, Obs
  name: Veradigm FHIR R4 API (formerly Allscripts)
  slug: allscripts-healthcare-solutions-api
- description: Veradigm's proprietary bidirectional API and the only Veradigm surface that can WRITE patient demographic, appointment or financial data - the Process Overview page states plainly that the FHIR API is
  name: Veradigm Unity API
  slug: veradigm-unity-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.allscripts.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.veradigm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.veradigm.com/Fhir/Introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.veradigm.com/Fhir/Resources
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.veradigm.com/Fhir/ProcessOverview
- group: start
  title: ''
  type: SignUp
  url: https://developer.veradigm.com/Account/RegisterSelf
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.veradigm.com/Home/LearnMore
- group: other
  title: ''
  type: Marketplace
  url: https://expo.veradigm.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veradigm.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.veradigm.com/Fhir/Introduction
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
  type: GitHubOrganization
  url: https://github.com/allscriptshealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allscripts
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/allscripts-healthcare-solutions-veradigm-fhir-r4-capabilitystatement.json
- group: other
  title: ''
  type: SMARTConfiguration
  url: well-known/allscripts-healthcare-solutions-smart-configuration.json
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/allscripts-healthcare-solutions-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allscripts-healthcare-solutions-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allscripts-healthcare-solutions-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allscripts-healthcare-solutions-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allscripts-healthcare-solutions-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allscripts-healthcare-solutions-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/allscripts-healthcare-solutions-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allscripts-healthcare-solutions-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/allscripts-healthcare-solutions-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allscripts-healthcare-solutions-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/allscripts-healthcare-solutions-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/allscripts-healthcare-solutions-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allscripts-healthcare-solutions-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/allscripts-healthcare-solutions-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/allscripts-healthcare-solutions-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/allscripts-healthcare-solutions-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allscripts-healthcare-solutions-domain-security.yml
created: '2026-04-19'
description: Allscripts Healthcare Solutions renamed itself Veradigm in 2022 and sold its hospital and large-physician-practice business (Sunrise, Paragon, TouchWorks) to Harris Computer, which now trades as Altera Digital Health. allscripts.com redirects to veradigm.com, and the developer program is now the Veradigm Connect Developer Program at developer.veradigm.com. Two API estates exist. The first is a public, standards-based HL7 FHIR R4 (4.0.1) surface serving USCDI data for 21st Century Cures Act patient and provider access - a live sandbox CapabilityStatement declares 31 FHIR resources, twelve of which accept create and update and none of which accept delete, authorized with SMART App Launch 2.0.0 over OAuth 2.0 and OpenID Connect, with FHIR Bulk Data $export available to backend System applications. Base URLs are per customer organization and are published in the Veradigm Endpoint Directory, downloadable as an NDJSON FHIR Bundle. The second is the proprietary bidirectional Unity
  API, the only surface that can write patient demographic, appointment or financial data; it is undocumented publicly and requires a paid Veradigm Connect Integrator subscription. No OpenAPI, no MCP server, no agent card and no public client SDK are published on either estate.
finops:
- name: Allscripts Healthcare Solutions Finops
  service_category: Electronic Health Records
  slug: allscripts-healthcare-solutions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allscripts-healthcare-solutions.png
layout: provider
modified: '2026-09-01'
name: Allscripts Healthcare Solutions
nav: Providers
network: true
overview: 'Allscripts Healthcare Solutions publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare IT, EHR, Clinical, FHIR, and HL7.


  Allscripts Healthcare Solutions'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, authentication, sandbox, and 27 more developer resources.'
plans:
- name: Allscripts Healthcare Solutions Plans Pricing
  plan_count: 6
  slug: allscripts-healthcare-solutions-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Allscripts Healthcare Solutions Rate Limits
  slug: allscripts-healthcare-solutions-rate-limits
scopes:
- name: Allscripts Healthcare Solutions Scopes
  scope_count: 237
  slug: allscripts-healthcare-solutions-scopes
  summary_line: 237 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 34.4
    developer_ergonomics: 58.9
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 60.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: us-core
    - jurisdiction: US
      standard: uscdi
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 70.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allscripts-healthcare-solutions/refs/heads/main/screenshots/allscripts-healthcare-solutions-2026-06-20T171537.png
security:
- kind: authentication
  name: Allscripts Healthcare Solutions Authentication
  slug: allscripts-healthcare-solutions-authentication
  summary_line: oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Allscripts Healthcare Solutions Domain Security
  slug: allscripts-healthcare-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allscripts-healthcare-solutions
tags:
- Healthcare IT
- EHR
- Clinical
- FHIR
- HL7
- SMART on FHIR
- USCDI
- Interoperability
- Patient Access
- 21st Century Cures
- Veradigm
website: https://www.allscripts.com
---
