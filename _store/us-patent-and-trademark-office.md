---
aid: us-patent-and-trademark-office
url: https://raw.githubusercontent.com/api-evangelist/us-patent-and-trademark-office/refs/heads/main/apis.yml
apis:
  - aid: us-patent-and-trademark-office:open-data-portal-api
    name: USPTO Open Data Portal API
    tags:
      - Patents
      - Trademarks
      - Intellectual Property
      - Federal Government
      - Open Data
    humanURL: https://data.uspto.gov/apis/getting-started
    properties:
      - url: https://data.uspto.gov/apis/getting-started
        type: Documentation
      - url: https://data.uspto.gov/swagger/swagger.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/us-patent-and-trademark-office/refs/heads/main/openapi/uspto-open-data-portal-openapi.yml
        type: OpenAPI
    description: The USPTO Open Data Portal (ODP) API allows public users to discover, search, and extract USPTO patent, trademark, PTAB trial, petition decision, and bulk dataset information at no cost. Requires an ODP API key passed via the X-API-KEY header.
  - aid: us-patent-and-trademark-office:tsdr-api
    name: USPTO Trademark Status and Document Retrieval API
    tags:
      - Trademarks
      - Intellectual Property
      - Federal Government
      - Open Data
    humanURL: https://developer.uspto.gov/api-catalog/tsdr-data-api
    properties:
      - url: https://developer.uspto.gov/api-catalog/tsdr-data-api
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-patent-and-trademark-office/refs/heads/main/openapi/uspto-tsdr-openapi.yml
        type: OpenAPI
    description: The Trademark Status and Document Retrieval (TSDR) REST API provides programmatic access to trademark case status, documents, case images, and related metadata. Requires an API key for bulk data downloads.
name: US Patent and Trademark Office
tags:
  - Federal Government
  - Patents
  - Trademarks
  - Intellectual Property
  - Open Data
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The US Patent and Trademark Office (USPTO) is responsible for granting patents and registering trademarks to protect intellectual property in the United States. The USPTO examines patent applications to determine if an invention is new, non-obvious, and useful, and grants patents to those that meet the criteria. They also register trademarks, which are words, phrases, symbols, or designs that distinguish goods or services of one entity from another. The USPTO Open Data Portal provides free programmatic access to patent applications, PTAB trial proceedings, petition decisions, trademark status, and bulk datasets.
features:
  - Patent Application Search
  - Patent File Wrapper Access
  - PTAB Trial Proceedings Search
  - Petition Decision Search
  - Trademark Status Retrieval
  - Trademark Document Retrieval
  - Bulk Dataset Downloads
useCases:
  - Patent research and prior art searches
  - Trademark availability checking
  - PTAB trial monitoring
  - IP portfolio management
  - Legal and compliance research
  - Academic and economic research
integrations:
  - data.gov
  - api.data.gov
solutions:
  - Intellectual Property Management
  - Patent Search and Analytics
  - Trademark Monitoring
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
