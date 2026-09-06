---
access_model:
  confidence: high
  label: Free and open — no registration, no key, no scopes
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting over Enlighten, the University of Glasgow's EPrints institutional repository of research outputs — journal articles, conference papers, books, book sections and theses.
  name: Enlighten Publications OAI-PMH
  slug: enlighten-oai
- description: OAI-PMH 2.0 metadata harvesting over Enlighten Research Data, the University of Glasgow's research data repository and registry. Records carry DataCite DOIs minted under the university's own prefix in
  name: Enlighten Research Data OAI-PMH
  slug: researchdata-oai
- description: OAI-PMH 2.0 metadata harvesting over Enlighten Theses, the University of Glasgow's electronic theses repository, with records back to 2012-12-10. Offers oai_dc, didl, mets, oai_bibl, rdf and uketd_dc,
  name: Enlighten Theses OAI-PMH
  slug: theses-oai
- baseURL: https://eprints.gla.ac.uk/rest
  baseurl_source: declared
  description: 'An anonymous read interface over the Enlighten repositories that the University of Glasgow does not document or advertise anywhere: a dataset index at /rest/, an object index per dataset, a full EPrin'
  name: Enlighten EPrints REST API
  slug: enlighten-rest
- description: The University of Glasgow's virtual learning environment, self-hosted on Moodle, exposes a live LTI 1.3 Advantage platform surface — a public JWKS at /mod/lti/certs.php carrying one RS256 signing key,
  name: Moodle VLE — LTI 1.3 Platform and Web Services
  slug: moodle-lti
- description: The library management system's Sierra REST API, live on the University of Glasgow Library's own catalogue host. /iii/sierra-api/v6/info/token returned 401 on 2026-08-30 — present and credentialed rat
  name: Library Sierra API (Innovative Interfaces)
  slug: sierra-library-api
- description: 'The University of Glasgow Library''s discovery layer, operated for the university by OCLC on a Glasgow-scoped WorldCat subdomain. Programmatic access exists but runs entirely on OCLC''s WorldCat Search '
  name: WorldCat Discovery (OCLC tenancy)
  slug: worldcat-discovery
- description: The library's research guides and databases A-Z, operated for the university by Springshare on a Glasgow-scoped LibGuides subdomain. Any machine access runs on Springshare's LibGuides API with site cr
  name: LibGuides (Springshare tenancy)
  slug: libguides
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.gla.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/University-of-Glasgow-Public
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UoGSoE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-glasgow/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.gla.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.gla.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchdata.gla.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://theses.gla.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://eleanor.lib.gla.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.gla.ac.uk/coursecatalogue/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.gla.ac.uk/research/arc/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.gla.ac.uk/myglasgow/leads/allstaff/generativeai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gla.ac.uk/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gla.ac.uk/legal/termsofuse/
- group: operate
  title: ''
  type: Support
  url: https://www.gla.ac.uk/myglasgow/it/
- group: design
  title: ''
  type: x-conformance
  url: conformance/university-of-glasgow-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-glasgow-authentication.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-glasgow-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/university-of-glasgow-lifecycle.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-glasgow-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-glasgow-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-glasgow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-glasgow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-glasgow-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-glasgow-context.jsonld
created: '2026-06-03'
description: 'The University of Glasgow is a public research university in Glasgow, Scotland, founded in 1451 and a member of the Russell Group. Its programmable footprint is entirely its own — no part of it was found to be a vendor''s contract running under the university''s name — but it is small, unadvertised and library-shaped rather than product-shaped. What the institution actually operates and runs itself, verified live on 2026-08-30, is the Enlighten repository estate on its own EPrints deployment: three OAI-PMH 2.0 endpoints (Publications, Research Data and Theses, the last of which was not previously catalogued) and an anonymous read REST interface over the same repositories that the university does not describe anywhere. Alongside them it operates a Shibboleth SAML 2.0 identity provider scoped gla.ac.uk and registered in the UK Access Management Federation, which by volume and maintenance is the institution''s largest machine-readable artifact and is a login federation rather
  than a data API. It mints its own DataCite DOIs under prefix 10.5525 and is Crossref member 21131. Two further surfaces are live on Glasgow hosts but run a third party''s contract — the self-hosted Moodle VLE''s LTI 1.3 platform endpoints and the library''s Innovative Interfaces Sierra API, both credentialed. Its discovery layer and its research guides are vendor tenancies on OCLC WorldCat and Springshare LibGuides, recorded here as tenant relationships and deliberately not credited to the university. There is no central developer portal, no API key issuance, no changelog, no status page and no developer support channel anywhere on gla.ac.uk.'
examples:
- key_count: 1
  name: University Of Glasgow Moodle Lti Jwks Example
  slug: university-of-glasgow-moodle-lti-jwks-example
finops:
- name: University Of Glasgow Finops
  service_category: Education
  slug: university-of-glasgow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-glasgow.png
jsonld:
- class_count: 18
  name: University Of Glasgow Context
  property_count: 6
  slug: university-of-glasgow-context
layout: provider
modified: '2026-08-30'
name: University of Glasgow
nav: Providers
network: true
overview: 'University of Glasgow publishes 1 API on the [APIs.io](https://apis.io/) network: Enlighten EPrints REST API. Tagged areas include University, Higher Education, Education, United Kingdom, and Scotland.


  The University of Glasgow catalog on APIs.io includes 1 JSON-LD context.


  University of Glasgow''s developer surface includes GitHub presence, support, authentication, and 23 more developer resources.'
plans:
- name: University Of Glasgow Plans Pricing
  plan_count: 2
  slug: university-of-glasgow-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Glasgow Rate Limits
  slug: university-of-glasgow-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 20.3
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 32.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-glasgow/refs/heads/main/screenshots/university-of-glasgow-2026-06-20T200152.png
security:
- kind: authentication
  name: University Of Glasgow Authentication
  slug: university-of-glasgow-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Glasgow Domain Security
  slug: university-of-glasgow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-glasgow
tags:
- University
- Higher Education
- Education
- United Kingdom
- Scotland
- Russell Group
- Research Data
- Repository
- OAI-PMH
- Open Access
- Identity Federation
- Digital Library
website: https://www.gla.ac.uk/
---
