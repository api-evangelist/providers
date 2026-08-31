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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Web Services Aws Agentic Access
  operation_count: 1
  slug: amazon-web-services-aws-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Amazon Bedrock is a fully managed service that provides access to foundation models from leading AI companies for building generative AI applications.
  name: Amazon Bedrock API
  slug: amazon-bedrock-api
- description: Amazon Virtual Private Cloud lets you define and launch AWS resources in a logically isolated virtual network with full control over your networking environment.
  name: Amazon VPC API
  slug: amazon-vpc-api
- description: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and co
  name: Amazon Aurora API
  slug: amazon-aurora-api
- description: Amazon Elastic Block Store provides persistent block storage volumes for use with Amazon EC2 instances in the AWS Cloud.
  name: Amazon EBS API
  slug: amazon-ebs-api
- description: AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS removing the need to manage servers.
  name: AWS Fargate API
  slug: aws-fargate-api
- description: Amazon Keyspaces is a scalable, highly available, and managed Apache Cassandra-compatible database service for running Cassandra workloads in the cloud.
  name: Amazon Keyspaces API
  slug: amazon-keyspaces-api
- description: AWS Transit Gateway connects VPCs and on-premises networks through a central hub simplifying your network and putting an end to complex peering relationships.
  name: AWS Transit Gateway API
  slug: aws-transit-gateway-api
- description: The Amazon EC2 API API from Amazon Web Services (AWS) — 1 operation(s) for amazon ec2 api.
  name: Amazon Web Services (AWS) Amazon EC2 API API
  slug: amazon-web-services-aws-amazon-ec2-api-api
artifact_total: 27
collections:
- collection_type: postman
  name: Amazon EC2 Amazon EC2 API API
  slug: postman-amazon-web-services-aws-amazon-ec2-api-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EC2 Amazon EC2 API API
  slug: open-amazon-web-services-aws-amazon-ec2-api-api
- collection_type: open
  name: Amazon EC2 API
  slug: open-amazon-web-services-aws
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-web-services-aws-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-web-services-aws/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-web-services-aws-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-web-services-aws-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-web-services-aws-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-web-services-aws-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-web-services-aws-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/pricing/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/
- group: company
  title: ''
  type: About
  url: https://aws.amazon.com/what-is-aws/
- group: start
  title: ''
  type: Signup
  url: https://aws.amazon.com/free/
- group: build
  title: ''
  type: CLI
  url: https://aws.amazon.com/cli/
- group: other
  title: ''
  type: Whitepapers
  url: https://aws.amazon.com/whitepapers/
- group: other
  title: ''
  type: Architecture
  url: https://aws.amazon.com/architecture/
- group: other
  title: ''
  type: Marketplace
  url: https://aws.amazon.com/marketplace/
- group: company
  title: ''
  type: Partners
  url: https://aws.amazon.com/partners/
- group: learn
  title: ''
  type: Training
  url: https://aws.amazon.com/training/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: other
  title: ''
  type: Open Source
  url: https://aws.amazon.com/opensource/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/aws
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-web-services-aws/refs/heads/main/rules/amazon-web-services-aws-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-web-services-aws/refs/heads/main/vocabulary/amazon-web-services-aws-vocabulary.yaml
created: '2024'
description: Amazon Web Services offers reliable, scalable, and inexpensive cloud computing services. Free to join, pay only for what you use.
examples:
- key_count: 2
  name: Amazon Web Services Aws Example
  slug: amazon-web-services-aws-example
features:
- description: Automate operational tasks with Amazon Web Services AWS.
  name: Automation
- description: Programmatic access to Amazon Web Services AWS resources.
  name: API Access
finops:
- name: Amazon Web Services Aws Finops
  service_category: API
  slug: amazon-web-services-aws-finops
graphqls:
- description: AWS AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint for data querying, updating, and publishing.
  name: Amazon Web Services (AWS) GraphQL API
  slug: amazon-web-services-aws-graphql
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
jsonld:
- class_count: 0
  name: Amazon Web Services Aws Context
  property_count: 0
  slug: amazon-web-services-aws-context
layout: provider
modified: '2026-04-19'
name: Amazon Web Services (AWS)
nav: Providers
network: true
overview: 'Amazon Web Services (AWS) publishes 1 API on the [APIs.io](https://apis.io/) network: Amazon EC2 API API. Tagged areas include Analytics, Artificial Intelligence, Cloud Computing, Computing, and Containers.


  The Amazon Web Services (AWS) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Web Services (AWS)''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, pricing, and 26 more developer resources.'
plans:
- name: Amazon Web Services Aws Plans Pricing
  plan_count: 3
  slug: amazon-web-services-aws-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Amazon Web Services Aws Rate Limits
  slug: amazon-web-services-aws-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Amazon Web Services (AWS) API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 7
  slug: amazon-web-services-aws-spectral-rules
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 26.5
    contract_quality: 60.5
    developer_ergonomics: 76.2
    discoverability: 61.1
    governance: 26.5
    operational_transparency: 39.5
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-web-services-aws/refs/heads/main/screenshots/amazon-web-services-aws-2026-06-20T171847.png
security:
- kind: authentication
  name: Amazon Web Services Aws Authentication
  slug: amazon-web-services-aws-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Web Services Aws Domain Security
  slug: amazon-web-services-aws-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Web Services Aws Vulnerability Disclosure
  slug: amazon-web-services-aws-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Web Services Aws Trust Center
  slug: amazon-web-services-aws-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-web-services-aws
tags:
- Analytics
- Artificial Intelligence
- Cloud Computing
- Computing
- Containers
- Databases
- Devops
- Iaas
- Infrastructure
- Machine-Learning
- Networking
- Paas
- Platform As A Service
- Security
- Serverless
- Storage
use_cases:
- description: Use Amazon Web Services AWS to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/
---
