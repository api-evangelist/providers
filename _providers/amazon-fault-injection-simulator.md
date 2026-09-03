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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Amazon Fault Injection Simulator Agentic Access
  operation_count: 18
  slug: amazon-fault-injection-simulator-agentic-access
  summary_line: 18 operations · 8 acting · 2 human-in-the-loop
api_count: 6
apis:
- baseURL: https://fis.amazonaws.com
  baseurl_source: declared
  description: Discover available FIS fault injection actions
  name: Amazon Fault Injection Simulator Actions API
  slug: amazon-fault-injection-simulator-actions-api
- baseURL: https://fis.amazonaws.com
  baseurl_source: declared
  description: Create and manage fault injection experiment templates
  name: Amazon Fault Injection Simulator Experiment Templates API
  slug: amazon-fault-injection-simulator-experiment-templates-api
- baseURL: https://fis.amazonaws.com
  baseurl_source: declared
  description: Start, stop, and monitor fault injection experiments
  name: Amazon Fault Injection Simulator Experiments API
  slug: amazon-fault-injection-simulator-experiments-api
- baseURL: https://fis.amazonaws.com
  baseurl_source: declared
  description: Manage safety levers for experiment control
  name: Amazon Fault Injection Simulator Safety Levers API
  slug: amazon-fault-injection-simulator-safety-levers-api
- baseURL: https://fis.amazonaws.com
  baseurl_source: declared
  description: Manage tags on FIS resources
  name: Amazon Fault Injection Simulator Tagging API
  slug: amazon-fault-injection-simulator-tagging-api
- baseURL: https://fis.amazonaws.com
  baseurl_source: declared
  description: Discover available target resource types
  name: Amazon Fault Injection Simulator Target Resource Types API
  slug: amazon-fault-injection-simulator-target-resource-types-api
arazzos:
- description: List the available FIS actions and fetch the full detail of the first action returned.
  name: AWS FIS Discover Action Detail
  slug: amazon-fault-injection-simulator-discover-action-detail-workflow
- description: List the supported target resource types and fetch the full detail of the first one returned.
  name: AWS FIS Discover Target Resource Type
  slug: amazon-fault-injection-simulator-discover-target-resource-type-workflow
- description: List experiments for a template, and if the first one is still active, stop it and confirm the stop.
  name: AWS FIS Find and Stop Running Experiment
  slug: amazon-fault-injection-simulator-find-and-stop-running-experiment-workflow
- description: List experiment templates and fetch the full definition of the first one returned.
  name: AWS FIS List Then Get Experiment Template
  slug: amazon-fault-injection-simulator-list-then-get-template-workflow
- description: Create an experiment template, start an experiment from it, and poll until the experiment reaches a terminal state.
  name: AWS FIS Run Experiment to Completion
  slug: amazon-fault-injection-simulator-run-experiment-to-completion-workflow
- description: Start an experiment from an existing template, confirm it is running, stop it, and poll until it is fully stopped.
  name: AWS FIS Start Then Stop Experiment
  slug: amazon-fault-injection-simulator-start-then-stop-experiment-workflow
- description: Fetch an existing experiment template, update its description, and start an experiment from the revised template.
  name: AWS FIS Update Template Then Run
  slug: amazon-fault-injection-simulator-update-template-then-run-workflow
artifact_total: 78
collections:
- collection_type: postman
  name: AWS Fault Injection Simulator API
  slug: postman-amazon-fis
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Fault Injection Simulator Actions API
  slug: open-amazon-fault-injection-simulator-actions-api
- collection_type: open
  name: AWS Fault Injection Simulator Actions Experiment Templates API
  slug: open-amazon-fault-injection-simulator-experiment-templates-api
- collection_type: open
  name: AWS Fault Injection Simulator Actions Experiments API
  slug: open-amazon-fault-injection-simulator-experiments-api
- collection_type: open
  name: AWS Fault Injection Simulator Actions Safety Levers API
  slug: open-amazon-fault-injection-simulator-safety-levers-api
- collection_type: open
  name: AWS Fault Injection Simulator Actions Tagging API
  slug: open-amazon-fault-injection-simulator-tagging-api
- collection_type: open
  name: AWS Fault Injection Simulator Actions Target Resource Types API
  slug: open-amazon-fault-injection-simulator-target-resource-types-api
- collection_type: open
  name: AWS Fault Injection Simulator API
  slug: open-amazon-fis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-fault-injection-simulator-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-fault-injection-simulator-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-fault-injection-simulator-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-fault-injection-simulator-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-fault-injection-simulator-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-fault-injection-simulator/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-discover-action-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-discover-target-resource-type-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-find-and-stop-running-experiment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-list-then-get-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-run-experiment-to-completion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-start-then-stop-experiment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-fault-injection-simulator-update-template-then-run-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/fis/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/fis/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/fis/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/tag/aws-fault-injection-simulator/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/fis/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-fis
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-fis-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-fis-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-fis-context.jsonld
created: '2026-03-16'
description: AWS Fault Injection Simulator (FIS) is a fully managed service for running fault injection experiments on AWS. It allows you to improve an application's performance, observability, and resiliency by identifying and fixing weaknesses through controlled chaos engineering experiments.
examples:
- key_count: 6
  name: Amazon Fis Action Example
  slug: amazon-fis-action-example
- key_count: 11
  name: Amazon Fis Experiment Example
  slug: amazon-fis-experiment-example
- key_count: 2
  name: Amazon Fis Experiment State Example
  slug: amazon-fis-experiment-state-example
- key_count: 5
  name: Amazon Fis Experiment Template Action Example
  slug: amazon-fis-experiment-template-action-example
- key_count: 10
  name: Amazon Fis Experiment Template Example
  slug: amazon-fis-experiment-template-example
- key_count: 2
  name: Amazon Fis Experiment Template Stop Condition Example
  slug: amazon-fis-experiment-template-stop-condition-example
- key_count: 5
  name: Amazon Fis Experiment Template Target Example
  slug: amazon-fis-experiment-template-target-example
- key_count: 3
  name: Amazon Fis Safety Lever Example
  slug: amazon-fis-safety-lever-example
- key_count: 2
  name: Amazon Fis Safety Lever State Example
  slug: amazon-fis-safety-lever-state-example
- key_count: 3
  name: Amazon Fis Target Resource Type Example
  slug: amazon-fis-target-resource-type-example
features:
- description: Fully managed service requiring no agent installation with pre-built fault injection actions for EC2, RDS, ECS, EKS, and more.
  name: Managed Fault Injection
- description: Ready-to-use resilience scenarios for AZ failures, power interruptions, network disruptions, and cross-region connectivity issues.
  name: Pre-built Scenarios
- description: CloudWatch alarm-based stop conditions and safety levers prevent unintended impact during live testing.
  name: Safety Controls
- description: Tag-based resource targeting scopes experiments to specific environments, applications, or resource subsets.
  name: Fine-grained Targeting
- description: Run experiments across multiple AWS accounts using target account configurations.
  name: Multi-account Support
- description: API and CLI access enables automated resilience testing in deployment pipelines.
  name: CI/CD Integration
- description: Console and API provide real-time status of executing actions, affected resources, and triggered stop conditions.
  name: Real-time Visibility
- description: Fine-grained IAM controls restrict which users can create, run, or view experiments and affected resources.
  name: IAM Security
finops:
- name: Amazon Fault Injection Simulator Finops
  service_category: API
  slug: amazon-fault-injection-simulator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-fault-injection-simulator.png
json_schemas:
- name: Action
  property_count: 6
  slug: amazon-fis-action
- name: Experiment
  property_count: 11
  slug: amazon-fis-experiment
- name: ExperimentState
  property_count: 2
  slug: amazon-fis-experiment-state
- name: ExperimentTemplateAction
  property_count: 5
  slug: amazon-fis-experiment-template-action
- name: ExperimentTemplate
  property_count: 10
  slug: amazon-fis-experiment-template
- name: ExperimentTemplateStopCondition
  property_count: 2
  slug: amazon-fis-experiment-template-stop-condition
- name: ExperimentTemplateTarget
  property_count: 5
  slug: amazon-fis-experiment-template-target
- name: SafetyLever
  property_count: 3
  slug: amazon-fis-safety-lever
- name: SafetyLeverState
  property_count: 2
  slug: amazon-fis-safety-lever-state
- name: TargetResourceType
  property_count: 3
  slug: amazon-fis-target-resource-type
json_structures:
- name: Amazon Fis Action Structure
  property_count: 6
  slug: amazon-fis-action-structure
- name: Amazon Fis Experiment State Structure
  property_count: 2
  slug: amazon-fis-experiment-state-structure
- name: Amazon Fis Experiment Structure
  property_count: 11
  slug: amazon-fis-experiment-structure
- name: Amazon Fis Experiment Template Action Structure
  property_count: 5
  slug: amazon-fis-experiment-template-action-structure
- name: Amazon Fis Experiment Template Stop Condition Structure
  property_count: 2
  slug: amazon-fis-experiment-template-stop-condition-structure
- name: Amazon Fis Experiment Template Structure
  property_count: 10
  slug: amazon-fis-experiment-template-structure
- name: Amazon Fis Experiment Template Target Structure
  property_count: 5
  slug: amazon-fis-experiment-template-target-structure
- name: Amazon Fis Safety Lever State Structure
  property_count: 2
  slug: amazon-fis-safety-lever-state-structure
- name: Amazon Fis Safety Lever Structure
  property_count: 3
  slug: amazon-fis-safety-lever-structure
- name: Amazon Fis Target Resource Type Structure
  property_count: 3
  slug: amazon-fis-target-resource-type-structure
jsonld:
- class_count: 13
  name: Amazon Fis Context
  property_count: 23
  slug: amazon-fis-context
layout: provider
modified: '2026-05-19'
name: Amazon Fault Injection Simulator
nav: Providers
network: true
overview: 'Amazon Fault Injection Simulator publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Experiment Templates API, Experiments API, and 3 more. Tagged areas include Chaos Engineering, DevOps, Fault Injection, and Resilience Testing.


  The Amazon Fault Injection Simulator catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Amazon Fault Injection Simulator''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 22 more developer resources.'
plans:
- name: Amazon Fault Injection Simulator Plans Pricing
  plan_count: 3
  slug: amazon-fault-injection-simulator-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Amazon Fault Injection Simulator Rate Limits
  slug: amazon-fault-injection-simulator-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Fault Injection Simulator API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-fault-injection-simulator-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Amazon Fault Injection Simulator API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 9
  slug: amazon-fault-injection-simulator-spectral-rules
- effective_rule_count: 28
  extends: []
  name: Amazon Fault Injection Simulator API Rules
  rule_count: 28
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 16
  slug: amazon-fis-spectral-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 35.6
    developer_ergonomics: 57.1
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/screenshots/amazon-fault-injection-simulator-2026-06-20T171648.png
security:
- kind: authentication
  name: Amazon Fault Injection Simulator Authentication
  slug: amazon-fault-injection-simulator-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Fault Injection Simulator Domain Security
  slug: amazon-fault-injection-simulator-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Fault Injection Simulator Vulnerability Disclosure
  slug: amazon-fault-injection-simulator-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Fault Injection Simulator Trust Center
  slug: amazon-fault-injection-simulator-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-fault-injection-simulator
tags:
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
use_cases:
- description: Validate application behavior under resource failures before they occur in production.
  name: Application Resilience Testing
- description: Run structured fault injection experiments following chaos engineering principles.
  name: Chaos Engineering
- description: Verify that monitoring and alerting systems detect and respond to failures correctly.
  name: Observability Validation
- description: Conduct planned game day exercises simulating failure scenarios for team readiness.
  name: Game Days
- description: Integrate resilience testing into CI/CD pipelines for continuous validation.
  name: Automated Pipeline Testing
- description: Test cross-region failover mechanisms and recovery time objectives.
  name: Multi-region Failover Testing
website: https://aws.amazon.com/fis/
---
