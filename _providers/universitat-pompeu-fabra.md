---
access_model:
  confidence: medium
  label: Free · no key required on the probed read endpoints
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: 'e-Repositori (Repositori digital de la UPF) is UPF''s open-access institutional repository, self-hosted on UPF''s own domain. Probed 2026-09-01: GET https://repositori.upf.edu/server/api returns HTTP 20'
  name: UPF Digital Repository REST API (DSpace 7)
  slug: repository-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for e-Repositori, on UPF''s own host. Probed 2026-09-01: verb=Identify returns HTTP 200 text/xml with repositoryName "Repositori digital de la UPF", repositoryI'
  name: UPF Digital Repository OAI-PMH Endpoint
  slug: repository-oai
- description: UPF's institutional single sign-on, registered in eduGAIN through RedIRIS SIR, the Spanish national research and education federation. entityID https://www.rediris.es/sir/upfidp, role IDPSSODescriptor
  name: UPF SAML 2.0 Identity Provider (RedIRIS SIR / eduGAIN)
  slug: identity-federation
- description: 'UPF is a Crossref member and registers DOIs under its own prefix. Probed 2026-09-01: GET https://api.crossref.org/members/14960 returns HTTP 200 with primary-name "Universitat Pompeu Fabra", prefixes '
  name: Crossref Membership (member 14960, prefix 10.31009)
  slug: crossref-member
- description: 'UPF''s entry in the Research Organization Registry. Probed 2026-09-01: GET https://api.ror.org/v2/organizations/04n0g0b29 returns HTTP 200 application/json with ror_display "Universitat Pompeu Fabra". '
  name: ROR Registration (04n0g0b29)
  slug: ror
- description: 'guiesbibtic.upf.edu is UPF Library/CRAI''s guides platform and the host of its generative-AI guidance for students and staff. It is not UPF-operated software: DNS resolves guiesbibtic.upf.edu as a CNAM'
  name: Guies BibTIC (Springshare LibGuides tenant)
  slug: libguides
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.upf.edu/en/home
- group: docs
  title: ''
  type: APIReference
  url: https://repositori.upf.edu/server/api
- group: docs
  title: ''
  type: Documentation
  url: https://repositori-api.upf.edu/oai/request?verb=Identify
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositori.upf.edu
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.rediris.es/sir/upfidp
- group: build
  title: ''
  type: LibraryCatalog
  url: https://guiesbibtic.upf.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://guiesbibtic.upf.edu/iag
- group: build
  title: ''
  type: AITooling
  url: https://guiesbibtic.upf.edu/prestatges-virtuals/IA_ensenyament
- group: auth
  title: ''
  type: Authentication
  url: https://repositori.upf.edu/server/api/authn
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MTG
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitat-pompeu-fabra/
- group: design
  href: https://artifacts.apis.io/universitat-pompeu-fabra/conformance/universitat-pompeu-fabra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/universitat-pompeu-fabra-conformance.yml
- group: design
  href: https://artifacts.apis.io/universitat-pompeu-fabra/json-ld/universitat-pompeu-fabra-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/universitat-pompeu-fabra-context.jsonld
- group: auth
  href: https://artifacts.apis.io/universitat-pompeu-fabra/security/universitat-pompeu-fabra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/universitat-pompeu-fabra-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/universitat-pompeu-fabra/plans/universitat-pompeu-fabra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/universitat-pompeu-fabra-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/universitat-pompeu-fabra/rate-limits/universitat-pompeu-fabra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/universitat-pompeu-fabra-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/universitat-pompeu-fabra/finops/universitat-pompeu-fabra-finops.yml
  title: ''
  type: FinOps
  url: finops/universitat-pompeu-fabra-finops.yml
- group: other
  href: https://artifacts.apis.io/universitat-pompeu-fabra/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universitat Pompeu Fabra (UPF) is a public research university in Barcelona, Catalonia, Spain, founded in 1990 and ranked #266 in the QS World University Rankings 2025. UPF operates no developer portal and publishes no OpenAPI, AsyncAPI or SDK of its own; a re-profile on 2026-09-01 probed every candidate host and found none. What it does operate, verified live, is the UPF Digital Repository (e-Repositori) at repositori.upf.edu — self-hosted on UPF''s own domain running DSpace 7.6.8, whose REST/HAL API answers at /server/api with 67 link relations over 78 communities, 1,022 collections and 43,503 discoverable objects, and whose OAI-PMH 2.0 endpoint answers verb=Identify at repositori-api.upf.edu with 13 metadata formats and 100 sets. The repository, the host and the content are UPF''s; the API contract is the DSpace project''s generic open-source one and is deliberately not saved here. The same host runs a real Shibboleth SP — the REST API returns WWW-Authenticate: shibboleth
  with a Shibboleth.sso/Login location — and UPF''s own SAML 2.0 Identity Provider is registered in eduGAIN through RedIRIS SIR, the Spanish national research and education federation, as entityID https://www.rediris.es/sir/upfidp with shibmd:Scope upf.edu, Sirtfi asserted and the REFEDS Research and Scholarship entity category. UPF is a Crossref member (member 14960, DOI prefix 10.31009, 1,593 DOIs) and holds ROR 04n0g0b29; it has no DataCite client of its own. The "UPF en Xifres 2.0" linked open data portal that the June 2026 profile was built around — a CKAN action API and a Virtuoso SPARQL endpoint at data.upf.edu — no longer exists: data.upf.edu returns an authoritative NXDOMAIN from UPF''s own nameservers, and both entries have been removed. Most other UPF software is published by research groups, above all the Music Technology Group on GitHub, rather than as institutional APIs.'
finops:
- has_sources: true
  method: generated
  name: Universitat Pompeu Fabra Finops
  primary_unit: ''
  service_category: Education
  slug: universitat-pompeu-fabra-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universitat-pompeu-fabra.png
jsonld:
- class_count: 24
  name: Universitat Pompeu Fabra Context
  property_count: 3
  slug: universitat-pompeu-fabra-context
layout: provider
modified: '2026-09-01'
name: Universitat Pompeu Fabra
nav: Providers
network: true
overview: 'Universitat Pompeu Fabra is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Public Research University, and Spain.


  The Universitat Pompeu Fabra catalog on APIs.io includes 1 JSON-LD context.


  Universitat Pompeu Fabra''s developer surface includes API reference, documentation, authentication, GitHub presence, and 14 more developer resources.'
plans:
- name: Universitat Pompeu Fabra Plans Pricing
  plan_count: 2
  slug: universitat-pompeu-fabra-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Universitat Pompeu Fabra Rate Limits
  slug: universitat-pompeu-fabra-rate-limits
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 71.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 20.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/universitat-pompeu-fabra/universitat-pompeu-fabra-2026-06-20T200116.png
security:
- kind: domain-security
  name: Universitat Pompeu Fabra Domain Security
  slug: universitat-pompeu-fabra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: universitat-pompeu-fabra
tags:
- University
- Higher Education
- Education
- Public Research University
- Spain
- Catalonia
- Barcelona
- Institutional Repository
- Research Data
- Identity Federation
- OAI-PMH
- DSpace
- Shibboleth
- Crossref
website: https://www.upf.edu/en/home
---
