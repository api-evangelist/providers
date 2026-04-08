---
aid: doordash
url: https://raw.githubusercontent.com/api-evangelist/doordash/refs/heads/main/apis.yml
apis:
- aid: doordash:drive-api
  name: DoorDash Drive API
  tags:
  - Delivery
  - Food Delivery
  - Last Mile
  - Logistics
  - On-Demand
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://openapi.doordash.com/drive/v2
  humanURL: https://developer.doordash.com/en-US/docs/drive/overview/about_drive/
  properties:
  - url: https://developer.doordash.com/en-US/docs/drive/overview/about_drive/
    type: Documentation
  - type: OpenAPI
    url: openapi/doordash-drive-openapi.yml
  - type: AsyncAPI
    url: asyncapi/doordash-drive-webhooks-asyncapi.yml
  description: The DoorDash Drive API enables businesses to request on-demand deliveries fulfilled by DoorDash's fleet of Dashers. It provides endpoints for checking delivery serviceability, getting delivery quotes, creating and managing deliveries, and tracking delivery status in real time. The API uses JWT-based authentication and is designed for businesses that want to offer delivery from their own ordering experience while leveraging DoorDash's logistics network.
- aid: doordash:drive-classic-api
  name: DoorDash Drive Classic API
  tags:
  - Delivery
  - Enterprise
  - Food Delivery
  - Last Mile
  - Logistics
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://openapi.doordash.com/drive/v1
  humanURL: https://developer.doordash.com/en-US/docs/drive_classic/overview/about_drive_classic/
  properties:
  - url: https://developer.doordash.com/en-US/docs/drive_classic/overview/about_drive_classic/
    type: Documentation
  - type: OpenAPI
    url: openapi/doordash-drive-classic-openapi.yml
  description: The DoorDash Drive Classic API is the legacy version of the Drive API, designed for large enterprises and middleware providers who require extensive configuration and customizability for their delivery integrations. It provides endpoints for managing businesses, stores, and deliveries through DoorDash's logistics platform. The API uses JWT-based Bearer token authentication and operates at the v1 endpoint path.
- aid: doordash:marketplace-api
  name: DoorDash Marketplace API
  tags:
  - Food Delivery
  - Marketplace
  - Orders
  - Restaurants
  - Retail
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://openapi.doordash.com/marketplace
  humanURL: https://developer.doordash.com/en-US/docs/marketplace/overview/about_marketplace/
  properties:
  - url: https://developer.doordash.com/en-US/docs/marketplace/overview/about_marketplace/
    type: Documentation
  - type: OpenAPI
    url: openapi/doordash-marketplace-openapi.yml
  - type: AsyncAPI
    url: asyncapi/doordash-marketplace-webhooks-asyncapi.yml
  description: The DoorDash Marketplace API allows merchants and third-party providers to integrate directly with the DoorDash marketplace for order management, menu synchronization, and store operations. It supports receiving orders from DoorDash, updating order statuses, and managing menu availability in real time. The API is not generally available and access is granted through a selective partner program where DoorDash evaluates integration quality and business fit.
- aid: doordash:marketplace-item-management-api
  name: DoorDash Item Management API
  tags:
  - Catalog
  - Inventory
  - Menus
  - Pricing
  - Retail
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://openapi.doordash.com/marketplace
  humanURL: https://developer.doordash.com/en-US/api/marketplace_v2/
  properties:
  - url: https://developer.doordash.com/en-US/api/marketplace_v2/
    type: Documentation
  - type: OpenAPI
    url: openapi/doordash-item-management-openapi.yml
  description: The DoorDash Item Management API enables merchants and integration partners to programmatically manage their item catalogs, inventory levels, pricing, and other product attributes on the DoorDash platform. It provides endpoints for creating, updating, and retrieving item data across stores. This API is particularly useful for retail and grocery partners who need to keep large catalogs synchronized between their own systems and DoorDash's marketplace.
- aid: doordash:reporting-api
  name: DoorDash Reporting API
  tags:
  - Analytics
  - Data
  - Financial
  - Operations
  - Reporting
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://openapi.doordash.com/dataexchange/v1
  humanURL: https://developer.doordash.com/en-US/docs/reporting/overview/about_reporting/
  properties:
  - url: https://developer.doordash.com/en-US/docs/reporting/overview/about_reporting/
    type: Documentation
  - type: OpenAPI
    url: openapi/doordash-reporting-openapi.yml
  - type: AsyncAPI
    url: asyncapi/doordash-reporting-webhooks-asyncapi.yml
  description: The DoorDash Reporting API provides approved partners with access to standardized financial, operations, and menu reporting data. It offers a POST endpoint for creating report requests and a GET endpoint for retrieving report download links, along with webhook notifications when reports are ready.
name: Doordash
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Production access to the Drive API is currently restricted, and we cannot provide a timeline for certification following development. If you have not completed development and submitted a production access request, we recommend pausing development. Contact us here to record your interest.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

