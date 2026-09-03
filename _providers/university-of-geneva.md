---
access_model:
  confidence: high
  label: Free · affiliation-gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probed
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 148
  human_in_the_loop: 0
  name: University Of Geneva Agentic Access
  operation_count: 337
  slug: university-of-geneva-agentic-access
  summary_line: 337 operations · 148 acting
api_count: 1
apis:
- description: The University of Geneva's own SAML 2.0 Shibboleth Identity Provider, published as machine-readable metadata in SWITCHaai, the Swiss national research and education identity federation. entityID https
  name: UNIGE Shibboleth Identity Provider (SWITCHaai)
  slug: switchaai-idp
- description: OAI-PMH 2.0 metadata-harvesting interface for the Archive ouverte UNIGE institutional repository, exposing the University's scientific publications in Dublin Core and two UNIGE-specific schemas. Anony
  name: Archive ouverte UNIGE OAI-PMH
  slug: archive-ouverte-oai
- baseURL: https://access.yareta.unige.ch
  baseurl_source: declared
  description: 'The access/accession module of Yareta, the University of Geneva e-Research long-term research-data preservation platform: discover, order and download archives (AIP/DIP). Runs on UNIGE''s own host acce'
  name: Yareta Access API
  slug: university-of-geneva-access-api
- baseURL: https://ingest.yareta.unige.ch
  baseurl_source: declared
  description: 'The pre-ingest/ingest module of Yareta: deposit, validate and submit research data, reserve a DOI, and submit a SIP for archiving. Runs on UNIGE''s own host ingest.yareta.unige.ch. Fully bearer-gated —'
  name: Yareta Ingest API
  slug: university-of-geneva-ingest-api
- baseURL: https://access.yareta.unige.ch
  baseurl_source: declared
  description: The OAI-PMH provider-information surface of the Yareta access module — sets, metadata formats and provider configuration for harvesting UNIGE research-data descriptions. Distinct from the Archive ouve
  name: Yareta OAI-PMH Provider API
  slug: university-of-geneva-oai-pmh-api
- description: A self-hosted GitLab instance operated by the University on its own domain, serving an anonymous GitLab REST API v4 over its public projects. GET /api/v4/projects returned 200 with X-Total 1146 on 202
  name: UNIGE GitLab REST API
  slug: gitlab
- description: A UNIGE-developed prediction service for protein N-terminal modifications (initial methionine cleavage and N-terminal acetylation) across taxonomic groups. Accepts protein sequences by HTTP POST in FA
  name: Terminus Protein Prediction API
  slug: terminus
- description: The University of Geneva's library discovery and management tenancy. Its catalog runs on Ex Libris Primo and Alma operated by SLSP (Swiss Library Service Platform), the national academic library conso
  name: swisscovery UNIGE (SLSP / Ex Libris)
  slug: swisscovery-slsp
- description: 'UNIGE is a registered DataCite repository operator through the Swiss consortium (DataCite provider "opkb"). Two repository accounts and two DOI prefixes are delegated to it: ethz.genfyareta ("Uni Genf'
  name: DataCite Repository Membership
  slug: datacite-membership
- description: The University of Geneva is a Crossref member, id 13327, primary-name "Universite de Geneve". Recorded as a registry relationship. Crossref's API is Crossref's and is not saved here. Verified live 202
  name: Crossref Membership
  slug: crossref-membership
- description: 'ROR identifier https://ror.org/01swzsf04 for the University of Geneva. Notable because the institution''s own live service declares it: the public Yareta configuration endpoint reports dlcm.repository.'
  name: ROR Organization Identifier
  slug: ror-registration
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yareta Research Data Access API
  slug: open-university-of-geneva-access-api
- collection_type: open
  name: Yareta Research Data Access Ingest API
  slug: open-university-of-geneva-ingest-api
- collection_type: open
  name: Yareta Research Data Access OAI-PMH API
  slug: open-university-of-geneva-oai-pmh-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.unige.ch/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.unige.ch/eresearch/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.unige.ch/eresearch/en/services/yareta/
- group: other
  title: ''
  type: ResearchRepository
  url: https://archive-ouverte.unige.ch/
- group: other
  title: ''
  type: ResearchRepository
  url: https://yareta.unige.ch/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://unige.swisscovery.slsp.ch/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://pgc.unige.ch/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.aai.switch.ch/metadata.switchaai.xml
- group: build
  title: ''
  type: AITooling
  url: https://www.unige.ch/ia/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dis-unige
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.unige.ch/
- group: operate
  title: ''
  type: Support
  url: https://www.unige.ch/help
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-geneva/
- group: company
  title: ''
  type: Blog
  url: https://www.unige.ch/feed/rss
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-geneva-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-geneva-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-geneva-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-geneva-lifecycle.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/university-of-geneva-jsonschema-spectral-rules.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-geneva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-geneva-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-geneva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-geneva-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-geneva-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Geneva (Université de Genève, UNIGE) is a public research university in Geneva, Switzerland, founded in 1559 and ranked #93 in the QS World University Rankings 2025. Like almost every university it is a federation of buyers rather than an API producer, and it operates no central developer portal, no API gateway, no public key issuance and no self-service onboarding of any kind. What it does operate is unusually real for this cohort, and all of it sits under unige.ch: the Archive ouverte UNIGE institutional repository runs on the University''s OWN software (the Identify response reports "AoU v2.3.5", not DSpace, EPrints or Figshare) and serves a live OAI-PMH 2.0 endpoint anonymously; Yareta, the e-Research long-term research-data preservation platform built on the Swiss DLCM/Solidify stack that UNIGE itself leads, exposes access and ingest REST modules on its own hosts with one genuinely public configuration endpoint and everything else behind a bearer token;
  a self-hosted GitLab serves an anonymous REST API over 1,146 public projects; and the Terminus protein-prediction service offers a small anonymous research API. UNIGE''s strongest machine-readable surface is one universities are rarely credited for: its own Shibboleth SAML 2.0 Identity Provider, registered in the SWITCHaai national federation alongside 122 other unige.ch entities. Its library is a tenancy, not an asset — Ex Libris Alma/Primo operated by the SLSP consortium — and its DOI, publication and organization identifiers are registry memberships at DataCite, Crossref and ROR. There is no open-data portal, no course-catalog API (pgc.unige.ch soft-404s every /api path back to its own HTML) and no teaching-and-learning interoperability surface.'
examples:
- key_count: 7
  name: University Of Geneva Aip Response Example
  slug: university-of-geneva-aip-response-example
- key_count: 5
  name: University Of Geneva Order Create Request Example
  slug: university-of-geneva-order-create-request-example
- key_count: 8
  name: University Of Geneva Order Response Example
  slug: university-of-geneva-order-response-example
- key_count: 5
  name: University Of Geneva Orgunit Response Example
  slug: university-of-geneva-orgunit-response-example
finops:
- name: University Of Geneva Finops
  service_category: Education
  slug: university-of-geneva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-geneva.png
json_schemas:
- name: Yareta Archival Information Package (AIP)
  property_count: 33
  slug: university-of-geneva-aip
- name: Yareta Dissemination Information Package (DIP)
  property_count: 8
  slug: university-of-geneva-dip
- name: Yareta Order
  property_count: 19
  slug: university-of-geneva-order
- name: Yareta Organizational Unit
  property_count: 10
  slug: university-of-geneva-orgunit
json_structures:
- name: University Of Geneva Aip Structure
  property_count: 33
  slug: university-of-geneva-aip-structure
- name: University Of Geneva Order Structure
  property_count: 19
  slug: university-of-geneva-order-structure
- name: University Of Geneva Orgunit Structure
  property_count: 10
  slug: university-of-geneva-orgunit-structure
jsonld:
- class_count: 30
  name: University Of Geneva Context
  property_count: 5
  slug: university-of-geneva-context
layout: provider
modified: '2026-09-01'
name: University of Geneva
nav: Providers
network: true
overview: 'University of Geneva publishes 3 APIs on the [APIs.io](https://apis.io/) network: Yareta Access API, Yareta Ingest API, and Yareta OAI-PMH Provider API. Tagged areas include Education, Higher Education, University, Public Research University, and Open Science.


  The University of Geneva catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Geneva''s developer surface includes documentation, GitHub presence, support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: University Of Geneva Plans Pricing
  plan_count: 2
  slug: university-of-geneva-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Geneva Rate Limits
  slug: university-of-geneva-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: University of Geneva API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: university-of-geneva-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of Geneva API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 4
  slug: university-of-geneva-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 37.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 42.9
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-geneva/refs/heads/main/screenshots/university-of-geneva-2026-06-20T200151.png
security:
- kind: authentication
  name: University Of Geneva Authentication
  slug: university-of-geneva-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Geneva Domain Security
  slug: university-of-geneva-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-geneva
tags:
- Education
- Higher Education
- University
- Public Research University
- Open Science
- Research Data
- Institutional Repository
- Research Repository
- Identity Federation
- OAI-PMH
- Switzerland
- Europe
website: https://www.unige.ch/
---
