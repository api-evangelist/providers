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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wageningen University Research Agentic Access
  operation_count: 55
  slug: wageningen-university-research-agentic-access
  summary_line: 55 operations
api_count: 3
apis:
- description: API for scientific data about food products, published by Wageningen Food & Biobased Research (WFBR) through WUR's own Azure API Management instance. Provides software services and algorithms returnin
  name: WFBR Food API
  slug: wfbr-food-api
- baseURL: https://library.wur.nl
  baseurl_source: declared
  description: 'Open, keyless OAI-PMH 2.0 harvesting interface over the WUR Publications repository — all six verbs verified live, four metadata formats (oai_dc, mods, nl_didl, oai_openaire) and eight sets including '
  name: WUR Library OAI-PMH API
  slug: wageningen-university-research-library-oai-pmh
- baseURL: https://agrodatacube.wur.nl/api/v2/rest
  baseurl_source: declared
  description: The Altitude API from AgroDataCube v2, operated by Wageningen Environmental Research — 1 operation for altitude zonal statistics.
  name: Wageningen University & Research Altitude API
  slug: wageningen-university-research-altitude-api
- baseURL: https://agrodatacube.wur.nl/api/v2/rest
  baseurl_source: declared
  description: The KPI API from AgroDataCube v2, operated by Wageningen Environmental Research — 2 operations for crop-rotation and greenness indicators.
  name: Wageningen University & Research KPI API
  slug: wageningen-university-research-kpi-api
- baseURL: https://agrodatacube.wur.nl/api/v2/rest
  baseurl_source: declared
  description: The Raster API from AgroDataCube v2, operated by Wageningen Environmental Research — 4 operations returning GeoTIFF altitude and NDVI imagery.
  name: Wageningen University & Research Raster API
  slug: wageningen-university-research-raster-api
- baseURL: https://agrodatacube.wur.nl/api/v2/rest
  baseurl_source: declared
  description: The Retrieve API from AgroDataCube v2, operated by Wageningen Environmental Research — 18 operations over fields, crops, soils, meteo data and code lists.
  name: Wageningen University & Research Retrieve API
  slug: wageningen-university-research-retrieve-api
- baseURL: https://agrodatacube.wur.nl/api/v2/rest
  baseurl_source: declared
  description: The Return API from AgroDataCube v2, operated by Wageningen Environmental Research — 9 operations returning meteo stations, regions, soil types and source information.
  name: Wageningen University & Research Return API
  slug: wageningen-university-research-return-api
- description: 'Institutional research portal and CRIS for WUR publications, projects, datasets and researcher profiles, running on Elsevier Pure. Listed as a tenant surface because it is a genuine WUR institutional '
  name: WUR Research Portal (Elsevier Pure tenancy)
  slug: wageningen-research-portal-pure
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AgroDataCube API v2 Altitude API
  slug: open-wageningen-university-research-altitude-api
- collection_type: open
  name: AgroDataCube API v2 KPI API
  slug: open-wageningen-university-research-kpi-api
- collection_type: open
  name: AgroDataCube API v2 Raster API
  slug: open-wageningen-university-research-raster-api
- collection_type: open
  name: AgroDataCube API v2 Retrieve API
  slug: open-wageningen-university-research-retrieve-api
- collection_type: open
  name: AgroDataCube API v2 Return API
  slug: open-wageningen-university-research-return-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.wur.nl/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://euw-apim-fism-001-p.developer.azure-api.net/
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/3284162/TVeqd7aa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://euw-apim-fism-001-p.developer.azure-api.net/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wur.nl/en/about-wur/organisation-profile/privacy-cookie-statement-wur
- group: other
  title: ''
  type: OpenData
  url: https://opengeodata.wmr.wur.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.wur.nl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.wur.nl/en/library
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.surfconext.nl/idps-metadata.xml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/WUR-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/wageningen-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/wageningen-university-research-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wageningen-university-research-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wageningen-university-research-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wageningen-university-research-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wageningen-university-research-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wageningen-university-research-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wageningen-university-research-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wageningen-university-research-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Wageningen University & Research (WUR) is the Dutch public research university and research foundation for healthy food and the living environment, in Wageningen, Netherlands, and ranked #100 in the QS World University Rankings 2025. Its programmable footprint is real but small, and it sits in the research institutes rather than in a central developer platform: AgroDataCube, run by Wageningen Environmental Research at agrodatacube.wur.nl, is a token-gated REST API over an open agri-food data collection for the Netherlands; the WFBR API Portal, run by Wageningen Food & Biobased Research on its own Azure API Management instance, publishes a Food API behind registration and WUR''s own terms of use; the university library operates a complete, keyless OAI-PMH 2.0 endpoint at library.wur.nl/oai over "Wageningen University & Research Publications", serving Dublin Core, MODS, DIDL and OpenAIRE/DataCite metadata; and Wageningen Marine Research runs an OGC WMS/WFS GeoServer at opengeodata.wmr.wur.nl.
  WUR also operates two SAML identity providers registered in SURFconext and therefore eduGAIN. What WUR does not have is a central API programme: there is no institution-wide developer portal, no course-catalog or registrar API (api.wur.nl and ssc.wur.nl resolve but time out from the public internet), and no published OpenAPI of its own — every OpenAPI in this repository is ours, derived from WUR''s Postman collections and from live probes. The Research Portal at research.wur.nl is an Elsevier Pure tenancy: WUR''s data and DOIs, Elsevier''s contract, and it is recorded here as a tenant relationship rather than credited to WUR as engineering.'
examples:
- key_count: 2
  name: Wageningen University Research Cropcodes Example
  slug: wageningen-university-research-cropcodes-example
- key_count: 2
  name: Wageningen University Research Fields Example
  slug: wageningen-university-research-fields-example
finops:
- name: Wageningen University Research Finops
  service_category: Education
  slug: wageningen-university-research-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wageningen-university-research.png
json_schemas:
- name: AgroDataCube Field FeatureCollection
  property_count: 2
  slug: wageningen-university-research-field
json_structures:
- name: Wageningen University Research Field Structure
  property_count: 7
  slug: wageningen-university-research-field-structure
jsonld:
- class_count: 15
  name: Wageningen University Research Context
  property_count: 2
  slug: wageningen-university-research-context
layout: provider
modified: '2026-08-30'
name: Wageningen University & Research
nav: Providers
network: true
overview: 'Wageningen University & Research publishes 6 APIs on the [APIs.io](https://apis.io/) network, including WUR Library OAI-PMH API, Altitude API, KPI API, and 3 more. Tagged areas include Education, Higher Education, University, Research, and Research Data.


  The Wageningen University & Research catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wageningen University & Research''s developer surface includes API reference, GitHub presence, authentication, and 17 more developer resources.'
plans:
- name: Wageningen University Research Plans Pricing
  plan_count: 2
  slug: wageningen-university-research-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Wageningen University Research Rate Limits
  slug: wageningen-university-research-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wageningen University & Research API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wageningen-university-research-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Wageningen University & Research API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: wageningen-university-research-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 28.0
    contract_quality: 26.0
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 28.0
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wageningen-university-research/refs/heads/main/screenshots/wageningen-university-research-2026-06-20T201159.png
security:
- kind: authentication
  name: Wageningen University Research Authentication
  slug: wageningen-university-research-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wageningen University Research Domain Security
  slug: wageningen-university-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wageningen University Research Vulnerability Disclosure
  slug: wageningen-university-research-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wageningen-university-research
tags:
- Education
- Higher Education
- University
- Research
- Research Data
- Agriculture
- Agrifood
- Geospatial
- Library
- Open Data
- Identity Federation
- Netherlands
website: https://www.wur.nl/
---
