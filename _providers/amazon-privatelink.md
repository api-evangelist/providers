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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Amazon Privatelink Agentic Access
  operation_count: 13
  slug: amazon-privatelink-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 4
apis:
- description: Endpoint connection management
  name: Amazon PrivateLink Endpoint Connections API
  slug: amazon-privatelink-endpoint-connections-api
- description: VPC endpoint services (provider side)
  name: Amazon PrivateLink Endpoint Services API
  slug: amazon-privatelink-endpoint-services-api
- description: Endpoint service principal management
  name: Amazon PrivateLink Principals API
  slug: amazon-privatelink-principals-api
- description: VPC endpoints (consumer side)
  name: Amazon PrivateLink VPC Endpoints API
  slug: amazon-privatelink-vpc-endpoints-api
artifact_total: 82
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-privatelink-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-privatelink-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-privatelink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-privatelink-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-privatelink-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/privatelink/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/vpc/latest/privatelink/
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
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/tag/aws-privatelink/
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
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-privatelink-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-privatelink-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-privatelink-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-accept-vpc-endpoint-connections-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-create-vpc-endpoint-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-create-vpc-endpoint-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-create-vpc-endpoint-service-configuration-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-create-vpc-endpoint-service-configuration-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-delete-vpc-endpoint-service-configurations-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-delete-vpc-endpoints-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-describe-vpc-endpoint-connections-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-describe-vpc-endpoint-services-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-describe-vpc-endpoints-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-modify-vpc-endpoint-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-modify-vpc-endpoint-service-configuration-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-reject-vpc-endpoint-connections-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-service-configuration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-service-detail-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-vpc-endpoint-connection-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-privatelink-vpc-endpoint-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-accept-vpc-endpoint-connections-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-create-vpc-endpoint-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-create-vpc-endpoint-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-create-vpc-endpoint-service-configuration-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-create-vpc-endpoint-service-configuration-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-delete-vpc-endpoint-service-configurations-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-delete-vpc-endpoints-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-describe-vpc-endpoint-connections-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-describe-vpc-endpoint-services-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-describe-vpc-endpoints-result-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-modify-vpc-endpoint-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-modify-vpc-endpoint-service-configuration-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-reject-vpc-endpoint-connections-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-service-configuration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-service-detail-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-vpc-endpoint-connection-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-privatelink-vpc-endpoint-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-accept-vpc-endpoint-connections-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-create-vpc-endpoint-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-create-vpc-endpoint-result-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-create-vpc-endpoint-service-configuration-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-create-vpc-endpoint-service-configuration-result-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-delete-vpc-endpoint-service-configurations-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-delete-vpc-endpoints-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-describe-vpc-endpoint-connections-result-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-describe-vpc-endpoint-services-result-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-describe-vpc-endpoints-result-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-modify-vpc-endpoint-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-modify-vpc-endpoint-service-configuration-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-reject-vpc-endpoint-connections-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-service-configuration-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-service-detail-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-vpc-endpoint-connection-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-privatelink-vpc-endpoint-example.json
created: '2026-03-16'
description: AWS PrivateLink provides private connectivity between virtual private clouds (VPCs), AWS services, and your on-premises networks without exposing your traffic to the public internet. It makes it easy to connect services across different accounts and VPCs to simplify your network architecture while maintaining security and compliance.
examples:
- key_count: 2
  name: Amazon Privatelink Accept Vpc Endpoint Connections Request Example
  slug: amazon-privatelink-accept-vpc-endpoint-connections-request-example
- key_count: 7
  name: Amazon Privatelink Create Vpc Endpoint Request Example
  slug: amazon-privatelink-create-vpc-endpoint-request-example
- key_count: 1
  name: Amazon Privatelink Create Vpc Endpoint Result Example
  slug: amazon-privatelink-create-vpc-endpoint-result-example
- key_count: 4
  name: Amazon Privatelink Create Vpc Endpoint Service Configuration Request Example
  slug: amazon-privatelink-create-vpc-endpoint-service-configuration-request-example
- key_count: 1
  name: Amazon Privatelink Create Vpc Endpoint Service Configuration Result Example
  slug: amazon-privatelink-create-vpc-endpoint-service-configuration-result-example
- key_count: 1
  name: Amazon Privatelink Delete Vpc Endpoint Service Configurations Request Example
  slug: amazon-privatelink-delete-vpc-endpoint-service-configurations-request-example
- key_count: 1
  name: Amazon Privatelink Delete Vpc Endpoints Request Example
  slug: amazon-privatelink-delete-vpc-endpoints-request-example
- key_count: 2
  name: Amazon Privatelink Describe Vpc Endpoint Connections Result Example
  slug: amazon-privatelink-describe-vpc-endpoint-connections-result-example
- key_count: 3
  name: Amazon Privatelink Describe Vpc Endpoint Services Result Example
  slug: amazon-privatelink-describe-vpc-endpoint-services-result-example
- key_count: 2
  name: Amazon Privatelink Describe Vpc Endpoints Result Example
  slug: amazon-privatelink-describe-vpc-endpoints-result-example
- key_count: 3
  name: Amazon Privatelink Modify Vpc Endpoint Request Example
  slug: amazon-privatelink-modify-vpc-endpoint-request-example
- key_count: 3
  name: Amazon Privatelink Modify Vpc Endpoint Service Configuration Request Example
  slug: amazon-privatelink-modify-vpc-endpoint-service-configuration-request-example
- key_count: 3
  name: Amazon Privatelink Modify Vpc Endpoint Service Permissions Request Example
  slug: amazon-privatelink-modify-vpc-endpoint-service-permissions-request-example
- key_count: 2
  name: Amazon Privatelink Reject Vpc Endpoint Connections Request Example
  slug: amazon-privatelink-reject-vpc-endpoint-connections-request-example
- key_count: 8
  name: Amazon Privatelink Service Configuration Example
  slug: amazon-privatelink-service-configuration-example
- key_count: 8
  name: Amazon Privatelink Service Detail Example
  slug: amazon-privatelink-service-detail-example
- key_count: 5
  name: Amazon Privatelink Vpc Endpoint Connection Example
  slug: amazon-privatelink-vpc-endpoint-connection-example
- key_count: 9
  name: Amazon Privatelink Vpc Endpoint Example
  slug: amazon-privatelink-vpc-endpoint-example
features:
- description: Connect to AWS services and endpoint services without using public IP addresses or internet gateways.
  name: Private VPC Endpoints
- description: Expose services running in your VPC to other VPCs and accounts using Network Load Balancers.
  name: VPC Endpoint Services
- description: Elastic network interfaces with private IP addresses that serve as entry points for supported services.
  name: Interface Endpoints
- description: Route table targets for S3 and DynamoDB traffic without using internet gateways.
  name: Gateway Endpoints
- description: Enable service consumers in other AWS accounts to access your endpoint services privately.
  name: Cross-Account Connectivity
- description: Control which service consumers can connect to your endpoint service with acceptance required settings.
  name: Acceptance Control
- description: Configure private DNS names for interface endpoints to simplify connectivity without code changes.
  name: Private DNS
- description: Control access to services through endpoint policy documents for fine-grained access control.
  name: Endpoint Policies
finops:
- name: Amazon Privatelink Finops
  service_category: API
  slug: amazon-privatelink-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AcceptVpcEndpointConnectionsRequest
  property_count: 2
  slug: amazon-privatelink-accept-vpc-endpoint-connections-request
- name: CreateVpcEndpointRequest
  property_count: 7
  slug: amazon-privatelink-create-vpc-endpoint-request
- name: CreateVpcEndpointResult
  property_count: 1
  slug: amazon-privatelink-create-vpc-endpoint-result
- name: CreateVpcEndpointServiceConfigurationRequest
  property_count: 4
  slug: amazon-privatelink-create-vpc-endpoint-service-configuration-request
- name: CreateVpcEndpointServiceConfigurationResult
  property_count: 1
  slug: amazon-privatelink-create-vpc-endpoint-service-configuration-result
- name: DeleteVpcEndpointServiceConfigurationsRequest
  property_count: 1
  slug: amazon-privatelink-delete-vpc-endpoint-service-configurations-request
- name: DeleteVpcEndpointsRequest
  property_count: 1
  slug: amazon-privatelink-delete-vpc-endpoints-request
- name: DescribeVpcEndpointConnectionsResult
  property_count: 2
  slug: amazon-privatelink-describe-vpc-endpoint-connections-result
- name: DescribeVpcEndpointServicesResult
  property_count: 3
  slug: amazon-privatelink-describe-vpc-endpoint-services-result
- name: DescribeVpcEndpointsResult
  property_count: 2
  slug: amazon-privatelink-describe-vpc-endpoints-result
- name: ModifyVpcEndpointRequest
  property_count: 3
  slug: amazon-privatelink-modify-vpc-endpoint-request
- name: ModifyVpcEndpointServiceConfigurationRequest
  property_count: 3
  slug: amazon-privatelink-modify-vpc-endpoint-service-configuration-request
- name: ModifyVpcEndpointServicePermissionsRequest
  property_count: 3
  slug: amazon-privatelink-modify-vpc-endpoint-service-permissions-request
- name: RejectVpcEndpointConnectionsRequest
  property_count: 2
  slug: amazon-privatelink-reject-vpc-endpoint-connections-request
- name: ServiceConfiguration
  property_count: 8
  slug: amazon-privatelink-service-configuration
- name: ServiceDetail
  property_count: 8
  slug: amazon-privatelink-service-detail
- name: VpcEndpointConnection
  property_count: 5
  slug: amazon-privatelink-vpc-endpoint-connection
- name: VpcEndpoint
  property_count: 9
  slug: amazon-privatelink-vpc-endpoint
json_structures:
- name: Amazon Privatelink Accept Vpc Endpoint Connections Request Structure
  property_count: 2
  slug: amazon-privatelink-accept-vpc-endpoint-connections-request-structure
- name: Amazon Privatelink Create Vpc Endpoint Request Structure
  property_count: 7
  slug: amazon-privatelink-create-vpc-endpoint-request-structure
- name: Amazon Privatelink Create Vpc Endpoint Result Structure
  property_count: 1
  slug: amazon-privatelink-create-vpc-endpoint-result-structure
- name: Amazon Privatelink Create Vpc Endpoint Service Configuration Request Structure
  property_count: 4
  slug: amazon-privatelink-create-vpc-endpoint-service-configuration-request-structure
- name: Amazon Privatelink Create Vpc Endpoint Service Configuration Result Structure
  property_count: 1
  slug: amazon-privatelink-create-vpc-endpoint-service-configuration-result-structure
- name: Amazon Privatelink Delete Vpc Endpoint Service Configurations Request Structure
  property_count: 1
  slug: amazon-privatelink-delete-vpc-endpoint-service-configurations-request-structure
- name: Amazon Privatelink Delete Vpc Endpoints Request Structure
  property_count: 1
  slug: amazon-privatelink-delete-vpc-endpoints-request-structure
- name: Amazon Privatelink Describe Vpc Endpoint Connections Result Structure
  property_count: 2
  slug: amazon-privatelink-describe-vpc-endpoint-connections-result-structure
- name: Amazon Privatelink Describe Vpc Endpoint Services Result Structure
  property_count: 3
  slug: amazon-privatelink-describe-vpc-endpoint-services-result-structure
- name: Amazon Privatelink Describe Vpc Endpoints Result Structure
  property_count: 2
  slug: amazon-privatelink-describe-vpc-endpoints-result-structure
- name: Amazon Privatelink Modify Vpc Endpoint Request Structure
  property_count: 3
  slug: amazon-privatelink-modify-vpc-endpoint-request-structure
- name: Amazon Privatelink Modify Vpc Endpoint Service Configuration Request Structure
  property_count: 3
  slug: amazon-privatelink-modify-vpc-endpoint-service-configuration-request-structure
- name: Amazon Privatelink Modify Vpc Endpoint Service Permissions Request Structure
  property_count: 3
  slug: amazon-privatelink-modify-vpc-endpoint-service-permissions-request-structure
- name: Amazon Privatelink Reject Vpc Endpoint Connections Request Structure
  property_count: 2
  slug: amazon-privatelink-reject-vpc-endpoint-connections-request-structure
- name: Amazon Privatelink Service Configuration Structure
  property_count: 8
  slug: amazon-privatelink-service-configuration-structure
- name: Amazon Privatelink Service Detail Structure
  property_count: 8
  slug: amazon-privatelink-service-detail-structure
- name: Amazon Privatelink Vpc Endpoint Connection Structure
  property_count: 5
  slug: amazon-privatelink-vpc-endpoint-connection-structure
- name: Amazon Privatelink Vpc Endpoint Structure
  property_count: 9
  slug: amazon-privatelink-vpc-endpoint-structure
jsonld:
- class_count: 18
  name: Amazon Privatelink Context
  property_count: 34
  slug: amazon-privatelink-context
layout: provider
modified: '2026-05-19'
name: Amazon PrivateLink
nav: Providers
network: true
overview: 'Amazon PrivateLink publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Endpoint Connections API, Endpoint Services API, Principals API, and 1 more. Tagged areas include Networking, Private Connectivity, Security, VPC, and Zero Trust.


  The Amazon PrivateLink catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon PrivateLink''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 65 more developer resources.'
plans:
- name: Amazon Privatelink Plans Pricing
  plan_count: 3
  slug: amazon-privatelink-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Amazon Privatelink Rate Limits
  slug: amazon-privatelink-rate-limits
rules:
- name: Amazon PrivateLink API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-privatelink-jsonschema-spectral-rules
- name: Amazon PrivateLink API Rules
  rule_count: 22
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 10
  slug: amazon-privatelink-spectral-rules
score:
  band: strong
  composite: 65.3
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 64.6
    developer_ergonomics: 41.3
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 65.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-privatelink/refs/heads/main/screenshots/amazon-privatelink-2026-06-20T171800.png
security:
- kind: authentication
  name: Amazon Privatelink Authentication
  slug: amazon-privatelink-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Privatelink Domain Security
  slug: amazon-privatelink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Privatelink Vulnerability Disclosure
  slug: amazon-privatelink-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Privatelink Trust Center
  slug: amazon-privatelink-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-privatelink
tags:
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
use_cases:
- description: Deliver SaaS services to customers privately without internet exposure using PrivateLink.
  name: SaaS Service Delivery
- description: Enable microservices in different VPCs or accounts to communicate privately.
  name: Microservices Private Connectivity
- description: Meet compliance requirements by keeping data transfer off the public internet.
  name: Regulatory Compliance
- description: Connect to marketplace services and partner APIs without public internet routing.
  name: Third-Party Service Integration
- description: Access AWS services from on-premises networks via VPN or Direct Connect without public endpoints.
  name: On-Premises Private Access
website: https://aws.amazon.com/privatelink/
---
