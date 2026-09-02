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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Rely Agentic Access
  operation_count: 23
  slug: rely-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 1
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rely.io Public Automations API
  slug: open-rely-automations-api
- collection_type: open
  name: Rely.io Public Automations Blueprints API
  slug: open-rely-blueprints-api
- collection_type: open
  name: Rely.io Public Automations Entities API
  slug: open-rely-entities-api
- collection_type: open
  name: Rely.io Public Automations Scorecards API
  slug: open-rely-scorecards-api
- collection_type: open
  name: Rely.io Public Automations Self-Service Actions API
  slug: open-rely-self-service-actions-api
- collection_type: open
  name: Rely.io Public Automations Users API
  slug: open-rely-users-api
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
random_paper: 3
rate_limits:
- limit_count: 5
  name: Rely Rate Limits
  slug: rely-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rely.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rely-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Rely.io API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: rely-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 65.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
