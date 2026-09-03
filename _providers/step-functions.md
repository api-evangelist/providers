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
- acting_count: 1
  human_in_the_loop: 0
  name: Step Functions Agentic Access
  operation_count: 1
  slug: step-functions-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://states.{region}.amazonaws.com
  baseurl_source: declared
  description: Create, describe, update, delete, and list state machines
  name: AWS Step Functions State Machines API
  slug: step-functions-state-machines-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Step Functions State Machines API
  slug: open-step-functions-state-machines-api
- collection_type: open
  name: AWS Step Functions API
  slug: open-step-functions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/step-functions-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/step-functions-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/step-functions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/step-functions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/step-functions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/step-functions/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/step-functions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/states/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/step-functions/pricing/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/category/compute/aws-step-functions/
created: '2026-03-27'
description: AWS Step Functions is a serverless orchestration service that enables developers to compose distributed applications and APIs using visual workflows called state machines. It supports Standard and Express workflows, activities, parallel execution, error handling, and integrates with over 200 AWS services. Step Functions uses the Amazon States Language (ASL) for defining workflow logic as JSON-based state machine definitions.
examples:
- key_count: 4
  name: Step Functions List State Machines Example
  slug: step-functions-list-state-machines-example
- key_count: 4
  name: Step Functions Start Execution Example
  slug: step-functions-start-execution-example
finops:
- name: Step Functions Finops
  service_category: API
  slug: step-functions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/step-functions.png
json_schemas:
- name: AWS Step Functions State Machine
  property_count: 12
  slug: step-functions-state-machine
json_structures:
- name: Step Functions State Machine Structure
  property_count: 0
  slug: step-functions-state-machine-structure
jsonld:
- class_count: 16
  name: Step Functions Context
  property_count: 8
  slug: step-functions-context
layout: provider
modified: '2026-05-19'
name: AWS Step Functions
nav: Providers
network: true
overview: 'AWS Step Functions publishes 1 API on the [APIs.io](https://apis.io/) network: State Machines API. Tagged areas include API Composition, Serverless Orchestration, Workflows, State Machine, and Automation.


  The AWS Step Functions catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AWS Step Functions'' developer surface includes authentication, documentation, developer console, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Step Functions Plans Pricing
  plan_count: 3
  slug: step-functions-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Step Functions Rate Limits
  slug: step-functions-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AWS Step Functions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: step-functions-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: AWS Step Functions API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: step-functions-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 63.3
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/step-functions/refs/heads/main/screenshots/step-functions-2026-06-20T194541.png
security:
- kind: authentication
  name: Step Functions Authentication
  slug: step-functions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Step Functions Domain Security
  slug: step-functions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Step Functions Vulnerability Disclosure
  slug: step-functions-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Step Functions Trust Center
  slug: step-functions-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: step-functions
tags:
- API Composition
- Serverless Orchestration
- Workflows
- State Machine
- Automation
website: https://aws.amazon.com/step-functions/
---
