---
aid: tazama
name: Tazama
description: Tazama is the first open source platform for real-time financial monitoring and fraud detection, launched by Linux Foundation Charities with support from the Bill and Melinda Gates Foundation. It provides real-time fraud management, AML compliance, and cost-effective monitoring of digital financial transactions through a microservices architecture with rule processors, typology scoring, and case management integration. Built to ISO 20022 standards for maximum financial messaging interoperability.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Technology
  - Fraud Detection
  - Anti-Money Laundering
  - Linux Foundation
  - Open Source
  - Transaction Monitoring
  - ISO 20022
  - Real Time
created: '2026-03-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tazama:transaction-monitoring-service
    name: Tazama Transaction Monitoring Service API
    description: The core API for ingesting real-time ISO 20022 financial transaction messages into the Tazama platform for fraud detection and AML compliance. Accepts pain.001, pain.013, pacs.008, and pacs.002 message types from financial service providers including banks, remitters, mobile money operators, clearing houses, and payment switches. Validates messages, routes them through configurable rule processors, and returns fraud and AML evaluation results.
    humanURL: https://tazama.org/products/
    baseURL: http://localhost:5000
    tags:
      - Transaction Monitoring
      - ISO 20022
      - Fraud Detection
      - Real Time
    properties:
      - type: Documentation
        url: https://tazama.org/products/
      - type: GitHubRepository
        url: https://github.com/tazama-lf/tms-service
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/openapi/tazama-transaction-monitoring-service-openapi.yml
    contact:
      - FN: Tazama Support
        url: https://tazama.org
  - aid: tazama:admin-service
    name: Tazama Admin Service API
    description: Administrative API for managing and configuring the Tazama platform. Supports configuration of rule processors, typology definitions, network maps, and system administration. Swagger documentation available at the admin service endpoint.
    humanURL: https://github.com/tazama-lf/admin-service
    baseURL: http://localhost:5100
    tags:
      - Administration
      - Configuration
      - Rule Management
    properties:
      - type: Documentation
        url: https://github.com/tazama-lf/admin-service
      - type: GitHubRepository
        url: https://github.com/tazama-lf/admin-service
    contact:
      - FN: Tazama Support
        url: https://tazama.org
common:
  - type: Documentation
    name: Tazama Documentation
    description: Official documentation for Tazama platform and APIs.
    url: https://tazama.org/products/
  - type: GitHubOrg
    name: Tazama GitHub Organization
    description: Source code and repositories for Tazama open source platform.
    url: https://github.com/tazama-lf
  - type: About
    name: About Tazama
    url: https://tazama.org/about/
  - type: Licensing
    name: Linux Foundation Charities
    url: https://www.linuxfoundation.org/press/linux-foundation-launches-tazama-for-real-time-fraud-management
  - type: OpenAPI
    name: Tazama TMS OpenAPI Specification
    url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/openapi/tazama-transaction-monitoring-service-openapi.yml
  - type: Vocabulary
    name: Tazama Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/vocabulary/tazama-vocabulary.yml
  - type: JSONSchema
    name: Transaction Response Schema
    url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/json-schema/tazama-transaction-response-schema.json
  - type: JSONLDContext
    name: Tazama JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/json-ld/tazama-context.jsonld
  - type: SpectralRules
    name: Tazama Spectral Rules
    url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/rules/tazama-rules.yml
  - type: NaftikoCapabilities
    name: Tazama Fraud Detection Capability
    url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/capabilities/fraud-detection.yaml
features:
  - name: Real-Time Transaction Monitoring
    description: Processes financial transactions in real time for immediate fraud detection.
  - name: ISO 20022 Compliance
    description: Built to ISO 20022 standards for financial messaging interoperability.
  - name: Payment Platform Adapter
    description: Transforms non-ISO 20022 messages into ISO 20022 compatible formats.
  - name: Rule-Based Fraud Detection
    description: Configurable rule processors evaluate transactions for suspicious behavior.
  - name: Typology Scoring
    description: Aggregates rule results into fraud and AML typology scores.
  - name: AML Compliance
    description: Anti-money laundering monitoring built into the transaction processing pipeline.
  - name: Case Management Integration
    description: Issues investigation alerts and case data to external case management systems.
  - name: Transaction Blocking
    description: Can block high-risk transactions to prevent financial loss.
  - name: Kubernetes Deployment
    description: Helm charts available for AKS, EKS, GKE, and on-premises Kubernetes deployments.
  - name: GraphQL Access
    description: Hasura GraphQL API layer for flexible database queries.
useCases:
  - name: Fraud Detection for Mobile Money Operators
    description: Real-time monitoring of mobile financial transactions for fraud patterns.
  - name: AML Compliance for Banks
    description: Automated AML screening of transactions to meet regulatory requirements.
  - name: Payment Switch Monitoring
    description: Monitor transactions passing through payment switches for suspicious activity.
  - name: Clearing House Risk Management
    description: Screen clearing house transactions for fraud and money laundering.
integrations:
  - name: Hasura GraphQL API
    description: GraphQL access layer to the Tazama database via Hasura.
    url: https://hasura.io
  - name: Keycloak Authentication
    description: Identity and access management via Keycloak.
    url: https://www.keycloak.org
  - name: NATS Messaging
    description: Event streaming via NATS message broker.
    url: https://nats.io
  - name: ArangoDB
    description: Multi-model database for transaction data and participant graphs.
    url: https://www.arangodb.com
  - name: Mojaloop
    description: ISO 20022 messages map to Mojaloop Quote, Quote Response, and Transfer messages.
    url: https://mojaloop.io
  - name: External Case Management Systems
    description: Alerts and case data sent to external case management platforms.
solutions:
  - name: Financial Inclusion
    description: Enables small financial service providers in developing markets to afford fraud monitoring.
  - name: Open Source Fraud Prevention
    description: First open-source real-time fraud management platform for financial services.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
