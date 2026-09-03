---
access_model:
  confidence: high
  label: Free, anonymous, undocumented
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 26.3
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://ruor.uottawa.ca/server/api
  baseurl_source: declared
  description: 'Public DSpace 8.3 REST/HATEOAS API for uO Research (Recherche uO Research), the University of Ottawa Library''s self-hosted institutional repository. Probed 2026-09-01: the root returns HTTP 200 applic'
  name: uO Research DSpace REST API
  slug: ruor-rest
- baseURL: https://ruor.uottawa.ca/server/oai/request
  baseurl_source: declared
  description: 'OAI-PMH 2.0 metadata-harvesting provider for uO Research. Probed 2026-09-01: Identify returns repositoryName "Recherche uO Research", repositoryIdentifier ruor.uottawa.ca, adminEmail ruor@uottawa.ca, '
  name: uO Research OAI-PMH
  slug: ruor-oai
- baseURL: https://www.uottawa.ca/en/jsonapi
  baseurl_source: declared
  description: 'Undocumented, anonymously readable JSON:API 1.0 surface on the University of Ottawa''s own Drupal web platform. Probed 2026-09-01: https://www.uottawa.ca/jsonapi returns HTTP 200 application/vnd.api+js'
  name: uottawa.ca Content JSON:API
  slug: www-jsonapi
- description: 'The University of Ottawa''s own SAML 2.0 identity provider and its published federation metadata. Probed 2026-09-01: https://fca-caf.uottawa.ca/idp/shibboleth returns HTTP 200 application/xml (7,299 by'
  name: uOttawa Shibboleth Identity Provider (Canadian Access Federation)
  slug: caf-idp
- description: 'uOttawa''s academic course catalogue, served on a uOttawa hostname but operated by Leepfrog Technologies: catalogue.uottawa.ca is a CNAME to uottawa-ca-public.courseleaf.com (12.175.6.54). CourseLeaf''s'
  name: uOttawa Course Catalogue (CourseLeaf tenancy)
  slug: catalogue-courseleaf
- description: 'The University of Ottawa''s research-data collection on Borealis, the Canadian Dataverse repository run by Scholars Portal / OCUL for CRKN. Probed 2026-09-01: GET https://borealisdata.ca/api/dataverses'
  name: uOttawa Dataverse collection on Borealis
  slug: borealis-dataverse
- description: uOttawa Library's discovery layer, Omni, is an Ex Libris Primo VE view delivered through the Ontario Council of University Libraries consortium at ocul-uo.primo.exlibrisgroup.com (CNAME ca01.primo.exl
  name: Omni library discovery (Ex Libris Primo VE tenancy)
  slug: omni-primo
- description: 'The University of Ottawa is a DataCite member and DOI registrant. Probed 2026-09-01: GET https://api.datacite.org/providers/uott returns HTTP 200 with name "University of Ottawa", symbol UOTT, memberT'
  name: DataCite membership (UOTT)
  slug: datacite
- description: Two Crossref member records belong to the institution. Member 7569, "University of Ottawa Library", holds prefixes 10.18192 and 10.51224 with 3,860 DOIs (989 current, 2,871 backfile); member 16151, "U
  name: Crossref membership (7569, 16151)
  slug: crossref
- description: 'The University of Ottawa is registered in the Research Organization Registry as https://ror.org/03c4mmv16, domain uottawa.ca, created 2018-11-14 and last modified 2026-07-20 in the ROR record. Probed '
  name: ROR registration (03c4mmv16)
  slug: ror
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.uottawa.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uottawa-wcms
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/uottawa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uottawa.ca/about-us/administration-services/aipo/privacy-rights/website-privacy-statement
- group: other
  title: ''
  type: Policies
  url: https://www.uottawa.ca/about-us/policies-regulations
- group: operate
  title: ''
  type: Support
  url: https://it.uottawa.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.uottawa.ca/about-us/news-all
- group: other
  title: ''
  type: ResearchRepository
  url: https://ruor.uottawa.ca/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ocul-uo.primo.exlibrisgroup.com/discovery/search?vid=01OCUL_UO:UO_DEFAULT
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalogue.uottawa.ca/en/
- group: other
  title: ''
  type: IdentityFederation
  url: https://fca-caf.uottawa.ca/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uottawa.ca/about-us/information-technology/it-artificial-intelligence/Cybersecurity-AI-guidelines
- group: build
  title: ''
  type: AITooling
  url: https://www.uottawa.ca/library/copyright/additional-resources/generative-ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-ottawa-ruor-dspace-rest-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-ottawa-ruor-community-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/university-of-ottawa-ruor-oai-identify-example.xml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-ottawa-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-ottawa-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-ottawa-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-ottawa-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-ottawa-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-ottawa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-ottawa-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-ottawa-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-ottawa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-ottawa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-ottawa-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Ottawa (uOttawa / Universite d''Ottawa) is a public bilingual research university in Ottawa, Ontario, Canada, and the largest English-French bilingual university in the world. Its programmable footprint is small, undocumented, and almost entirely a by-product of the platforms it runs rather than anything it sells or supports: uOttawa publishes no developer portal, no API gateway, no OpenAPI, no llms.txt and no security.txt, and api.uottawa.ca and developer.uottawa.ca do not resolve. What it does operate itself, on its own hosts, is worth naming precisely. uO Research (Recherche uO Research) at ruor.uottawa.ca is a self-hosted DSpace 8.3 institutional repository exposing a public REST/HATEOAS API and an OAI-PMH 2.0 provider with fourteen metadata formats; www.uottawa.ca serves an undocumented but fully anonymous Drupal JSON:API surface advertising 287 resource types; and fca-caf.uottawa.ca runs the institution''s own Shibboleth SAML 2.0 identity provider, registered
  in the Canadian Access Federation by CANARIE and interfederated through eduGAIN. Everything else that looks like a uOttawa API belongs to a vendor: the Omni library discovery layer is Ex Libris Primo VE via the OCUL consortium, the course catalogue at catalogue.uottawa.ca is Leepfrog CourseLeaf (CNAME uottawa-ca-public.courseleaf.com), and the research-data collection is a Borealis (Dataverse) tenancy. Those are recorded here as tenant relationships, never as uOttawa contracts. The institution is also a registrant in three identifier registries - DataCite (member UOTT, repository uott.library, prefix 10.20381), Crossref (members 7569 and 16151), and ROR (03c4mmv16) - which is a fact about uOttawa even though the registries'' own APIs are not.'
examples:
- key_count: 3
  name: University Of Ottawa Ruor Communities Example
  slug: university-of-ottawa-ruor-communities-example
- key_count: 3
  name: University Of Ottawa Www Jsonapi Article Example
  slug: university-of-ottawa-www-jsonapi-article-example
finops:
- name: University Of Ottawa Finops
  service_category: Education
  slug: university-of-ottawa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-ottawa.png
json_schemas:
- name: uO Research DSpace Community
  property_count: 9
  slug: university-of-ottawa-ruor-community
- name: uottawa.ca JSON:API article resource
  property_count: 5
  slug: university-of-ottawa-www-jsonapi-article
jsonld:
- class_count: 17
  name: University Of Ottawa Context
  property_count: 14
  slug: university-of-ottawa-context
layout: provider
modified: '2026-09-01'
name: University of Ottawa
nav: Providers
network: true
overview: 'University of Ottawa publishes 3 APIs on the [APIs.io](https://apis.io/) network: uO Research DSpace REST API, uO Research OAI-PMH, and uottawa.ca Content JSON:API. Tagged areas include University, Higher Education, Education, Canada, and Ontario.


  The University of Ottawa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Ottawa''s developer surface includes GitHub presence, support, engineering blog, code examples, authentication, and 23 more developer resources.'
plans:
- name: University Of Ottawa Plans Pricing
  plan_count: 2
  slug: university-of-ottawa-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: University Of Ottawa Rate Limits
  slug: university-of-ottawa-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of Ottawa API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-ottawa-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 34.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 15.2
    contract_quality: 60.5
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-ottawa/refs/heads/main/screenshots/university-of-ottawa-2026-06-20T200215.png
security:
- kind: authentication
  name: University Of Ottawa Authentication
  slug: university-of-ottawa-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Ottawa Domain Security
  slug: university-of-ottawa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-ottawa
tags:
- University
- Higher Education
- Education
- Canada
- Ontario
- Bilingual
- Public Research University
- U15
- Institutional Repository
- Research Data
- Library
- Course Catalog
- Identity Federation
- Shibboleth
- SAML
- DSpace
- OAI-PMH
- JSON API
- Open Access
- DataCite
- Crossref
- ROR
website: https://www.uottawa.ca/
---
