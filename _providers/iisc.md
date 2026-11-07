---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Iisc Agentic Access
  operation_count: 8
  slug: iisc-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Institution-operated Shibboleth SAML 2.0 identity provider, self-published as machine-readable metadata on IISc's own host and registered in the INFLIBNET Access Management Federation (INFED), which c
  name: IISc Shibboleth Identity Provider (INFED / eduGAIN)
  slug: identity-federation
- description: Live OAI-PMH 2.0 metadata-harvesting provider for the Journal of the Indian Institute of Science, served from IISc's own journal.iisc.ac.in host on an Open Journal Systems 3.3.0.22 (Public Knowledge P
  name: Journal of the Indian Institute of Science OAI-PMH
  slug: jiisc-oai
- description: IISc's own learning management system, a self-hosted Moodle branded "IKEN" at courses.iisc.ac.in, exposing two machine surfaces verified live 2026-09-01. The LTI 1.3 Advantage platform endpoints are p
  name: IKEN Moodle LMS — web services and LTI 1.3 platform
  slug: courses-moodle
- baseURL: https://etd.iisc.ac.in/rest
  baseurl_source: declared
  description: Read-only REST API of ETD@IISc, the Electronic Theses and Dissertations repository IISc runs on DSpace 6 at its own etd.iisc.ac.in host, serving the Community / Collection / Item / Bitstream hierarchy
  name: ETD@IISc DSpace 6 REST API
  slug: etd-dspace-rest
- description: 'ePrints@IISc is the open-access institutional repository of IISc research publications, established in 2002 on EPrints software and self-hosted on the institute''s own eprints.iisc.ac.in domain. It is '
  name: ePrints@IISc OAI-PMH
  slug: eprints-oai
- description: IISc is registered in the Research Organization Registry as https://ror.org/04dese585. Verified 2026-09-01 — https://api.ror.org/organizations/04dese585 returns 200 with names "Indian Institute of Sci
  name: ROR registration — Indian Institute of Science
  slug: ror-registration
- description: IISc holds Crossref Open Funder Registry id 100007780. Verified 2026-09-01 — https://api.crossref.org/funders/100007780 returns 200 naming "Indian Institute of Science" with a hierarchy of its own cen
  name: Crossref Open Funder Registry entry — Indian Institute of Science
  slug: crossref-funder-registry
artifact_total: 28
collections:
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams API
  slug: open-iisc-bitstreams-api
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams Collections API
  slug: open-iisc-collections-api
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams Communities API
  slug: open-iisc-communities-api
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams Items API
  slug: open-iisc-items-api
common:
- group: company
  title: ''
  type: Website
  url: https://iisc.ac.in/
- group: build
  title: ''
  type: Library
  url: https://library.iisc.ac.in/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://libraryopac.iisc.ac.in/
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.iisc.ac.in/
- group: other
  title: ''
  type: IdentityFederation
  url: https://libraryidp.iisc.ac.in/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.iisc.ac.in/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.serc.iisc.ac.in/
- group: docs
  title: ''
  type: APIReference
  url: https://journal.iisc.ac.in/index.php/iisc/oai?verb=Identify
- group: docs
  title: ''
  type: Documentation
  url: https://iisc.ac.in/academics/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/val-iisc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/csl-iisc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cni-iisc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/indian-institute-of-science/
- group: design
  href: https://artifacts.apis.io/iisc/conformance/iisc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iisc-conformance.yml
- group: other
  href: https://artifacts.apis.io/iisc/capabilities/iisc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/iisc-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/iisc/agentic-access/iisc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iisc-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/iisc/security/iisc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iisc-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/iisc/plans/iisc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iisc-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/iisc/rate-limits/iisc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iisc-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/iisc/finops/iisc-finops.yml
  title: ''
  type: FinOps
  url: finops/iisc-finops.yml
- group: other
  href: https://artifacts.apis.io/iisc/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Indian Institute of Science (IISc) Bangalore, founded 1909, is India''s premier research-intensive institution — a deemed university, an Institute of Eminence, and ranked #211 in the QS World University Rankings 2025. It operates no developer portal, publishes no OpenAPI of its own, and this profile does not pretend otherwise. What it does run, on hosts under its own iisc.ac.in domain, are three verified institution-operated machine surfaces: a Shibboleth SAML 2.0 identity provider at libraryidp.iisc.ac.in registered in the INFLIBNET Access Management Federation (INFED) and carried into eduGAIN; an OAI-PMH 2.0 provider on the Open Journal Systems instance behind the Journal of the Indian Institute of Science at journal.iisc.ac.in; and a self-hosted Moodle LMS at courses.iisc.ac.in whose LTI 1.3 JWKS and token-gated web-services REST endpoint are both live. Two older repository surfaces are currently unreadable rather than absent — ETD@IISc (DSpace 6) has returned 502 on
  every path since roughly May 2026, and ePrints@IISc sits behind an Azure WAF that 403s every automated client including the Internet Archive. IISc is registered in ROR (04dese585) and the Crossref Open Funder Registry (100007780) but is not a DataCite or Crossref member. Its public code lives in departmental GitHub organisations (val-iisc, csl-iisc, cni-iisc), not in a central institutional org — github.com/IISc exists but holds zero public repositories.'
examples:
- key_count: 5
  name: Iisc Listcollections Example
  slug: iisc-listCollections-example
- key_count: 5
  name: Iisc Listcommunities Example
  slug: iisc-listCommunities-example
- key_count: 5
  name: Iisc Listitems Example
  slug: iisc-listItems-example
finops:
- has_sources: true
  method: generated
  name: Iisc Finops
  primary_unit: ''
  service_category: Education
  slug: iisc-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iisc.png
json_schemas:
- name: ETD@IISc Bitstream
  property_count: 14
  slug: iisc-bitstream
- name: ETD@IISc Collection
  property_count: 16
  slug: iisc-collection
- name: ETD@IISc Community
  property_count: 15
  slug: iisc-community
- name: ETD@IISc Item
  property_count: 11
  slug: iisc-item
json_structures:
- name: Iisc Community Structure
  property_count: 10
  slug: iisc-community-structure
- name: Iisc Item Structure
  property_count: 10
  slug: iisc-item-structure
jsonld:
- class_count: 25
  name: Iisc Context
  property_count: 1
  slug: iisc-context
layout: provider
modified: '2026-09-01'
name: Indian Institute of Science Bangalore
nav: Providers
network: true
overview: 'Indian Institute of Science Bangalore publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including ETD@IISc DSpace 6 REST API, and 6 more. Tagged areas include Education, Higher Education, University, India, and Institute of Eminence.


  The Indian Institute of Science Bangalore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Indian Institute of Science Bangalore''s developer surface includes API reference, documentation, and 19 more developer resources.'
plans:
- name: Iisc Plans Pricing
  plan_count: 2
  slug: iisc-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Iisc Rate Limits
  slug: iisc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Indian Institute of Science Bangalore — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: iisc-jsonschema-spectral-rules
- authorship: derived
  effective_rule_count: 6
  extends: []
  name: Indian Institute of Science Bangalore API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: iisc-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.3
    catalog_earned_first_party: 0.0
    catalog_gap: 62.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 5.3
    contract_governance: 28.0
    contract_quality: 56.2
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/iisc/iisc-2026-06-20T183226.png
security:
- kind: domain-security
  name: Iisc Domain Security
  slug: iisc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iisc
tags:
- Education
- Higher Education
- University
- India
- Institute of Eminence
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Shibboleth
- Library
- LMS
- Research Computing
website: https://iisc.ac.in/
---
