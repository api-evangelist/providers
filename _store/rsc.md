---
aid: rsc
name: RSC
description: The Royal Society of Chemistry (RSC) provides developer APIs through its ChemSpider platform, enabling programmatic access to one of the world's largest chemistry databases with over 88 million unique chemical compounds. The APIs support compound search, structure retrieval, format conversion, and data enrichment for cheminformatics applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Chemistry
  - Cheminformatics
  - Chemical Data
  - Science
created: '2025-03-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/rsc/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: rsc:chemspider-compounds
    name: ChemSpider Compounds API
    description: The ChemSpider Compounds API (v1) provides comprehensive access to the RSC ChemSpider chemical database, supporting compound filtering by name, SMILES, InChI, InChIKey, formula, molecular weight, mass, and elemental composition. Authenticated endpoints allow retrieval of compound records, external references, molecular images, and MOL files. The API also supports batch operations and chemical format conversions between SMILES, InChI, InChIKey, and Mol formats.
    humanURL: https://developer.rsc.org/
    baseURL: https://api.rsc.org/compounds/v1
    tags:
      - Chemistry
      - Cheminformatics
      - Compounds
      - Chemical Search
    properties:
      - type: Documentation
        url: https://developer.rsc.org/compounds-v1/apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rsc/refs/heads/main/openapi/rsc-chemspider-compounds-openapi.yml
    contact:
      - FN: RSC Developer Support
        url: https://developer.rsc.org/
  - aid: rsc:chemspider-tools
    name: ChemSpider Tools API
    description: The ChemSpider Tools API provides chemical format conversion utilities, supporting conversions between SMILES, InChI, InChIKey, and Mol file formats. It also includes InChIKey validation. The tools are useful for cheminformatics pipelines that need to normalize chemical identifiers across different format conventions.
    humanURL: https://developer.rsc.org/
    baseURL: https://api.rsc.org/compounds/v1
    tags:
      - Chemistry
      - Format Conversion
      - Cheminformatics
      - Tools
    properties:
      - type: Documentation
        url: https://developer.rsc.org/compounds-v1/apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rsc/refs/heads/main/openapi/rsc-chemspider-compounds-openapi.yml
common:
  - type: Portal
    url: https://developer.rsc.org/
  - type: Authentication
    url: https://developer.rsc.org/
  - type: SignUp
    url: https://developer.rsc.org/
  - type: TermsOfService
    url: https://www.rsc.org/legal/
  - type: PrivacyPolicy
    url: https://www.rsc.org/help-legal/legal/privacy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
