---
aid: denodo
name: Denodo
description: Denodo is a leading data virtualization platform that enables real-time access, integration, and delivery of data from disparate sources across enterprise data landscapes. The Denodo Platform exposes a portfolio of REST, OData, GraphQL, and SOAP web service endpoints through Virtual DataPort, the Data Catalog, the Solution Manager, and the Scheduler so that data products can be published, governed, and administered programmatically.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Catalog
  - Data Fabric
  - Data Mesh
  - Data Virtualization
  - GraphQL
  - Logical Data Warehouse
  - OData
  - REST
  - Scheduler
  - Solution Manager
url: https://raw.githubusercontent.com/api-evangelist/denodo/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Producer
access: 3rd-Party
apis:
  - aid: denodo:solution-manager-api
    name: Denodo Solution Manager REST API
    description: The Solution Manager REST API provides programmatic access to administer the Denodo Platform across environments and clusters. It exposes endpoints for cluster lifecycle management, environment configuration, deployment of revisions across servers (VDP, SCHEDULER, VDP_DATA_CATALOG), monitoring, license management, and permissions administration. Most operations require HTTP Basic authentication or token-based authentication.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://community.denodo.com/docs/html/browse/latest/en/solution_manager/administration/appendix/rest_api/rest_api
    baseURL: https://solution-manager.example.com/solution-manager
    tags:
      - Administration
      - Clusters
      - Deployment
      - Environments
      - Solution Manager
    properties:
      - type: Documentation
        url: https://community.denodo.com/docs/html/browse/latest/en/solution_manager/administration/appendix/rest_api/rest_api
      - type: Reference
        url: https://community.denodo.com/docs/html/browse/9.4/en/solution_manager/administration/appendix/rest_api/rest_api
    contact:
      - FN: Denodo Support
        email: support@denodo.com
        url: https://support.denodo.com
  - aid: denodo:data-catalog-api
    name: Denodo Data Catalog REST API
    description: The Denodo Data Catalog REST API provides programmatic access to the catalog of virtual views, web services, search, lineage, tags, categories, and certifications managed by the Denodo Platform. It powers metadata exploration, data product publishing, and governance workflows. Interactive documentation is available via Swagger at /denodo-data-catalog/swagger-ui/index.html.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://community.denodo.com/docs/html/browse/latest/en/vdp/data_catalog/appendix/rest_api/rest_api
    baseURL: https://denodo.example.com/denodo-data-catalog
    tags:
      - Catalog
      - Data Catalog
      - Governance
      - Metadata
      - Search
    properties:
      - type: Documentation
        url: https://community.denodo.com/docs/html/browse/latest/en/vdp/data_catalog/appendix/rest_api/rest_api
      - type: Swagger
        url: https://community.denodo.com/docs/html/browse/9.0/en/vdp/data_catalog/appendix/rest_api/rest_api
    contact:
      - FN: Denodo Support
        email: support@denodo.com
        url: https://support.denodo.com
  - aid: denodo:rest-web-service
    name: Denodo RESTful Web Service
    description: The Denodo RESTful Web Service exposes any view in Virtual DataPort as a resource-oriented REST endpoint. It supports JSON, XML, and HTML representations, query filtering, projection, pagination, and HATEOAS navigation between associated views. The same RESTful approach is used to publish custom REST Web services declared via VQL.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://community.denodo.com/docs/html/browse/latest/en/vdp/administration/restful_architecture/restful_architecture
    baseURL: https://denodo.example.com/denodo-restfulws
    tags:
      - HATEOAS
      - REST
      - Virtual DataPort
      - Web Services
    properties:
      - type: Documentation
        url: https://community.denodo.com/docs/html/browse/latest/en/vdp/administration/restful_architecture/restful_architecture
      - type: Tutorial
        url: https://community.denodo.com/tutorials/browse/dataservices/2rest
    contact:
      - FN: Denodo Support
        email: support@denodo.com
        url: https://support.denodo.com
  - aid: denodo:odata-service
    name: Denodo OData 4.0 Service
    description: The Denodo OData 4.0 service provides an OASIS OData v4 compliant interface for querying Virtual DataPort views over HTTP. It supports filter, select, expand, orderby, top, and skip query options as well as service metadata documents and entity navigation between related views.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://community.denodo.com/docs/html/browse/latest/en/vdp/administration/restful_architecture/odata_4_service/odata_4_service
    baseURL: https://denodo.example.com/denodo-odata4-service
    tags:
      - OData
      - Query
      - REST
      - Virtual DataPort
    properties:
      - type: Documentation
        url: https://community.denodo.com/docs/html/browse/latest/en/vdp/administration/restful_architecture/odata_4_service/odata_4_service
    contact:
      - FN: Denodo Support
        email: support@denodo.com
        url: https://support.denodo.com
  - aid: denodo:graphql-service
    name: Denodo GraphQL Service
    description: The Denodo GraphQL Service enables clients to execute GraphQL queries against virtual views in the Denodo Platform. It generates a GraphQL schema from selected views and supports filtering, pagination, and field selection through standard GraphQL syntax over HTTP.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://community.denodo.com/docs/html/browse/latest/en/vdp/administration/restful_architecture/graphql_service/graphql_service
    baseURL: https://denodo.example.com/denodo-graphql-service
    tags:
      - GraphQL
      - Query
      - Virtual DataPort
    properties:
      - type: Documentation
        url: https://community.denodo.com/docs/html/browse/latest/en/vdp/administration/restful_architecture/graphql_service/graphql_service
    contact:
      - FN: Denodo Support
        email: support@denodo.com
        url: https://support.denodo.com
  - aid: denodo:scheduler-rest-api
    name: Denodo Scheduler REST API
    description: The Denodo Scheduler REST API allows programmatic management and monitoring of scheduled jobs and projects in the Denodo Scheduler component. Endpoints support listing, creating, executing, cancelling jobs and retrieving their status, history, and configuration.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://community.denodo.com/docs/html/browse/latest/en/scheduler/administration/scheduler_rest_web_service/scheduler_rest_web_service
    baseURL: https://denodo.example.com/webadmin/denodo-scheduler-admin
    tags:
      - Jobs
      - Scheduler
      - Workflow
    properties:
      - type: Documentation
        url: https://community.denodo.com/docs/html/browse/latest/en/scheduler/administration/scheduler_rest_web_service/scheduler_rest_web_service
    contact:
      - FN: Denodo Support
        email: support@denodo.com
        url: https://support.denodo.com
common:
  - type: Website
    url: https://www.denodo.com
  - type: Portal
    url: https://community.denodo.com/
  - type: Documentation
    url: https://community.denodo.com/docs/
  - type: Knowledge Base
    url: https://community.denodo.com/kb/
  - type: Tutorials
    url: https://community.denodo.com/tutorials/
  - type: Express Edition
    url: https://www.denodo.com/en/denodo-platform/free-trials
  - type: Pricing
    url: https://www.denodo.com/en/pricing
  - type: Support
    url: https://support.denodo.com/
  - type: Status
    url: https://www.denodo.com/en/legal/denodo-trust-center
  - type: Blog
    url: https://www.denodo.com/en/blog
  - type: Customers
    url: https://www.denodo.com/en/customers
  - type: Partners
    url: https://www.denodo.com/en/partners
  - type: Training
    url: https://www.denodo.com/en/services/training
  - type: GitHub Organization
    url: https://github.com/denodo
  - type: Terms of Service
    url: https://www.denodo.com/en/legal/legal-notice
  - type: Privacy Policy
    url: https://www.denodo.com/en/legal/privacy-policy
  - type: Security
    url: https://www.denodo.com/en/legal/denodo-trust-center
  - type: JSON-LD
    url: json-ld/denodo-context.jsonld
  - type: Vocabulary
    url: vocabulary/denodo-vocabulary.yml
  - type: Capabilities
    url: capabilities/denodo-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
