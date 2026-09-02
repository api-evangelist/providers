---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
api_count: 10
apis:
- description: The University of Chile self-hosts a Dataverse installation at datos.uchile.cl on its own network (200.89.78.15, the same /16 as uchile.cl), administered from repositoriodedatos@uchile.cl. The REST AP
  name: UChile Research Data Repository API (Dataverse)
  slug: datos-dataverse-api
- description: 'OAI-PMH 2.0 provider on the University of Chile Dataverse installation. Confirmed live on 2026-09-01: ?verb=Identify returned 200 with repositoryName "Repositorio de datos de investigación de la Unive'
  name: UChile Research Data Repository OAI-PMH
  slug: datos-oai-pmh
- description: OAI-PMH 2.0 provider on the University of Chile institutional repository (Repositorio Académico), managed by SISIB and built on DSpace. CONFIRMED LIVE on 2026-09-01, correcting the June 2026 profile w
  name: Repositorio Académico OAI-PMH
  slug: repositorio-oai-pmh
- description: 'The DSpace 6 REST API on the University of Chile institutional repository, not catalogued before this run. Confirmed live and open for read on 2026-09-01: GET /rest/test returned 200 "REST api is runn'
  name: Repositorio Académico DSpace REST API
  slug: repositorio-dspace-rest
- description: U-Campus is the University of Chile's own academic and curricular management platform, built in-house by the Área de Infotecnologías of the Facultad de Ciencias Físicas y Matemáticas and extended acro
  name: U-Campus Academic Management API
  slug: ucampus-api
- description: U-Cursos is the course-management platform used across University of Chile faculties, built on the same U-Campus codebase and now productised by Centro Tecnológico Ucampus (ucampus.cl) for other Chile
  name: U-Cursos API
  slug: ucursos-api
- description: 'Library discovery for the University of Chile runs on Ex Libris (Clarivate) Primo VE at catalogo.uchile.cl, institution code 56UDC_INST. Probed 2026-09-01: the bare host 200s into /mng/login (the Alma'
  name: Catálogo Bibliotecas UChile (Ex Libris Primo VE)
  slug: catalogo-primo
- description: 'The University of Chile is a DataCite member, not a DataCite operator. Evidenced 2026-09-01 from the DataCite REST API: provider UCHILE (memberType consortium, rorId https://ror.org/047gc3g35, country'
  name: DataCite membership and repository registration
  slug: datacite-membership
- description: The University of Chile is a Crossref member, id 3330, primary name "Universidad de Chile", DOI prefix 10.5354, with 2,330 current DOIs recorded at probe time (2026-09-01). Used for the university's j
  name: Crossref membership
  slug: crossref-membership
- description: 'The University of Chile''s Research Organization Registry record: https://ror.org/047gc3g35, established 1842, declared domain uchile.cl, last modified 2026-08-25 (ROR schema 2.1). Confirmed 200 from t'
  name: ROR organization record
  slug: ror-record
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://uchile.cl/
- group: other
  title: ''
  type: OpenData
  url: https://datos.uchile.cl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositorio.uchile.cl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogo.uchile.cl/discovery/search?vid=56UDC_INST:56UDC_INST
- group: learn
  title: ''
  type: CourseCatalog
  url: https://ucampus.uchile.cl/
- group: other
  title: ''
  type: AIPolicy
  url: https://uchile.cl/informacion-y-bibliotecas/lineamientos-uso-ia-en-tesis
- group: docs
  title: ''
  type: Documentation
  url: https://guides.dataverse.org/en/latest/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eol-uchile
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-uchile
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-de-chile/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-chile-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-chile-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-chile-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-chile-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-chile-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-chile-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-chile-context.jsonld
created: '2026-06-03'
description: 'The University of Chile (Universidad de Chile, UChile) is the country''s oldest public university, founded in 1842 in Santiago, and Chile''s largest research institution (ROR 047gc3g35, domain uchile.cl). Its programmable footprint is entirely scholarly infrastructure and is real but SMALL: the institution self-hosts a Dataverse research data repository at datos.uchile.cl (Dataverse 5.13, build 1244-79d6e57, administered from repositoriodedatos@uchile.cl) and a DSpace institutional repository at repositorio.uchile.cl, and both answer machine calls today — a Dataverse REST API and OAI-PMH provider on the first, a DSpace 6 REST API and OAI-PMH provider on the second. It also runs U-Campus (ucampus.uchile.cl), the academic-management platform built in-house at the Facultad de Ciencias Físicas y Matemáticas, whose /api/ path answers with structured JSON but is authenticated and undocumented. What UChile does NOT have is engineering of its own behind any of it: every contract on
  those hosts is the product''s, generated by Dataverse or DSpace and identical to every other deployment of that software, so no OpenAPI is carried in this repo. There is no central developer portal, no self-service key issuance, no published API terms of use (the Dataverse install answers apiTermsOfUse with "There are no API Terms of Use"), no llms.txt and no security.txt. The institution is a registrant rather than a publisher: a DataCite member (UCHILE) and repository client (UCHILE.DATAVERSE, prefix 10.34691, 5,709 DOIs) and a Crossref member (id 3330, prefix 10.5354, 2,330 current DOIs). Library discovery runs on Ex Libris Primo VE (catalogo.uchile.cl, institution code 56UDC_INST) as a tenant, not as a UChile contract. No UChile Shibboleth or SAML identity provider is published in the eduGAIN metadata aggregate, and Chile''s COFRe federation carries no uchile.cl entity — the one strong institution-operated identity surface most universities have is absent here.'
examples:
- key_count: 5
  name: University Of Chile Info Version Example
  slug: university-of-chile-info-version-example
- key_count: 5
  name: University Of Chile Search Example
  slug: university-of-chile-search-example
finops:
- name: University Of Chile Finops
  service_category: Education
  slug: university-of-chile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-chile.png
jsonld:
- class_count: 21
  name: University Of Chile Context
  property_count: 7
  slug: university-of-chile-context
layout: provider
modified: '2026-09-01'
name: University of Chile
nav: Providers
network: true
overview: 'University of Chile publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Public University, and Research Data.


  The University of Chile catalog on APIs.io includes 1 JSON-LD context.


  University of Chile''s developer surface includes documentation and 17 more developer resources.'
plans:
- name: University Of Chile Plans Pricing
  plan_count: 2
  slug: university-of-chile-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: University Of Chile Rate Limits
  slug: university-of-chile-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -3.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 16.1
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 28.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-chile/refs/heads/main/screenshots/university-of-chile-2026-06-20T200146.png
security:
- kind: domain-security
  name: University Of Chile Domain Security
  slug: university-of-chile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-chile
tags:
- Education
- Higher Education
- University
- Public University
- Research Data
- Research Repository
- Open Access
- OAI-PMH
- Dataverse
- DSpace
- Persistent Identifiers
- Chile
- Latin America
- Spanish Language
website: https://uchile.cl/
---
