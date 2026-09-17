---
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.0
  scored_at: '2026-09-16'
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
artifact_total: 19
asyncapis:
- description: ''
  name: Xcures Application Webhooks
  slug: xcures-application-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/overlays/xcures-patient-registry-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/llms/xcures-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xcures-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/a2a/xcures-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xcures-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/mcp/xcures-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xcures-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/mcp/xcures-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/xcures-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/well-known/xcures-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xcures-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/conventions/xcures-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xcures-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/conformance/xcures-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xcures-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/lifecycle/xcures-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xcures-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/changelog/xcures-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xcures-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/authentication/xcures-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xcures-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/security/xcures-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xcures-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/plans/xcures-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xcures-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/rate-limits/xcures-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xcures-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/sandbox/xcures-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xcures-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/packages/xcures-packages.yml
  title: ''
  type: Packages
  url: packages/xcures-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/errors/xcures-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xcures-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/data-model/xcures-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xcures-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/asyncapi/xcures-application-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/xcures-application-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/conventions/xcures-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xcures-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/lifecycle/xcures-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/xcures-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xcures/refs/heads/main/examples/_index.yml
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
overview: 'xCures publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Application API, Checklist API, Clinical Concepts API, and 8 more. Tagged areas include Health, Healthcare, Medical Records, Interoperability, and FHIR.


  The xCures catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  xCures'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 32 more developer resources.'
plans:
- name: Xcures Plans Pricing
  plan_count: 0
  slug: xcures-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Xcures Rate Limits
  slug: xcures-rate-limits
score:
  band: strong
  composite: 64.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 63.5
    developer_ergonomics: 76.2
    discoverability: 75.9
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 64.2
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
    score: 52.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
website: https://xcures.com/
---
