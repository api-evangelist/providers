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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uppsala Agentic Access
  operation_count: 7
  slug: uppsala-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: The Norse World REST-API, part of the Norse World research infrastructure at Uppsala University's Department of Scandinavian Languages, provides access to attestation and location records of foreign p
  name: Norse World REST-API
  slug: norseworld
- description: DiVA (Academic Archive On-line) is Uppsala University Library's institutional repository for publications and research data produced by the university's researchers and students. It exposes an OAI-PMH
  name: DiVA OAI-PMH
  slug: diva-oai
- description: Uppsala University runs its own Shibboleth Identity Provider and publishes its SAML 2.0 federation metadata as a machine-readable EntityDescriptor. It is registered in SWAMID, the Swedish identity fed
  name: Uppsala University SAML 2.0 Identity Provider Metadata
  slug: idp-saml
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The BattleDeaths API from Uppsala University — 1 operation(s) for battledeaths.
  name: Uppsala University BattleDeaths API
  slug: uppsala-battledeaths-api
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The Dyadic API from Uppsala University — 1 operation(s) for dyadic.
  name: Uppsala University Dyadic API
  slug: uppsala-dyadic-api
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The GEDEvents API from Uppsala University — 1 operation(s) for gedevents.
  name: Uppsala University GEDEvents API
  slug: uppsala-gedevents-api
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The NonState API from Uppsala University — 1 operation(s) for nonstate.
  name: Uppsala University NonState API
  slug: uppsala-nonstate-api
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The OneSided API from Uppsala University — 1 operation(s) for onesided.
  name: Uppsala University OneSided API
  slug: uppsala-onesided-api
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The OrganizedViolenceCY API from Uppsala University — 1 operation(s) for organizedviolencecy.
  name: Uppsala University OrganizedViolenceCY API
  slug: uppsala-organizedviolencecy-api
- baseURL: https://ucdpapi.pcr.uu.se/api/
  baseurl_source: declared
  description: The UcdpPrioConflict API from Uppsala University — 1 operation(s) for ucdpprioconflict.
  name: Uppsala University UcdpPrioConflict API
  slug: uppsala-ucdpprioconflict-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UCDP - The Public BattleDeaths API
  slug: open-uppsala-battledeaths-api
- collection_type: open
  name: UCDP - The Public BattleDeaths Dyadic API
  slug: open-uppsala-dyadic-api
- collection_type: open
  name: UCDP - The Public BattleDeaths GEDEvents API
  slug: open-uppsala-gedevents-api
- collection_type: open
  name: UCDP - The Public BattleDeaths NonState API
  slug: open-uppsala-nonstate-api
- collection_type: open
  name: UCDP - The Public BattleDeaths OneSided API
  slug: open-uppsala-onesided-api
- collection_type: open
  name: UCDP - The Public BattleDeaths OrganizedViolenceCY API
  slug: open-uppsala-organizedviolencecy-api
- collection_type: open
  name: UCDP - The Public BattleDeaths UcdpPrioConflict API
  slug: open-uppsala-ucdpprioconflict-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.uu.se/
- group: docs
  title: ''
  type: Documentation
  url: https://ucdp.uu.se/apidocs/
- group: docs
  title: ''
  type: APIReference
  url: https://ucdp.uu.se/apidocs/
- group: other
  title: ''
  type: ResearchRepository
  url: https://uu.diva-portal.org/
- group: other
  title: ''
  type: IdentityFederation
  url: https://weblogin.uu.se/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.uppmax.uu.se/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.uu.se/en/study/course
- group: build
  title: ''
  type: AITooling
  url: https://www.uu.se/en/staff/service-and-tools/ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uu.se/en/about-uu/data-protection-policy
- group: operate
  title: ''
  type: Support
  url: https://www.uu.se/en/contact-and-organisation
- group: company
  title: ''
  type: Blog
  url: https://www.uu.se/en/news
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uppsala-university
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UppsalaConflictDataProgram
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uppsala-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/uppsala-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uppsala-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uppsala-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uppsala-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uppsala-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uppsala-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uppsala-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uppsala-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Uppsala University (Uppsala universitet) is Sweden''s oldest university, founded in 1477, and a public research university ranked #103 in the QS World University Rankings 2025. It operates no central developer portal and no institution-wide open-data portal — data.uu.se, opendata.uu.se and api.uu.se do not resolve — so its programmable footprint is decentralized, sitting inside individual research infrastructures, the university library, and IT services. Four surfaces were verified live as institution-operated: the Uppsala Conflict Data Program (UCDP) REST API at ucdpapi.pcr.uu.se, which is the university''s most substantial public API and requires a free token; the Norse World REST-API at norseworld.nordiska.uu.se, returning JSON, GeoJSON and JSON-LD; the DiVA OAI-PMH endpoint at uu.diva-portal.org, notable because Uppsala University Library builds and hosts the DiVA platform for the whole Swedish DiVA consortium rather than renting it from a vendor; and the university''s
  SWAMID-registered Shibboleth SAML 2.0 identity provider at weblogin.uu.se, which publishes machine-readable federation metadata. No Figshare, Elsevier Pure, Ex Libris or Dataverse contract is attributed to Uppsala in this profile.'
examples:
- key_count: 7
  name: Uppsala Gedevents Example
  slug: uppsala-gedevents-example
- key_count: 7
  name: Uppsala Ucdpprioconflict Example
  slug: uppsala-ucdpprioconflict-example
finops:
- name: Uppsala Finops
  service_category: Education
  slug: uppsala-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uppsala.png
json_schemas:
- name: UcdpApiResponse
  property_count: 5
  slug: uppsala-apiresponse
- name: GedDb
  property_count: 49
  slug: uppsala-gedevent
- name: OrganizedViolenceCYDb
  property_count: 74
  slug: uppsala-organizedviolencecy
- name: UcdpPrioConflictDb
  property_count: 28
  slug: uppsala-ucdpprioconflict
json_structures:
- name: Uppsala Gedevent Structure
  property_count: 49
  slug: uppsala-gedevent-structure
- name: Uppsala Ucdpprioconflict Structure
  property_count: 28
  slug: uppsala-ucdpprioconflict-structure
jsonld:
- class_count: 31
  name: Uppsala Context
  property_count: 3
  slug: uppsala-context
layout: provider
modified: '2026-08-30'
name: Uppsala University
nav: Providers
network: true
overview: 'Uppsala University publishes 7 APIs on the [APIs.io](https://apis.io/) network, including BattleDeaths API, Dyadic API, GEDEvents API, and 4 more. Tagged areas include University, Higher Education, Education, Sweden, and Public Research University.


  The Uppsala University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Uppsala University''s developer surface includes documentation, API reference, support, engineering blog, GitHub presence, authentication, and 17 more developer resources.'
plans:
- name: Uppsala Plans Pricing
  plan_count: 3
  slug: uppsala-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Uppsala Rate Limits
  slug: uppsala-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Uppsala University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uppsala-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Uppsala University API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: uppsala-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 31.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 56.9
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 35.6
    operational_transparency: 34.2
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uppsala/refs/heads/main/screenshots/uppsala-2026-06-20T200453.png
security:
- kind: authentication
  name: Uppsala Authentication
  slug: uppsala-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uppsala Domain Security
  slug: uppsala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uppsala Vulnerability Disclosure
  slug: uppsala-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: uppsala
tags:
- University
- Higher Education
- Education
- Sweden
- Public Research University
- Research Data
- Institutional Repository
- Identity Federation
- Research Computing
- Conflict Data
- Open Access
website: https://www.uu.se/
---
