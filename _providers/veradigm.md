---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
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
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/veradigm/rate-limits/unity-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/unity-api-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://veradigm.com/
- group: auth
  href: https://artifacts.apis.io/veradigm/security/allscripts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allscripts-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/veradigm/authentication/allscripts-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allscripts-authentication.yml
- group: auth
  href: https://artifacts.apis.io/veradigm/scopes/allscripts-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/allscripts-scopes.yml
- group: other
  href: https://artifacts.apis.io/veradigm/conformance/allscripts-fhir-r4-capabilitystatement.json
  title: ''
  type: CapabilityStatement
  url: conformance/allscripts-fhir-r4-capabilitystatement.json
- group: design
  href: https://artifacts.apis.io/veradigm/conformance/allscripts-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allscripts-conformance.yml
- group: agent
  href: https://artifacts.apis.io/veradigm/well-known/allscripts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allscripts-well-known.yml
- group: build
  href: https://artifacts.apis.io/veradigm/packages/allscripts-packages.yml
  title: ''
  type: Packages
  url: packages/allscripts-packages.yml
- group: agent
  href: https://artifacts.apis.io/veradigm/mcp/allscripts-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/allscripts-mcp.yml
- group: agent
  href: https://artifacts.apis.io/veradigm/llms/allscripts-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allscripts-llms.txt
- group: design
  href: https://artifacts.apis.io/veradigm/errors/allscripts-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allscripts-problem-types.yml
- group: design
  href: https://artifacts.apis.io/veradigm/lifecycle/allscripts-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/allscripts-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/veradigm/lifecycle/allscripts-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/allscripts-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/veradigm/conventions/allscripts-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allscripts-conventions.yml
- group: design
  href: https://artifacts.apis.io/veradigm/data-model/allscripts-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allscripts-data-model.yml
- group: start
  href: https://artifacts.apis.io/veradigm/sandbox/allscripts-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/allscripts-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/veradigm/skills/allscripts-fhir-patient-summary.md
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
  url: https://raw.githubusercontent.com/api-evangelist/veradigm/refs/heads/main/finops/allscripts-finops.yml
created: '2026-06-13'
description: Allscripts, now operating as Veradigm, is a healthcare IT company providing REST and FHIR APIs for EHR data exchange, clinical workflows, patient portal, and practice management integrations. The Veradigm Developer Program (formerly Allscripts Developer Program) offers FHIR R4 APIs covering 28 clinical resources as well as a Unity API for clinical, scheduling, demographic, and practice management functions across Allscripts EHR products.
finops:
- has_sources: false
  method: generated
  name: Allscripts Finops
  primary_unit: ''
  service_category: ''
  slug: allscripts-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allscripts.png
jsonld:
- class_count: 0
  name: Allscripts Context
  property_count: 19
  slug: allscripts-context
layout: provider
modified: '2026-08-14'
name: Veradigm (Allscripts)
nav: Providers
network: true
overview: 'Veradigm (Allscripts) is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare IT, Electronic Health Records, FHIR, Clinical Data, and Practice Management.


  The Veradigm (Allscripts) catalog on APIs.io includes 1 JSON-LD context.


  Veradigm (Allscripts)''s developer surface includes authentication, sandbox, signup flow, engineering blog, and 28 more developer resources.'
plans:
- name: Unity Api Plans
  plan_count: 3
  slug: unity-api-plans
- name: Veradigm Fhir Plans
  plan_count: 6
  slug: veradigm-fhir-plans
random_paper: 7
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
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 12.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 40.9
    developer_ergonomics: 54.2
    discoverability: 78.6
    operational_transparency: 10.5
  previous_composite: 49.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/veradigm/allscripts-2026-06-20T171537.png
security:
- kind: authentication
  name: Allscripts Authentication
  slug: allscripts-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Allscripts Domain Security
  slug: allscripts-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 1
skills:
- name: veradigm-fhir-patient-summary
  slug: allscripts-fhir-patient-summary
slug: veradigm
tags:
- Healthcare IT
- Electronic Health Records
- FHIR
- Clinical Data
- Practice Management
- HL7
website: https://veradigm.com/
---
