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
api_count: 1
apis:
- description: OAI-PMH 2.0 harvesting endpoint for UAB's institutional repository of theses, articles, preprints, postprints, ebooks, rare books, periodicals, graphic documents and political posters. Identify return
  name: DDD — Dipòsit Digital de Documents de la UAB (OAI-PMH 2.0)
  slug: ddd-oai-pmh
- description: 'The repository''s search endpoint returns machine-readable records when given an output format: of=xm yields MARC21 XML in the loc.gov/MARC21/slim namespace, of=xd yields Dublin Core XML, of=hx yields '
  name: DDD Invenio Search and Export Interface
  slug: ddd-search
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
artifact_total: 19
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
  title: ''
  type: OpenAPI
  url: openapi/uab-ddd-openapi.yml
- group: build
  title: ''
  type: Examples
  url: examples/uab-examples.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uab-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uab-conformance.yml
- group: other
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
  title: ''
  type: JSONLD
  url: json-ld/uab-context.jsonld
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uabbarcelona/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uab-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uab-finops.yml
- group: other
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
- name: Uab Finops
  service_category: Education
  slug: uab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uab.png
jsonld:
- class_count: 12
  name: Uab Context
  property_count: 3
  slug: uab-context
layout: provider
modified: '2026-09-01'
name: Autonomous University of Barcelona
nav: Providers
network: true
overview: 'Autonomous University of Barcelona publishes 2 APIs on the [APIs.io](https://apis.io/) network: DDD — Dipòsit Digital de Documents de la UAB (OAI-PMH 2.0) and DDD Invenio Search and Export Interface. Tagged areas include Education, Higher Education, University, Spain, and Catalonia.


  The Autonomous University of Barcelona catalog on APIs.io includes 1 JSON-LD context.


  Autonomous University of Barcelona''s developer surface includes documentation, code examples, authentication, and 16 more developer resources.'
plans:
- name: Uab Plans Pricing
  plan_count: 2
  slug: uab-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Uab Rate Limits
  slug: uab-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 14.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 22.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.9
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
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/uab/refs/heads/main/screenshots/uab-2026-06-20T195920.png
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
