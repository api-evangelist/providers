---
access_model:
  confidence: high
  label: Free — one keyless public API, everything else gated on HKUST affiliation
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://www.ust.hk/'', ''status'': 301, ''note'': ''declared website redirects to https://hkust.edu.hk/ — a different registrable domain (ust.hk -> hkust.edu.hk), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  - probed
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://pathadvisor.ust.hk/api
  baseurl_source: declared
  description: 'Public, keyless JSON API behind HKUST Path Advisor, the university''s campus wayfinding service. Serves the campus spatial model: 7 buildings, 43 calibrated floor plans with metres-per-pixel and origin'
  name: HKUST Path Advisor API
  slug: path-advisor
- description: HKUST's Azure API Management tenant, operated by the IT Services Office. The gateway is live and callable at hkust.azure-api.net and returns the Azure APIM 401 "missing subscription key" on the two pr
  name: HKUST API Gateway and API Portal
  slug: api-gateway
- description: 'The institutional research data repository, running Dataverse 6.1 on Payara. HKUST self-hosts it: dataspace.hkust.edu.hk is on the university''s own registrable domain and CNAMEs to lbnx99.ust.hk on HK'
  name: DataSpace@HKUST Research Data Repository API
  slug: dataspace
- description: HKUST's own SAML 2.0 identity provider, serving machine-readable metadata at idp.ust.hk/idp/shibboleth. Asserts the scopes ust.hk, connect.ust.hk and alumni.ust.hk, and declares HTTP-POST, HTTP-POST-S
  name: HKUST Shibboleth Identity Provider
  slug: identity-federation
- description: HKUST Library is Crossref member 5801 and owns DOI prefix 10.14711, under which 14,453 records are registered and retrievable through the Crossref REST API — including the dataset DOIs minted by DataS
  name: HKUST Library Crossref DOI Registration
  slug: crossref-doi
- description: Central Elastic Stack repository established by ITSO to collect, search and visualise smart-campus data, including the IoT sensor inventory and sensor readings. It is institution-operated, but there i
  name: HKUST Open Data Platform
  slug: open-data-platform
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.ust.hk/
- group: docs
  title: ''
  type: Documentation
  url: https://itso.hkust.edu.hk/services/it-infrastructure/api-gateway-api-portal
- group: docs
  title: ''
  type: APIReference
  url: https://itso.hkust.edu.hk/services/it-infrastructure/smart-campus-infrastructure/open-data-platform/retrieve-iot-data-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hkust.developer.azure-api.net/
- group: operate
  title: ''
  type: Support
  url: https://itso.hkust.edu.hk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataprivacy.hkust.edu.hk/university-data-privacy-policy-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://hk.linkedin.com/school/hkust/
- group: other
  title: ''
  type: OpenData
  url: https://itso.hkust.edu.hk/services/it-infrastructure/smart-campus-infrastructure/open-data-platform
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataspace.hkust.edu.hk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.hkust.edu.hk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://w5.ab.ust.hk/wcq/cgi-bin/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.ust.hk/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://cei.hkust.edu.hk/en-hk/education-innovation/generative-ai-education
- group: build
  title: ''
  type: AITooling
  url: https://itso.hkust.edu.hk/services/it-infrastructure/azure-openai-api-service
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hkust-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hkust-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/hkust-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hkust-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hkust-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hkust-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hkust-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/hkust-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hkust-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hkust-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Hong Kong University of Science and Technology (HKUST) is a public research university in Clear Water Bay, Hong Kong SAR. Its programmable footprint is real but small and mostly closed. One API on an HKUST host is public and keyless: the Path Advisor campus wayfinding API at pathadvisor.ust.hk, which serves buildings, calibrated floor plans, point-of-interest categories and named map nodes with GeoJSON footprints, CORS-open and with no key. Beyond it, the IT Services Office runs an Azure API Management gateway and portal — live and callable at hkust.azure-api.net, but every product needs an ITSO account, a subscription request and human approval, and the catalog cannot be enumerated anonymously. DataSpace@HKUST is a Dataverse 6.1 instance HKUST self-hosts on its own domain and network, serving 151 published datasets over the upstream Dataverse Native API; its OAI-PMH provider is switched off. The institution''s most substantial machine-readable assets are not developer
  APIs at all: a Shibboleth SAML identity provider published into eduGAIN through the Hong Kong Access Federation, and HKUST Library''s Crossref membership under DOI prefix 10.14711, with 14,453 registered records. HKUST publishes no OpenAPI, no changelog, no status page and no security.txt for any of it. A previously catalogued API base URL of api.ust.hk does not exist — HKUST''s own authoritative nameservers return NXDOMAIN for that hostname — and has been removed.'
finops:
- name: Hkust Finops
  service_category: Education
  slug: hkust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hkust.png
json_schemas:
- name: HKUST Path Advisor Building
  property_count: 2
  slug: hkust-path-advisor-building
- name: HKUST Path Advisor Error
  property_count: 1
  slug: hkust-path-advisor-error
- name: HKUST Path Advisor Floor
  property_count: 16
  slug: hkust-path-advisor-floor
- name: HKUST Path Advisor MultiPolygon
  property_count: 2
  slug: hkust-path-advisor-multipolygon
- name: HKUST Path Advisor Node
  property_count: 7
  slug: hkust-path-advisor-node
- name: HKUST Path Advisor Tag
  property_count: 3
  slug: hkust-path-advisor-tag
jsonld:
- class_count: 10
  name: Hkust Context
  property_count: 2
  slug: hkust-context
layout: provider
modified: '2026-08-30'
name: Hong Kong University of Science and Technology
nav: Providers
network: true
overview: 'Hong Kong University of Science and Technology publishes 1 API on the [APIs.io](https://apis.io/) network: HKUST Path Advisor API. Tagged areas include University, Higher Education, Education, Research, and Hong Kong.


  The Hong Kong University of Science and Technology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hong Kong University of Science and Technology''s developer surface includes documentation, API reference, support, authentication, and 21 more developer resources.'
plans:
- name: Hkust Plans Pricing
  plan_count: 2
  slug: hkust-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Hkust Rate Limits
  slug: hkust-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Hong Kong University of Science and Technology API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: hkust-path-advisor-rules
scopes:
- name: Hkust Scopes
  scope_count: 0
  slug: hkust-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 70.3
    catalog_earned_first_party: 12.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 3.8
    contract_quality: 63.4
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 31.6
  previous_composite: 49.9
  provenance:
    conformance: first-party
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hkust/refs/heads/main/screenshots/hkust-2026-06-20T182813.png
security:
- kind: authentication
  name: Hkust Authentication
  slug: hkust-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hkust Domain Security
  slug: hkust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hkust
tags:
- University
- Higher Education
- Education
- Research
- Hong Kong
- China
- Research Data
- Open Data
- Identity Federation
- Course Catalog
- Library
- Smart Campus
- API Gateway
- Wayfinding
website: https://www.ust.hk/
---
