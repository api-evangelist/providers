---
aid: audatex
name: Audatex
description: |
  Audatex (part of Solera Holdings) provides automotive claims and repair solutions with data and technology services for the automotive insurance, collision repair, and fleet management industries. It offers the AudaConnect API platform for third-party integration with claims processing, damage assessment, repair cost estimation, and vehicle data workflows. APIs are RESTful with JSON/XML support and OAuth 2.0 authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - Claims Processing
  - Insurance
  - Repair Management
  - Vehicle Data
url: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: audatex:audatex-audaconnect-api
    name: Audatex AudaConnect API
    description: |
      The AudaConnect API enables third-party software developers to access, query, and update the Audatex platform including assessments, vehicle reference data, repair orders, and photo management using RESTful methods with OAuth 2.0.
    humanURL: https://audaconnect-demo.ax-aee.co.uk/AudaAPI.Portal/Home/About
    baseURL: https://audaconnect-demo.ax-aee.co.uk/AudaAPI.Bmsapi
    tags:
      - Assessments
      - Claims
      - Insurance
      - Repair
    properties:
      - type: Documentation
        url: https://audaconnect-demo.ax-aee.co.uk/AudaAPI.Portal/Home/About
      - type: OpenAPI
        url: https://audaconnect-demo.ax-aee.co.uk/AudaAPI.Bmsapi/
      - type: Authentication
        url: https://audaconnect-demo.ax-aee.co.uk/AudaAPI.Portal/Home/About
  - aid: audatex:audatex-gic-api
    name: Audatex GIC API
    description: |
      The Audatex GIC (Global Integration Component) API provides integration capabilities for claims processing and vehicle damage assessment workflows in the insurance and collision repair industries.
    humanURL: https://api-demo.audatex.com/TestGICapi/docs/index.html
    baseURL: https://api-demo.audatex.com/TestGICapi
    tags:
      - Claims
      - GIC
      - Insurance
      - Integration
    properties:
      - type: Documentation
        url: https://api-demo.audatex.com/TestGICapi/docs/index.html
  - aid: audatex:solera-api-gateway
    name: Solera API Gateway
    description: |
      The Solera API Gateway provides access to Audatex and Solera claims processing services including ClaimImage document return and other automotive claims data APIs for North American insurance markets.
    humanURL: https://na.api.solera.com/
    baseURL: https://na.api.solera.com
    tags:
      - Claims
      - Documents
      - Insurance
      - Solera
    properties:
      - type: Documentation
        url: https://na.api.solera.com/
      - type: Authentication
        url: https://na.api.solera.com/
common:
  - type: Website
    url: https://www.audatex.com/
  - type: Documentation
    url: https://www.audatex.com/solutions/
  - type: Privacy Policy
    url: https://www.audatex.com/privacy-policy/
  - type: TermsOfService
    url: https://www.audatex.com/terms-and-conditions/
  - type: Contact
    url: https://www.audatex.com/contact/
  - type: Features
    data:
      - name: Claims Assessment API
        description: Search, download, upload, and amend vehicle damage assessments programmatically via the AudaConnect API.
      - name: Repair Cost Estimation
        description: Access Audatex repair cost estimation data and labor rates for collision repair workflow automation.
      - name: Photo Management
        description: Upload, retrieve, and manage vehicle damage photos attached to claims via the assessment API.
      - name: Repair Order Integration
        description: Create, update, and query repair orders from bodyshop management systems via BMS API integration.
      - name: Vehicle Reference Data
        description: Query vehicle reference data including make, model, trim, and VIN decoding for assessment setup.
      - name: OAuth 2.0 Security
        description: All AudaConnect APIs are secured with OAuth 2.0 authorization for enterprise-grade access control.
  - type: UseCases
    data:
      - name: Insurance Claims Automation
        description: Automate first notice of loss, damage assessment, and claims settlement workflows for auto insurers.
      - name: Bodyshop Management System Integration
        description: Integrate bodyshop management systems with Audatex for repair order creation, parts pricing, and labor time.
      - name: Total Loss Determination
        description: Access vehicle valuation and total loss thresholds to automate total loss claims decisions.
      - name: Digital Claims Submission
        description: Enable digital submission of vehicle damage photos and assessment data from mobile apps to the Audatex platform.
  - type: Integrations
    data:
      - name: Bodyshop Management Systems
        description: Native integration with major BMS platforms for automated repair order and parts pricing workflows.
      - name: Insurance Core Systems
        description: Integration with insurance policy and claims management systems for end-to-end claims processing.
      - name: Vehicle History Providers
        description: Integration with vehicle history and VIN data providers for complete vehicle information at claims initiation.
      - name: Parts Suppliers
        description: Connection to OEM and aftermarket parts supplier catalogs for parts pricing and availability in repair estimates.
  - type: Solutions
    data:
      - name: Claims Process Automation
        description: End-to-end automation of auto insurance claims from FNOL through repair authorization and settlement.
      - name: Repair Shop Workflow
        description: Digital workflow management for collision repair shops integrating estimates, parts, labor, and customer communication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
