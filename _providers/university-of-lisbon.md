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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://fenix.tecnico.ulisboa.pt/api/fenix/v1
  baseurl_source: declared
  description: Public REST API of the FenixEdu academic information system operated by Instituto Superior Tecnico, a school of the University of Lisbon. Anonymous access to institution metadata, academic terms, cont
  name: FenixEdu Academic API (Instituto Superior Tecnico)
  slug: fenixedu-tecnico
- description: OAI-PMH 2.0 metadata harvesting interface over the DSpace 7.6.1 institutional open-access repository. Operating since November 2002; 100,245 items; twelve metadata formats including oai_dc, marcxml, m
  name: Repositorio da Universidade de Lisboa — OAI-PMH
  slug: repositorio-oai-pmh
- description: Anonymous HAL+JSON REST API of the institution's DSpace 7.6.1 repository — communities, collections, items, bitstreams, discovery search, metadata schemas and external-source integrations. The deploym
  name: Repositorio da Universidade de Lisboa — DSpace REST API
  slug: repositorio-dspace-rest
- description: OAI-PMH 2.0 interface over the union library catalog of the 18 schools, the National Museum of Natural History and Science and the Tropical Scientific Research Institute, running on Koha. Serves marcx
  name: Catalogo Coletivo ULisboa (Koha) — OAI-PMH
  slug: catalogo-bibliotecas-oai-pmh
- description: 'The institution''s central SAML 2.0 identity provider, published into the Portuguese national identity federation RCTSaai (operated by FCCN) and onward to eduGAIN. Live machine-readable metadata: IDPSS'
  name: Universidade de Lisboa SAML 2.0 Identity Provider (RCTSaai / eduGAIN)
  slug: identity-federation-ulisboa
- description: The identity provider for Instituto Superior Tecnico, federated through RCTSaai into eduGAIN and asserting SIRTFI incident-response assurance — a stronger security posture than the central IdP declare
  name: Instituto Superior Tecnico SAML 2.0 Identity Provider (RCTSaai / eduGAIN)
  slug: identity-federation-tecnico
- description: 'The institution''s current research information system, an Elsevier Pure tenant (tenant id "ulisbon") presented on a ulisboa.pt hostname. The relationship is real and is recorded here; the CONTRACT is '
  name: ULisboa Research Portal — Elsevier Pure tenancy
  slug: researchportal-pure
- description: The institution's node in the Erasmus Without Paper network, through which student mobility, inter-institutional agreements, learning agreements and transcripts move between European universities mach
  name: Erasmus Without Paper node (HEI ulisboa.pt)
  slug: ewp-node
- description: 'An active DataCite repository client registered to the university''s central services for minting DOIs over the institutional repository. Recorded honestly with its caveat: the DataCite DOI API returns'
  name: DataCite repository membership (QWBT.ULISBOA)
  slug: datacite-membership
- description: The institution's registered ROR identifier — the canonical machine-readable organizational identity used across DataCite, Crossref and OpenAIRE metadata. ROR also holds records for the university's c
  name: ROR organization identifier
  slug: ror-registration
- description: Five ULisboa organic units hold Crossref member IDs in their own right, minting DOIs for their journals independently of the rectorate. There is no single institutional Crossref member — the federated
  name: Crossref memberships (organic units)
  slug: crossref-membership
artifact_total: 32
common:
- group: company
  title: ''
  type: Website
  url: https://www.ulisboa.pt/en
- group: docs
  title: ''
  type: Documentation
  url: https://fenixedu.org/dev/api/
- group: docs
  title: ''
  type: APIReference
  url: https://fenixedu.org/dev/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ULisboa
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ULisboa/ewp-node
- group: learn
  title: ''
  type: CourseCatalog
  url: https://fenix.tecnico.ulisboa.pt/api/fenix/v1/degrees
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositorio.ulisboa.pt/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogo-bibliotecas.ulisboa.pt/
- group: other
  title: ''
  type: IdentityFederation
  url: https://id.ulisboa.pt/nidp/saml2/metadata
- group: other
  title: ''
  type: AIPolicy
  url: https://tecnico.ulisboa.pt/en/news/campus-community/tecnico-apresenta-guia-para-a-utilizacao-responsavel-da-inteligencia-artificial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ulisboa.pt/en/info/terms-use-0
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ulisboa.pt/en/info/cookies-policy
- group: operate
  title: ''
  type: Support
  url: https://www.ulisboa.pt/en/info/contacts-1
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ulisboa.pt/en/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidade-de-lisboa/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-lisbon-fenixedu-academic-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-lisbon-fenixedu-degree.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-lisbon-organization.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/university-of-lisbon-examples.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-lisbon-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-lisbon-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-lisbon-errors.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-lisbon-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-lisbon-vocabulary.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-lisbon-domain-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-lisbon-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-lisbon-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-lisbon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-lisbon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-lisbon-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Lisbon (Universidade de Lisboa, ULisboa) is Portugal''s largest public university — 18 schools plus the National Museum of Natural History and Science — and it is a federation of buyers rather than a producer of APIs. It runs no central developer portal, publishes no OpenAPI of its own, and has no open data portal: data.ulisboa.pt and dados.ulisboa.pt do not resolve, and the institution has no organization on the national portal dados.gov.pt. What it does operate, on its own infrastructure, is a small but real set of standards-based surfaces: the FenixEdu academic API at Instituto Superior Tecnico — institution-authored open-source software serving degrees, courses, campus spaces, blueprints, parking and a 1.2 MB serialized domain model anonymously, with Bennu OAuth 2.0 in front of person-scoped data; two independent OAI-PMH 2.0 endpoints, one over a 100,245-item DSpace 7.6.1 repository running since 2002 and one over the Koha union library catalog; and a
  SAML 2.0 identity provider published into the national RCTSaai federation and onward to eduGAIN, alongside a second IdP for Instituto Superior Tecnico that asserts SIRTFI. The institution also authors an open-source Erasmus Without Paper node on GitHub, which is its most substantive piece of public API engineering. Everything else is someone else''s contract running under its name — most importantly researchportal.ulisboa.pt, which looks institutional and CNAMEs to ulisbon.elsevierpure.com; its own OAI-PMH Identify calls it a "Pure OAI Repository" and its Pure Web Service OpenAPI is behind an API key. Its Erasmus Without Paper node is hosted by another university entirely. Both are recorded here as tenancies, with the vendor contract deliberately left out of this repository.'
examples:
- key_count: 1
  name: Datacite Client Qwbt Ulisboa
  slug: datacite-client-qwbt-ulisboa
- key_count: 7
  name: Fenixedu About
  slug: fenixedu-about
- key_count: 106
  name: Fenixedu Academicterms
  slug: fenixedu-academicterms
- key_count: 12
  name: Fenixedu Degree
  slug: fenixedu-degree
- key_count: 2
  name: Fenixedu Error 401
  slug: fenixedu-error-401
- key_count: 2
  name: Fenixedu Error 404
  slug: fenixedu-error-404
- key_count: 2
  name: Fenixedu Parking
  slug: fenixedu-parking
- key_count: 6
  name: Repositorio Dspace Api Root
  slug: repositorio-dspace-api-root
- key_count: 3
  name: Repositorio Dspace Externalsources
  slug: repositorio-dspace-externalsources
finops:
- name: University Of Lisbon Finops
  service_category: Education
  slug: university-of-lisbon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-lisbon.png
json_schemas:
- name: FenixEdu About
  property_count: 7
  slug: university-of-lisbon-fenixedu-about
- name: FenixEdu Degree
  property_count: 11
  slug: university-of-lisbon-fenixedu-degree
- name: FenixEdu Space
  property_count: 4
  slug: university-of-lisbon-fenixedu-space
jsonld:
- class_count: 36
  name: University Of Lisbon Context
  property_count: 5
  slug: university-of-lisbon-context
- class_count: 0
  name: University Of Lisbon Organization Context
  property_count: 0
  slug: university-of-lisbon-organization
layout: provider
modified: '2026-09-01'
name: University of Lisbon
nav: Providers
network: true
overview: 'University of Lisbon publishes 1 API on the [APIs.io](https://apis.io/) network: FenixEdu Academic API (Instituto Superior Tecnico). Tagged areas include University, Higher Education, Education, Portugal, and Europe.


  The University of Lisbon catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  University of Lisbon''s developer surface includes documentation, API reference, support, code examples, authentication, and 26 more developer resources.'
plans:
- name: University Of Lisbon Plans Pricing
  plan_count: 2
  slug: university-of-lisbon-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Lisbon Rate Limits
  slug: university-of-lisbon-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: University of Lisbon API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 1
  slug: university-of-lisbon-rules
scopes:
- name: University Of Lisbon Scopes
  scope_count: 0
  slug: university-of-lisbon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.0
    catalog_earned_first_party: 0.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 61.2
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 49.6
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
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-lisbon/refs/heads/main/screenshots/university-of-lisbon-2026-06-20T200201.png
security:
- kind: authentication
  name: University Of Lisbon Authentication
  slug: university-of-lisbon-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Lisbon Domain Security
  slug: university-of-lisbon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-lisbon
tags:
- University
- Higher Education
- Education
- Portugal
- Europe
- Public Research University
- Course Catalog
- Research Repository
- Library
- Identity Federation
- OAI-PMH
- Open Access
- Erasmus Without Paper
- Metadata
website: https://www.ulisboa.pt/en
---
