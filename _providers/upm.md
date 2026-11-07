---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: UPM's own Shibboleth identity provider, publishing conforming SAML 2.0 and SAML 1.1 metadata at its entityID (HTTP 200, application/xml, verified 2026-09-01). Asserts the scope upm.edu.my, carries HTT
  name: UPM Shibboleth SAML 2.0 Identity Provider
  slug: saml-idp
- description: 'Universiti Putra Malaysia''s identity provider is registered in eduGAIN, the global identity interfederation, through SIFULAN — the Malaysian Access Federation — as eduGAIN entity 672307, registration '
  name: eduGAIN / SIFULAN federation membership
  slug: edugain-sifulan
- description: Universiti Putra Malaysia is a Crossref member in its own right, member id 27687, holding DOI prefix 10.47836 with 5,871 registered DOIs (3,105 current, 2,766 backfile) as of 2026-09-01. The prefix ca
  name: Crossref membership — DOI prefix 10.47836
  slug: crossref-member
- description: Universiti Putra Malaysia holds ROR identifier https://ror.org/02e91jd64, cross-walked in the ROR record to GRID grid.11142.37, ISNI 0000 0001 2231 800X, Wikidata Q1458579 and five Crossref Funder Reg
  name: ROR organization record
  slug: ror
- baseURL: http://psasir.upm.edu.my/cgi/oai2
  baseurl_source: declared
  description: Per-item export plugins.
  name: Universiti Putra Malaysia Export API
  slug: upm-export-api
- baseURL: http://psasir.upm.edu.my/cgi/oai2
  baseurl_source: declared
  description: OAI-PMH 2.0 harvesting verbs.
  name: Universiti Putra Malaysia OAI PMH API
  slug: upm-oai-pmh-api
- baseURL: http://psasir.upm.edu.my/cgi/oai2
  baseurl_source: declared
  description: EPrints REST dataset browser.
  name: Universiti Putra Malaysia REST API
  slug: upm-rest-api
- baseURL: http://psasir.upm.edu.my/cgi/oai2
  baseurl_source: declared
  description: Search with selectable output format.
  name: Universiti Putra Malaysia Search API
  slug: upm-search-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://upm.edu.my/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-putra-malaysia/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.upm.edu.my/
- group: other
  title: ''
  type: ResearchRepository
  url: http://psasir.upm.edu.my/
- group: other
  title: ''
  type: ResearchRepository
  url: http://myagric.upm.edu.my/
- group: other
  href: https://artifacts.apis.io/upm/identity-federation/upm-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/upm-identity-federation.yml
- group: auth
  href: https://artifacts.apis.io/upm/authentication/upm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upm-authentication.yml
- group: design
  href: https://artifacts.apis.io/upm/conformance/upm-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upm-education-standards-conformance.yml
- group: design
  href: https://artifacts.apis.io/upm/errors/upm-errors.yml
  title: ''
  type: Errors
  url: errors/upm-errors.yml
- group: build
  href: https://artifacts.apis.io/upm/examples/upm-examples.yml
  title: ''
  type: Examples
  url: examples/upm-examples.yml
- group: docs
  href: https://artifacts.apis.io/upm/json-schema/upm-eprints-record-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/upm-eprints-record-schema.json
- group: auth
  href: https://artifacts.apis.io/upm/security/upm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upm-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/upm/plans/upm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/upm-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/upm/rate-limits/upm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/upm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/upm/finops/upm-finops.yml
  title: ''
  type: FinOps
  url: finops/upm-finops.yml
- group: other
  href: https://artifacts.apis.io/upm/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Putra Malaysia (UPM) is a Malaysian public research university in Serdang, Selangor, founded as an agricultural college in 1931 and known as Universiti Pertanian Malaysia until 1997. UPM operates no developer portal, publishes no OpenAPI definition, issues no API keys and runs no self-service developer programme — and it does not need one to have a real programmable footprint. Four machine-readable surfaces were verified live on 2026-09-01, and all four are operated by the institution itself rather than by a vendor under its name. PSASIR, the institutional repository, runs EPrints 3.3.16 inside UPM''s own campus network allocation and answers a full OAI-PMH 2.0 harvest as well as an anonymous EPrints REST, export and OpenSearch interface offering twenty output representations. MyAgric, the Malaysian Agricultural Repository, is a second and distinct EPrints deployment UPM hosts on the same network, with its own repository identifier and its own OAI-PMH endpoint. UPM
  publishes conforming SAML 2.0 metadata for its own Shibboleth identity provider at idf.upm.edu.my, registered in eduGAIN through SIFULAN, the Malaysian Access Federation, since 2020. UPM is also a Crossref member in its own right, holding DOI prefix 10.47836 across roughly 5,900 registered DOIs for its Pertanika and UPM Press journals. What UPM does not have is any interface for its student, staff and administrative systems: the Putra portal, SMP and the study portal sit behind UPM-ID single sign-on with no public contract, there is no open-data portal, no course-catalog API, no institutional GitHub organisation, and no llms.txt, sitemap or security.txt on the main site.'
examples:
- key_count: 17
  name: Upm Psasir Eprint Export
  slug: upm-psasir-eprint-export
finops:
- has_sources: true
  method: generated
  name: Upm Finops
  primary_unit: ''
  service_category: Education
  slug: upm-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upm.png
json_schemas:
- name: UPM PSASIR EPrints record (JSON export)
  property_count: 18
  slug: upm-eprints-record
jsonld:
- class_count: 15
  name: Upm Context
  property_count: 1
  slug: upm-context
layout: provider
modified: '2026-09-01'
name: Universiti Putra Malaysia
nav: Providers
network: true
overview: 'Universiti Putra Malaysia publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Export API, OAI PMH API, REST API, and 5 more. Tagged areas include University, Higher Education, Education, Malaysia, and Public Research University.


  The Universiti Putra Malaysia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Universiti Putra Malaysia''s developer surface includes authentication, code examples, and 14 more developer resources.'
plans:
- name: Upm Plans Pricing
  plan_count: 2
  slug: upm-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Upm Rate Limits
  slug: upm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Universiti Putra Malaysia API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 1
  slug: upm-rules
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 24.0
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - malaysia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 19.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/upm/upm-2026-06-20T200449.png
security:
- kind: authentication
  name: Upm Authentication
  slug: upm-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Upm Domain Security
  slug: upm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upm
tags:
- University
- Higher Education
- Education
- Malaysia
- Public Research University
- Research Data
- Institutional Repository
- Open Access
- OAI-PMH
- Identity Federation
- Shibboleth
- Agriculture
- Scholarly Publishing
website: https://upm.edu.my/
---
