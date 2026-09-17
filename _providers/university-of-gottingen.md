---
access_model:
  confidence: high
  label: Free and anonymous — no registration, no key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probes
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-09-16'
api_count: 6
apis:
- description: The university's own SAML 2.0 identity provider, entityID https://shibboleth-idp.uni-goettingen.de/uni/shibboleth, registered by DFN-AAI, exported to eduGAIN as entity 696098 since 2017-04-13, scope u
  name: Georg-August-Universität Göttingen SAML Identity Provider
  slug: identity-provider
- description: 'GRO.data is the Göttingen Campus research-data repository, operated by the Göttingen eResearch Alliance and hosted at GWDG on data.goettingen-research-online.de. The deployment, the data and the DOIs '
  name: GRO.data (Göttingen Research Online) Research Data Repository
  slug: grodata
- description: The university self-hosts Stud.IP, the open-source German learning management system, at studip.uni-goettingen.de and exposes its REST and JSON:API surfaces there. Anonymous callers receive "401 Unaut
  name: Stud.IP Learning Management REST and JSON:API
  slug: studip
- description: The Göttingen university catalogue is served from opac.sub.uni-goettingen.de, which is a DNS CNAME to lbsgoe.gbv.de — the library system platform of the Verbundzentrale des GBV. The subdomain is Götti
  name: SUB Göttingen Library Catalogue (GUK)
  slug: opac
- baseURL: https://gdz.sub.uni-goettingen.de/oai2/
  baseurl_source: declared
  description: IIIF Image API 2.0, level 2 compliance as advertised by the live info.json profile.
  name: University of Göttingen IIIF Image API
  slug: university-of-gottingen-iiif-image-api
- baseURL: https://gdz.sub.uni-goettingen.de/oai2/
  baseurl_source: declared
  description: IIIF Presentation API manifests for digitised GDZ objects.
  name: University of Göttingen IIIF Presentation API
  slug: university-of-gottingen-iiif-presentation-api
- baseURL: https://gdz.sub.uni-goettingen.de/oai2/
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting, version 2.0.
  name: University of Göttingen OAI PMH API
  slug: university-of-gottingen-oai-pmh-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://www.uni-goettingen.de/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uni-goettingen
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/subugoe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-gottingen/
- group: company
  title: ''
  type: Blog
  url: https://news.uni-goettingen.de/feed/
- group: other
  title: ''
  type: IdentityFederation
  url: https://technical.edugain.org/entities?e_name=Georg-August
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.eresearch.uni-goettingen.de/services-and-software/gro-data/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.sub.uni-goettingen.de/DB=1/LNG=DU/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://ecampus.uni-goettingen.de/h1/pages/cs/sys/portal/subMenu.faces?navigationPosition=studiesOffered
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.hpc.gwdg.de/
- group: other
  title: ''
  type: AIPolicy
  url: https://uni-goettingen.de/de/umgang+mit+ki-modellen+in+studium+und+lehre/674738.html
- group: build
  title: ''
  type: AITooling
  url: https://academiccloud.de/services/chatai/
- group: docs
  title: ''
  type: Documentation
  url: https://gdz.sub.uni-goettingen.de/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uni-goettingen.de/en/439238.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uni-goettingen.de/en/439479.html
- group: operate
  title: ''
  type: Support
  url: https://uni-goettingen.de/en/545353.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/conformance/university-of-gottingen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-gottingen-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/authentication/university-of-gottingen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-gottingen-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/errors/university-of-gottingen-errors.yml
  title: ''
  type: Errors
  url: errors/university-of-gottingen-errors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/lifecycle/university-of-gottingen-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-gottingen-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/scopes/university-of-gottingen-scopes.yml
  title: ''
  type: Scopes
  url: scopes/university-of-gottingen-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/vocabulary/university-of-gottingen-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-gottingen-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/security/university-of-gottingen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-gottingen-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/plans/university-of-gottingen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-gottingen-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/rate-limits/university-of-gottingen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-gottingen-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/finops/university-of-gottingen-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-gottingen-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Göttingen (Georg-August-Universität Göttingen) is a public research university in Lower Saxony, Germany, founded 1737, a German U15 member and QS-ranked in the mid-200s. Its programmable footprint is real but small, and it belongs almost entirely to the Göttingen State and University Library (SUB Göttingen) rather than to the university''s central IT: two live OAI-PMH 2.0 harvesting endpoints on the university''s own domains — the Göttinger Digitalisierungszentrum, harvesting back to 1998, and the eDiss dissertation server, which disseminates the German national xMetaDissPlus, epicur and picaxml profiles — plus a IIIF Image API 2.0 level-2 image service and IIIF Presentation manifests for the digitised collections. The university also operates its own SAML 2.0 identity provider, registered in DFN-AAI, exported to eduGAIN and Sirtfi-compliant, and holds the DataCite prefix 10.25625 as repository client SUBGOE.GRO. There is no central developer portal, no self-service
  API key, no published rate limits and no OpenAPI authored by the institution; every specification in this repository was written by API Evangelist from live probes and is marked as such. The GRO.data research-data repository and the SUB library catalogue are recorded here as relationships rather than as Göttingen contracts — GRO.data runs Dataverse and the catalogue resolves onto the GBV/VZG library platform.'
examples:
- key_count: 9
  name: University Of Gottingen Ediss Oai Identify Example
  slug: university-of-gottingen-ediss-oai-identify-example
- key_count: 9
  name: University Of Gottingen Gdz Oai Identify Example
  slug: university-of-gottingen-gdz-oai-identify-example
- key_count: 9
  name: University Of Gottingen Sub Iiif Image Info Example
  slug: university-of-gottingen-sub-iiif-image-info-example
finops:
- name: University Of Gottingen Finops
  service_category: Education
  slug: university-of-gottingen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-gottingen.png
layout: provider
modified: '2026-08-30'
name: University of Göttingen
nav: Providers
network: true
overview: 'University of Göttingen publishes 3 APIs on the [APIs.io](https://apis.io/) network: IIIF Image API, IIIF Presentation API, and OAI PMH API. Tagged areas include University, Higher Education, Education, Germany, and German U15.


  University of Göttingen''s developer surface includes engineering blog, documentation, support, authentication, and 23 more developer resources.'
plans:
- name: University Of Gottingen Plans Pricing
  plan_count: 2
  slug: university-of-gottingen-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: University Of Gottingen Rate Limits
  slug: university-of-gottingen-rate-limits
scopes:
- name: University Of Gottingen Scopes
  scope_count: 0
  slug: university-of-gottingen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 34.2
    contract_governance: 15.2
    contract_quality: 40.6
    developer_ergonomics: 28.6
    discoverability: 64.8
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-gottingen/refs/heads/main/screenshots/university-of-gottingen-2026-06-20T200154.png
security:
- kind: authentication
  name: University Of Gottingen Authentication
  slug: university-of-gottingen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Gottingen Domain Security
  slug: university-of-gottingen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-gottingen
tags:
- University
- Higher Education
- Education
- Germany
- German U15
- Public Research University
- Research Data
- Digital Library
- IIIF
- OAI-PMH
- Identity Federation
- Research Repository
website: https://www.uni-goettingen.de/en/
---
