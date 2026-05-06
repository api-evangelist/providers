---
name: Amazon Direct Connect
description: AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services or to Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the region with which it is associated, providing reduced network costs, increased bandwidth throughput, and a more consistent network experience.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/directconnect/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Direct Connect API
    description: The AWS Direct Connect API provides programmatic access to create and manage dedicated network connections between your on-premises network and AWS, including connections, virtual interfaces, gateways, and link aggregation groups. Covers 63 operations for full lifecycle management of hybrid network connectivity.
    humanURL: https://aws.amazon.com/directconnect/
    baseURL: https://directconnect.amazonaws.com
    tags:
      - AWS
      - Dedicated Connection
      - Direct Connect
      - Hybrid Cloud
      - Networking
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/directconnect/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-direct-connect-openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/directconnect/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/directconnect/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/directconnect/faqs/
      - type: JSONSchema
        url: json-schema/amazon-direct-connect-connection-schema.json
      - type: JSONSchema
        url: json-schema/amazon-direct-connect-virtual-interface-schema.json
      - type: JSONSchema
        url: json-schema/amazon-direct-connect-direct-connect-gateway-schema.json
      - type: JSONSchema
        url: json-schema/amazon-direct-connect-lag-schema.json
      - type: JSONStructure
        url: json-structure/amazon-direct-connect-connection-structure.json
      - type: JSONStructure
        url: json-structure/amazon-direct-connect-virtual-interface-structure.json
      - type: JSON-LD
        url: json-ld/amazon-direct-connect-context.jsonld
      - type: Example
        url: examples/amazon-direct-connect-connection-example.json
      - type: Example
        url: examples/amazon-direct-connect-virtual-interface-example.json
      - type: Example
        url: examples/amazon-direct-connect-lag-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/directconnect/
  - type: Documentation
    url: https://docs.aws.amazon.com/directconnect/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/networking-and-content-delivery/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/directconnect/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-direct-connect
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-direct-connect-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-direct-connect-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/hybrid-network-connectivity.yaml
  - type: Features
    data:
      - name: Dedicated Physical Connections
        description: Provides dedicated private connectivity with consistent bandwidth from 50 Mbps to 100 Gbps directly to AWS data centers.
      - name: Private Virtual Interfaces
        description: Create private virtual interfaces for direct access to Amazon VPC without traversing the public internet.
      - name: Public Virtual Interfaces
        description: Create public virtual interfaces to access all AWS public services using private bandwidth.
      - name: Transit Virtual Interfaces
        description: Create transit virtual interfaces to connect to AWS Transit Gateway for centralized hub-and-spoke connectivity.
      - name: Direct Connect Gateways
        description: Use gateways to connect to multiple VPCs across different regions through a single Direct Connect connection.
      - name: Link Aggregation Groups
        description: Bundle multiple connections into a LAG to increase bandwidth and improve redundancy with active-active failover.
      - name: Hosted Connections
        description: Purchase sub-1G and 1G connections through Direct Connect partners for flexible capacity options.
      - name: MACsec Encryption
        description: Secure point-to-point Ethernet connections with 802.1AE MACsec encryption for data-in-transit security.
  - type: UseCases
    data:
      - name: Hybrid Cloud Connectivity
        description: Establish private, high-bandwidth connections between on-premises data centers and AWS for consistent hybrid workloads.
      - name: Data Migration
        description: Transfer large datasets to AWS efficiently using dedicated connections that offer higher throughput than internet-based transfers.
      - name: Latency-Sensitive Applications
        description: Run latency-sensitive applications that require consistent, predictable network performance to AWS services.
      - name: Compliance and Security
        description: Meet regulatory requirements that mandate private network connections rather than internet-based access to cloud resources.
      - name: Backup and Disaster Recovery
        description: Create reliable backup and DR connections to AWS for on-premises infrastructure with predictable bandwidth for replication.
  - type: Integrations
    data:
      - name: Amazon VPC
        description: Connect directly to private VPC subnets using private virtual interfaces without internet exposure.
      - name: AWS Transit Gateway
        description: Use transit virtual interfaces to connect multiple VPCs and VPNs through a single gateway hub.
      - name: AWS Direct Connect Partners
        description: Purchase hosted connections and virtual interfaces through AWS Direct Connect delivery partners worldwide.
      - name: AWS CloudFormation
        description: Automate Direct Connect resource provisioning using CloudFormation templates for infrastructure as code.
      - name: Amazon Route 53 Resolver
        description: Use Direct Connect for private DNS resolution between on-premises and AWS environments.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Dedicated Connection
  - Direct Connect
  - Hybrid Cloud
  - Networking
---
