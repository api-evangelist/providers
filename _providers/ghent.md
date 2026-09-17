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
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-09-16'
api_count: 8
apis:
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
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Item API from Ghent University — 1 operation(s) for add item.
  name: Ghent University Add Item API
  slug: ghent-add-item-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Metadata Format API from Ghent University — 1 operation(s) for add metadata format.
  name: Ghent University Add Metadata Format API
  slug: ghent-add-metadata-format-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Organization API from Ghent University — 1 operation(s) for add organization.
  name: Ghent University Add Organization API
  slug: ghent-add-organization-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Person API from Ghent University — 1 operation(s) for add person.
  name: Ghent University Add Person API
  slug: ghent-add-person-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Project API from Ghent University — 1 operation(s) for add project.
  name: Ghent University Add Project API
  slug: ghent-add-project-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Record API from Ghent University — 1 operation(s) for add record.
  name: Ghent University Add Record API
  slug: ghent-add-record-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Add Set API from Ghent University — 1 operation(s) for add set.
  name: Ghent University Add Set API
  slug: ghent-add-set-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Delete Project API from Ghent University — 1 operation(s) for delete project.
  name: Ghent University Delete Project API
  slug: ghent-delete-project-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Delete Record API from Ghent University — 1 operation(s) for delete record.
  name: Ghent University Delete Record API
  slug: ghent-delete-record-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: Daily full-dataset dumps under ODbL.
  name: Ghent University Dumps API
  slug: ghent-dumps-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: Per-record and result-set exports in bibliographic formats.
  name: Ghent University Export API
  slug: ghent-export-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: RSS 1.0 feeds for any CQL search.
  name: Ghent University Feeds API
  slug: ghent-feeds-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Food API from Ghent University — 6 operation(s) for food.
  name: Ghent University Food API
  slug: ghent-food-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get Organization API from Ghent University — 1 operation(s) for get organization.
  name: Ghent University Get Organization API
  slug: ghent-get-organization-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get Organizations API from Ghent University — 1 operation(s) for get organizations.
  name: Ghent University Get Organizations API
  slug: ghent-get-organizations-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get Organizations By Id API from Ghent University — 1 operation(s) for get organizations by id.
  name: Ghent University Get Organizations By Id API
  slug: ghent-get-organizations-by-id-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get Organizations By Identifier API from Ghent University — 1 operation(s) for get organizations by identifier.
  name: Ghent University Get Organizations By Identifier API
  slug: ghent-get-organizations-by-identifier-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get People API from Ghent University — 1 operation(s) for get people.
  name: Ghent University Get People API
  slug: ghent-get-people-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get People By Id API from Ghent University — 1 operation(s) for get people by id.
  name: Ghent University Get People By Id API
  slug: ghent-get-people-by-id-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get People By Identifier API from Ghent University — 1 operation(s) for get people by identifier.
  name: Ghent University Get People By Identifier API
  slug: ghent-get-people-by-identifier-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get Person API from Ghent University — 1 operation(s) for get person.
  name: Ghent University Get Person API
  slug: ghent-get-person-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Get Project API from Ghent University — 1 operation(s) for get project.
  name: Ghent University Get Project API
  slug: ghent-get-project-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Locations API from Ghent University — 1 operation(s) for locations.
  name: Ghent University Locations API
  slug: ghent-locations-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Menu API from Ghent University — 2 operation(s) for menu.
  name: Ghent University Menu API
  slug: ghent-menu-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata harvesting.
  name: Ghent University OAI PMH API
  slug: ghent-oai-pmh-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: REST search over publications and datasets.
  name: Ghent University Search API
  slug: ghent-search-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Set Person Orcid API from Ghent University — 1 operation(s) for set person orcid.
  name: Ghent University Set Person Orcid API
  slug: ghent-set-person-orcid-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Set Person Role API from Ghent University — 1 operation(s) for set person role.
  name: Ghent University Set Person Role API
  slug: ghent-set-person-role-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Set Person Settings API from Ghent University — 1 operation(s) for set person settings.
  name: Ghent University Set Person Settings API
  slug: ghent-set-person-settings-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Set Person Token API from Ghent University — 1 operation(s) for set person token.
  name: Ghent University Set Person Token API
  slug: ghent-set-person-token-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: SRU 1.1 search/retrieve over CQL.
  name: Ghent University SRU API
  slug: ghent-sru-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Suggest Organizations API from Ghent University — 1 operation(s) for suggest organizations.
  name: Ghent University Suggest Organizations API
  slug: ghent-suggest-organizations-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Suggest People API from Ghent University — 1 operation(s) for suggest people.
  name: Ghent University Suggest People API
  slug: ghent-suggest-people-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: The Suggest Projects API from Ghent University — 1 operation(s) for suggest projects.
  name: Ghent University Suggest Projects API
  slug: ghent-suggest-projects-api
- baseURL: https://biblio.ugent.be
  baseurl_source: declared
  description: unAPI 1 alternate-format discovery.
  name: Ghent University Un API
  slug: ghent-unapi-api
artifact_total: 51
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
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/conformance/ghent-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ghent-education-standards-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/authentication/ghent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ghent-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/errors/ghent-errors.yml
  title: ''
  type: Errors
  url: errors/ghent-errors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/lifecycle/ghent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ghent-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/vocabulary/ghent-biblio-cql-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ghent-biblio-cql-vocabulary.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/examples/ghent-examples.yml
  title: ''
  type: Examples
  url: examples/ghent-examples.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/security/ghent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ghent-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/plans/ghent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ghent-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/rate-limits/ghent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ghent-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/finops/ghent-finops.yml
  title: ''
  type: FinOps
  url: finops/ghent-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/review.yml
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
overview: 'Ghent University publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Add Item API, Add Metadata Format API, Add Organization API, and 32 more. Tagged areas include University, Higher Education, Education, Research, and Research Data.


  The Ghent University catalog on APIs.io includes 1 JSON-LD context.


  Ghent University''s developer surface includes documentation, API reference, GitHub presence, authentication, code examples, and 19 more developer resources.'
plans:
- name: Ghent Plans Pricing
  plan_count: 2
  slug: ghent-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Ghent Rate Limits
  slug: ghent-rate-limits
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 50.0
    contract_governance: 3.8
    contract_quality: 61.9
    developer_ergonomics: 28.6
    discoverability: 59.3
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 42.6
  provenance:
    conformance: first-party
    contracts:
      callable: 28.6
      derived: 0
      marker_coverage: 0.0
      total: 35
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
