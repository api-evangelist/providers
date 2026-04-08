---
aid: meddra
url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/apis.yml
apis:
- aid: meddra:meddra-api
  name: MedDRA / WHO Drug Dictionary API
  tags:
  - Adverse Events
  - Coding
  - Medical Terminology
  - Pharma
  image: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/image.png
  humanURL: https://www.meddra.org/
  baseURL: https://api.meddra.example.com
  properties:
  - url: https://www.meddra.org/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/openapi/meddra-terminology-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/json-schema/meddra-term-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/json-ld/meddra-context.jsonld
    type: JSONLDContext
  description: MedDRA (Medical Dictionary for Regulatory Activities) and the WHO Drug Dictionary provide standardized medical terminology APIs for adverse event coding, drug safety reporting, and pharmacovigilance. APIs enable term lookup, hierarchy navigation, and coding validation for regulatory submissions.
name: Meddra
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: MedDRA (Medical Dictionary for Regulatory Activities) is a clinically validated international medical terminology dictionary used by regulatory authorities and the regulated biopharmaceutical industry.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

