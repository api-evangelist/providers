---
access_model:
  confidence: high
  label: Free · anonymous open read, no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Lausanne Agentic Access
  operation_count: 6
  slug: university-of-lausanne-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- baseURL: https://spica.unil.ch
  baseurl_source: declared
  description: The SPICA single-cell / spatial atlas project listing, on UNIL's own host spica.unil.ch. Anonymous open read, confirmed 200 on 2026-09-01. SPICA is UNIL-built and UNIL-run; the host, the application a
  name: SPICA Atlas Projects.json API
  slug: university-of-lausanne-projects-json-api
- baseURL: https://spica.unil.ch
  baseurl_source: declared
  description: 'SPICA project query and archive download on UNIL''s own host: filter by reference atlas (ref_id), free-text search across metadata and paginate. /projects/query.json confirmed 200 anonymously on 2026-0'
  name: SPICA Atlas Projects API
  slug: university-of-lausanne-projects-api
- baseURL: https://api.unil.ch/iris/server/api
  baseurl_source: declared
  description: Community and collection resources of IRIS, UNIL's institutional research information system and open-access repository, served from UNIL's own host api.unil.ch behind a Kong gateway. /core/communitie
  name: IRIS Repository Core API (DSpace REST)
  slug: university-of-lausanne-core-api
- baseURL: https://api.unil.ch/iris/server/api
  baseurl_source: declared
  description: DSpace Discovery search across everything indexed in IRIS. Confirmed anonymous 200 on 2026-09-01, reporting a last page of 253,798 at size=1, i.e. 253,799 indexed objects. This matters because /core/i
  name: IRIS Repository Discover API (DSpace Discovery)
  slug: university-of-lausanne-discover-api
- baseURL: https://api.unil.ch/iris/server/api
  baseurl_source: declared
  description: The IRIS DSpace REST root document, exposing version metadata and a HAL hypermedia catalogue of 92 link relations. On 2026-09-01 it reported irisVersion 1.3.13 and irisRole "follower" — drifted from t
  name: IRIS Repository API root (DSpace REST)
  slug: university-of-lausanne-iris-repository-dspace-rest-api-api
- baseURL: https://api.unil.ch/iris/server/oai/request
  baseurl_source: declared
  description: 'OAI-PMH 2.0 metadata harvesting for IRIS, on UNIL''s own host. Two contexts answer anonymously: /oai/request (11 metadata prefixes — oai_dc, qdc, dim, mods, marc, rdf, ore, mets, didl, etdms, uketd_dc '
  name: IRIS OAI-PMH
  slug: university-of-lausanne-oai-pmh-api
- description: UNIL's own Shibboleth identity provider, entityID https://aai.unil.ch/idp/shibboleth, carrying an IDPSSODescriptor with OrganizationName "unil.ch", OrganizationDisplayName "Université de Lausanne" and
  name: UNIL Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: unil-shibboleth-idp
- description: UNIL's membership of the DataCite DOI registry, not DataCite's contract. api.datacite.org/clients?query=unil returns client PWKB.PGDJAM, name "Old DOIs Unil", clientType repository, created 2025-12-12
  name: DataCite repository registration (UNIL data service)
  slug: datacite-repository-registration
- description: UNIL's entry in the Research Organization Registry, https://ror.org/019whta54, established 1537, domain unil.ch, cross-walked to Fundref 501100006390, GRID grid.9851.5, ISNI 0000 0001 2165 4204 and Wi
  name: ROR organisation registration
  slug: ror-registration
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IRIS Repository (DSpace REST API) Core API
  slug: open-university-of-lausanne-core-api
- collection_type: open
  name: IRIS Repository (DSpace REST API) Core IRIS Repository (DSpace REST API) API
  slug: open-university-of-lausanne-iris-repository-dspace-rest-api-api
- collection_type: open
  name: IRIS Repository (DSpace REST API) Core Projects API
  slug: open-university-of-lausanne-projects-api
- collection_type: open
  name: IRIS Repository (DSpace REST API) Core Projects.json API
  slug: open-university-of-lausanne-projects-json-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.unil.ch
- group: docs
  title: ''
  type: Documentation
  url: https://spica.unil.ch/home/api
- group: docs
  title: ''
  type: APIReference
  url: https://api.unil.ch/iris/server/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openscienceunil
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-lausanne/
- group: company
  title: ''
  type: Blog
  url: https://news.unil.ch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unil.ch/unil/en/home/termes/conditions/protection-des-donnees.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unil.ch/unil/en/home/termes/conditions/informations-legales.html
- group: operate
  title: ''
  type: Support
  url: https://www.unil.ch/ci/en/home/menuinst/catalogue-de-services/support-et-formation/help-desk.html
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.unil.ch/.well-known/security.txt
- group: other
  title: ''
  type: SignIn
  url: https://my.unil.ch/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.unil.ch/ci/fr/home/menuinst/catalogue-de-services/authentification-et-comptes/authentification-aai.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://iris.unil.ch
- group: learn
  title: ''
  type: CourseCatalog
  url: https://applicationspub.unil.ch/interpub/noauth/php/Ud/index.php?v_lang=en
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.unil.ch/ci/dcsr
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unil.ch/unil/en/home/menuinst/universite/intelligence-artificielle.html
- group: build
  title: ''
  type: AITooling
  url: https://www.unil.ch/unil/en/home/menuinst/universite/intelligence-artificielle/faq.html
- group: other
  title: ''
  type: OpenScience
  url: https://www.unil.ch/unil/en/home/menuinst/recherche/open-science.html
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-lausanne-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-lausanne-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-lausanne-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-lausanne-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-lausanne-vocabulary.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-lausanne-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-lausanne-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-lausanne-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-lausanne-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-lausanne-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Lausanne (UNIL) is a public research university in Lausanne, Switzerland, founded in 1537, with roughly 17,000 students across seven faculties and ROR identifier https://ror.org/019whta54. UNIL publishes no developer portal, no API key programme, no API terms and no changelog, and no central catalogue of its own interfaces exists — but unlike most of this cohort its small programmable footprint is genuinely its own rather than a vendor''s contract wearing its name. Three surfaces answer anonymously on UNIL''s own registrable domain: the SPICA single-cell / spatial atlas JSON API at spica.unil.ch; the IRIS institutional research repository''s DSpace-CRIS REST API at api.unil.ch/iris/server/api, behind a Kong gateway, with 253,799 indexed objects reachable through Discovery search while /core/items and /core/bitstreams answer 401; and two anonymous OAI-PMH 2.0 harvesting contexts on the same host, one of them declaring OpenAIRE Guidelines for CRIS Managers v1.1.
  Beyond the contracts, UNIL operates its own Shibboleth identity provider (entityID https://aai.unil.ch/idp/shibboleth, scope unil.ch) registered in SWITCHaai and exported to eduGAIN, and holds a DataCite repository registration minting DOIs under prefix 10.48657. Everything else — student information, timetables, course registration — sits behind the my.unil.ch SSO gateway and is not documented as an API anywhere. No OpenAPI, AsyncAPI or MCP server is published by UNIL itself; every contract in this repository was written by API Evangelist from live probes and is marked as such.'
examples:
- key_count: 1
  name: University Of Lausanne Datacite Client Example
  slug: university-of-lausanne-datacite-client-example
- key_count: 3
  name: University Of Lausanne Listcollections Example
  slug: university-of-lausanne-listCollections-example
- key_count: 2
  name: University Of Lausanne Listcommunities Example
  slug: university-of-lausanne-listCommunities-example
- key_count: 2
  name: University Of Lausanne Queryprojects Example
  slug: university-of-lausanne-queryProjects-example
- key_count: 10
  name: University Of Lausanne Searchobjects Example
  slug: university-of-lausanne-searchObjects-example
finops:
- name: University Of Lausanne Finops
  service_category: Education
  slug: university-of-lausanne-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-lausanne.png
json_schemas:
- name: DSpace Community
  property_count: 9
  slug: university-of-lausanne-community
- name: SPICA Project
  property_count: 11
  slug: university-of-lausanne-project
json_structures:
- name: University Of Lausanne Community Structure
  property_count: 8
  slug: university-of-lausanne-community-structure
- name: University Of Lausanne Project Structure
  property_count: 11
  slug: university-of-lausanne-project-structure
jsonld:
- class_count: 14
  name: University Of Lausanne Context
  property_count: 6
  slug: university-of-lausanne-context
layout: provider
modified: '2026-09-01'
name: University of Lausanne
nav: Providers
network: true
overview: 'University of Lausanne publishes 6 APIs on the [APIs.io](https://apis.io/) network, including SPICA Atlas Projects.json API, SPICA Atlas Projects API, IRIS Repository Core API (DSpace REST), and 3 more. Tagged areas include Education, Higher Education, University, Switzerland, and Open Science.


  The University of Lausanne catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Lausanne''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 24 more developer resources.'
plans:
- name: University Of Lausanne Plans Pricing
  plan_count: 2
  slug: university-of-lausanne-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: University Of Lausanne Rate Limits
  slug: university-of-lausanne-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Lausanne API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-lausanne-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: University of Lausanne API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: university-of-lausanne-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 58.9
    developer_ergonomics: 35.7
    discoverability: 85.2
    governance: 35.6
    operational_transparency: 10.5
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-lausanne/refs/heads/main/screenshots/university-of-lausanne-2026-06-20T200157.png
security:
- kind: authentication
  name: University Of Lausanne Authentication
  slug: university-of-lausanne-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Lausanne Domain Security
  slug: university-of-lausanne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-lausanne
tags:
- Education
- Higher Education
- University
- Switzerland
- Open Science
- Research Data
- Institutional Repository
- Research Repository
- Identity Federation
- OAI-PMH
- Course Catalog
- Research Computing
website: https://www.unil.ch
---
