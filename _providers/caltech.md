---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
api_count: 4
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for CaltechDATA. Verified live 2026-08-19 via the Identify verb (repositoryName CaltechDATA, protocolVersion 2.0) and via ListMetadataFormats, which advertises
  name: CaltechDATA OAI-PMH
  slug: caltechdata-oai
- description: Caltech's institutional publications repository, also on self-hosted InvenioRDM. Exposes the same REST record API and an OAI-PMH 2.0 endpoint, carrying ORCID and ROR identifiers and Caltech-specific c
  name: CaltechAUTHORS REST API and OAI-PMH
  slug: caltechauthors
- description: A metadata service built and operated by Caltech Library (v1.6), harvesting its institutional repositories, public directory and archival systems into static JSON datasets published for data-science u
  name: Caltech Library Feeds
  slug: library-feeds
- description: The NASA/IPAC Infrared Science Archive exposes IVOA-standard Virtual Observatory interfaces — Table Access Protocol (TAP/ADQL), Simple Cone Search and Simple Image Access v2 — over NASA infrared and s
  name: IRSA Virtual Observatory APIs (Caltech/IPAC)
  slug: irsa-vo
- description: The NASA/IPAC Extragalactic Database, operated by Caltech/IPAC, exposes an IVOA TAP service over its extragalactic object catalog. Verified live 2026-08-19 returning TAP_SCHEMA rows as CSV, and return
  name: NED Table Access Protocol (Caltech/IPAC)
  slug: ned-tap
- description: The NASA Exoplanet Archive, operated by Caltech/IPAC, exposes an IVOA TAP service over its confirmed-planet and related tables. Verified live 2026-08-19 returning real planet names from the `ps` table
  name: NASA Exoplanet Archive TAP (Caltech/IPAC)
  slug: exoplanet-archive-tap
- description: 'Caltech operates its own Shibboleth identity provider at idp.caltech.edu, asserting scoped attributes for caltech.edu. The SAML 2.0 metadata is machine-readable and publicly retrievable both from the '
  name: Caltech Shibboleth Identity Provider (InCommon)
  slug: identity-federation
- description: 'Caltech Library''s discovery and research-guide layer runs on Springshare LibGuides/LibApps rather than on institution-operated software. Recorded as a real institutional relationship — one of the few '
  name: Caltech Library Guides (Springshare tenancy)
  slug: libguides-springshare
- description: Caltech Library's OpenURL link resolver is an EBSCO tenancy — instance `l7ubco` on the shared host resolver.ebsco.com — referenced from Caltech's own library pages. Recorded as a relationship only — n
  name: EBSCO Link Resolver (Caltech instance)
  slug: ebsco-resolver
- description: Time-series waveform retrieval (fdsnws-dataselect).
  name: California Institute of Technology Data Select API
  slug: caltech-dataselect-api
- description: Earthquake event catalog queries (fdsnws-event).
  name: California Institute of Technology Event API
  slug: caltech-event-api
- description: Published research data records, their metadata, files and DOIs.
  name: California Institute of Technology Records API
  slug: caltech-records-api
- description: Station and channel metadata queries (fdsnws-station).
  name: California Institute of Technology Station API
  slug: caltech-station-api
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://www.caltech.edu/
- group: company
  title: ''
  type: Blog
  url: https://www.caltech.edu/about/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.caltech.edu/about/news/rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caltech.edu/privacy-notice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/california-institute-of-technology/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caltechlibrary
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Caltech-IPAC
- group: other
  title: ''
  type: OpenData
  url: https://data.caltech.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://data.caltech.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://authors.library.caltech.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Fidp.caltech.edu%2Fidp%2Fshibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.caltech.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.caltech.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.imss.caltech.edu/services/ai
- group: operate
  title: ''
  type: Support
  url: https://library.caltech.edu/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/caltech-caltechdata-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/caltech-scedc-fdsn-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/caltech-caltechdata-record-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/caltech-library-feeds-person-schema.json
- group: design
  title: ''
  type: Conformance
  url: conformance/caltech-education-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caltech-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/caltech-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caltech-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/caltech-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/caltech-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/caltech-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caltech-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/caltech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caltech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/caltech-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The California Institute of Technology (Caltech) is a private research university in Pasadena, California, and one of the rare institutions in this cohort whose machine-readable footprint is genuinely its own rather than a vendor''s contract running under its name. Caltech operates no central developer portal — neither api.caltech.edu nor developer.caltech.edu resolves — and publishes no OpenAPI, no llms.txt, no .well-known catalog and no status page. What it does operate is real research infrastructure on its own domain, engineered by four independent units with no shared convention between them: Caltech Library runs CaltechDATA and CaltechAUTHORS on self-hosted InvenioRDM, with public REST APIs, OAI-PMH 2.0 endpoints and DataCite DOIs minted under Caltech''s own 10.22002 prefix; the Seismological Laboratory runs the Southern California Earthquake Data Center''s FDSN web services; Caltech/IPAC runs three NASA archives — IRSA, NED and the NASA Exoplanet Archive — behind IVOA
  Virtual Observatory interfaces; and IMSS runs a Shibboleth identity provider registered in the InCommon federation. Five of the twelve education-regime domain standards are evidenced directly inside live Caltech contracts: shibboleth, saml, oai-pmh, datacite and orcid. The library discovery layer is the one genuinely outsourced surface, a Springshare tenancy at libguides.caltech.edu. The honest summary is that Caltech ships excellent open research data and almost no API product management around it.'
examples:
- key_count: 9
  name: Caltech Caltechdata Record Example
  slug: caltech-caltechdata-record-example
finops:
- name: Caltech Finops
  service_category: Education
  slug: caltech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caltech.png
json_schemas:
- name: CaltechDATA Record
  property_count: 18
  slug: caltech-caltechdata-record
- name: Caltech Library Feeds — Person
  property_count: 5
  slug: caltech-library-feeds-person
jsonld:
- class_count: 17
  name: Caltech Context
  property_count: 6
  slug: caltech-context
layout: provider
modified: '2026-08-19'
name: California Institute of Technology
nav: Providers
network: true
overview: 'California Institute of Technology publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data Select API, Event API, Records API, and 1 more. Tagged areas include University, Higher Education, Education, Private Research University, and Institute of Technology.


  The California Institute of Technology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  California Institute of Technology''s developer surface includes engineering blog, support, authentication, and 28 more developer resources.'
plans:
- name: Caltech Plans Pricing
  plan_count: 2
  slug: caltech-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Caltech Rate Limits
  slug: caltech-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: California Institute of Technology API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: caltech-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 45.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 3.8
    contract_quality: 25.5
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 31.7
  provenance:
    conformance: first-party
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
    score: 38.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caltech/refs/heads/main/screenshots/caltech-2026-06-20T173852.png
security:
- kind: authentication
  name: Caltech Authentication
  slug: caltech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Caltech Domain Security
  slug: caltech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caltech
tags:
- University
- Higher Education
- Education
- Private Research University
- Institute of Technology
- United States
- California
- Research Data
- Open Data
- Research Repository
- Identity Federation
- Astronomy
- Seismology
- Research Computing
- OAI-PMH
website: https://www.caltech.edu/
---
