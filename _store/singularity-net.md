---
name: SingularityNET
description: SingularityNET is a decentralized AI services marketplace built on blockchain. Developers can publish AI services to the network and consumers can access them using the ASI (FET) token. The platform uses a daemon (snetd) that exposes AI applications as gRPC APIs accessible through the SingularityNET Network, with a REST API for marketplace interaction and service discovery.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/singularity-net/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Artificial Intelligence
  - Blockchain
  - Decentralized AI
  - AI Marketplace
  - Web3
apis:
  - name: SingularityNET Daemon API
    description: The SingularityNET Daemon (snetd) exposes an AI service as an API accessible through the SingularityNET Network. The daemon handles blockchain interaction for payment authorization using Multi-Party Escrow (MPE) contracts and routes API calls to the underlying AI service via gRPC.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dev.singularitynet.io/docs/products/DecentralizedAIPlatform/Daemon/daemon-api/
    baseURL: https://services.singularitynet.io
    tags:
      - AI Services
      - gRPC
      - Blockchain
      - Payment Channels
      - Daemon
    properties:
      - type: Documentation
        url: https://dev.singularitynet.io/docs/products/DecentralizedAIPlatform/Daemon/daemon-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/singularity-net/refs/heads/main/openapi/singularitynet-marketplace-openapi.yml
      - type: GitHubOrganization
        url: https://github.com/singnet
      - type: DaemonGitHub
        url: https://github.com/singnet/snet-daemon
      - type: PythonSDK
        url: https://github.com/singnet/snet-sdk-python
      - type: Authentication
        url: https://dev.singularitynet.io/docs/products/DecentralizedAIPlatform/SDK/sdk-concept/
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/singularity-net/refs/heads/main/rules/singularitynet-rules.yml
    contact:
      - FN: SingularityNET Foundation
        url: https://singularitynet.io
  - name: SingularityNET Marketplace API
    description: The SingularityNET AI Marketplace REST API provides service discovery, organization management, and metadata access for the decentralized AI network. Allows consumers to browse available AI services, retrieve service metadata, and access pricing information.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dev.singularitynet.io/docs/products/AIMarketplace/
    baseURL: https://marketplace.singularitynet.io
    tags:
      - AI Marketplace
      - Service Discovery
      - Organizations
      - Metadata
    properties:
      - type: Documentation
        url: https://dev.singularitynet.io/docs/products/AIMarketplace/
      - type: GitHubOrganization
        url: https://github.com/singnet
common:
  - type: GitHubOrganization
    url: https://github.com/singnet
  - type: DeveloperPortal
    url: https://dev.singularitynet.io
  - type: Documentation
    url: https://dev.singularitynet.io/docs/products/DecentralizedAIPlatform/
  - type: AIMarketplace
    url: https://marketplace.singularitynet.io
  - type: Whitepaper
    url: https://public.singularitynet.io/whitepaper.pdf
  - type: PythonSDK
    url: https://github.com/singnet/snet-sdk-python
  - type: DaemonGitHub
    url: https://github.com/singnet/snet-daemon
  - type: TermsOfService
    url: https://singularitynet.io/terms-of-service
  - type: PrivacyPolicy
    url: https://singularitynet.io/privacy-policy
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
---
