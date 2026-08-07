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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Architecture Pattern Agentic Access
  operation_count: 5
  slug: architecture-pattern-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Domains API from Architecture Pattern — 1 operation(s) for domains.
  name: Architecture Pattern Domains API
  slug: architecture-pattern-domains-api
- description: The Patterns API from Architecture Pattern — 3 operation(s) for patterns.
  name: Architecture Pattern Patterns API
  slug: architecture-pattern-patterns-api
- description: The Trade-offs API from Architecture Pattern — 1 operation(s) for trade-offs.
  name: Architecture Pattern Trade-offs API
  slug: architecture-pattern-trade-offs-api
artifact_total: 38
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/architecture-pattern-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/architecture-pattern-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://microservices.io/patterns/
- group: docs
  title: ''
  type: Documentation
  url: https://microservices.io/patterns/
- group: company
  title: ''
  type: Blog
  url: https://microservices.io/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/rules/architecture-pattern-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/vocabulary/architecture-pattern-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/json-ld/architecture-pattern-api-context.jsonld
created: '2025-01-01'
description: Architecture Patterns provide reusable solutions to commonly occurring software and system design problems. They offer proven templates for organizing code, components, and interactions across distributed systems, microservices, cloud-native applications, and enterprise software.
examples:
- key_count: 2
  name: Architecture Pattern Api Domain Example
  slug: architecture-pattern-api-domain-example
- key_count: 2
  name: Architecture Pattern Api Domain List Example
  slug: architecture-pattern-api-domain-list-example
- key_count: 2
  name: Architecture Pattern Api Pattern Example
  slug: architecture-pattern-api-pattern-example
- key_count: 2
  name: Architecture Pattern Api Pattern List Example
  slug: architecture-pattern-api-pattern-list-example
- key_count: 2
  name: Architecture Pattern Api Tradeoff Example
  slug: architecture-pattern-api-tradeoff-example
- key_count: 2
  name: Architecture Pattern Api Tradeoff List Example
  slug: architecture-pattern-api-tradeoff-list-example
features:
- description: Comprehensive catalog of architecture patterns for microservices, distributed systems, and cloud-native applications.
  name: Pattern Catalog
- description: Each pattern includes problem statement, solution approach, and known trade-offs.
  name: Problem-Solution Framework
- description: Related patterns organized into a coherent pattern language for navigating complex architecture decisions.
  name: Pattern Language
- description: Patterns illustrated with real-world implementations from production systems.
  name: Real-World Examples
- description: Guidance for selecting appropriate patterns based on context and constraints.
  name: Decision Support
finops:
- name: Architecture Pattern Finops
  service_category: API
  slug: architecture-pattern-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/architecture-pattern.png
json_schemas:
- name: DomainList
  property_count: 2
  slug: architecture-pattern-api-domain-list
- name: Domain
  property_count: 5
  slug: architecture-pattern-api-domain
- name: PatternList
  property_count: 4
  slug: architecture-pattern-api-pattern-list
- name: Pattern
  property_count: 12
  slug: architecture-pattern-api-pattern
- name: TradeoffList
  property_count: 2
  slug: architecture-pattern-api-tradeoff-list
- name: Tradeoff
  property_count: 7
  slug: architecture-pattern-api-tradeoff
json_structures:
- name: Architecture Pattern Api Domain List Structure
  property_count: 2
  slug: architecture-pattern-api-domain-list-structure
- name: Architecture Pattern Api Domain Structure
  property_count: 5
  slug: architecture-pattern-api-domain-structure
- name: Architecture Pattern Api Pattern List Structure
  property_count: 4
  slug: architecture-pattern-api-pattern-list-structure
- name: Architecture Pattern Api Pattern Structure
  property_count: 12
  slug: architecture-pattern-api-pattern-structure
- name: Architecture Pattern Api Tradeoff List Structure
  property_count: 2
  slug: architecture-pattern-api-tradeoff-list-structure
- name: Architecture Pattern Api Tradeoff Structure
  property_count: 7
  slug: architecture-pattern-api-tradeoff-structure
jsonld:
- class_count: 6
  name: Architecture Pattern Api Context
  property_count: 0
  slug: architecture-pattern-api-context
layout: provider
modified: '2026-05-19'
name: Architecture Pattern
nav: Providers
network: true
overview: 'Architecture Pattern publishes 3 APIs on the [APIs.io](https://apis.io/) network: Domains API, Patterns API, and Trade-offs API. Tagged areas include Architecture Patterns, Software Architecture, Design Patterns, System Design, and Microservices.


  The Architecture Pattern catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Architecture Pattern''s developer surface includes developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Architecture Pattern Plans Pricing
  plan_count: 3
  slug: architecture-pattern-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Architecture Pattern Rate Limits
  slug: architecture-pattern-rate-limits
rules:
- name: Architecture Pattern API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: architecture-pattern-jsonschema-spectral-rules
- name: Architecture Pattern API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: architecture-pattern-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/screenshots/architecture-pattern-2026-06-20T172407.png
security:
- kind: domain-security
  name: Architecture Pattern Domain Security
  slug: architecture-pattern-domain-security
  summary_line: TLSv1.3
slug: architecture-pattern
tags:
- Architecture Patterns
- Software Architecture
- Design Patterns
- System Design
- Microservices
- Cloud Native
use_cases:
- description: Apply patterns for decomposing monolithic applications into microservices.
  name: Microservices Design
- description: Reference patterns for handling distributed computing challenges like consistency and availability.
  name: Distributed Systems
- description: Select cloud-native patterns when migrating on-premises applications to cloud platforms.
  name: Cloud Migration
- description: Evaluate architecture decisions against proven patterns and identify improvement areas.
  name: Architecture Review
website: https://microservices.io/patterns/
---
