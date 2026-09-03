---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
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
  score: 28.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 76
  human_in_the_loop: 0
  name: University Of Vienna Agentic Access
  operation_count: 145
  slug: university-of-vienna-agentic-access
  summary_line: 145 operations · 76 acting
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for PHAIDRA, the University of Vienna's own institutional repository platform. Harvested by OpenAIRE, Europeana, BASE, OAPEN, EBSCO and Primo; supports oai_dc
  name: PHAIDRA OAI-PMH Endpoint
  slug: phaidra-oai-pmh
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests for transforming and validating datastreams
  name: PHAIDRA datastream API (University of Vienna)
  slug: university-of-vienna-datastream-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests related to users, user groups and organisation structure
  name: PHAIDRA directory API (University of Vienna)
  slug: university-of-vienna-directory-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests to the imageserver
  name: PHAIDRA imageserver API (University of Vienna)
  slug: university-of-vienna-imageserver-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests for manipulating object lists
  name: PHAIDRA lists API (University of Vienna)
  slug: university-of-vienna-lists-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: The misc API from University of Vienna — 7 operation(s) for misc.
  name: PHAIDRA misc API (University of Vienna)
  slug: university-of-vienna-misc-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Look at the [OAI-PMH protocol](https://www.openarchives.org/pmh) used in this endpoint
  name: PHAIDRA oai-pmh API (University of Vienna)
  slug: university-of-vienna-oai-pmh-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Additional requests for the manipulation of digital objects
  name: PHAIDRA object-advanced API (University of Vienna)
  slug: university-of-vienna-object-advanced-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Most important requests you'll need to manage digital objects in PHAIDRA
  name: PHAIDRA object-basics API (University of Vienna)
  slug: university-of-vienna-object-basics-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests for adding and removing object relationships
  name: PHAIDRA relationships API (University of Vienna)
  slug: university-of-vienna-relationships-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: The search API from University of Vienna — 1 operation(s) for search.
  name: PHAIDRA search API (University of Vienna)
  slug: university-of-vienna-search-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Session management
  name: PHAIDRA session API (University of Vienna)
  slug: university-of-vienna-session-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: The stats API from University of Vienna — 4 operation(s) for stats.
  name: PHAIDRA stats API (University of Vienna)
  slug: university-of-vienna-stats-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests for managing metadata templates
  name: PHAIDRA templates API (University of Vienna)
  slug: university-of-vienna-templates-api
- baseURL: https://phaidra.univie.ac.at/api
  baseurl_source: declared
  description: Requests for controlled vocabularies
  name: PHAIDRA vocabularies API (University of Vienna)
  slug: university-of-vienna-vocabularies-api
- description: 'u:cris is the University of Vienna''s research information system. It runs Elsevier Pure and says so in its own OAI-PMH Identify response: ''This service is based on Pure.'' The Pure Web Service is live '
  name: u:cris Research Information System (Elsevier Pure)
  slug: ucris-pure
- description: u:ai is the University of Vienna's AI assistant for staff and students, offered with API access for scripted and research use. The API base is https://univie-api.academic-ai.at - an institution-brande
  name: u:ai API (Academic AI)
  slug: uai-api
- description: 'An API gateway on the university''s apex domain. Probed 2026-08-30 on /, /v1, /api, /docs, /openapi.json, /swagger.json, /health and /.well-known/openapi: every path returns an identical structured JSO'
  name: api.univie.ac.at (authenticated gateway)
  slug: univie-api-gateway
- description: The university's SAML 2.0 identity provider, entityID https://weblogin.univie.ac.at/shibboleth, registered in the ACOnet Austrian research and education federation and propagated to eduGAIN. Its IDPSS
  name: University of Vienna Shibboleth Identity Provider
  slug: shibboleth-idp
- description: 'u:search is the Vienna University Library''s discovery layer. Probed 2026-08-30: https://usearch.univie.ac.at/ redirects to /primo-explore/search?vid=UWI - an Ex Libris Primo instance. Recorded as a TE'
  name: u:search Library Discovery (Ex Libris Primo)
  slug: usearch-primo
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PHAIDRA datastream API
  slug: open-university-of-vienna-datastream-api
- collection_type: open
  name: PHAIDRA datastream directory API
  slug: open-university-of-vienna-directory-api
- collection_type: open
  name: PHAIDRA datastream imageserver API
  slug: open-university-of-vienna-imageserver-api
- collection_type: open
  name: PHAIDRA datastream lists API
  slug: open-university-of-vienna-lists-api
- collection_type: open
  name: PHAIDRA datastream misc API
  slug: open-university-of-vienna-misc-api
- collection_type: open
  name: PHAIDRA datastream oai-pmh API
  slug: open-university-of-vienna-oai-pmh-api
- collection_type: open
  name: PHAIDRA datastream object-advanced API
  slug: open-university-of-vienna-object-advanced-api
- collection_type: open
  name: PHAIDRA datastream object-basics API
  slug: open-university-of-vienna-object-basics-api
- collection_type: open
  name: PHAIDRA datastream relationships API
  slug: open-university-of-vienna-relationships-api
- collection_type: open
  name: PHAIDRA datastream search API
  slug: open-university-of-vienna-search-api
- collection_type: open
  name: PHAIDRA datastream session API
  slug: open-university-of-vienna-session-api
- collection_type: open
  name: PHAIDRA datastream stats API
  slug: open-university-of-vienna-stats-api
- collection_type: open
  name: PHAIDRA datastream templates API
  slug: open-university-of-vienna-templates-api
- collection_type: open
  name: PHAIDRA datastream vocabularies API
  slug: open-university-of-vienna-vocabularies-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-vienna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-vienna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-vienna-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.univie.ac.at/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/univienna/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-vienna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-vienna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-vienna-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: docs
  title: ''
  type: Documentation
  url: https://phaidra.org/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/phaidra/phaidra-api/wiki/Documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phaidra
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.univie.ac.at/en/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dsba.univie.ac.at/en/data-protection-declaration/
- group: operate
  title: ''
  type: Support
  url: https://servicedesk.univie.ac.at/
- group: company
  title: ''
  type: Blog
  url: https://medienportal.univie.ac.at/en/uniview/
- group: other
  title: ''
  type: ResearchRepository
  url: https://rdm.univie.ac.at/phaidra-repository/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://usearch.univie.ac.at/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://ufind.univie.ac.at/en/
- group: other
  title: ''
  type: IdentityFederation
  url: https://eduid.at/md/aconet-registered.xml
- group: build
  title: ''
  type: AITooling
  url: https://zid.univie.ac.at/en/uai/uai-api-access/
- group: other
  title: ''
  type: AIPolicy
  url: https://studieren.univie.ac.at/en/using-ai-in-your-studies/uai-the-university-of-viennas-ai-tool/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-vienna-conformance.yml
created: '2026-06-03'
description: 'The University of Vienna (Universitat Wien), founded 1365, is Austria''s largest university and a member of LERU. Its programmable footprint is unusual for a university in one specific way: Vienna does not merely deploy a repository platform, it AUTHORS one. PHAIDRA (Permanent Hosting, Archiving and Indexing of Digital Resources and Assets) is open-source Fedora-based software built and hosted by the university''s Zentraler Informatikdienst and University Library, published under Apache 2.0 at github.com/phaidra, and deployed by 25+ institutions across Europe including Padua, Ca'' Foscari and IUAV. The OpenAPI in this repository is therefore the institution''s own engineering output, not a vendor''s contract running under its name. Everything else is bought: u:cris (research information) is Elsevier Pure, u:search is Ex Libris Primo, and u:ai runs on the ACOmarket-operated Academic AI platform shared by 20+ Austrian universities - all recorded here as tenant relationships,
  not as Vienna''s contracts. The university also operates a Shibboleth identity provider registered in the ACOnet federation and eduGAIN, and an authenticated API gateway at api.univie.ac.at. There is no central branded developer portal, no public API documentation site, and no official GitHub organization for the institution itself (github.com/univie is an unrelated personal account).'
examples:
- key_count: 3
  name: University Of Vienna Object Info Example
  slug: university-of-vienna-object-info-example
- key_count: 3
  name: University Of Vienna Search Select Example
  slug: university-of-vienna-search-select-example
finops:
- name: University Of Vienna Finops
  service_category: Education
  slug: university-of-vienna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-vienna.png
json_schemas:
- name: PHAIDRA Solr Index Document
  property_count: 29
  slug: university-of-vienna-index
- name: PHAIDRA Object Info
  property_count: 30
  slug: university-of-vienna-object-info
json_structures:
- name: University Of Vienna Index Structure
  property_count: 29
  slug: university-of-vienna-index-structure
- name: University Of Vienna Object Info Structure
  property_count: 30
  slug: university-of-vienna-object-info-structure
jsonld:
- class_count: 28
  name: University Of Vienna Context
  property_count: 0
  slug: university-of-vienna-context
layout: provider
modified: '2026-08-30'
name: University of Vienna
nav: Providers
network: true
overview: 'University of Vienna publishes 14 APIs on the [APIs.io](https://apis.io/) network, including PHAIDRA datastream API (University of Vienna), PHAIDRA directory API (University of Vienna), PHAIDRA imageserver API (University of Vienna), and 11 more. Tagged areas include Education, Higher Education, University, Public Research University, and Austria.


  The University of Vienna catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Vienna''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 18 more developer resources.'
plans:
- name: University Of Vienna Plans Pricing
  plan_count: 2
  slug: university-of-vienna-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Vienna Rate Limits
  slug: university-of-vienna-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Vienna API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-vienna-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: University of Vienna API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: university-of-vienna-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 39.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 58.6
    developer_ergonomics: 28.6
    discoverability: 63.0
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-vienna/refs/heads/main/screenshots/university-of-vienna-2026-06-20T200302.png
security:
- kind: authentication
  name: University Of Vienna Authentication
  slug: university-of-vienna-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: University Of Vienna Domain Security
  slug: university-of-vienna-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-vienna
tags:
- Education
- Higher Education
- University
- Public Research University
- Austria
- Europe
- Research
- Research Data
- Repository
- Open-Source
- Digital Preservation
- Identity Federation
- OAI-PMH
- Library
- Course Catalog
website: https://www.univie.ac.at/en/
---
