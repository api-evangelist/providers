---
access_model:
  confidence: medium
  label: Free · no key required on the probed endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
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
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: 'Docta Complutense is UCM''s open-access institutional repository, migrated in 2023 to DSpace 7 and self-hosted on UCM''s own domain. Probed 2026-08-30: GET https://docta.ucm.es/rest/api returns HTTP 200'
  name: Docta Complutense Repository API (DSpace 7)
  slug: docta-complutense
- description: 'OAI-PMH 2.0 harvesting endpoint for Docta Complutense, on UCM''s own host. Probed 2026-08-30: verb=Identify returns HTTP 200 text/xml with repositoryName "Docta Complutense", repositoryIdentifier docta'
  name: Docta Complutense OAI-PMH Endpoint
  slug: docta-oai-pmh
- description: UCM's institutional single sign-on, registered in eduGAIN through RedIRIS SIR, the Spanish national research and education federation. entityID https://www.rediris.es/sir/ucmidp, role IDPSSODescriptor
  name: UCM SAML 2.0 Identity Provider (RedIRIS SIR / eduGAIN)
  slug: identity-federation
- description: DataStore query API of UniversiDATA, the DKAN open-data platform shared by five Spanish public universities (UAM, UCM, UHU, UVa, URJC) of which UCM is a founding member. Returns the records of a publi
  name: UniversiDATA DataStore API
  slug: universidata-datastore
- description: 'CKAN-compatible metadata API of the UniversiDATA consortium platform, supporting current_package_list_with_resources, package_show and resource_show. Probed 2026-08-30: HTTP 200 application/json retur'
  name: UniversiDATA CKAN Dataset API
  slug: universidata-ckan
- description: 'DCAT catalogue endpoint of UniversiDATA, addressed per participating university by acronym. The UCM catalogue is the only UCM-specific path on this host. Probed 2026-08-30: the previously recorded bas'
  name: UniversiDATA DCAT Catalog API
  slug: universidata-dcat
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.ucm.es/
- group: docs
  title: ''
  type: Documentation
  url: https://www.universidata.es/el-api
- group: docs
  title: ''
  type: APIReference
  url: https://docta.ucm.es/rest
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.universidata.es/el-api
- group: other
  title: ''
  type: OpenData
  url: https://www.ucm.es/portaldetransparencia/datos-abiertos
- group: other
  title: ''
  type: ResearchRepository
  url: https://docta.ucm.es/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.rediris.es/sir/ucmidp
- group: build
  title: ''
  type: LibraryCatalog
  url: https://biblioteca.ucm.es/
- group: other
  title: ''
  type: AIPolicy
  url: https://bouc.ucm.es/pdf/5785.pdf
- group: build
  title: ''
  type: AITooling
  url: https://ssii.ucm.es/herramientas-ia-generativa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucm.es/aviso-legal
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversidadComplutense
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-complutense-de-madrid/
- group: design
  title: ''
  type: Conformance
  url: conformance/complutense-university-of-madrid-conformance.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/complutense-university-of-madrid-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/complutense-university-of-madrid-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/complutense-university-of-madrid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/complutense-university-of-madrid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/complutense-university-of-madrid-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universidad Complutense de Madrid (UCM) is Spain''s largest public research university, founded 1499 and ranked #164 in the QS World University Rankings 2025. UCM operates no central developer portal and publishes no OpenAPI, AsyncAPI or SDK of its own — a re-profile on 2026-08-30 probed every candidate host and found none. What it does operate, verified live, is two things. First, Docta Complutense (docta.ucm.es), its institutional repository, self-hosted on UCM''s own domain running DSpace 7.6.5: the DSpace REST/HAL API answers at /rest/api and an OAI-PMH 2.0 endpoint answers verb=Identify at /rest/oai/request with twelve metadata formats. The repository is UCM''s; the API contract is DSpace''s open-source one and is not saved here. Second, UCM is registered in eduGAIN through the Spanish RedIRIS SIR federation as a SAML 2.0 Identity Provider (entityID https://www.rediris.es/sir/ucmidp, scope ucm.es, Sirtfi asserted) — machine-readable, institution-scoped, but hosted on RedIRIS
  infrastructure, so recorded as a tenant relationship. UCM''s open data is not self-hosted either: it is published through UniversiDATA, a five-university DKAN consortium portal (UAM, UCM, UHU, UVa, URJC) that exposes DataStore, CKAN and DCAT APIs. Thirteen of the portal''s seventy-one datasets are UCM''s — degree programmes, faculties, departments, budgets, mobility and procurement. UCM''s data, the consortium''s platform, so every UniversiDATA surface below is x-operator tenant, not institution. No course/timetable API, no library discovery API, no research-computing or campus-life API was found on any ucm.es host.'
finops:
- name: Complutense University Of Madrid Finops
  service_category: Education
  slug: complutense-university-of-madrid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/complutense-university-of-madrid.png
jsonld:
- class_count: 20
  name: Complutense University Of Madrid Context
  property_count: 0
  slug: complutense-university-of-madrid-context
layout: provider
modified: '2026-08-30'
name: Complutense University of Madrid
nav: Providers
network: true
overview: 'Complutense University of Madrid publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Public Research University, and Spain.


  The Complutense University of Madrid catalog on APIs.io includes 1 JSON-LD context.


  Complutense University of Madrid''s developer surface includes documentation, API reference, GitHub presence, and 17 more developer resources.'
plans:
- name: Complutense University Of Madrid Plans Pricing
  plan_count: 2
  slug: complutense-university-of-madrid-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Complutense University Of Madrid Rate Limits
  slug: complutense-university-of-madrid-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 22.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 30.4
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/complutense-university-of-madrid/refs/heads/main/screenshots/complutense-university-of-madrid-2026-06-20T174834.png
security:
- kind: domain-security
  name: Complutense University Of Madrid Domain Security
  slug: complutense-university-of-madrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: complutense-university-of-madrid
tags:
- University
- Higher Education
- Education
- Public Research University
- Spain
- Madrid
- Open Data
- Research Data
- Institutional Repository
- Identity Federation
- OAI-PMH
- DSpace
- DKAN
website: https://www.ucm.es/
---
