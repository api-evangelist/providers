---
aid: whmcs
name: WHMCS
description: WHMCS (Web Host Manager Complete Solution) is a leading web hosting automation platform that provides billing, client management, support, domain management, and provisioning automation for web hosting businesses. It offers a comprehensive API with 150+ commands covering clients, orders, invoicing, domains, support tickets, and system administration.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Web Hosting
  - Billing Automation
  - Client Management
  - Domain Management
  - Support Tickets
  - Provisioning
url: https://raw.githubusercontent.com/api-evangelist/whmcs/refs/heads/main/apis.yml
created: '2025-02-09'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: whmcs:whmcs
    name: WHMCS API
    description: The WHMCS API provides an interface to perform operations and actions within WHMCS from external applications and scripts. It supports 150+ commands for client management, order processing, billing, invoice management, domain registration and management, support ticket handling, service provisioning, OAuth/SSO authentication, and system administration.
    humanURL: https://developers.whmcs.com/
    baseURL: https://{your-domain}/includes/api.php
    tags:
      - Web Hosting
      - Billing Automation
      - Client Management
      - Domain Management
      - Support Tickets
      - Provisioning
      - Automation
    properties:
      - type: Documentation
        url: https://developers.whmcs.com/api/
      - type: APIReference
        url: https://developers.whmcs.com/api-reference/
      - type: APIIndex
        url: https://developers.whmcs.com/api/api-index/
      - type: GettingStarted
        url: https://developers.whmcs.com/api/getting-started/
      - type: Authentication
        url: https://developers.whmcs.com/api/authentication/
      - type: SampleCode
        url: https://developers.whmcs.com/api/sample-code/
      - type: GitHub
        url: https://github.com/WHMCS
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/openapi/whmcs-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/json-schema/whmcs-client-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/json-schema/whmcs-invoice-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/json-schema/whmcs-ticket-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/json-structure/whmcs-api-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/json-ld/whmcs-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/rules/whmcs-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/whmcs/main/vocabulary/whmcs-vocabulary.yml
    contact:
      - FN: WHMCS Support
        url: https://www.whmcs.com/contact/
    features:
      - 150+ API commands via HTTP POST
      - Client account management (create, update, delete, retrieve)
      - Order processing and management
      - Invoice and billing automation
      - Domain registration and management
      - Support ticket management
      - Service provisioning via modules
      - OAuth 2.0 and SSO token support
      - Addon and upgrade management
      - Project management
      - Affiliate tracking
      - System configuration and statistics
    use-cases:
      - Automate client onboarding from external applications
      - Integrate billing with third-party accounting systems
      - Build custom client portals
      - Automate domain registration workflows
      - Sync support tickets with external helpdesk systems
      - Provision hosting services programmatically
      - Create SSO integrations for client area access
    integrations:
      - cPanel/WHM via provisioning modules
      - Plesk via provisioning modules
      - DirectAdmin via provisioning modules
      - PayPal payment gateway
      - Stripe payment gateway
      - Authorize.Net payment gateway
      - WHMCS Marketplace modules
common:
  - type: Website
    url: https://www.whmcs.com/
  - type: Documentation
    url: https://developers.whmcs.com/
  - type: APIReference
    url: https://developers.whmcs.com/api-reference/
  - type: Blog
    url: https://blog.whmcs.com/
  - type: GitHub Organization
    url: https://github.com/WHMCS
  - type: Marketplace
    url: https://marketplace.whmcs.com/
  - type: Forum
    url: https://whmcs.community/
  - type: StatusPage
    url: https://whmcsstatus.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
