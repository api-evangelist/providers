---
aid: flower-shop-network
name: Flower Shop Network
description: Flower Shop Network is a platform that connects customers with local florists across the country. They provide an online marketplace where users can browse and purchase a wide variety of floral arrangements for all occasions, and expose a JSON API for partner POS systems to authenticate, look up products and florists, and exchange wire orders across the FSN florist network.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-24'
modified: '2026-04-28'
position: Consumer
tags:
  - Florists
  - Flowers
  - Wire Orders
  - Point of Sale
url: https://raw.githubusercontent.com/api-evangelist/flower-shop-network/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: flower-shop-network:flower-shop-network-json-api
    name: Flower Shop Network JSON API
    description: The FSN JSON API is a REST-style HTTPS interface for florist POS systems and partners to authenticate, retrieve product data, search filling florists, and send, receive, accept, refuse, and confirm wire orders.
    humanURL: https://api.flowershopnetwork.com/
    baseURL: https://api.flowershopnetwork.com/api/
    tags:
      - Florists
      - Flowers
      - Orders
      - Wire Orders
      - Point of Sale
    properties:
      - type: Documentation
        url: https://api.flowershopnetwork.com/
      - type: OpenAPI
        url: openapi/flower-shop-network-openapi.yml
common:
  - type: Website
    url: https://www.flowershopnetwork.com/
  - type: Documentation
    url: https://api.flowershopnetwork.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
