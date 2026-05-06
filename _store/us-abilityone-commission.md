---
aid: us-abilityone-commission
url: https://raw.githubusercontent.com/api-evangelist/us-abilityone-commission/refs/heads/main/apis.yml
name: US AbilityOne Commission
tags:
  - Federal Government
  - Disability Employment
  - Procurement
  - Nonprofit
  - Accessibility
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-20'
modified: '2026-05-03'
position: Consumer
description: The US AbilityOne Commission is an independent federal agency that administers the AbilityOne Program, which creates employment opportunities for individuals who are blind or have significant disabilities. Operating under the Javits-Wagner-O'Day (JWOD) Act, the Commission maintains the AbilityOne Procurement List — a catalog of products and services that federal agencies are required to purchase from qualified nonprofit agencies employing people who are blind or have significant disabilities. The PLIMS (Procurement List Information Management System) provides web-based search access to the products and services list. Two central nonprofit agencies, NIB (National Industries for the Blind) and SourceAmerica, manage the affiliated nonprofit network.
specificationVersion: '0.19'
apis:
  - aid: us-abilityone-commission:procurement-list-api
    name: AbilityOne Procurement List API
    description: The Procurement List Information Management System (PLIMS) provides search access to the AbilityOne Procurement List — the catalog of products (identified by NSN) and services that federal agencies are mandated to procure from AbilityOne-participating nonprofit agencies. Supports search by NSN, product description, service type, agency, and nonprofit affiliate.
    humanURL: https://plims.abilityone.gov/search-products/
    baseURL: https://plims.abilityone.gov
    tags:
      - Procurement
      - Products
      - Services
      - NSN
      - Federal Acquisition
    properties:
      - type: Documentation
        url: https://www.abilityone.gov/procurement_list/
      - type: OpenAPI
        url: openapi/abilityone-procurement-list-api-openapi.yml
      - type: JSONSchema
        url: json-schema/procurement-list-api-product-schema.json
      - type: JSONSchema
        url: json-schema/procurement-list-api-service-schema.json
common:
  - type: Website
    url: https://www.abilityone.gov
  - type: Portal
    url: https://plims.abilityone.gov
    title: PLIMS - Procurement List Information Management System
  - type: Documentation
    url: https://www.abilityone.gov/procurement_list/
  - type: DataAPI
    url: https://plims.abilityone.gov/reports/
    title: Procurement List Data Downloads
  - type: JSONLD
    url: json-ld/us-abilityone-commission-context.jsonld
  - type: SpectralRules
    url: rules/us-abilityone-commission-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/us-abilityone-commission-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/disability-employment-procurement.yaml
    title: Disability Employment Procurement
  - type: NaftikoCapability
    url: capabilities/shared/procurement-list-api.yaml
    title: Procurement List API (Shared)
  - type: Features
    data:
      - name: Procurement List Search
        description: Web-based search of the AbilityOne Procurement List by NSN, product description, agency, and nonprofit affiliate via PLIMS.
      - name: Products List
        description: Searchable and downloadable catalog of products on the AbilityOne Procurement List, identified by National Stock Number (NSN).
      - name: Services List
        description: Searchable catalog of services on the AbilityOne Procurement List, organized by service category and performing nonprofit agency.
      - name: Nonprofit Agency Directory
        description: Directory of NIB-affiliated and SourceAmerica-affiliated nonprofit agencies that employ people who are blind or have significant disabilities.
      - name: Reports and Data Downloads
        description: Downloadable Excel reports of the Procurement List products and services, nonprofit agency rosters, and distributor lists.
  - type: UseCases
    data:
      - name: Federal Acquisition Compliance
        description: Federal contracting officers verifying mandatory source requirements for AbilityOne products and services before placing orders.
      - name: Procurement List Lookup
        description: Defense and civilian agencies searching by NSN to determine if a product must be procured through the AbilityOne program.
      - name: Nonprofit Agency Discovery
        description: Federal buyers identifying which nonprofit agency supplies a specific product or service in their geographic region.
      - name: Distributor Integration
        description: Authorized distributors accessing the Procurement List to maintain current product catalogs and pricing.
  - type: Integrations
    data:
      - name: NIB (National Industries for the Blind)
        description: Central nonprofit agency managing blind-employing organizations participating in the AbilityOne program.
      - name: SourceAmerica
        description: Central nonprofit agency managing organizations employing people with significant disabilities in the AbilityOne program.
      - name: GSA Advantage
        description: GSA procurement platform where AbilityOne products are listed and available for federal purchase.
      - name: SAM.gov
        description: System for Award Management integration for federal contract and acquisition data linked to AbilityOne awards.
      - name: FPDS
        description: Federal Procurement Data System tracking AbilityOne program spending and contract awards across federal agencies.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
