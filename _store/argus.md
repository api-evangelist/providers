---
aid: argus
name: ARGUS
description: ARGUS is the industry-standard suite of commercial real estate software solutions by Altus Group. The ARGUS platform includes ARGUS Enterprise (property valuation and cash flow forecasting), ARGUS Developer (development feasibility and project management), ARGUS Intelligence Platform (portfolio analytics, asset management, and fund management), ARGUS EstateMaster (property development feasibility), and ARGUS Taliance (real estate fund management). ARGUS is recognized as the industry standard and taught at 200+ universities worldwide. The ARGUS API provides integration capabilities across cloud-enabled ARGUS solutions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Altus Group
  - Asset Management
  - Commercial Real Estate
  - Fund Management
  - Portfolio Management
  - Real Estate Software
  - Valuation
url: https://raw.githubusercontent.com/api-evangelist/argus/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: argus:argus-api
    name: ARGUS API
    description: The ARGUS API is a cloud-based integration gateway that provides programmatic access to data in ARGUS Enterprise and other cloud-enabled ARGUS solutions. It enables users to extract and ingest data, trigger calculations, and integrate ARGUS models with third-party property management, ERP, and analytics systems without logging into the ARGUS application.
    humanURL: https://www.altusgroup.com/solutions/argus-integrations/
    tags:
      - API Integration
      - Commercial Real Estate
      - Data Integration
    properties:
      - type: Documentation
        url: https://www.altusgroup.com/argus/downloads/argus-integration-solutions/
      - type: GettingStarted
        url: https://www.altusgroup.com/support/start-using-argus-intelligence/
  - aid: argus:argus-enterprise
    name: ARGUS Enterprise
    description: The industry-standard commercial property valuation and cash flow forecasting software providing lease-by-lease modeling, DCF valuations, budgeting, scenario testing, and 40+ portfolio reports.
    humanURL: https://www.altusgroup.com/solutions/argus-enterprise/
    tags:
      - Cash Flow Modeling
      - Commercial Real Estate
      - Portfolio Management
      - Valuation
    properties:
      - type: Documentation
        url: https://www.altusgroup.com/argus/downloads/argus-enterprise/
  - aid: argus:argus-developer
    name: ARGUS Developer
    description: Real estate development feasibility and project management software for property developers, appraisers, and financiers covering pro forma modeling, residual land value, scenario analysis, and cash flow forecasting.
    humanURL: https://www.altusgroup.com/solutions/argus-developer/
    tags:
      - Cash Flow
      - Development
      - Feasibility Analysis
      - Real Estate
    properties:
      - type: Documentation
        url: https://www.altusgroup.com/argus/downloads/argus-developer/
  - aid: argus:argus-intelligence
    name: ARGUS Intelligence Platform
    description: Next-generation real estate investment management platform integrating ARGUS Enterprise with portfolio dashboards, benchmarking, asset manager, portfolio manager, and fund manager capabilities for comprehensive performance monitoring.
    humanURL: https://www.altusgroup.com/solutions/argus-intelligence/
    tags:
      - Asset Management
      - Benchmarking
      - Fund Management
      - Portfolio Analytics
    properties:
      - type: Documentation
        url: https://www.altusgroup.com/support/start-using-argus-intelligence/
  - aid: argus:argus-taliance
    name: ARGUS Taliance
    description: Real estate fund management software for modeling and managing the performance of real estate funds, supporting complex fund structures, waterfall calculations, and investor reporting.
    humanURL: https://www.altusgroup.com/solutions/argus-intelligence/
    tags:
      - Fund Management
      - Real Estate Funds
      - Waterfall Calculations
    properties:
      - type: Documentation
        url: https://www.altusgroup.com/solutions/argus-intelligence/
common:
  - type: Website
    url: https://www.altusgroup.com/argus/
  - type: Documentation
    url: https://www.altusgroup.com/argus/downloads/
  - type: GettingStarted
    url: https://www.altusgroup.com/support/start-using-argus-intelligence/
  - type: Portal
    url: https://cloud.altusplatform.com/login
  - type: Support
    url: https://www.altusgroup.com/support/
  - type: Training
    url: https://www.altusgroup.com/argus/training/
  - type: TermsOfService
    url: https://www.altusgroup.com/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.altusgroup.com/privacy-policy/
  - type: ReleaseNotes
    url: https://www.altusgroup.com/argus/downloads/
  - type: Security
    url: https://www.altusgroup.com/security/
  - type: Features
    data:
      - name: Industry Standard Platform
        description: ARGUS is recognized as the industry standard for CRE investment analysis, taught at 200+ universities worldwide.
      - name: ARGUS API Integration
        description: Cloud-based API gateway enabling programmatic extraction and ingestion of data across ARGUS solutions.
      - name: ARGUS Connector
        description: Pre-built connectors for integrating ARGUS with Yardi, MRI, and other property management systems.
      - name: Cloud Delivery
        description: All ARGUS solutions available as cloud-based platform via ARGUS Cloud on Microsoft Azure.
      - name: ISO 27001 Certified
        description: ISO/IEC 27001:2022 certified and SOC 2 Type II audited for enterprise security standards.
      - name: ARGUS Intelligence Dashboard
        description: Portfolio-level dashboards, performance analytics, and benchmarking across all ARGUS-managed assets.
  - type: UseCases
    data:
      - name: CRE Investment Lifecycle Management
        description: Manage the full commercial real estate investment lifecycle from acquisition underwriting through asset management and disposition.
      - name: Portfolio Analytics and Benchmarking
        description: Monitor portfolio performance across all assets using standardized metrics and industry benchmarking.
      - name: Third-Party System Integration
        description: Integrate ARGUS data with property management, ERP, and analytics platforms via the ARGUS API.
      - name: Fund Management
        description: Model complex real estate fund structures, waterfalls, and investor reporting with ARGUS Taliance.
      - name: Development Feasibility
        description: Assess development project financial viability from initial feasibility through construction completion.
  - type: Integrations
    data:
      - name: Yardi
        description: Pre-built ARGUS Connector for ingesting lease and property management data from Yardi.
      - name: MRI Software
        description: Integration with MRI property management platform for data synchronization.
      - name: Microsoft Azure
        description: ARGUS Cloud hosted on Microsoft Azure for cloud delivery and data security.
      - name: JLL
        description: JLL uses ARGUS across their global real estate asset management operations.
      - name: CBRE
        description: CBRE relies on ARGUS for valuation and investment analysis services worldwide.
      - name: Power BI
        description: Export ARGUS data for visualization in Microsoft Power BI dashboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
