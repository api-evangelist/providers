---
aid: volkswagen
name: Volkswagen
url: https://productdata.volkswagenag.com/
description: Volkswagen is a German automotive company and the parent of the VW Group, manufacturing vehicles under brands including Volkswagen, Audi, SEAT, Skoda, CUPRA, Porsche, Lamborghini, and Bentley. The OKAPI (Open Konfigurator API) provides programmatic access to VW AG product data for vehicle catalog browsing, interactive configuration, buildability validation, WLTP emissions data, configuration images, and order/pricing information across global markets.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-25'
modified: '2026-05-03'
position: Consumer
tags:
  - Automobiles
  - Cars
  - Vehicles
  - Automotive
  - Vehicle Configuration
specificationVersion: '0.19'
apis:
  - aid: volkswagen:volkswagen-okapi
    name: Volkswagen OKAPI - Open Konfigurator API
    description: The VW OKAPI API provides access to Volkswagen AG product data and vehicle configuration services across global markets. Catalog endpoints (GET) browse countries, brands, models, types, and options. Operation endpoints (POST) handle buildability checking, configuration recovery, interactive configuration, resolution, WLTP emissions data, vehicle images, and order information with pricing.
    humanURL: https://productdata.volkswagenag.com/
    baseURL: https://productdata.volkswagenag.com/v3
    tags:
      - Automobiles
      - Vehicle Configuration
      - Konfigurator
      - Product Data
    properties:
      - url: https://productdata.volkswagenag.com/swagger-doc.html
        type: Documentation
      - url: https://productdata.volkswagenag.com/tutorial.html
        type: GettingStarted
      - url: openapi/volkswagen-okapi-openapi.yml
        type: OpenAPI
      - url: json-schema/volkswagen-vehicle-config-schema.json
        type: JSONSchema
common:
  - name: Volkswagen OKAPI - Whats New
    description: Release notes and updates for the OKAPI API.
    url: https://productdata.volkswagenag.com/whats-new.html
    type: WhatsNew
  - name: Volkswagen OKAPI Guide
    description: Tutorial and guide for using the OKAPI API.
    url: https://productdata.volkswagenag.com/introduction.html
    type: Guide
  - name: Volkswagen OKAPI - Support
    description: Support resources for OKAPI API users.
    url: https://productdata.volkswagenag.com/support.html
    type: Support
  - name: Volkswagen OKAPI Terms and Condition of Use
    description: Terms and conditions for OKAPI API access.
    url: https://productdata.volkswagenag.com/condition-of-use.html
    type: TermsOfService
  - name: Volkswagen OKAPI Developer Portal
    description: Developer registration and API key management.
    url: https://okapi-ddp.productdata.volkswagenag.com/dev-portal/
    type: Portal
  - type: OpenAPI
    url: openapi/volkswagen-okapi-openapi.yml
  - type: JSONSchema
    url: json-schema/volkswagen-vehicle-config-schema.json
  - type: JSONStructure
    url: json-structure/volkswagen-vehicle-config-structure.json
  - type: JSON-LD
    url: json-ld/volkswagen-context.jsonld
  - type: Vocabulary
    url: vocabulary/volkswagen-vocabulary.yml
  - type: SpectralRules
    url: rules/volkswagen-rules.yml
  - type: NaftikoCapability
    url: capabilities/vehicle-configuration.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
