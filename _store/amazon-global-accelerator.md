---
aid: amazon-global-accelerator
name: Amazon Global Accelerator
description: Amazon Global Accelerator is a networking service that improves the performance and availability of applications with local or global users. It provides static IP addresses that act as a fixed entry point to your applications and uses the AWS global network to optimize the path from users to applications, improving performance by up to 60%.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-global-accelerator/refs/heads/main/apis.yml
type: Index
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Availability
  - AWS
  - CDN
  - Global
  - Load Balancing
  - Networking
  - Performance
apis:
  - aid: amazon-global-accelerator:amazon-global-accelerator-api
    name: Amazon Global Accelerator API
    description: The Amazon Global Accelerator API enables programmatic access to create and manage accelerators, listeners, and endpoint groups. You can configure traffic routing, health checks, and client IP address preservation to optimize application performance across AWS Regions.
    humanURL: https://aws.amazon.com/global-accelerator/
    baseURL: https://globalaccelerator.amazonaws.com
    tags:
      - Global
      - Networking
      - Performance
      - Traffic Management
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html
      - type: OpenAPI
        url: openapi/amazon-global-accelerator-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/global-accelerator/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/global-accelerator/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/global-accelerator/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: JSONSchema
        url: json-schema/global-accelerator-accelerator-schema.json
      - type: JSONLD
        url: json-ld/amazon-global-accelerator-context.jsonld
common:
  - type: Portal
    url: https://console.aws.amazon.com/
  - type: Documentation
    url: https://docs.aws.amazon.com/global-accelerator/
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
    url: https://console.aws.amazon.com/globalaccelerator
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-global-accelerator-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-global-accelerator-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-global-accelerator-network-operations.yaml
  - type: Features
    data:
      - name: Static Anycast IP Addresses
        description: Provides two static IP addresses as fixed entry points to applications, simplifying DNS management and whitelisting.
      - name: AWS Global Network Routing
        description: Routes user traffic through the AWS global network backbone for up to 60% performance improvement over public internet.
      - name: Intelligent Traffic Distribution
        description: Automatically routes traffic to the closest healthy endpoint based on geography, health, and routing policies.
      - name: Health Checking
        description: Continuously monitors endpoint health and instantly reroutes traffic away from unhealthy endpoints.
      - name: Client IP Preservation
        description: Preserves the original client IP address for application endpoints that need it.
      - name: Custom Routing
        description: Enables deterministic routing of connections to specific EC2 instances using port mappings.
  - type: UseCases
    data:
      - name: Global Application Performance
        description: Improve latency and throughput for globally distributed users by routing through AWS edge locations.
      - name: Multi-Region Failover
        description: Automatically failover traffic to healthy endpoints across regions without DNS changes.
      - name: Gaming Applications
        description: Reduce latency for real-time gaming applications using the AWS global network.
  - type: Integrations
    data:
      - name: AWS Elastic Load Balancing
        description: Route traffic to Application, Network, or Classic Load Balancers as endpoints.
      - name: Amazon EC2
        description: Use EC2 instances directly as Global Accelerator endpoints.
      - name: Amazon CloudWatch
        description: Monitor accelerator metrics and set alarms for traffic and health status.
      - name: AWS CloudFormation
        description: Provision Global Accelerator resources using infrastructure templates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
