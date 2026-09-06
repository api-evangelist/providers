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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-05'
api_count: 9
apis:
- description: 'HAL-based REST API for Biblos-e Archivo, UAM''s institutional repository, running DSpace 7.6.5. Anonymously readable, HATEOAS-navigable access to communities, collections, items, bitstreams, discovery '
  name: Biblos-e Archivo REST API (DSpace 7)
  slug: biblos-rest
- description: OAI-PMH 2.0 metadata-harvesting endpoint for Biblos-e Archivo. Identify returns repositoryName "Biblos-e Archivo. Repositorio Institucional de la UAM", baseURL https://repositorio.uam.es/server/oai/re
  name: Biblos-e Archivo OAI-PMH Endpoint
  slug: biblos-oai
- description: OAI-PMH 2.0 endpoint over the university's Open Journal Systems 3.3.0.6 installation, which hosts UAM's electronic journals under a UAM-built theme ("cantoblanco"). Identify returns repositoryName "Po
  name: Portal de Revistas Electrónicas de la UAM — OAI-PMH Endpoint
  slug: revistas-oai
- description: 'UAM''s SAML 2.0 identity in SIR, the Servicio de Identidad de RedIRIS, Spain''s national research and education federation and an eduGAIN participant. entityID https://www.rediris.es/sir/uamidp, shibmd:'
  name: UAM Identity Provider — SIR / eduGAIN SAML 2.0 Metadata
  slug: idp-federation
- description: 'UAM self-hosts two Moodle learning platforms, Grado 2026/27 at moodle.uam.es and Posgrado at posgrado.uam.es, both acting as LTI 1.3 / LTI Advantage platforms. Each publishes live public signing keys '
  name: UAM Moodle — LTI 1.3 Platform and Web Services
  slug: moodle-lti
- description: UAM's publications service is a Crossref member (member id 6788) and mints DOIs under prefix 10.15366, with 10,886 DOIs registered at time of probe (1,557 current, 9,329 backfile), predominantly for t
  name: Crossref Membership — Servicio de Publicaciones de la UAM
  slug: crossref-member
- description: UAM's Research Organization Registry identifier, https://ror.org/01cby8j38, the canonical machine-readable identifier for the institution across scholarly infrastructure. Recorded as a registry member
  name: ROR Registration — Universidad Autónoma de Madrid
  slug: ror
- description: The UAM library's research-guide platform. biblioguias.uam.es is a UAM hostname CNAMEd to region-eu.libguides.com, Springshare's EU LibGuides service — an institution-specific tenancy on a vendor plat
  name: Biblioguías UAM — Springshare LibGuides Tenancy
  slug: biblioguias
- description: The UAM library's room-booking, appointment and opening-hours platform. biblioagenda.uam.es is a UAM hostname CNAMEd to region-eu.libcal.com, Springshare's EU LibCal service. Campus space and hours da
  name: BiblioAgenda UAM — Springshare LibCal Tenancy
  slug: biblioagenda
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.uam.es/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositorio.uam.es/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/uam-identity-federation.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.uam.es/uam/vida-universitaria/bibliotecas/repositorio
- group: other
  title: ''
  type: SingleSignOn
  url: https://id.uam.es/
- group: auth
  title: ''
  type: Authentication
  url: authentication/uam-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uam-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/uam-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uam-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://es.linkedin.com/school/universidad-autonoma-de-madrid/
created: '2026-06-03'
description: 'The Autonomous University of Madrid (Universidad Autónoma de Madrid, UAM) is a public research university in Madrid, Spain, founded in 1968 and ranked #198 in the QS World University Rankings 2025. UAM publishes no developer portal, no API terms and no OpenAPI description of anything, and it issues no API keys — but unlike most institutions in this cohort its machine-readable surfaces are genuinely its own rather than a vendor''s contract running under its name. Every host carrying a surface below resolves inside RIPE inetnum 150.244.0.0 – 150.244.255.255, netname UAM, org ORG-UADM1-RIPE, with no CNAME to a vendor platform: UAM licenses DSpace, Open Journal Systems and Moodle and runs them on its own address space. What is anonymously consumable today is the Biblos-e Archivo repository (a DSpace 7.6.5 HAL REST API, an OAI-PMH 2.0 endpoint and an OpenSearch descriptor) and a second OAI-PMH 2.0 endpoint over the university''s Open Journal Systems journals portal at revistas.uam.es.
  Beyond that, UAM operates a Shibboleth service provider on its own repository host, is registered as an identity provider in SIR/eduGAIN through RedIRIS, runs two Moodle instances that publish live LTI 1.3 signing keys, and is a Crossref member minting DOIs under prefix 10.15366. No vendor product specification is stored in this repository: a generic DSpace, OJS or Moodle contract describes the vendor''s engineering, not UAM''s.'
examples:
- key_count: 6
  name: Uam Biblos Dspace Root Example
  slug: uam-biblos-dspace-root-example
- key_count: 1
  name: Uam Moodle Lti Jwks Example
  slug: uam-moodle-lti-jwks-example
finops:
- name: Uam Finops
  service_category: Education
  slug: uam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uam.png
jsonld:
- class_count: 8
  name: Uam Context
  property_count: 0
  slug: uam-context
layout: provider
modified: '2026-09-01'
name: Autonomous University of Madrid
nav: Providers
network: true
overview: 'Autonomous University of Madrid publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Spain, and Public Research University.


  The Autonomous University of Madrid catalog on APIs.io includes 1 JSON-LD context.


  Autonomous University of Madrid''s developer surface includes documentation, authentication, code examples, and 12 more developer resources.'
plans:
- name: Uam Plans Pricing
  plan_count: 2
  slug: uam-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Uam Rate Limits
  slug: uam-rate-limits
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 20.5
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 25.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uam/refs/heads/main/screenshots/uam-2026-06-20T195920.png
security:
- kind: authentication
  name: Uam Authentication
  slug: uam-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Uam Domain Security
  slug: uam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uam
tags:
- University
- Higher Education
- Education
- Spain
- Public Research University
- Institutional Repository
- Research Data
- Open Access
- OAI-PMH
- Identity Federation
- Learning Management
- DSpace
- Open Journal Systems
- Shibboleth
website: https://www.uam.es/
---
