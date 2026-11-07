---
access_model:
  confidence: high
  label: Free · registration and institutional approval required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - documentation
  - terms-of-service
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Anonymous OAI-PMH 2.0 metadata-harvesting endpoint over the NYCU Dataverse research-data repository ("NYCU Dataverse Dataverse OAI Archive"). Verified with verb=Identify on 2026-09-01. Serves Datacite
  name: NYCU Dataverse OAI-PMH Endpoint
  slug: dataverse-oai-pmh
- description: Anonymous OAI-PMH 2.0 harvesting endpoint over the NYCU institutional repository (國立陽明交通大學機構典藏), running back to 2014. Verified with verb=Identify on 2026-09-01. Serves didl, mods, ore, mets, xoai, da
  name: NYCU Institutional Repository OAI-PMH Endpoint
  slug: ir-oai-pmh
- description: NYCU Dataverse, the university library's research-data repository — a self-hosted deployment of Dataverse Project v5.10.1 holding 290 published datasets under DOI prefix 10.57770. Institution-operated
  name: NYCU Dataverse (Dataverse Project deployment)
  slug: dataverse
- description: 國立陽明交通大學機構典藏 — the NYCU institutional repository, a self-hosted DSpace 11 deployment with content back to 2014. Its DSpace REST API at /server/api answers anonymous requests, but that contract belongs
  name: NYCU Institutional Repository (DSpace deployment)
  slug: institutional-repository
- description: 'NYCU''s library discovery layer, an Ex Libris Primo tenancy. Recorded as a real institutional relationship. No Ex Libris contract is saved under this institution — Primo''s APIs are Ex Libris''s product '
  name: NYCU Library Discovery (Ex Libris Primo tenancy)
  slug: primo
- description: NYCU is a DataCite direct member in its own name — provider gtfe — and operates the DataCite repository client gtfe.kagikv, "NYCU Research Data Service", minting DOIs on prefix 10.57770. A registry me
  name: DataCite Membership — NYCU Research Data Service
  slug: datacite
- description: 'NYCU''s entry in the Research Organization Registry, ROR ID 00se2k293 — the canonical machine-readable identifier for the institution as an organization, and the join key most scholarly infrastructure '
  name: ROR Registration
  slug: ror
- baseURL: https://id.nycu.edu.tw
  baseurl_source: declared
  description: Consented NYCU user identity attributes.
  name: National Yang Ming Chiao Tung University Profile API
  slug: nycu-profile-api
- baseURL: https://dataverse.lib.nycu.edu.tw/oai
  baseurl_source: declared
  description: OAuth 2.0 authorization-code endpoints.
  name: National Yang Ming Chiao Tung University O Auth API
  slug: nycu-oauth-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.nycu.edu.tw/nycu/ch/index
- group: company
  title: ''
  type: Website
  url: https://www.nycu.edu.tw/nycu/en/index
- group: start
  title: ''
  type: DeveloperPortal
  url: https://id.nycu.edu.tw/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://id.nycu.edu.tw/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://id.nycu.edu.tw/docs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://id.nycu.edu.tw/policy/
- group: operate
  title: ''
  type: Support
  url: https://github.com/NYCU-OAuth/issue-report
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NYCU-OAuth
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.lib.nycu.edu.tw/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.lib.nycu.edu.tw/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://nycu.primo.exlibrisgroup.com/discovery/search?vid=886UST_NYCU:886UST_NYCU
- group: learn
  title: ''
  type: CourseCatalog
  url: https://timetable.nycu.edu.tw/
- group: other
  title: ''
  type: AIPolicy
  url: https://oaeri.nycu.edu.tw/oaeri/ch/app/data/view?module=nycu0014&id=2074&serno=9fd4480f-1c5e-4b0d-b9de-fe3719d46b25
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nycu/
- group: auth
  href: https://artifacts.apis.io/nycu/security/nycu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nycu-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/nycu/plans/nycu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nycu-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nycu/rate-limits/nycu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nycu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nycu/finops/nycu-finops.yml
  title: ''
  type: FinOps
  url: finops/nycu-finops.yml
- group: other
  href: https://artifacts.apis.io/nycu/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'National Yang Ming Chiao Tung University (NYCU) is a public research university in Hsinchu and Taipei, Taiwan, formed in 2021 from the merger of National Yang-Ming University and National Chiao Tung University. Its programmable footprint is small but genuinely its own in one place: the NYCU OAuth service at id.nycu.edu.tw, an OAuth 2.0 (RFC 6749) authorization server run by the university''s Information Technology Service Center that lets approved applications authenticate NYCU single sign-on users and read three consented identity attributes. It is documented publicly, in Chinese and English, with its own terms of service and issue tracker, and it is the only contract in this repo NYCU actually engineered. Everything else is a relationship rather than an interface the university wrote. NYCU self-hosts a Dataverse research-data repository and a DSpace institutional repository on its own network, and both expose an anonymous OAI-PMH 2.0 harvesting endpoint that is institution-operated
  — but the REST contracts underneath them belong to the Dataverse Project and DSpace, not to NYCU. Library discovery is an Ex Libris Primo tenancy. NYCU is a DataCite direct member in its own name, minting DOIs on prefix 10.57770 through its "NYCU Research Data Service" repository, and is registered in ROR. There is no central developer portal, no open-data portal, no course or timetable API, no OpenID Connect discovery document, and no publicly discoverable Shibboleth or SAML identity provider. The course registration and timetable systems are human web applications behind institutional login.'
examples:
- key_count: 3
  name: Nycu Oauth Profile Example
  slug: nycu-oauth-profile-example
- key_count: 3
  name: Nycu Oauth Token Example
  slug: nycu-oauth-token-example
finops:
- has_sources: true
  method: generated
  name: Nycu Finops
  primary_unit: ''
  service_category: Education
  slug: nycu-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nycu.png
json_schemas:
- name: NYCU OAuth Profile
  property_count: 2
  slug: nycu-oauth-profile
- name: NYCU OAuth Token Response
  property_count: 5
  slug: nycu-oauth-token
layout: provider
modified: '2026-09-16'
name: National Yang Ming Chiao Tung University
nav: Providers
network: true
overview: 'National Yang Ming Chiao Tung University publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Profile API, O Auth API, and 7 more. Tagged areas include Education, Higher Education, University, Taiwan, and Identity.


  The National Yang Ming Chiao Tung University catalog on APIs.io includes 1 Spectral governance ruleset.


  National Yang Ming Chiao Tung University''s developer surface includes documentation, API reference, support, and 16 more developer resources.'
plans:
- name: Nycu Plans Pricing
  plan_count: 2
  slug: nycu-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Nycu Rate Limits
  slug: nycu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 7
  extends: []
  name: National Yang Ming Chiao Tung University API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: nycu-rules
scopes:
- name: Nycu Scopes
  scope_count: 3
  slug: nycu-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 7.6
    contract_quality: 19.1
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 28.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nycu/nycu-2026-06-20T190547.png
security:
- kind: authentication
  name: Nycu Authentication
  slug: nycu-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Nycu Domain Security
  slug: nycu-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nycu
tags:
- Education
- Higher Education
- University
- Taiwan
- Identity
- OAuth
- Authentication
- SSO
- Research Data
- Institutional Repository
- Library
- Metadata
- OAI-PMH
- Identity Federation
website: https://www.nycu.edu.tw/nycu/ch/index
---
