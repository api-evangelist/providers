---
aid: goodyear-tire-and-rubber
url: https://raw.githubusercontent.com/api-evangelist/goodyear-tire-and-rubber/refs/heads/main/apis.yml
apis:
  - aid: goodyear-tire-and-rubber:sightline-api
    name: Goodyear SightLine API
    tags:
      - Connected Vehicles
      - IoT
      - Telematics
      - Tire Data
      - Tires
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.goodyearsightline.com
    humanURL: https://developer.goodyearsightline.com/
    properties:
      - type: Portal
        url: https://developer.goodyearsightline.com/
      - type: OpenAPI
        url: openapi/sightline-api.yml
    description: Goodyear SightLine API provides developer-friendly access to intelligent tire data including tire type, tread depth, tire pressure, load, wear state, and temperature. The API uses REST architecture with robust security protocols for efficient and secure data sharing.
  - aid: goodyear-tire-and-rubber:gaas-portal
    name: Goodyear API Management Portal
    tags:
      - API Management
      - Fleet Management
      - Tires
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://gaas-portal.goodyear.com
    humanURL: https://gaas-portal.goodyear.com/
    properties:
      - type: Portal
        url: https://gaas-portal.goodyear.com/
      - type: SignUp
        url: https://gaas-portal.goodyear.com/signup
      - type: OpenAPI
        url: openapi/gaas-portal.yml
    description: The Goodyear API Management Portal (GaaS) provides access to Goodyear's suite of APIs for tire and fleet management services.
  - aid: goodyear-tire-and-rubber:catalog-api
    name: Goodyear Truck Tire Catalog API
    tags:
      - Catalog
      - Tires
      - Truck Tires
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.catalog.goodyeartrucktires.com
    humanURL: https://api.catalog.goodyeartrucktires.com/
    properties:
      - type: Portal
        url: https://api.catalog.goodyeartrucktires.com/
    description: The Goodyear Truck Tire Catalog API provides access to Goodyear's commercial truck tire catalog data.
  - aid: goodyear-tire-and-rubber:work-order-api
    name: Goodyear Work Order API
    tags:
      - Fleet Management
      - Tires
      - Work Orders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.workorder.goodyeartrucktires.com
    humanURL: https://api.workorder.goodyeartrucktires.com/
    properties:
      - type: Portal
        url: https://api.workorder.goodyeartrucktires.com/
    description: The Goodyear Work Order API enables management of service work orders for commercial truck tire services.
  - aid: goodyear-tire-and-rubber:service-ticket-api
    name: Goodyear Service Ticket API
    tags:
      - Fleet Management
      - Service Tickets
      - Tires
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.serviceticket.goodyeartrucktires.com
    humanURL: https://api.serviceticket.goodyeartrucktires.com/
    properties:
      - type: Portal
        url: https://api.serviceticket.goodyeartrucktires.com/
    description: The Goodyear Service Ticket API provides management of service tickets for commercial truck tire services.
name: Goodyear Tire & Rubber
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Connected Vehicles
  - Fleet Management
  - IoT
  - Telematics
  - Tires
common:
  - url: https://www.goodyear.com
    name: Goodyear Website
    type: Website
  - url: https://developer.goodyearsightline.com/
    name: SightLine Developer Portal
    type: Portal
  - url: https://gaas-portal.goodyear.com/
    name: Goodyear API Management Portal
    type: Portal
description: The Goodyear Tire & Rubber Company is a global tire manufacturer that provides developer APIs for intelligent tire data, fleet management, and commercial truck tire services. Goodyear's SightLine technology and GaaS API platform enable programmatic access to tire telematics, catalogs, work orders, and service tickets.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
