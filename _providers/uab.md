---
access_model:
  confidence: high
  label: Free · open harvesting endpoints, no registration; personal services gated by institutional SSO
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - examples
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'A second institution-operated OAI-PMH 2.0 endpoint, for Traces, UAB''s bibliographic database of Catalan language and literature. Identify returns repositoryName "Traces : base de dades de llengua i li'
  name: Traces — Base de Dades de Llengua i Literatura Catalanes (OAI-PMH 2.0)
  slug: traces-oai-pmh
- description: 'A third institution-operated OAI-PMH 2.0 endpoint, for the Inventory of Music Collections of Catalonia, a UAB-hosted national musical-heritage catalogue. Identify returns repositoryName "IFMuC: Invent'
  name: IFMuC — Inventari dels Fons Musicals de Catalunya (OAI-PMH 2.0)
  slug: ifmuc-oai-pmh
- description: 'UAB self-hosts the journal platform on which its scholarly journals are published, and each journal exposes its own OAI-PMH 2.0 endpoint. Catalan Journal of Linguistics, for example, answers Identify '
  name: Revistes UAB — Open Journal Systems (per-journal OAI-PMH 2.0)
  slug: revistes-ojs-oai
- description: UAB self-publishes a complete SAML 2.0 IdP EntityDescriptor at https://sso.uab.cat/cas/idp/metadata (HTTP 200, text/xml), entityID https://sso.uab.cat/cas/idp, shibmd:Scope sso.uab.cat. It declares se
  name: UAB Single Sign-On — SAML 2.0 Identity Provider
  slug: sso-saml-idp
- description: The CAS protocol face of the same server. https://sso.uab.cat/ redirects to /cas/login and the ticket-validation endpoint at /cas/p3/serviceValidate returns a well-formed cas:serviceResponse — an INVA
  name: UAB Central Authentication Service (CAS 3.0)
  slug: sso-cas
- description: UAB's entry in the Spanish national identity federation SIR, operated by RedIRIS, which is how UAB reaches eduGAIN. The EntityDescriptor at entityID https://www.rediris.es/sir/uabidp carries Organizat
  name: UAB in SIR / eduGAIN (RedIRIS federation entity)
  slug: sir-federation-entity
- description: UAB's research data lives in a named collection on CORA RDR, the Dataverse instance operated by the Consorci de Serveis Universitaris de Catalunya. The collection API at https://dataverse.csuc.cat/api
  name: CORA Repositori de Dades de Recerca — UAB collection (CSUC tenant)
  slug: cora-rdr
- description: UAB is a Crossref member in its own name. https://api.crossref.org/members/3612 returns primary-name "Universitat Autonoma de Barcelona", location "Bellaterra (Cerdanyola del Valles), Spain", prefixes
  name: Crossref membership (member 3612, prefix 10.5565)
  slug: crossref-member
- description: UAB's entry in the Research Organization Registry, https://ror.org/052g8jq94, which resolves the institution's canonical name, its website https://www.uab.cat and its cross-registry identifiers — Fund
  name: ROR registration (052g8jq94)
  slug: ror
- baseURL: https://ddd.uab.cat/oai2d
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting 2.0. The repository is OpenAIRE-compliant and is harvested by Google Scholar, BASE and CORE.
  name: Autonomous University of Barcelona OAI PMH API
  slug: uab-oai-pmh-api
- baseURL: https://ddd.uab.cat/oai2d
  baseurl_source: declared
  description: Invenio search with machine-readable output formats, used for record export outside the OAI-PMH flow.
  name: Autonomous University of Barcelona Search API
  slug: uab-search-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.uab.cat/
- group: docs
  title: ''
  type: Documentation
  url: https://www.uab.cat/en/libraries/digital-document-repository
- group: docs
  href: https://artifacts.apis.io/uab/openapi/_original/uab-ddd-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/uab-ddd-openapi.yml
- group: build
  href: https://artifacts.apis.io/uab/examples/uab-examples.yml
  title: ''
  type: Examples
  url: examples/uab-examples.yml
- group: auth
  href: https://artifacts.apis.io/uab/authentication/uab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uab-authentication.yml
- group: design
  href: https://artifacts.apis.io/uab/conformance/uab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uab-conformance.yml
- group: other
  href: https://artifacts.apis.io/uab/identity-federation/uab-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/uab-identity-federation.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://ddd.uab.cat/
- group: other
  title: ''
  type: OpenData
  url: https://www.uab.cat/ca/ciencia-oberta/dades-de-recerca-obert
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uab.cat/ca/etica-recerca/artificial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uab.cat/web/about-the-uab/itineraries/legal-notice-1345668684716.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uab.cat/web/la-uab/itineraris/proteccio-de-dades-1345668257177.html
- group: design
  href: https://artifacts.apis.io/uab/json-ld/uab-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/uab-context.jsonld
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uabbarcelona/
- group: auth
  href: https://artifacts.apis.io/uab/security/uab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uab-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/uab/plans/uab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uab-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/uab/rate-limits/uab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/uab-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/uab/finops/uab-finops.yml
  title: ''
  type: FinOps
  url: finops/uab-finops.yml
- group: other
  href: https://artifacts.apis.io/uab/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Universitat Autònoma de Barcelona (UAB) is a public research university in Bellaterra, Catalonia, founded in 1968. Unusually for this cohort, its programmable footprint is real and is genuinely its own. UAB runs four OAI-PMH 2.0 endpoints on its own RIPE allocation — the Dipòsit Digital de Documents (ddd.uab.cat, 221,931 records, 18 sets, oai_dc / marcxml / edm / oai_openaire), the Traces database of Catalan language and literature, the IFMuC inventory of Catalan music collections, and per-journal endpoints on its self-hosted OJS platform at revistes.uab.cat — and an Invenio search interface that exports MARC21 XML, Dublin Core and BibTeX without a key. It self-publishes a complete SAML 2.0 IdP EntityDescriptor from its own Apereo CAS server at sso.uab.cat, which is the one institution-published machine-readable contract here, and it reaches eduGAIN through the Spanish federation SIR, whose UAB entity is operated on RedIRIS''s gateway rather than UAB''s. UAB is a Crossref
  member in its own name (member 3612, prefix 10.5565, 23,089 DOIs) and holds ROR 052g8jq94. What it does not have is a developer programme: no OpenAPI is published for anything, api.uab.cat, data.uab.cat and opendata.uab.cat do not resolve, there is no API-key or OAuth path, no institutional GitHub organisation was found, and www.uab.cat has no llms.txt. Research data is a tenant relationship, not a UAB contract: the 567 datasets in UAB''s named collection live on the CSUC-operated CORA Repositori de Dades de Recerca and carry CSUC''s DataCite prefix.'
examples:
- key_count: 2
  name: Uab Cora Rdr Dataverse
  slug: uab-cora-rdr-dataverse
- key_count: 4
  name: Uab Crossref Member 3612
  slug: uab-crossref-member-3612
finops:
- has_sources: true
  method: generated
  name: Uab Finops
  primary_unit: ''
  service_category: Education
  slug: uab-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uab.png
jsonld:
- class_count: 12
  name: Uab Context
  property_count: 3
  slug: uab-context
layout: provider
modified: '2026-09-16'
name: Autonomous University of Barcelona
nav: Providers
network: true
overview: 'Autonomous University of Barcelona publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including OAI PMH API, Search API, and 9 more. Tagged areas include Education, Higher Education, University, Spain, and Catalonia.


  The Autonomous University of Barcelona catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Autonomous University of Barcelona''s developer surface includes documentation, code examples, authentication, and 16 more developer resources.'
plans:
- name: Uab Plans Pricing
  plan_count: 2
  slug: uab-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Uab Rate Limits
  slug: uab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Autonomous University of Barcelona API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: uab-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 22.1
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 24.9
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/uab/uab-2026-06-20T195920.png
security:
- kind: authentication
  name: Uab Authentication
  slug: uab-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Uab Domain Security
  slug: uab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uab
tags:
- Education
- Higher Education
- University
- Spain
- Catalonia
- Research
- Open Access
- Institutional Repository
- Research Repository
- Research Data
- OAI-PMH
- Identity Federation
- Scholarly Publishing
website: https://www.uab.cat/
---
