---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Ecr Agentic Access
  operation_count: 6
  slug: amazon-ecr-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Amazon ECR Amazon Elastic Container Registry (ECR) API API from Amazon ECR — 1 operation(s) for amazon ecr amazon elastic container registry (ecr) api.
  name: Amazon ECR Amazon ECR Amazon Elastic Container Registry (ECR) API
  slug: amazon-ecr-amazon-ecr-amazon-elastic-container-registry-ecr-api-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Lifecycle Policy API from Amazon ECR — 3 operation(s) for ecr lifecycle policy.
  name: Amazon ECR Ecr Lifecycle Policy API
  slug: amazon-ecr-lifecycle-policy-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Operations API from Amazon ECR — 29 operation(s) for ecr operations.
  name: Amazon ECR Ecr Operations API
  slug: amazon-ecr-operations-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Pull Through Cache Rule API from Amazon ECR — 5 operation(s) for ecr pull through cache rule.
  name: Amazon ECR Ecr Pull Through Cache Rule API
  slug: amazon-ecr-pull-through-cache-rule-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Pull Time Update Exclusion API from Amazon ECR — 3 operation(s) for ecr pull time update exclusion.
  name: Amazon ECR Ecr Pull Time Update Exclusion API
  slug: amazon-ecr-pull-time-update-exclusion-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Registry Policy API from Amazon ECR — 3 operation(s) for ecr registry policy.
  name: Amazon ECR Ecr Registry Policy API
  slug: amazon-ecr-registry-policy-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Replication Backfill API from Amazon ECR — 3 operation(s) for ecr replication backfill.
  name: Amazon ECR Ecr Replication Backfill API
  slug: amazon-ecr-replication-backfill-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Repository Creation Template API from Amazon ECR — 4 operation(s) for ecr repository creation template.
  name: Amazon ECR Ecr Repository Creation Template API
  slug: amazon-ecr-repository-creation-template-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Repository Policy API from Amazon ECR — 3 operation(s) for ecr repository policy.
  name: Amazon ECR Ecr Repository Policy API
  slug: amazon-ecr-repository-policy-api
- baseURL: https://api.ecr.amazonaws.com
  baseurl_source: declared
  description: The Ecr Signing Configuration API from Amazon ECR — 3 operation(s) for ecr signing configuration.
  name: Amazon ECR Ecr Signing Configuration API
  slug: amazon-ecr-signing-configuration-api
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
artifact_total: 59
collections:
- collection_type: postman
  name: Amazon ECR Amazon Elastic Container Registry (ECR) API
  slug: postman-amazon-ecr
- collection_type: open
  name: Amazon ECR Amazon Elastic Container Registry (ECR) Amazon ECR Amazon Elastic Container Registry (ECR) API API
  slug: open-amazon-ecr-amazon-ecr-amazon-elastic-container-registry-ecr-api-api
- collection_type: open
  name: 'Amazon ECR Amazon Elastic Container Registry (ECR) Amazon ECR Amazon Elastic Container Registry (ECR) API #BatchGetImage API'
  slug: open-amazon-ecr-batchgetimage-api
- collection_type: open
  name: 'Amazon ECR Amazon Elastic Container Registry (ECR) Amazon ECR Amazon Elastic Container Registry (ECR) API #DeleteRepository API'
  slug: open-amazon-ecr-deleterepository-api
- collection_type: open
  name: 'Amazon ECR Amazon Elastic Container Registry (ECR) Amazon ECR Amazon Elastic Container Registry (ECR) API #DescribeRepositories API'
  slug: open-amazon-ecr-describerepositories-api
- collection_type: open
  name: 'Amazon ECR Amazon Elastic Container Registry (ECR) Amazon ECR Amazon Elastic Container Registry (ECR) API #ListImages API'
  slug: open-amazon-ecr-listimages-api
- collection_type: open
  name: 'Amazon ECR Amazon Elastic Container Registry (ECR) Amazon ECR Amazon Elastic Container Registry (ECR) API #PutImage API'
  slug: open-amazon-ecr-putimage-api
- collection_type: open
  name: Amazon ECR Amazon Elastic Container Registry (ECR) API
  slug: open-amazon-ecr
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-ecr/plans/amazon-ecr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-ecr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-ecr/rate-limits/amazon-ecr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-ecr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-ecr/finops/amazon-ecr-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-ecr-finops.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/ecr/
- group: agent
  href: https://artifacts.apis.io/amazon-ecr/agentic-access/amazon-ecr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-ecr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-ecr/security/amazon-ecr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-ecr-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-ecr/security/amazon-ecr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ecr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-ecr/security/amazon-ecr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-ecr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-ecr/authentication/amazon-ecr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-ecr-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-ecr/overview
- group: design
  href: https://artifacts.apis.io/amazon-ecr/arazzo/amazon-ecr-decommission-repository-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-decommission-repository-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-ecr/arazzo/amazon-ecr-ensure-repository-and-seed-image-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-ensure-repository-and-seed-image-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-ecr/arazzo/amazon-ecr-image-inventory-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-image-inventory-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-ecr/arazzo/amazon-ecr-provision-repository-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-provision-repository-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-ecr/arazzo/amazon-ecr-publish-image-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-ecr-publish-image-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-ecr/arazzo/amazon-ecr-registry-audit-workflow.yml
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
  href: https://artifacts.apis.io/amazon-ecr/rules/amazon-ecr-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-ecr-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-ecr/vocabulary/amazon-ecr-vocabulary.yaml
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
- has_sources: true
  method: derived
  name: Amazon Ecr Finops
  primary_unit: gb
  service_category: ''
  slug: amazon-ecr-finops
  template: false
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
modified: '2026-09-16'
name: Amazon ECR
nav: Providers
network: true
overview: 'Amazon ECR publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Amazon ECR Amazon Elastic Container Registry (ECR) API, Ecr Lifecycle Policy API, Ecr Operations API, and 7 more. Tagged areas include Amazon Web Services, Container Images, Container Registry, Containers, and Docker.


  The Amazon ECR catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon ECR''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 29 more developer resources.'
plans:
- name: Amazon Ecr Plans Pricing
  plan_count: 4
  slug: amazon-ecr-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Amazon Ecr Rate Limits
  slug: amazon-ecr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon ECR — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-ecr-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Amazon ECR API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 17
  slug: amazon-ecr-spectral-rules
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.4
    catalog_earned_first_party: 12.0
    catalog_gap: 45.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 93.4
    contract_governance: 27.3
    contract_quality: 70.8
    developer_ergonomics: 65.5
    discoverability: 58.9
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 90.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-ecr/amazon-ecr-2026-06-20T171634.png
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
website: https://aws.amazon.com/ecr/
---
