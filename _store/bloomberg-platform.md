---
aid: bloomberg-platform
name: Bloomberg Platform
description: The Bloomberg Platform is the integrated technology infrastructure underpinning all Bloomberg professional products and services. It encompasses the data distribution network, cloud and on-premises deployment options, API connectivity layer, identity and access management, and enterprise integration capabilities that connect Bloomberg data and analytics to client systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-platform/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Platform
  - Infrastructure
  - Data Distribution
  - API Gateway
  - Integration
  - Bloomberg
apis:
  - aid: bloomberg-platform:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: The foundational API layer of the Bloomberg Platform providing real-time, reference, and historical data access through a socket-based protocol with SDKs for multiple programming languages.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - Core API
      - Market Data
      - Platform API
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
      - type: GitHubRepository
        url: https://github.com/bloomberg/blpapi-node
  - aid: bloomberg-platform:bloomberg-cloud-api
    name: Bloomberg Cloud Connect
    description: Cloud-native connectivity to Bloomberg data enabling access from AWS, Azure, and Google Cloud environments without on-premises Bloomberg infrastructure.
    humanURL: https://www.bloomberg.com/professional/solution/cloud/
    baseURL: https://api.bloomberg.com/cloud
    tags:
      - Cloud
      - AWS
      - Azure
      - Google Cloud
      - Cloud Native
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/cloud/
  - aid: bloomberg-platform:bloomberg-identity-api
    name: Bloomberg Identity and Access Management
    description: Authentication and authorization services for the Bloomberg Platform providing entitlement management, user authentication, and access control for Bloomberg data and applications.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: https://auth.bloomberg.com
    tags:
      - Authentication
      - Authorization
      - Identity
      - Entitlements
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: API Connectivity
        description: BLPAPI socket protocol for real-time data connectivity.
      - name: Cloud Deployment
        description: Cloud-native Bloomberg data access from major cloud platforms.
      - name: On-Premises Integration
        description: B-PIPE and Server API for on-premises enterprise data integration.
      - name: Identity Management
        description: Enterprise authentication and entitlement management.
      - name: High Availability
        description: Redundant infrastructure for mission-critical data connectivity.
      - name: Low Latency
        description: Optimized data delivery for latency-sensitive trading applications.
  - type: UseCases
    data:
      - name: Enterprise Integration
        description: Integrate Bloomberg data into enterprise technology stacks.
      - name: Cloud Migration
        description: Migrate Bloomberg data consumption to cloud-native architectures.
      - name: Trading Infrastructure
        description: Build low-latency trading systems on the Bloomberg Platform.
      - name: Data Platform Development
        description: Develop enterprise data platforms consuming Bloomberg data.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
