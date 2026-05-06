---
aid: medidata
url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/apis.yml
apis:
  - aid: medidata:medidata-api
    name: Medidata Rave EDC API
    tags:
      - Clinical Trials
      - Data Capture
      - EDC
      - Pharma
    image: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/image.png
    humanURL: https://www.medidata.com/
    baseURL: https://api.medidata.example.com
    properties:
      - url: https://www.medidata.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/openapi/medidata-rave-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/json-schema/medidata-subject-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/json-ld/medidata-context.jsonld
        type: JSONLDContext
    description: Medidata Rave provides electronic data capture (EDC) APIs for clinical trial data collection and management. APIs enable access to study designs, case report forms, patient data, queries, and audit trails for clinical research organizations and pharmaceutical companies.
common:
  - url: https://www.medidata.com/
    type: Portal
  - url: https://www.medidata.com/
    type: Website
  - url: https://www.medidata.com/en/life-science-resources/medidata-blog/
    type: Blog
  - url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/openapi/medidata-rave-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/json-schema/medidata-subject-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/medidata/refs/heads/main/json-ld/medidata-context.jsonld
    type: JSONLDContext
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-03-18'
description: Medidata powers smarter clinical trials with unified data, AI-driven insights, and patient-centric technology to accelerate research.
---
