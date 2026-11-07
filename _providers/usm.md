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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 2
apis:
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
- baseURL: https://eprints.usm.my/cgi/oai2
  baseurl_source: declared
  description: EPrints export plugins — one bibliographic serialization per format.
  name: Universiti Sains Malaysia Export API
  slug: usm-export-api
- baseURL: https://eprints.usm.my/cgi/oai2
  baseurl_source: declared
  description: OAI-PMH 2.0 protocol verbs exposed by Repository@USM.
  name: Universiti Sains Malaysia OAI PMH API
  slug: usm-oai-pmh-api
- baseURL: https://eprints.usm.my/cgi/oai2
  baseurl_source: declared
  description: EPrints REST dataset and record access.
  name: Universiti Sains Malaysia Repository API
  slug: usm-repository-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Blog
  url: https://www.usm.my/en/news
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
  href: https://artifacts.apis.io/usm/openapi/_original/usm-repository-oai-pmh-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/usm-repository-oai-pmh-openapi.yml
- group: docs
  href: https://artifacts.apis.io/usm/openapi/_original/usm-repository-eprints-rest-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/usm-repository-eprints-rest-openapi.yml
- group: docs
  href: https://artifacts.apis.io/usm/json-schema/usm-eprint-record.json
  title: ''
  type: JSONSchema
  url: json-schema/usm-eprint-record.json
- group: build
  href: https://artifacts.apis.io/usm/examples/usm-repository-examples.yml
  title: ''
  type: Examples
  url: examples/usm-repository-examples.yml
- group: design
  href: https://artifacts.apis.io/usm/errors/usm-repository-oai-pmh-errors.yml
  title: ''
  type: Errors
  url: errors/usm-repository-oai-pmh-errors.yml
- group: auth
  href: https://artifacts.apis.io/usm/authentication/usm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usm-authentication.yml
- group: design
  href: https://artifacts.apis.io/usm/conformance/usm-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usm-education-standards-conformance.yml
- group: design
  href: https://artifacts.apis.io/usm/vocabulary/usm-repository-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usm-repository-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usm/lifecycle/usm-repository-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usm-repository-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/usm/rules/usm-rules.yml
  title: ''
  type: Rules
  url: rules/usm-rules.yml
- group: design
  href: https://artifacts.apis.io/usm/json-ld/usm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usm-context.jsonld
- group: auth
  href: https://artifacts.apis.io/usm/security/usm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usm-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/usm/plans/usm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usm-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/usm/rate-limits/usm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/usm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/usm/finops/usm-finops.yml
  title: ''
  type: FinOps
  url: finops/usm-finops.yml
- group: other
  href: https://artifacts.apis.io/usm/review.yml
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
- has_sources: true
  method: generated
  name: Usm Finops
  primary_unit: ''
  service_category: Education
  slug: usm-finops
  template: false
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
modified: '2026-10-06'
name: Universiti Sains Malaysia
nav: Providers
network: true
overview: 'Universiti Sains Malaysia publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Export API, OAI PMH API, Repository API, and 4 more. Tagged areas include University, Higher Education, Education, Public Research University, and Malaysia.


  The Universiti Sains Malaysia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Universiti Sains Malaysia''s developer surface includes engineering blog, support, code examples, authentication, and 22 more developer resources.'
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
- authorship: derived
  effective_rule_count: 8
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
  composite: 26.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.2
    catalog_earned_first_party: 0.0
    catalog_gap: 56.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 11.4
    contract_quality: 27.2
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - malaysia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 26.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/usm/usm-2026-06-20T200723.png
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
