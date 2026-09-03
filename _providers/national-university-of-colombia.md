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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National University Of Colombia Agentic Access
  operation_count: 7
  slug: national-university-of-colombia-agentic-access
  summary_line: 7 operations
api_count: 2
apis:
- baseURL: https://bffrepositorio.unal.edu.co/server
  baseurl_source: declared
  description: 'OAI-PMH 2.0 metadata harvesting interface of the Repositorio Institucional UNAL, served from the university''s own host. Twelve metadata prefixes (oai_dc, qdc, mods, mets, didl, dim, etdms, marc, ore, '
  name: National University of Colombia OAI-PMH API
  slug: national-university-of-colombia-oai-pmh-api
- baseURL: https://bffrepositorio.unal.edu.co/server
  baseurl_source: declared
  description: Anonymous HAL+JSON read endpoints for the repository's community/collection structure on UNAL's own host. The contract documents only what a credential-free caller can actually reach on THIS deploymen
  name: National University of Colombia REST - Core API
  slug: national-university-of-colombia-rest-core-api
- baseURL: https://bffrepositorio.unal.edu.co/server
  baseurl_source: declared
  description: Faceted, anonymous search across archived objects in UNAL's institutional repository, on the university's own host. Verified live 2026-09-01.
  name: National University of Colombia REST - Discover API
  slug: national-university-of-colombia-rest-discover-api
- baseURL: https://revistas.unal.edu.co/index.php/index
  baseurl_source: declared
  description: 'A SECOND institution-operated OAI-PMH 2.0 endpoint, found in this run and not previously catalogued: the Portal de Revistas UN, UNAL''s own journal publishing platform on revistas.unal.edu.co, running '
  name: National University of Colombia Portal de Revistas UN OAI-PMH API
  slug: national-university-of-colombia-journals-oai-pmh-api
- description: UNAL's open data is not published on its own portal. datosabiertos.unal.edu.co is a static informational page with no catalogue and no API; the actual datasets sit on Colombia's national Socrata porta
  name: UNAL open data on datos.gov.co (Socrata)
  slug: datos-gov-co-publisher
- description: 'UNAL is a Crossref member in its own right — member id 6146, DOI prefix 10.15446 — with a second member record for its Faculty of Sciences, member id 21512, prefix 10.36385. This is a fact about UNAL '
  name: Crossref membership (DOI registrant)
  slug: crossref-membership
- description: UNAL is registered in the Research Organization Registry as https://ror.org/059yx9a68 ("National University of Colombia", UNAL), carrying GRID grid.10689.36, ISNI 0000 0004 9129 0751, Wikidata Q115041
  name: ROR organization identifier
  slug: ror-identifier
- description: catalogo.unal.edu.co runs Ex Libris Aleph on UNAL's own infrastructure (168.176.5.96), not on an Ex Libris cloud tenancy — the host verdict is institution, but the product is a vendor's and no Aleph c
  name: SINAB library catalog (self-hosted Ex Libris Aleph)
  slug: library-catalog-aleph
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: National University of Colombia - Institutional Repository OAI-PMH API
  slug: open-national-university-of-colombia-oai-pmh-api
- collection_type: open
  name: National University of Colombia - Institutional Repository OAI-PMH REST - Core API
  slug: open-national-university-of-colombia-rest-core-api
- collection_type: open
  name: National University of Colombia - Institutional Repository OAI-PMH REST - Discover API
  slug: open-national-university-of-colombia-rest-discover-api
common:
- group: company
  title: ''
  type: Website
  url: https://unal.edu.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-nacional-de-colombia/
- group: other
  title: ''
  type: OpenData
  url: https://datosabiertos.unal.edu.co/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositorio.unal.edu.co/
- group: other
  title: ''
  type: ScholarlyPublishing
  url: https://revistas.unal.edu.co/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogo.unal.edu.co/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://dninfoa.unal.edu.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.re3data.org/repository/r3d100013982
- group: design
  title: ''
  type: Conformance
  url: conformance/national-university-of-colombia-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-university-of-colombia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-university-of-colombia-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/national-university-of-colombia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/national-university-of-colombia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/national-university-of-colombia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The National University of Colombia (Universidad Nacional de Colombia, UNAL) is the country''s largest public research university, ranked #219 in the QS World University Rankings 2025. UNAL operates NO central developer portal, no API gateway and no documented public API program, and no llms.txt, ai.txt or .well-known/apis.json exists on unal.edu.co. What it does operate, on its own hosts, is scholarly infrastructure: a DSpace 7.6.5 institutional repository at bffrepositorio.unal.edu.co with an anonymous HAL+JSON REST API and an OAI-PMH 2.0 endpoint, and a second, independent OAI-PMH 2.0 endpoint on the Portal de Revistas UN (Open Journal Systems 3.4.0.10) serving 100+ journal sets. Beyond that its programmable footprint is relationships rather than engineering: six open datasets published as a named publisher scope on Colombia''s national Socrata portal datos.gov.co, a self-hosted Ex Libris Aleph library catalog whose X-Services gate answers with a configuration error, Crossref
  membership (prefix 10.15446), a ROR identifier, and single sign-on brokered by a commercial vendor rather than a Shibboleth IdP. Colombia has no eduGAIN federation, so the identity-federation surface most universities have does not exist here.'
examples:
- key_count: 2
  name: National University Of Colombia Listcollections Example
  slug: national-university-of-colombia-listCollections-example
- key_count: 2
  name: National University Of Colombia Listcommunities Example
  slug: national-university-of-colombia-listCommunities-example
- key_count: 3
  name: National University Of Colombia Oairecord Example
  slug: national-university-of-colombia-oaiRecord-example
finops:
- name: National University Of Colombia Finops
  service_category: Education
  slug: national-university-of-colombia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-university-of-colombia.png
json_schemas:
- name: DSpace Collection
  property_count: 8
  slug: national-university-of-colombia-collection
- name: DSpace Community
  property_count: 8
  slug: national-university-of-colombia-community
json_structures:
- name: National University Of Colombia Collection Structure
  property_count: 6
  slug: national-university-of-colombia-collection-structure
- name: National University Of Colombia Community Structure
  property_count: 6
  slug: national-university-of-colombia-community-structure
jsonld:
- class_count: 18
  name: National University Of Colombia Context
  property_count: 3
  slug: national-university-of-colombia-context
layout: provider
modified: '2026-09-01'
name: National University of Colombia
nav: Providers
network: true
overview: 'National University of Colombia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including OAI-PMH API, REST - Core API, REST - Discover API, and 1 more. Tagged areas include Education, Higher Education, University, Public Research University, and Colombia.


  The National University of Colombia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  National University of Colombia''s developer surface includes documentation and 15 more developer resources.'
plans:
- name: National University Of Colombia Plans Pricing
  plan_count: 2
  slug: national-university-of-colombia-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: National University Of Colombia Rate Limits
  slug: national-university-of-colombia-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: National University of Colombia API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: national-university-of-colombia-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: National University of Colombia API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 3
  slug: national-university-of-colombia-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 37.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 51.4
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 25.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: National University Of Colombia Domain Security
  slug: national-university-of-colombia-domain-security
  summary_line: TLSv1.2 · DMARC
slug: national-university-of-colombia
tags:
- Education
- Higher Education
- University
- Public Research University
- Colombia
- Latin America
- Open Data
- Institutional Repository
- Research Data
- Scholarly Publishing
- Library
- OAI-PMH
website: https://unal.edu.co/
---
