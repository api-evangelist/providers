---
aid: equinix
name: Equinix
description: Equinix is a global digital infrastructure company that provides interconnection and data center services to enterprises, cloud and IT service providers, and telecommunications networks worldwide. Equinix exposes a broad set of public APIs covering interconnection (Fabric), bare metal compute (Metal), Internet access, colocation operations, orders, smart hands, and authentication.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-04'
specificationVersion: '0.20'
tags:
  - Data Centers
  - Interconnection
  - Colocation
  - Bare Metal
  - Cloud Infrastructure
  - Networking
apis:
  - aid: equinix:fabric
    name: Equinix Fabric API
    description: Equinix Fabric is a software-defined interconnection solution that enables direct, secure, and dynamic connections to distributed infrastructure and digital ecosystems across the Equinix platform, including cloud service providers, enterprises, and customer-owned instances.
    humanURL: https://developer.equinix.com/catalog/fabricv4
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Interconnection
      - Fabric
      - Cloud Connectivity
      - Networking
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/fabricv4
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/fabric-openapi-original.yml
  - aid: equinix:metal
    name: Equinix Metal API
    description: Equinix Metal provides a RESTful HTTP API for programmatically managing bare metal infrastructure including devices, networks, IP addresses, organizations, projects, and user accounts. Every feature of the Equinix Metal web interface is accessible through the API.
    humanURL: https://deploy.equinix.com/developers/api/metal/
    baseURL: https://api.equinix.com/metal/v1
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Bare Metal
      - Compute
      - Cloud Infrastructure
    properties:
      - type: Documentation
        url: https://deploy.equinix.com/developers/api/metal/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/metal-openapi-original.yml
  - aid: equinix:internet-access
    name: Equinix Internet Access API
    description: Equinix Internet Access provides direct access to the Internet with scalable bandwidth options in IBX data centers. The API supports ordering and managing Internet Access services across the Equinix platform.
    humanURL: https://developer.equinix.com/catalog/eiav2
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Internet Access
      - Networking
      - Connectivity
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/eiav2
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/eia-openapi-original.yml
  - aid: equinix:lookup
    name: Equinix Lookup API
    description: The Equinix Lookup API provides reference data lookup capabilities used across Equinix services, including IBX locations, regions, and supporting metadata for ordering and provisioning workflows.
    humanURL: https://developer.equinix.com/catalog/lookupv2
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Lookup
      - Reference Data
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/lookupv2
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/lookup-openapi-original.yml
  - aid: equinix:orders
    name: Equinix Orders API
    description: The Equinix Orders API enables programmatic creation, retrieval, and management of customer orders for Equinix products and services across the global IBX footprint.
    humanURL: https://developer.equinix.com/catalog/ordersv2
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Orders
      - Provisioning
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/ordersv2
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/orders-openapi-original.yml
  - aid: equinix:order-history
    name: Equinix Order History API
    description: The Equinix Order History API provides access to historical order data and order status information across previously placed orders for Equinix services.
    humanURL: https://developer.equinix.com/catalog/orderhistoryv1
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Orders
      - Order History
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/orderhistoryv1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/orderhistory-openapi-original.yml
  - aid: equinix:secure-cabinet
    name: Equinix Secure Cabinet API
    description: The Equinix Secure Cabinet API enables management of secure colocation cabinet products, including configuration and ordering of secure cabinet services within Equinix IBX data centers.
    humanURL: https://developer.equinix.com/catalog/securecabinetv1
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Colocation
      - Secure Cabinet
      - Data Center
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/securecabinetv1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/securecabinet-openapi-original.yml
  - aid: equinix:smart-hands
    name: Equinix Smart Hands API
    description: The Equinix Smart Hands API allows customers to programmatically request on-site technical support services from Equinix engineers within the IBX data centers, including remote hands tasks, troubleshooting, and physical installations.
    humanURL: https://developer.equinix.com/catalog/smarthandsv1
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Smart Hands
      - Operations
      - Data Center
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/smarthandsv1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/smarthands-openapi-original.yml
  - aid: equinix:access-token
    name: Equinix API Authentication
    description: The Equinix API Authentication service provides OAuth 2.0 access tokens that are required to authenticate against all Equinix REST APIs in the developer catalog.
    humanURL: https://developer.equinix.com/catalog/accesstokenv1
    baseURL: https://api.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Authentication
      - OAuth
      - Security
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/accesstokenv1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/accesstoken-openapi-original.yml
  - aid: equinix:sts
    name: Equinix Security Token Service
    description: The Equinix Security Token Service issues short-lived security tokens used to authenticate workloads and services across the Equinix platform.
    humanURL: https://developer.equinix.com/catalog/stsv1alpha
    baseURL: https://sts.eqix.equinix.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Authentication
      - Security
      - Tokens
    properties:
      - type: Documentation
        url: https://developer.equinix.com/catalog/stsv1alpha
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/openapi/sts-openapi-original.yml
common:
  - type: Website
    url: https://www.equinix.com
  - type: Developer
    url: https://developer.equinix.com/
  - type: Documentation
    url: https://docs.equinix.com/
  - type: GitHub
    url: https://github.com/equinix
  - type: Features
    data:
      - 'Equinix: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Equinix Fabric, Metal, and Network Edge APIs require commercial accounts; pricing per port/cross-connect/server.
    sources:
      - https://developer.equinix.com/
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
