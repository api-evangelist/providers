---
aid: fake-store-api
name: Fake Store API
description: Fake Store API is a tool that allows users to access a database of fake products, customers, and orders. Users can use the API to generate test data for their e-commerce applications or to practice integrating with external APIs. The Fake Store API provides a simple and easy-to-use interface for retrieving information such as product details, customer information, and order history.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Customers
  - Fake Data
  - Orders
  - Products
  - Synthetic Data
url: https://raw.githubusercontent.com/api-evangelist/fake-store-api/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: fake-store-api:fake-store-api
    name: Fake Store API
    description: Public REST API for prototyping and teaching e-commerce integrations. Exposes products, carts, users, and authentication endpoints. Write operations return fabricated responses without persisting data on the server, making it safe for demos and integration testing.
    humanURL: https://fakestoreapi.com/
    baseURL: https://fakestoreapi.com
    tags:
      - Customers
      - Fake Data
      - Orders
      - Products
      - Synthetic Data
    properties:
      - type: Documentation
        url: https://fakestoreapi.com/docs
      - type: Website
        url: https://fakestoreapi.com/
      - type: OpenAPI
        url: openapi/fake-store-api-openapi.yml
common:
  - type: Website
    url: https://fakestoreapi.com/
  - type: Documentation
    url: https://fakestoreapi.com/docs
  - type: GitHub Repository
    url: https://github.com/keikaavousi/fake-store-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
