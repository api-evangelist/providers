---
name: Amazon PrivateLink
description: AWS PrivateLink provides private connectivity between virtual private clouds (VPCs), AWS services, and your on-premises networks without exposing your traffic to the public internet. It makes it easy to connect services across different accounts and VPCs to simplify your network architecture while maintaining security and compliance.
url: https://raw.githubusercontent.com/api-evangelist/amazon-privatelink/refs/heads/main/apis.yml
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Networking
  - Private Connectivity
  - Security
  - VPC
  - Zero Trust
  - Endpoint Services
created: '2026-03-16'
modified: '2026-04-19'
apis:
  - name: AWS PrivateLink API
    description: The AWS PrivateLink API (part of Amazon EC2) provides programmatic access to create and manage VPC endpoint services, VPC endpoints, and endpoint connections for private AWS service connectivity without internet exposure.
    humanURL: https://aws.amazon.com/privatelink/
    baseURL: https://ec2.amazonaws.com
    tags:
      - Networking
      - Private Connectivity
      - VPC
      - Endpoint Services
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html
      - type: OpenAPI
        url: openapi/amazon-privatelink-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/privatelink/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/privatelink/pricing/
      - type: FAQ
        url: https://aws.amazon.com/privatelink/faqs/
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-quotas.html
common:
  - type: Portal
    url: https://aws.amazon.com/privatelink/
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc/latest/privatelink/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/networking-and-content-delivery/tag/aws-privatelink/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/vpc/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SpectralRules
    url: rules/amazon-privatelink-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/private-connectivity.yaml
  - type: Vocabulary
    url: vocabulary/amazon-privatelink-vocabulary.yaml
  - type: Features
    data:
      - name: Private VPC Endpoints
        description: Connect to AWS services and endpoint services without using public IP addresses or internet gateways.
      - name: VPC Endpoint Services
        description: Expose services running in your VPC to other VPCs and accounts using Network Load Balancers.
      - name: Interface Endpoints
        description: Elastic network interfaces with private IP addresses that serve as entry points for supported services.
      - name: Gateway Endpoints
        description: Route table targets for S3 and DynamoDB traffic without using internet gateways.
      - name: Cross-Account Connectivity
        description: Enable service consumers in other AWS accounts to access your endpoint services privately.
      - name: Acceptance Control
        description: Control which service consumers can connect to your endpoint service with acceptance required settings.
      - name: Private DNS
        description: Configure private DNS names for interface endpoints to simplify connectivity without code changes.
      - name: Endpoint Policies
        description: Control access to services through endpoint policy documents for fine-grained access control.
  - type: UseCases
    data:
      - name: SaaS Service Delivery
        description: Deliver SaaS services to customers privately without internet exposure using PrivateLink.
      - name: Microservices Private Connectivity
        description: Enable microservices in different VPCs or accounts to communicate privately.
      - name: Regulatory Compliance
        description: Meet compliance requirements by keeping data transfer off the public internet.
      - name: Third-Party Service Integration
        description: Connect to marketplace services and partner APIs without public internet routing.
      - name: On-Premises Private Access
        description: Access AWS services from on-premises networks via VPN or Direct Connect without public endpoints.
  - type: Integrations
    data:
      - name: AWS VPC
        description: PrivateLink endpoints live in VPC subnets and use VPC security groups for access control.
      - name: AWS Direct Connect
        description: Access endpoint services from on-premises via Direct Connect without internet routing.
      - name: AWS VPN
        description: Combine PrivateLink with Site-to-Site VPN for private access from on-premises.
      - name: AWS Network Load Balancer
        description: Back endpoint services with NLBs for high availability and automatic scaling.
      - name: AWS Marketplace
        description: Subscribe to AWS Marketplace services and connect privately using PrivateLink.
  - type: JSON-LD
    url: json-ld/amazon-privatelink-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-privatelink-accept-vpc-endpoint-connections-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-create-vpc-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-create-vpc-endpoint-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-create-vpc-endpoint-service-configuration-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-create-vpc-endpoint-service-configuration-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-delete-vpc-endpoint-service-configurations-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-delete-vpc-endpoints-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-describe-vpc-endpoint-connections-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-describe-vpc-endpoint-services-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-describe-vpc-endpoints-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-modify-vpc-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-modify-vpc-endpoint-service-configuration-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-reject-vpc-endpoint-connections-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-service-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-service-detail-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-vpc-endpoint-connection-schema.json
  - type: JSONSchema
    url: json-schema/amazon-privatelink-vpc-endpoint-schema.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-accept-vpc-endpoint-connections-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-create-vpc-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-create-vpc-endpoint-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-create-vpc-endpoint-service-configuration-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-create-vpc-endpoint-service-configuration-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-delete-vpc-endpoint-service-configurations-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-delete-vpc-endpoints-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-describe-vpc-endpoint-connections-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-describe-vpc-endpoint-services-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-describe-vpc-endpoints-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-modify-vpc-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-modify-vpc-endpoint-service-configuration-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-reject-vpc-endpoint-connections-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-service-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-service-detail-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-vpc-endpoint-connection-structure.json
  - type: JSONStructure
    url: json-structure/amazon-privatelink-vpc-endpoint-structure.json
  - type: Example
    url: examples/amazon-privatelink-accept-vpc-endpoint-connections-request-example.json
  - type: Example
    url: examples/amazon-privatelink-create-vpc-endpoint-request-example.json
  - type: Example
    url: examples/amazon-privatelink-create-vpc-endpoint-result-example.json
  - type: Example
    url: examples/amazon-privatelink-create-vpc-endpoint-service-configuration-request-example.json
  - type: Example
    url: examples/amazon-privatelink-create-vpc-endpoint-service-configuration-result-example.json
  - type: Example
    url: examples/amazon-privatelink-delete-vpc-endpoint-service-configurations-request-example.json
  - type: Example
    url: examples/amazon-privatelink-delete-vpc-endpoints-request-example.json
  - type: Example
    url: examples/amazon-privatelink-describe-vpc-endpoint-connections-result-example.json
  - type: Example
    url: examples/amazon-privatelink-describe-vpc-endpoint-services-result-example.json
  - type: Example
    url: examples/amazon-privatelink-describe-vpc-endpoints-result-example.json
  - type: Example
    url: examples/amazon-privatelink-modify-vpc-endpoint-request-example.json
  - type: Example
    url: examples/amazon-privatelink-modify-vpc-endpoint-service-configuration-request-example.json
  - type: Example
    url: examples/amazon-privatelink-modify-vpc-endpoint-service-permissions-request-example.json
  - type: Example
    url: examples/amazon-privatelink-reject-vpc-endpoint-connections-request-example.json
  - type: Example
    url: examples/amazon-privatelink-service-configuration-example.json
  - type: Example
    url: examples/amazon-privatelink-service-detail-example.json
  - type: Example
    url: examples/amazon-privatelink-vpc-endpoint-connection-example.json
  - type: Example
    url: examples/amazon-privatelink-vpc-endpoint-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-privatelink.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
