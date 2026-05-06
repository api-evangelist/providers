---
aid: amazon-managed-blockchain
name: Amazon Managed Blockchain
description: Amazon Managed Blockchain is a fully managed service that allows you to create and manage scalable blockchain networks using popular open-source frameworks such as Hyperledger Fabric and Ethereum. It eliminates the overhead required to create the network or join a public network, and automatically scales to meet the demands of thousands of applications running millions of transactions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Blockchain
  - Distributed Ledger
  - Hyperledger Fabric
  - Ethereum
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-blockchain/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-managed-blockchain:amazon-managed-blockchain-api
    name: Amazon Managed Blockchain API
    description: The Amazon Managed Blockchain API provides a fully managed service for creating and managing scalable blockchain networks using open-source frameworks such as Hyperledger Fabric and Ethereum. Covers 27 operations for networks, members, nodes, proposals, invitations, and accessors management.
    humanURL: https://aws.amazon.com/managed-blockchain/
    baseURL: https://managedblockchain.amazonaws.com
    tags:
      - Blockchain
      - Distributed Ledger
      - Hyperledger Fabric
      - Ethereum
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/managed-blockchain/
      - type: OpenAPI
        url: openapi/amazon-managed-blockchain-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/managed-blockchain/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/managed-blockchain/pricing/
      - type: FAQ
        url: https://aws.amazon.com/managed-blockchain/faqs/
      - type: JSONSchema
        url: json-schema/amazon-managed-blockchain-network-schema.json
      - type: JSON-LD
        url: json-ld/amazon-managed-blockchain-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/managed-blockchain/
  - type: Documentation
    url: https://docs.aws.amazon.com/managed-blockchain/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/managedblockchain/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-managed-blockchain-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-managed-blockchain-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/blockchain-network-operations.yaml
  - type: Features
    data:
      - name: Hyperledger Fabric Support
        description: Create permissioned blockchain networks using Hyperledger Fabric framework.
      - name: Ethereum Support
        description: Create and participate in public Ethereum networks.
      - name: Network Member Management
        description: Invite AWS accounts to join your network as members and manage their access.
      - name: Peer Node Management
        description: Create and manage peer nodes to participate in blockchain network transactions.
      - name: Proposal and Voting
        description: Create and vote on proposals to manage network configuration changes.
  - type: UseCases
    data:
      - name: Supply Chain Transparency
        description: Track products through supply chains with immutable blockchain records shared across organizations.
      - name: Financial Settlement
        description: Automate financial settlement processes with smart contracts on Hyperledger Fabric.
      - name: Healthcare Data Sharing
        description: Share patient data securely across healthcare providers using blockchain consent records.
      - name: Digital Asset Management
        description: Manage digital assets and NFTs on Ethereum through a fully managed blockchain service.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store blockchain application code and configuration in S3 buckets.
      - name: AWS KMS
        description: Encrypt blockchain network data using AWS Key Management Service.
      - name: Amazon CloudWatch
        description: Monitor blockchain node and network metrics in CloudWatch.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
