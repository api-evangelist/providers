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
common:
  aid: eu-open-data-portal
  name: EU Open Data Portal
  description: The EU Open Data Portal (data.europa.eu) is the official portal for European Union open data, operated by the Publications Office of the European Union. It provides SPARQL and REST APIs for accessing statistical datasets, legislative documents, and institutional data from EU institutions under open licenses.
  image: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/refs/heads/main/image.png
  tags:
    - Government
    - Open Data
    - SPARQL
    - EU
    - Regulatory
    - Linked Data
  properties:
    - url: https://data.europa.eu/
      type: Portal
    - url: https://dataeuropa.gitlab.io/data-provider-manual/
      type: Documentation
    - url: https://data.europa.eu/sparql
      type: Getting Started
    - url: https://data.europa.eu/en/legal-notice
      type: Terms of Service
    - url: https://data.europa.eu/en/legal-notice
      type: Privacy Policy
    - url: https://data.europa.eu/
      type: Website
    - url: openapi/eu-open-data-portal-search-openapi.yml
      type: OpenAPI
    - url: json-schema/eu-open-data-portal-dataset-schema.json
      type: JSONSchema
    - url: json-ld/eu-open-data-portal-context.jsonld
      type: JSONLDContext
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
description: Discover the single point of access to open data from European countries, EU institutions, agencies and bodies and other European countries.
---
