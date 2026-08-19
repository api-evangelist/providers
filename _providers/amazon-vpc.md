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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Vpc Agentic Access
  operation_count: 17
  slug: amazon-vpc-agentic-access
  summary_line: 17 operations
api_count: 6
apis:
- description: Operations for managing internet gateways that connect VPCs to the internet
  name: Amazon VPC Internet Gateways API
  slug: amazon-vpc-internet-gateways-api
- description: Operations for managing NAT gateways for outbound internet access from private subnets
  name: Amazon VPC NAT Gateways API
  slug: amazon-vpc-nat-gateways-api
- description: Operations for managing network access control lists for subnet-level traffic filtering
  name: Amazon VPC Network ACLs API
  slug: amazon-vpc-network-acls-api
- description: Operations for managing route tables and routes within a VPC
  name: Amazon VPC Route Tables API
  slug: amazon-vpc-route-tables-api
- description: Operations for creating and managing subnets within a VPC
  name: Amazon VPC Subnets API
  slug: amazon-vpc-subnets-api
- description: Operations for creating and managing Virtual Private Clouds
  name: Amazon VPC VPCs API
  slug: amazon-vpc-vpcs-api
artifact_total: 63
collections:
- collection_type: postman
  name: Amazon VPC Internet Gateways API
  slug: postman-amazon-vpc-internet-gateways-api
- collection_type: postman
  name: Amazon VPC Internet Gateways NAT Gateways API
  slug: postman-amazon-vpc-nat-gateways-api
- collection_type: postman
  name: Amazon VPC Internet Gateways Network ACLs API
  slug: postman-amazon-vpc-network-acls-api
- collection_type: postman
  name: Amazon VPC Internet Gateways Route Tables API
  slug: postman-amazon-vpc-route-tables-api
- collection_type: postman
  name: Amazon VPC Internet Gateways Subnets API
  slug: postman-amazon-vpc-subnets-api
- collection_type: postman
  name: Amazon VPC Internet Gateways VPCs API
  slug: postman-amazon-vpc-vpcs-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon VPC Internet Gateways API
  slug: open-amazon-vpc-internet-gateways-api
- collection_type: open
  name: Amazon VPC Internet Gateways NAT Gateways API
  slug: open-amazon-vpc-nat-gateways-api
- collection_type: open
  name: Amazon VPC Internet Gateways Network ACLs API
  slug: open-amazon-vpc-network-acls-api
- collection_type: open
  name: Amazon VPC Internet Gateways Route Tables API
  slug: open-amazon-vpc-route-tables-api
- collection_type: open
  name: Amazon VPC Internet Gateways Subnets API
  slug: open-amazon-vpc-subnets-api
- collection_type: open
  name: Amazon VPC Internet Gateways VPCs API
  slug: open-amazon-vpc-vpcs-api
- collection_type: open
  name: Amazon VPC API
  slug: open-amazon-vpc
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-vpc/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-vpc-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-vpc-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-vpc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-vpc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-vpc-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/vpc/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/vpc/
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
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/vpc/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-vpc
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/vpc/latest/userguide/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/rules/amazon-vpc-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/vocabulary/amazon-vpc-vocabulary.yaml
created: '2024-01-15'
description: Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define, with complete control over IP addressing, subnets, routing, and network gateways.
examples:
- key_count: 2
  name: Amazon Vpc Example
  slug: amazon-vpc-example
features:
- description: Automate operational tasks with Amazon VPC.
  name: Automation
- description: Programmatic access to Amazon VPC resources.
  name: API Access
finops:
- name: Amazon Vpc Finops
  service_category: API
  slug: amazon-vpc-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: CreateInternetGatewayResponse
  property_count: 1
  slug: amazon-vpc-create-internet-gateway-response
- name: CreateNatGatewayResponse
  property_count: 1
  slug: amazon-vpc-create-nat-gateway-response
- name: CreateRouteTableResponse
  property_count: 1
  slug: amazon-vpc-create-route-table-response
- name: CreateSubnetResponse
  property_count: 1
  slug: amazon-vpc-create-subnet-response
- name: CreateVpcResponse
  property_count: 1
  slug: amazon-vpc-create-vpc-response
- name: DescribeSubnetsResponse
  property_count: 2
  slug: amazon-vpc-describe-subnets-response
- name: DescribeVpcsResponse
  property_count: 2
  slug: amazon-vpc-describe-vpcs-response
- name: InternetGateway
  property_count: 4
  slug: amazon-vpc-internet-gateway
- name: NatGateway
  property_count: 8
  slug: amazon-vpc-nat-gateway
- name: RouteTable
  property_count: 6
  slug: amazon-vpc-route-table
- name: Amazon VPC
  property_count: 15
  slug: amazon-vpc
- name: Subnet
  property_count: 12
  slug: amazon-vpc-subnet
- name: Tag
  property_count: 2
  slug: amazon-vpc-tag
- name: Vpc
  property_count: 10
  slug: amazon-vpc-vpc
json_structures:
- name: Amazon Vpc Create Internet Gateway Response Structure
  property_count: 0
  slug: amazon-vpc-create-internet-gateway-response-structure
- name: Amazon Vpc Create Nat Gateway Response Structure
  property_count: 0
  slug: amazon-vpc-create-nat-gateway-response-structure
- name: Amazon Vpc Create Route Table Response Structure
  property_count: 0
  slug: amazon-vpc-create-route-table-response-structure
- name: Amazon Vpc Create Subnet Response Structure
  property_count: 0
  slug: amazon-vpc-create-subnet-response-structure
- name: Amazon Vpc Create Vpc Response Structure
  property_count: 0
  slug: amazon-vpc-create-vpc-response-structure
- name: Amazon Vpc Describe Subnets Response Structure
  property_count: 0
  slug: amazon-vpc-describe-subnets-response-structure
- name: Amazon Vpc Describe Vpcs Response Structure
  property_count: 0
  slug: amazon-vpc-describe-vpcs-response-structure
- name: Amazon Vpc Internet Gateway Structure
  property_count: 0
  slug: amazon-vpc-internet-gateway-structure
- name: Amazon Vpc Nat Gateway Structure
  property_count: 0
  slug: amazon-vpc-nat-gateway-structure
- name: Amazon Vpc Route Table Structure
  property_count: 0
  slug: amazon-vpc-route-table-structure
- name: Amazon Vpc Structure
  property_count: 0
  slug: amazon-vpc-structure
- name: Amazon Vpc Subnet Structure
  property_count: 0
  slug: amazon-vpc-subnet-structure
- name: Amazon Vpc Tag Structure
  property_count: 0
  slug: amazon-vpc-tag-structure
- name: Amazon Vpc Vpc Structure
  property_count: 0
  slug: amazon-vpc-vpc-structure
jsonld:
- class_count: 0
  name: Amazon Vpc Context
  property_count: 6
  slug: amazon-vpc-context
layout: provider
modified: '2026-05-19'
name: Amazon VPC
nav: Providers
network: true
overview: 'Amazon VPC publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Internet Gateways API, NAT Gateways API, Network ACLs API, and 3 more. Tagged areas include Networking, Private Cloud, Security, Subnets, and VPC.


  The Amazon VPC catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon VPC''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 19 more developer resources.'
plans:
- name: Amazon Vpc Plans Pricing
  plan_count: 3
  slug: amazon-vpc-plans-pricing
random_paper: 126
rate_limits:
- limit_count: 5
  name: Amazon Vpc Rate Limits
  slug: amazon-vpc-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amazon VPC API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-vpc-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Amazon VPC API Rules
  rule_count: 17
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 12
  slug: amazon-vpc-spectral-rules
score:
  band: strong
  composite: 55.0
  delta: -7.2
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 25.0
    contract_quality: 69.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/screenshots/amazon-vpc-2026-06-20T171843.png
security:
- kind: authentication
  name: Amazon Vpc Authentication
  slug: amazon-vpc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Vpc Domain Security
  slug: amazon-vpc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Vpc Vulnerability Disclosure
  slug: amazon-vpc-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Vpc Trust Center
  slug: amazon-vpc-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-vpc
tags:
- Networking
- Private Cloud
- Security
- Subnets
- VPC
use_cases:
- description: Use Amazon VPC to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/vpc/
---
