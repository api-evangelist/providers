---
access_model:
  confidence: high
  label: Free · No signup, anonymous read
  onboarding: open
  pricing: free
  public: true
  source:
  - authentication
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of The Witwatersrand Agentic Access
  operation_count: 9
  slug: university-of-the-witwatersrand-agentic-access
  summary_line: 9 operations
api_count: 2
apis:
- baseURL: https://wiredspace.wits.ac.za/server/api
  baseurl_source: declared
  description: HAL/JSON root document of the WIReDSpace DSpace 9.2 REST API, advertising 80 endpoint links including communities, collections, items, discovery, authn and identifiers. Operated by the University of t
  name: WIReDSpace DSpace REST Root API
  slug: university-of-the-witwatersrand-root-api
- baseURL: https://wiredspace.wits.ac.za/server/api
  baseurl_source: declared
  description: Top-level and sub-community containers in WIReDSpace, aligned to Wits faculties, schools and research groupings. Anonymous read, paginated HAL collections.
  name: WIReDSpace DSpace REST Communities API
  slug: university-of-the-witwatersrand-communities-api
- baseURL: https://wiredspace.wits.ac.za/server/api
  baseurl_source: declared
  description: 'Collections of items within WIReDSpace communities. Repaired on 2026-08-30: this contract had been welded to twenty-one Figshare /collections and /account/collections paths by a per-tag split across t'
  name: WIReDSpace DSpace REST Collections API
  slug: university-of-the-witwatersrand-collections-api
- baseURL: https://wiredspace.wits.ac.za/server/api
  baseurl_source: declared
  description: Individual repository records — theses, dissertations, research articles and reports — each with Dublin Core metadata, bitstreams and a Handle under the 10539 prefix.
  name: WIReDSpace DSpace REST Items API
  slug: university-of-the-witwatersrand-items-api
- baseURL: https://wiredspace.wits.ac.za/server/api
  baseurl_source: declared
  description: Browse indexes and the search/discovery endpoint over WIReDSpace holdings, plus an OpenSearch 1.1 description document at /server/opensearch/service.
  name: WIReDSpace DSpace REST Discovery API
  slug: university-of-the-witwatersrand-discovery-api
- baseURL: https://wiredspace.wits.ac.za/server/oai
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata harvesting endpoint for WIReDSpace. Single-endpoint, verb-driven, answering anonymously, advertising thirteen metadata prefixes (oai_dc, qdc, dim, mets, mods, ore, didl, rdf, marc
  name: WIReDSpace OAI-PMH Interface
  slug: university-of-the-witwatersrand-request-api
- description: The Wits research data repository. The hostname opendata.wits.ac.za is the university's and CNAMEs to proxy-eu-01.figshare.com; the DOIs are minted under the Wits DataCite prefix 10.71796 through Data
  name: Wits Open Data Vault (Figshare tenant)
  slug: university-of-the-witwatersrand-open-data-vault
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WIReDSpace DSpace REST Collections API
  slug: open-university-of-the-witwatersrand-collections-api
- collection_type: open
  name: WIReDSpace DSpace REST Communities API
  slug: open-university-of-the-witwatersrand-communities-api
- collection_type: open
  name: WIReDSpace DSpace REST Discovery API
  slug: open-university-of-the-witwatersrand-discovery-api
- collection_type: open
  name: WIReDSpace DSpace REST Items API
  slug: open-university-of-the-witwatersrand-items-api
- collection_type: open
  name: WIReDSpace OAI-PMH Interface Request API
  slug: open-university-of-the-witwatersrand-request-api
- collection_type: open
  name: WIReDSpace DSpace REST Root API
  slug: open-university-of-the-witwatersrand-root-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.wits.ac.za/
- group: company
  title: ''
  type: About
  url: https://www.wits.ac.za/about-wits/
- group: other
  title: ''
  type: ResearchRepository
  url: https://wiredspace.wits.ac.za/
- group: other
  title: ''
  type: OpenData
  url: https://opendata.wits.ac.za/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.wits.ac.za/safss/saml2/idp/metadata.php
- group: build
  title: ''
  type: Library
  url: https://www.wits.ac.za/library/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.wits.ac.za/course-finder/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.wits.ac.za/ai-policies/
- group: company
  title: ''
  type: Blog
  url: https://www.wits.ac.za/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wits.ac.za/site-assets/small-footer/terms-and-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wits.ac.za/popia/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WitsSoftDev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-the-witwatersrand/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-the-witwatersrand-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-the-witwatersrand-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-the-witwatersrand-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-the-witwatersrand-domain-security.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-the-witwatersrand-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-the-witwatersrand-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/university-of-the-witwatersrand-rules.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/university-of-the-witwatersrand-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-the-witwatersrand-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-the-witwatersrand-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-the-witwatersrand-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of the Witwatersrand (Wits) is a public research university in Johannesburg, South Africa (ROR 03rp50x72). Wits operates no central developer portal and no student, timetable or registrar API. What it does operate, on its own domain and its own infrastructure, is WIReDSpace — the institutional repository running DSpace 9.2 — which exposes a HAL/JSON REST API and a complete OAI-PMH 2.0 harvesting interface advertising thirteen metadata formats, both answering anonymous callers. It also runs its own SAML 2.0 identity provider, registered in SAFIRE (the South African Identity Federation) and published to eduGAIN, which serves signed metadata as application/samlmetadata+xml — a genuine machine-readable institutional surface that is almost never catalogued as one. Its research data repository, the Wits Open Data Vault at opendata.wits.ac.za, is a Figshare tenant: the hostname is the university''s and the 214 DOIs under the Wits DataCite prefix 10.71796 are the university''s,
  but the API contract underneath is Figshare''s and is catalogued against Figshare, not against Wits. Everything else in the estate — library discovery, LibGuides, the LMS, student self-service — is vendor software behind authentication. This profile was corrected on 2026-08-30: it previously credited Wits with the generic Figshare v2 API and nine of its tag splits, which were the vendor''s engineering, not the university''s.'
examples:
- key_count: 8
  name: University Of The Witwatersrand Getcommunity Example
  slug: university-of-the-witwatersrand-getCommunity-example
- key_count: 3
  name: University Of The Witwatersrand Oai Identify Example
  slug: university-of-the-witwatersrand-oai-identify-example
finops:
- name: University Of The Witwatersrand Finops
  service_category: Education
  slug: university-of-the-witwatersrand-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-the-witwatersrand.png
json_schemas:
- name: WIReDSpace Community
  property_count: 8
  slug: university-of-the-witwatersrand-community
json_structures:
- name: University Of The Witwatersrand Community Structure
  property_count: 6
  slug: university-of-the-witwatersrand-community-structure
jsonld:
- class_count: 15
  name: University Of The Witwatersrand Context
  property_count: 3
  slug: university-of-the-witwatersrand-context
layout: provider
modified: '2026-08-30'
name: University of the Witwatersrand
nav: Providers
network: true
overview: 'University of the Witwatersrand publishes 6 APIs on the [APIs.io](https://apis.io/) network, including WIReDSpace DSpace REST Root API, WIReDSpace DSpace REST Communities API, WIReDSpace DSpace REST Collections API, and 3 more. Tagged areas include University, Higher Education, Education, Research, and South Africa.


  The University of the Witwatersrand catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of the Witwatersrand''s developer surface includes engineering blog, authentication, and 23 more developer resources.'
plans:
- name: University Of The Witwatersrand Plans Pricing
  plan_count: 2
  slug: university-of-the-witwatersrand-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: University Of The Witwatersrand Rate Limits
  slug: university-of-the-witwatersrand-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of the Witwatersrand API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-the-witwatersrand-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of the Witwatersrand API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: university-of-the-witwatersrand-rules
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.5
    catalog_earned_first_party: 0.0
    catalog_gap: 40.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 61.8
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-the-witwatersrand/refs/heads/main/screenshots/university-of-the-witwatersrand-2026-08-17T082627.png
security:
- kind: authentication
  name: University Of The Witwatersrand Authentication
  slug: university-of-the-witwatersrand-authentication
  summary_line: none/session · 2 schemes
- kind: domain-security
  name: University Of The Witwatersrand Domain Security
  slug: university-of-the-witwatersrand-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-the-witwatersrand
tags:
- University
- Higher Education
- Education
- Research
- South Africa
- Africa
- Institutional Repository
- Research Data
- Open Access
- Identity Federation
- OAI-PMH
- DSpace
website: https://www.wits.ac.za/
---
