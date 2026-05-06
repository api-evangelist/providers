---
aid: clickpost
name: ClickPost
url: https://raw.githubusercontent.com/api-evangelist/clickpost/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-26'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - Carriers
  - Delivery
  - E-Commerce Logistics
  - Logistics
  - Returns
  - Shipping
  - Supply Chain
  - Tracking
description: ClickPost is a logistics and supply chain platform that aggregates 500+ carrier integrations, multi-channel customer notifications, and 50+ storefront/OMS/WMS connectors behind a unified REST API. The platform covers carrier recommendation, order creation (single and multi-piece), serviceability, manifesting, pickups, real-time tracking with webhooks, proof of delivery, NDR (non-delivery report) management, returns, and expected delivery date forecasting for both Indian domestic and international shipments.
apis:
  - aid: clickpost:clickpost-api
    name: ClickPost API
    tags:
      - Logistics
      - Shipping
      - Tracking
    humanURL: https://docs.clickpost.ai/docs/getting-started
    properties:
      - url: https://docs.clickpost.ai/docs/getting-started
        type: Documentation
      - url: https://docs.clickpost.ai/
        type: Portal
    description: ClickPost's REST API provides programmatic access to carrier recommendation, order creation, cancellation, serviceability, manifesting, pickup scheduling, tracking (polling and webhooks), proof of delivery, NDR action management, returns, expected delivery date prediction, PUDO services, and rider/quick-commerce operations. Authentication is token-based.
common:
  - type: Website
    url: https://www.clickpost.ai
  - type: Documentation
    url: https://docs.clickpost.ai/
  - type: Carrier Integrations
    url: https://www.clickpost.ai/carrier-integration
  - type: Privacy Policy
    url: https://www.clickpost.ai/privacy-policy
  - type: Terms of Service
    url: https://www.clickpost.ai/terms-and-conditions
  - type: JSON-LD
    url: json-ld/clickpost-context.jsonld
  - type: Spectral
    url: rules/clickpost-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clickpost-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
