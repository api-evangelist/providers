---
aid: snow-software
name: Snow Software
description: Snow Software (now Flexera Snow) is an IT asset and SaaS management platform providing visibility into software licenses, cloud spend, SaaS usage, and hardware assets across the enterprise. Snow Atlas is the cloud-native platform offering SAM (Software Asset Management), SaaS Management, Cloud License Management, and Commander for hybrid IT. The Snow Atlas REST APIs enable programmatic access to licenses, computers, SaaS applications, subscriptions, user accounts, agreements, and audit logs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud License Management
  - FinOps
  - IT Asset Management
  - SaaS Management
  - Software Asset Management
url: https://raw.githubusercontent.com/api-evangelist/snow-software/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: snow-software:snow-atlas-licenses-api
    name: Snow Atlas SAM Licenses API
    description: The Snow Atlas SAM Licenses API provides programmatic access to software license data including license upgrades, application license transfers, computer license tracking, license policies, maintenance periods, purchase orders, and license metrics. Supports filtering and pagination.
    humanURL: https://docs.flexera.com/snow-atlas/snow-atlas-api/sam-core-apis
    tags:
      - IT Asset Management
      - License Management
      - Software Asset Management
    properties:
      - type: Documentation
        url: https://docs.flexera.com/snow-atlas/snow-atlas-api/sam-core-apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snow-software/refs/heads/main/openapi/snow-software-licenses-openapi.yml
  - aid: snow-software:snow-atlas-saas-applications-api
    name: Snow Atlas SaaS Applications API
    description: The Snow Atlas SaaS Applications API provides visibility into SaaS applications in use across the organization. Enables listing, updating, and managing SaaS apps, application KPIs, users, and consumption data for SaaS spend optimization.
    humanURL: https://docs.flexera.com/snow-atlas/snow-atlas-api/saas-apis
    tags:
      - SaaS Management
      - Software Asset Management
      - Spend Optimization
    properties:
      - type: Documentation
        url: https://docs.flexera.com/snow-atlas/snow-atlas-api/saas-apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snow-software/refs/heads/main/openapi/snow-software-saas-applications-openapi.yml
  - aid: snow-software:snow-atlas-saas-subscriptions-api
    name: Snow Atlas SaaS Subscriptions API
    description: The Snow Atlas SaaS Subscriptions API manages SaaS subscription data including subscription details, costs, renewal dates, and vendor information for enterprise SaaS portfolio management.
    humanURL: https://docs.flexera.com/snow-atlas/snow-atlas-api/saas-apis
    tags:
      - Contract Management
      - SaaS Management
      - Subscription Management
    properties:
      - type: Documentation
        url: https://docs.flexera.com/snow-atlas/snow-atlas-api/saas-apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snow-software/refs/heads/main/openapi/snow-software-saas-subscriptions-openapi.yml
  - aid: snow-software:snow-atlas-computers-api
    name: Snow Atlas SAM Computers API
    description: The Snow Atlas SAM Computers API provides access to computer inventory data including hardware assets, application metering per computer, installed software, update history, custom values, and bulk status management for IT asset lifecycle management.
    humanURL: https://docs.flexera.com/snow-atlas/snow-atlas-api/sam-core-apis
    tags:
      - Hardware Asset Management
      - IT Asset Management
      - Inventory
    properties:
      - type: Documentation
        url: https://docs.flexera.com/snow-atlas/snow-atlas-api/sam-core-apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snow-software/refs/heads/main/openapi/snow-software-computers-openapi.json
common:
  - type: Website
    url: https://www.snowsoftware.com
  - type: Documentation
    url: https://docs.snowsoftware.com/
  - type: DeveloperPortal
    url: https://docs.flexera.com/snow-atlas/snow-atlas-api/get-started-with-apis
  - type: GitHubOrganization
    url: https://github.com/SnowSoftware
  - type: Integrations
    url: https://github.com/SnowSoftware/snowatlas-integrations
  - type: Blog
    url: https://www.snowsoftware.com/blog
  - type: Support
    url: https://community.snowsoftware.com
  - type: Login
    url: https://app.snowsoftware.io
  - type: About
    url: https://www.snowsoftware.com/company
segments:
  - ITAM
  - FinOps
  - Enterprise Software
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
