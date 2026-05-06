---
aid: adp
name: ADP
description: ADP (Automatic Data Processing) is a global provider of cloud-based human capital management solutions including payroll, benefits, talent, time, tax, and HR services for businesses of all sizes.
image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
url: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Contract
access: 3rd-Party
apis:
  - aid: adp:adp-workers-api
    name: ADP Workers API
    description: The ADP Workers API enables access to employee and worker data including personal information, job assignments, pay grades, and employment status. REST APIs support worker lifecycle management for HCM integrations across ADP Workforce Now, Vantage HCM, and Enterprise HR platforms.
    tags:
      - HCM
      - HR
      - Payroll
      - Workers
      - Workforce
    image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
    humanURL: https://developers.adp.com/
    baseURL: https://api.adp.com
    properties:
      - type: Documentation
        url: https://developers.adp.com/
      - type: GettingStarted
        url: https://developers.adp.com/getting-started/client-integration-overview
      - type: OpenAPI
        url: openapi/adp-workers-openapi.yml
      - type: JSONSchema
        url: json-schema/adp-worker-schema.json
      - type: JSONLD
        url: json-ld/adp-workers-context.jsonld
  - aid: adp:adp-payroll-api
    name: ADP Payroll API
    description: The ADP Payroll API provides programmatic access to payroll processing, payroll output data, and compensation management. REST APIs support payroll runs, payroll output retrieval (including CSV-formatted bulk data), and headcount and compensation analysis across ADP payroll platforms.
    tags:
      - Compensation
      - HCM
      - HR
      - Payroll
    image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
    humanURL: https://developers.adp.com/
    baseURL: https://api.adp.com
    properties:
      - type: Documentation
        url: https://developers.adp.com/
      - type: GettingStarted
        url: https://developers.adp.com/getting-started/client-integration-overview
      - type: OpenAPI
        url: openapi/adp-payroll-openapi.yml
      - type: JSONLD
        url: json-ld/adp-payroll-context.jsonld
  - aid: adp:adp-embedded-payroll-api
    name: ADP Embedded Payroll API
    description: The ADP Embedded Payroll API enables ISVs and platforms to embed ADP payroll capabilities directly into their applications. REST APIs support payroll processing, tax compliance, and workforce management embedded within partner software products.
    tags:
      - Embedded
      - HCM
      - Payroll
      - Small Business
    image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
    humanURL: https://developers.adp.com/getting-started/embedded-payroll
    baseURL: https://api.adp.com
    properties:
      - type: Documentation
        url: https://developers.adp.com/getting-started/embedded-payroll
      - type: GettingStarted
        url: https://developers.adp.com/getting-started/embedded-payroll
  - aid: adp:adp-benefits-api
    name: ADP Benefits Administration API
    description: The ADP Benefits Administration API provides access to employee benefits enrollment, eligibility, and plan data. APIs support benefits carrier connectivity, open enrollment workflows, and benefits data exchange for insurance carriers and benefits administrators.
    tags:
      - Benefits
      - Enrollment
      - HCM
      - HR
    image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
    humanURL: https://developers.adp.com/
    baseURL: https://api.adp.com
    properties:
      - type: Documentation
        url: https://developers.adp.com/
common:
  - type: Portal
    url: https://developers.adp.com/
  - type: Documentation
    url: https://developers.adp.com/
  - type: GettingStarted
    url: https://developers.adp.com/getting-started/client-integration-overview
  - type: Authentication
    url: https://developers.adp.com/getting-started/client-integration-overview
  - type: OpenAPI
    url: openapi/adp-workers-openapi.yml
    title: ADP Workers OpenAPI
  - type: OpenAPI
    url: openapi/adp-payroll-openapi.yml
    title: ADP Payroll OpenAPI
  - type: JSONSchema
    url: json-schema/adp-worker-schema.json
    title: ADP Worker JSON Schema
  - type: JSONLD
    url: json-ld/adp-context.jsonld
    title: ADP JSON-LD Context
  - type: Features
    data:
      - name: Worker Lifecycle Management
        description: Manage the complete worker lifecycle including hiring, onboarding, job changes, and termination through REST APIs.
      - name: Payroll Processing
        description: Programmatic access to payroll runs, payroll output data, and compensation analysis across ADP platforms.
      - name: Embedded Payroll
        description: Embed ADP payroll capabilities directly into ISV and partner applications with white-label support.
      - name: Benefits Administration
        description: Manage employee benefits enrollment, eligibility, and plan data with carrier connectivity support.
      - name: Organizational Data
        description: Access department structures, organizational hierarchies, and work assignment data.
      - name: Bulk Data Export
        description: Retrieve payroll and workforce data in CSV-formatted bulk exports for analytics and reporting.
  - type: UseCases
    data:
      - name: HCM Integration
        description: Synchronize worker data between ADP and third-party HRIS, ERP, and workforce management systems.
      - name: Payroll Automation
        description: Automate payroll instruction submission and output retrieval for streamlined payroll processing workflows.
      - name: Workforce Analytics
        description: Extract headcount, compensation, and departmental data for workforce planning and business intelligence.
      - name: ISV Embedded Payroll
        description: Integrate ADP payroll processing directly into partner software applications for small business customers.
  - type: Integrations
    data:
      - name: ADP Workforce Now
        description: Full integration with ADP Workforce Now for mid-market HR, payroll, talent, and benefits management.
      - name: ADP Vantage HCM
        description: Enterprise-grade HCM integration for large organizations with complex payroll and HR requirements.
      - name: ADP RUN Powered by ADP
        description: Payroll and HR integration for small businesses using the ADP RUN platform.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
tags:
  - Benefits
  - HCM
  - HR
  - Payroll
  - Workforce
---
