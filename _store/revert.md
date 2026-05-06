---
aid: revert
name: Revert
description: Revert is an open-source unified API platform that makes it easy to build product integrations 10x faster. It provides a single standardized API to integrate with CRMs (Salesforce, HubSpot, Zoho CRM, Pipedrive, Close CRM), ticketing systems (Jira, Asana), accounting (Xero, QuickBooks), chat (Slack, Microsoft Teams, Discord), and more, with built-in OAuth management, token refresh, and retry logic.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Integrations
  - CRM
  - Unified API
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/revert/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: revert:revert-unified-api
    name: Revert Unified API
    description: The Revert Unified API provides a single interface to integrate with multiple third-party platforms across CRM, ticketing, chat, and accounting categories. Developers authenticate once per tenant using OAuth 2.0 and access a normalized data model across all supported providers.
    humanURL: https://www.revert.dev/
    baseURL: https://api.revert.dev
    tags:
      - Integrations
      - CRM
      - Unified API
      - Salesforce
      - HubSpot
      - Slack
      - Jira
    properties:
      - type: Documentation
        url: https://docs.revert.dev
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/revert/refs/heads/main/openapi/revert-unified-api-openapi.yml
      - type: GitHub
        url: https://github.com/revertinc/revert
      - type: GitHubOrganization
        url: https://github.com/revertinc
    contact:
      - FN: Revert Support
        url: https://www.revert.dev/
        email: security@revert.dev
features:
  - name: Unified CRM API
    description: Single API surface for Salesforce, HubSpot, Zoho CRM, Pipedrive, and Close CRM
  - name: Ticketing Integration
    description: Unified interface for Jira and Asana project management
  - name: Chat Integration
    description: Unified messaging API for Slack, Microsoft Teams, and Discord
  - name: Accounting Integration
    description: Unified financial data API for Xero and QuickBooks
  - name: OAuth Management
    description: Automatic OAuth token lifecycle management with refresh and failure handling
  - name: Self-Hosting
    description: Full Docker-compose deployment for self-hosted installations
useCases:
  - name: CRM Integration
    description: Build integrations with multiple CRMs through a single API without managing per-provider authentication
  - name: Multi-Platform Ticketing
    description: Read and write tickets across Jira and Asana from a single endpoint
  - name: Unified Messaging
    description: Send and receive messages across chat platforms from one API
integrations:
  - name: Salesforce
    type: CRM
    url: https://www.salesforce.com/
  - name: HubSpot
    type: CRM
    url: https://www.hubspot.com/
  - name: Zoho CRM
    type: CRM
    url: https://www.zoho.com/crm/
  - name: Pipedrive
    type: CRM
    url: https://www.pipedrive.com/
  - name: Close CRM
    type: CRM
    url: https://www.close.com/
  - name: Jira
    type: Ticketing
    url: https://www.atlassian.com/software/jira
  - name: Asana
    type: Ticketing
    url: https://asana.com/
  - name: Slack
    type: Chat
    url: https://slack.com/
  - name: Microsoft Teams
    type: Chat
    url: https://www.microsoft.com/en-us/microsoft-teams/
  - name: Discord
    type: Chat
    url: https://discord.com/
  - name: Xero
    type: Accounting
    url: https://www.xero.com/
  - name: QuickBooks
    type: Accounting
    url: https://quickbooks.intuit.com/
solutions:
  - name: SaaS Integration Platform
    description: Build multi-CRM, multi-ticketing, and multi-chat integrations in your SaaS product
common:
  - type: Website
    url: https://www.revert.dev/
  - type: GitHub
    url: https://github.com/revertinc/revert
  - type: Documentation
    url: https://docs.revert.dev
  - type: Authentication
    url: https://docs.revert.dev
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
