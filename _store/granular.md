---
aid: granular
url: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/apis.yml
apis:
  - aid: granular:granular-farm-management-api
    name: Granular Farm Management API
    tags:
      - Agriculture
      - AgriForce
      - Corteva
      - Crop Planning
      - Farm Management
      - Financial
    image: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/image.png
    humanURL: https://granular.ag/
    baseURL: https://api.granular.ag
    properties:
      - url: https://granular.ag/
        type: Documentation
      - url: openapi/granular-farm-management-openapi.yml
        type: OpenAPI
    description: Granular (now part of Corteva Agriscience) provides farm management software APIs for crop planning, field records, financial analysis, and operational tracking. APIs enable access to field-level production data, input cost tracking, and agronomic decision support for agriculture enterprises.
  - aid: granular:granular-insights-api
    name: Granular Insights API
    tags:
      - Agriculture
      - Agronomy
      - Analytics
      - Corteva
      - Farm Management
    image: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/image.png
    humanURL: https://us.app.granular.ag/
    baseURL: https://api.granular.ag
    properties:
      - url: https://us.app.granular.ag/
        type: Documentation
    description: Granular Insights provides analytics and reporting APIs for farm operations, enabling agronomic analysis, yield benchmarking, and field performance reporting for precision agriculture workflows.
common:
  aid: granular
  name: Granular (Corteva Agriscience)
  description: Granular is a farm management platform now part of Corteva Agriscience, providing APIs for crop planning, field records management, financial analysis, and farm operational tracking. The platform serves commercial agriculture operations with data-driven decision support tools.
  image: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/image.png
  tags:
    - Agriculture
    - Farm Management
    - Financial
    - Crop Planning
    - Agronomy
  properties:
    - url: https://granular.ag/
      type: Portal
    - url: https://granular.ag/
      type: Documentation
    - url: https://granular.ag/
      type: Website
    - url: https://www.corteva.com/
      type: Website
    - url: openapi/granular-farm-management-openapi.yml
      type: OpenAPI
    - url: json-schema/granular-field-schema.json
      type: JSONSchema
    - url: json-ld/granular-context.jsonld
      type: JSONLDContext
    - url: granular-rules.yml
      type: Rules
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
---
