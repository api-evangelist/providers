---
aid: sigma-aldrich
url: https://raw.githubusercontent.com/api-evangelist/sigma-aldrich/refs/heads/main/apis.yml
apis:
  - aid: sigma-aldrich:sigma-aldrich-product-api
    name: Sigma-Aldrich Product Search API
    tags:
      - Life Science
      - Chemistry
      - Products
      - Search
    humanURL: https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/chemistry/labware/sigma-aldrich-developer-portal
    properties:
      - url: https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/chemistry/labware/sigma-aldrich-developer-portal
        type: Documentation
      - url: openapi/sigma-aldrich-product-openapi.yml
        type: OpenAPI
      - url: rules/sigma-aldrich-rules.yml
        type: SpectralRules
      - url: capabilities/chemical-research.yaml
        type: Capabilities
      - url: json-schema/sigma-aldrich-product-schema.json
        type: JSONSchema
      - url: json-ld/sigma-aldrich-context.jsonld
        type: JSONLD
      - url: vocabulary/sigma-aldrich-vocabulary.yml
        type: Vocabulary
    description: The Sigma-Aldrich Product Search API provides programmatic access to the Sigma-Aldrich product catalog containing hundreds of thousands of chemical compounds, reagents, biochemicals, and laboratory supplies. Researchers and laboratory information management systems (LIMS) can query products by CAS number, catalog number, product name, or chemical structure (SMILES notation) to retrieve product details, safety data, pricing, and availability information.
  - aid: sigma-aldrich:sigma-aldrich-structure-search-api
    name: Sigma-Aldrich Chemical Structure Search API
    tags:
      - Chemistry
      - Cheminformatics
      - Structure Search
      - SMILES
    humanURL: https://www.sigmaaldrich.com/US/en/support/contact-us
    properties:
      - url: https://www.sigmaaldrich.com/US/en/support/contact-us
        type: Documentation
    description: The Sigma-Aldrich Chemical Structure Search API enables substructure, exact structure, and similarity searches against the Sigma-Aldrich chemical catalog using SMILES, InChI, or molecular formula notation. Supports configuring similarity thresholds and returning ranked results for drug discovery, materials research, and synthetic chemistry workflows.
  - aid: sigma-aldrich:sigma-aldrich-sds-api
    name: Sigma-Aldrich Safety Data Sheet API
    tags:
      - Safety
      - SDS
      - GHS
      - Compliance
    humanURL: https://www.sigmaaldrich.com/US/en/support/sds-portal
    properties:
      - url: https://www.sigmaaldrich.com/US/en/support/sds-portal
        type: Documentation
    description: The Safety Data Sheet (SDS) API provides programmatic access to GHS- compliant Safety Data Sheets for all Sigma-Aldrich chemical products. Enables EHS systems, LIMS platforms, and safety management software to retrieve current SDSs in multiple languages and formats for regulatory compliance and laboratory safety management.
name: Sigma-Aldrich
tags:
  - Life Science
  - Chemistry
  - Biochemistry
  - Laboratory
  - Research
  - Chemical Catalog
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-05-02'
position: Consuming
segments:
  - Life Science
  - Chemistry
  - Research Tools
description: Sigma-Aldrich was a leading life science and high technology company whose biochemical and organic chemical products, kits, and services are used in scientific research, including genomics, proteomics, and drug discovery. Acquired by Merck KGaA in 2015, Sigma-Aldrich now operates as part of MilliporeSigma in North America and Merck in other regions, continuing to provide the world's largest catalog of research chemicals, biochemicals, laboratory equipment, and life science products to researchers globally.
common:
  - type: Website
    url: https://www.sigmaaldrich.com/
  - type: ProductCatalog
    url: https://www.sigmaaldrich.com/US/en/catalog
  - type: SDS Portal
    url: https://www.sigmaaldrich.com/US/en/support/sds-portal
  - type: Developer Portal
    url: https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/chemistry/labware/sigma-aldrich-developer-portal
  - type: Parent Company
    url: https://www.merckgroup.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
