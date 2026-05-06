---
aid: amazon-supply-chain
name: Amazon Supply Chain
description: AWS Supply Chain is a cloud-based application that works with your existing enterprise resource planning (ERP) and supply chain management systems to help you manage supply chain risks. It provides ML-powered insights and recommended actions to help mitigate supply chain disruptions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - ERP Integration
  - Logistics
  - Machine Learning
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-supply-chain:aws-supply-chain-api
    name: AWS Supply Chain API
    description: The AWS Supply Chain API provides programmatic access to create and manage supply chain instances, data lakes, data integrations, and bills of materials for supply chain visibility and risk management.
    humanURL: https://aws.amazon.com/supply-chain/
    baseURL: https://scn.amazonaws.com
    tags:
      - Logistics
      - Machine Learning
      - Supply Chain
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-supply-chain.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/supply-chain/
      - type: Pricing
        url: https://aws.amazon.com/supply-chain/pricing/
      - type: FAQ
        url: https://aws.amazon.com/supply-chain/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/supply-chain/
  - type: Documentation
    url: https://docs.aws.amazon.com/aws-supply-chain/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/industries/supply-chain/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/scn/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-supply-chain-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-supply-chain-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-supply-chain.yaml
  - type: Features
    data:
      - name: ML-Powered Insights
        description: Machine learning models provide risk visibility and recommended actions for supply chain disruptions.
      - name: ERP Integration
        description: Connects with existing ERP and supply chain management systems via data integration flows.
      - name: Data Lake
        description: Centralized data lake for supply chain data with namespace and dataset management.
      - name: Bill of Materials Import
        description: Import bill of materials data from S3 for inventory and component tracking.
      - name: Data Integration Events
        description: Event-driven data ingestion for real-time supply chain data updates.
      - name: Multi-instance
        description: Create and manage multiple supply chain instances for different business units.
  - type: UseCases
    data:
      - name: Supply Chain Risk Management
        description: Identify and mitigate supply chain disruptions with ML-powered risk insights.
      - name: Inventory Visibility
        description: Unified view of inventory across suppliers, warehouses, and distribution centers.
      - name: ERP Data Integration
        description: Integrate ERP data with AWS Supply Chain for unified supply chain visibility.
      - name: Demand Forecasting
        description: Use ML models to forecast demand and optimize inventory levels.
  - type: Integrations
    data:
      - name: SAP ERP
        description: Connect SAP ERP data to AWS Supply Chain via data integration flows.
      - name: Oracle ERP
        description: Integrate Oracle ERP supply chain data for unified visibility.
      - name: Amazon S3
        description: Import and export supply chain data via S3 for batch processing.
      - name: Amazon EventBridge
        description: Send supply chain events to EventBridge for downstream processing.
      - name: AWS IoT
        description: Integrate IoT sensor data for real-time supply chain monitoring.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
x-type: company
---
