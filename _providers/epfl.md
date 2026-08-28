---
access_model:
  confidence: high
  label: Free · No signup required
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - conformance
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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Epfl Agentic Access
  operation_count: 33
  slug: epfl-agentic-access
  summary_line: 33 operations
api_count: 9
apis:
- description: 'EPFL''s public news API, serving the Actu newsroom — news, projects, channels, faculties, categories, themes and publics. Django REST Framework, read-only (Allow: GET, HEAD, OPTIONS), unauthenticated b'
  name: EPFL Actu News API
  slug: actu-news-api
- description: EPFL's public events and agenda API, serving the Memento calendar — events, mementos, registrations, domains, categories, faculties, spoken languages and vulgarizations. Django REST Framework, read-on
  name: EPFL Memento Events API
  slug: memento-events-api
- description: Infoscience is EPFL's institutional repository and CRIS, self-hosted on EPFL infrastructure and running DSpace-CRIS. It exposes a HAL/HATEOAS REST API rooted at /server/api with 40+ link relations, an
  name: EPFL Infoscience Institutional Repository
  slug: infoscience
- description: GETprime is a public, unauthenticated HTTP service from EPFL's Gene Expression Core Facility that returns ranked, validated qPCR primer pairs for a gene identifier, organism and Ensembl release. It is
  name: EPFL GETprime qPCR Primer API
  slug: getprime
- description: EPFL Graph Search is an EPFL-built knowledge-graph search over EPFL concepts, people, units and publications. It has a live HTTP API router — every /api/* path returns a JSON {"message":"Route not fou
  name: EPFL Graph Search
  slug: graphsearch
- description: EPFL's institutional URL shortener publishes an API page describing token-authenticated link creation. Access is gated to EPFL community members holding an institutional token, so it is a real institu
  name: EPFL go.epfl.ch URL Shortener API
  slug: go-url-shortener
- description: EPFL is a registered member of SWITCHaai, the Swiss academic identity federation, which is exported to eduGAIN. Seventeen entityIDs containing "epfl" appear in the federation aggregate. EPFL's identit
  name: EPFL SAML Identity Federation Entities
  slug: identity-federation
- description: EPFL's SAML identity provider is delivered by SWITCH edu-ID as a hosted, EPFL-branded IdP. The relationship is a real institutional fact — EPFL authenticates its community through it and its entity is
  name: EPFL Identity Provider (SWITCH edu-ID, tenant)
  slug: eduid-idp
- description: EPFL's library discovery and resolution run on Ex Libris Primo VE with Alma behind it, delivered through SLSP (Swiss Library Service Platform). EPFL's holdings, EPFL's patrons, EPFL's branded entry po
  name: EPFL Library Discovery on swisscovery (Ex Libris, tenant)
  slug: swisscovery-library
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EPFL Categories API
  slug: open-epfl-categories-api
- collection_type: open
  name: EPFL Channels API
  slug: open-epfl-channels-api
- collection_type: open
  name: EPFL Domains API
  slug: open-epfl-domains-api
- collection_type: open
  name: EPFL Events API
  slug: open-epfl-events-api
- collection_type: open
  name: EPFL Faculties API
  slug: open-epfl-faculties-api
- collection_type: open
  name: EPFL Mementos API
  slug: open-epfl-mementos-api
- collection_type: open
  name: EPFL News API
  slug: open-epfl-news-api
- collection_type: open
  name: EPFL Projects API
  slug: open-epfl-projects-api
- collection_type: open
  name: EPFL Publics API
  slug: open-epfl-publics-api
- collection_type: open
  name: EPFL Registrations API
  slug: open-epfl-registrations-api
- collection_type: open
  name: EPFL Spoken Languages API
  slug: open-epfl-spoken-languages-api
- collection_type: open
  name: EPFL Themes API
  slug: open-epfl-themes-api
- collection_type: open
  name: EPFL Vulgarizations API
  slug: open-epfl-vulgarizations-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.epfl.ch
- group: learn
  title: ''
  type: CourseCatalog
  url: https://edu.epfl.ch/
- group: other
  title: ''
  type: ResearchRepository
  url: https://infoscience.epfl.ch/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://epfl.swisscovery.ch/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.aai.switch.ch/metadata.switchaai.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.epfl.ch/research/facilities/scitas/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.epfl.ch/education/teaching/index-html/ai-teaching/guidelines-for-the-use-of-ai-in-teaching-at-epfl/
- group: build
  title: ''
  type: AITooling
  url: https://www.epfl.ch/education/teaching/index-html/ai-teaching/
- group: docs
  title: ''
  type: Documentation
  url: https://actu.epfl.ch/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://memento.epfl.ch/api/docs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epfl.ch/about/overview/regulations-and-guidelines/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epfl.ch/about/presidency/presidents-team/legal-affairs/epfl-privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.epfl.ch/campus/library/
- group: company
  title: ''
  type: Blog
  url: https://actu.epfl.ch/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/epfl-si
- group: build
  title: ''
  type: GitHub
  url: https://github.com/epfl-si
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/epfl/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.epfl.ch/.well-known/security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/epfl-conformance.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/epfl-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/epfl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/epfl-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/epfl-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/epfl-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/epfl-rules.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/epfl-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/epfl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epfl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epfl-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/epfl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/epfl-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/epfl-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'EPFL (École polytechnique fédérale de Lausanne) is a Swiss federal institute of technology in Lausanne and one of the two federal technical universities in the ETH Domain. Measured on what it actually operates rather than what runs under its name, EPFL is unusual among research universities: it runs FOUR public, unauthenticated APIs on its own registrable domain. The Actu news API (actu.epfl.ch) and the Memento events API (memento.epfl.ch) are Django REST Framework services with live interactive CoreAPI documentation; Infoscience (infoscience.epfl.ch) is EPFL''s self-hosted DSpace-CRIS repository serving a HAL/HATEOAS REST API and a working OAI-PMH provider; and GETprime (getprime.epfl.ch), from the Gene Expression Core Facility, answers primer-design queries over HTTP. EPFL publishes no OpenAPI for any of them and operates no developer portal, no API gateway (api.epfl.ch resolves only to RFC 1918 space), no plans, no rate-limit documentation and no deprecation policy — every
  OpenAPI in this repo is derived by API Evangelist and marked as such. Its library discovery runs on Ex Libris Primo/Alma through the SLSP consortium and its identity provider endpoint is hosted by SWITCH edu-ID; both are recorded here as tenant relationships, not as EPFL engineering. There is no public course-catalog or timetable API.'
examples:
- key_count: 4
  name: Epfl Listevents Example
  slug: epfl-listEvents-example
- key_count: 4
  name: Epfl Listnews Example
  slug: epfl-listNews-example
finops:
- name: Epfl Finops
  service_category: Education
  slug: epfl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epfl.png
json_schemas:
- name: EPFL Memento Event
  property_count: 38
  slug: epfl-event
- name: EPFL Actu News
  property_count: 26
  slug: epfl-news
json_structures:
- name: Epfl Event Structure
  property_count: 25
  slug: epfl-event-structure
- name: Epfl News Structure
  property_count: 21
  slug: epfl-news-structure
jsonld:
- class_count: 27
  name: Epfl Context
  property_count: 12
  slug: epfl-context
layout: provider
modified: '2026-08-19'
name: EPFL
nav: Providers
network: true
overview: 'EPFL publishes 3 APIs on the [APIs.io](https://apis.io/) network: Actu News API, Memento Events API, and GETprime qPCR Primer API. Tagged areas include University, Higher Education, Education, Technical University, and Research.


  The EPFL catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  EPFL''s developer surface includes documentation, API reference, support, engineering blog, GitHub presence, authentication, and 27 more developer resources.'
plans:
- name: Epfl Plans Pricing
  plan_count: 2
  slug: epfl-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Epfl Rate Limits
  slug: epfl-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: EPFL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: epfl-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: EPFL API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: epfl-rules
scopes:
- name: Epfl Scopes
  scope_count: 0
  slug: epfl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.3
  delta: 0.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 26.2
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 23.7
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epfl/refs/heads/main/screenshots/epfl-2026-06-20T180750.png
security:
- kind: authentication
  name: Epfl Authentication
  slug: epfl-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Epfl Domain Security
  slug: epfl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Epfl Vulnerability Disclosure
  slug: epfl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: epfl
tags:
- University
- Higher Education
- Education
- Technical University
- Research
- Research Repository
- Open Access
- Identity Federation
- News
- Event
- Switzerland
- Europe
website: https://www.epfl.ch
---
