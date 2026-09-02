---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agile-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://agilemanifesto.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2025-01-01'
description: A collection of resources, standards, and APIs representing the broader agile landscape — the set of software development principles first codified in the 2001 Agile Manifesto. Agile values individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan. This topic index covers the full ecosystem of agile frameworks, methodologies, tools, and APIs including Scrum, Kanban, SAFe, XP, and Lean.
examples:
- key_count: 4
  name: Agile Agile Principle Example
  slug: agile-agile-principle-example
features:
- description: The 12 principles of the Agile Manifesto form the philosophical foundation for all agile frameworks and practices.
  name: Agile Manifesto Principles
- description: Agile encompasses multiple frameworks — Scrum, Kanban, SAFe, LeSS, XP, and DSDM — each suited to different team sizes and contexts.
  name: Framework Diversity
- description: Agile practices emphasize continuous customer and stakeholder engagement through demos, reviews, and feedback loops.
  name: Customer Collaboration
- description: Agile teams embrace change, using iterative planning cycles to adapt priorities and scope based on learning and feedback.
  name: Adaptive Planning
- description: Agile prioritizes delivering working, tested software over creating documentation or following rigid processes.
  name: Working Software First
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agile.png
integrations:
- description: The most widely used agile project management platform with Scrum and Kanban board support.
  name: Jira
- description: Agile documentation and knowledge base platform that integrates with Jira.
  name: Confluence
- description: Team communication platform widely used for agile standup notifications and sprint updates.
  name: Slack
- description: Source control and project management platform that supports agile workflows through Issues and Projects.
  name: GitHub
- description: Microsoft's agile planning and DevOps platform with comprehensive APIs for agile work management.
  name: Azure DevOps
json_schemas:
- name: AgilePrinciple
  property_count: 4
  slug: agile-agile-principle
json_structures:
- name: Agile Agile Principle Structure
  property_count: 4
  slug: agile-agile-principle-structure
jsonld:
- class_count: 1
  name: Agile Context
  property_count: 4
  slug: agile-context
layout: provider
modified: '2026-04-19'
name: Agile
nav: Providers
network: true
overview: 'Agile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Iterative Development, Methodology, Project Management, Software Development, and Agile Manifesto.


  The Agile catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agile''s developer surface includes developer portal and 2 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 4
  extends: []
  name: Agile API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: agile-jsonschema-spectral-rules
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 79.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 6.7
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 10.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agile/refs/heads/main/screenshots/agile-2026-06-20T170144.png
security:
- kind: domain-security
  name: Agile Domain Security
  slug: agile-domain-security
  summary_line: TLSv1.3
slug: agile
tags:
- Iterative Development
- Methodology
- Project Management
- Software Development
- Agile Manifesto
- Scrum
- Kanban
use_cases:
- description: Apply agile principles to build software products iteratively, incorporating user feedback between delivery cycles.
  name: Software Product Development
- description: Scale agile practices across large organizations using frameworks like SAFe to improve delivery speed and quality.
  name: Enterprise Digital Transformation
- description: Use agile's emphasis on early delivery and feedback to validate product hypotheses before large investments.
  name: Startup Product Discovery
- description: Apply agile practices to API development, delivering versioned API increments with developer feedback incorporated each sprint.
  name: Platform and API Development
website: https://agilemanifesto.org/
---
