---
name: Amazon VPC
description: Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define, with complete control over IP addressing, subnets, routing, and network gateways.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/vpc/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon VPC API
    description: Core API for managing Amazon Virtual Private Cloud resources including VPCs, subnets, internet gateways, NAT gateways, route tables, and network ACLs. VPC operations are part of the Amazon EC2 API.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/vpc/
    baseURL: https://ec2.amazonaws.com
    tags:
      - AWS
      - Networking
      - Private Cloud
      - Security
      - Subnets
      - VPC
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-vpc.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/openapi/amazon-vpc-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-vpc-schema.json
      - type: JSONLD
        url: json-ld/amazon-vpc-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/vpc/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/vpc/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/vpc/faqs/
      - type: User Guide
        url: https://docs.aws.amazon.com/vpc/latest/userguide/
      - type: API Reference
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
      - type: CLI Reference
        url: https://docs.aws.amazon.com/cli/latest/reference/ec2/
      - type: Security
        url: https://docs.aws.amazon.com/vpc/latest/userguide/security.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/vpc/
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc/
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
    url: https://stackoverflow.com/questions/tagged/amazon-vpc
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://docs.aws.amazon.com/vpc/latest/userguide/security.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/rules/amazon-vpc-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/vocabulary/amazon-vpc-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/capabilities/amazon-vpc-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon VPC.
      - name: API Access
        description: Programmatic access to Amazon VPC resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon VPC to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Networking
  - Private Cloud
  - Security
  - Subnets
  - VPC
---
