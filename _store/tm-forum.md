---
aid: tm-forum
name: TM Forum
description: TM Forum is a global industry association that helps communications service providers (CSPs) and technology suppliers to digitally transform and thrive in the digital economy. Through collaboration across 850+ member organizations in 180 countries, TM Forum develops the Open API suite — a portfolio of 88+ standardized REST APIs (Apache 2.0 licensed) covering the full telecommunications business support systems (BSS) and operations support systems (OSS) landscape, including product catalog, ordering, customer management, inventory, billing, network resources, and partner management. The Open APIs implement consistent REST/JSON patterns aligned to the TM Forum Information Framework (SID) and enable interoperability across telecom ecosystems.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Telco
  - Telecommunications
  - BSS
  - OSS
  - Open APIs
  - Standards
created: '2024-11-27'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tm-forum/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tm-forum:tmf620-product-catalog
    name: TMF620 Product Catalog Management
    description: The Product Catalog Management API provides a consistent set of mechanisms to manage product offerings, product specifications, and product catalog entries across telecom BSS systems. Covers catalog creation, product offering management, pricing, and lifecycle management.
    humanURL: https://www.tmforum.org/resources/specification/tmf620-product-catalog-management-api-rest-specification-r17-5-0/
    tags:
      - Product Catalog
      - BSS
    properties:
      - type: Documentation
        url: https://www.tmforum.org/resources/specification/tmf620-product-catalog-management-api-rest-specification-r17-5-0/
      - type: OpenAPI
        url: openapi/tm-forum-tmf620-product-catalog-openapi.yaml
  - aid: tm-forum:tmf621-trouble-ticket
    name: TMF621 Trouble Ticket Management
    description: The Trouble Ticket API provides standardized access to telecom trouble ticket management functions including incident creation, tracking, routing, and resolution across network and customer-facing support systems.
    humanURL: https://github.com/tmforum-apis/TMF621_TroubleTicket
    tags:
      - Trouble Ticket
      - OSS
      - Incident Management
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF621_TroubleTicket
      - type: OpenAPI
        url: openapi/tm-forum-tmf621-trouble-ticket-openapi.yaml
  - aid: tm-forum:tmf622-product-ordering
    name: TMF622 Product Order Management
    description: The Product Ordering Management API provides a standardized interface for managing product orders across telecom BSS systems, covering order creation, tracking, amendment, and cancellation for telecommunications products and services.
    humanURL: https://github.com/tmforum-apis/TMF622_ProductOrder
    tags:
      - Product Ordering
      - BSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF622_ProductOrder
      - type: OpenAPI
        url: openapi/tm-forum-tmf622-product-ordering-openapi.yaml
  - aid: tm-forum:tmf629-customer-management
    name: TMF629 Customer Management
    description: The Customer Management API provides a consistent interface for managing customer accounts, customer hierarchy, and customer engagement across telecom BSS systems, supporting B2C and B2B customer lifecycle operations.
    humanURL: https://github.com/tmforum-apis/TMF629_CustomerManagement
    tags:
      - Customer Management
      - BSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF629_CustomerManagement
      - type: OpenAPI
        url: openapi/tm-forum-tmf629-customer-management-openapi.yaml
  - aid: tm-forum:tmf632-party-management
    name: TMF632 Party Management
    description: The Party Management API provides a standardized way to manage parties (organizations and individuals) across telecom systems, supporting customer, partner, supplier, and employee management in a unified party data model aligned to the TM Forum SID.
    humanURL: https://github.com/tmforum-apis/TMF632_PartyManagement
    tags:
      - Party Management
      - BSS
      - Master Data
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF632_PartyManagement
      - type: OpenAPI
        url: openapi/tm-forum-tmf632-party-management-openapi.yaml
  - aid: tm-forum:tmf633-service-catalog
    name: TMF633 Service Catalog Management
    description: The Service Catalog API manages service specifications and service catalog entries, enabling telecom operators to expose and manage network and digital service offerings through standardized catalog APIs.
    humanURL: https://github.com/tmforum-apis/TMF633_ServiceCatalog
    tags:
      - Service Catalog
      - OSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF633_ServiceCatalog
      - type: OpenAPI
        url: openapi/tm-forum-tmf633-service-catalog-openapi.json
  - aid: tm-forum:tmf634-resource-catalog
    name: TMF634 Resource Catalog Management
    description: The Resource Catalog API manages resource specifications and resource catalog entries, providing a standardized interface for network and IT infrastructure resource discovery, specification, and lifecycle management.
    humanURL: https://github.com/tmforum-apis/TMF634_ResourceCatalog
    tags:
      - Resource Catalog
      - OSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF634_ResourceCatalog
      - type: OpenAPI
        url: openapi/tm-forum-tmf634-resource-catalog-openapi.json
  - aid: tm-forum:tmf637-product-inventory
    name: TMF637 Product Inventory Management
    description: The Product Inventory API provides standardized access to product instances subscribed by customers, enabling product lifecycle management operations including provisioning, suspension, termination, and status queries.
    humanURL: https://github.com/tmforum-apis/TMF637_ProductInventory
    tags:
      - Product Inventory
      - BSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF637_ProductInventory
      - type: OpenAPI
        url: openapi/tm-forum-tmf637-product-inventory-openapi.yaml
  - aid: tm-forum:tmf641-service-ordering
    name: TMF641 Service Order Management
    description: The Service Ordering API manages service orders for provisioning and activating telecom services, orchestrating the end-to-end service delivery workflow from order intake to service activation.
    humanURL: https://github.com/tmforum-apis/TMF641_ServiceOrder
    tags:
      - Service Ordering
      - OSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF641_ServiceOrder
      - type: OpenAPI
        url: openapi/tm-forum-tmf641-service-ordering-openapi.json
  - aid: tm-forum:tmf648-quote-management
    name: TMF648 Quote Management
    description: The Quote Management API handles the lifecycle of commercial quotes for telecommunications products and services, supporting quote creation, pricing, approval workflow, and conversion to orders.
    humanURL: https://github.com/tmforum-apis/TMF648_QuoteManagement
    tags:
      - Quote Management
      - BSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF648_QuoteManagement
      - type: OpenAPI
        url: openapi/tm-forum-tmf648-quote-management-openapi.json
  - aid: tm-forum:tmf651-agreement-management
    name: TMF651 Agreement Management
    description: The Agreement Management API manages commercial agreements between parties in the telecom ecosystem, supporting SLA contracts, partner agreements, and customer agreements across BSS and partner management systems.
    humanURL: https://github.com/tmforum-apis/TMF651_AgreementManagement
    tags:
      - Agreement Management
      - BSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF651_AgreementManagement
      - type: OpenAPI
        url: openapi/tm-forum-tmf651-agreement-management-openapi.json
  - aid: tm-forum:tmf666-account-management
    name: TMF666 Account Management
    description: The Account Management API provides standardized management of financial and billing accounts, supporting account creation, balance management, credit limit operations, and financial transaction history queries.
    humanURL: https://github.com/tmforum-apis/TMF666_AccountManagement
    tags:
      - Account Management
      - Billing
      - BSS
    properties:
      - type: Documentation
        url: https://github.com/tmforum-apis/TMF666_AccountManagement
      - type: OpenAPI
        url: openapi/tm-forum-tmf666-account-management-openapi.json
common:
  - type: Website
    url: https://www.tmforum.org/
  - type: Documentation
    url: https://www.tmforum.org/oda/open-apis/
  - type: Portal
    url: https://www.tmforum.org/open-digital-architecture/open-apis
  - type: GitHubOrganization
    url: https://github.com/tmforum-apis
  - type: GitHubOrganization
    url: https://github.com/tmforum-oda
  - type: Features
    data:
      - name: 88+ Open APIs
        description: Comprehensive portfolio of Apache 2.0 licensed REST APIs covering the full BSS/OSS stack for telecommunications.
      - name: TM Forum Information Framework (SID) Alignment
        description: All APIs implement data models aligned to the TM Forum SID ensuring semantic interoperability across implementations.
      - name: Consistent REST/JSON Patterns
        description: All TMF APIs follow identical REST operation patterns with consistent endpoint naming, HTTP methods, and schema conventions.
      - name: Open Digital Architecture (ODA)
        description: Component-based framework built on TM Forum Open APIs for cloud-native, modular telecom platform design.
      - name: Conformance Testing
        description: API conformance test kits (CTK) and static CTKs validate implementation compliance to TM Forum API specifications.
      - name: Versioned Specifications
        description: APIs published with semantic versioning; both Swagger 2.0 (v4.x) and OpenAPI 3.0 (v5.x) formats available.
  - type: UseCases
    data:
      - name: BSS Modernization
        description: Telcos replace monolithic BSS systems with modular TM Forum Open API implementations for agile service delivery.
      - name: Multi-Vendor Interoperability
        description: CSPs integrate products from multiple vendors using TM Forum Open APIs as a common integration layer.
      - name: Omnichannel Order Management
        description: End-to-end product ordering across digital channels using TMF622 Product Ordering and TMF648 Quote Management.
      - name: Customer Experience Management
        description: Unified customer profile and interaction management using TMF629 Customer and TMF632 Party Management APIs.
      - name: Network-as-a-Service (NaaS)
        description: Expose network resources as programmable services using TMF634 Resource Catalog and TMF641 Service Ordering.
      - name: Partner Ecosystem Integration
        description: Manage commercial partnerships using TMF651 Agreement and TMF632 Party APIs for ecosystem orchestration.
  - type: Integrations
    data:
      - name: Salesforce Communications Cloud
        description: Salesforce implements TMF620 and other Open APIs natively in Communications Cloud for CSP deployments.
      - name: Amdocs
        description: Amdocs BSS/OSS products implement TM Forum Open API interfaces for interoperability.
      - name: Ericsson
        description: Ericsson telecom platforms expose TM Forum Open APIs for cloud-native BSS/OSS integration.
      - name: Nokia
        description: Nokia network management products implement TM Forum Open APIs for multi-vendor environments.
      - name: Huawei
        description: Huawei BSS/OSS solutions support TM Forum Open API compliance for operator deployments.
      - name: Pega Systems
        description: Pega for Communications implements TM Forum Open APIs including TMF620 Product Catalog.
  - type: SpectralRules
    url: rules/tm-forum-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/tm-forum-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/product-to-cash.yaml
    name: Product-to-Cash
  - type: NaftikoCapability
    url: capabilities/customer-support.yaml
    name: Customer Support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
