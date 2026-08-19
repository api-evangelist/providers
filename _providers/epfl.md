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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Epfl Agentic Access
  operation_count: 33
  slug: epfl-agentic-access
  summary_line: 33 operations
api_count: 14
apis:
- description: Infoscience is EPFL's institutional repository, running on DSpace 7.6.2. It exposes a public HATEOAS/HAL REST API (items, collections, communities, bitstreams, discovery/search and more) and an OAI-PM
  name: EPFL Infoscience Repository API
  slug: infoscience
- description: The Categories API from EPFL — 2 operation(s) for categories.
  name: EPFL Categories API
  slug: epfl-categories-api
- description: The Channels API from EPFL — 4 operation(s) for channels.
  name: EPFL Channels API
  slug: epfl-channels-api
- description: The Domains API from EPFL — 2 operation(s) for domains.
  name: EPFL Domains API
  slug: epfl-domains-api
- description: The Events API from EPFL — 2 operation(s) for events.
  name: EPFL Events API
  slug: epfl-events-api
- description: The Faculties API from EPFL — 2 operation(s) for faculties.
  name: EPFL Faculties API
  slug: epfl-faculties-api
- description: The Mementos API from EPFL — 3 operation(s) for mementos.
  name: EPFL Mementos API
  slug: epfl-mementos-api
- description: The News API from EPFL — 2 operation(s) for news.
  name: EPFL News API
  slug: epfl-news-api
- description: The Projects API from EPFL — 2 operation(s) for projects.
  name: EPFL Projects API
  slug: epfl-projects-api
- description: The Publics API from EPFL — 2 operation(s) for publics.
  name: EPFL Publics API
  slug: epfl-publics-api
- description: The Registrations API from EPFL — 2 operation(s) for registrations.
  name: EPFL Registrations API
  slug: epfl-registrations-api
- description: The Spoken Languages API from EPFL — 2 operation(s) for spoken languages.
  name: EPFL Spoken Languages API
  slug: epfl-spoken-languages-api
- description: The Themes API from EPFL — 2 operation(s) for themes.
  name: EPFL Themes API
  slug: epfl-themes-api
- description: The Vulgarizations API from EPFL — 2 operation(s) for vulgarizations.
  name: EPFL Vulgarizations API
  slug: epfl-vulgarizations-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EPFL Actu News Categories API
  slug: open-epfl-categories-api
- collection_type: open
  name: EPFL Actu News Categories Channels API
  slug: open-epfl-channels-api
- collection_type: open
  name: EPFL Actu News Categories Domains API
  slug: open-epfl-domains-api
- collection_type: open
  name: EPFL Actu News Categories Events API
  slug: open-epfl-events-api
- collection_type: open
  name: EPFL Actu News Categories Faculties API
  slug: open-epfl-faculties-api
- collection_type: open
  name: EPFL Actu News Categories Mementos API
  slug: open-epfl-mementos-api
- collection_type: open
  name: EPFL Actu Categories News API
  slug: open-epfl-news-api
- collection_type: open
  name: EPFL Actu News Categories Projects API
  slug: open-epfl-projects-api
- collection_type: open
  name: EPFL Actu News Categories Publics API
  slug: open-epfl-publics-api
- collection_type: open
  name: EPFL Actu News Categories Registrations API
  slug: open-epfl-registrations-api
- collection_type: open
  name: EPFL Actu News Categories Spoken Languages API
  slug: open-epfl-spoken-languages-api
- collection_type: open
  name: EPFL Actu News Categories Themes API
  slug: open-epfl-themes-api
- collection_type: open
  name: EPFL Actu News Categories Vulgarizations API
  slug: open-epfl-vulgarizations-api
common:
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
- group: company
  title: ''
  type: Website
  url: https://www.epfl.ch
- group: build
  title: ''
  type: GitHub
  url: https://github.com/epfl-si
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/epfl/
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
description: 'EPFL (École Polytechnique Fédérale de Lausanne) is a public research university in Lausanne, Switzerland, ranked #19 in the QS World University Rankings 2025. EPFL exposes several public, documented REST APIs across its digital campus, including the Actu news API and the Memento events API (both with self-service interactive docs), and its Infoscience institutional repository runs on DSpace 7 with a public REST API and OAI-PMH endpoint. Additional EPFL code is published openly across official GitHub organizations such as EPFL-SI (IT systems and infrastructure) and EPFL-ENAC.'
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
modified: '2026-06-03'
name: EPFL
nav: Providers
network: true
overview: 'EPFL publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Channels API, Domains API, and 10 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The EPFL catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  EPFL''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Epfl Plans Pricing
  plan_count: 2
  slug: epfl-plans-pricing
random_paper: 125
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
score:
  band: thin
  composite: 36.6
  delta: -4.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 56.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- Education
- Higher Education
- University
- Research
- Open Data
- Switzerland
- Europe
website: https://www.epfl.ch
---
