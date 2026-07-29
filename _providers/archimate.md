---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Archimate Agentic Access
  operation_count: 6
  slug: archimate-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 3
apis:
- description: Architecture element management
  name: ArchiMate Elements API
  slug: archimate-elements-api
- description: ArchiMate model management
  name: ArchiMate Models API
  slug: archimate-models-api
- description: Architecture relationship management
  name: ArchiMate Relationships API
  slug: archimate-relationships-api
artifact_total: 56
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archimate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archimate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archimate-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.opengroup.org/archimate-forum
- group: docs
  title: ''
  type: Documentation
  url: https://pubs.opengroup.org/architecture/archimate32-doc/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.opengroup.org/archimate-forum/archimate-overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/archimate-org
- group: operate
  title: ''
  type: Support
  url: https://www.opengroup.org/archimate-forum/forums
- group: company
  title: ''
  type: Blog
  url: https://blog.opengroup.org/tag/archimate/
- group: learn
  title: ''
  type: Training
  url: https://www.opengroup.org/certifications/archimate
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/rules/archimate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/vocabulary/archimate-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/json-ld/archimate-model-exchange-api-context.jsonld
created: '2024-01-01'
description: ArchiMate is an open and independent enterprise architecture modeling language developed by The Open Group, supporting description, analysis and visualization of architecture within and across business domains in an unambiguous way. The current version is ArchiMate 3.2.
examples:
- key_count: 5
  name: Archimate Model Exchange Api Element Example
  slug: archimate-model-exchange-api-element-example
- key_count: 2
  name: Archimate Model Exchange Api Element List Example
  slug: archimate-model-exchange-api-element-list-example
- key_count: 2
  name: Archimate Model Exchange Api Error Response Example
  slug: archimate-model-exchange-api-error-response-example
- key_count: 7
  name: Archimate Model Exchange Api Model Detail Example
  slug: archimate-model-exchange-api-model-detail-example
- key_count: 6
  name: Archimate Model Exchange Api Model Example
  slug: archimate-model-exchange-api-model-example
- key_count: 2
  name: Archimate Model Exchange Api Model Import Request Example
  slug: archimate-model-exchange-api-model-import-request-example
- key_count: 2
  name: Archimate Model Exchange Api Model List Example
  slug: archimate-model-exchange-api-model-list-example
- key_count: 5
  name: Archimate Model Exchange Api Relationship Example
  slug: archimate-model-exchange-api-relationship-example
- key_count: 2
  name: Archimate Model Exchange Api Relationship List Example
  slug: archimate-model-exchange-api-relationship-list-example
features:
- description: Standardized language for modeling business, application, and technology architecture layers.
  name: Enterprise Architecture Modeling
- description: ArchiMate Model Exchange File Format (AMEFF) for tool interoperability using XML.
  name: Model Exchange Format
- description: Business, Application, and Technology layers for comprehensive EA modeling.
  name: Three Architecture Layers
- description: Strategy and motivation aspect elements for stakeholder and driver modeling.
  name: Motivation and Strategy
- description: Work package and implementation elements for roadmap and migration planning.
  name: Implementation and Migration
- description: Supported by 20+ enterprise architecture tools including Archi, Sparx EA, BiZZdesign, and MEGA.
  name: Tool Ecosystem
- description: Open Group standard freely available for implementation without licensing fees.
  name: Open Standard
finops:
- name: Archimate Finops
  service_category: API
  slug: archimate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archimate.png
integrations:
- description: Open source ArchiMate modelling tool with full AMEFF import/export support.
  name: Archi
- description: Commercial EA tool with ArchiMate 3 profile and exchange format support.
  name: Sparx Enterprise Architect
- description: Enterprise architecture platform with native ArchiMate support.
  name: BiZZdesign
- description: Enterprise architecture management platform supporting ArchiMate standard.
  name: MEGA HOPEX
- description: ArchiMate is the recommended modeling language for TOGAF enterprise architecture framework.
  name: TOGAF
json_schemas:
- name: ElementList
  property_count: 2
  slug: archimate-model-exchange-api-element-list
- name: Element
  property_count: 5
  slug: archimate-model-exchange-api-element
- name: ErrorResponse
  property_count: 2
  slug: archimate-model-exchange-api-error-response
- name: ModelDetail
  property_count: 7
  slug: archimate-model-exchange-api-model-detail
- name: ModelImportRequest
  property_count: 2
  slug: archimate-model-exchange-api-model-import-request
- name: ModelList
  property_count: 2
  slug: archimate-model-exchange-api-model-list
- name: Model
  property_count: 6
  slug: archimate-model-exchange-api-model
- name: RelationshipList
  property_count: 2
  slug: archimate-model-exchange-api-relationship-list
- name: Relationship
  property_count: 5
  slug: archimate-model-exchange-api-relationship
json_structures:
- name: Archimate Model Exchange Api Element List Structure
  property_count: 2
  slug: archimate-model-exchange-api-element-list-structure
- name: Archimate Model Exchange Api Element Structure
  property_count: 5
  slug: archimate-model-exchange-api-element-structure
- name: Archimate Model Exchange Api Error Response Structure
  property_count: 2
  slug: archimate-model-exchange-api-error-response-structure
- name: Archimate Model Exchange Api Model Detail Structure
  property_count: 7
  slug: archimate-model-exchange-api-model-detail-structure
- name: Archimate Model Exchange Api Model Import Request Structure
  property_count: 2
  slug: archimate-model-exchange-api-model-import-request-structure
- name: Archimate Model Exchange Api Model List Structure
  property_count: 2
  slug: archimate-model-exchange-api-model-list-structure
- name: Archimate Model Exchange Api Model Structure
  property_count: 6
  slug: archimate-model-exchange-api-model-structure
- name: Archimate Model Exchange Api Relationship List Structure
  property_count: 2
  slug: archimate-model-exchange-api-relationship-list-structure
- name: Archimate Model Exchange Api Relationship Structure
  property_count: 5
  slug: archimate-model-exchange-api-relationship-structure
jsonld:
- class_count: 9
  name: Archimate Model Exchange Api Context
  property_count: 22
  slug: archimate-model-exchange-api-context
layout: provider
modified: '2026-05-19'
name: ArchiMate
nav: Providers
network: true
overview: 'ArchiMate publishes 3 APIs on the [APIs.io](https://apis.io/) network: Elements API, Models API, and Relationships API. Tagged areas include Enterprise Architecture, Architecture Framework, Modeling Language, Business Architecture, and Technology Architecture.


  The ArchiMate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ArchiMate''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, training material, and 6 more developer resources.'
plans:
- name: Archimate Plans Pricing
  plan_count: 3
  slug: archimate-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Archimate Rate Limits
  slug: archimate-rate-limits
rules:
- name: ArchiMate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: archimate-jsonschema-spectral-rules
- name: ArchiMate API Rules
  rule_count: 24
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 11
  slug: archimate-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: -7.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.9
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/screenshots/archimate-2026-06-20T172408.png
security:
- kind: authentication
  name: Archimate Authentication
  slug: archimate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Archimate Domain Security
  slug: archimate-domain-security
  summary_line: TLSv1.3
slug: archimate
tags:
- Enterprise Architecture
- Architecture Framework
- Modeling Language
- Business Architecture
- Technology Architecture
- Standard
- Open Group
use_cases:
- description: Document and communicate enterprise architecture across business, application, and technology layers.
  name: Enterprise Architecture Documentation
- description: Analyze dependencies, impacts, and gaps in enterprise architecture using standardized notation.
  name: Architecture Analysis
- description: Migrate ArchiMate models between EA tools using the standardized exchange format.
  name: Tool Migration
- description: Establish governance controls and compliance checking for enterprise architecture standards.
  name: Architecture Governance
- description: Manage IT application portfolios and rationalize technology investments using ArchiMate models.
  name: IT Portfolio Management
website: https://www.opengroup.org/archimate-forum
---
