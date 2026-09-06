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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://freidok.uni-freiburg.de/jsonApi/v1/
  baseurl_source: declared
  description: Read-only JSON API for FreiDok plus, the institutional repository and university bibliography built and operated by the Universitätsbibliothek Freiburg on the university's own host. Four anonymous col
  name: FreiDok plus JSON API
  slug: freidok-json
- description: OAI-PMH 2.0 metadata-harvesting endpoint for FreiDok plus, on the university's own host. Identify (probed 2026-09-01) reports repositoryName "FreiDok plus", repositoryIdentifier freidok.uni-freiburg.d
  name: FreiDok plus OAI-PMH
  slug: freidok-oai
- description: REST API of FreiData, the university's research-data repository, deployed and operated on its own host at freidata.uni-freiburg.de. Anonymous read of records, files and IIIF manifests; records mint Da
  name: FreiData research-data repository REST API
  slug: freidata-rest
- description: Second OAI-PMH 2.0 endpoint, on the FreiData research-data host, serving marcxml, oai_dc, dcat, marc21, datacite, oai_datacite, datacite4 and oai_datacite4. Identify returns the InvenioRDM product def
  name: FreiData OAI-PMH
  slug: freidata-oai
- description: 'Self-hosted GitLab operated by the university''s computing centre. The v4 REST API answers anonymous requests for public resources — probed 2026-09-01, GET /api/v4/projects returned 56 public projects '
  name: University of Freiburg GitLab REST API
  slug: gitlab
- description: Public status page for central university services, with a JSON API — /api/status-page/ufr-services returns the monitor configuration and /api/status-page/heartbeat/ufr-services returns per-monitor he
  name: Uni-Freiburg Services status API
  slug: status-api
- description: The university's own Shibboleth Identity Provider, myLogin, operated by the Universitätsrechenzentrum. Its SAML 2.0 metadata is published on the university's host (entityID https://mylogin.uni-freibur
  name: myLogin Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: The University of Freiburg is a DataCite member (symbol QVVC, country DE, consortium organization under the TIB consortium, rorId https://ror.org/0245cg223) and operates the registered repository clie
  name: DataCite membership and repository registration
  slug: datacite-membership
- description: The institution's Research Organization Registry identifier, https://ror.org/0245cg223, carrying its names in German and English and its website. Recorded as a registry membership; the ROR API is ROR'
  name: ROR organization identifier
  slug: ror-record
artifact_total: 21
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-freiburg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-freiburg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uni-freiburg.de/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/albert-ludwigs-universitaet-freiburg/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-freiburg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-freiburg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-freiburg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://freidok.uni-freiburg.de/
- group: other
  title: ''
  type: OpenData
  url: https://freidata.uni-freiburg.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.ub.uni-freiburg.de/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://campus.uni-freiburg.de/qisserver/pages/cs/sys/portal/subMenu.faces?navigationPosition=studiesOffered
- group: other
  title: ''
  type: IdentityFederation
  url: https://mylogin.uni-freiburg.de/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.nemo.uni-freiburg.de/
- group: other
  title: ''
  type: AIPolicy
  url: https://uni-freiburg.de/forschung/qualitaetssicherung/gute-wissenschaftliche-praxis/policy-zum-umgang-mit-generativer-ki-in-der-forschung/
- group: operate
  title: ''
  type: Status
  url: https://status.uni-freiburg.de/status/ufr-services
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.uni-freiburg.de/explore/projects
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uni-freiburg.de/datenschutzerklaerung/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://uni-freiburg.de/.well-known/security.txt
created: '2026-06-03'
description: 'The University of Freiburg (Albert-Ludwigs-Universität Freiburg) is a public research university in Baden-Württemberg, Germany, founded in 1457, a member of the German U15 and ranked #212 in the QS World University Rankings 2025. Like most universities it operates no central developer portal, publishes no OpenAPI description of anything, and offers no API program, keys, plans or support channel for developers — but unlike most of the cohort a meaningful part of what it does run is genuinely its own rather than a vendor contract wearing its name. Its library (Universitätsbibliothek Freiburg) operates FreiDok plus, an institutional repository and university bibliography whose read-only JSON API and OAI-PMH 2.0 endpoint are open, anonymous and live (267,771 publications, 238,730 persons, 1,277 institutions and 10,612 projects as probed on 2026-09-01). The university also runs a FreiData research-data repository (an InvenioRDM deployment minting DataCite DOIs under its own prefix
  10.60493), a self-hosted GitLab whose REST API answers anonymously for 56 public projects, a public status page with a JSON monitor feed, and its own Shibboleth/SAML Identity Provider published into the DFN-AAI national federation. Its library discovery catalog is live but IP-blocked to automated clients, and its campus-management and LMS systems (HISinOne, ILIAS) are human-facing only. Everything programmable here is read-only metadata infrastructure built for harvesting, not a product; there is nothing to sign up for and nothing to buy.'
examples:
- key_count: 7
  name: University Of Freiburg Freidok Plus Institutions Example
  slug: university-of-freiburg-freidok-plus-institutions-example
- key_count: 7
  name: University Of Freiburg Freidok Plus Persons Example
  slug: university-of-freiburg-freidok-plus-persons-example
- key_count: 7
  name: University Of Freiburg Freidok Plus Projects Example
  slug: university-of-freiburg-freidok-plus-projects-example
- key_count: 7
  name: University Of Freiburg Freidok Plus Publications Example
  slug: university-of-freiburg-freidok-plus-publications-example
finops:
- name: University Of Freiburg Finops
  service_category: Education
  slug: university-of-freiburg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-freiburg.png
json_schemas:
- name: FreiDok plus JSON API response envelope
  property_count: 6
  slug: university-of-freiburg-freidok-plus-response
jsonld:
- class_count: 20
  name: University Of Freiburg Context
  property_count: 3
  slug: university-of-freiburg-context
layout: provider
modified: '2026-09-01'
name: University of Freiburg
nav: Providers
network: true
overview: 'University of Freiburg publishes 1 API on the [APIs.io](https://apis.io/) network: FreiDok plus JSON API. Tagged areas include Education, Higher Education, University, Research, and Research Data.


  The University of Freiburg catalog on APIs.io includes 1 JSON-LD context.


  University of Freiburg''s developer surface includes status page and 18 more developer resources.'
plans:
- name: University Of Freiburg Plans Pricing
  plan_count: 2
  slug: university-of-freiburg-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: University Of Freiburg Rate Limits
  slug: university-of-freiburg-rate-limits
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 74.0
    catalog_earned_first_party: 0.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 62.7
    developer_ergonomics: 21.4
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 44.0
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
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-freiburg/refs/heads/main/screenshots/university-of-freiburg-2026-06-20T200150.png
security:
- kind: authentication
  name: University Of Freiburg Authentication
  slug: university-of-freiburg-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Freiburg Domain Security
  slug: university-of-freiburg-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: University Of Freiburg Vulnerability Disclosure
  slug: university-of-freiburg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-freiburg
tags:
- Education
- Higher Education
- University
- Research
- Research Data
- Open Data
- Library
- Repository
- OAI-PMH
- Identity Federation
- Germany
website: https://www.uni-freiburg.de/
---
