---
aid: consumer-product-safety-commission
name: Consumer Product Safety Commission
url: https://raw.githubusercontent.com/api-evangelist/consumer-product-safety-commission/refs/heads/main/apis.yml
tags:
  - Consumer Protection
  - Federal Government
  - Hazards
  - Open Data
  - Product Safety
  - Recalls
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
access: 3rd-Party
created: '2024-12-25'
modified: '2026-04-29'
position: Consumer
specificationVersion: '0.19'
x-type: government
description: The U.S. Consumer Product Safety Commission (CPSC) is the federal agency responsible for protecting the public from unreasonable risks of injury or death associated with consumer products such as toys, household items, electronics, and furniture. CPSC publishes a public, unauthenticated Recalls Retrieval Web Service that exposes recall records (with products, hazards, manufacturers, retailers, distributors, importers, and remedies) in JSON or XML, plus the SaferProducts.gov OData service for incident-report data accessed by application key.
apis:
  - aid: consumer-product-safety-commission:recalls
    name: CPSC Recalls API
    tags:
      - JSON
      - Open Data
      - Recalls
      - REST
      - XML
    humanURL: https://www.cpsc.gov/Recalls/CPSC-Recalls-Application-Program-Interface-API-Information
    baseURL: https://www.saferproducts.gov/RestWebServices
    properties:
      - url: https://www.cpsc.gov/Recalls/CPSC-Recalls-Application-Program-Interface-API-Information
        type: Documentation
      - url: https://cpsc.gov/s3fs-public/RecallRetrievalWebServicesProgrammersGuide20180917.pdf
        type: Reference
      - url: openapi/cpsc-recalls-openapi.yml
        type: OpenAPI
    description: Public REST web service that returns CPSC recall records published on cpsc.gov. Supports case-insensitive wildcard search across recall number, date, product type, hazard, country, manufacturer, retailer, importer, distributor, and UPC. Output is available as JSON or XML and the API requires no authentication.
  - aid: consumer-product-safety-commission:saferproducts
    name: SaferProducts.gov OData API
    tags:
      - Incident Reports
      - OData
      - Open Data
    humanURL: https://www.saferproducts.gov/FAQs/FrequentlyAskedQuestions11
    baseURL: https://www.saferproducts.gov/WebApi/Cpsc.Cpsrms.Web.Api.svc
    properties:
      - url: https://www.saferproducts.gov/FAQs/FrequentlyAskedQuestions11
        type: Documentation
      - url: https://www.saferproducts.gov/WebApi/Cpsc.Cpsrms.Web.Api.svc/$metadata
        type: Reference
    description: OData web service exposing publicly published consumer product incident-report data submitted through SaferProducts.gov. Authenticated with a basic-auth header where the registered application key is sent as the username (no password).
common:
  - type: Website
    url: https://www.cpsc.gov/
  - type: Recalls
    url: https://www.cpsc.gov/Recalls
  - type: Data
    url: https://www.cpsc.gov/Data
  - type: SaferProducts.gov
    url: https://www.saferproducts.gov/
  - type: Public Search
    url: https://www.saferproducts.gov/PublicSearch
  - type: Programmers Guide
    url: https://cpsc.gov/s3fs-public/RecallRetrievalWebServicesProgrammersGuide20180917.pdf
  - type: Privacy Policy
    url: https://www.cpsc.gov/Newsroom/Privacy-and-Security-Statement
  - type: Terms of Service
    url: https://www.cpsc.gov/Newsroom/Privacy-and-Security-Statement
  - type: JSON-LD
    url: json-ld/consumer-product-safety-commission-context.jsonld
  - type: JSONSchema
    url: json-schema/cpsc-recall-schema.json
  - type: Spectral
    url: rules/consumer-product-safety-commission-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/consumer-product-safety-commission-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
