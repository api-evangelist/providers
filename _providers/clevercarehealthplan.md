---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clevercarehealthplan Agentic Access
  operation_count: 27
  slug: clevercarehealthplan-agentic-access
  summary_line: 27 operations
api_count: 1
apis:
- baseURL: https://fhir.clevercarehealthplan.com/r4
  baseurl_source: declared
  description: Public (rate limited) drug formulary resources
  name: Clever Care Health Plan Drug Formulary API
  slug: clevercarehealthplan-drug-formulary-api
- baseURL: https://fhir.clevercarehealthplan.com/r4
  baseurl_source: declared
  description: Secured (OpenID Connect / OAuth 2.0) member data resources
  name: Clever Care Health Plan Patient Access API
  slug: clevercarehealthplan-patient-access-api
- baseURL: https://fhir.clevercarehealthplan.com/r4
  baseurl_source: declared
  description: Public (rate limited) provider directory resources
  name: Clever Care Health Plan Provider Directory API
  slug: clevercarehealthplan-provider-directory-api
artifact_total: 14
collections:
- collection_type: open
  name: Clever Care Health Plan FHIR R4 Drug Formulary API
  slug: open-clevercarehealthplan-drug-formulary-api
- collection_type: open
  name: Clever Care Health Plan FHIR R4 Drug Formulary Patient Access API
  slug: open-clevercarehealthplan-patient-access-api
- collection_type: open
  name: Clever Care Health Plan FHIR R4 Drug Formulary Provider Directory API
  slug: open-clevercarehealthplan-provider-directory-api
common:
- group: other
  href: https://artifacts.apis.io/clevercarehealthplan/capabilities/clevercarehealthplan-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clevercarehealthplan-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/clevercarehealthplan/overlays/clevercarehealthplan-fhir-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clevercarehealthplan-fhir-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir-portal.clevercarehealthplan.com/devportal
- group: start
  title: ''
  type: GettingStarted
  url: https://clevercarehealthplan.com/fhir-api-developer-resources/
- group: docs
  title: ''
  type: Documentation
  url: https://fhir-portal.clevercarehealthplan.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://fhir-portal.clevercarehealthplan.com/api-docs/
- group: start
  title: ''
  type: SignUp
  url: https://fhir-portal.clevercarehealthplan.com/devportal
- group: auth
  href: https://artifacts.apis.io/clevercarehealthplan/authentication/clevercarehealthplan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clevercarehealthplan-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clevercarehealthplan/scopes/clevercarehealthplan-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clevercarehealthplan-scopes.yml
- group: agent
  href: https://artifacts.apis.io/clevercarehealthplan/agentic-access/clevercarehealthplan-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clevercarehealthplan-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/clevercarehealthplan/mcp/clevercarehealthplan-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clevercarehealthplan-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clevercarehealthplan/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/clevercarehealthplan/well-known/clevercarehealthplan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clevercarehealthplan-well-known.yml
- group: agent
  href: https://artifacts.apis.io/clevercarehealthplan/llms/clevercarehealthplan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clevercarehealthplan-llms.txt
- group: design
  href: https://artifacts.apis.io/clevercarehealthplan/conformance/clevercarehealthplan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clevercarehealthplan-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clevercarehealthplan.com/medicare-compliance/
- group: design
  href: https://artifacts.apis.io/clevercarehealthplan/errors/clevercarehealthplan-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clevercarehealthplan-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clevercarehealthplan/conventions/clevercarehealthplan-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clevercarehealthplan-conventions.yml
- group: design
  href: https://artifacts.apis.io/clevercarehealthplan/lifecycle/clevercarehealthplan-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clevercarehealthplan-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/clevercarehealthplan/data-model/clevercarehealthplan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clevercarehealthplan-data-model.yml
- group: auth
  href: https://artifacts.apis.io/clevercarehealthplan/security/clevercarehealthplan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clevercarehealthplan-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevercarehealthplan.com/privacy-practices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevercarehealthplan.com/terms-of-use/
- group: company
  title: ''
  type: Website
  url: https://clevercarehealthplan.com
created: '2026-07-17'
description: 'Clever Care Health Plan is a California Medicare Advantage (HMO and HMO C-SNP) insurer that blends Eastern and Western medicine for seniors. For developers it publishes an HL7 FHIR R4 (4.0.1) API implementing the CMS Interoperability and Patient Access final rule (CMS-9115-F): a secured Patient Access API (Patient, Coverage, and CARIN Blue Button ExplanationOfBenefit) protected with SMART-on-FHIR OAuth 2.0 / OpenID Connect, plus public, rate-limited Provider Directory and Drug Formulary APIs. The FHIR server runs on WSO2 Open Healthcare with a developer portal for app registration and API subscription.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clevercarehealthplan.png
layout: provider
modified: '2026-07-18'
name: Clever Care Health Plan
nav: Providers
network: true
overview: 'Clever Care Health Plan publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Drug Formulary API, Patient Access API, and Provider Directory API. Tagged areas include Company, Healthcare, Health Insurance, Medicare Advantage, and FHIR.


  The Clever Care Health Plan catalog on APIs.io includes 1 Spectral governance ruleset.


  Clever Care Health Plan''s developer surface includes getting-started guide, documentation, API reference, signup flow, authentication, and 19 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Clever Care Health Plan API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: clevercarehealthplan-rules
scopes:
- name: Clevercarehealthplan Scopes
  scope_count: 4
  slug: clevercarehealthplan-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.7
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 44.5
    developer_ergonomics: 51.8
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
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
    score: 53.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/clevercarehealthplan/clevercarehealthplan-2026-07-25T205602.png
security:
- kind: authentication
  name: Clevercarehealthplan Authentication
  slug: clevercarehealthplan-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Clevercarehealthplan Domain Security
  slug: clevercarehealthplan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Clever Care drug formulary lookup
  slug: clevercarehealthplan-drug-formulary
- name: Clever Care patient access (claims and coverage)
  slug: clevercarehealthplan-patient-access
- name: Clever Care provider directory search
  slug: clevercarehealthplan-provider-directory
slug: clevercarehealthplan
tags:
- Company
- Healthcare
- Health Insurance
- Medicare Advantage
- FHIR
- Interoperability
- Patient Access
- Provider Directory
- Drug Formulary
- CMS-9115-F
website: https://clevercarehealthplan.com
---
