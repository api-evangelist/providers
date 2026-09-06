---
access_model:
  confidence: high
  label: Free and open, no registration on the public surfaces
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Academic Bibliography (Biblio) is Ghent University's institutional publication and dataset registry, operated by Ghent University Library on the university's own host. It exposes a JSON/JSONP REST
  name: Ghent University Academic Bibliography API
  slug: biblio
- baseURL: https://biblio.ugent.be/oai
  baseurl_source: declared
  description: OAI-PMH 2.0 harvesting endpoint for the Academic Bibliography. The live Identify response names the repository "Ghent University Institutional Archive", declares repositoryIdentifier archive.ugent.be,
  name: Ghent University Academic Bibliography OAI-PMH
  slug: biblio-oai
- baseURL: https://biblio.ugent.be/sru
  baseurl_source: declared
  description: 'SRU 1.1 search/retrieve service over the Academic Bibliography, driven by Contextual Query Language. Seventy-eight indexes are documented with their supported relations and sortability, from abstract '
  name: Ghent University Academic Bibliography SRU
  slug: biblio-sru
- baseURL: https://hydra.ugent.be/api/2.0/resto
  baseurl_source: declared
  description: Open JSON API for Ghent University's student restaurants - locations and opening hours, day menus, weekly ecological sandwiches, salad bowls, extra food and allergen information - served from hydra.ug
  name: Hydra Resto API
  slug: hydra-resto
- baseURL: /api/v1
  baseurl_source: spec
  description: An OpenAPI 3.1 contract authored and open-sourced by Ghent University Library for the people and organizations directory behind the Academic Bibliography. Sixteen operations covering person and organi
  name: Ghent University Library People Service
  slug: people-service
- baseURL: /api/v1
  baseurl_source: spec
  description: An OpenAPI 3.1 contract authored and open-sourced by Ghent University Library for the directory of research projects at Ghent University - add, get, delete and suggest operations over project records.
  name: Ghent University Library Projects Service
  slug: projects-service
- baseURL: /api/v1
  baseurl_source: spec
  description: An OpenAPI 3.1 contract authored and open-sourced by Ghent University Library for the administrative side of the OAI-PMH server that fronts the Academic Bibliography - adding metadata formats, sets, i
  name: Ghent University Library OAI Service
  slug: oai-service
- description: Ghent University's own SAML 2.0 identity provider, operated by the university's ICT directorate. The signed metadata document is publicly readable and carries entityID https://identity.ugent.be/simple
  name: Ghent University SAML 2.0 Identity Provider
  slug: saml-idp
- description: 'lib.ugent.be redirects to libcatalog.ugent.be, an Ex Libris Primo VE discovery layer running under institution code 32RUG_INST and resolving through libugent.primo.exlibrisgroup.com. The catalogue is '
  name: Ghent University Library catalogue (Ex Libris Alma/Primo VE tenancy)
  slug: library-catalog
- description: Dodona is the automated programming-practice platform that originated at Ghent University and is still used in its computer-science teaching; Ghent registered it as a service provider in the Belnet R&
  name: Dodona
  slug: dodona
- description: Ghent University is a Crossref member in its own name - member id 9286, DOI prefix 10.21825, registered in Ghent, Belgium, with 28,489 DOIs deposited (960 current, 27,529 backfile) as of 2026-09-01. T
  name: Crossref membership
  slug: crossref
- description: Ghent University is registered in the Research Organization Registry as https://ror.org/00cv9y106, distinct from Ghent University Hospital (https://ror.org/00xmkp704) and HOGENT (https://ror.org/00rs4
  name: ROR registration
  slug: ror
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://www.ugent.be/en
- group: docs
  title: ''
  type: Documentation
  url: https://biblio.ugent.be/doc/api
- group: docs
  title: ''
  type: APIReference
  url: https://biblio.ugent.be/doc/api
- group: other
  title: ''
  type: ResearchRepository
  url: https://biblio.ugent.be
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.ugent.be/catalog
- group: other
  title: ''
  type: IdentityFederation
  url: https://identity.ugent.be/simplesaml/saml2/idp/metadata.php
- group: other
  title: ''
  type: OpenData
  url: https://biblio.ugent.be/doc/api
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ugent
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ugent-library
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ugent-library
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ugent.be/en/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ugent.be/en/ghentuniv/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ghent-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/ghent-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ghent-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/ghent-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ghent-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ghent-biblio-cql-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/ghent-examples.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ghent-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ghent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ghent-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ghent-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Ghent University (Universiteit Gent, UGent) is a public research university in Ghent, Belgium, founded in 1817 and ranked around #169 in the QS World University Rankings. Like almost every institution, it is a federation of buyers rather than an API producer, and its profile is written on that basis: it operates no central developer portal, no gateway and no institution-wide API programme, and most of what looks like a Ghent API on first inspection belongs to a supplier. The real programmable footprint is concentrated in one place - Ghent University Library. The Academic Bibliography at biblio.ugent.be is genuinely the university''s own: a documented JSON/JSONP REST search API, fourteen export formats, a live OAI-PMH 2.0 endpoint identifying itself as the Ghent University Institutional Archive, an SRU 1.1 service over CQL with 78 documented indexes, unAPI discovery, RSS feeds and daily full-dataset dumps, all under the Open Database License. The library also authors and open-sources
  the software behind it, and three of those services carry first-party OpenAPI 3.1 contracts. Beyond the library the university runs its own SAML 2.0 identity provider and eight entities in the Belgian Belnet R&E Federation, and hosts the student-built Hydra Resto API on a university domain. Everything else is somebody else''s: the library catalogue is now an Ex Libris Alma/Primo VE tenancy, and Dodona, which began at Ghent, has moved to its own domain and its own pricing. There is no DataCite membership. Ghent is a Crossref member in its own name.'
examples:
- key_count: 34
  name: Ghent Biblio Publication
  slug: ghent-biblio-publication
- key_count: 5
  name: Ghent Hydra Resto Menu Day
  slug: ghent-hydra-resto-menu-day
- key_count: 1
  name: Ghent Hydra Resto Meta
  slug: ghent-hydra-resto-meta
finops:
- name: Ghent Finops
  service_category: Education
  slug: ghent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ghent.png
json_schemas:
- name: Ghent Biblio Publication
  property_count: 69
  slug: ghent-biblio-publication
- name: Hydra Resto API payloads
  property_count: 0
  slug: ghent-hydra-resto
jsonld:
- class_count: 19
  name: Ghent Context
  property_count: 3
  slug: ghent-context
layout: provider
modified: '2026-09-01'
name: Ghent University
nav: Providers
network: true
overview: 'Ghent University publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Academic Bibliography API, Academic Bibliography OAI-PMH, Academic Bibliography SRU, and 4 more. Tagged areas include University, Higher Education, Education, Research, and Research Data.


  The Ghent University catalog on APIs.io includes 1 JSON-LD context.


  Ghent University''s developer surface includes documentation, API reference, GitHub presence, authentication, code examples, and 19 more developer resources.'
plans:
- name: Ghent Plans Pricing
  plan_count: 2
  slug: ghent-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Ghent Rate Limits
  slug: ghent-rate-limits
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 69.3
    catalog_earned_first_party: 0.0
    catalog_gap: 45.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 3.8
    contract_quality: 59.1
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 3.8
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 43.7
  provenance:
    conformance: first-party
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 60.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/screenshots/ghent-2026-06-20T181815.png
security:
- kind: authentication
  name: Ghent Authentication
  slug: ghent-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ghent Domain Security
  slug: ghent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ghent
tags:
- University
- Higher Education
- Education
- Research
- Research Data
- Library
- Open Data
- Identity Federation
- OAI-PMH
- Belgium
- Flanders
- Europe
website: https://www.ugent.be/en
---
