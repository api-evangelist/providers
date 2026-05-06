---
aid: microsoft-azure-cdn
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-cdn:rest-api
    name: Azure CDN REST API
    tags:
      - Caching
      - CDN
      - Content Delivery
      - Edge
      - Performance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/cdn/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/cdn/
        type: Documentation
    description: Azure CDN REST API enables management of content delivery network profiles, endpoints, and custom domains. It supports configuring caching rules, compression, geo-filtering, custom HTTPS, and purging cached content across global edge locations.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
created: '2026-03-13'
modified: '2026-04-28'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
description: The Azure Content Delivery Network (CDN) caches static web content at strategically placed locations to provide maximum throughput for delivering content to users.
---
