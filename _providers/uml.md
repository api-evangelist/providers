---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Uml Agentic Access
  operation_count: 9
  slug: uml-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 3
apis:
- description: Generate diagrams from textual descriptions
  name: UML Diagrams API
  slug: uml-diagrams-api
- description: Service health check
  name: UML Health API
  slug: uml-health-api
- description: Validate PlantUML source syntax
  name: UML Validation API
  slug: uml-validation-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kroki Diagram API
  slug: open-kroki
- collection_type: open
  name: PlantUML Server API
  slug: open-plantuml-server
- collection_type: open
  name: Kroki Diagram Diagrams API
  slug: open-uml-diagrams-api
- collection_type: open
  name: Kroki Diagram Diagrams Health API
  slug: open-uml-health-api
- collection_type: open
  name: Kroki Diagram Diagrams Validation API
  slug: open-uml-validation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uml-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uml-domain-security.yml
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/plantuml
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/yuzutech
- group: company
  title: ''
  type: Website
  url: https://www.omg.org/uml/
- group: other
  title: ''
  type: Standards
  url: https://www.omg.org/spec/UML/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Unified_Modeling_Language
- group: build
  title: ''
  type: GitHub
  url: https://github.com/plantuml/plantuml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/yuzutech/kroki
- group: docs
  title: ''
  type: Documentation
  url: https://plantuml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kroki.io/kroki/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/uml-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uml-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uml-diagram-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/uml-rules.yml
created: '2025-01-01'
description: UML (Unified Modeling Language) is the standard modeling language for software architecture, system design, and technical documentation. Governed by the Object Management Group (OMG), UML defines a set of notation conventions and diagram types — class, sequence, activity, use case, state, component, deployment, and more — used across the software development lifecycle. This collection profiles the ecosystem of tools, APIs, and services that work with UML diagrams programmatically.
examples:
- key_count: 4
  name: Kroki Post Diagram Example
  slug: kroki-post-diagram-example
- key_count: 5
  name: Plantuml Get Diagram Png Example
  slug: plantuml-get-diagram-png-example
finops:
- name: Uml Finops
  service_category: API
  slug: uml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uml.png
json_schemas:
- name: UML Diagram
  property_count: 12
  slug: uml-diagram
json_structures:
- name: Uml Diagram Structure
  property_count: 0
  slug: uml-diagram-structure
jsonld:
- class_count: 6
  name: Uml Context
  property_count: 10
  slug: uml-context
layout: provider
modified: '2026-05-19'
name: UML
nav: Providers
network: true
overview: 'UML publishes 3 APIs on the [APIs.io](https://apis.io/) network: Diagrams API, Health API, and Validation API. Tagged areas include UML, Modeling, Diagrams, Software Architecture, and Design.


  The UML catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UML''s developer surface includes GitHub presence, documentation, and 13 more developer resources.'
plans:
- name: Uml Plans Pricing
  plan_count: 3
  slug: uml-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Uml Rate Limits
  slug: uml-rate-limits
rules:
- name: UML API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: uml-jsonschema-spectral-rules
- name: UML API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: uml-rules
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 62.2
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uml/refs/heads/main/screenshots/uml-2026-06-20T200022.png
security:
- kind: domain-security
  name: Uml Domain Security
  slug: uml-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uml
tags:
- UML
- Modeling
- Diagrams
- Software Architecture
- Design
- Standards
website: https://www.omg.org/uml/
---
