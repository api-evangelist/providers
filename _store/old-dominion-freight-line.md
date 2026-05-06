---
aid: old-dominion-freight-line
name: Old Dominion Freight Line
url: https://raw.githubusercontent.com/api-evangelist/old-dominion-freight-line/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Freight
  - Less-Than-Truckload
  - Logistics
  - Shipping
  - Transportation
created: '2026-03-24'
modified: '2026-04-28'
description: Old Dominion Freight Line is a leading less-than-truckload (LTL) motor carrier providing regional, inter-regional, and national freight services in the United States. ODFL offers a suite of REST web services for shippers and partners to integrate freight booking, pickup, tracking, document retrieval, and electronic bill of lading capabilities directly into their systems.
apis:
  - aid: old-dominion-freight-line:bill-of-lading-api
    name: ODFL Bill of Lading API
    description: Submits electronic bills of lading to the Old Dominion Freight Line billing system, generating shipping labels and BOL documents. Used by shippers to programmatically create freight documentation.
    humanURL: https://www.odfl.com/us/en/resources/shipping-api-integrations.html
    baseURL: https://www.odfl.com
    tags:
      - Bill of Lading
      - Documents
      - Freight
      - Shipping
    properties:
      - type: Documentation
        url: https://www.odfl.com/content/dam/odfl/us/en/documents/web-services/Bill%20of%20Lading%20API%20Development%20Guide.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/old-dominion-freight-line/refs/heads/main/openapi/old-dominion-freight-line-bill-of-lading-api-openapi.yml
  - aid: old-dominion-freight-line:pickup-api
    name: ODFL Pickup API
    description: Processes electronic pickup requests for one or more shipments. Returns pickup numbers and PPIDs that shippers use to confirm and track pickup requests with Old Dominion Freight Line.
    humanURL: https://www.odfl.com/us/en/resources/shipping-api-integrations.html
    baseURL: https://www.odfl.com
    tags:
      - Freight
      - Logistics
      - Pickup
      - Shipping
    properties:
      - type: Documentation
        url: https://www.odfl.com/content/dam/odfl/us/en/documents/web-services/Pickup%20API%20Development%20Guide.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/old-dominion-freight-line/refs/heads/main/openapi/old-dominion-freight-line-pickup-api-openapi.yml
  - aid: old-dominion-freight-line:tracking-api
    name: ODFL Tracking API
    description: Provides shipment status information for ODFL freight movements. Used to integrate real-time and historical freight tracking data into shipper and partner systems.
    humanURL: https://www.odfl.com/us/en/resources/shipping-api-integrations.html
    baseURL: https://www.odfl.com
    tags:
      - Freight
      - Shipping
      - Tracking
    properties:
      - type: Documentation
        url: https://www.odfl.com/content/dam/odfl/us/en/documents/web-services/Tracking%20API%20Development%20Guide.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/old-dominion-freight-line/refs/heads/main/openapi/old-dominion-freight-line-tracking-api-openapi.yml
  - aid: old-dominion-freight-line:document-api
    name: ODFL Document API
    description: Retrieves PDF documents associated with shipments, including bills of lading and delivery receipts, by PRO number. Used to programmatically pull shipment documentation from Old Dominion Freight Line.
    humanURL: https://www.odfl.com/us/en/resources/shipping-api-integrations.html
    baseURL: https://www.odfl.com
    tags:
      - Documents
      - Freight
      - Shipping
    properties:
      - type: Documentation
        url: https://www.odfl.com/content/dam/odfl/us/en/documents/web-services/Document%20API%20Development%20Guide.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/old-dominion-freight-line/refs/heads/main/openapi/old-dominion-freight-line-document-api-openapi.yml
common:
  - type: Website
    url: https://www.odfl.com
  - type: Developer
    url: https://www.odfl.com/us/en/resources/shipping-api-integrations.html
  - type: Support
    url: mailto:api@odfl.com
  - type: Tools
    url: https://www.odfl.com/us/en/resources.html
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.19'
---
