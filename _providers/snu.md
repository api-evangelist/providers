---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: SNU's federated identity provider, entityID https://kafegw.snu.ac.kr/idp/simplesamlphp, registered by the Korea Access Federation (registrationAuthority http://kafe.kreonet.net, registrationInstant 20
  name: Seoul National University SAML 2.0 Identity Provider
  slug: kafe-saml-idp
- description: Seoul National University Library runs library management and discovery on Ex Libris Alma and Primo, institution code 82SNU / 82SNU_INST, on the institution-specific host snu-primo.hosted.exlibrisgrou
  name: SNU Library Discovery (Ex Libris Primo / Alma) — tenancy
  slug: library-discovery-primo
- baseURL: https://s-space.snu.ac.kr/oai/request
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting 2.0 verbs.
  name: Seoul National University OAI PMH API
  slug: snu-oai-pmh-api
- baseURL: https://kafegw.snu.ac.kr/saml/module.php/saml/idp/singleSignOnService
  baseurl_source: declared
  description: OpenSearch 1.1 description and query endpoints.
  name: Seoul National University Open Search API
  slug: snu-open-search-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://en.snu.ac.kr/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.snu.ac.kr/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/seoulnational-university
- group: operate
  title: ''
  type: Support
  url: https://ist.snu.ac.kr/
- group: other
  title: ''
  type: ResearchRepository
  url: https://s-space.snu.ac.kr/
- group: other
  title: ''
  type: ResearchRepository
  url: https://kossda.snu.ac.kr/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.snu.ac.kr/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://sugang.snu.ac.kr/
- group: other
  title: ''
  type: IdentityFederation
  url: https://kafegw.snu.ac.kr/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.snu.ac.kr/about/downloads?md=v&bbsidx=166508
- group: build
  title: ''
  type: AITooling
  url: https://www.snu.ac.kr/snunow/press?md=v&bbsidx=170942
- group: auth
  href: https://artifacts.apis.io/snu/authentication/snu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snu-authentication.yml
- group: design
  href: https://artifacts.apis.io/snu/conformance/snu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snu-conformance.yml
- group: design
  href: https://artifacts.apis.io/snu/lifecycle/snu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snu-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/snu/scopes/snu-scopes.yml
  title: ''
  type: Scopes
  url: scopes/snu-scopes.yml
- group: design
  href: https://artifacts.apis.io/snu/errors/snu-errors.yml
  title: ''
  type: Errors
  url: errors/snu-errors.yml
- group: design
  href: https://artifacts.apis.io/snu/vocabulary/snu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/snu/json-ld/snu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snu-context.jsonld
- group: design
  href: https://artifacts.apis.io/snu/rules/snu-rules.yml
  title: ''
  type: Rules
  url: rules/snu-rules.yml
- group: auth
  href: https://artifacts.apis.io/snu/security/snu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snu-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/snu/plans/snu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snu-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/snu/rate-limits/snu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/snu/finops/snu-finops.yml
  title: ''
  type: FinOps
  url: finops/snu-finops.yml
- group: other
  href: https://artifacts.apis.io/snu/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Seoul National University (SNU) is South Korea''s flagship national research university, a national university corporation in Seoul ranked in the QS World top 40 and identified by ROR as https://ror.org/04h9pn542. Like most universities it is a federation of buyers rather than a producer of APIs: it operates no developer portal, no open-data portal, no API gateway, no official GitHub organization, and no OAuth or OIDC authorization server. It publishes no API documentation of any kind, and every contract in this repository was written from live probing rather than from something SNU wrote. What it does operate — verified on its own hosts and its own address block on 2026-08-19 — is four machine-readable surfaces. Two OAI-PMH 2.0 data providers: S-Space, the SNU Open Repository and Archive (DSpace 5.5, content from 2008, twelve metadata formats, 100+ sets, three harvesting contexts including OpenAIRE and DRIVER), and KOSSDA, the Korea Social Science Data Archive (DSpace 5.6,
  content from 2017). An OpenSearch 1.1 search interface over S-Space. And a SAML 2.0 Identity Provider, entityID https://kafegw.snu.ac.kr/idp/simplesamlphp, registered in the KAFE national federation and exported into eduGAIN with REFEDS Research & Scholarship support and a Sirtfi assurance assertion — the single most consequential programmable surface the institution runs, and one no catalog had recorded. Two honest limits belong in the same breath. The repository hosts front everything except OAI-PMH with a JavaScript bot challenge that returns HTTP 200 and an HTML shell to any machine client, so the OpenSearch interface is gated rather than open. And SNU''s library discovery runs on Ex Libris Alma and Primo under institution code 82SNU — real, but a tenancy, recorded below as such and never scored as SNU''s engineering.'
finops:
- has_sources: true
  method: generated
  name: Snu Finops
  primary_unit: ''
  service_category: Education
  slug: snu-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snu.png
json_schemas:
- name: SNU OAI-PMH Identify
  property_count: 9
  slug: snu-oai-identify
- name: SNU OAI-PMH Record (oai_dc)
  property_count: 2
  slug: snu-oai-record
jsonld:
- class_count: 20
  name: Snu Context
  property_count: 11
  slug: snu-context
layout: provider
modified: '2026-08-19'
name: Seoul National University
nav: Providers
network: true
overview: 'Seoul National University publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including OAI PMH API, Open Search API, and 2 more. Tagged areas include University, Higher Education, Education, South Korea, and Research.


  The Seoul National University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Seoul National University''s developer surface includes support, authentication, and 22 more developer resources.'
plans:
- name: Snu Plans Pricing
  plan_count: 2
  slug: snu-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Snu Rate Limits
  slug: snu-rate-limits
rules:
- authorship: derived
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Seoul National University API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: snu-rules
scopes:
- name: Snu Scopes
  scope_count: 0
  slug: snu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 15.8
    contract_governance: 33.3
    contract_quality: 62.2
    developer_ergonomics: 16.7
    discoverability: 71.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 34.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/snu/snu-2026-06-20T194118.png
security:
- kind: authentication
  name: Snu Authentication
  slug: snu-authentication
  summary_line: none/saml2 · 3 schemes
- kind: domain-security
  name: Snu Domain Security
  slug: snu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snu
tags:
- University
- Higher Education
- Education
- South Korea
- Research
- Research Data
- Institutional Repository
- Research Repository
- Identity Federation
- OAI-PMH
- SAML
- Open Access
- Library
- National University
website: https://en.snu.ac.kr/
---
