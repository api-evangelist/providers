---
aid: wynsure
name: Wynsure
description: Wynsure is an end-to-end insurance policy administration platform from Mphasis Wyde that delivers Quote-to-Claims capabilities across Group, Individual, Life, Annuities, Health, Disability, Accident, Dental, and Vision lines. The multi-language, multi-currency platform combines policy administration, underwriting, billing, claims, enrollment, broker distribution, and analytics with AI-powered modules such as the Wynsure Smart Underwriting Platform (WSUP), Underwriter Assist, and Intelligent Document Processing. Wynsure exposes RESTful APIs and SOA web services through a bundled Talend Enterprise Service Bus (ESB) as part of the Wynsure as a Service (WaaS) offering for integration with third-party systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Insurance
  - InsurTech
  - Policy Administration
  - Claims Management
  - Billing
  - Underwriting
  - Enrollment
  - Life Insurance
  - Annuities
  - Health Insurance
  - Disability Insurance
  - Group Benefits
  - Voluntary Benefits
  - Brokers
  - Financial Services
created: '2024-01-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wynsure/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wynsure:wynsure-rest-api
    name: Wynsure REST API
    description: RESTful API exposing Wynsure's core insurance platform capabilities for integration with third-party systems. Provides programmatic access to policy administration, underwriting, billing, claims, and enrollment workflows across Wynsure's Quote-to-Claims value chain. Bundled as part of the Wynsure as a Service (WaaS) offering with an integration-ready Talend Enterprise Service Bus (ESB) for connecting to internal systems and third-party insurance applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.wyde.com/en/home/products/wynsure.html
    baseURL: https://api.wyde.com
    tags:
      - Policy Administration
      - Underwriting
      - Claims
      - Billing
      - Enrollment
      - Insurance
      - REST
    properties:
      - type: Documentation
        url: https://www.wyde.com/en/home/products/wynsure.html
      - type: APIReference
        url: https://www.wyde.com/en/home/products/wynsure.html
      - type: Portal
        url: https://www.wyde.com/en/home/products/wynsure-as-a-service.html
    contact:
      - type: Support
        url: https://www.wyde.com/en/home/contact-us.html
  - aid: wynsure:wynsure-web-services
    name: Wynsure Web Services
    description: Service-Oriented Architecture (SOA) web services exposed by Wynsure for end-to-end insurance integration. Delivered through the bundled Talend Enterprise Service Bus (ESB), the web services provide access to policy, billing, claims, commissions, and enrollment functions for system integrators connecting Wynsure with broker portals, payment processors, medical data providers (APS, Labs, MIB), and other downstream systems.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.wyde.com/en/home/products/wynsure-as-a-service.html
    baseURL: https://api.wyde.com
    tags:
      - Web Services
      - SOA
      - Integration
      - Insurance
      - ESB
    properties:
      - type: Documentation
        url: https://www.wyde.com/en/home/products/wynsure-as-a-service.html
      - type: Integrations
        url: https://www.wyde.com/en/home/products/wynsure-as-a-service.html
    contact:
      - type: Support
        url: https://www.wyde.com/en/home/contact-us.html
  - aid: wynsure:wynsure-smart-underwriting-platform-api
    name: Wynsure Smart Underwriting Platform API
    description: API surface for the Wynsure Smart Underwriting Platform (WSUP), a Generative AI-powered underwriting solution that connects employers, employees, brokers, carriers, and affinity partners across the group insurance value chain. Includes RFP Assist for streamlining group RFP responses and Underwriter Assist (UW Assist), a contextual conversation bot that augments underwriter productivity with risk-centric workflows and integrations to medical data sources (APS, Labs, MIB).
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.wyde.com/en/home/solutions/wynsure-smart-underwriting-platform.html
    baseURL: https://api.wyde.com
    tags:
      - Underwriting
      - Generative AI
      - Risk
      - Group Insurance
      - Insurance
    properties:
      - type: Documentation
        url: https://www.wyde.com/en/home/solutions/wynsure-smart-underwriting-platform.html
    contact:
      - type: Support
        url: https://www.wyde.com/en/home/contact-us.html
  - aid: wynsure:wynsure-billing-api
    name: Wynsure Billing API
    description: API capabilities of the Wynsure Billing solution covering the entire billing process for individual and group insurance carriers, including invoice creation and delivery, consolidated billing, automated reconciliation, commission processing, payment processing, lapsing and cancellation, and billing-related customer service. Modular by design so carriers can adopt only the capabilities that fit their business needs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.wyde.com/en/home/solutions/wynsure-billing.html
    baseURL: https://api.wyde.com
    tags:
      - Billing
      - Payments
      - Commissions
      - Reconciliation
      - Insurance
    properties:
      - type: Documentation
        url: https://www.wyde.com/en/home/solutions/wynsure-billing.html
    contact:
      - type: Support
        url: https://www.wyde.com/en/home/contact-us.html
  - aid: wynsure:wynsure-enrollment-acceleration-api
    name: Wynsure Enrollment Acceleration API
    description: Data-driven and intelligent front-office enrollment API for carriers, brokers, employers, and members. Wynsure Enrollment Acceleration ingests enrollment data from multiple enrollment platforms and other internal and external data sources, supports electronic document intake and distribution, and surfaces actionable analytics to enrollment operations managers, brokers, benefit administrators, and individual members.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.wyde.com/en/home/solutions/wynsure-enrollment-acceleration.html
    baseURL: https://api.wyde.com
    tags:
      - Enrollment
      - Brokers
      - Employers
      - Members
      - Group Benefits
      - Insurance
    properties:
      - type: Documentation
        url: https://www.wyde.com/en/home/solutions/wynsure-enrollment-acceleration.html
    contact:
      - type: Support
        url: https://www.wyde.com/en/home/contact-us.html
  - aid: wynsure:wynsure-sales-and-broker-management-api
    name: Wynsure Sales and Broker Management API
    description: Front-office sales management API focused on monitoring and visualizing insurance sales performance for brokers and agents. Part of the Wynsure Front Office suite, providing 360-degree customer views, broker distribution support, and sales analytics for group and individual insurance carriers.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.wyde.com/en/home/solutions/wynsure-sales-and-broker-management.html
    baseURL: https://api.wyde.com
    tags:
      - Sales
      - Brokers
      - Distribution
      - CRM
      - Insurance
    properties:
      - type: Documentation
        url: https://www.wyde.com/en/home/solutions/wynsure-sales-and-broker-management.html
    contact:
      - type: Support
        url: https://www.wyde.com/en/home/contact-us.html
common:
  - type: Website
    url: https://www.wyde.com
  - type: Documentation
    url: https://www.wyde.com/en/home/products/wynsure.html
  - type: Portal
    url: https://www.wyde.com/en/home/products/wynsure-as-a-service.html
  - type: Support
    url: https://support.eldocomp.com
  - type: Contact
    url: https://www.wyde.com/en/home/contact-us.html
  - type: Partners
    url: https://www.wyde.com/en/home/partners.html
  - type: TermsOfService
    url: https://www.mphasis.com/home/terms-of-Use.html
  - type: PrivacyPolicy
    url: https://www.wyde.com/en/home/privacy.html
  - type: LinkedIn
    url: https://www.linkedin.com/company/mphasiswyde
  - type: GitHubOrganization
    url: https://github.com/wynsure
  - type: Features
    data:
      - name: Speed to Market with MVP
        description: Accelerated speed-to-market through a Minimum Viable Product approach that lets carriers launch new insurance products quickly.
      - name: Persona-based Digital Experience
        description: Enhanced persona-based digital experiences for carriers, brokers, employers, and members across web and mobile channels.
      - name: Rapid Product Configuration
        description: Product Factory module supports multi-product configuration across Group, Individual, Life, Annuities, Health, Disability, Accident, Dental, and Vision lines.
      - name: End-to-End Quote-to-Claims Lifecycle
        description: Single platform covering the complete insurance functional value chain from quote and enrollment to billing, servicing, and claims.
      - name: Intelligent Document Processing
        description: AI- and OCR-powered Intelligent Document Processing (IDP) for automated extraction and classification of insurance documents.
      - name: Generative AI Underwriter Assist
        description: Gen AI-enabled Underwriter Assist contextual conversation bot that augments underwriter productivity with risk-centric workflows.
      - name: Multi-language and Multi-currency
        description: Multi-language and multi-currency support for global insurance carriers operating across multiple regions and regulatory regimes.
      - name: Service-Oriented Architecture
        description: SOA-based architecture with bundled Talend Enterprise Service Bus accelerates system integration and reduces overall implementation time.
      - name: Flexible Deployment
        description: Available on-premise, hosted, and as Wynsure as a Service (WaaS) on a scalable private-cloud infrastructure.
      - name: Operational Data Store and Analytics
        description: Integrated operational data store with business intelligence and analytics, including GDPR compliance support.
  - type: UseCases
    data:
      - name: Group Benefits Administration
        description: Administer group and worksite life, disability, accident, dental, and vision insurance for group carriers such as AIG Benefit Solutions and Aflac.
      - name: Individual Life and Annuity
        description: End-to-end policy administration, billing, and claims for individual life and annuity carriers across multiple jurisdictions.
      - name: Voluntary Benefits Enrollment
        description: Streamline voluntary benefits enrollment through self-service portals for brokers, employers, and members.
      - name: Smart Group Underwriting
        description: AI-powered group underwriting with RFP Assist and Underwriter Assist to accelerate quote turnaround and improve risk decisions.
      - name: Consolidated Billing and Reconciliation
        description: Consolidated multi-product billing with automated reconciliation, commission processing, and AI chatbots for billing customer service.
      - name: Claims Processing with Medical Oversight
        description: End-to-end claims management for life and health products with integrated medical oversight workflows.
      - name: Broker and Agent Distribution
        description: Sales management and 360-degree customer view for broker and agent distribution channels.
      - name: Cloud-Based Policy Administration
        description: Wynsure as a Service (WaaS) delivers policy administration on a scalable private-cloud environment for carriers seeking SaaS deployment.
  - type: Integrations
    data:
      - name: Talend Enterprise Service Bus
        description: Bundled Talend ESB exposes Wynsure RESTful APIs and SOA web services to internal systems and third-party insurance applications.
      - name: Medical Data Providers
        description: Underwriting integrations with Attending Physician Statements (APS), Labs, and the Medical Information Bureau (MIB) for risk evaluation.
      - name: Third-Party Quote and Sales Apps
        description: APIs to support third-party quote and sales applications integrating with Wynsure's policy administration platform.
      - name: Third-Party Claims Apps
        description: APIs to support third-party claims applications integrating with Wynsure's claims processing module.
      - name: Enrollment Platforms
        description: Wynsure Enrollment Acceleration ingests enrollment data from external enrollment platforms used by brokers and benefit administrators.
      - name: Mphasis Cloud and Data Services
        description: Integration with broader Mphasis offerings including cloud services, data analytics, and business process services.
      - name: Payment Processing
        description: Wynsure Billing integrates with payment processors for premium collection, lapsing/cancellation, and reconciliation workflows.
  - type: Solutions
    data:
      - name: Wynsure as a Service (WaaS)
        description: Cloud-based Wynsure offering providing policy administration on a scalable private-cloud environment with bundled ESB integration.
      - name: Wynsure Smart Underwriting Platform
        description: Generative AI-powered underwriting platform connecting employers, employees, brokers, carriers, and affinity partners.
      - name: Wynsure Billing
        description: State-of-the-art billing solution covering invoicing, commissions, payments, lapsing, and customer service for individual and group carriers.
      - name: Wynsure Enrollment Acceleration
        description: Front-office enrollment solution that streamlines broker, employer, and member enrollment through analytics and self-service.
      - name: Wynsure Sales and Broker Management
        description: Sales management tool for monitoring and visualizing insurance sales performance across broker and agent distribution channels.
      - name: Wynsure Medical Underwriting
        description: New business and underwriting solution with straight-through processing and integrations to medical data sources.
      - name: Wynsure Group Member Portal
        description: Enrollment portal with self-service capabilities, electronic document intake and distribution, and dashboard data visualization for brokers, employers, and members.
      - name: Wynsure Front Office
        description: Front-office suite combining broker distribution, sales management, and 360-degree customer view for carrier sales operations.
      - name: Wynsure Claims
        description: End-to-end claims management module covering life, health, disability, accident, dental, and vision claims with medical oversight.
      - name: Wynsure Data Analytics
        description: Integrated operational data store and business intelligence module with GDPR compliance support.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
