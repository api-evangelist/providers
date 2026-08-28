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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Lambda Agentic Access
  operation_count: 11
  slug: lambda-agentic-access
  summary_line: 11 operations · 5 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Operations for managing persistent storage file systems.
  name: Lambda File Systems API
  slug: lambda-file-systems-api
- description: Operations for listing available machine images.
  name: Lambda Images API
  slug: lambda-images-api
- description: Operations for listing available GPU instance types.
  name: Lambda Instance Types API
  slug: lambda-instance-types-api
- description: Operations for managing GPU cloud instances.
  name: Lambda Instances API
  slug: lambda-instances-api
- description: Operations for managing SSH keys.
  name: Lambda SSH Keys API
  slug: lambda-ssh-keys-api
artifact_total: 40
collections:
- collection_type: postman
  name: Lambda Cloud File Systems API
  slug: postman-lambda-file-systems-api
- collection_type: postman
  name: Lambda Cloud File Systems Images API
  slug: postman-lambda-images-api
- collection_type: postman
  name: Lambda Cloud File Systems Instance Types API
  slug: postman-lambda-instance-types-api
- collection_type: postman
  name: Lambda Cloud File Systems Instances API
  slug: postman-lambda-instances-api
- collection_type: postman
  name: Lambda Cloud File Systems SSH Keys API
  slug: postman-lambda-ssh-keys-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lambda Cloud API
  slug: open-lambda-cloud-api
- collection_type: open
  name: Lambda Cloud File Systems API
  slug: open-lambda-file-systems-api
- collection_type: open
  name: Lambda Cloud File Systems Images API
  slug: open-lambda-images-api
- collection_type: open
  name: Lambda Cloud File Systems Instance Types API
  slug: open-lambda-instance-types-api
- collection_type: open
  name: Lambda Cloud File Systems Instances API
  slug: open-lambda-instances-api
- collection_type: open
  name: Lambda Cloud File Systems SSH Keys API
  slug: open-lambda-ssh-keys-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lambda/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lambda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lambda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lambda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lambda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lambda-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://lambda.ai/cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lambda.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lambda.ai/public-cloud/on-demand/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.lambdalabs.com/api/v1/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://lambda.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://lambda.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lambda.ai
- group: operate
  title: ''
  type: Support
  url: https://support.lambdalabs.com/hc/en-us
- group: start
  title: ''
  type: Signup
  url: https://cloud.lambdalabs.com/sign-up
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/lambda-cloud-client/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LambdaLabsML
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lambda-cloud-api-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lambda-context.jsonld
created: '2025-01-07'
description: Lambda gives your team instant access to the compute you need to build and deploy Artificial Intelligence. Lambda Cloud provides on-demand GPU instances powered by NVIDIA A100, H100, and other high-performance GPUs for deep learning training and inference workloads.
features:
- On-demand GPU cloud instances (A100, H100)
- Persistent storage file systems
- SSH key management
- Jupyter notebook integration
- RESTful API with API key authentication
- Multiple region availability
- Pre-installed deep learning frameworks
finops:
- name: Lambda Finops
  service_category: API
  slug: lambda-finops
image: /assets/icons/lambda.png
json_schemas:
- name: Lambda Cloud API Resources
  property_count: 0
  slug: lambda-cloud-api
jsonld:
- class_count: 0
  name: Lambda Context
  property_count: 4
  slug: lambda-context
layout: provider
modified: '2026-05-19'
name: Lambda
nav: Providers
network: true
overview: 'Lambda publishes 5 APIs on the [APIs.io](https://apis.io/) network, including File Systems API, Images API, Instance Types API, and 2 more. Tagged areas include Artificial Intelligence, Cloud Computing, Compute, Deep Learning, and GPU.


  The Lambda catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lambda''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Lambda Plans Pricing
  plan_count: 3
  slug: lambda-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Lambda Rate Limits
  slug: lambda-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Lambda API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: lambda-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.7
  delta: 1.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.7
    developer_ergonomics: 69.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lambda/refs/heads/main/screenshots/lambda-2026-06-20T184249.png
security:
- kind: authentication
  name: Lambda Authentication
  slug: lambda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lambda Domain Security
  slug: lambda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lambda Vulnerability Disclosure
  slug: lambda-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lambda Trust Center
  slug: lambda-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017
slug: lambda
tags:
- Artificial Intelligence
- Cloud Computing
- Compute
- Deep Learning
- GPU
- Machine-Learning
use_cases:
- Training large language models and deep learning models
- Running GPU-accelerated inference workloads
- Provisioning ephemeral compute for ML experiments
- Managing persistent datasets across training runs
- Automating GPU infrastructure with CI/CD pipelines
website: https://lambda.ai/cloud
---
