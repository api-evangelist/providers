---
aid: supaglue
name: Supaglue
description: Supaglue is an open-source unified API platform that enables B2B SaaS developers to build product integrations with CRM, HRIS, sales engagement, ticketing, and other business applications. It provides a unified API layer that abstracts away provider-specific differences, managed OAuth authentication, data syncing to data warehouses (BigQuery, Snowflake, Redshift, Postgres), and a management API for configuring customers, connections, and sync configurations. Supported providers include Salesforce, HubSpot, Pipedrive, Zendesk, Slack, and 15+ others. The platform is available as a managed cloud service (api.supaglue.io) and as a self-hosted open-source deployment. The GitHub organization is github.com/supaglue-labs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CRM
  - HRIS
  - Unified API
  - Open Source
  - Integrations
  - Sales Engagement
url: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: supaglue:management-api
    name: Supaglue Management API
    description: 'The Supaglue Management API configures all aspects of the integration platform. Manages customers (the end users of the integrations), their connections to third-party providers, sync configurations, data destinations (BigQuery, Snowflake, Redshift, Postgres), schema and entity mappings, field mappings, providers, sync operations (trigger/pause/resume), sync run history, and magic link generation for OAuth flows. Authentication uses an API key passed via the x-api-key header. Base URL: https://api.supaglue.io/mgmt/v2.'
    humanURL: https://docs.supaglue.com/api/v2/mgmt/management-api
    tags:
      - Management
      - Customers
      - Connections
      - Sync
      - Destinations
    properties:
      - type: Documentation
        url: https://docs.supaglue.com/api/v2/mgmt/management-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/openapi/supaglue-management-api-openapi.yml
  - aid: supaglue:crm-api
    name: Supaglue Unified CRM API
    description: 'The Supaglue Unified CRM API provides a single interface for reading and writing CRM data across Salesforce, HubSpot, Pipedrive, and other providers. Supports accounts, contacts, leads, opportunities, users, custom objects, standard objects, associations, lists, and metadata (custom object schemas, property definitions). All operations use the x-api-key header plus a customer ID context. Base URL: https://api.supaglue.io/crm/v2.'
    humanURL: https://docs.supaglue.com/api/v2/crm/unified-crm-api
    tags:
      - CRM
      - Contacts
      - Accounts
      - Opportunities
      - Leads
      - Salesforce
      - HubSpot
    properties:
      - type: Documentation
        url: https://docs.supaglue.com/api/v2/crm/unified-crm-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/openapi/supaglue-crm-api-openapi.yml
  - aid: supaglue:engagement-api
    name: Supaglue Unified Engagement API
    description: 'The Supaglue Unified Engagement API provides a single interface for reading and writing sales engagement data across Outreach, Salesloft, Apollo, and other sales engagement platforms. Supports accounts, contacts, sequences, sequence states, mailboxes, users, and metadata for custom objects and standard objects. Base URL: https://api.supaglue.io/engagement/v2.'
    humanURL: https://docs.supaglue.com/api/v2/engagement
    tags:
      - Sales Engagement
      - Outreach
      - Salesloft
      - Sequences
      - Contacts
    properties:
      - type: Documentation
        url: https://docs.supaglue.com/api/v2/engagement
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/openapi/supaglue-engagement-api-openapi.yml
  - aid: supaglue:ticketing-api
    name: Supaglue Unified Ticketing API
    description: 'The Supaglue Unified Ticketing API (Preview) provides a single interface for reading ticketing and support data across Zendesk, Linear, and other ticketing platforms. Supports accounts, collections, tickets, tags, contacts, users, and attachments. Base URL: https://api.supaglue.io/ticketing/v2.'
    humanURL: https://docs.supaglue.com/api/v2/ticketing
    tags:
      - Ticketing
      - Support
      - Zendesk
      - Help Desk
    properties:
      - type: Documentation
        url: https://docs.supaglue.com/api/v2/ticketing
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supaglue/refs/heads/main/openapi/supaglue-ticketing-api-openapi.yml
common:
  - type: Website
    url: https://www.supaglue.com/
  - type: Documentation
    url: https://docs.supaglue.com/
  - type: GitHub Organization
    url: https://github.com/supaglue-labs
  - type: Getting Started
    url: https://docs.supaglue.com/getting-started
  - type: API Introduction
    url: https://docs.supaglue.com/api/introduction
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
