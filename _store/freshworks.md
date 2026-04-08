---
aid: freshworks
url: https://raw.githubusercontent.com/api-evangelist/freshworks/refs/heads/main/apis.yml
apis:
- aid: freshworks:freshdesk-api
  name: Freshworks Freshdesk API
  tags:
  - Agents
  - Contacts
  - Customer Support
  - Helpdesk
  - Ticketing
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://domain.freshdesk.com/api/v2
  humanURL: https://developers.freshdesk.com/api/
  properties:
  - url: https://developers.freshdesk.com/api/
    type: Documentation
  - url: openapi/freshworks-freshdesk-api-openapi.yml
    type: OpenAPI
  description: The Freshdesk API v2 is a RESTful API that provides programmatic access to Freshdesk helpdesk functionality. It allows developers to manage tickets, contacts, companies, agents, groups, and other helpdesk resources through standard CRUD operations. The API uses JSON for data exchange, supports API key authentication, and enables integration of Freshdesk customer support workflows into third-party applications and automation pipelines.
- aid: freshworks:freshservice-api
  name: Freshworks Freshservice API
  tags:
  - Asset Management
  - IT Service Management
  - ITSM
  - Service Desk
  - Ticketing
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://domain.freshservice.com/api/v2
  humanURL: https://api.freshservice.com/
  properties:
  - url: https://api.freshservice.com/
    type: Documentation
  - url: openapi/freshworks-freshservice-api-openapi.yml
    type: OpenAPI
  description: The Freshservice API v2 is a RESTful API for managing IT service desk operations programmatically. It provides endpoints for tickets, problems, changes, releases, assets, requesters, agents, and other ITSM resources. The API supports Cross-Origin Resource Sharing (CORS) for web-based applications, uses API key authentication via Base64-encoded authorization headers, and allows organizations to automate IT service management workflows and integrate Freshservice with other enterprise tools.
- aid: freshworks:freshsales-api
  name: Freshworks Freshsales API
  tags:
  - Contacts
  - CRM
  - Deals
  - Leads
  - Sales
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://domain.myfreshworks.com/crm/sales/api
  humanURL: https://developers.freshworks.com/crm/api/
  properties:
  - url: https://developers.freshworks.com/crm/api/
    type: Documentation
  - url: openapi/freshworks-freshsales-api-openapi.yml
    type: OpenAPI
  description: The Freshsales API is a RESTful API that enables developers to access and manage CRM data within Freshsales. It supports operations for contacts, accounts, deals, leads, tasks, appointments, notes, and sales activities. The API uses token-based authentication and allows developers to read, modify, add, or delete CRM data, making it possible to build custom integrations, automate sales workflows, and synchronize Freshsales data with other business applications.
- aid: freshworks:freshchat-api
  name: Freshworks Freshchat API
  tags:
  - Chat
  - Conversations
  - Customer Engagement
  - Live Chat
  - Messaging
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.freshchat.com/v2
  humanURL: https://developers.freshchat.com/api/
  properties:
  - url: https://developers.freshchat.com/api/
    type: Documentation
  - url: openapi/freshworks-freshchat-api-openapi.yml
    type: OpenAPI
  description: The Freshchat API provides programmatic access to the Freshchat messaging platform for managing customer conversations and engagement. It supports operations for conversations, messages, agents, channels, and users. The API enables developers to automate customer communication workflows, integrate Freshchat with external systems, and build custom messaging solutions on top of the Freshchat platform. Authentication is handled via API tokens obtained from the Freshchat admin panel.
- aid: freshworks:freshcaller-api
  name: Freshworks Freshcaller API
  tags:
  - Call Center
  - Contact Center
  - Phone
  - Telephony
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://domain.freshcaller.com/api/v1
  humanURL: https://developers.freshcaller.com/api/
  properties:
  - url: https://developers.freshcaller.com/api/
    type: Documentation
  - url: openapi/freshworks-freshcaller-api-openapi.yml
    type: OpenAPI
  description: The Freshcaller API provides access to cloud-based phone system functionality for contact center operations. It allows developers to export call data, call recordings, user information, and agent team details stored in the Freshcaller system. The API supports integration of voice and telephony workflows into broader business applications, enabling organizations to automate call center reporting, synchronize agent data, and build custom dashboards around their phone operations.
- aid: freshworks:freshteam-api
  name: Freshworks Freshteam API
  tags:
  - Applicant Tracking
  - Employees
  - HR
  - Human Resources
  - Recruiting
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://domain.freshteam.com/api
  humanURL: https://developers.freshworks.com/api-sdk/freshteam/
  properties:
  - url: https://developers.freshworks.com/api-sdk/freshteam/
    type: Documentation
  - url: openapi/freshworks-freshteam-api-openapi.yml
    type: OpenAPI
  description: The Freshteam API provides programmatic access to HR and recruiting functionality within the Freshteam platform. It supports operations for managing employees, job postings, candidates, branches, departments, and other HR resources.
- aid: freshworks:freshmarketer-api
  name: Freshworks Freshmarketer API
  tags:
  - Analytics
  - Campaigns
  - Email Marketing
  - Marketing
  - Marketing Automation
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.freshmarketer.com/
  properties:
  - url: https://developer.freshmarketer.com/
    type: Documentation
  description: The Freshmarketer API provides developer access to marketing automation capabilities within the Freshmarketer platform. It enables programmatic management of marketing campaigns, contact lists, email sequences, and conversion optimization workflows. Developers can use the API to integrate Freshmarketer with other marketing tools, automate campaign management, and synchronize marketing data across their technology stack for unified customer engagement analytics.
- aid: freshworks:freshworks-app-sdk
  name: Freshworks App SDK
  tags:
  - App Development
  - Extensions
  - Integrations
  - Platform
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developers.freshworks.com/docs/
  properties:
  - url: https://developers.freshworks.com/docs/
    type: Documentation
  description: The Freshworks App SDK enables developers to build custom applications and extensions that run within the Freshworks product ecosystem. It provides tools for creating apps for Freshdesk, Freshservice, Freshsales, and other Freshworks products using a unified development framework.
name: Freshworks
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Freshworks is a software company that develops cloud-based business software including customer support, IT service management, sales force automation, marketing automation, and HR applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

