---
name: Gainsight
description: Gainsight is a customer success platform that helps companies retain and grow their customer base through data-driven insights, automation, and engagement tools.
url: https://www.gainsight.com
created: '2024'
modified: '2026-05-04'
apis:
  - name: Gainsight REST API
    description: The Gainsight REST API allows developers to integrate customer success data, automate workflows, and build custom applications on top of the Gainsight platform.
    humanURL: https://support.gainsight.com/PX/API_for_Developers/02About/Work_with_the_Gainsight_API
    baseURL: https://api.gainsight.com
    tags:
      - Analytics
      - CRM
      - Customer Success
      - SaaS
    properties:
      - type: documentation
        url: https://support.gainsight.com/PX/API_for_Developers
      - type: authentication
        url: https://support.gainsight.com/PX/API_for_Developers/02About/Authentication
      - type: swagger
        url: https://api.gainsight.com/swagger
      - type: OpenAPI
        url: openapi/gainsight-rest-api-openapi.yml
    contact:
      - name: Gainsight Support
        url: https://support.gainsight.com
        email: support@gainsight.com
  - name: Gainsight PX API
    description: Product Experience (PX) API for tracking product usage, user behavior, and in-app engagement analytics.
    humanURL: https://support.gainsight.com/PX/API_for_Developers
    baseURL: https://api.aptrinsic.com/v1
    tags:
      - Product Analytics
      - Product Experience
      - User Engagement
    properties:
      - type: documentation
        url: https://support.gainsight.com/PX/API_for_Developers/APIs_for_Developers/PX_API
      - type: api-key
        url: https://support.gainsight.com/PX/API_for_Developers/02About/API_Keys
      - type: documentation
        url: https://gainsightpx.docs.apiary.io/
      - type: OpenAPI
        url: openapi/gainsight-px-api-openapi.yml
  - name: Gainsight CS Company API
    description: The Company API enables inserting, updating, reading, and deleting records in the Gainsight Company object, supporting up to 50 records per call for write operations and 5000 records per read call.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation
    baseURL: https://companyapi.gainsightcloud.com
    tags:
      - Accounts
      - Companies
      - Customer Success
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-company-api-openapi.yml
  - name: Gainsight CS Person API
    description: The Person API facilitates upserting person records into the Gainsight Person object model, enabling management of customer contacts and stakeholders.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Person_API/People_API_Documentation
    baseURL: https://personapi.gainsightcloud.com
    tags:
      - Contacts
      - Customer Success
      - People
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Person_API/People_API_Documentation
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-person-api-openapi.yml
  - name: Gainsight CS Custom Object API
    description: The Custom Object API allows inserting, updating, reading, and deleting records in Gainsight transactional custom objects, supporting flexible data models for customer success workflows.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Custom_Object_API/Gainsight_Custom_Object_API_Documentation
    baseURL: https://customobjectapi.gainsightcloud.com
    tags:
      - Custom Objects
      - Customer Success
      - Data Management
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Custom_Object_API/Gainsight_Custom_Object_API_Documentation
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-custom-object-api-openapi.yml
  - name: Gainsight CS CTA API
    description: The Call To Action (CTA) API enables creating and updating CTAs, fetching CTA details, and retrieving CTA configurations through Cockpit REST APIs for managing customer success actions.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Cockpit_API/Call_To_Action_(CTA)_API_Documentation
    baseURL: https://cta.gainsightcloud.com
    tags:
      - Calls to Action
      - Cockpit
      - Customer Success
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Cockpit_API/Call_To_Action_(CTA)_API_Documentation
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-cta-api-openapi.yml
  - name: Gainsight CS Timeline API
    description: The Timeline API enables creating, updating, reading, and deleting Timeline activities, supporting both single and bulk operations with up to 80MB payloads for bulk requests.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Timeline_API/Timeline_APIs
    baseURL: https://timeline.gainsightcloud.com
    tags:
      - Activities
      - Customer Success
      - Timeline
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Timeline_API/Timeline_APIs
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-timeline-api-openapi.yml
  - name: Gainsight CS Success Plan API
    description: The Success Plan API enables creating, updating, and fetching Success Plans and their configurations, supporting structured goal tracking for customer engagements.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Success_Plan_APIs/Success_Plan_APIs
    baseURL: https://successplan.gainsightcloud.com
    tags:
      - Customer Success
      - Goal Tracking
      - Success Plans
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Success_Plan_APIs/Success_Plan_APIs
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-success-plan-api-openapi.yml
  - name: Gainsight CS Data Management API
    description: The Data Management API provides access to Gainsight object and field metadata, enabling retrieval of schema information for integration and data mapping purposes.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Data_Management_APIs/Data_Management_APIs
    baseURL: https://data.gainsightcloud.com
    tags:
      - Customer Success
      - Data Management
      - Metadata
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Data_Management_APIs/Data_Management_APIs
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-data-management-api-openapi.yml
  - name: Gainsight CS Bulk API
    description: The Gainsight Bulk API is an asynchronous connector that automates insert or update of large data volumes from CSV files into Gainsight standard and custom objects, with rate limits of 10 calls per hour and 100 per day.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Bulk_API/Gainsight_Bulk_REST_APIs
    baseURL: https://bulk.gainsightcloud.com
    tags:
      - Bulk Data
      - Customer Success
      - Data Import
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Bulk_API/Gainsight_Bulk_REST_APIs
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Bulk_API/Gainsight_Bulk_API
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-bulk-api-openapi.yml
  - name: Gainsight CS Events API
    description: The Events API enables external systems to publish events into Gainsight, supporting system asset events for cross-system communication with operations including insert, update, upsert, and delete.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Events_API/Events_API
    baseURL: https://events.gainsightcloud.com
    tags:
      - Customer Success
      - Events
      - Webhooks
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Events_API/Events_API
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-events-api-openapi.yml
  - name: Gainsight CS User Management API
    description: The User Management API provides endpoints for managing Gainsight users, company team records, and includes SCIM support for automated user provisioning and de-provisioning through identity providers.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/User_Management_APIs/User_Management_APIs
    baseURL: https://usermanagement.gainsightcloud.com
    tags:
      - Customer Success
      - Provisioning
      - SCIM
      - User Management
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/User_Management_APIs/User_Management_APIs
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/User_Management_APIs/SCIM_API
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/User_Management_APIs/API_for_Company_Team_Record
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-user-management-api-openapi.yml
  - name: Gainsight CS Customer Goals API
    description: The Customer Goals API enables external systems to create, update, and fetch customer goals programmatically, including template and metrics management for structured goal tracking.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Customer_Goals_API/Customer_Goals_APIs
    baseURL: https://goals.gainsightcloud.com
    tags:
      - Customer Success
      - Goals
      - Outcomes
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Customer_Goals_API/Customer_Goals_APIs
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-customer-goals-api-openapi.yml
  - name: Gainsight CS Renewal Center API
    description: The Renewal Center API enables creating and updating opportunity records in the Gainsight Opportunity object, supporting renewal, upsell, and downsell booking types within the Matrix Data Architecture.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Renewal_Center_API/Renewal_Center_API
    baseURL: https://renewals.gainsightcloud.com
    tags:
      - Customer Success
      - Opportunities
      - Renewals
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Renewal_Center_API/Renewal_Center_API
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-renewal-center-api-openapi.yml
  - name: Gainsight CS Task and Playbook API
    description: The Task and Playbook API manages task creation and updates, and retrieves task and playbook details for orchestrating customer success workflows within the Cockpit.
    humanURL: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Cockpit_API/Task_APIs
    baseURL: https://task.gainsightcloud.com
    tags:
      - Cockpit
      - Customer Success
      - Playbooks
      - Tasks
    properties:
      - type: documentation
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Cockpit_API/Task_APIs
      - type: authentication
        url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
      - type: OpenAPI
        url: openapi/gainsight-cs-task-and-playbook-api-openapi.yml
common:
  - type: portal
    url: https://support.gainsight.com
  - type: login
    url: https://app.gainsight.com
  - type: terms-of-service
    url: https://www.gainsight.com/terms-of-service/
  - type: privacy-policy
    url: https://www.gainsight.com/privacy-policy/
  - type: status
    url: https://trust.gainsight.com/
  - type: developer-docs
    url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs
  - type: authentication
    url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
  - type: oauth
    url: https://support.gainsight.com/gainsight_nxt/01Onboarding_and_Implementation/Onboarding_for_Gainsight_NXT/Login_and_Permissions/OAuth_for_Gainsight_APIs
  - type: release-notes
    url: https://support.gainsight.com/gainsight_nxt/Release_Notes
  - type: community
    url: https://communities.gainsight.com
  - type: blog
    url: https://www.gainsight.com/blog/
  - type: education
    url: https://education.gainsight.com
  - type: JSON-LD
    url: json-ld/gainsight-context.jsonld
  - type: JSONSchema
    url: json-schema/gainsight-company-schema.json
  - type: JSONSchema
    url: json-schema/gainsight-person-schema.json
  - type: JSONSchema
    url: json-schema/gainsight-cta-schema.json
  - type: JSONSchema
    url: json-schema/gainsight-opportunity-schema.json
  - type: JSONSchema
    url: json-schema/gainsight-timeline-activity-schema.json
  - type: Features
    data:
      - 'Essentials: 10 full users, 100 customers per user (custom price)'
      - 'Enterprise: 20 full users, 200 customers per user (custom price)'
      - AI Insights and Automations
      - Customer 360 unified profile
      - Playbooks and Success Plans
      - Health Scorecards
      - Surveys (CSAT, NPS)
      - Digital Journeys for in-app onboarding
      - Renewal and Expansion Forecasting (Enterprise)
      - Org Mapping and Sponsor Tracking (Enterprise)
      - REST API at api.gainsight.com
      - Default 100 req/min/tenant
      - OAuth 2.0 + access tokens
      - Webhooks for customer health events
      - Salesforce-native (Gainsight CS) or standalone (NXT)
      - Unlimited Viewer Licenses on both tiers
    sources:
      - https://www.gainsight.com/pricing/
    updated: '2026-05-04'
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://www.gainsight.com
---
