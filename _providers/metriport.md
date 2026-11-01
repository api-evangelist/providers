---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Metriport Agentic Access
  operation_count: 30
  slug: metriport-agentic-access
  summary_line: 30 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Medical API consolidated FHIR data.
  name: Metriport Consolidated API
  slug: metriport-consolidated-api
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Devices API normalized health data.
  name: Metriport Devices Data API
  slug: metriport-devices-data-api
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Medical API clinical document query and retrieval.
  name: Metriport Document API
  slug: metriport-document-api
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Medical API facility management.
  name: Metriport Facility API
  slug: metriport-facility-api
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Medical API patient management.
  name: Metriport Patient API
  slug: metriport-patient-api
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Account settings and webhooks.
  name: Metriport Settings API
  slug: metriport-settings-api
- baseURL: https://api.metriport.com/medical/v1
  baseurl_source: declared
  description: Devices API user and connect management.
  name: Metriport User API
  slug: metriport-user-api
arazzos:
- description: Register a patient, start a consolidated FHIR R4 query for the requested resources, poll until conversion completes, then count the consolidated data.
  name: Metriport Consolidated FHIR Query
  slug: metriport-consolidated-fhir-query-workflow
- description: Register a patient, trigger an IHE document query across the networks, poll until retrieval completes, list the resulting documents, and obtain a signed download URL.
  name: Metriport Patient Document Retrieval
  slug: metriport-patient-document-retrieval-workflow
- description: Create a facility, register a patient under it, then run an MPI demographic match to resolve an existing patient record.
  name: Metriport Patient Matching
  slug: metriport-patient-matching-workflow
- description: Create a devices user, mint a Connect Widget session token, then pull the user's activity and biometrics data from connected wearables.
  name: Metriport Wearables Connect
  slug: metriport-wearables-connect-workflow
artifact_total: 45
asyncapis:
- description: ''
  name: Metriport Webhooks
  slug: metriport-webhooks
collections:
- collection_type: open
  name: Metriport Consolidated API
  slug: open-metriport-consolidated-api
- collection_type: open
  name: Metriport Consolidated Devices Data API
  slug: open-metriport-devices-data-api
- collection_type: open
  name: Metriport Consolidated Document API
  slug: open-metriport-document-api
- collection_type: open
  name: Metriport Consolidated Facility API
  slug: open-metriport-facility-api
- collection_type: open
  name: Metriport Consolidated Patient API
  slug: open-metriport-patient-api
- collection_type: open
  name: Metriport Consolidated Settings API
  slug: open-metriport-settings-api
- collection_type: open
  name: Metriport Consolidated User API
  slug: open-metriport-user-api
- collection_type: open
  name: Metriport API
  slug: open-metriport
common:
- group: design
  href: https://artifacts.apis.io/metriport/rules/metriport-rules.yml
  title: ''
  type: Spectral
  url: rules/metriport-rules.yml
- group: design
  href: https://artifacts.apis.io/metriport/json-ld/metriport-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/metriport-context.jsonld
- group: design
  href: https://artifacts.apis.io/metriport/vocabulary/metriport-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/metriport-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/metriport/hosts/metriport-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metriport-hosts.yml
- group: other
  href: https://artifacts.apis.io/metriport/vendors/metriport-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metriport-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.metriport.com/news
- group: other
  href: https://artifacts.apis.io/metriport/capabilities/metriport-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/metriport-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/metriport/agentic-access/metriport-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/metriport-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/metriport/security/metriport-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metriport-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/metriport/authentication/metriport-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metriport-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metriport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metriport
- group: company
  title: ''
  type: Website
  url: https://www.metriport.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metriport.com
- group: operate
  href: https://artifacts.apis.io/metriport/rate-limits/metriport-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/metriport-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/metriport/finops/metriport-finops.yml
  title: ''
  type: FinOps
  url: finops/metriport-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.metriport.com/blog
- group: build
  href: https://artifacts.apis.io/metriport/packages/metriport-packages.yml
  title: ''
  type: Packages
  url: packages/metriport-packages.yml
- group: build
  href: https://artifacts.apis.io/metriport/packages/metriport-packages.yml
  title: ''
  type: SDKs
  url: packages/metriport-packages.yml
- group: agent
  href: https://artifacts.apis.io/metriport/well-known/metriport-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metriport-well-known.yml
- group: agent
  href: https://artifacts.apis.io/metriport/mcp/metriport-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/metriport-mcp.yml
- group: build
  href: https://artifacts.apis.io/metriport/mcp/metriport-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/metriport-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/metriport/a2a/metriport-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/metriport-a2a.yml
- group: agent
  href: https://artifacts.apis.io/metriport/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/metriport/llms/metriport-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metriport-llms.txt
- group: design
  href: https://artifacts.apis.io/metriport/conformance/metriport-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metriport-conformance.yml
- group: auth
  href: https://artifacts.apis.io/metriport/security/metriport-trust-center.yml
  title: ''
  type: Compliance
  url: security/metriport-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/metriport/security/metriport-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/metriport-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/metriport/security/metriport-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/metriport-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/metriport/security/metriport-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/metriport-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/metriport/errors/metriport-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/metriport-problem-types.yml
- group: design
  href: https://artifacts.apis.io/metriport/lifecycle/metriport-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/metriport-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/metriport/conventions/metriport-conventions.yml
  title: ''
  type: Conventions
  url: conventions/metriport-conventions.yml
- group: start
  href: https://artifacts.apis.io/metriport/sandbox/metriport-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/metriport-sandbox.yml
- group: design
  href: https://artifacts.apis.io/metriport/components/metriport-components.yml
  title: ''
  type: Components
  url: components/metriport-components.yml
- group: design
  href: https://artifacts.apis.io/metriport/data-model/metriport-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metriport-data-model.yml
- group: design
  href: https://artifacts.apis.io/metriport/asyncapi/metriport-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/metriport-webhooks.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metriport.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.metriport.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metriport.com/medical-api/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.metriport.com/medical-api/api-reference/patient/create-patient
- group: operate
  title: ''
  type: Support
  url: https://www.metriport.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://dash.metriport.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metriport.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metriport.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/metriport/metriport-api/folder/7zl228v/medical
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/metriport/metriport
created: '2026-06-21'
description: Metriport is an open-source, universal API for healthcare data. The Medical API exchanges patient medical records across the CommonWell and Carequality networks and returns consolidated FHIR R4 data, while the Devices API hydrates activity, biometrics, nutrition, and sleep data from consumer wearables and mHealth apps. Companies can use the hosted Metriport cloud or self-host the open-source code to avoid vendor lock-in.
finops:
- has_sources: true
  method: generated
  name: Metriport Finops
  primary_unit: ''
  service_category: Healthcare and Life Sciences
  slug: metriport-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metriport.png
json_schemas:
- name: BaseFacility
  property_count: 5
  slug: metriport-base-facility
- name: BasePatient
  property_count: 7
  slug: metriport-base-patient
- name: ConsolidatedQuery
  property_count: 4
  slug: metriport-consolidated-query
- name: DevicesData
  property_count: 6
  slug: metriport-devices-data
- name: DevicesUser
  property_count: 3
  slug: metriport-devices-user
- name: DocumentQuery
  property_count: 2
  slug: metriport-document-query
- name: DocumentReference
  property_count: 7
  slug: metriport-document-reference
- name: Facility
  property_count: 0
  slug: metriport-facility
- name: Patient
  property_count: 0
  slug: metriport-patient
- name: Settings
  property_count: 4
  slug: metriport-settings
jsonld:
- class_count: 11
  name: Metriport Context
  property_count: 46
  slug: metriport-context
layout: provider
mcp_servers:
- description: Metriport serves a remote MCP endpoint from its documentation host. A tools/list POST returns HTTP 200 anonymously with three real tools and their inputSchemas — captured verbatim in metriport-mcp-too
  name: Metriport MCP Server
  slug: metriport-docs
modified: '2026-08-14'
name: Metriport
nav: Providers
network: true
overview: 'Metriport publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Consolidated API, Devices Data API, Document API, and 4 more. Tagged areas include Healthcare, Medical Records, FHIR, Health Data, and Wearables.


  The Metriport catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Metriport''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, API reference, support, and 40 more developer resources.'
plans:
- name: Metriport Plans Pricing
  plan_count: 0
  slug: metriport-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 10
  name: Metriport Rate Limits
  slug: metriport-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Metriport API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: metriport-rules
score:
  band: exemplar
  composite: 66.6
  coverage:
    artifact_dirs: 36
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 67.0
    developer_ergonomics: 83.3
    discoverability: 66.7
    operational_transparency: 71.1
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/metriport/metriport-2026-08-07T172739.png
security:
- kind: authentication
  name: Metriport Authentication
  slug: metriport-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metriport Domain Security
  slug: metriport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Metriport Vulnerability Disclosure
  slug: metriport-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Metriport Trust Center
  slug: metriport-trust-center
  summary_line: SOC 2 Type II, HIPAA
skill_count: 4
skills:
- name: metriport-consolidated-fhir-query
  slug: metriport-consolidated-fhir-query
- name: metriport-medical-api-skill
  slug: metriport-medical-api-skill
- name: metriport-patient-document-retrieval
  slug: metriport-patient-document-retrieval
- name: metriport-webhook-onboarding
  slug: metriport-webhook-onboarding
slug: metriport
tags:
- Healthcare
- Medical Records
- FHIR
- Health Data
- Wearables
- Open Source
- A2A
website: https://www.metriport.com
---
