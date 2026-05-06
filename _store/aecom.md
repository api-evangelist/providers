---
aid: aecom
url: https://raw.githubusercontent.com/api-evangelist/aecom/refs/heads/main/apis.yml
name: AECOM
tags:
  - Engineering
  - Infrastructure
  - Construction
  - Environmental Services
  - Transportation
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2026-03-21'
modified: '2026-04-19'
description: AECOM is a global infrastructure consulting firm providing professional services across planning, design, engineering, program management, and construction management for clients in transportation, water, energy, and the environment. AECOM operates in over 150 countries and is listed on the NYSE as ACM. The firm serves governments, businesses, and organizations worldwide, delivering integrated lifecycle solutions from advisory and design through construction and operations.
specificationVersion: '0.16'
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
apis:
  - aid: aecom:aecom-pipeinsights-api
    name: AECOM PipeInsights API
    tags:
      - Water Infrastructure
      - Sewer Inspection
      - AI
      - SaaS
      - Digital
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://digital.aecom.com
    humanURL: https://digital.aecom.com/pipeinsights
    description: PipeInsights is AECOM's cloud-based SaaS solution for AI-powered sewer inspection analysis. It enables municipalities and utilities to upload sewer inspection footage, perform QA/QC defect coding, automate defect detection using machine learning, visualize infrastructure health, and generate rehabilitation strategy recommendations. Available on the Microsoft Azure Marketplace.
    properties:
      - url: https://digital.aecom.com/pipeinsights
        type: Documentation
      - url: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/aecom.pipeinsights
        type: Marketplace
common:
  - url: https://www.aecom.com
    type: Portal
  - url: https://www.aecom.com/services/
    type: Documentation
  - url: https://digital.aecom.com
    type: Portal
    title: Digital AECOM
  - url: https://www.aecom.com/insights/
    type: Blog
  - url: https://www.aecom.com/careers/
    type: Careers
  - url: https://www.aecom.com/legal/terms-of-use/
    type: TermsOfService
  - url: https://www.aecom.com/legal/privacy-policy/
    type: PrivacyPolicy
  - url: https://www.aecom.com/legal/cookie-policy/
    type: Legal
  - url: https://investors.aecom.com
    type: Portal
    title: Investor Relations
  - url: https://www.aecom.com/contact-us/
    type: Contact
  - url: https://www.linkedin.com/company/aecom/
    type: LinkedIn
  - type: Features
    data:
      - name: Digital AECOM Platform
        description: A suite of cloud-based SaaS solutions and digital tools that help clients accelerate their digital journeys and achieve better project outcomes in infrastructure delivery.
      - name: PipeInsights
        description: AI-powered sewer inspection analysis platform available on Microsoft Azure Marketplace that automates defect coding and generates infrastructure rehabilitation strategies.
      - name: Program Management
        description: Digital program management capabilities for large-scale infrastructure programs enabling real-time visibility into project portfolios, budgets, and schedules.
      - name: Environmental Intelligence
        description: Digital tools for environmental data collection, analysis, and reporting to support environmental impact assessments, remediation tracking, and sustainability reporting.
      - name: Infrastructure Analytics
        description: Data analytics and visualization tools for infrastructure asset management, helping clients make data-driven decisions about maintenance and capital investment.
      - name: BIM and Digital Delivery
        description: Building Information Modeling and digital project delivery tools integrated into engineering and design workflows across transportation, buildings, and water projects.
  - type: UseCases
    data:
      - name: Sewer System Asset Management
        description: Use PipeInsights to automate sewer inspection defect coding, prioritize rehabilitation, and reduce costs for municipal water utilities.
      - name: Transportation Infrastructure Planning
        description: Digital planning and design tools supporting road, rail, airport, and transit infrastructure projects from concept through delivery.
      - name: Environmental Remediation Management
        description: Digital platforms for tracking environmental remediation programs including site characterization, contaminant monitoring, and regulatory compliance reporting.
      - name: Water System Digital Twin
        description: Creating digital representations of water and wastewater infrastructure for operational optimization, predictive maintenance, and resilience planning.
      - name: Sustainable Infrastructure Reporting
        description: Tools for measuring, reporting, and improving the sustainability performance of infrastructure projects and assets.
  - type: Integrations
    data:
      - name: Microsoft Azure
        description: AECOM Digital products including PipeInsights are available through the Microsoft Azure Marketplace for enterprise cloud deployment.
      - name: Bentley Systems
        description: Integration with Bentley infrastructure engineering software for BIM and digital delivery workflows.
      - name: Autodesk
        description: Integration with Autodesk design and construction platforms including Civil 3D, Revit, and BIM 360 for engineering project delivery.
      - name: Esri ArcGIS
        description: Integration with Esri GIS platforms for spatial data analysis, environmental mapping, and infrastructure asset management.
  - type: Solutions
    data:
      - name: Transportation
        description: End-to-end transportation infrastructure consulting for roads, bridges, railways, airports, and transit systems.
      - name: Water
        description: Water and wastewater engineering services including treatment, distribution, collection, and stormwater management with digital asset management tools.
      - name: Environment
        description: Environmental consulting, remediation, and restoration services with digital data management platforms.
      - name: Buildings
        description: Architecture, design, and engineering services for government, commercial, healthcare, and education facilities with BIM-based delivery.
      - name: Energy
        description: Energy transition consulting and infrastructure engineering for power generation, transmission, distribution, and renewable energy projects.
---
