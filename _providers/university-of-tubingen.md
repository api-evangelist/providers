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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-05'
api_count: 8
apis:
- description: Keyless, read-only JSON REST API of FDAT, the university's institutional research data repository, operated by the Digital Humanities Center on the InvenioRDM platform and served from the university's
  name: FDAT Repository REST API
  slug: fdat-rest
- description: 'OAI-PMH 2.0 metadata harvesting provider for the FDAT research data repository. Verified live 2026-09-01 — verb=Identify returns 200 text/xml with repositoryName "FDAT Data Repository", baseURL https:'
  name: FDAT Repository OAI-PMH
  slug: fdat-oai
- description: OAI-PMH 2.0 provider for the University Library's institutional publication server (TOBIAS-lib), running DSpace on the library's own host publikationen.uni-tuebingen.de (ub01.uni-tuebingen.de, 134.2.5
  name: TOBIAS-lib / Publikationssystem UB Tübingen OAI-PMH
  slug: tobias-lib-oai
- description: 'Institution-operated Shibboleth SAML 2.0 identity provider, registered in DFN-AAI — the German national research and education identity federation — and published as machine-readable metadata through '
  name: University of Tübingen Shibboleth Identity Provider (DFN-AAI / eduGAIN)
  slug: identity-federation
- description: The university is a DataCite member and DOI registrant — a fact about the institution, recorded here as a membership rather than as a contract. The DataCite REST API is DataCite's and is never saved u
  name: DataCite membership and DOI registration (member AWZY)
  slug: datacite-membership
- description: The institution's entry in the Research Organization Registry, ROR ID https://ror.org/03a1kwz48. A registry membership, not a contract — the ROR API is ROR's. Verified 2026-09-01 via https://api.ror.o
  name: ROR registration (Research Organization Registry)
  slug: ror-registration
- description: Three national subject-information discovery services built and operated by Tübingen University Library on TueFind, the library's own VuFind derivative, whose source it develops in the open at https:/
  name: TueFind subject discovery services (ixTheo, RelBib, KrimDok)
  slug: tuefind-discovery
- description: 'The University Library''s main catalogue and discovery interface. Verified 2026-09-01: https://katalog.ub.uni-tuebingen.de/ redirects (301) to https://rds-tue.ibs-bw.de/opac/, a Tübingen-scoped instanc'
  name: UB Tübingen library catalogue (IBS|BW consortium tenant)
  slug: library-discovery
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://uni-tuebingen.de/en/
- group: docs
  title: ''
  type: APIReference
  url: https://fdat.uni-tuebingen.de/api/records
- group: docs
  title: ''
  type: Documentation
  url: https://dh-center.uni-tuebingen.de/fdat-policy/faq.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://uni-tuebingen.de/en/249679
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ub.uni-tuebingen.de/
- group: other
  title: ''
  type: IdentityFederation
  url: https://uni-tuebingen.de/en/einrichtungen/zentrum-fuer-datenverarbeitung/dienstleistungen/digitale-identitaet/single-sign-on/
- group: other
  title: ''
  type: ResearchComputing
  url: https://uni-tuebingen.de/en/einrichtungen/zentrum-fuer-datenverarbeitung/dienstleistungen/server/computing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ubtue
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/se-tuebingen
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubtue/tuefind
- group: operate
  title: ''
  type: Support
  url: https://uni-tuebingen.de/en/einrichtungen/zentrum-fuer-datenverarbeitung/dienstleistungen/a-z/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fdat.uni-tuebingen.de/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uni-tuebingen.de/en/data-privacy-statement
- group: company
  title: ''
  type: Blog
  url: https://uni-tuebingen.de/en/university/news-and-publications/press-releases/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/university-of-tuebingen
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-tubingen-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-tubingen-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-tubingen-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-tubingen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-tubingen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-tubingen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Tübingen (Eberhard Karls Universität Tübingen), founded in 1477, is one of Germany''s oldest public research universities and a member of the German Universities Excellence Initiative, with roughly 27,000 students in Baden-Württemberg. It runs no developer portal, publishes no OpenAPI and issues no API keys, and this profile does not pretend otherwise. What it does operate, on its own uni-tuebingen.de hosts, are four genuinely institution-run machine surfaces: the FDAT research data repository (InvenioRDM, Digital Humanities Center) exposing a keyless JSON REST API with IIIF manifests and DataCite DOIs; an OAI-PMH 2.0 provider on the same host; a second, much older OAI-PMH provider for the University Library''s TOBIAS-lib publication server (DSpace, records back to 1998, xMetaDissPlus); and a Shibboleth SAML 2.0 identity provider registered in DFN-AAI since 2009 and exported to eduGAIN, asserting REFEDS Research & Scholarship and SIRTFI/SIRTFI2. Its DataCite
  membership is verifiable — member AWZY "IKM Universität Tübingen", repository client AWZY.FEDNNV, DOI prefix 10.57754 — as is its ROR record 03a1kwz48. The University Library additionally builds and operates TueFind, its own VuFind derivative, in the open on GitHub, and runs three national subject discovery services on it (ixTheo, RelBib, KrimDok), currently behind a proof-of-work browser challenge. Campus management (alma), the VLE and the licensed library estate sit behind SSO and are not publicly documented APIs. No InvenioRDM, DSpace or VuFind product contract is saved under this institution — those belong to their upstream projects.'
finops:
- name: University Of Tubingen Finops
  service_category: Education
  slug: university-of-tubingen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-tubingen.png
jsonld:
- class_count: 20
  name: University Of Tubingen Context
  property_count: 11
  slug: university-of-tubingen-context
layout: provider
modified: '2026-09-01'
name: University of Tübingen
nav: Providers
network: true
overview: 'University of Tübingen publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Germany, and Research.


  The University of Tübingen catalog on APIs.io includes 1 JSON-LD context.


  University of Tübingen''s developer surface includes API reference, documentation, GitHub presence, support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: University Of Tubingen Plans Pricing
  plan_count: 2
  slug: university-of-tubingen-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: University Of Tubingen Rate Limits
  slug: university-of-tubingen-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 18.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 39.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-tubingen/refs/heads/main/screenshots/university-of-tubingen-2026-06-20T200240.png
security:
- kind: authentication
  name: University Of Tubingen Authentication
  slug: university-of-tubingen-authentication
  summary_line: none/saml2 · 2 schemes
- kind: domain-security
  name: University Of Tubingen Domain Security
  slug: university-of-tubingen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-tubingen
tags:
- Education
- Higher Education
- University
- Germany
- Research
- Research Data
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Library
- DataCite
website: https://uni-tuebingen.de/en/
---
