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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Fargate Agentic Access
  operation_count: 16
  slug: fargate-agentic-access
  summary_line: 16 operations · 16 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Operations for managing ECS clusters that host Fargate tasks and services, including cluster creation, configuration, and capacity provider association.
  name: AWS Fargate Clusters API
  slug: fargate-clusters-api
- description: Operations for registering and managing ECS task definitions with Fargate compatibility, including CPU, memory, network mode, and container configuration.
  name: AWS Fargate Task Definitions API
  slug: fargate-task-definitions-api
- description: Operations for running and managing individual Fargate tasks, including launching tasks, stopping tasks, and querying task status.
  name: AWS Fargate Tasks API
  slug: fargate-tasks-api
- description: 'The #X Amz Target=AmazonEC2ContainerServiceV20141113.CreateService API from AWS Fargate — 1 operation(s) for #x amz target=amazonec2containerservicev20141113.createservice.'
  name: 'AWS Fargate #X Amz Target=AmazonEC2ContainerServiceV20141113.CreateService API'
  slug: fargate-x-amz-target-amazonec2containerservicev20141113-createservice-api
- description: 'The #X Amz Target=AmazonEC2ContainerServiceV20141113.DeleteService API from AWS Fargate — 1 operation(s) for #x amz target=amazonec2containerservicev20141113.deleteservice.'
  name: 'AWS Fargate #X Amz Target=AmazonEC2ContainerServiceV20141113.DeleteService API'
  slug: fargate-x-amz-target-amazonec2containerservicev20141113-deleteservice-api
- description: 'The #X Amz Target=AmazonEC2ContainerServiceV20141113.DescribeServices API from AWS Fargate — 1 operation(s) for #x amz target=amazonec2containerservicev20141113.describeservices.'
  name: 'AWS Fargate #X Amz Target=AmazonEC2ContainerServiceV20141113.DescribeServices API'
  slug: fargate-x-amz-target-amazonec2containerservicev20141113-describeservices-api
- description: 'The #X Amz Target=AmazonEC2ContainerServiceV20141113.ListServices API from AWS Fargate — 1 operation(s) for #x amz target=amazonec2containerservicev20141113.listservices.'
  name: 'AWS Fargate #X Amz Target=AmazonEC2ContainerServiceV20141113.ListServices API'
  slug: fargate-x-amz-target-amazonec2containerservicev20141113-listservices-api
- description: 'The #X Amz Target=AmazonEC2ContainerServiceV20141113.UpdateService API from AWS Fargate — 1 operation(s) for #x amz target=amazonec2containerservicev20141113.updateservice.'
  name: 'AWS Fargate #X Amz Target=AmazonEC2ContainerServiceV20141113.UpdateService API'
  slug: fargate-x-amz-target-amazonec2containerservicev20141113-updateservice-api
artifact_total: 34
collections:
- collection_type: postman
  name: AWS Fargate Amazon ECS API (Fargate) Clusters API
  slug: postman-fargate-clusters-api
- collection_type: postman
  name: AWS Fargate Amazon ECS API (Fargate) Clusters Task Definitions API
  slug: postman-fargate-task-definitions-api
- collection_type: postman
  name: AWS Fargate Amazon ECS API (Fargate) Clusters Tasks API
  slug: postman-fargate-tasks-api
- collection_type: postman
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.CreateService API'
  slug: postman-fargate-x-amz-target-amazonec2containerservicev20141113-createservice-api
- collection_type: postman
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.DeleteService API'
  slug: postman-fargate-x-amz-target-amazonec2containerservicev20141113-deleteservice-api
- collection_type: postman
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.DescribeServices API'
  slug: postman-fargate-x-amz-target-amazonec2containerservicev20141113-describeservices-api
- collection_type: postman
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.ListServices API'
  slug: postman-fargate-x-amz-target-amazonec2containerservicev20141113-listservices-api
- collection_type: postman
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.UpdateService API'
  slug: postman-fargate-x-amz-target-amazonec2containerservicev20141113-updateservice-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Fargate Amazon ECS API (Fargate) Clusters API
  slug: open-fargate-clusters-api
- collection_type: open
  name: AWS Fargate Amazon ECS API (Fargate)
  slug: open-fargate-ecs
- collection_type: open
  name: AWS Fargate Amazon ECS API (Fargate) Clusters Task Definitions API
  slug: open-fargate-task-definitions-api
- collection_type: open
  name: AWS Fargate Amazon ECS API (Fargate) Clusters Tasks API
  slug: open-fargate-tasks-api
- collection_type: open
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.CreateService API'
  slug: open-fargate-x-amz-target-amazonec2containerservicev20141113-createservice-api
- collection_type: open
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.DeleteService API'
  slug: open-fargate-x-amz-target-amazonec2containerservicev20141113-deleteservice-api
- collection_type: open
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.DescribeServices API'
  slug: open-fargate-x-amz-target-amazonec2containerservicev20141113-describeservices-api
- collection_type: open
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.ListServices API'
  slug: open-fargate-x-amz-target-amazonec2containerservicev20141113-listservices-api
- collection_type: open
  name: 'AWS Fargate Amazon ECS API (Fargate) Clusters #X Amz Target=AmazonEC2ContainerServiceV20141113.UpdateService API'
  slug: open-fargate-x-amz-target-amazonec2containerservicev20141113-updateservice-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aws/containers-roadmap/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aws/containers-roadmap/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aws/containers-roadmap/blob/master/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-fargate/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fargate-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fargate-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fargate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fargate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fargate-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/fargate/
- group: docs
  title: ''
  type: Documentation
  url: https://aws.amazon.com/documentation-overview/fargate/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/fargate/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/fargate/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/fargate/faqs/
- group: other
  title: ''
  type: Customers
  url: https://aws.amazon.com/fargate/customers/
- group: company
  title: ''
  type: Partners
  url: https://aws.amazon.com/fargate/partners/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/ecs/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: build
  title: ''
  type: CLI
  url: https://aws.amazon.com/cli/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/category/compute/aws-fargate/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://aws.amazon.com/ecs/sla/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/tags/TAd-wgX2x3QgSxyelEN6raFg/amazon-elastic-container-service
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-fargate.html
- group: auth
  title: ''
  type: Security Whitepaper
  url: https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws-containers
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws/containers-roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-changelog.html
- group: operate
  title: ''
  type: Service Quotas
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
created: '2024-01-01'
description: AWS Fargate is a serverless, pay-as-you-go compute engine for containers that works with Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). It removes the need to provision and manage servers, letting you focus on building and running applications without managing infrastructure.
finops:
- name: Fargate Finops
  service_category: API
  slug: fargate-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
layout: provider
modified: '2026-05-19'
name: AWS Fargate
nav: Providers
network: true
overview: 'AWS Fargate publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Task Definitions API, Tasks API, and 5 more. Tagged areas include Compute, Containers, Docker, Kubernetes, and Serverless.


  AWS Fargate''s developer surface includes authentication, developer portal, documentation, pricing, getting-started guide, FAQ, developer console, and 26 more developer resources.'
plans:
- name: Fargate Plans Pricing
  plan_count: 3
  slug: fargate-plans-pricing
random_paper: 134
rate_limits:
- limit_count: 5
  name: Fargate Rate Limits
  slug: fargate-rate-limits
score:
  band: strong
  composite: 56.0
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 62.7
    developer_ergonomics: 69.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fargate/refs/heads/main/screenshots/fargate-2026-06-20T181042.png
security:
- kind: authentication
  name: Fargate Authentication
  slug: fargate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fargate Domain Security
  slug: fargate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fargate Vulnerability Disclosure
  slug: fargate-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fargate Trust Center
  slug: fargate-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: fargate
tags:
- Compute
- Containers
- Docker
- Kubernetes
- Serverless
website: https://aws.amazon.com/fargate/
---
