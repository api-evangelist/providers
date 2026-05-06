---
aid: weis-markets
url: https://raw.githubusercontent.com/api-evangelist/weis-markets/refs/heads/main/apis.yml
modified: '2026-05-03'
description: Weis Markets is a regional supermarket chain operating grocery stores in the mid-Atlantic United States, with 197 store locations across Pennsylvania, Maryland, Delaware, New Jersey, New York, Virginia, and West Virginia. The company operates a digital commerce platform, loyalty rewards program (Weis Rewards), mobile app, and vendor/supplier integration ecosystem using EDI and supply chain APIs. Weis Markets uses Toshiba ELERA commerce platform for unified in-store and online commerce.
common:
  - type: Website
    url: https://www.weismarkets.com
  - type: VendorPortal
    url: https://weismarkets.streamcollab.com/
  - type: MobileApp
    url: https://www.weismarkets.com/wendys-app
  - type: GitHubOrg
    url: https://github.com/weis-markets
  - type: JSONLDContext
    url: json-ld/weis-markets-context.jsonld
  - type: Vocabulary
    url: vocabulary/weis-markets-vocabulary.yml
apis:
  - aid: weis-markets:vendor-integration-api
    name: Weis Markets Vendor Integration API
    tags:
      - Grocery
      - Retail
      - Supply Chain
      - EDI
      - Vendor Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://weismarkets.streamcollab.com
    humanURL: https://www.weismarkets.com/vendor-partners
    description: The Weis Markets Vendor Integration API enables supplier and vendor partners to exchange purchase orders, invoices, item management data, and vendor contact information electronically. The platform uses the Biceps purchase order system with EDI connectivity and supports vendor deal submissions, item setup, and performance monitoring. Third-party EDI providers such as Vantree, TrueCommerce, and eZCom Software can automate workflows for vendors connecting to the Weis Markets supply chain network.
    properties:
      - url: https://www.weismarkets.com/vendor-partners
        type: Documentation
      - url: https://weismarkets.streamcollab.com/
        type: Portal
      - url: examples/weis-markets-vendor-purchase-order-example.json
        type: Example
  - aid: weis-markets:loyalty-rewards-api
    name: Weis Markets Loyalty Rewards API
    tags:
      - Grocery
      - Retail
      - Loyalty
      - Rewards
      - Digital Commerce
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.weismarkets.com
    humanURL: https://www.weismarkets.com
    description: The Weis Markets Loyalty Rewards API supports the Weis Rewards program, enabling digital loyalty card management, points accumulation, personalized offers, and integration with third-party platforms including Amazon. The program is powered by Birdzi analytics and CitrusAd digital advertising, providing customer insights and targeted promotions through the Weis Markets mobile app and e-grocery website (Mercatus-powered).
    properties:
      - url: https://www.weismarkets.com/wendys-app
        type: Documentation
---
