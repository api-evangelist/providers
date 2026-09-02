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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-09-01'
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
artifact_total: 29
asyncapis:
- description: ''
  name: Amazon Web Services Aws Events
  slug: amazon-web-services-aws-events
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
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/
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
  url: https://health.aws.amazon.com/health/status
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amazon-web-services-aws-amazon-ec2-api-api-openapi.yml
- group: other
  title: ''
  type: WSDL
  url: wsdl/amazon-web-services-aws-amazon-s3.wsdl
- group: other
  title: ''
  type: WSDL
  url: wsdl/amazon-web-services-aws-amazon-sqs.wsdl
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-web-services-aws-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-web-services-aws-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-web-services-aws-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-web-services-aws-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-web-services-aws-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-web-services-aws-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-web-services-aws-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-web-services-aws-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-web-services-aws-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-web-services-aws-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/amazon-web-services-aws-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-web-services-aws-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-web-services-aws-cli.yml
- group: design
  title: ''
  type: Components
  url: components/amazon-web-services-aws-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/amazon-web-services-aws-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amazon-web-services-aws-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amazon-web-services-aws-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amazon-web-services-aws-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-web-services-aws-amazon-ec2-api-api-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/amazon-web-services-aws-example.json
- group: commercial
  title: ''
  type: FinOps
  url: finops/amazon-web-services-aws-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/aws/containers-roadmap
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
created: '2024-01-01'
description: 'Amazon Web Services is the cloud computing arm of Amazon and the largest public cloud provider in the world, offering more than 200 services across compute, storage, databases, networking, analytics, machine learning, security and developer tooling from data centers in dozens of Regions. Nearly every service is API-first: capacity is created, configured and destroyed through signed HTTPS calls, and the console, the AWS CLI and the CloudFormation and CDK toolchains are all clients of the same control plane. Requests are authenticated with AWS Signature Version 4 and authorized by IAM policy rather than by OAuth scope, versioned with a dated API version parameter instead of a URL path, and paginated uniformly with MaxResults and NextToken. Pricing is usage-based per service with a credit-capped Free Tier for new accounts rather than API request plans.'
examples:
- key_count: 8
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
mcp_servers:
- description: ''
  name: AWS MCP servers (hosted Knowledge MCP + 62 awslabs stdio servers)
  slug: aws-mcp-servers-hosted-knowledge-mcp-62-awslabs-stdio-servers
modified: '2026-09-01'
name: Amazon Web Services (AWS)
nav: Providers
network: true
overview: 'Amazon Web Services (AWS) publishes 1 API on the [APIs.io](https://apis.io/) network: Amazon EC2 API API. Tagged areas include Analytics, Artificial Intelligence, Cloud Computing, Computing, and Containers.


  The Amazon Web Services (AWS) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Amazon Web Services (AWS)''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, pricing, and 57 more developer resources.'
plans:
- name: Amazon Web Services Aws Plans Pricing
  plan_count: 2
  slug: amazon-web-services-aws-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
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
  band: exemplar
  composite: 79.2
  coverage:
    artifact_dirs: 33
    catalog_gap: 44.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 21.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 44.7
    contract_quality: 71.1
    developer_ergonomics: 90.5
    discoverability: 70.4
    governance: 44.7
    operational_transparency: 100.0
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-web-services-aws/refs/heads/main/screenshots/amazon-web-services-aws-2026-06-20T171847.png
security:
- kind: authentication
  name: Amazon Web Services Aws Authentication
  slug: amazon-web-services-aws-authentication
  summary_line: apiKey/custom-request-signing · 3 schemes
- kind: domain-security
  name: Amazon Web Services Aws Domain Security
  slug: amazon-web-services-aws-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Web Services Aws Vulnerability Disclosure
  slug: amazon-web-services-aws-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
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
- DevOps
- Infrastructure-as-a-Service
- Infrastructure
- Machine-Learning
- Networking
- Platform-as-a-Service
- Security
- Serverless
- Storage
use_cases:
- description: Use Amazon Web Services AWS to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/
---
