---
aid: eu-open-data-portal
url: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/refs/heads/main/apis.yml
apis:
- aid: eu-open-data-portal:eu-open-data-portal-sparql-api
  name: EU Open Data Portal SPARQL API
  tags:
  - EU
  - Government
  - Linked Data
  - Open Data
  - Regulatory
  - SPARQL
  image: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/refs/heads/main/image.png
  humanURL: https://data.europa.eu/
  baseURL: https://data.europa.eu/sparql
  properties:
  - url: https://data.europa.eu/sparql
    type: Documentation
  - url: https://data.europa.eu/sparql
    type: Reference
  description: The EU Open Data Portal SPARQL endpoint provides structured queries against linked open data from European Union institutions. Based on OpenLink Virtuoso, the endpoint enables querying of RDF datasets using SPARQL with output in HTML, XML, JSON, Turtle, CSV, TSV, and other formats.
- aid: eu-open-data-portal:eu-open-data-portal-search-api
  name: EU Open Data Portal Search API
  tags:
  - DCAT-AP
  - EU
  - Government
  - Open Data
  - REST
  - Search
  image: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/refs/heads/main/image.png
  humanURL: https://data.europa.eu/
  baseURL: https://data.europa.eu/api/hub/search/
  properties:
  - url: https://data.europa.eu/api/hub/search/
    type: Reference
  - url: https://dataeuropa.gitlab.io/data-provider-manual/
    type: Documentation
  - url: openapi/eu-open-data-portal-search-openapi.yml
    type: OpenAPI
  description: The EU Open Data Portal Search API provides REST access for discovering and querying European open datasets following DCAT-AP metadata standards. The API supports dataset search, filtering, and harvesting workflows for data publishers and consumers.
name: Eu Open Data Portal
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Discover the single point of access to open data from European countries, EU institutions, agencies and bodies and other European countries.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

