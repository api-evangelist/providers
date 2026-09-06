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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://partner.xcures.com
  baseurl_source: declared
  description: 'REST API for the xCures Clinical Clarity Engine. Register patients (Subjects), dispatch and poll queries against Carequality/TEFCA health information networks, retrieve and publish clinical documents '
  name: xCures Public API
  slug: xcures-public-api
artifact_total: 9
asyncapis:
- description: ''
  name: Xcures Application Webhooks
  slug: xcures-application-webhooks
common:
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
  title: ''
  type: LLMsTxt
  url: llms/xcures-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/xcures-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xcures-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/xcures-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xcures-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xcures-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xcures-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xcures-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xcures-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xcures-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xcures-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xcures-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xcures-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/xcures-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/xcures-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xcures-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xcures-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/xcures-application-webhooks.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/xcures-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/xcures-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
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
overview: 'xCures publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Health, Healthcare, Medical Records, Interoperability, and FHIR.


  The xCures catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  xCures'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 30 more developer resources.'
plans:
- name: Xcures Plans Pricing
  plan_count: 0
  slug: xcures-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Xcures Rate Limits
  slug: xcures-rate-limits
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 62.4
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 64.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- Real World Data
- Clinical Data
- Artificial Intelligence
- TEFCA
- Carequality
- Patient Data
- HITRUST
- HIPAA
website: https://xcures.com/
---
