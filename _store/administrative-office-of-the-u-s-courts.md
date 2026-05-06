---
aid: administrative-office-of-the-u-s-courts
url: https://raw.githubusercontent.com/api-evangelist/administrative-office-of-the-u-s-courts/refs/heads/main/apis.yml
name: Administrative Office of the U.S. Courts
created: '2024-11-20'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Courts
  - Federal Government
  - Legal
  - PACER
  - Case Records
  - Judiciary
  - Open Data
description: The Administrative Office of the United States Courts is the administrative agency of the United States federal court system, established in 1939. It provides legislative, administrative, legal, financial, management, program, and information technology support services to the federal courts. The agency operates PACER (Public Access to Court Electronic Records), which provides programmatic access to case and docket information from Federal Appellate, District, and Bankruptcy courts via the PACER Authentication API and PACER Case Locator (PCL) REST API. The agency also provides CM/ECF developer resources for building tools that interface with the Case Management and Electronic Case Filing system.
apis:
  - aid: administrative-office-of-the-u-s-courts:pacer-authentication-api
    name: PACER Authentication API
    description: The PACER Authentication API allows users to authenticate automatically and without a user interface, facilitating programmatic access for automated systems to court records. Users provide PACER credentials to receive an authentication token used to access the PCL API and other PACER services. Required before using the PACER Case Locator API.
    humanURL: https://pacer.uscourts.gov/help/pacer/pacer-authentication-api-user-guide
    tags:
      - Authentication
      - Courts
      - PACER
      - REST API
    properties:
      - type: Documentation
        url: https://pacer.uscourts.gov/help/pacer/pacer-authentication-api-user-guide
      - type: APIReference
        url: https://pacer.uscourts.gov/help/pacer/pacer-authentication-api-user-guide
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/administrative-office-of-the-u-s-courts/refs/heads/main/openapi/pacer-authentication-api-openapi.yml
  - aid: administrative-office-of-the-u-s-courts:pacer-case-locator-pcl-api
    name: PACER Case Locator (PCL) API
    description: The PACER Case Locator (PCL) API is a REST API providing programmatic access to a nationwide index of federal court cases across all Federal Appellate, District, and Bankruptcy courts. Supports both immediate searches (returning up to 5,400 items per search) and batch searches (up to 108,000 items). Case searches return groups of cases; party searches return parties associated with cases. Supports JSON and XML encoding. Requires PACER authentication token. Separate QA and Production environments are available for development and testing.
    humanURL: https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide
    tags:
      - Courts
      - Legal
      - Case Records
      - Federal Courts
      - REST API
      - PACER
    properties:
      - type: Documentation
        url: https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide
      - type: APIReference
        url: https://pacer.uscourts.gov/sites/default/files/files/PCL-API-Document_3.pdf
      - type: GettingStarted
        url: https://pacer.uscourts.gov/file-case/developer-resources
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/administrative-office-of-the-u-s-courts/refs/heads/main/openapi/pacer-case-locator-pcl-api-openapi.yml
common:
  - type: Website
    url: https://www.uscourts.gov/
  - type: Portal
    url: https://pacer.uscourts.gov/
  - type: DeveloperPortal
    url: https://pacer.uscourts.gov/file-case/developer-resources
  - type: SignUp
    url: https://pacer.uscourts.gov/register-account
  - type: Contact
    url: https://pacer.uscourts.gov/contact-us
  - type: Features
    data:
      - name: Federal Court Case Search
        description: Programmatic search across a nationwide index of all Federal Appellate, District, and Bankruptcy court cases using the PCL REST API, supporting case search and party search with immediate and batch result modes.
      - name: Automated PACER Authentication
        description: Token-based authentication API enabling automated systems to obtain PACER authentication tokens without requiring a user interface, suitable for integration into automated data pipelines and legal research tools.
      - name: CM/ECF Developer Integration
        description: Technical resources for developers building tools that interface with the Case Management and Electronic Case Filing (CM/ECF) system, including XML tag specifications, NextGen CM/ECF documentation, and release notes for appellate and bankruptcy systems.
      - name: Court Lookup Data Feeds
        description: JSON and XML data feeds providing court lookup information for identifying CM/ECF courts and their configurations, available for integration into court filing software.
      - name: Bankruptcy Filing Integration
        description: Specialized resources for bankruptcy petition preparation software and case trustee management software vendors, including creditor claim filing specifications and official form changes.
      - name: Bulk Data Access
        description: Commercial users can run large batch data pulls via the PCL API, with recommended off-peak hours (6 p.m. to 6 a.m. Central Time) to minimize system impact.
  - type: UseCases
    data:
      - name: Legal Research Automation
        description: Law firms and legal research platforms can use the PCL API to programmatically search federal court case indexes and retrieve case and party information for automated legal research workflows.
      - name: Litigation Monitoring
        description: Corporate legal departments can monitor federal court filings involving specific parties, cases, or subject matters using automated PCL API queries.
      - name: Bankruptcy Software Integration
        description: Bankruptcy petition preparation software and trustee management applications can integrate with CM/ECF and PACER APIs to file documents, retrieve case data, and manage creditor information.
      - name: Court Data Analytics
        description: Academic researchers and legal analytics firms can build datasets of federal court case activity using batch PCL API searches across federal court jurisdictions.
      - name: Legal Technology Development
        description: Legal technology companies can build PACER-integrated products for case tracking, docket monitoring, and court record retrieval using the PACER Authentication and PCL APIs.
  - type: Integrations
    data:
      - name: CM/ECF System
        description: Case Management and Electronic Case Filing system for all federal courts.
      - name: PACER Case Locator
        description: Nationwide index of federal court cases searchable via REST API.
      - name: NextGen CM/ECF
        description: Next-generation electronic filing system with enhanced developer integration support.
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: info@apievangelist.com
---
