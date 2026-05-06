---
aid: ifs
url: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/apis.yml
apis:
  - aid: ifs:ifs-cloud-erp-api
    name: IFS Cloud ERP API
    tags:
      - Cloud
      - ERP
      - Finance
      - Manufacturing
      - Supply Chain
    image: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/image.png
    humanURL: https://www.ifs.com/
    baseURL: https://api.ifs.com
    properties:
      - url: https://www.ifs.com/
        type: Documentation
      - url: openapi/ifs-cloud-erp-openapi.yml
        type: OpenAPI
    description: IFS Cloud ERP provides REST APIs for enterprise resource planning covering financials, procurement, manufacturing, project management, and supply chain for energy, manufacturing, aerospace, and defense industries.
  - aid: ifs:ifs-field-service-management-api
    name: IFS Field Service Management API
    tags:
      - Asset Management
      - Field Service
      - Mobile
      - Scheduling
      - Work Order
    image: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/image.png
    humanURL: https://www.ifs.com/
    baseURL: https://api.ifs.com
    properties:
      - url: https://www.ifs.com/
        type: Documentation
    description: IFS Field Service Management APIs enable work order management, scheduling optimization, technician dispatch, parts inventory, and mobile workforce coordination for energy, manufacturing, and telecom field service operations.
  - aid: ifs:ifs-enterprise-asset-management-api
    name: IFS Enterprise Asset Management API
    tags:
      - Asset Management
      - EAM
      - Energy
      - Maintenance
      - Manufacturing
    image: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/image.png
    humanURL: https://www.ifs.com/
    baseURL: https://api.ifs.com
    properties:
      - url: https://www.ifs.com/
        type: Documentation
    description: IFS Enterprise Asset Management APIs provide integration with asset lifecycle management, maintenance planning, work order execution, and predictive maintenance workflows for industrial and infrastructure asset-intensive organizations.
  - aid: ifs:ifs-enterprise-service-management-api
    name: IFS Enterprise Service Management API
    tags:
      - Cloud
      - Helpdesk
      - ITSM
      - Service Management
    image: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/image.png
    humanURL: https://www.ifs.com/
    baseURL: https://api.ifs.com
    properties:
      - url: https://www.ifs.com/
        type: Documentation
    description: IFS Enterprise Service Management APIs enable IT service management, service catalog, incident management, and CMDB integration for enterprise IT and shared service organizations using the IFS Cloud platform.
common:
  aid: ifs
  name: IFS
  description: IFS is a global enterprise software company providing cloud ERP, enterprise asset management, field service management, and enterprise service management platforms. APIs enable integration with IFS Cloud across manufacturing, energy, aerospace, defense, and service industries. IFS is headquartered in Linköping, Sweden with operations in over 90 countries.
  image: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/image.png
  tags:
    - ERP
    - Field Service
    - Asset Management
    - Manufacturing
    - Energy
    - Cloud
  properties:
    - url: https://www.ifs.com/
      type: Portal
    - url: https://www.ifs.com/
      type: Documentation
    - url: https://www.ifs.com/
      type: Website
    - url: https://www.ifs.com/
      type: Support
    - url: openapi/ifs-cloud-erp-openapi.yml
      type: OpenAPI
    - url: json-schema/ifs-work-order-schema.json
      type: JSONSchema
    - url: json-ld/ifs-context.jsonld
      type: JSONLDContext
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
description: Recognized as a leading enterprise software solution provider, IFS develops and delivers ERP, EAM, FSM and ESM to businesses worldwide. From cloud technology to easy-to-use interfaces, our solutions are for customers who maintain assets, manage service operations, or manufacture and distribute goods.
---
