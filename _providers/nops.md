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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Nops Agentic Access
  operation_count: 12
  slug: nops-agentic-access
  summary_line: 12 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.nops.io
  baseurl_source: declared
  description: Endpoints for managing the nOps Essentials scheduler, which automates resource management tasks like starting and stopping non-production workloads to reduce costs.
  name: nOps Essentials Scheduler API
  slug: nops-essentials-scheduler-api
- baseURL: https://app.nops.io
  baseurl_source: declared
  description: Endpoints for managing and retrieving information about AWS Migration Acceleration Program (MAP) migration projects, including projects, products, and resources.
  name: nOps MAP Migration API
  slug: nops-map-migration-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: nOps Essentials Scheduler API
  slug: open-nops-essentials-scheduler-api
- collection_type: open
  name: nOps Essentials Scheduler MAP Migration API
  slug: open-nops-map-migration-api
- collection_type: open
  name: nOps API
  slug: open-nops-nops
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nops-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nops-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nops-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nops
- group: company
  title: ''
  type: Blog
  url: https://www.nops.io/blog/
- group: learn
  title: ''
  type: Webinars
  url: https://www.nops.io/webinars-and-workshops/
- group: other
  title: ''
  type: Resources
  url: https://www.nops.io/ncast/
- group: docs
  title: ''
  type: Documentation
  url: https://help.nops.io/docs/introduction/platform-introduction
- group: docs
  title: ''
  type: Documentation
  url: https://help.nops.io/docs/support/customer-service-sla
- group: operate
  title: ''
  type: Support
  url: https://help.nops.io/docs/support/open-support-case
created: '2026-01-02'
description: nOps is an AI-powered cloud cost visibility and optimization platform that helps organizations reduce their AWS spending by 50% or more through autonomous management and automation. The platform provides 100% visibility into cloud costs across AWS, GCP, Azure, Kubernetes, GenAI, and SaaS applications, enabling teams to allocate and track spending by customer, product, cost center, or any other dimension even without complete tagging.
examples:
- key_count: 3
  name: Nops Nops Map Migration Product Example
  slug: nops-nops-map-migration-product-example
- key_count: 5
  name: Nops Nops Map Migration Project Example
  slug: nops-nops-map-migration-project-example
- key_count: 4
  name: Nops Nops Map Migration Resource Example
  slug: nops-nops-map-migration-resource-example
- key_count: 4
  name: Nops Nops Scheduler Create Request Example
  slug: nops-nops-scheduler-create-request-example
- key_count: 5
  name: Nops Nops Scheduler Example
  slug: nops-nops-scheduler-example
features:
- description: AI-powered autonomous management that identifies and implements cost savings without manual intervention.
  name: Autonomous Cost Optimization
- description: Complete visibility into cloud costs across AWS, GCP, Azure, Kubernetes, GenAI, and SaaS applications.
  name: 100% Cost Visibility
- description: Automated scheduling of non-production workloads to eliminate idle resource costs.
  name: Essentials Scheduler
- description: AWS Migration Acceleration Program tracking for migration projects, products, and resources.
  name: MAP Migration Support
- description: Intelligent spot instance management for maximizing cost savings on compute workloads.
  name: Spot Instance Optimization
finops:
- name: Nops Finops
  service_category: API
  slug: nops-finops
image: /assets/icons/nops.png
integrations:
- description: Deep integration with AWS billing, CUR, CloudTrail, CloudWatch, and resource management services.
  name: AWS Services
- description: Container cost visibility and optimization for EKS and self-managed Kubernetes clusters.
  name: Kubernetes
- description: Notification integrations for cost alerts, optimization recommendations, and scheduler events.
  name: Slack and Teams
json_schemas:
- name: nOps MAP Migration Product
  property_count: 3
  slug: map-migration-product
- name: nOps MAP Migration Project
  property_count: 5
  slug: map-migration-project
- name: nOps MAP Migration Resource
  property_count: 4
  slug: map-migration-resource
- name: MapMigrationProduct
  property_count: 3
  slug: nops-nops-map-migration-product
- name: MapMigrationProject
  property_count: 5
  slug: nops-nops-map-migration-project
- name: MapMigrationResource
  property_count: 4
  slug: nops-nops-map-migration-resource
- name: SchedulerCreateRequest
  property_count: 4
  slug: nops-nops-scheduler-create-request
- name: Scheduler
  property_count: 5
  slug: nops-nops-scheduler
- name: nOps Scheduler
  property_count: 7
  slug: scheduler
json_structures:
- name: Nops Nops Map Migration Product Structure
  property_count: 3
  slug: nops-nops-map-migration-product-structure
- name: Nops Nops Map Migration Project Structure
  property_count: 5
  slug: nops-nops-map-migration-project-structure
- name: Nops Nops Map Migration Resource Structure
  property_count: 4
  slug: nops-nops-map-migration-resource-structure
- name: Nops Nops Scheduler Create Request Structure
  property_count: 4
  slug: nops-nops-scheduler-create-request-structure
- name: Nops Nops Scheduler Structure
  property_count: 5
  slug: nops-nops-scheduler-structure
jsonld:
- class_count: 0
  name: Nops Context
  property_count: 4
  slug: nops-context
- class_count: 0
  name: Nops Nops Context
  property_count: 0
  slug: nops-nops-context
layout: provider
modified: '2026-05-19'
name: nOps
nav: Providers
network: true
overview: 'nOps publishes 2 APIs on the [APIs.io](https://apis.io/) network: Essentials Scheduler API and MAP Migration API. Tagged areas include Costs and FinOps.


  The nOps catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  nOps'' developer surface includes authentication, engineering blog, documentation, support, and 7 more developer resources.'
plans:
- name: Nops Plans Pricing
  plan_count: 3
  slug: nops-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Nops Rate Limits
  slug: nops-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: nOps API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nops-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: nOps API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: nops-spectral-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 67.3
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nops/refs/heads/main/screenshots/nops-2026-06-20T190405.png
security:
- kind: authentication
  name: Nops Authentication
  slug: nops-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nops Domain Security
  slug: nops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nops
tags:
- Costs
- FinOps
use_cases:
- description: Automate cloud cost allocation, tracking, and optimization across teams and business units.
  name: FinOps Automation
- description: Track MAP migration projects and measure cost savings from AWS migration programs.
  name: Cloud Migration Tracking
- description: Identify and schedule or terminate idle resources to reduce wasted cloud spending.
  name: Idle Resource Elimination
- description: Real-time detection and alerting on unusual cost spikes and billing anomalies.
  name: Cost Anomaly Detection
---
