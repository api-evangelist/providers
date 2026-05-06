---
aid: shopper-approved
name: Shopper Approved
description: Shopper Approved is an e-commerce ratings and reviews platform that helps merchants collect, manage, and display verified customer reviews to improve conversion rates and build trust. The platform powers Google Seller Ratings, enabling reviews to appear in Google Shopping ads and organic search results. Shopper Approved offers a REST API for programmatic access to review data, order submission for review collection, product review management, and site statistics.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Reviews
  - Ratings
  - Ecommerce
  - Customer Feedback
  - Social Proof
url: https://raw.githubusercontent.com/api-evangelist/shopper-approved/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shopper-approved:shopper-approved-api
    name: Shopper Approved API
    description: The Shopper Approved API enables merchants to pull review data, submit orders for review collection, retrieve site statistics, manage product reviews, and update review follow-up scheduling. All API requests require a Site ID (included in the URL path) and an API token (passed as a query parameter), both available in the Shopper Approved merchant dashboard.
    humanURL: https://help.shopperapproved.com/en/articles/9796973-how-to-use-our-api
    baseURL: https://api.shopperapproved.com
    tags:
      - Reviews
      - Ratings
      - Ecommerce
      - Customer Feedback
    properties:
      - type: Documentation
        url: https://help.shopperapproved.com/en/articles/9796973-how-to-use-our-api
      - type: HelpCenter
        url: https://help.shopperapproved.com/en/collections/10456439-api
      - type: Authentication
        url: https://help.shopperapproved.com/en/articles/9796973-how-to-use-our-api
      - type: Website
        url: https://www.shopperapproved.com/
      - type: OpenAPI
        url: openapi/shopper-approved-openapi.yml
      - type: JSONSchema
        url: json-schema/shopper-approved-review-schema.json
      - type: JSONSchema
        url: json-schema/shopper-approved-product-review-schema.json
      - type: JSONStructure
        url: json-structure/shopper-approved-review-structure.json
      - type: JSONLD
        url: json-ld/shopper-approved-context.jsonld
      - type: SpectralRules
        url: rules/shopper-approved-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/review-management.yaml
      - type: Vocabulary
        url: vocabulary/shopper-approved-vocabulary.yml
    contact:
      - FN: Shopper Approved Support
        url: https://help.shopperapproved.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
