---
aid: yardi
url: https://raw.githubusercontent.com/api-evangelist/yardi/refs/heads/main/apis.yml
apis:
- name: Yardi Voyager API
  description: Core property management platform API providing access to accounting, operations, and reporting functionality for real estate portfolios. Yardi Voyager uses SOAP-based web services defined via WSDL, with interfaces for billing and payments, common data, service requests, vendor invoicing, job cost, and commercial data export.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.yardi.com/products/voyager/
  baseURL: https://api.yardi.com
  tags:
  - Accounting
  - Commercial
  - Property Management
  - Real Estate
  - Residential
  properties:
  - type: Documentation
    url: https://www.yardi.com/platform/api/
  - type: OpenAPI
    url: https://api.yardi.com/swagger
  - type: Authentication
    url: https://www.yardi.com/platform/api/authentication/
  - type: Getting Started
    url: https://www.yardi.com/company/become-an-interface-partner/
  - type: Reference
    url: https://www.yardi.com/services/interfaces/standard-interface-options/
- name: Yardi Voyager Commercial Data API
  description: Web service interface that provides the ability to export commercial data from Yardi Voyager databases, including property, unit, lease, and rent roll information. Built on the OSCRE standard with Yardi-specific extensions, this API expands existing services geared towards financial transactions and facilities management.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.yardi.com/news/press-releases/yardi-adds-commercial-data-interface-to-voyager-standard-interface-partnership-program/
  baseURL: https://api.yardi.com
  tags:
  - Commercial
  - Data Export
  - Leasing
  - OSCRE
  properties:
  - type: Documentation
    url: https://www.yardi.com/services/interfaces/standard-interface-options/
  - type: Getting Started
    url: https://www.yardi.com/company/become-an-interface-partner/
- name: Yardi RENTCafe API
  description: API for online rental applications, payments, and resident portal functionality for multifamily properties. RENTCafe APIv2 provides transaction-based pricing with an annual price cap, enabling vendors to integrate leasing, marketing, and resident services into their applications.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.rentcafe.com/
  baseURL: https://api.rentcafe.com
  tags:
  - Applications
  - Multifamily
  - Payments
  - Portal
  - Residents
  properties:
  - type: Documentation
    url: https://www.rentcafe.com/api/
  - type: Terms of Service
    url: https://resources.yardi.com/legal/rc-api-tou/
  - type: Getting Started
    url: https://www.yardi.com/company/become-an-interface-partner/
- name: Yardi Maintenance IQ API
  description: Maintenance and work order management API enabling integration with maintenance operations, service requests, and vendor management. Part of the Voyager Standard Interface Partnership Program, this API supports creating and updating work orders between Yardi and third-party systems.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.yardi.com/products/maintenance-iq/
  baseURL: https://api.yardi.com/maintenance
  tags:
  - Facilities
  - Maintenance
  - Vendors
  - Work Orders
  properties:
  - type: Documentation
    url: https://www.yardi.com/platform/api/maintenance/
  - type: Getting Started
    url: https://www.yardi.com/company/become-an-interface-partner/
- name: Yardi Investment Manager API
  description: API for investment and asset management functions including deal tracking, investor reporting, and portfolio analytics. Provides programmatic access to investment management data within the Yardi Voyager platform.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.yardi.com/products/investment-manager/
  baseURL: https://api.yardi.com/investment
  tags:
  - Analytics
  - Asset Management
  - Investment
  - Reporting
  properties:
  - type: Documentation
    url: https://www.yardi.com/platform/api/investment/
  - type: Getting Started
    url: https://www.yardi.com/company/become-an-interface-partner/
- name: Yardi Store Web Services API
  description: SOAP-based API for Yardi's self-storage management platform, formerly known as CenterShift. The SWS2 API provides tokenized authentication and access to store management methods for creating custom applications and websites that interact with Yardi Store Enterprise and Store Advantage systems.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://centershiftdevx.com/
  baseURL: https://api.yardi.com
  tags:
  - Reservations
  - Self Storage
  - SOAP
  - Store Management
  properties:
  - type: Documentation
    url: https://centershiftdevx.com/2015/01/22/sws2-api-documentation/
  - type: Reference
    url: https://centershiftdevx.com/2017/01/23/end-points/
  - type: Getting Started
    url: https://centershiftdevx.com/2017/04/16/overview-using-yardi-store-web-services-sws/
  - type: Support
    url: https://centershiftdevx.com/2011/06/20/contacting-centershift/
- name: Yardi Kube API
  description: API and webhook integration for Yardi Kube, the coworking and flexible workspace management platform. Enables connecting third-party applications with Yardi Kube for member management, billing, space booking, access control, and CRM integrations.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.yardikube.com/integrations-api/
  baseURL: https://api.yardikube.com
  tags:
  - Booking
  - Coworking
  - Flexible Workspace
  - Webhooks
  properties:
  - type: Documentation
    url: https://www.yardikube.com/integrations-api/
- name: Yardi Senior Living EHR API
  description: Interface API for Yardi's Electronic Health Records platform designed for senior living communities. Supports secure data exchange with pharmacy networks, laboratory systems, and other healthcare partners through standardized interfaces including NCPDP 10.6 SCRIPT compliance.
  image: https://www.yardi.com/wp-content/uploads/2023/01/yardi-logo.svg
  humanURL: https://www.yardi.com/product/ehr/
  baseURL: https://api.yardi.com
  tags:
  - EHR
  - Healthcare
  - Pharmacy
  - Senior Living
  properties:
  - type: Documentation
    url: https://www.yardi.com/product/ehr/
name: Yardi
tags:
- Accounting
- Commercial Real Estate
- Coworking
- Investment Management
- Multifamily
- Property Management
- Real Estate
- Residential
- Self Storage
- Senior Living
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Yardi develops and supports industry-leading investment and property management software for all types and sizes of real estate companies. The platform includes solutions for residential, commercial, public housing, affordable housing, and military housing management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

