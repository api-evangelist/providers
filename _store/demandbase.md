---
aid: demandbase
url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/apis.yml
apis:
- name: Demandbase API
  description: The Demandbase API provides programmatic access to account identification, firmographic data, and visitor intelligence to enable account-based experiences.
  image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
  humanURL: https://www.demandbase.com
  baseURL: https://api.demandbase.com
  tags:
  - Accounts
  - B2b Data
  - Firmographics
  - Identification
  properties:
  - type: documentation
    url: https://docs.demandbase.com/
  - type: openapi
    url: https://api.demandbase.com/openapi.json
  - type: authentication
    url: https://docs.demandbase.com/docs/authentication
  - type: OpenAPI
    url: openapi/demandbase-api-openapi.yml
- name: Demandbase Real-Time Identification API
  description: Identifies companies visiting your website in real-time based on IP address and provides firmographic data and intent signals.
  humanURL: https://www.demandbase.com/solutions/demandbase-one/
  baseURL: https://api.company-target.com
  tags:
  - Identification
  - Ip Intelligence
  - Real-Time
  - Visitor Tracking
  properties:
  - type: documentation
    url: https://docs.demandbase.com/docs/real-time-identification-api
  - type: use-cases
    url: https://www.demandbase.com/use-cases/
  - type: OpenAPI
    url: openapi/demandbase-real-time-identification-openapi.yml
- name: Demandbase Advertising API
  description: Programmatically manage advertising campaigns, audiences, and performance metrics for account-based advertising.
  humanURL: https://www.demandbase.com/solutions/advertising/
  baseURL: https://api.demandbase.com/advertising
  tags:
  - Abm
  - Advertising
  - Audiences
  - Campaigns
  properties:
  - type: documentation
    url: https://docs.demandbase.com/docs/advertising-api
  - type: rate-limits
    url: https://docs.demandbase.com/docs/api-rate-limits
  - type: OpenAPI
    url: openapi/demandbase-advertising-openapi.yml
- name: Demandbase Engagement API
  description: Access engagement data and activity streams for target accounts across web, email, and advertising channels.
  humanURL: https://www.demandbase.com/solutions/engagement/
  baseURL: https://api.demandbase.com/engagement
  tags:
  - Account Insights
  - Activity Tracking
  - Analytics
  - Engagement
  properties:
  - type: documentation
    url: https://docs.demandbase.com/docs/engagement-api
  - type: webhooks
    url: https://docs.demandbase.com/docs/webhooks
  - type: OpenAPI
    url: openapi/demandbase-engagement-openapi.yml
- name: Demandbase Account List API
  description: Create, manage, and sync target account lists for ABM campaigns and personalization efforts.
  humanURL: https://www.demandbase.com
  baseURL: https://api.demandbase.com/accounts
  tags:
  - Account Lists
  - Crm Sync
  - List Management
  - Target Accounts
  properties:
  - type: documentation
    url: https://docs.demandbase.com/docs/account-list-api
  - type: integration-guides
    url: https://docs.demandbase.com/docs/integrations
  - type: OpenAPI
    url: openapi/demandbase-account-list-openapi.yml
- name: Demandbase B2B Data API
  description: REST-based API providing programmatic access to B2B company and contact intelligence, including company search, contact discovery, data enrichment, and firmographic data across millions of businesses.
  image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
  humanURL: https://www.demandbase.com/products/data/api-integration/
  baseURL: https://api.demandbase.com
  tags:
  - B2b Data
  - Company Search
  - Contact Discovery
  - Data Enrichment
  - Firmographics
  properties:
  - type: documentation
    url: https://kb.demandbase.com/hc/en-us/categories/6520773158171-API
  - type: getting-started
    url: https://kb.demandbase.com/hc/en-us/sections/7272741440667-API-Introduction-and-Overview
  - type: OpenAPI
    url: openapi/demandbase-b2b-data-openapi.yml
- name: Demandbase IP API
  description: Returns firmographic data for a specific IP address or cookie, enabling real-time company identification of website visitors with attributes including employee count, revenue, industry, and corporate hierarchy with parent and ultimate parent IDs.
  image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
  humanURL: https://www.demandbase.com/products/data/api-integration/
  baseURL: https://api.demandbase.com
  tags:
  - Company Identification
  - Firmographics
  - Ip Intelligence
  - Real-Time
  - Visitor Identification
  properties:
  - type: documentation
    url: https://support.demandbase.com/hc/en-us/articles/23789223879323-Demandbase-IP-API-v3-for-Demandbase-One-Current-Version
  - type: change-log
    url: https://support.demandbase.com/hc/en-us/articles/25137915441947-Upgrading-to-Demandbase-IP-API-v3
  - type: OpenAPI
    url: openapi/demandbase-ip-openapi.yml
- name: Demandbase Admin API
  description: Provides programmatic access to user management and platform administration capabilities, including creating, reading, updating, and deleting users and managing API key sets for Demandbase One.
  image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
  humanURL: https://www.demandbase.com
  baseURL: https://api.demandbase.com
  tags:
  - Administration
  - Api Keys
  - Platform Management
  - User Management
  properties:
  - type: documentation
    url: https://support.demandbase.com/hc/en-us/sections/360011444531-API-Documentation
  - type: authentication
    url: https://support.demandbase.com/hc/en-us/articles/38999526296603-Generate-and-Manage-API-Key-Sets
  - type: OpenAPI
    url: openapi/demandbase-admin-openapi.yml
- name: Demandbase Data Export API
  description: Enables bulk, asynchronous, programmatic data exports from Demandbase One, supporting extraction of records for accounts, people, opportunities, activities, campaigns, and Buying Groups with full granularity, delivered as downloadable CSVs up to 10GB per day.
  image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
  humanURL: https://www.demandbase.com/resources/solution-sheet/data-export-api/
  baseURL: https://api.demandbase.com
  tags:
  - Accounts
  - Analytics
  - Bulk Export
  - Data Export
  - Reporting
  properties:
  - type: documentation
    url: https://support.demandbase.com/hc/en-us/articles/26668967193627-Understanding-the-Demandbase-API-Suite-and-MCP
  - type: OpenAPI
    url: openapi/demandbase-data-export-openapi.yml
- name: Demandbase Data Import API
  description: Allows bulk, asynchronous, programmatic import of new data rows into Demandbase One or updates to existing records, supporting data on accounts, people, opportunities, and activities with CSV-based ingestion.
  image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
  humanURL: https://www.demandbase.com
  baseURL: https://api.demandbase.com
  tags:
  - Accounts
  - Bulk Import
  - Csv
  - Data Import
  - Data Ingestion
  properties:
  - type: documentation
    url: https://support.demandbase.com/hc/en-us/articles/26668967193627-Understanding-the-Demandbase-API-Suite-and-MCP
  - type: OpenAPI
    url: openapi/demandbase-data-import-openapi.yml
name: Demandbase
tags:
- Account-Based Marketing
- Advertising
- Ai Agents
- B2b Marketing
- Data Enrichment
- Intent Data
- Personalization
- Sales Intelligence
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Demandbase is the leading Account-Based Marketing (ABM) platform that helps B2B companies identify, engage, and convert target accounts through intent data, advertising, personalization, and sales intelligence.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

