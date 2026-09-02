---
access_model:
  confidence: high
  label: Free · course data open, SSO keys issued by email on request
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - documentation
  - authentication
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'The university''s own single sign-on service, in production at account.it.chula.ac.th since January 2017 and originally built as part of the 2015 CU DataGateway project. The protocol is a modified CAS '
  name: Chula SSO Authentication API
  slug: sso
- description: The read-only JSON backend behind CU-REG Course Schedule, the Office of the Registrar's public course, curriculum and timetable browser. Two endpoints answer HTTP 200 to an unauthenticated request fro
  name: CU-REG Course Schedule API
  slug: course-schedule
- description: The university's digital preservation platform for theses, dissertations, rare books, multimedia and digitised manuscripts, operated by the Office of Academic Resources. cuir.car.chula.ac.th, the lega
  name: Chula DigiVerse — Institutional Digital Repository
  slug: digiverse
- description: The university's open-access journals, theses and ETD platform, and the only working OAI-PMH endpoint in the estate. The Identify response names "Chula Digital Collections", ListSets returns 30 sets i
  name: Chula Digital Collections (bepress Digital Commons tenant)
  slug: digital-collections
- description: The university's cloud identity, and the most complete machine-readable contract anywhere in this profile. Entra tenant 271d5e7b-1350-4b96-ab84-52dbda4cf40c carries the federation brand name "Chulalon
  name: Chulalongkorn University Identity Federation (Microsoft Entra ID tenant)
  slug: entra-federation
- description: Chulalongkorn University is a DataCite consortium organization, provider id lygd, country TH, with one registered repository — lygd.aguxul, "Chula Digiverse", pointing at digiverse.chula.ac.th. This i
  name: DataCite Membership (consortium organization lygd)
  slug: datacite
- description: Chulalongkorn registers Crossref DOIs through eleven separate member records, one per faculty, institute or office, each with its own prefix — Engineering 10.4186, Medicine 10.5372, Architecture 10.54
  name: Crossref Membership (eleven faculty and institute member records)
  slug: crossref
- description: 'Chulalongkorn University''s Research Organization Registry record, carrying the Thai and English names, the acronym CU, ten Crossref Funder IDs, GRID grid.7922.e, ISNI 0000 0001 0244 7875 and Wikidata '
  name: ROR Registration (https://ror.org/028wp3y58)
  slug: ror
- description: The Office of Academic Resources fronts its licensed-content discovery through EBSCO, under the named customer account chulalun. The links published on car.chula.ac.th carry that account explicitly (p
  name: Chula Library Discovery (EBSCO tenant)
  slug: library-discovery
- description: The university's central data exchange, consolidating and sharing data across departments in two connection modes — batch over SFTP and online over an API. Access is limited to officially assigned uni
  name: CU Data Gateway
  slug: data-gateway
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.chula.ac.th/en/
- group: docs
  title: ''
  type: APIReference
  url: https://account.it.chula.ac.th/wiki/doku.php?id=how_does_it_work
- group: docs
  title: ''
  type: Documentation
  url: https://account.it.chula.ac.th/wiki/doku.php
- group: learn
  title: ''
  type: CourseCatalog
  url: https://cas.reg.chula.ac.th/class/course-schedule
- group: other
  title: ''
  type: ResearchRepository
  url: https://digiverse.chula.ac.th/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.car.chula.ac.th/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/chulalongkorn-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chulalongkorn-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chulalongkorn-authentication.yml
- group: other
  title: ''
  type: AIPolicy
  url: https://www.chula.ac.th/en/news/125190/
- group: build
  title: ''
  type: AITooling
  url: https://genie.chula.ac.th/
- group: operate
  title: ''
  type: Support
  url: https://portal.it.chula.ac.th/home
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ChulalongkornUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/chulalongkorn-university/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chulalongkorn-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/chulalongkorn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chulalongkorn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chulalongkorn-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Chulalongkorn University is Thailand''s oldest public research university, founded in 1917 in Bangkok. Its programmable footprint is small, real, and almost entirely undeclared: there is no developer portal, no open data portal, no published specification of any kind, and no self-service registration anywhere in the estate. What it does operate are two genuine institution-run surfaces. Chula SSO at account.it.chula.ac.th has been in production since January 2017 and is documented endpoint-by-endpoint on a public wiki — a modified CAS 1.0 protocol with an added application-authentication step, backed by the university LDAP directory, with keys issued by email rather than by a console. The Office of the Registrar''s CU-REG Course Schedule application answers unauthenticated JSON at cas.reg.chula.ac.th/class/api for its curriculum register and build version, though the thirteen further endpoints its own client declares return 404 from outside the campus network. Everything else
  that looks like a Chulalongkorn API belongs to somebody else: Chula Digital Collections, which serves the university''s only working OAI-PMH endpoint, is a bepress Digital Commons tenancy (digital.car.chula.ac.th is a CNAME to dcchula.bepress.com, adminEmail dc-support@elsevier.com); federated login is a Microsoft Entra ID tenant; DOIs are registered through DataCite and, faculty by faculty, through eleven separate Crossref member records. The institution''s own DigiVerse repository publishes no machine-readable interface at all, and the previously recorded claim that it is a DSpace deployment exposing DSpace REST and OAI-PMH does not survive probing. The central data exchange, CU Data Gateway, is restricted to assigned university personnel and unreachable from outside the campus network.'
examples:
- key_count: 2
  name: Chulalongkorn Course Studies Example
  slug: chulalongkorn-course-studies-example
- key_count: 3
  name: Chulalongkorn Sso Servicevalidation Example
  slug: chulalongkorn-sso-servicevalidation-example
finops:
- name: Chulalongkorn Finops
  service_category: Education
  slug: chulalongkorn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chulalongkorn.png
json_schemas:
- name: CU-REG Course Study (Degree Program)
  property_count: 34
  slug: chulalongkorn-course-study
- name: Chula SSO Authenticated User
  property_count: 6
  slug: chulalongkorn-sso-user
jsonld:
- class_count: 12
  name: Chulalongkorn Context
  property_count: 6
  slug: chulalongkorn-context
layout: provider
modified: '2026-09-01'
name: Chulalongkorn University
nav: Providers
network: true
overview: 'Chulalongkorn University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chula SSO Authentication API and CU-REG Course Schedule API. Tagged areas include Education, Higher Education, University, Research, and Thailand.


  The Chulalongkorn University catalog on APIs.io includes 1 JSON-LD context.


  Chulalongkorn University''s developer surface includes API reference, documentation, authentication, support, GitHub presence, and 14 more developer resources.'
plans:
- name: Chulalongkorn Plans Pricing
  plan_count: 2
  slug: chulalongkorn-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Chulalongkorn Rate Limits
  slug: chulalongkorn-rate-limits
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 13.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 41.9
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/chulalongkorn/refs/heads/main/screenshots/chulalongkorn-2026-06-20T174339.png
security:
- kind: authentication
  name: Chulalongkorn Authentication
  slug: chulalongkorn-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Chulalongkorn Domain Security
  slug: chulalongkorn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chulalongkorn
tags:
- Education
- Higher Education
- University
- Research
- Thailand
- Bangkok
- Identity Federation
- Single Sign-On
- Course Catalog
- Research Repository
- Library
- Open Access
- OAI-PMH
website: https://www.chula.ac.th/en/
---
