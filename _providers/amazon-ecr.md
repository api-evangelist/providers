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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Ecr Agentic Access
  operation_count: 6
  slug: amazon-ecr-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 6
apis:
- description: The Amazon ECR Amazon Elastic Container Registry (ECR) API API from Amazon ECR — 1 operation(s) for amazon ecr amazon elastic container registry (ecr) api.
  name: Amazon ECR Amazon ECR Amazon Elastic Container Registry (ECR) API API
  slug: amazon-ecr-amazon-ecr-amazon-elastic-container-registry-ecr-api-api
- description: 'The #BatchGetImage API from Amazon ECR — 1 operation(s) for #batchgetimage.'
  name: 'Amazon ECR #BatchGetImage API'
  slug: amazon-ecr-batchgetimage-api
- description: 'The #DeleteRepository API from Amazon ECR — 1 operation(s) for #deleterepository.'
  name: 'Amazon ECR #DeleteRepository API'
  slug: amazon-ecr-deleterepository-api
- description: 'The #DescribeRepositories API from Amazon ECR — 1 operation(s) for #describerepositories.'
  name: 'Amazon ECR #DescribeRepositories API'
  slug: amazon-ecr-describerepositories-api
- description: 'The #ListImages API from Amazon ECR — 1 operation(s) for #listimages.'
  name: 'Amazon ECR #ListImages API'
  slug: amazon-ecr-listimages-api
- description: 'The #PutImage API from Amazon ECR — 1 operation(s) for #putimage.'
  name: 'Amazon ECR #PutImage API'
  slug: amazon-ecr-putimage-api
arazzos:
- description: Inventory a repository's images, then delete it with a force branch when images remain.
  name: Amazon ECR Decommission Repository
  slug: amazon-ecr-decommission-repository-workflow
- description: Describe a repository, create it only when missing, then seed it with an image manifest.
  name: Amazon ECR Ensure Repository and Seed Image
  slug: amazon-ecr-ensure-repository-and-seed-image-workflow
- description: Describe a repository, list its image IDs with pagination, and fetch image detail.
  name: Amazon ECR Image Inventory
  slug: amazon-ecr-image-inventory-workflow
- description: Create a container repository, confirm it exists, and inspect its current images.
  name: Amazon ECR Provision Repository
  slug: amazon-ecr-provision-repository-workflow
- description: Confirm a repository exists, put an image manifest, then read the image back.
  name: Amazon ECR Publish Image
  slug: amazon-ecr-publish-image-workflow
- description: Page through every repository in a registry following the DescribeRepositories token loop.
  name: Amazon ECR Registry Audit
  slug: amazon-ecr-registry-audit-workflow
artifact_total: 49
collections:
- collection_type: postman
  name: Amazon ECR Amazon Elastic Container Registry (ECR) API
  slug: postman-amazon-ecr
- collection_type: open
  name: Amazon ECR Amazon Elastic Container Registry (ECR) API
  slug: open-amazon-ecr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-ecr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-ecr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ecr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-ecr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-ecr-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-ecr/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-decommission-repository-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-ensure-repository-and-seed-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-image-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-provision-repository-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-publish-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-registry-audit-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
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
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/
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
  url: https://status.aws.amazon.com/
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
  url: https://stackoverflow.com/questions/tagged/amazon-web-services
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
  url: rules/amazon-ecr-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-ecr-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy container images and artifacts. ECR eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure, and integrates with Amazon ECS and Amazon EKS for simplified development to production workflows.
examples:
- key_count: 3
  name: Amazon Ecr Repository Example
  slug: amazon-ecr-repository-example
- key_count: 1
  name: Ecr Openapi Create Repository Response Example
  slug: ecr-openapi-create-repository-response-example
- key_count: 2
  name: Ecr Openapi Describe Repositories Response Example
  slug: ecr-openapi-describe-repositories-response-example
- key_count: 3
  name: Ecr Openapi Repository Example
  slug: ecr-openapi-repository-example
features:
- description: Eliminate the need to operate your own container repositories or worry about scaling infrastructure.
  name: Fully Managed Registry
- description: Automated vulnerability assessment via Amazon Inspector integration for continuous image security.
  name: Image Vulnerability Scanning
- description: Automatically expire and delete images based on rules to reduce storage costs.
  name: Lifecycle Policies
- description: Replicate images to registries in other AWS accounts and regions for availability.
  name: Cross-Account Replication
- description: Store and manage OCI-compliant artifacts including Helm charts and SBOMs.
  name: OCI Artifact Support
- description: Sign and verify container images automatically without additional infrastructure.
  name: Image Signing
- description: Cache upstream public registry images in ECR for reduced egress costs and improved availability.
  name: Pull Through Cache
finops:
- name: Amazon Ecr Finops
  service_category: API
  slug: amazon-ecr-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon ECR Repository
  property_count: 12
  slug: amazon-ecr-repository
- name: CreateRepositoryResponse
  property_count: 1
  slug: ecr-openapi-create-repository-response
- name: DescribeRepositoriesResponse
  property_count: 2
  slug: ecr-openapi-describe-repositories-response
- name: Repository
  property_count: 8
  slug: ecr-openapi-repository
json_structures:
- name: Amazon Ecr Repository Structure
  property_count: 12
  slug: amazon-ecr-repository-structure
- name: Ecr Openapi Create Repository Response Structure
  property_count: 1
  slug: ecr-openapi-create-repository-response-structure
- name: Ecr Openapi Describe Repositories Response Structure
  property_count: 2
  slug: ecr-openapi-describe-repositories-response-structure
- name: Ecr Openapi Repository Structure
  property_count: 8
  slug: ecr-openapi-repository-structure
jsonld:
- class_count: 4
  name: Amazon Ecr Context
  property_count: 22
  slug: amazon-ecr-context
layout: provider
modified: '2026-05-19'
name: Amazon ECR
nav: Providers
network: true
overview: 'Amazon ECR publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Amazon ECR Amazon Elastic Container Registry (ECR) API API, #BatchGetImage API, #DeleteRepository API, and 3 more. Tagged areas include Amazon Web Services, Container Images, Container Registry, Containers, and Docker.


  The Amazon ECR catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon ECR''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 25 more developer resources.'
plans:
- name: Amazon Ecr Plans Pricing
  plan_count: 3
  slug: amazon-ecr-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 5
  name: Amazon Ecr Rate Limits
  slug: amazon-ecr-rate-limits
rules:
- name: Amazon ECR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-ecr-jsonschema-spectral-rules
- name: Amazon ECR API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 17
  slug: amazon-ecr-spectral-rules
score:
  band: exemplar
  composite: 69.2
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 76.2
    developer_ergonomics: 45.7
    discoverability: 66.7
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 69.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-ecr/refs/heads/main/screenshots/amazon-ecr-2026-06-20T171634.png
security:
- kind: authentication
  name: Amazon Ecr Authentication
  slug: amazon-ecr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Ecr Domain Security
  slug: amazon-ecr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ecr Vulnerability Disclosure
  slug: amazon-ecr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Ecr Trust Center
  slug: amazon-ecr-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-ecr
tags:
- Amazon Web Services
- Container Images
- Container Registry
- Containers
- Docker
- ECR
- OCI
use_cases:
- description: Store container images in ECR and deploy to ECS or EKS as part of automated pipelines.
  name: CI/CD Pipeline Integration
- description: Automated vulnerability scanning and image signing for security-compliant container deployments.
  name: Security and Compliance
- description: Replicate images across regions for low-latency pulls and improved resilience.
  name: Multi-Region Deployments
- description: Store Helm charts as OCI artifacts for Kubernetes application deployment management.
  name: Helm Chart Repository
- description: Manage image retention policies to keep registries clean and reduce storage costs.
  name: Image Lifecycle Management
website: https://aws.amazon.com/
---
