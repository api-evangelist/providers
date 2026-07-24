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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 77
  human_in_the_loop: 0
  name: University Of Padua Agentic Access
  operation_count: 146
  slug: university-of-padua-agentic-access
  summary_line: 146 operations · 77 acting
api_count: 19
apis:
- description: PHAIDRA serves digital images through an IIIF (International Image Interoperability Framework) image server, enabling standards-based deep zoom and image delivery for the university's digital collecti
  name: PHAIDRA IIIF Image API
  slug: phaidra-iiif
- description: OAI-PMH metadata harvesting endpoint for the PHAIDRA digital collections, allowing programmatic harvesting of Dublin Core and related metadata. Verified live (verb=Identify returns HTTP 200) at time o
  name: PHAIDRA OAI-PMH
  slug: phaidra-oai
- description: Padua@Research (Padua Research Archive) is an EPrints-based institutional repository of the University of Padua's scientific production. It exposes an OAI-PMH 2.0 metadata harvesting interface; full t
  name: Padua@Research OAI-PMH
  slug: padua-research-oai
- description: Research Data Unipd is the EPrints-based research-data archive of the University of Padua, supporting data discovery, sharing, and reuse using DataCite and Dublin Core metadata. It is an OpenAIRE cont
  name: Research Data Unipd OAI-PMH
  slug: researchdata-oai
- description: 'The University of Padua provides centralized authentication via a Shibboleth-based Single Sign-On, integrated with the IDEM GARR federation and eduGAIN. Service Provider integration and SAML metadata '
  name: Single Sign-On (Shibboleth/SAML)
  slug: sso
- description: Requests for transforming and validating datastreams
  name: University of Padua datastream API
  slug: university-of-padua-datastream-api
- description: Requests related to users, user groups and organisation structure
  name: University of Padua directory API
  slug: university-of-padua-directory-api
- description: Requests to the imageserver
  name: University of Padua imageserver API
  slug: university-of-padua-imageserver-api
- description: Requests for manipulating object lists
  name: University of Padua lists API
  slug: university-of-padua-lists-api
- description: The misc API from University of Padua — 7 operation(s) for misc.
  name: University of Padua misc API
  slug: university-of-padua-misc-api
- description: Look at the [OAI-PMH protocol](https://www.openarchives.org/pmh) used in this endpoint
  name: University of Padua oai-pmh API
  slug: university-of-padua-oai-pmh-api
- description: Additional requests for the manipulation of digital objects
  name: University of Padua object-advanced API
  slug: university-of-padua-object-advanced-api
- description: Most important requests you'll need to manage digital objects in PHAIDRA
  name: University of Padua object-basics API
  slug: university-of-padua-object-basics-api
- description: Requests for adding and removing object relationships
  name: University of Padua relationships API
  slug: university-of-padua-relationships-api
- description: The search API from University of Padua — 1 operation(s) for search.
  name: University of Padua search API
  slug: university-of-padua-search-api
- description: Session management
  name: University of Padua session API
  slug: university-of-padua-session-api
- description: The stats API from University of Padua — 4 operation(s) for stats.
  name: University of Padua stats API
  slug: university-of-padua-stats-api
- description: Requests for managing metadata templates
  name: University of Padua templates API
  slug: university-of-padua-templates-api
- description: Requests for controlled vocabularies
  name: University of Padua vocabularies API
  slug: university-of-padua-vocabularies-api
artifact_total: 34
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-padua-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-padua-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-padua-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unipd.it/en
- group: build
  title: ''
  type: Library
  url: https://biblio.unipd.it/en
- group: company
  title: ''
  type: LinkedIn
  url: https://it.linkedin.com/school/university-of-padova/
- group: auth
  title: ''
  type: Authentication
  url: https://asit.unipd.it/single-sign-informazioni-tecniche-service-provider
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-padua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-padua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-padua-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Padua (Università degli Studi di Padova) is a public research university in Padua, Italy, founded in 1222 and ranked #236 in the QS World University Rankings 2025. Its public developer/API footprint is centered on the University Library System (SBA) rather than a single official developer portal: PHAIDRA, the digital-collections platform, exposes a documented REST API (OpenAPI), a IIIF image service, and an OAI-PMH endpoint, while the EPrints-based Padua@Research and Research Data Unipd repositories provide OAI-PMH metadata harvesting. Authentication across university services is delivered through a Shibboleth/SAML Single Sign-On integrated with the IDEM GARR federation and eduGAIN. There is no central institutional GitHub organization for the university as a whole; public code lives in individual lab and department orgs.'
examples:
- key_count: 3
  name: University Of Padua Object Info Example
  slug: university-of-padua-object-info-example
- key_count: 2
  name: University Of Padua Search Select Example
  slug: university-of-padua-search-select-example
- key_count: 2
  name: University Of Padua Signin Example
  slug: university-of-padua-signin-example
finops:
- name: University Of Padua Finops
  service_category: Education
  slug: university-of-padua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-padua.png
json_schemas:
- name: PHAIDRA Collection
  property_count: 27
  slug: university-of-padua-collection
- name: PHAIDRA Object Info
  property_count: 30
  slug: university-of-padua-object_info
json_structures:
- name: University Of Padua Object_Info Structure
  property_count: 18
  slug: university-of-padua-object_info-structure
jsonld:
- class_count: 3
  name: University Of Padua Context
  property_count: 17
  slug: university-of-padua-context
layout: provider
modified: '2026-06-03'
name: University of Padua
nav: Providers
network: true
overview: 'University of Padua publishes 14 APIs on the [APIs.io](https://apis.io/) network, including datastream API, directory API, imageserver API, and 11 more. Tagged areas include Education, Higher Education, University, Open Data, and Research Data.


  The University of Padua catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Padua''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: University Of Padua Plans Pricing
  plan_count: 2
  slug: university-of-padua-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: University Of Padua Rate Limits
  slug: university-of-padua-rate-limits
rules:
- name: University of Padua API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-padua-jsonschema-spectral-rules
- name: University of Padua API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 2
  slug: university-of-padua-rules
score:
  band: thin
  composite: 42.1
  delta: -0.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.6
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 42.9
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-padua/refs/heads/main/screenshots/university-of-padua-2026-06-20T200320.png
security:
- kind: authentication
  name: University Of Padua Authentication
  slug: university-of-padua-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: University Of Padua Domain Security
  slug: university-of-padua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-padua
tags:
- Education
- Higher Education
- University
- Open Data
- Research Data
- Library
- Repository
- Italy
website: https://www.unipd.it/en
---
