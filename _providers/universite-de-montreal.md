---
access_model:
  confidence: high
  label: Free · open · no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.recherche.umontreal.ca/vitrine/rest/api/1.8/umontreal
  baseurl_source: declared
  description: 'Université de Montréal''s own read-only research API, and the one genuinely institution-engineered contract in this profile. Five services: reference-value exposure (faculties, departments, administrat'
  name: SADVR REST API (Vitrine-Recherche)
  slug: sadvr
- description: 'Université de Montréal''s campus single sign-on, published as machine-readable SAML 2.0 entity metadata. The document declares an IDPSSODescriptor supporting SAML 2.0, SAML 1.1 and the legacy urn:mace:'
  name: UdeM Shibboleth Identity Provider (SAML metadata)
  slug: shibboleth-idp
- description: OAI-PMH 2.0 harvesting interface for PAPYRUS, Université de Montréal's institutional repository of open-access theses, dissertations and scholarly output. Identify returns repositoryName "PAPYRUS - Dé
  name: PAPYRUS OAI-PMH Endpoint (institutional repository)
  slug: papyrus-oai
- description: 'The DSpace 8 REST API behind PAPYRUS, answering anonymously at the HAL root and advertising the repository''s entry points as application/hal+json. Reads are open; deposit and restricted items require '
  name: PAPYRUS DSpace REST API (HAL)
  slug: papyrus-dspace-rest
- description: Université de Montréal's research-data collection inside Borealis, the Canadian national Dataverse. 452 UdeM datasets, each carrying a DataCite DOI under the 10.5683 prefix, plus 20-odd sub-collection
  name: Borealis Dataverse — Université de Montréal collection
  slug: borealis-dataverse
- description: Library discovery for the Université de Montréal libraries, delivered on OCLC WorldCat Discovery. Recorded as the institution's library-catalogue surface and explicitly as a tenancy. OCLC's WorldCat S
  name: WorldCat Discovery — Université de Montréal
  slug: worldcat-discovery
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.umontreal.ca/en/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.umontreal.ca/spaces/DOC/pages/294781211/API+REST+%E2%80%93+Description+technique
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.umontreal.ca/spaces/DOC/overview
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.umontreal.ca/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://umontreal.scholaris.ca/
- group: other
  title: ''
  type: ResearchData
  url: https://borealisdata.ca/dataverse/montreal
- group: build
  title: ''
  type: LibraryCatalog
  url: https://umontreal.on.worldcat.org/discovery
- group: learn
  title: ''
  type: CourseCatalog
  url: https://admission.umontreal.ca/repertoire-des-cours/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.umontreal.ca/intelligenceartificielle/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bibudem
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vie-privee.umontreal.ca/conditions-dutilisation/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vie-privee.umontreal.ca/confidentialite/
- group: company
  title: ''
  type: Blog
  url: https://nouvelles.umontreal.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universite-de-montreal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/universite-de-montreal-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/universite-de-montreal-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/universite-de-montreal-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/universite-de-montreal-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/universite-de-montreal-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universite-de-montreal-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/universite-de-montreal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/universite-de-montreal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/universite-de-montreal-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: Université de Montréal (UdeM) is Québec's largest French-language public research university and, with its two affiliated schools, the second-largest research complex in Canada. Its programmable footprint is small, real, and almost entirely research-facing — and it is important to say plainly what UdeM does and does not operate, because this profile previously claimed 36 APIs it does not have. UdeM genuinely operates two machine-readable surfaces. The first is the SADVR REST API (Service d'accès aux données de la Vitrine-Recherche), built in-house by the Centre d'expertise numérique pour la recherche and serving UdeM's faculties, departments, job titles, programmes, disciplines, research-expertise keywords and its own persistent identifiers (idsadvr) for 3,516 indexed researchers and 429 research units — read-only, keyless, French-first, documented on the institution's own wiki, and confirmed live on 2026-08-30. The second is UdeM's Shibboleth Identity Provider, which publishes
  SAML 2.0 entity metadata under the institution's own domain; it is institution-operated by definition and is the kind of surface this cohort systematically fails to catalogue. Everything else in UdeM's footprint is a tenancy. PAPYRUS, the institutional repository, moved to Scholaris, the CRKN-hosted national DSpace service, so its OAI-PMH and DSpace REST contracts are DSpace's. UdeM's research data lives in a collection on Borealis, the shared Canadian Dataverse operated by Scholars Portal, so that contract is Dataverse's. Library discovery runs on OCLC WorldCat, and the LMS is Moodle. The data in all four is UdeM's; the engineering is not. There is no central developer portal, no self-service credential, no OAuth authorization server and no published status page. api.umontreal.ca resolves and answers, but returns HTTP 400 with an empty body on every anonymous path and is documented nowhere — an internal gateway, not a public API.
examples:
- key_count: 9
  name: Universite De Montreal Sadvr Ressource Domaineetude Example
  slug: universite-de-montreal-sadvr-ressource-domaineetude-example
- key_count: 9
  name: Universite De Montreal Sadvr Ressource Faculte Example
  slug: universite-de-montreal-sadvr-ressource-faculte-example
- key_count: 9
  name: Universite De Montreal Sadvr Ressource Langue Example
  slug: universite-de-montreal-sadvr-ressource-langue-example
- key_count: 9
  name: Universite De Montreal Sadvr Ressource Typeuniterech Example
  slug: universite-de-montreal-sadvr-ressource-typeuniterech-example
finops:
- name: Universite De Montreal Finops
  service_category: Education
  slug: universite-de-montreal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universite-de-montreal.png
json_schemas:
- name: SADVR Reference Resource Envelope
  property_count: 1
  slug: universite-de-montreal-sadvr-ressource
- name: SADVR Research Unit (unité de recherche)
  property_count: 10
  slug: universite-de-montreal-sadvr-uniterech
jsonld:
- class_count: 15
  name: Universite De Montreal Context
  property_count: 23
  slug: universite-de-montreal-context
layout: provider
modified: '2026-08-30'
name: Université de Montréal
nav: Providers
network: true
overview: 'Université de Montréal publishes 1 API on the [APIs.io](https://apis.io/) network: SADVR REST API (Vitrine-Recherche). Tagged areas include University, Higher Education, Education, Canada, and Québec.


  The Université de Montréal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Université de Montréal''s developer surface includes documentation, API reference, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Universite De Montreal Plans Pricing
  plan_count: 2
  slug: universite-de-montreal-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Universite De Montreal Rate Limits
  slug: universite-de-montreal-rate-limits
rules:
- effective_rule_count: 15
  extends: []
  name: Université de Montréal API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 6
  slug: universite-de-montreal-sadvr-rules
scopes:
- name: Universite De Montreal Scopes
  scope_count: 0
  slug: universite-de-montreal-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 28.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 45.5
    contract_quality: 30.6
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 23.7
  previous_composite: 44.3
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
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universite-de-montreal/refs/heads/main/screenshots/universite-de-montreal-2026-06-20T200115.png
security:
- kind: authentication
  name: Universite De Montreal Authentication
  slug: universite-de-montreal-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Universite De Montreal Domain Security
  slug: universite-de-montreal-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: universite-de-montreal
tags:
- University
- Higher Education
- Education
- Canada
- Québec
- French Language
- U15
- Public Research University
- Research
- Research Data
- Research Expertise
- Identity Federation
- Institutional Repository
- Library
- Open Access
- OAI-PMH
- Shibboleth
- SAML
website: https://www.umontreal.ca/en/
---
