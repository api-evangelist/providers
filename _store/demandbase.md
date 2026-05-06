---
aid: demandbase
name: Demandbase
description: Demandbase is the leading Account-Based Marketing (ABM) platform that helps B2B companies identify, engage, and convert target accounts through intent data, advertising, personalization, and sales intelligence.
type: Index
position: Consumer
access: 3rd-Party
xType: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/apis.yml
created: '2024-01-20'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Account-Based Marketing
  - Advertising
  - AI Agents
  - B2B Marketing
  - Data Enrichment
  - Intent Data
  - Personalization
  - Sales Intelligence
apis:
  - aid: demandbase:demandbase-api
    name: Demandbase API
    description: The Demandbase API provides programmatic access to account identification, firmographic data, and visitor intelligence to enable account-based experiences.
    image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
    humanURL: https://www.demandbase.com
    baseURL: https://api.demandbase.com
    tags:
      - Accounts
      - B2B Data
      - Firmographics
      - Identification
    properties:
      - type: Documentation
        url: https://docs.demandbase.com/
      - type: Authentication
        url: https://docs.demandbase.com/docs/authentication
      - type: OpenAPI
        url: openapi/demandbase-api-openapi.yml
      - type: Rules
        url: rules/demandbase-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/demandbase-account-schema.json
  - aid: demandbase:demandbase-real-time-identification-api
    name: Demandbase Real-Time Identification API
    description: Identifies companies visiting your website in real-time based on IP address and provides firmographic data and intent signals.
    humanURL: https://www.demandbase.com/solutions/demandbase-one/
    baseURL: https://api.company-target.com
    tags:
      - Identification
      - IP Intelligence
      - Real-Time
      - Visitor Tracking
    properties:
      - type: Documentation
        url: https://docs.demandbase.com/docs/real-time-identification-api
      - type: UseCases
        url: https://www.demandbase.com/use-cases/
      - type: OpenAPI
        url: openapi/demandbase-real-time-identification-openapi.yml
      - type: Rules
        url: rules/demandbase-real-time-identification-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-real-time-identification-api-capabilities.yml
  - aid: demandbase:demandbase-advertising-api
    name: Demandbase Advertising API
    description: Programmatically manage advertising campaigns, audiences, and performance metrics for account-based advertising.
    humanURL: https://www.demandbase.com/solutions/advertising/
    baseURL: https://api.demandbase.com/advertising
    tags:
      - ABM
      - Advertising
      - Audiences
      - Campaigns
    properties:
      - type: Documentation
        url: https://docs.demandbase.com/docs/advertising-api
      - type: RateLimits
        url: https://docs.demandbase.com/docs/api-rate-limits
      - type: OpenAPI
        url: openapi/demandbase-advertising-openapi.yml
      - type: Rules
        url: rules/demandbase-advertising-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-advertising-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/demandbase-campaign-schema.json
  - aid: demandbase:demandbase-engagement-api
    name: Demandbase Engagement API
    description: Access engagement data and activity streams for target accounts across web, email, and advertising channels.
    humanURL: https://www.demandbase.com/solutions/engagement/
    baseURL: https://api.demandbase.com/engagement
    tags:
      - Account Insights
      - Activity Tracking
      - Analytics
      - Engagement
    properties:
      - type: Documentation
        url: https://docs.demandbase.com/docs/engagement-api
      - type: Webhooks
        url: https://docs.demandbase.com/docs/webhooks
      - type: OpenAPI
        url: openapi/demandbase-engagement-openapi.yml
      - type: Rules
        url: rules/demandbase-engagement-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-engagement-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/demandbase-engagement-schema.json
  - aid: demandbase:demandbase-account-list-api
    name: Demandbase Account List API
    description: Create, manage, and sync target account lists for ABM campaigns and personalization efforts.
    humanURL: https://www.demandbase.com
    baseURL: https://api.demandbase.com/accounts
    tags:
      - Account Lists
      - CRM Sync
      - List Management
      - Target Accounts
    properties:
      - type: Documentation
        url: https://docs.demandbase.com/docs/account-list-api
      - type: IntegrationGuides
        url: https://docs.demandbase.com/docs/integrations
      - type: OpenAPI
        url: openapi/demandbase-account-list-openapi.yml
      - type: Rules
        url: rules/demandbase-account-list-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-account-list-api-capabilities.yml
  - aid: demandbase:demandbase-b2b-data-api
    name: Demandbase B2B Data API
    description: REST-based API providing programmatic access to B2B company and contact intelligence, including company search, contact discovery, data enrichment, and firmographic data across millions of businesses.
    image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
    humanURL: https://www.demandbase.com/products/data/api-integration/
    baseURL: https://api.demandbase.com
    tags:
      - B2B Data
      - Company Search
      - Contact Discovery
      - Data Enrichment
      - Firmographics
    properties:
      - type: Documentation
        url: https://kb.demandbase.com/hc/en-us/categories/6520773158171-API
      - type: GettingStarted
        url: https://kb.demandbase.com/hc/en-us/sections/7272741440667-API-Introduction-and-Overview
      - type: OpenAPI
        url: openapi/demandbase-b2b-data-openapi.yml
      - type: Rules
        url: rules/demandbase-b2b-data-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-b2b-data-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/demandbase-contact-schema.json
  - aid: demandbase:demandbase-ip-api
    name: Demandbase IP API
    description: Returns firmographic data for a specific IP address or cookie, enabling real-time company identification of website visitors with attributes including employee count, revenue, industry, and corporate hierarchy with parent and ultimate parent IDs.
    image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
    humanURL: https://www.demandbase.com/products/data/api-integration/
    baseURL: https://api.demandbase.com
    tags:
      - Company Identification
      - Firmographics
      - IP Intelligence
      - Real-Time
      - Visitor Identification
    properties:
      - type: Documentation
        url: https://support.demandbase.com/hc/en-us/articles/23789223879323-Demandbase-IP-API-v3-for-Demandbase-One-Current-Version
      - type: ChangeLog
        url: https://support.demandbase.com/hc/en-us/articles/25137915441947-Upgrading-to-Demandbase-IP-API-v3
      - type: OpenAPI
        url: openapi/demandbase-ip-openapi.yml
      - type: Rules
        url: rules/demandbase-ip-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-ip-api-capabilities.yml
  - aid: demandbase:demandbase-admin-api
    name: Demandbase Admin API
    description: Provides programmatic access to user management and platform administration capabilities, including creating, reading, updating, and deleting users and managing API key sets for Demandbase One.
    image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
    humanURL: https://www.demandbase.com
    baseURL: https://api.demandbase.com
    tags:
      - Administration
      - API Keys
      - Platform Management
      - User Management
    properties:
      - type: Documentation
        url: https://support.demandbase.com/hc/en-us/sections/360011444531-API-Documentation
      - type: Authentication
        url: https://support.demandbase.com/hc/en-us/articles/38999526296603-Generate-and-Manage-API-Key-Sets
      - type: OpenAPI
        url: openapi/demandbase-admin-openapi.yml
      - type: Rules
        url: rules/demandbase-admin-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-admin-api-capabilities.yml
  - aid: demandbase:demandbase-data-export-api
    name: Demandbase Data Export API
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
      - type: Documentation
        url: https://support.demandbase.com/hc/en-us/articles/26668967193627-Understanding-the-Demandbase-API-Suite-and-MCP
      - type: OpenAPI
        url: openapi/demandbase-data-export-openapi.yml
      - type: Rules
        url: rules/demandbase-data-export-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-data-export-api-capabilities.yml
  - aid: demandbase:demandbase-data-import-api
    name: Demandbase Data Import API
    description: Allows bulk, asynchronous, programmatic import of new data rows into Demandbase One or updates to existing records, supporting data on accounts, people, opportunities, and activities with CSV-based ingestion.
    image: https://www.demandbase.com/wp-content/themes/demandbase/assets/images/demandbase-logo.svg
    humanURL: https://www.demandbase.com
    baseURL: https://api.demandbase.com
    tags:
      - Accounts
      - Bulk Import
      - CSV
      - Data Import
      - Data Ingestion
    properties:
      - type: Documentation
        url: https://support.demandbase.com/hc/en-us/articles/26668967193627-Understanding-the-Demandbase-API-Suite-and-MCP
      - type: OpenAPI
        url: openapi/demandbase-data-import-openapi.yml
      - type: Rules
        url: rules/demandbase-data-import-api-rules.yml
      - type: Capabilities
        url: capabilities/demandbase-data-import-api-capabilities.yml
common:
  - type: GettingStarted
    url: https://docs.demandbase.com/docs/getting-started
  - type: Authentication
    url: https://docs.demandbase.com/docs/authentication
  - type: Status
    url: https://status.demandbase.com/
  - type: Support
    url: https://support.demandbase.com/
  - type: PrivacyPolicy
    url: https://www.demandbase.com/privacy-policy/
  - type: TermsOfService
    url: https://www.demandbase.com/terms-of-service/
  - type: Blog
    url: https://www.demandbase.com/blog/
  - type: Contact
    url: https://www.demandbase.com/contact/
  - type: LinkedIn
    url: https://www.linkedin.com/company/demandbase/
  - type: Twitter
    url: https://twitter.com/Demandbase
  - type: Portal
    url: https://developer.demandbase.com
  - type: KnowledgeBase
    url: https://kb.demandbase.com/hc/en-us
  - type: Partners
    url: https://partners.demandbase.com/
  - type: Integrations
    url: https://partners.demandbase.com/t/partners/integrations
  - type: TermsOfUse
    url: https://www.demandbase.com/terms-of-use/
  - type: SignUp
    url: https://www.demandbase.com/products/data/api-integration/api-trial/
  - type: JSON-LD
    url: json-ld/demandbase-context.jsonld
  - type: JSONSchema
    url: json-schema/demandbase-account-schema.json
  - type: JSONSchema
    url: json-schema/demandbase-contact-schema.json
  - type: JSONSchema
    url: json-schema/demandbase-campaign-schema.json
  - type: JSONSchema
    url: json-schema/demandbase-engagement-schema.json
  - type: Vocabulary
    url: vocabulary/demandbase-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://www.demandbase.com
---
