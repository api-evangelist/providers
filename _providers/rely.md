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
- acting_count: 14
  human_in_the_loop: 0
  name: Rely Agentic Access
  operation_count: 23
  slug: rely-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 6
apis:
- description: Manage automation rules that trigger workflows based on catalog entity changes or external events via plugin integrations.
  name: Rely.io Automations API
  slug: rely-automations-api
- description: Manage blueprint schemas that define the structure and attributes of catalog entities such as services, teams, and resources.
  name: Rely.io Blueprints API
  slug: rely-blueprints-api
- description: Manage catalog entity instances — the individual services, teams, deployments, and resources tracked in the software catalog.
  name: Rely.io Entities API
  slug: rely-entities-api
- description: Define and manage engineering scorecards that track adoption of standards and production readiness across services.
  name: Rely.io Scorecards API
  slug: rely-scorecards-api
- description: Configure developer self-service actions that automate infrastructure provisioning, service scaffolding, and deployment workflows.
  name: Rely.io Self-Service Actions API
  slug: rely-self-service-actions-api
- description: Manage user accounts and invitations in the organization.
  name: Rely.io Users API
  slug: rely-users-api
artifact_total: 21
collections:
- collection_type: open
  name: Rely.io Public API
  slug: open-rely
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rely-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rely-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rely-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rely.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rely.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rely-io
- group: build
  title: ''
  type: GitHub SDK
  url: https://github.com/Rely-io/galaxy-oss
- group: start
  title: ''
  type: Signup
  url: https://app.rely.io/register
- group: start
  title: ''
  type: Demo
  url: https://demo.rely.io
- group: operate
  title: ''
  type: Support
  url: mailto:support@rely.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rely-io
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.rely.io/llms.txt
created: '2026-03-27'
description: Rely.io is an internal developer portal that aggregates engineering data, provides software catalogs with blueprints and entities, engineering scorecards, self-service developer actions, and workflow automation for platform engineering teams. The platform integrates with CI/CD pipelines, incident management, observability, and cloud providers to create a centralized service catalog with real-time data. Rely.io's Public REST API provides full CRUD access to blueprints, entities, scorecards, self-service actions, and automations using Bearer token authentication.
examples:
- key_count: 2
  name: Rely Create Entity Example
  slug: rely-create-entity-example
- key_count: 2
  name: Rely List Blueprints Example
  slug: rely-list-blueprints-example
finops:
- name: Rely Finops
  service_category: API
  slug: rely-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rely.png
json_schemas:
- name: Rely.io Blueprint
  property_count: 7
  slug: rely-blueprint
- name: Rely.io Entity
  property_count: 7
  slug: rely-entity
json_structures:
- name: Rely Blueprint Structure
  property_count: 0
  slug: rely-blueprint-structure
jsonld:
- class_count: 7
  name: Rely Context
  property_count: 13
  slug: rely-context
layout: provider
modified: '2026-05-19'
name: Rely.io
nav: Providers
network: true
overview: 'Rely.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Automations API, Blueprints API, Entities API, and 3 more. Tagged areas include Developer Experience, Internal Developer Portal, Platform Engineering, Software Catalog, and Service Catalog.


  The Rely.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rely.io''s developer surface includes authentication, documentation, signup flow, support, and 8 more developer resources.'
plans:
- name: Rely Plans Pricing
  plan_count: 3
  slug: rely-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Rely Rate Limits
  slug: rely-rate-limits
rules:
- name: Rely.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rely-jsonschema-spectral-rules
- name: Rely.io API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: rely-rules
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.9
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 50.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rely/refs/heads/main/screenshots/rely-2026-06-20T192840.png
security:
- kind: authentication
  name: Rely Authentication
  slug: rely-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rely Domain Security
  slug: rely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rely
tags:
- Developer Experience
- Internal Developer Portal
- Platform Engineering
- Software Catalog
- Service Catalog
- Engineering Scorecards
website: https://www.rely.io
---
