---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: Account creation (e.g., identity proofing, eConsent) that is required for a patient to progress on the xCures Platform.
  name: xCures Application API
  slug: xcures-application-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: AI-powered feature leveraging xCures’ targeted data extraction/processing to populate validated, customizable question/answer-style items. Responses can be highly flexible and every item returns a jus
  name: xCures Checklist API
  slug: xcures-checklist-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: Clinical concepts is a proprietary xCures higher-level, flattened, filtered, opinionated view of medical record information, structured around FHIR guidelines.
  name: xCures Clinical Concepts API
  slug: xcures-clinical-concepts-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: Patient records retrieved by the xCures platform and/or loaded by platform users.
  name: xCures Document API
  slug: xcures-document-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: '**F**ast **H**ealthcare **I**nteroperability **R**esource is an international data model specification developed by HL7 International to enable healthcare data exchange and interoperability between di'
  name: xCures FHIR API
  slug: xcures-fhir-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: A configured workspace on the xCures Platform. Use this endpoint to discover the projectId value(s) required by other API calls, without needing to log into the portal.
  name: xCures Project API
  slug: xcures-project-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: A specified, approved request for patient records across the network (e.g., via Carequality/TEFCA to support treatment activities, via TEFCA for IAS queries) with an associated status (e.g., “complete
  name: xCures Query API
  slug: xcures-query-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: Reciprocity or "Responder" workflows refer to the process of sharing clinical documentation housed within your system with other organizations/providers, when participating in health data exchange net
  name: xCures Reciprocity Template API
  slug: xcures-reciprocity-template-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: An individual patient created on the xCures Platform.
  name: xCures Subject API
  slug: xcures-subject-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: The AI-generated summary of a patient’s overall records and condition(s).
  name: xCures Summary API
  slug: xcures-summary-api
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: All API requests to xCures must provide an access token, retrieved via the standard OAuth authorization flow below.
  name: xCures O Auth API
  slug: xcures-oauth-api
artifact_total: 27
asyncapis:
- description: ''
  name: Xcures Application Webhooks
  slug: xcures-application-webhooks
common:
- group: other
  href: https://artifacts.apis.io/xcures/overlays/xcures-patient-registry-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xcures-patient-registry-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://xcures.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.xcures.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xcures.com/api-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xcures.com/apis/current
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xcures.com/api-introduction
- group: operate
  title: ''
  type: Support
  url: https://docs.xcures.com/support
- group: company
  title: ''
  type: Blog
  url: https://xcures.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xCures
- group: start
  title: ''
  type: SignUp
  url: https://xcures.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xcures.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xcures.com/privacy-security-notice/
- group: auth
  title: ''
  type: TrustCenter
  url: https://xcures.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://xcures.com/trust/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xcures.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.xcures.com/downloads/xCures_SDK_Workflows.postman_collection.json
- group: agent
  href: https://artifacts.apis.io/xcures/llms/xcures-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xcures-llms.txt
- group: other
  href: https://artifacts.apis.io/xcures/a2a/xcures-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xcures-a2a.yml
- group: agent
  href: https://artifacts.apis.io/xcures/mcp/xcures-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xcures-mcp.yml
- group: build
  href: https://artifacts.apis.io/xcures/mcp/xcures-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/xcures-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/xcures/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/xcures/well-known/xcures-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xcures-well-known.yml
- group: design
  href: https://artifacts.apis.io/xcures/conventions/xcures-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xcures-conventions.yml
- group: design
  href: https://artifacts.apis.io/xcures/conformance/xcures-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xcures-conformance.yml
- group: design
  href: https://artifacts.apis.io/xcures/lifecycle/xcures-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xcures-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/xcures/changelog/xcures-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xcures-changelog.yml
- group: auth
  href: https://artifacts.apis.io/xcures/authentication/xcures-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xcures-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xcures/security/xcures-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xcures-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/xcures/plans/xcures-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xcures-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/xcures/rate-limits/xcures-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xcures-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/xcures/sandbox/xcures-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xcures-sandbox.yml
- group: build
  href: https://artifacts.apis.io/xcures/packages/xcures-packages.yml
  title: ''
  type: Packages
  url: packages/xcures-packages.yml
- group: design
  href: https://artifacts.apis.io/xcures/errors/xcures-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xcures-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xcures/data-model/xcures-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xcures-data-model.yml
- group: design
  href: https://artifacts.apis.io/xcures/asyncapi/xcures-application-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/xcures-application-webhooks.yml
- group: design
  href: https://artifacts.apis.io/xcures/conventions/xcures-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xcures-conventions.yml
- group: operate
  href: https://artifacts.apis.io/xcures/lifecycle/xcures-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/xcures-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/xcures/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:help@xcures.com
created: '2026-09-04'
description: xCures operates the Clinical Clarity Engine, an AI platform that retrieves, organizes and structures fragmented patient medical records into decision-ready clinical data. Founded in 2018 and headquartered in Oakland, California, the company connects to national health information networks (Carequality and TEFCA) to pull a patient's longitudinal record across every provider and care location, then applies LLM-based named-entity/relation extraction and retrieval-augmented checklist assertion to normalize it into FHIR R4 resources, OHDSI/OMOP-mapped vocabularies (SNOMED, LOINC, RxNorm) and HL7 mCODE oncology elements, with every field anchored to its source document. The xCures Public API exposes that engine over REST at partner.xcures.com — patient (Subject) registration, network Query dispatch and polling, document retrieval and reciprocity publishing, FHIR resource reads and bulk export, fifteen Clinical Concepts domains, AI Checklist evaluation and subject summaries — authenticated
  with OAuth 2.0 client-credentials bearer tokens scoped by a ProjectId header. Originally an oncology real-world-data platform, it expanded to all therapeutic areas and is sold as SaaS, embedded API connections and de-identified real-world datasets to providers, diagnostics companies, value-based-care organizations and channel partners.
examples:
- key_count: 3
  name: Xcures Workflow Playbook.Postman_Collection
  slug: xcures-workflow-playbook.postman_collection
finops:
- has_sources: true
  method: derived
  name: Xcures Finops
  primary_unit: ''
  service_category: ''
  slug: xcures-finops
  template: true
image: https://xcures.com/wp-content/uploads/2026/06/default-image-sharing.png
layout: provider
mcp_servers:
- description: A remote MCP server xCures runs on its own documentation host as part of the Redocly Realm API Hub. It exposes the documentation corpus and the six published Agent Skills as MCP tools. It is a documen
  name: xCures Docs MCP Server
  slug: xcures-docs-mcp-server
modified: '2026-09-04'
name: xCures
nav: Providers
network: true
overview: 'xCures publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Application API, Checklist API, Clinical Concepts API, and 8 more. Tagged areas include Health, Healthcare, Medical Records, Interoperability, and FHIR.


  The xCures catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  xCures'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 32 more developer resources.'
plans:
- name: Xcures Plans Pricing
  plan_count: 0
  slug: xcures-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Xcures Rate Limits
  slug: xcures-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: xCures API Rules
  rule_count: 59
  severity_counts:
    error: 47
    hint: 0
    info: 4
    warn: 8
  slug: xcures-rules
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 58.2
    developer_ergonomics: 76.2
    discoverability: 75.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 62.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/xcures/xcures-2026-10-11T195246.png
security:
- kind: authentication
  name: Xcures Authentication
  slug: xcures-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Xcures Domain Security
  slug: xcures-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Xcures Trust Center
  slug: xcures-trust-center
  summary_line: trust center published
skill_count: 6
skills:
- name: bulk-patient-onboarding
  slug: xcures-bulk-patient-onboarding
- name: byod-ingestion
  slug: xcures-byod-ingestion
- name: reciprocity
  slug: xcures-reciprocity
- name: requery-patient
  slug: xcures-requery-patient
- name: retrieval-only
  slug: xcures-retrieval-only
- name: standard-treatment-workflow
  slug: xcures-standard-treatment-workflow
slug: xcures
tags:
- Health
- Healthcare
- Medical Records
- Interoperability
- FHIR
- Oncology
- Real-World Data
- Clinical Data
- Artificial Intelligence
- TEFCA
- Carequality
- Patient Data
- HITRUST
- HIPAA
- A2A
website: https://xcures.com/
---
