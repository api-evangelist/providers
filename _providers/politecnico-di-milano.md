---
access_model:
  confidence: high
  label: Free · open, unauthenticated
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: The university's own open data portal. It is not CKAN, Socrata or a data.json endpoint — all three 404 — but a DCAT-AP_IT catalogue serialised as RDF Turtle at /opendata_polimi.ttl, declaring 25 datas
  name: Politecnico di Milano Open Data
  slug: open-data
- description: OAI-PMH 2.0 harvesting endpoint for IRIS Re.Public@Polimi, the institutional research product catalogue. Live Identify returns repositoryName "IRIS - POLIMI - prod", earliest datestamp 2015-06-10, del
  name: Re.Public@Polimi OAI-PMH
  slug: iris-oai-pmh
- description: A second, separate OAI-PMH 2.0 endpoint — the POLITESI archive of Politecnico di Milano theses and dissertations, handle prefix 10589, earliest datestamp 2010-08-24. It offers a wider metadata set tha
  name: POLITESI OAI-PMH
  slug: politesi-oai-pmh
- description: The university's own Shibboleth identity provider, publishing its SAML 2.0 EntityDescriptor at https://shibidp.polimi.it/idp/shibboleth over unauthenticated HTTPS. The IDPSSODescriptor advertises Shib
  name: Politecnico di Milano Shibboleth Identity Provider
  slug: shibboleth-idp
- description: 'Politecnico di Milano''s membership of IDEM, the Italian academic identity federation run by GARR. The federation aggregate at md.idem.garr.it carries the university''s own IdP entity plus three of its '
  name: IDEM GARR Identity Federation membership
  slug: idem-garr-federation
- description: 'The institution''s entry in the Research Organization Registry, ROR ID 01nffqt88, carrying its canonical name in Italian, English and French and its own domain. ROR''s API is a registry the institution '
  name: ROR registration
  slug: ror-registration
- description: Politecnico di Milano's tenancy of CINECA's IRIS research information platform. The data is the university's; the contract is the vendor's, and it is not saved in this repository. Recorded here becaus
  name: IRIS REST API (CINECA platform tenancy)
  slug: iris-rest
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://www.polimi.it/en/
- group: company
  title: ''
  type: About
  url: https://www.polimi.it/en/the-politecnico
- group: company
  title: ''
  type: Blog
  url: https://www.polimi.it/en/the-politecnico/news
- group: operate
  title: ''
  type: Support
  url: https://www.polimi.it/en/the-politecnico/contacts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polimi.it/en/the-politecnico/communication/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/polimi/
- group: other
  title: ''
  type: OpenData
  url: https://www.opendata.polimi.it/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.opendata.polimi.it/dataset/course_catalog/
- group: other
  title: ''
  type: ResearchRepository
  url: https://re.public.polimi.it/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.politesi.polimi.it/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibidp.polimi.it/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://www.normativa.polimi.it/fileadmin/user_upload/regolamenti/privacy_e_sicurezza/LG_IA_PTA_v1.0def.pdf
- group: other
  title: ''
  type: AIPolicy
  url: https://www.normativa.polimi.it/privacy-e-sicurezza
- group: auth
  title: ''
  type: Authentication
  url: authentication/politecnico-di-milano-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/politecnico-di-milano-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/politecnico-di-milano-opendata-vocabulary.yml
- group: design
  title: ''
  type: Errors
  url: errors/politecnico-di-milano-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/politecnico-di-milano-lifecycle.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/politecnico-di-milano-scopes.yml
- group: design
  title: ''
  type: Rules
  url: rules/politecnico-di-milano-spectral-ruleset.yml
- group: build
  title: ''
  type: Examples
  url: examples/politecnico-di-milano-examples.yml
- group: other
  title: ''
  type: Provenance
  url: provenance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/politecnico-di-milano-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/politecnico-di-milano-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/politecnico-di-milano-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/politecnico-di-milano-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Politecnico di Milano is Italy''s largest technical university — engineering, architecture and design — and a public research institution in Milan, ROR 01nffqt88. Like almost every university it is a federation of buyers rather than an API producer: there is no developer portal, no public API key, no status page and no changelog anywhere on polimi.it. What it does operate itself is real and was verified live on 2026-09-01. An open data portal at www.opendata.polimi.it publishes a DCAT-AP_IT catalogue in RDF Turtle describing 25 datasets, each with a CSV and a JSON distribution at a stable unauthenticated URL — all 25 returned 200 and 38,255 rows on probe, covering the course catalogue, enrolments, graduates, mobility, internships, grade distributions and research output under CC BY 4.0. Two separate OAI-PMH 2.0 endpoints are served from its own hosts: Re.Public@Polimi for research products and POLITESI for theses, the latter also harvestable in the DataCite kernel-4 metadata
  schema. It runs its own Shibboleth identity provider, shibidp.polimi.it, whose SAML 2.0 metadata is public and whose entityID is registered in the Italian IDEM GARR federation. Against that, the surfaces it does NOT own are recorded as such: the authenticated IRIS REST API on its repository host is CINECA''s product contract, not the university''s, and api.polimi.it is a live Kong gateway with no publicly routable endpoint behind it. This profile saves contracts only for the surfaces the institution itself operates.'
examples:
- key_count: 1
  name: Politecnico Di Milano Opendata Course Catalog
  slug: politecnico-di-milano-opendata-course-catalog
finops:
- name: Politecnico Di Milano Finops
  service_category: Education
  slug: politecnico-di-milano-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/politecnico-di-milano.png
json_schemas:
- name: Politecnico di Milano course catalog row
  property_count: 8
  slug: politecnico-di-milano-course-catalog
- name: Politecnico di Milano open data recordset
  property_count: 1
  slug: politecnico-di-milano-opendata-recordset
jsonld:
- class_count: 19
  name: Politecnico Di Milano Context
  property_count: 5
  slug: politecnico-di-milano-context
- class_count: 12
  name: Politecnico Di Milano Opendata Catalog Context
  property_count: 0
  slug: politecnico-di-milano-opendata-catalog
layout: provider
modified: '2026-09-01'
name: Politecnico di Milano
nav: Providers
network: true
overview: 'Politecnico di Milano publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data, Re.Public@Polimi OAI-PMH, POLITESI OAI-PMH, and 1 more. Tagged areas include Education, Higher Education, University, Technical University, and Research.


  The Politecnico di Milano catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Politecnico di Milano''s developer surface includes engineering blog, support, authentication, code examples, and 23 more developer resources.'
plans:
- name: Politecnico Di Milano Plans Pricing
  plan_count: 2
  slug: politecnico-di-milano-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Politecnico Di Milano Rate Limits
  slug: politecnico-di-milano-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Politecnico di Milano API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 3
  slug: politecnico-di-milano-spectral-ruleset
scopes:
- name: Politecnico Di Milano Scopes
  scope_count: 0
  slug: politecnico-di-milano-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 18.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 20.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 60.6
    contract_quality: 29.4
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 60.6
    operational_transparency: 21.1
  previous_composite: 22.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/politecnico-di-milano/refs/heads/main/screenshots/politecnico-di-milano-2026-06-20T191910.png
security:
- kind: authentication
  name: Politecnico Di Milano Authentication
  slug: politecnico-di-milano-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Politecnico Di Milano Domain Security
  slug: politecnico-di-milano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: politecnico-di-milano
tags:
- Education
- Higher Education
- University
- Technical University
- Research
- Open Data
- Research Repository
- Course Catalog
- Identity Federation
- OAI-PMH
- Shibboleth
- DCAT
- Italy
- Europe
website: https://www.polimi.it/en/
---
