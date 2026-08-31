---
access_model:
  confidence: high
  label: Free · no key required for catalog metadata
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Cape Town Agentic Access
  operation_count: 5
  slug: university-of-cape-town-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: DataFirst is a University of Cape Town research unit and data service providing online access to survey and administrative microdata from South Africa and other African countries. Its open data portal
  name: DataFirst Microdata Catalog API (NADA)
  slug: datafirst-nada
- description: OpenUCT is the University of Cape Town's open access institutional repository, running DSpace 7.4 on UCT's own host. It preserves and openly shares UCT scholarly outputs including theses, dissertation
  name: OpenUCT Institutional Repository OAI-PMH
  slug: openuct-oai-pmh
- description: 'The OpenUCT repository additionally exposes the DSpace 7 REST API anonymously at open.uct.ac.za/server/api, returning application/hal+json. Probed live on 2026-08-30: the API root reports dspaceName O'
  name: OpenUCT DSpace REST API
  slug: openuct-dspace-rest
- description: UCT's Information and Communication Technology Services operates a SAML 2.0 identity provider registered in the South African Identity Federation (SAFIRE, registry id 000002) and published onward to e
  name: UCT Identity Provider (SAML 2.0 / SAFIRE / eduGAIN)
  slug: identity-provider
- description: 'ZivaHub is UCT''s institutional open data repository for research data and scholarly outputs. It is a Figshare for Institutions TENANCY, not a UCT system: zivahub.uct.ac.za CNAMEs to figshare.com, and '
  name: ZivaHub Open Data (Figshare for Institutions tenancy)
  slug: zivahub-figshare
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DataFirst Microdata API (NADA) Catalog API
  slug: open-university-of-cape-town-catalog-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.uct.ac.za/
- group: other
  title: ''
  type: OpenData
  url: https://www.datafirst.uct.ac.za/
- group: other
  title: ''
  type: ResearchRepository
  url: https://open.uct.ac.za/
- group: other
  title: ''
  type: ResearchRepository
  url: https://zivahub.uct.ac.za/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.safire.ac.za/safire-prod-idp.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://ucthpc.uct.ac.za/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.uct.ac.za/eresearch
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.uct.ac.za/
- group: other
  title: ''
  type: AIPolicy
  url: https://cilt.uct.ac.za/artificial-intelligence
- group: other
  title: ''
  type: AIPolicy
  url: https://libguides.lib.uct.ac.za/c.php?g=1440358&p=11020298
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uct-eresearch
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uct-cbio
- group: company
  title: ''
  type: LinkedIn
  url: https://za.linkedin.com/school/university-of-cape-town/
- group: company
  title: ''
  type: Blog
  url: https://www.news.uct.ac.za/
- group: operate
  title: ''
  type: Support
  url: https://icts.uct.ac.za/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uct.ac.za/calendar/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uct.ac.za/protection-personal-information-act-popia
- group: other
  title: ''
  type: x-ror
  url: https://ror.org/03p74gp79
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/university-of-cape-town-datafirst-nada.yaml
- group: design
  title: ''
  type: x-conformance
  url: conformance/university-of-cape-town-conformance.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/university-of-cape-town-authentication.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-cape-town-errors.yml
- group: docs
  title: ''
  type: x-json-schema
  url: json-schema/university-of-cape-town-study-schema.json
- group: docs
  title: ''
  type: x-json-schema
  url: json-schema/university-of-cape-town-datafile-schema.json
- group: docs
  title: ''
  type: x-json-schema
  url: json-schema/university-of-cape-town-variable-schema.json
- group: other
  title: ''
  type: x-json-structure
  url: json-structure/university-of-cape-town-study-structure.json
- group: design
  title: ''
  type: x-spectral-rules
  url: rules/university-of-cape-town-rules.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-cape-town-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-cape-town-context.jsonld
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-cape-town-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-cape-town-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-cape-town-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-cape-town-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-cape-town-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-cape-town-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Cape Town (UCT) is South Africa''s oldest and highest-ranked public research university and the top-ranked institution on the African continent. UCT operates no central developer portal and publishes no institution-wide API programme; its student-information, finance, HR and learning-management systems are vendor platforms behind institutional authentication and are not programmable from outside. What UCT does operate itself is a small, genuinely first-party research-data footprint: DataFirst, a UCT research unit, runs a NADA microdata catalog on www.datafirst.uct.ac.za with a public unauthenticated REST/JSON API over 582 studies; OpenUCT, the institutional repository, runs DSpace 7.4 on open.uct.ac.za and exposes both an OAI-PMH 2.0 harvesting endpoint and the DSpace REST API anonymously; and UCT''s ICTS operates a SAML 2.0 identity provider registered in the South African Identity Federation (SAFIRE) and published to eduGAIN. UCT is a DataCite direct member
  (symbol DAFI, ROR 03p74gp79) minting under prefixes 10.25828 and 10.25375. ZivaHub, the open data repository, is a Figshare for Institutions tenancy — zivahub.uct.ac.za CNAMEs to figshare.com — so the data is UCT''s and the API contract is Figshare''s; it is recorded here as a tenant relationship and is deliberately not scored as UCT engineering.'
examples:
- key_count: 3
  name: University Of Cape Town Getstudy Example
  slug: university-of-cape-town-getStudy-example
- key_count: 2
  name: University Of Cape Town Listcatalog Example
  slug: university-of-cape-town-listCatalog-example
- key_count: 3
  name: University Of Cape Town Liststudyvariables Example
  slug: university-of-cape-town-listStudyVariables-example
finops:
- name: University Of Cape Town Finops
  service_category: Education
  slug: university-of-cape-town-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-cape-town.png
json_schemas:
- name: DataFirst Study Data File
  property_count: 13
  slug: university-of-cape-town-datafile
- name: DataFirst Catalog Study
  property_count: 13
  slug: university-of-cape-town-study
- name: DataFirst Study Variable
  property_count: 6
  slug: university-of-cape-town-variable
json_structures:
- name: University Of Cape Town Study Structure
  property_count: 13
  slug: university-of-cape-town-study-structure
jsonld:
- class_count: 25
  name: University Of Cape Town Context
  property_count: 6
  slug: university-of-cape-town-context
layout: provider
modified: '2026-08-30'
name: University of Cape Town
nav: Providers
network: true
overview: 'University of Cape Town publishes 1 API on the [APIs.io](https://apis.io/) network: DataFirst Microdata Catalog API (NADA). Tagged areas include University, Higher Education, Education, Public Research University, and South Africa.


  The University of Cape Town catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Cape Town''s developer surface includes GitHub presence, engineering blog, support, and 33 more developer resources.'
plans:
- name: University Of Cape Town Plans Pricing
  plan_count: 2
  slug: university-of-cape-town-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: University Of Cape Town Rate Limits
  slug: university-of-cape-town-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Cape Town API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-cape-town-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: University of Cape Town API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: university-of-cape-town-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-cape-town/refs/heads/main/screenshots/university-of-cape-town-2026-06-20T200148.png
security:
- kind: authentication
  name: University Of Cape Town Authentication
  slug: university-of-cape-town-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Cape Town Domain Security
  slug: university-of-cape-town-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-cape-town
tags:
- University
- Higher Education
- Education
- Public Research University
- South Africa
- Africa
- Research Data
- Open Data
- Institutional Repository
- OAI-PMH
- Identity Federation
- Microdata
- Research Computing
website: https://www.uct.ac.za/
---
