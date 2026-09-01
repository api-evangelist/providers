---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Amazon Eks Agentic Access
  operation_count: 16
  slug: amazon-eks-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- description: Operations for managing EKS add-ons
  name: Amazon EKS Addons API
  slug: amazon-eks-addons-api
- description: Operations for managing EKS clusters
  name: Amazon EKS Clusters API
  slug: amazon-eks-clusters-api
- description: Operations for managing EKS Fargate profiles
  name: Amazon EKS Fargate Profiles API
  slug: amazon-eks-fargate-profiles-api
- description: Operations for managing EKS managed node groups
  name: Amazon EKS Node Groups API
  slug: amazon-eks-node-groups-api
artifact_total: 122
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EKS Addons API
  slug: open-amazon-eks-addons-api
- collection_type: open
  name: Amazon EKS Addons Clusters API
  slug: open-amazon-eks-clusters-api
- collection_type: open
  name: Amazon EKS Addons Fargate Profiles API
  slug: open-amazon-eks-fargate-profiles-api
- collection_type: open
  name: Amazon EKS Addons Node Groups API
  slug: open-amazon-eks-node-groups-api
- collection_type: open
  name: Amazon EKS API
  slug: open-amazon-eks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-eks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-eks-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-eks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-eks-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/eks/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- group: commercial
  title: ''
  type: Terms
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: Privacy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/containers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/eks/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-eks
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-eks-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-eks-vocabulary.yaml
description: Amazon Elastic Kubernetes Service (Amazon EKS) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. Amazon EKS runs upstream Kubernetes and is certified Kubernetes conformant, so you can use existing tools and plugins from partners and the Kubernetes community.
examples:
- key_count: 3
  name: Amazon Eks Cluster Example
  slug: amazon-eks-cluster-example
- key_count: 3
  name: Eks Openapi Addon Example
  slug: eks-openapi-addon-example
- key_count: 3
  name: Eks Openapi Cluster Example
  slug: eks-openapi-cluster-example
- key_count: 3
  name: Eks Openapi Create Addon Request Example
  slug: eks-openapi-create-addon-request-example
- key_count: 1
  name: Eks Openapi Create Addon Response Example
  slug: eks-openapi-create-addon-response-example
- key_count: 3
  name: Eks Openapi Create Cluster Request Example
  slug: eks-openapi-create-cluster-request-example
- key_count: 1
  name: Eks Openapi Create Cluster Response Example
  slug: eks-openapi-create-cluster-response-example
- key_count: 3
  name: Eks Openapi Create Fargate Profile Request Example
  slug: eks-openapi-create-fargate-profile-request-example
- key_count: 1
  name: Eks Openapi Create Fargate Profile Response Example
  slug: eks-openapi-create-fargate-profile-response-example
- key_count: 3
  name: Eks Openapi Create Nodegroup Request Example
  slug: eks-openapi-create-nodegroup-request-example
- key_count: 1
  name: Eks Openapi Create Nodegroup Response Example
  slug: eks-openapi-create-nodegroup-response-example
- key_count: 1
  name: Eks Openapi Delete Addon Response Example
  slug: eks-openapi-delete-addon-response-example
- key_count: 1
  name: Eks Openapi Delete Cluster Response Example
  slug: eks-openapi-delete-cluster-response-example
- key_count: 1
  name: Eks Openapi Delete Fargate Profile Response Example
  slug: eks-openapi-delete-fargate-profile-response-example
- key_count: 1
  name: Eks Openapi Delete Nodegroup Response Example
  slug: eks-openapi-delete-nodegroup-response-example
- key_count: 1
  name: Eks Openapi Describe Addon Response Example
  slug: eks-openapi-describe-addon-response-example
- key_count: 1
  name: Eks Openapi Describe Cluster Response Example
  slug: eks-openapi-describe-cluster-response-example
- key_count: 1
  name: Eks Openapi Describe Fargate Profile Response Example
  slug: eks-openapi-describe-fargate-profile-response-example
- key_count: 1
  name: Eks Openapi Describe Nodegroup Response Example
  slug: eks-openapi-describe-nodegroup-response-example
- key_count: 3
  name: Eks Openapi Fargate Profile Example
  slug: eks-openapi-fargate-profile-example
- key_count: 2
  name: Eks Openapi Fargate Profile Selector Example
  slug: eks-openapi-fargate-profile-selector-example
- key_count: 3
  name: Eks Openapi Kubernetes Network Config Response Example
  slug: eks-openapi-kubernetes-network-config-response-example
- key_count: 2
  name: Eks Openapi List Addons Response Example
  slug: eks-openapi-list-addons-response-example
- key_count: 2
  name: Eks Openapi List Clusters Response Example
  slug: eks-openapi-list-clusters-response-example
- key_count: 2
  name: Eks Openapi List Fargate Profiles Response Example
  slug: eks-openapi-list-fargate-profiles-response-example
- key_count: 2
  name: Eks Openapi List Nodegroups Response Example
  slug: eks-openapi-list-nodegroups-response-example
- key_count: 1
  name: Eks Openapi Logging Example
  slug: eks-openapi-logging-example
- key_count: 3
  name: Eks Openapi Nodegroup Example
  slug: eks-openapi-nodegroup-example
- key_count: 3
  name: Eks Openapi Nodegroup Scaling Config Example
  slug: eks-openapi-nodegroup-scaling-config-example
- key_count: 3
  name: Eks Openapi Vpc Config Response Example
  slug: eks-openapi-vpc-config-response-example
features:
- description: AWS manages the Kubernetes control plane across multiple Availability Zones with automatic upgrades.
  name: Managed Control Plane
- description: Automates cluster infrastructure management for compute, storage, and networking with machine learning optimization.
  name: EKS Auto Mode
- description: Connect on-premises and edge infrastructure to EKS clusters for unified management.
  name: EKS Hybrid Nodes
- description: Run Kubernetes pods on serverless compute without managing EC2 node groups.
  name: Fargate Integration
- description: Automate provisioning and lifecycle management of EC2 nodes for Kubernetes clusters.
  name: Managed Node Groups
- description: Deploy and manage Kubernetes clusters on customer-managed infrastructure including on-premises.
  name: EKS Anywhere
- description: Manage operational software add-ons like VPC CNI, CoreDNS, and kube-proxy through EKS.
  name: Add-Ons Management
finops:
- name: Amazon Eks Finops
  service_category: API
  slug: amazon-eks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-eks.png
json_schemas:
- name: Amazon EKS Cluster
  property_count: 13
  slug: amazon-eks-cluster
- name: Addon
  property_count: 9
  slug: eks-openapi-addon
- name: Cluster
  property_count: 13
  slug: eks-openapi-cluster
- name: CreateAddonRequest
  property_count: 5
  slug: eks-openapi-create-addon-request
- name: CreateAddonResponse
  property_count: 1
  slug: eks-openapi-create-addon-response
- name: CreateClusterRequest
  property_count: 7
  slug: eks-openapi-create-cluster-request
- name: CreateClusterResponse
  property_count: 1
  slug: eks-openapi-create-cluster-response
- name: CreateFargateProfileRequest
  property_count: 5
  slug: eks-openapi-create-fargate-profile-request
- name: CreateFargateProfileResponse
  property_count: 1
  slug: eks-openapi-create-fargate-profile-response
- name: CreateNodegroupRequest
  property_count: 9
  slug: eks-openapi-create-nodegroup-request
- name: CreateNodegroupResponse
  property_count: 1
  slug: eks-openapi-create-nodegroup-response
- name: DeleteAddonResponse
  property_count: 1
  slug: eks-openapi-delete-addon-response
- name: DeleteClusterResponse
  property_count: 1
  slug: eks-openapi-delete-cluster-response
- name: DeleteFargateProfileResponse
  property_count: 1
  slug: eks-openapi-delete-fargate-profile-response
- name: DeleteNodegroupResponse
  property_count: 1
  slug: eks-openapi-delete-nodegroup-response
- name: DescribeAddonResponse
  property_count: 1
  slug: eks-openapi-describe-addon-response
- name: DescribeClusterResponse
  property_count: 1
  slug: eks-openapi-describe-cluster-response
- name: DescribeFargateProfileResponse
  property_count: 1
  slug: eks-openapi-describe-fargate-profile-response
- name: DescribeNodegroupResponse
  property_count: 1
  slug: eks-openapi-describe-nodegroup-response
- name: FargateProfile
  property_count: 9
  slug: eks-openapi-fargate-profile
- name: FargateProfileSelector
  property_count: 2
  slug: eks-openapi-fargate-profile-selector
- name: KubernetesNetworkConfigResponse
  property_count: 3
  slug: eks-openapi-kubernetes-network-config-response
- name: ListAddonsResponse
  property_count: 2
  slug: eks-openapi-list-addons-response
- name: ListClustersResponse
  property_count: 2
  slug: eks-openapi-list-clusters-response
- name: ListFargateProfilesResponse
  property_count: 2
  slug: eks-openapi-list-fargate-profiles-response
- name: ListNodegroupsResponse
  property_count: 2
  slug: eks-openapi-list-nodegroups-response
- name: Logging
  property_count: 1
  slug: eks-openapi-logging
- name: NodegroupScalingConfig
  property_count: 3
  slug: eks-openapi-nodegroup-scaling-config
- name: Nodegroup
  property_count: 16
  slug: eks-openapi-nodegroup
- name: VpcConfigResponse
  property_count: 7
  slug: eks-openapi-vpc-config-response
json_structures:
- name: Amazon Eks Cluster Structure
  property_count: 13
  slug: amazon-eks-cluster-structure
- name: Eks Openapi Addon Structure
  property_count: 9
  slug: eks-openapi-addon-structure
- name: Eks Openapi Cluster Structure
  property_count: 13
  slug: eks-openapi-cluster-structure
- name: Eks Openapi Create Addon Request Structure
  property_count: 5
  slug: eks-openapi-create-addon-request-structure
- name: Eks Openapi Create Addon Response Structure
  property_count: 1
  slug: eks-openapi-create-addon-response-structure
- name: Eks Openapi Create Cluster Request Structure
  property_count: 7
  slug: eks-openapi-create-cluster-request-structure
- name: Eks Openapi Create Cluster Response Structure
  property_count: 1
  slug: eks-openapi-create-cluster-response-structure
- name: Eks Openapi Create Fargate Profile Request Structure
  property_count: 5
  slug: eks-openapi-create-fargate-profile-request-structure
- name: Eks Openapi Create Fargate Profile Response Structure
  property_count: 1
  slug: eks-openapi-create-fargate-profile-response-structure
- name: Eks Openapi Create Nodegroup Request Structure
  property_count: 9
  slug: eks-openapi-create-nodegroup-request-structure
- name: Eks Openapi Create Nodegroup Response Structure
  property_count: 1
  slug: eks-openapi-create-nodegroup-response-structure
- name: Eks Openapi Delete Addon Response Structure
  property_count: 1
  slug: eks-openapi-delete-addon-response-structure
- name: Eks Openapi Delete Cluster Response Structure
  property_count: 1
  slug: eks-openapi-delete-cluster-response-structure
- name: Eks Openapi Delete Fargate Profile Response Structure
  property_count: 1
  slug: eks-openapi-delete-fargate-profile-response-structure
- name: Eks Openapi Delete Nodegroup Response Structure
  property_count: 1
  slug: eks-openapi-delete-nodegroup-response-structure
- name: Eks Openapi Describe Addon Response Structure
  property_count: 1
  slug: eks-openapi-describe-addon-response-structure
- name: Eks Openapi Describe Cluster Response Structure
  property_count: 1
  slug: eks-openapi-describe-cluster-response-structure
- name: Eks Openapi Describe Fargate Profile Response Structure
  property_count: 1
  slug: eks-openapi-describe-fargate-profile-response-structure
- name: Eks Openapi Describe Nodegroup Response Structure
  property_count: 1
  slug: eks-openapi-describe-nodegroup-response-structure
- name: Eks Openapi Fargate Profile Selector Structure
  property_count: 2
  slug: eks-openapi-fargate-profile-selector-structure
- name: Eks Openapi Fargate Profile Structure
  property_count: 9
  slug: eks-openapi-fargate-profile-structure
- name: Eks Openapi Kubernetes Network Config Response Structure
  property_count: 3
  slug: eks-openapi-kubernetes-network-config-response-structure
- name: Eks Openapi List Addons Response Structure
  property_count: 2
  slug: eks-openapi-list-addons-response-structure
- name: Eks Openapi List Clusters Response Structure
  property_count: 2
  slug: eks-openapi-list-clusters-response-structure
- name: Eks Openapi List Fargate Profiles Response Structure
  property_count: 2
  slug: eks-openapi-list-fargate-profiles-response-structure
- name: Eks Openapi List Nodegroups Response Structure
  property_count: 2
  slug: eks-openapi-list-nodegroups-response-structure
- name: Eks Openapi Logging Structure
  property_count: 1
  slug: eks-openapi-logging-structure
- name: Eks Openapi Nodegroup Scaling Config Structure
  property_count: 3
  slug: eks-openapi-nodegroup-scaling-config-structure
- name: Eks Openapi Nodegroup Structure
  property_count: 16
  slug: eks-openapi-nodegroup-structure
- name: Eks Openapi Vpc Config Response Structure
  property_count: 7
  slug: eks-openapi-vpc-config-response-structure
jsonld:
- class_count: 30
  name: Amazon Eks Context
  property_count: 61
  slug: amazon-eks-context
layout: provider
modified: '2026-05-19'
name: Amazon EKS
nav: Providers
network: true
overview: 'Amazon EKS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Addons API, Clusters API, Fargate Profiles API, and 1 more. Tagged areas include Container Orchestration, Containers, EKS, and Kubernetes.


  The Amazon EKS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EKS''s developer surface includes developer portal, documentation, terms of service, privacy policy, support, engineering blog, GitHub presence, and 17 more developer resources.'
plans:
- name: Amazon Eks Plans Pricing
  plan_count: 1
  slug: amazon-eks-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Amazon Eks Rate Limits
  slug: amazon-eks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon EKS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-eks-jsonschema-spectral-rules
- effective_rule_count: 80
  extends:
  - spectral:oas
  name: Amazon EKS API Rules
  rule_count: 39
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 23
  slug: amazon-eks-spectral-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 61.2
    developer_ergonomics: 33.3
    discoverability: 42.6
    governance: 28.8
    operational_transparency: 52.6
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-eks/refs/heads/main/screenshots/amazon-eks-2026-06-20T171637.png
security:
- kind: domain-security
  name: Amazon Eks Domain Security
  slug: amazon-eks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Eks Vulnerability Disclosure
  slug: amazon-eks-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Eks Trust Center
  slug: amazon-eks-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-eks
tags:
- Container Orchestration
- Containers
- EKS
- Kubernetes
use_cases:
- description: Scale production-grade AI deployments with GPU nodes for distributed training and inference.
  name: Generative AI Applications
- description: Deploy and manage containerized microservices with Kubernetes-native service discovery and scaling.
  name: Microservices Architecture
- description: Standardized Kubernetes environments combining open source with AWS managed services.
  name: Internal Developer Platforms
- description: Unified Kubernetes management across AWS cloud and on-premises infrastructure.
  name: Hybrid Cloud Applications
- description: Scalable batch processing and streaming data workloads using Spark, Flink, or Ray.
  name: Data Processing Platforms
website: https://aws.amazon.com/eks/
---
