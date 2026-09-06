---
access_model:
  confidence: high
  label: Free · no key, no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Michigan State University Agentic Access
  operation_count: 6
  slug: michigan-state-university-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://catalog.lib.msu.edu/api/v1
  baseurl_source: declared
  description: 'Record-retrieval half of the MSU Libraries VuFind 11.0.4 REST API, served from the university''s own host at catalog.lib.msu.edu/api/v1. Keyless and read-only: GET /record, /index2/record and /web/reco'
  name: MSU Libraries Catalog Record API
  slug: michigan-state-university-record-api
- baseURL: https://catalog.lib.msu.edu/api/v1
  baseurl_source: declared
  description: Search half of the same MSU Libraries VuFind 11.0.4 REST API on catalog.lib.msu.edu/api/v1 — GET /search, /index2/search and /web/search return result sets and facets over the library discovery index.
  name: MSU Libraries Catalog Search API
  slug: michigan-state-university-search-api
- description: 'OAI-PMH 2.0 metadata harvesting provider over the MSU Libraries catalog, on the university''s own host. Verified live on 2026-08-30: verb=Identify returns repositoryName "Michigan State University Libr'
  name: MSU Libraries Catalog OAI-PMH
  slug: catalog-oai
- description: 'OAI-PMH 2.0 provider over the MSU Libraries Digital Repository at d.lib.msu.edu. Verified live on 2026-08-30: verb=Identify returns repositoryName "MSU Libraries Digital Repository", repositoryIdentif'
  name: MSU Libraries Digital Repository OAI-PMH
  slug: dlib-oai
- description: MSU's federated single sign-on. The Shibboleth Identity Provider publishes SAML 2.0 metadata unauthenticated at idp.idm.msu.edu/idp/shibboleth — verified live on 2026-08-30, returning an md:EntityDesc
  name: MSU Identity Provider (Shibboleth / SAML 2.0)
  slug: idp
- description: MSU's learning management system is D2L Brightspace, running as an MSU-branded tenant at d2l.msu.edu, which CNAMEs to msu.brightspace.com — confirmed by DNS on 2026-08-30, with the login page titled "
  name: D2L Brightspace at MSU (tenant)
  slug: brightspace-lms
- description: MSU's public research-expertise portal at scholars.msu.edu. The host is MSU-branded, but the application is an Angular single-page client whose compiled bundle (main-VSM345O5.js, fetched 2026-08-30) c
  name: Scholars @ MSU (Academic Analytics tenant)
  slug: scholars-msu
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Library Catalog Record API
  slug: open-michigan-state-university-record-api
- collection_type: open
  name: Library Catalog Record Search API
  slug: open-michigan-state-university-search-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/MSU-Libraries/oai_repo/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.msu.edu
- group: docs
  title: ''
  type: APIReference
  url: https://catalog.lib.msu.edu/api/v1/?swagger
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.lib.msu.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://d.lib.msu.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.idm.msu.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://icer.msu.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.icer.msu.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.msu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MSU-Libraries
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Michigan-State-University
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/msu-icer
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.msu.edu/llms.txt
- group: other
  title: ''
  type: Sitemap
  url: https://msu.edu/sitemap.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://msu.edu/privacy
- group: operate
  title: ''
  type: Support
  url: https://msu.edu/contact
- group: company
  title: ''
  type: Blog
  url: https://msutoday.msu.edu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/michigan-state-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/michigan-state-university-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/michigan-state-university-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/michigan-state-university-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/michigan-state-university-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/michigan-state-university-lifecycle.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/michigan-state-university-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/michigan-state-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/michigan-state-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/michigan-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/michigan-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/michigan-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Michigan State University is a public land-grant research university in East Lansing, Michigan, and a founding member of the Big Ten and the AAU. It runs no central developer portal, issues no API keys, and operates no self-service onboarding of any kind, and this profile does not pretend otherwise. What it genuinely operates, on its own msu.edu hosts, is a small set of real machine surfaces run by MSU Libraries and MSU IT: a keyless VuFind 11.0.4 REST API for the library discovery index at catalog.lib.msu.edu/api/v1, whose OpenAPI 3.0.3 the university itself publishes live at /api/v1/?swagger; two OAI-PMH 2.0 providers, one over the catalog and one over the digital repository at d.lib.msu.edu, the latter running oai_repo — an OAI-PMH server library MSU Libraries wrote themselves and release Apache-2.0 on GitHub, which is real institutional engineering rather than a vendor deployment; and a Shibboleth SAML 2.0 identity provider registered in InCommon as urn:mace:incommon:msu.edu.
  MSU also publishes an llms.txt and a /.well-known/ai.txt naming three AI content endpoints, though the Imperva edge in front of msu.edu answers every non-browser client with a JavaScript challenge, so those declared endpoints are not actually reachable by the agents they are addressed to. Two vendor platforms are recorded as tenant relationships rather than as MSU contracts: D2L Brightspace (d2l.msu.edu, CNAME msu.brightspace.com) and Academic Analytics (Scholars @ MSU at scholars.msu.edu). Student records, registration, HR and finance are behind institutional SSO and are not public APIs.'
examples:
- key_count: 3
  name: Michigan State University Record Example
  slug: michigan-state-university-record-example
- key_count: 3
  name: Michigan State University Search Example
  slug: michigan-state-university-search-example
finops:
- name: Michigan State University Finops
  service_category: Education
  slug: michigan-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/michigan-state-university.png
json_schemas:
- name: MSU Libraries Catalog Record
  property_count: 35
  slug: michigan-state-university-record
- name: MSU Libraries Catalog Search Response
  property_count: 5
  slug: michigan-state-university-searchresponse
json_structures:
- name: Michigan State University Record Structure
  property_count: 31
  slug: michigan-state-university-record-structure
- name: Michigan State University Searchresponse Structure
  property_count: 5
  slug: michigan-state-university-searchresponse-structure
jsonld:
- class_count: 38
  name: Michigan State University Context
  property_count: 5
  slug: michigan-state-university-context
layout: provider
modified: '2026-08-30'
name: Michigan State University
nav: Providers
network: true
overview: 'Michigan State University publishes 2 APIs on the [APIs.io](https://apis.io/) network: MSU Libraries Catalog Record API and MSU Libraries Catalog Search API. Tagged areas include Education, Higher Education, University, Public Research University, and Land-Grant University.


  The Michigan State University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Michigan State University''s developer surface includes API reference, documentation, GitHub presence, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Michigan State University Plans Pricing
  plan_count: 2
  slug: michigan-state-university-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Michigan State University Rate Limits
  slug: michigan-state-university-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Michigan State University API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: michigan-state-university-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Michigan State University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: michigan-state-university-rules
scopes:
- name: Michigan State University Scopes
  scope_count: 0
  slug: michigan-state-university-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.3
    catalog_earned_first_party: 0.0
    catalog_gap: 47.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 50.7
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/michigan-state-university/refs/heads/main/screenshots/michigan-state-university-2026-06-20T185328.png
security:
- kind: authentication
  name: Michigan State University Authentication
  slug: michigan-state-university-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Michigan State University Domain Security
  slug: michigan-state-university-domain-security
  summary_line: TLSv1.3 · DMARC
slug: michigan-state-university
tags:
- Education
- Higher Education
- University
- Public Research University
- Land-Grant University
- Big Ten
- United States
- Michigan
- Library
- Library Catalog
- Digital Repository
- Metadata
- OAI-PMH
- Identity Federation
- Shibboleth
- Research Computing
website: https://www.msu.edu
---
