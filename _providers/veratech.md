---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://veratech.es/
- group: docs
  title: ''
  type: Documentation
  url: https://linkehr.veratech.es/modules.html
- group: docs
  title: ''
  type: Manual
  url: https://linkehr.veratech.es/data/LinkEHRStudioManual.pdf
- group: other
  title: ''
  type: Download
  url: https://linkehr.veratech.es/getlinkehr.html
- group: operate
  title: ''
  type: Support
  url: http://help.veratech.es
- group: company
  title: ''
  type: Blog
  url: https://veratech.es/noticias/
- group: operate
  title: ''
  type: Contact
  url: https://veratech.es/hablemos/
- group: company
  title: ''
  type: Careers
  url: https://veratech.es/trabaja-con-nosotros/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veratech.es/aviso-legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veratech.es/politica-privacidad/
- group: other
  title: ''
  type: CookiePolicy
  url: https://veratech.es/cookies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veratech-for-health/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/veratech
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/veratech-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/veratech-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/veratech-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/veratech-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/veratech-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veratech-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veratech-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: VeraTech for Health sells consulting plus the LinkEHR desktop/server tooling and has no developer program at all — full contract discovery across every company-controlled host found no OpenAPI, GraphQL, MCP, WSDL or AsyncAPI, no /.well-known/ document, no SDK in any public registry and no GitHub organization; the only machine-readable file the company serves is a Yoast-generated /llms.txt, and its live openEHR-to-FHIR transformer at openehr2fhir.veratech.es is a browser-only app with no documented endpoint.
  evidence:
  - status: 404
    url: https://veratech.es/openapi.json
  - status: 404
    url: https://linkehr.veratech.es/openapi.json
  - status: 404
    url: https://openehr2fhir.veratech.es/openehr2fhir/v3/api-docs
  - status: 404
    url: https://veratech.es/.well-known/api-catalog
  - status: 404
    url: https://veratech.es/.well-known/agent-card.json
  - status: 404
    url: https://registry.npmjs.org/linkehr
  - status: 200
    url: https://veratech.es/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: VeraTech for Health S.L. is a Spanish semantic-interoperability consultancy and health-data tooling vendor, founded in 2010 in Valencia as a spin-off of the Biomedical Informatics group (IBIME) at the Universitat Politecnica de Valencia and based at BIOHUB VLC. It helps hospitals, regional health services and research networks make clinical data comprehensible and reusable, combining advisory work, an interoperability office model and applied innovation (NLP, knowledge graphs, machine learning) with its own LinkEHR Interoperability Platform. LinkEHR is a set of desktop and server tools for authoring clinical information models as archetypes and normalizing legacy clinical data into openEHR, ISO/EN 13606, HL7 CDA, HL7 FHIR, OMOP CDM and CDISC ODM. Veratech is an official openEHR training provider for CatSalut, is EHDEN-accredited for OMOP CDM mapping, and works on SNOMED CT adoption in the Spanish national health system. It publishes no public developer program, no API and no
  machine-readable contract; its software is distributed as downloadable builds and commercially licensed modules sold through direct contact.
image: https://www.veratech.es/wp-content/uploads/2025/03/VT_15Aniversario-negativo.png
layout: provider
modified: '2026-09-02'
name: Veratech for Health
nav: Providers
network: true
overview: 'Veratech for Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Semantic Interoperability, and openEHR.


  Veratech for Health''s developer surface includes documentation, support, engineering blog, changelog, and 16 more developer resources.'
plans:
- name: Veratech Plans Pricing
  plan_count: 2
  slug: veratech-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Veratech Rate Limits
  slug: veratech-rate-limits
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 21.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Veratech Domain Security
  slug: veratech-domain-security
  summary_line: DMARC
slug: veratech
tags:
- Company
- Healthcare
- Health Data
- Semantic Interoperability
- openEHR
- HL7 FHIR
- ISO 13606
- SNOMED CT
- OMOP CDM
- Clinical Data
- Electronic Health Records
- Consulting
- Spain
website: https://veratech.es/
---
