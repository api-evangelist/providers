---
access_model:
  confidence: high
  label: Free · no registration
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://status.its.uq.edu.au
  baseurl_source: declared
  description: Keyless read-only JSON, RSS and SVG feeds describing the operational state of 678 University of Queensland systems across 43 service categories, plus every published incident. All five endpoints retur
  name: UQ Status API
  slug: status-api
- description: UQ operates a SAML 2.0 Shibboleth identity provider, entityID urn:mace:federation.org.au:testfed:uq.edu.au, with SSO endpoints for the HTTP-Redirect, HTTP-POST and HTTP-POST-SimpleSign bindings. The e
  name: UQ Identity Provider (SAML 2.0 / Shibboleth)
  slug: identity-federation
- description: 'REST API behind UQ eSpace, the institutional repository for UQ research outputs and datasets, operated on UQ''s own host by UQ Library. Not callable from outside the institution: every path probed on 2'
  name: UQ eSpace REST API
  slug: espace-api
- description: 'UQ''s internal API platform for transactional and business data, paired with the Data Hub synchronisation platform. Access is neither open nor self-service: consumers request access through the Integra'
  name: Central Integration Platform
  slug: central-integration
- description: UQ has no open data portal of its own. It publishes as an organisation on the Queensland Government's CKAN portal, where a live keyless package_search on 2026-08-30 returned a count of 2 datasets. Rec
  name: Queensland Government Open Data Portal (UQ organisation)
  slug: qld-open-data
- description: UQ's library discovery layer, a Primo VE tenancy on Ex Libris. No contract is saved under UQ — any Primo or Alma API definition belongs to Ex Libris and scores against Ex Libris.
  name: UQ Library discovery (Ex Libris Primo VE tenancy)
  slug: library-discovery
- description: UQ course reading lists hosted on Talis Aspire. Recorded as a tenant relationship; the Talis Aspire APIs are Talis's contract, not UQ's.
  name: UQ Reading Lists (Talis Aspire tenancy)
  slug: reading-lists
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.uq.edu.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uqlibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-queensland/
- group: operate
  title: ''
  type: Status
  url: https://status.its.uq.edu.au/
- group: company
  title: ''
  type: Blog
  url: https://news.uq.edu.au/
- group: operate
  title: ''
  type: Support
  url: https://support.my.uq.edu.au/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uq.edu.au/legal/copyright-privacy-disclaimer/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uq.edu.au/legal/website-terms-of-use/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp-prod.uq.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://espace.library.uq.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.uq.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://study.uq.edu.au/
- group: other
  title: ''
  type: ResearchComputing
  url: https://rcc.uq.edu.au/
- group: other
  title: ''
  type: OpenData
  url: https://www.data.qld.gov.au/organization/university-of-queensland
- group: other
  title: ''
  type: AIPolicy
  url: https://itali.uq.edu.au/teaching-guidance/artificial-intelligence-ai-and-learning-and-assessment
- group: build
  title: ''
  type: AITooling
  url: https://ai.uq.edu.au/
- group: company
  title: ''
  type: About
  url: https://about.uq.edu.au/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uq-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uq-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/uq-conformance.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/uq-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/uq-context.jsonld
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The University of Queensland (UQ) is a public research university in Brisbane, Australia, a member of the Group of Eight and of Universitas 21. Like nearly every institution of its kind, UQ is a federation of buyers rather than an API producer, and its programmable footprint has to be described honestly: UQ operates no developer portal, publishes no API terms, and offers no self-service registration for any interface. What it does operate, verified live on 2026-08-30, is three genuinely institution-run machine-readable surfaces. First, a keyless status API at status.its.uq.edu.au serving JSON, RSS and SVG covering 678 systems across 43 service categories. Second, a SAML 2.0 Shibboleth identity provider that self-serves its own EntityDescriptor at idp-prod.uq.edu.au and is registered in the Australian Access Federation alongside 27 UQ-operated service providers. Third, the UQ eSpace repository API on UQ''s own host api.library.uq.edu.au, built and run by UQ Library''s own engineering
  team in the open on GitHub, but blocked to outside clients by a CloudFront WAF. UQ''s institutional data platforms — the Central Integration Platform and Data Hub — are real but entirely gated behind an access-request process. Its discovery layer (Ex Libris Primo), reading lists (Talis Aspire) and open-data publishing (the Queensland Government CKAN portal) are tenancies on platforms other parties operate, and are recorded here as tenant relationships rather than as UQ contracts.'
examples:
- key_count: 2
  name: Uq Status Index Example
  slug: uq-status-index-example
finops:
- name: Uq Finops
  service_category: Education
  slug: uq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uq.png
json_schemas:
- name: UQ Status index document
  property_count: 15
  slug: uq-status-index
jsonld:
- class_count: 13
  name: Uq Context
  property_count: 5
  slug: uq-context
layout: provider
modified: '2026-08-30'
name: University of Queensland
nav: Providers
network: true
overview: 'University of Queensland publishes 1 API on the [APIs.io](https://apis.io/) network: UQ Status API. Tagged areas include University, Higher Education, Education, Australia, and Group of Eight.


  The University of Queensland catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Queensland''s developer surface includes status page, engineering blog, support, and 23 more developer resources.'
plans:
- name: Uq Plans Pricing
  plan_count: 2
  slug: uq-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Uq Rate Limits
  slug: uq-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Queensland API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: uq-status-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 7.6
    contract_quality: 19.8
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 7.6
    operational_transparency: 23.7
  previous_composite: 34.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uq/refs/heads/main/screenshots/uq-2026-06-20T200520.png
security:
- kind: authentication
  name: Uq Status Authentication
  slug: uq-status-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Uq Domain Security
  slug: uq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uq
tags:
- University
- Higher Education
- Education
- Australia
- Group of Eight
- Research
- Institutional Repository
- Identity Federation
- Status
- Library
- Research Computing
- Open Data
website: https://www.uq.edu.au/
---
