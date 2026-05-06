---
aid: odata
name: OData
description: OData (Open Data Protocol) is an OASIS standard that defines best practices for building and consuming RESTful APIs. It enables the creation of query-based data services over HTTP, providing a uniform way to describe data and data models, query and edit data, and perform batch operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - OASIS Standard
  - OData
  - Open Data Protocol
  - Query Language
  - RESTful APIs
url: https://raw.githubusercontent.com/api-evangelist/odata/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: odata:odata-service
    name: OData Service API
    description: Standard OData service endpoints including service document, metadata document, entity set CRUD operations, and batch processing as defined by the OData v4.01 specification.
    humanURL: https://www.odata.org/documentation/
    tags:
      - Metadata
      - OData
      - Service Document
    properties:
      - type: Documentation
        url: https://www.odata.org/documentation/
      - type: Getting Started
        url: https://www.odata.org/getting-started/
common:
  - type: Website
    url: https://www.odata.org/
  - type: Documentation
    url: https://www.odata.org/documentation/
  - type: GitHub Organization
    url: https://github.com/OData
  - type: Reference
    url: https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
