---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The university's own Shibboleth/SAML identity provider, published through RedIRIS's SIR2 national identity federation and interfederated into eduGAIN. This is the institution's strongest institution-o
  name: Institutional SAML Identity Provider (RedIRIS SIR2 / eduGAIN)
  slug: sir2-edugain-idp
- description: The University of Navarra is a Crossref member and registers DOIs under its own prefix 10.15581 — 33,267 DOIs as of 2026-09-01 (1,699 current, 31,568 backfile). Sampled works resolve to journals publi
  name: Crossref Membership (DOI prefix 10.15581)
  slug: crossref-member
- description: The institution's entry in the Research Organization Registry, the open identifier used to disambiguate research affiliations. Distinct from the neighbouring and frequently confused Universidad Public
  name: ROR Registration
  slug: ror
- description: DADUN (Deposito Academico Digital de la Universidad de Navarra) is the university's open-access institutional repository, running DSpace and exposing a standard OAI-PMH 2.0 interface for harvesting Du
  name: DADUN Institutional Repository (OAI-PMH)
  slug: dadun-oai-pmh
- description: Unika is the university library's discovery layer, an Ex Libris Primo VE tenancy. Primo's public "primaws" REST interface answers unauthenticated JSON search requests against the institution's own vie
  name: Unika Library Discovery (Ex Libris Primo VE tenancy)
  slug: unika-primo
- description: 'The university''s current research information system (CRIS) and public research portal, listing researchers, research units, publications and projects. It runs as a hosted Dialnet CRIS tenancy rather '
  name: Portal Cientifico (Dialnet CRIS tenancy)
  provenance: unpublished
  slug: portal-cientifico
- description: The library's guides platform, including the institution's public generative AI guidance for students and researchers (definitions, ethics, tooling). Hosted on Springshare LibGuides; the guidance cont
  name: BiblioGuias (Springshare LibGuides tenancy)
  slug: biblioguias
- baseURL: https://revistas.unav.edu/index.php/index/oai
  baseurl_source: declared
  description: OAI-PMH 2.0 verbs for harvesting scholarly metadata
  name: University of Navarra Harvesting API
  slug: university-of-navarra-harvesting-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://en.unav.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.unav.edu/web/biblioteca/apoyo-investigador/acceso-abierto-dadun
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unav.edu/informacion-legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unav.edu/proteccion-de-datos
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.unav.edu/web/biblioteca/apoyo-investigador/acceso-abierto-dadun
- group: build
  title: ''
  type: LibraryCatalog
  url: https://unika.unav.edu/discovery/search?vid=34UNAV_INST:VU1
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.rediris.es/sir/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unav.edu/documents/10162/161278125/Politica+IA.pdf
- group: build
  title: ''
  type: AITooling
  url: https://biblioguias.unav.edu/inteligencia-artificial-generativa
- group: docs
  href: https://artifacts.apis.io/university-of-navarra/openapi/_original/university-of-navarra-revistas-oai-pmh-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/university-of-navarra-revistas-oai-pmh-openapi.yml
- group: auth
  href: https://artifacts.apis.io/university-of-navarra/authentication/university-of-navarra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-navarra-authentication.yml
- group: design
  href: https://artifacts.apis.io/university-of-navarra/conformance/university-of-navarra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-navarra-conformance.yml
- group: build
  href: https://artifacts.apis.io/university-of-navarra/examples/index.yml
  title: ''
  type: Examples
  url: examples/index.yml
- group: auth
  href: https://artifacts.apis.io/university-of-navarra/security/university-of-navarra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-navarra-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-de-navarra-cp
- group: commercial
  href: https://artifacts.apis.io/university-of-navarra/plans/university-of-navarra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-navarra-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/university-of-navarra/rate-limits/university-of-navarra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-navarra-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-navarra/finops/university-of-navarra-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-navarra-finops.yml
- group: other
  href: https://artifacts.apis.io/university-of-navarra/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Navarra (Universidad de Navarra) is a private research university founded in 1952, headquartered in Pamplona, Spain, with campuses in San Sebastian, Madrid and Barcelona. Its programmable footprint is small, and most of it is bought rather than built: the library discovery layer is an Ex Libris Primo VE tenancy, the DADUN institutional repository runs on a hosted DSpace whose host CNAMEs to a third-party platform, the research portal is a Dialnet CRIS tenancy operated by Fundacion Dialnet, and the library guides are Springshare LibGuides. Three surfaces are genuinely the institution''s own. The Servicio de Publicaciones operates a self-hosted Open Journal Systems instance at revistas.unav.edu with a live, unauthenticated OAI-PMH 2.0 harvesting interface across 100 sets — the only institution-operated machine-readable API confirmed here. The university runs its own SAML Identity Provider, published through the RedIRIS SIR2 federation and interfederated into
  eduGAIN since 2018 with REFEDS Sirtfi declared. And it is a Crossref member with its own DOI prefix, 10.15581, covering more than 33,000 registered DOIs. There is no central developer portal, no open-data platform, no documented registrar, timetable or campus API, and no verifiable institutional GitHub organization.'
finops:
- has_sources: true
  method: generated
  name: University Of Navarra Finops
  primary_unit: ''
  service_category: Education
  slug: university-of-navarra-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-navarra.png
jsonld:
- class_count: 25
  name: University Of Navarra Context
  property_count: 2
  slug: university-of-navarra-context
layout: provider
modified: '2026-09-16'
name: University of Navarra
nav: Providers
network: true
overview: 'University of Navarra publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Harvesting API. Tagged areas include Education, Higher Education, University, Spain, and Private Research University.


  The University of Navarra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Navarra''s developer surface includes documentation, authentication, code examples, and 16 more developer resources.'
plans:
- name: University Of Navarra Plans Pricing
  plan_count: 2
  slug: university-of-navarra-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: University Of Navarra Rate Limits
  slug: university-of-navarra-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: University of Navarra API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: university-of-navarra-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.5
    catalog_earned_first_party: 0.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 22.5
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 18.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
screenshot: https://apis.io/screenshots/university-of-navarra/university-of-navarra-2026-06-20T200213.png
security:
- kind: authentication
  name: University Of Navarra Authentication
  slug: university-of-navarra-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Navarra Domain Security
  slug: university-of-navarra-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-navarra
tags:
- Education
- Higher Education
- University
- Spain
- Private Research University
- Open Access
- Institutional Repository
- Scholarly Publishing
- OAI-PMH
- Identity Federation
- Library
website: https://en.unav.edu/
---
