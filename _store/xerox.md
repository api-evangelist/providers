---
aid: xerox
name: Xerox
description: Xerox is a global technology company and document management leader providing printing, digital document management, and business process solutions. Xerox offers the Xerox Developer Program providing open, standards-based APIs for integration with ConnectKey multifunction printers, FreeFlow production printing, Managed Print Services (MPS), and the Xerox Public Print Service. The program provides SDKs, APIs, and tools for building custom printing applications, workflow integrations, and enterprise print management solutions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Document Management
  - Enterprise
  - Fortune 500
  - Managed Print Services
  - Print Services
  - Printing
created: '2024-01-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/xerox/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: xerox:xerox-public-print-api
    name: Xerox Public Print API
    description: REST API for managing print jobs through the Xerox Public Print Service. Provides endpoints for job creation, status monitoring, site discovery, provider management, EULA handling, and print history. Requires authentication via xrxauth header, user-email, and appid for all secure calls. Supports location-based site search for finding nearby printers.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://publicprintapi.services.xerox.com/
    baseURL: https://publicprintapi.services.xerox.com/api/v1
    tags:
      - Print Jobs
      - Print Management
      - Printing
      - REST
    properties:
      - type: Documentation
        url: https://publicprintapi.services.xerox.com/
      - type: OpenAPI
        url: openapi/xerox-public-print-openapi.yml
    contact:
      - type: Email
        url: mailto:xerox.global.developer.program@xerox.com
  - aid: xerox:xerox-managed-print-services-api
    name: Xerox Managed Print Services API
    description: The Xerox MPS-API and Support Assistant API (SA-API) provide a secure common interface allowing third parties to access features in the Xerox hosted technology suite for managed print services. Based on standard Web Service technologies supporting fleet management, device monitoring, supply replenishment, and service request automation.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.xerox.com/en-us/about/developer-program
    tags:
      - Fleet Management
      - Managed Print Services
      - Monitoring
      - Print Management
    properties:
      - type: Documentation
        url: https://www.xerox.com/en-us/about/developer-program
  - aid: xerox:xerox-extensible-interface-platform
    name: Xerox Extensible Interface Platform (EIP)
    description: SDK and API framework for building custom applications that run directly on Xerox ConnectKey-enabled multifunction printers and compatible devices. Apps are deployed through the Xerox App Gallery and can integrate device capabilities including scanning, printing, and workflow automation. Includes the Xerox App Developer Kit for ConnectKey applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.xerox.com/en-us/about/developer-program
    tags:
      - App Development
      - ConnectKey
      - Multifunction Printer
      - SDK
    properties:
      - type: Documentation
        url: https://www.xerox.com/en-us/about/developer-program
      - type: AppGallery
        url: https://appgallery.services.xerox.com
  - aid: xerox:xerox-freeflow-api
    name: Xerox FreeFlow SDK
    description: Software development kit for integrating with the Xerox FreeFlow production printing platform. Includes interfaces for Prepress, Press, Variable Information (VIPP), and Photo modules enabling custom workflow automation for high-volume production printing environments.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.xerox.com/en-us/about/developer-program
    tags:
      - FreeFlow
      - Production Printing
      - SDK
      - VIPP
    properties:
      - type: Documentation
        url: https://www.xerox.com/en-us/about/developer-program
common:
  - type: Website
    url: https://www.xerox.com
  - type: DeveloperProgram
    url: https://www.xerox.com/en-us/about/developer-program
  - type: AppGallery
    url: https://appgallery.services.xerox.com
  - type: DeveloperPortal
    url: https://developers.xerox-solutions.net
  - type: PublicPrintAPI
    url: https://publicprintapi.services.xerox.com/
  - type: TermsOfService
    url: https://www.xerox.com/en-us/about/legal
  - type: PrivacyPolicy
    url: https://www.xerox.com/en-us/about/privacy
  - type: Contact
    url: mailto:xerox.global.developer.program@xerox.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
