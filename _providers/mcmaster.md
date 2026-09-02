---
access_model:
  confidence: high
  label: Free and anonymous where public; MacID required for the developer portal
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
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
    error_semantics: false
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
  score: 20.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Public, unauthenticated JSON API behind McMaster Experts, the university''s researcher and expertise discovery gateway. Three operations confirmed by live probe on 2026-09-01: a cross-entity keyword se'
  name: McMaster Experts API
  slug: experts-api
- description: McMaster University Libraries' institutional repository of theses, dissertations and open-access research outputs. DSpace 8.2, self-hosted, holding 26,361 items with an earliest datestamp of 2014-06-1
  name: MacSphere Institutional Repository
  slug: macsphere
- description: McMaster's own SAML 2.0 Identity Provider, the authentication authority behind MacID. Publishes machine-readable SAML metadata anonymously at its entityID, carrying an IDPSSODescriptor, an AttributeAu
  name: McMaster University Shibboleth Identity Provider
  slug: shibboleth-idp
- description: Central API management developer portal operated by University Technology Services, running on Azure API Management. Both /apis and /products redirect to /signin, so neither the API catalog nor the pr
  name: McMaster API Service Developer Portal
  slug: developer-portal
- description: McMaster's research data repository, a named collection on the Borealis Canadian Dataverse Repository holding sub-collections including the McMaster Research Data Repository, the McMaster University W
  name: McMaster University Dataverse on Borealis
  slug: borealis-dataverse
- description: McMaster University's membership of DataCite as a consortium organisation within the Canadian DataCite consortium, giving it the ability to mint DOIs for research outputs and datasets. Recorded as a r
  name: McMaster University DataCite Registration
  slug: datacite
- description: McMaster University Library's Crossref membership, under which it mints DOIs on its own prefix 10.15173 for library-published scholarship. A publication record in the McMaster Experts API bearing this
  name: McMaster University Library Crossref Membership
  slug: crossref
- description: McMaster University's entry in the Research Organization Registry, the persistent identifier that links the institution across DataCite, Crossref and the wider scholarly infrastructure. Distinct ROR r
  name: McMaster University ROR Registration
  slug: ror
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.mcmaster.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.mcmaster.ca/
- group: docs
  title: ''
  type: APIReference
  url: openapi/mcmaster-experts-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mcmaster-experts-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mcmaster-experts-schemas.json
- group: build
  title: ''
  type: Examples
  url: examples/mcmaster-experts-examples.yml
- group: design
  title: ''
  type: Rules
  url: rules/mcmaster-experts-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mcmaster-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mcmaster-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/mcmaster-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/mcmaster-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mcmaster-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mcmaster-lifecycle.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://macsphere.mcmaster.ca/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.mcmaster.ca/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://academiccalendars.romcmaster.ca/
- group: other
  title: ''
  type: ResearchComputing
  url: https://research.mcmaster.ca/home/support-for-researchers/research-resources/mcmaster-it/rhpcs/
- group: other
  title: ''
  type: AIPolicy
  url: https://provost.mcmaster.ca/generative-artificial-intelligence-2/generative-ai-and-academic-integrity/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secretariat.mcmaster.ca/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/McMasterRS
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/mcmaster-university/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcmaster-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mcmaster-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mcmaster-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mcmaster-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mcmaster-context.jsonld
created: '2026-06-03'
description: 'McMaster University is a public research university in Hamilton, Ontario, Canada. Its programmable footprint is small but genuinely its own, and it is larger than a June 2026 pass concluded. McMaster operates an undocumented but fully public JSON API behind McMaster Experts, its researcher and expertise discovery gateway at experts.mcmaster.ca — a bespoke application, not a vendor research-information system — answering anonymously across 7,301 directory records and 273,828 scholarly works. It self-hosts MacSphere, a DSpace 8.2 institutional repository of 26,361 items with a conformant OAI-PMH 2.0 interface on its own domain. It operates its own Shibboleth Identity Provider, published into eduGAIN through the Canadian Access Federation, which is the strongest machine-readable surface most universities have and the one this cohort was most completely missing. It runs a central Azure API Management developer portal at developer.api.mcmaster.ca, but that portal is gated behind
  MacID sign-in and a registration step: neither the API catalog nor the product list can be read without an institutional account, so the size of McMaster''s actual internal API estate is unknown from outside. Beyond what it operates, McMaster holds real relationships on platforms it does not run — a named collection on the Borealis Dataverse, DataCite provider registration, and Crossref membership under McMaster University Library''s own DOI prefix. Those are facts about McMaster; the contracts belong to the platforms. McMaster publishes no status page, no llms.txt, no security.txt, no API terms of use and no rate-limit statement, and its course catalog exists only as a human surface on a Modern Campus deployment with no API.'
finops:
- name: Mcmaster Finops
  service_category: Education
  slug: mcmaster-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcmaster.png
json_schemas:
- name: McMaster Experts API schemas
  property_count: 0
  slug: mcmaster-experts-schemas
jsonld:
- class_count: 24
  name: Mcmaster Context
  property_count: 5
  slug: mcmaster-context
- class_count: 11
  name: Mcmaster Experts Context
  property_count: 12
  slug: mcmaster-experts-context
layout: provider
modified: '2026-09-01'
name: McMaster University
nav: Providers
network: true
overview: 'McMaster University publishes 1 API on the [APIs.io](https://apis.io/) network: McMaster Experts API. Tagged areas include University, Higher Education, Education, Canada, and Ontario.


  The McMaster University catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  McMaster University''s developer surface includes API reference, code examples, authentication, and 24 more developer resources.'
plans:
- name: Mcmaster Plans Pricing
  plan_count: 2
  slug: mcmaster-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Mcmaster Rate Limits
  slug: mcmaster-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: McMaster University API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: mcmaster-experts-rules
scopes:
- name: Mcmaster Scopes
  scope_count: 0
  slug: mcmaster-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 42.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 27.2
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 15.2
    contract_quality: 66.6
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 15.2
    operational_transparency: 26.3
  previous_composite: 21.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/mcmaster/refs/heads/main/screenshots/mcmaster-2026-06-20T185102.png
security:
- kind: authentication
  name: Mcmaster Authentication
  slug: mcmaster-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mcmaster Domain Security
  slug: mcmaster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcmaster
tags:
- University
- Higher Education
- Education
- Canada
- Ontario
- U15 Group of Canadian Research Universities
- Research
- Research Data
- Research Repository
- Identity Federation
- Scholarly Communication
- Open Access
- Library
- Course Catalog
website: https://www.mcmaster.ca/
---
