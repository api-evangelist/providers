---
aid: dana
name: Dana
url: https://raw.githubusercontent.com/api-evangelist/dana/refs/heads/main/apis.yml
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Aftermarket
  - Auto Parts
  - Drivetrain
  - eCommerce
  - Supply Chain
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
apis:
  - aid: dana:aftermarket-api
    name: Dana Aftermarket API
    tags:
      - Aftermarket
      - Auto Parts
      - Drivetrain
      - eCommerce
      - Supply Chain
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.danaaftermarket.com
    humanURL: https://developer.danaaftermarket.com/
    properties:
      - url: https://developer.danaaftermarket.com/
        type: Portal
      - url: https://developer.danaaftermarket.com/
        type: Documentation
      - url: openapi/dana-aftermarket-api-openapi.yml
        type: OpenAPI
      - url: json-schema/part.json
        type: JSONSchema
      - url: json-schema/order.json
        type: JSONSchema
      - url: rules/dana-aftermarket-api-rules.yml
        type: Rules
      - url: capabilities/dana-aftermarket-api-capabilities.yml
        type: Capabilities
    description: The Dana Aftermarket API provides programmatic access to Dana's aftermarket e-commerce platform with eight active APIs including advanced shipping notification, availability, deep linking, order status, part details, part search by application, place order, and pricing. The APIs enable customers to display inventory availability from Dana's global distribution network, obtain real-time quotes, and manage orders with confirmation, shipping details, packing slips, and tracking numbers.
common:
  - type: Website
    url: https://www.dana.com/
  - type: Portal
    url: https://developer.danaaftermarket.com/
  - type: JSON-LD
    url: json-ld/dana-context.jsonld
  - type: Vocabulary
    url: vocabulary/dana-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
description: Dana Incorporated is a global supplier of fully integrated drivetrain and electrified propulsion systems for passenger vehicles, commercial trucks, and off-highway equipment. Dana operates a developer portal at developer.danaaftermarket.com offering eight APIs for aftermarket parts search, availability, pricing, ordering, and shipment tracking across its global distribution network.
---
