---
aid: copper
name: Copper
x-type: company
description: Copper is a CRM platform built natively for Google Workspace, designed to help teams cultivate enduring client relationships through purposeful collaboration. Copper offers a RESTful Developer API providing programmatic access to People, Companies, Leads, Opportunities, Projects, Tasks, Activities, Webhooks, and related resources for CRM integration and automation.
url: https://raw.githubusercontent.com/api-evangelist/copper/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
tags:
  - Activities
  - Companies
  - Contact Relationship Management
  - Contacts
  - CRM
  - Customer Relationship Management
  - Google Workspace
  - Leads
  - Opportunities
  - People
  - Projects
  - Sales
  - Tasks
created: '2025-01-07'
modified: '2026-05-04'
specificationVersion: '0.20'
apis:
  - aid: copper:developer-api
    name: Copper Developer API
    description: The Copper Developer API is a RESTful JSON API providing programmatic access to Copper CRM resources including people, companies, leads, opportunities, projects, tasks, activities, and webhooks. The API uses token-based authentication with three required headers (X-PW-AccessToken, X-PW-Application, X-PW-UserEmail) and supports full CRUD operations, search, bulk actions, and lead conversion. Rate limits are 180 requests per minute and 3 requests per second for bulk operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.copper.com/
    baseURL: https://api.copper.com/developer_api/v1
    tags:
      - Activities
      - Companies
      - CRM
      - Leads
      - Opportunities
      - People
      - Projects
      - REST
      - Tasks
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.copper.com/
      - type: Authentication
        url: https://developer.copper.com/introduction/requests.html
      - type: GettingStarted
        url: https://developer.copper.com/introduction/quick-start.html
      - type: OAuth
        url: https://developer.copper.com/introduction/oauth-quickstart.html
      - type: Webhooks
        url: https://developer.copper.com/webhooks/general/list-of-webhook-events.html
      - type: PostmanCollection
        url: https://developer.copper.com/introduction/postman-collection.html
      - type: People
        url: https://developer.copper.com/people/
      - type: Companies
        url: https://developer.copper.com/companies/
      - type: Leads
        url: https://developer.copper.com/leads/
      - type: Opportunities
        url: https://developer.copper.com/opportunities/
      - type: Projects
        url: https://developer.copper.com/projects/
      - type: Tasks
        url: https://developer.copper.com/tasks/
      - type: Activities
        url: https://developer.copper.com/activities/
      - type: CustomFields
        url: https://developer.copper.com/custom-fields/
      - type: Tags
        url: https://developer.copper.com/tags/
      - type: OpenAPI
        url: openapi/copper-developer-api-openapi.yml
      - type: Rules
        url: rules/copper-developer-api-rules.yml
      - type: JSONLD
        url: json-ld/copper-context.jsonld
      - type: Vocabulary
        url: vocabulary/copper-vocabulary.yml
      - type: Capabilities
        url: capabilities/copper-developer-api-capabilities.yml
    contact:
      - type: Support
        url: https://www.copper.com/contact-us
common:
  - type: Website
    url: https://www.copper.com
  - type: DeveloperPortal
    url: https://developer.copper.com/
  - type: Documentation
    url: https://developer.copper.com/
  - type: Authentication
    url: https://developer.copper.com/introduction/requests.html
  - type: GettingStarted
    url: https://developer.copper.com/introduction/quick-start.html
  - type: RateLimits
    url: https://developer.copper.com/introduction/requests.html
  - type: Errors
    url: https://developer.copper.com/introduction/responses.html
  - type: Pricing
    url: https://www.copper.com/pricing
  - type: Blog
    url: https://www.copper.com/blog
  - type: PrivacyPolicy
    url: https://www.copper.com/privacy-policy
  - type: TermsOfService
    url: https://www.copper.com/terms-of-service
  - type: Status
    url: https://status.copper.com/
  - type: Twitter
    url: https://twitter.com/copperinc
  - type: LinkedIn
    url: https://www.linkedin.com/company/copperinc/
  - type: YouTube
    url: https://www.youtube.com/c/CopperCRM
  - type: Features
    data:
      - 'Starter $9/mo: 1K contacts, Google Workspace integration'
      - 'Basic $23/mo: 2,500 contacts, pipelines, project management'
      - 'Professional $59/mo: 15K contacts, workflow automation, bulk email'
      - 'Business $99/mo: unlimited contacts, custom reports, multi-currency'
      - Native Google Workspace integration (Gmail, Calendar, Drive, Docs)
      - REST API at api.copper.com/developer_api/v1
      - Default 600 req/min, 10 req/sec
      - OAuth 2.0 + API keys
      - Webhooks for record/activity events
      - Pipelines and opportunity stages
      - Lead scoring (Professional+)
      - Workflow automation (Professional+)
      - Bulk email (Professional+)
      - Email templates and tracking
      - Project Management module
      - Mobile apps (iOS + Android)
    sources:
      - https://www.copper.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
