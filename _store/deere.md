---
aid: deere
name: John Deere
url: https://raw.githubusercontent.com/api-evangelist/deere/refs/heads/main/apis.yml
description: John Deere is a manufacturer of agricultural, construction, and forestry machinery, equipment, and technology. Through its Operations Center and Precision Tech developer programs, John Deere exposes APIs that allow authorized partners and customers to access organization, field, machine, field operations, and webhook data tied to connected equipment and farm management workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consuming
specificationVersion: '0.19'
xType: company
tags:
  - Agriculture
  - Agricultural Technology
  - AgTech
  - Construction
  - Farming
  - Forestry
  - Machinery
  - Operations Center
  - Precision Agriculture
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: deere:operations-center-organizations-api
    name: John Deere Operations Center Organizations API
    description: Provides access to the organizations a John Deere Operations Center user belongs to. Organizations are the top-level container for users, fields, equipment, and partner relationships in Operations Center.
    humanURL: https://developer.deere.com/dev-docs/organizations
    tags:
      - Operations Center
      - Organizations
    properties:
      - type: Documentation
        url: https://developer.deere.com/dev-docs/organizations
  - aid: deere:operations-center-fields-api
    name: John Deere Operations Center Fields API
    description: Exposes growers, farms, fields, and field boundaries in Operations Center so that partner applications can sync agronomic field metadata and boundary geometry.
    humanURL: https://developer.deere.com/
    tags:
      - Operations Center
      - Fields
      - Boundaries
      - Agronomy
    properties:
      - type: Documentation
        url: https://developer.deere.com/
  - aid: deere:operations-center-machines-api
    name: John Deere Operations Center Machines API
    description: Provides metadata, telematics, and engine information for connected John Deere machines, including machine locations, engine hours, hours of operation, alerts, and device state reports.
    humanURL: https://developer.deere.com/
    tags:
      - Operations Center
      - Machines
      - Telematics
      - Equipment
    properties:
      - type: Documentation
        url: https://developer.deere.com/
  - aid: deere:operations-center-field-operations-api
    name: John Deere Operations Center Field Operations API
    description: Returns information about field operations such as planting, application, tillage, and harvest performed by connected John Deere machines, with links to machine, field, and product data.
    humanURL: https://developer.deere.com/
    tags:
      - Operations Center
      - Field Operations
      - Planting
      - Harvest
      - Application
    properties:
      - type: Documentation
        url: https://developer.deere.com/
  - aid: deere:operations-center-products-api
    name: John Deere Operations Center Products API
    description: Manages crop, seed, chemical, and fertilizer products used in field operations, allowing applications to read and reconcile product catalogs across an organization.
    humanURL: https://developer.deere.com/dev-docs/products
    tags:
      - Operations Center
      - Products
      - Inputs
    properties:
      - type: Documentation
        url: https://developer.deere.com/dev-docs/products
  - aid: deere:operations-center-webhook-api
    name: John Deere Operations Center Webhook API
    description: Lets partner applications subscribe to event notifications from Operations Center so that changes to organizations, machines, fields, and field operations can be received without polling.
    humanURL: https://developer.deere.com/dev-docs/webhook
    tags:
      - Operations Center
      - Webhooks
      - Events
    properties:
      - type: Documentation
        url: https://developer.deere.com/dev-docs/webhook
  - aid: deere:precision-tech-apis
    name: John Deere Precision Tech APIs
    description: A suite of APIs supporting precision agriculture workflows including prescription maps, work plans, setup files, and equipment configuration for connected John Deere machinery.
    humanURL: https://developer.deere.com/precision
    tags:
      - Precision Agriculture
      - Prescriptions
      - Work Plans
      - Setup Files
    properties:
      - type: Documentation
        url: https://developer.deere.com/precision
common:
  - type: Website
    url: https://www.deere.com
  - type: Developer Portal
    url: https://developer.deere.com/
  - type: Getting Started
    url: https://developer.deere.com/precision/get-started
  - type: Documentation
    url: https://developer.deere.com/
  - type: ChangeLog
    url: https://developer.deere.com/whats-new
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
