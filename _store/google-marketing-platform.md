---
aid: google-marketing-platform
name: Google Marketing Platform Admin
description: The Google Marketing Platform Admin API provides programmatic access to manage links between Google Marketing Platform organizations and Google Analytics accounts. It enables creating, updating, deleting, and listing organization links and managing service levels for integrated marketing analytics.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-marketing-platform/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
tags:
  - Analytics
  - Google Marketing Platform
  - Marketing
  - Organization Management
  - Platform Administration
apis:
  - aid: google-marketing-platform:admin
    name: Google Marketing Platform Admin API
    description: The Marketing Platform Admin API enables programmatic management of organization-level settings including links to Google Analytics accounts, service level configuration, and organization administration.
    humanURL: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
    baseURL: https://marketingplatformadmin.googleapis.com
    tags:
      - Admin
      - Analytics
      - Organizations
    properties:
      - type: Documentation
        url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/docs/api/how-tos/authorizing
      - type: GettingStarted
        url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.yml
common:
  - type: Portal
    url: https://marketingplatform.google.com
  - type: GettingStarted
    url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
  - type: Documentation
    url: https://developers.google.com/marketing-platform
  - type: Authentication
    url: https://developers.google.com/docs/api/how-tos/authorizing
  - type: Pricing
    url: https://marketingplatform.google.com/about/
  - type: TermsOfService
    url: https://developers.google.com/terms
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: StatusPage
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/marketing-platform/support
  - type: JSONLD
    url: json-ld/json-ld.yml
  - type: NaftikoCapability
    url: capabilities/shared/admin-api.yaml
    title: Admin API Shared Definition
  - type: NaftikoCapability
    url: capabilities/marketing-analytics.yaml
    title: Marketing Analytics Administration Workflow
  - type: Features
    data:
      - name: Organization Management
        description: List and manage Google Marketing Platform organizations with programmatic access to organization settings.
      - name: Analytics Account Linking
        description: Create, list, and delete links between Marketing Platform organizations and Google Analytics accounts.
      - name: Service Level Configuration
        description: Set and manage Analytics property service levels including standard and 360 tier assignments.
      - name: Multi-Organization Access
        description: Access and manage multiple Marketing Platform organizations from a single authenticated session.
  - type: UseCases
    data:
      - name: Enterprise Analytics Setup
        description: Programmatically link Google Analytics accounts to Marketing Platform organizations for enterprise-scale deployments.
      - name: Service Tier Management
        description: Automate the assignment of Analytics 360 service levels to properties across large organizations.
      - name: Organization Auditing
        description: List and audit all Marketing Platform organizations and their linked Analytics accounts for governance.
  - type: Integrations
    data:
      - name: Google Analytics
        description: Direct linking and service level management for Google Analytics accounts within Marketing Platform organizations.
      - name: Google Tag Manager
        description: Part of the Google Marketing Platform suite for tag management and measurement integration.
      - name: Display and Video 360
        description: Integrated advertising platform within Google Marketing Platform for programmatic media buying.
      - name: Search Ads 360
        description: Search campaign management platform integrated with Marketing Platform for cross-channel analytics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
