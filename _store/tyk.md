---
aid: tyk
url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/apis.yml
apis:
  - aid: tyk:tyk-dashboard-api
    name: Tyk Dashboard API
    tags:
      - Dashboards
      - API Management
    humanURL: https://tyk.io/docs/tyk-dashboard-api/
    properties:
      - url: properties/tyk-dashboard-api-openapi.yml
        type: OpenAPI
    description: >-
      The Tyk Dashboard API offers granular, programmatic access to a
      centralised database of resources that your Tyk nodes can pull from. This
      API has a dynamic user administrative structure which means the secret key
      that is used to communicate with your Tyk nodes can be kept secret and
      access to the wider management functions can be handled on a user-by-user
      and organisation-by-organisation basis.
  - aid: tyk:tyk-dashboard-admin-api
    name: Tyk Dashboard Admin API
    tags:
      - API Management
      - Dashboards
      - Administration
    humanURL: https://tyk.io/docs/dashboard-admin-api/
    properties:
      - url: properties/tyk-dashboard-admin-api-openapi.yml
        type: OpenAPI
    description: >-
      For Tyk On-Premises installations, the Dashboard Admin API provides two
      endpoints for setting up and provisioning a Tyk Dashboard instance without
      using the command line. To use the API, retrieve the admin_secret value
      from your Tyk Dashboard configuration. This secret must be included as a
      header in every Dashboard Admin API request for successful authentication.
  - aid: tyk:tyk-dashboard-admin-api
    name: Tyk Dashboard Admin API
    tags:
      - API Management
      - Dashboards
      - Administration
    humanURL: https://tyk.io/docs/dashboard-admin-api/
    properties:
      - url: properties/tyk-dashboard-admin-api-openapi.yml
        type: OpenAPI
    description: >-
      For Tyk On-Premises installations, the Dashboard Admin API provides two
      endpoints for setting up and provisioning a Tyk Dashboard instance without
      using the command line. To use the API, retrieve the admin_secret value
      from your Tyk Dashboard configuration. This secret must be included as a
      header in every Dashboard Admin API request for successful authentication.
  - aid: tyk:tyk-mdcb-api
    name: Tyk MDCB API
    tags:
      - Monitoring
      - Data Planes
      - Diagnostics
    humanURL: https://tyk.io/docs/tyk-mdcb-api/
    properties:
      - url: properties/tyk-mdcb-api-openapi.yml
        type: OpenAPI
    description: >-
      This API provides operations for monitoring Data Planes connected to MDCB
      and accessing diagnostic data. It includes endpoints for retrieving
      connected data plane details, performing health checks, and accessing Gos
      built-in pprof diagnostics for advanced performance profiling.
  - aid: tyk:tyk-gateway-api
    name: Tyk Gateway API
    tags:
      - Gateways
      - API Management
    humanURL: https://tyk.io/docs/tyk-gateway-api/
    properties:
      - url: properties/tyk-gateway-api-openapi.yml
        type: OpenAPI
    description: >+
      The Tyk Gateway API is the primary means for integrating your application
      with the Tyk API Gateway system. This API is very small, and has no
      granular permissions system. It is intended to be used purely for internal
      automation and integration.

name: Tyk
tags:
  - Management
  - Gateways
  - Portals
  - Documentation
  - Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common: []
created: '2025-01-08'
modified: '2025-02-11'
position: Consumer
description: >-
  API discovery is the process of searching for and finding API resources. It
  covers both internal and external APIs. Why use API discovery?
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---