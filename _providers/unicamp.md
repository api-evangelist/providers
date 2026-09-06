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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REDU (Repositorio de Dados de Pesquisa da Unicamp) is Unicamp's institutional research data repository, self-hosted on the open-source Dataverse platform at redu.unicamp.br - a Unicamp-owned host, not
  name: REDU Dataverse Native & Search API
  slug: redu-dataverse-api
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for REDU, on Unicamp''s own host. Verified live 2026-09-01: verb=Identify returns 200 for repository "Repositorio de Dados de Pesquisa da Unicamp Dataverse OAI '
  name: REDU OAI-PMH Metadata Endpoint
  slug: redu-oai-pmh
- baseURL: https://api.dados.unicamp.br
  baseurl_source: declared
  description: API gateway (Kong) for Unicamp's Escritorio de Dados e Apoio a Tomada de Decisao (EDAT), the university's data office. It backs catalogo.dados.unicamp.br and apoio.dados.unicamp.br. Verified live 2026
  name: EDAT Data Platform API
  slug: edat-data-api
- description: 'Unicamp-operated Keycloak authorization server (realm `edat`) that issues the credentials for the EDAT data platform. Verified live 2026-09-01: the OIDC discovery document at /realms/edat/.well-known/'
  name: EDAT Keycloak OpenID Connect Provider
  slug: edat-keycloak-oidc
- description: Unicamp's own SAML 2.0 / Shibboleth identity provider, entityID https://cafe.unicamp.br/idp/shibboleth, registered in CAFe - RNP's Brazilian academic identity federation and an eduGAIN participant. Th
  name: Unicamp Shibboleth Identity Provider (CAFe)
  slug: cafe-shibboleth-idp
- description: Unicamp's library system (SBU) self-hosts the Portal de Periodicos Eletronicos Cientificos on Open Journal Systems 3.4.0.9 at periodicos.sbu.unicamp.br, with a per-journal OAI-PMH endpoint. Verified l
  name: SBU Journal Portal OAI-PMH Endpoints
  slug: sbu-periodicos-oai
- description: API host of the Diretoria Academica (DAC), Unicamp's registrar, which runs the course catalogs, enrollment and academic records. Resolves to Unicamp-operated addresses (177.220.121.139-141) and is liv
  name: DAC Registrar API (closed)
  slug: dac-registrar-api
- description: Unicamp's central API gateway. The hostname is Unicamp's; the gateway platform is Sensedia (api.unicamp.br CNAMEs to alias.b3r06ix53m-gateway-default.sensedia.net behind an AWS sa-east-1 load balancer
  name: Institutional API Gateway (api.unicamp.br)
  slug: institutional-api-gateway
- description: 'Unicamp is a DataCite provider (member) in its own right, not merely a client of one. Verified 2026-09-01: https://api.datacite.org/providers/unicamp returns 200 - id `unicamp`, symbol UNICAMP, member'
  name: DataCite Membership and DOI Registration
  slug: datacite-membership
- description: 'Unicamp is Crossref member 27633, "Universidade Estadual de Campinas", registering DOIs for its SBU journal portal and other scholarly output. Verified 2026-09-01: https://api.crossref.org/members/276'
  name: Crossref Membership
  slug: crossref-membership
- description: Unicamp is registered in the Research Organization Registry as https://ror.org/04wffgt70, with domain unicamp.br, established 1966, and cross-references to GRID (grid.411087.b), ISNI (0000 0001 0723 2
  name: ROR Organization Registration
  slug: ror-registration
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unicamp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unicamp.br/
- group: company
  title: ''
  type: LinkedIn
  url: https://br.linkedin.com/school/universidade-estadual-de-campinas/
- group: commercial
  title: ''
  type: Plans
  url: plans/unicamp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unicamp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unicamp-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: OpenData
  url: https://catalogo.dados.unicamp.br/
- group: other
  title: ''
  type: OpenData
  url: https://transparencia.unicamp.br/
- group: other
  title: ''
  type: ResearchRepository
  url: https://redu.unicamp.br/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.sbu.unicamp.br/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.dac.unicamp.br/portal/graduacao/catalogos-de-cursos
- group: other
  title: ''
  type: IdentityFederation
  url: https://cafe.unicamp.br/idp/shibboleth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacidade.dados.unicamp.br/politica-de-privacidade/
- group: operate
  title: ''
  type: Support
  url: https://www.dados.unicamp.br/fale-com-o-edat/
- group: design
  title: ''
  type: Conformance
  url: conformance/unicamp-conformance.yml
created: '2026-06-03'
description: 'The University of Campinas (Universidade Estadual de Campinas, Unicamp) is a public research university in Campinas, Sao Paulo, Brazil, and one of Latin America''s largest producers of research output. It publishes no central developer portal and no public API documentation, but it does operate more machine-readable surface than that absence suggests, and all of it sits on its own registrable domain: REDU, a self-hosted Dataverse 6.2 research data repository with a live Native/Search API and an OAI-PMH endpoint over 2,149 datasets; the EDAT data platform, whose Kong gateway at api.dados.unicamp.br serves at least one publicly callable JSON endpoint and gates the rest behind Unicamp''s own Keycloak realm with full OIDC discovery; per-journal OAI-PMH across the SBU journal portal; and a Shibboleth identity provider registered in CAFe, Brazil''s academic identity federation. Two further gateways are live but closed - the registrar API at api.dac.unicamp.br (403 on every path)
  and an institutional Sensedia gateway at api.unicamp.br (routing but no public route). Unicamp is also a DataCite provider in its own right and a Crossref member. Nothing here is documented for third-party developers; the contracts in this repo were reconstructed by probe, not published by the university.'
finops:
- name: Unicamp Finops
  service_category: Education
  slug: unicamp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unicamp.png
jsonld:
- class_count: 10
  name: Unicamp Context
  property_count: 4
  slug: unicamp-context
layout: provider
modified: '2026-09-01'
name: University of Campinas
nav: Providers
network: true
overview: 'University of Campinas publishes 1 API on the [APIs.io](https://apis.io/) network: EDAT Data Platform API. Tagged areas include Education, Higher Education, University, Public Research University, and Brazil.


  The University of Campinas catalog on APIs.io includes 1 JSON-LD context.


  University of Campinas'' developer surface includes support and 15 more developer resources.'
plans:
- name: Unicamp Plans Pricing
  plan_count: 2
  slug: unicamp-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Unicamp Rate Limits
  slug: unicamp-rate-limits
scopes:
- name: Unicamp Edat Oidc Scopes
  scope_count: 0
  slug: unicamp-edat-oidc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 59.5
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 49.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unicamp/refs/heads/main/screenshots/unicamp-2026-06-20T200024.png
security:
- kind: authentication
  name: Unicamp Edat Oidc Authentication
  slug: unicamp-edat-oidc-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Unicamp Domain Security
  slug: unicamp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: unicamp
tags:
- Education
- Higher Education
- University
- Public Research University
- Brazil
- Latin America
- Research Data
- Open Data
- Research Repository
- Identity Federation
- OAI-PMH
- Dataverse
- Course Catalog
website: https://www.unicamp.br/
---
