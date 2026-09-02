---
access_model:
  confidence: high
  label: Free · anonymous read, no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata-harvesting interface for Repository@USM, the EPrints 3.3.16 institutional repository USM runs on its own host. The live Identify response gives repositoryName "USM Repository", pr
  name: USM Repository OAI-PMH
  slug: eprints-oai
- description: 'Anonymous read interface to Repository@USM beyond OAI-PMH, verified route by route on 2026-09-01. /rest/ exposes three datasets (eprint, user, subject); /rest/eprint/{id}.xml returns full EPrints EP2 '
  name: USM Repository EPrints REST and Export
  slug: eprints-rest
- description: USM's own SAML 2.0 Shibboleth identity provider, entityID https://shibsso.usm.my/idp/shibboleth, scope usm.my. Registered in the SIFULAN Malaysian Access Federation on 2021-10-30 under registration au
  name: USM Shibboleth Identity Provider (SIFULAN / eduGAIN)
  slug: shibboleth-idp
- description: Self-hosted Moodle at elearning.usm.my with the REST web-service server enabled and token-gated. An unauthenticated call returns Moodle's own invalidtoken exception, which proves the service is live r
  name: e-Learning@USM Moodle Web Services
  slug: moodle-ws
- description: USM is Crossref member 8963, registering DOIs under prefixes 10.21315 (USM Press journals such as the Malaysian Journal of Medical Sciences, Journal of Physical Science, Kajian Malaysia and Tropical L
  name: Crossref membership — Universiti Sains Malaysia
  slug: crossref-member
- description: 'USM''s Research Organization Registry identifier, https://ror.org/02rgb2k63. The identifier is the join key used by ORCID, Crossref and DataCite to attribute research output to the institution — 4,821 '
  name: ROR record — Universiti Sains Malaysia
  slug: ror-record
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.usm.my/en/
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.usm.my/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibsso.usm.my/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.usm.my/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.usm.my/
- group: company
  title: ''
  type: Blog
  url: https://news.usm.my/
- group: operate
  title: ''
  type: Support
  url: https://ppkt.usm.my/
- group: other
  title: ''
  type: AIPolicy
  url: https://cdae.usm.my/images/DownloadPDF/GARIS%20PANDUAN%20PENGGUNAAN%20TEKNOLOGI%20KECERDASAN%20BUATAN%20GENERATIF%20KBG%20DALAM%20PENGAJARAN%20DAN%20PEMBELAJARAN%20PdP%20PENDIDIKAN%20TINGGI.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-sains-malaysia-official/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/usm-repository-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/usm-repository-eprints-rest-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/usm-eprint-record.json
- group: build
  title: ''
  type: Examples
  url: examples/usm-repository-examples.yml
- group: design
  title: ''
  type: Errors
  url: errors/usm-repository-oai-pmh-errors.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usm-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usm-education-standards-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/usm-repository-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/usm-repository-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/usm-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/usm-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usm-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/usm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Sains Malaysia (USM) is a public research university founded in 1969 in Penang, Malaysia, holding APEX (Accelerated Programme for Excellence) status. USM operates no developer programme, no API catalog and no developer documentation of any kind, and its programmable footprint is entirely a by-product of the software it runs rather than anything it publishes for integrators. Three institution-operated machine-readable surfaces were verified live on 2026-09-01, all on hosts under usm.my: the OAI-PMH 2.0 endpoint and the EPrints REST/export tree of Repository@USM (eprints.usm.my, EPrints 3.3.16, seventeen export serializations), and USM''s own Shibboleth SAML 2.0 identity provider at shibsso.usm.my, registered in the SIFULAN Malaysian Access Federation since 2021 and exported to eduGAIN. USM is a Crossref member (id 8963, prefixes 10.21315 and 10.36777) and holds a ROR record; it is not a DataCite provider or client. The host advertised as an API portal, api.usm.my,
  is an unmodified commercial HTML template with lorem ipsum body copy and no catalog behind its login — it is scaffolding, not a gated API programme, and this profile no longer counts it as a surface.'
examples:
- key_count: 27
  name: Usm Repository Eprint Record
  slug: usm-repository-eprint-record
finops:
- name: Usm Finops
  service_category: Education
  slug: usm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usm.png
json_schemas:
- name: Repository@USM EPrint record (JSON export)
  property_count: 0
  slug: usm-eprint-record
jsonld:
- class_count: 13
  name: Usm Context
  property_count: 4
  slug: usm-context
layout: provider
modified: '2026-09-01'
name: Universiti Sains Malaysia
nav: Providers
network: true
overview: 'Universiti Sains Malaysia publishes 2 APIs on the [APIs.io](https://apis.io/) network: USM Repository OAI-PMH and USM Repository EPrints REST and Export. Tagged areas include University, Higher Education, Education, Public Research University, and Malaysia.


  The Universiti Sains Malaysia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Universiti Sains Malaysia''s developer surface includes engineering blog, support, code examples, authentication, and 21 more developer resources.'
plans:
- name: Usm Plans Pricing
  plan_count: 2
  slug: usm-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Usm Rate Limits
  slug: usm-rate-limits
rules:
- effective_rule_count: 8
  extends: []
  name: Universiti Sains Malaysia API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: usm-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 41.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 7.9
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 11.4
    contract_quality: 27.5
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 21.1
  previous_composite: 26.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/usm/refs/heads/main/screenshots/usm-2026-06-20T200723.png
security:
- kind: authentication
  name: Usm Authentication
  slug: usm-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Usm Domain Security
  slug: usm-domain-security
  summary_line: TLSv1.3
slug: usm
tags:
- University
- Higher Education
- Education
- Public Research University
- Malaysia
- Southeast Asia
- Research
- Open Access
- Institutional Repository
- OAI-PMH
- EPrints
- Identity Federation
- Shibboleth
- SAML
- Crossref
website: https://www.usm.my/en/
---
