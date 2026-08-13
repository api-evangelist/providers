---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 182
  human_in_the_loop: 3
  name: Scalr Agentic Access
  operation_count: 310
  slug: scalr-agentic-access
  summary_line: 310 operations · 182 acting · 3 human-in-the-loop
api_count: 26
apis:
- description: The Scalr IaC Management API (TFC-compatible) provides programmatic control over workspaces, environments, runs, state, variables, policies, and provider configurations. Fully compatible with Terrafor
  name: Scalr IaC Management API
  slug: scalr-iac-api
- description: The Acl Roles API from Scalr — 1 operation(s) for acl roles.
  name: Scalr Acl Roles API
  slug: scalr-acl-roles-api
- description: The Ansible Tower API from Scalr — 6 operation(s) for ansible tower.
  name: Scalr Ansible Tower API
  slug: scalr-ansible-tower-api
- description: The Cloud Credentials API from Scalr — 4 operation(s) for cloud credentials.
  name: Scalr Cloud Credentials API
  slug: scalr-cloud-credentials-api
- description: The Clouds API from Scalr — 2 operation(s) for clouds.
  name: Scalr Clouds API
  slug: scalr-clouds-api
- description: The Cost Centers API from Scalr — 3 operation(s) for cost centers.
  name: Scalr Cost Centers API
  slug: scalr-cost-centers-api
- description: The Environments API from Scalr — 6 operation(s) for environments.
  name: Scalr Environments API
  slug: scalr-environments-api
- description: The Event Logs API from Scalr — 2 operation(s) for event logs.
  name: Scalr Event Logs API
  slug: scalr-event-logs-api
- description: The Events API from Scalr — 5 operation(s) for events.
  name: Scalr Events API
  slug: scalr-events-api
- description: The Farm Roles API from Scalr — 13 operation(s) for farm roles.
  name: Scalr Farm Roles API
  slug: scalr-farm-roles-api
- description: The Farms API from Scalr — 16 operation(s) for farms.
  name: Scalr Farms API
  slug: scalr-farms-api
- description: The Global Variables API from Scalr — 6 operation(s) for global variables.
  name: Scalr Global Variables API
  slug: scalr-global-variables-api
- description: The Images API from Scalr — 12 operation(s) for images.
  name: Scalr Images API
  slug: scalr-images-api
- description: The Orchestration Logs API from Scalr — 2 operation(s) for orchestration logs.
  name: Scalr Orchestration Logs API
  slug: scalr-orchestration-logs-api
- description: The Orchestration Rules API from Scalr — 4 operation(s) for orchestration rules.
  name: Scalr Orchestration Rules API
  slug: scalr-orchestration-rules-api
- description: The Os API from Scalr — 6 operation(s) for os.
  name: Scalr Os API
  slug: scalr-os-api
- description: The Projects API from Scalr — 4 operation(s) for projects.
  name: Scalr Projects API
  slug: scalr-projects-api
- description: The Role Categories API from Scalr — 6 operation(s) for role categories.
  name: Scalr Role Categories API
  slug: scalr-role-categories-api
- description: The Roles API from Scalr — 33 operation(s) for roles.
  name: Scalr Roles API
  slug: scalr-roles-api
- description: The Scaling Metrics API from Scalr — 4 operation(s) for scaling metrics.
  name: Scalr Scaling Metrics API
  slug: scalr-scaling-metrics-api
- description: The Script Executions API from Scalr — 1 operation(s) for script executions.
  name: Scalr Script Executions API
  slug: scalr-script-executions-api
- description: The Scripts API from Scalr — 10 operation(s) for scripts.
  name: Scalr Scripts API
  slug: scalr-scripts-api
- description: The Servers API from Scalr — 9 operation(s) for servers.
  name: Scalr Servers API
  slug: scalr-servers-api
- description: The Teams API from Scalr — 2 operation(s) for teams.
  name: Scalr Teams API
  slug: scalr-teams-api
- description: The Users API from Scalr — 2 operation(s) for users.
  name: Scalr Users API
  slug: scalr-users-api
- description: The Webhook Endpoints API from Scalr — 2 operation(s) for webhook endpoints.
  name: Scalr Webhook Endpoints API
  slug: scalr-webhook-endpoints-api
artifact_total: 42
collections:
- collection_type: open
  name: Scalr Account API
  slug: open-scalr-account
- collection_type: open
  name: Scalr Global API
  slug: open-scalr-global
- collection_type: open
  name: Scalr User API
  slug: open-scalr-user
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scalr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalr-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scalr
- group: company
  title: ''
  type: Website
  url: https://scalr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scalr.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scalr.io/reference/overview-1
- group: other
  title: ''
  type: API Explorer
  url: https://api-explorer.scalr.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/scalr
- group: company
  title: ''
  type: Blog
  url: https://scalr.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.scalr.io/
- group: agent
  title: ''
  type: MCP Server
  url: https://docs.scalr.io/docs/mcp-server
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/Scalr/scalr/latest/docs
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/vocabulary/scalr-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/json-schema/scalr-workspace-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/json-schema/scalr-run-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/json-ld/scalr-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/rules/scalr-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.scalr.io/llms.txt
created: '2026-05-02'
description: Scalr is an enterprise-grade, drop-in replacement for Terraform Cloud and a remote Terraform operations backend that provides cost estimation, policy enforcement, and collaborative infrastructure management. Scalr features a hierarchical account-environment-workspace model, full compatibility with the TFC API and Terraform/OpenTofu CLI, OIDC authentication, GitOps workflows, OPA policy enforcement, and a comprehensive REST API for managing infrastructure as code operations at scale.
examples:
- key_count: 2
  name: Scalr Create Run Example
  slug: scalr-create-run-example
- key_count: 2
  name: Scalr List Workspaces Example
  slug: scalr-list-workspaces-example
finops:
- name: Scalr Finops
  service_category: Developer Tools
  slug: scalr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalr.png
json_schemas:
- name: Scalr Run
  property_count: 13
  slug: scalr-run
- name: Scalr Workspace
  property_count: 17
  slug: scalr-workspace
json_structures:
- name: Scalr Workspace Structure
  property_count: 0
  slug: scalr-workspace-structure
jsonld:
- class_count: 1
  name: Scalr Context
  property_count: 27
  slug: scalr-context
layout: provider
modified: '2026-05-19'
name: Scalr
nav: Providers
network: true
overview: 'Scalr publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Acl Roles API, Ansible Tower API, Cloud Credentials API, and 22 more. Tagged areas include FinOps, GitOps, Infrastructure as Code, Kubernetes, and OPA.


  The Scalr catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scalr''s developer surface includes documentation, API reference, GitHub presence, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Scalr Plans Pricing
  plan_count: 2
  slug: scalr-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 1
  name: Scalr Rate Limits
  slug: scalr-rate-limits
rules:
- name: Scalr API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: scalr-jsonschema-spectral-rules
- name: Scalr API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 2
    info: 2
    warn: 4
  slug: scalr-rules
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 43.3
    developer_ergonomics: 17.4
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/screenshots/scalr-2026-06-20T193608.png
security:
- kind: domain-security
  name: Scalr Domain Security
  slug: scalr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scalr
tags:
- FinOps
- GitOps
- Infrastructure as Code
- Kubernetes
- OPA
- OpenTofu
- Policy
- Terraform
website: https://scalr.com/
---
