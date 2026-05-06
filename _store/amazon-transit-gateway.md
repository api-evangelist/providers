---
name: Amazon Transit Gateway
description: Amazon Transit Gateway connects VPCs and on-premises networks through a central hub, simplifying network architecture and reducing operational complexity for large-scale cloud deployments.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/transit-gateway/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Transit Gateway REST API
    description: RESTful API for Amazon Transit Gateway operations including creating and managing transit gateways, VPC attachments, route tables, peering connections, and multicast domains.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/transit-gateway/
    baseURL: https://ec2.amazonaws.com
    tags:
      - AWS
      - Networking
      - Transit Gateway
      - VPC
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-tgw.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/openapi/amazon-transit-gateway-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-transit-gateway-schema.json
      - type: JSONLD
        url: json-ld/amazon-transit-gateway-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/transit-gateway/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/transit-gateway/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html
      - type: SDKs
        url: https://aws.amazon.com/tools/
      - type: StatusPage
        url: https://status.aws.amazon.com/
      - type: FAQ
        url: https://aws.amazon.com/transit-gateway/faqs/
      - type: Service Level Agreement
        url: https://aws.amazon.com/ec2/sla/
      - type: User Guide
        url: https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html
      - type: API Reference
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-tgw.html
      - type: Code Examples
        url: https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html
      - type: Security
        url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-security.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/transit-gateway/
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc/latest/tgw/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/networking-and-content-delivery/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/vpc/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Knowledge Center
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/aws-transit-gateway
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/rules/amazon-transit-gateway-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/vocabulary/amazon-transit-gateway-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/capabilities/amazon-transit-gateway-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon Transit Gateway.
      - name: API Access
        description: Programmatic access to Amazon Transit Gateway resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon Transit Gateway to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Cloud Networking
  - Network Hub
  - Networking
  - Transit Gateway
  - VPC
---
