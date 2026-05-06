---
aid: truto
url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/apis.yml
name: Truto
description: Truto is a unified API and embedded integration platform that enables B2B SaaS companies to ship native integrations without writing integration-specific code. Founded in 2023, Truto uses a declarative, config-driven architecture where every connector is data, not code. The platform provides Unified APIs across four major categories — HRIS (41 providers, 20 resources), ATS (27 providers, 17 resources), CRM (27 providers, 17 resources), and an expanding set of additional categories — plus an Admin API for managing integrated accounts, generating link tokens, and programmatic MCP server provisioning. Truto supports real-time pass-through (no data stored in between), full schema customization via JSONata, and one-API-call MCP server generation for AI agent access. Authentication uses Bearer tokens. Truto supports over 250 integrations and is available as Truto Cloud or on-premise.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Unified API
  - Integration Platform
  - HRIS
  - ATS
  - CRM
  - Embedded Integrations
  - MCP
  - AI Agents
  - SaaS
access: 3rd-Party
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: truto:truto-admin-api
    name: Truto Admin API
    tags:
      - Administration
      - Integrated Accounts
      - Link Tokens
      - MCP
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truto.one
    humanURL: https://truto.one/docs/api-reference/admin
    properties:
      - url: https://truto.one/docs/api-reference/admin
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/openapi/truto-admin-openapi.yml
        type: OpenAPI
    description: The Truto Admin API enables programmatic management of the Truto platform, including creating and managing integrated accounts, generating link tokens for customer-initiated OAuth flows, running post-install actions, and provisioning MCP servers. Integrated accounts represent a connection between your Truto account and a customer's connected app. Link tokens initiate the Truto linking process from within your application. The Admin API uses Bearer token authentication with the tenant API token.
  - aid: truto:truto-unified-hris-api
    name: Truto Unified HRIS API
    tags:
      - HRIS
      - Human Resources
      - Employees
      - Payroll
      - Unified API
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truto.one/unified/hris
    humanURL: https://truto.one/docs/api-reference/unified-hris-api
    properties:
      - url: https://truto.one/docs/api-reference/unified-hris-api
        type: Documentation
      - url: https://truto.one/unified-apis/hris/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/openapi/truto-unified-hris-openapi.yml
        type: OpenAPI
    description: The Truto Unified HRIS API provides a single normalized interface for accessing HR data across 41 HRIS providers including BambooHR, Workday, Rippling, Gusto, HiBob, Personio, and more. Offers 20 unified resources including employees, employments, companies, groups (departments and roles), timeoff requests, and more. Data is accessed in real-time with no caching. Schema can be extended using JSONata mappings. Authentication uses Bearer token with integrated_account_id query parameter to specify the target connected account.
  - aid: truto:truto-unified-ats-api
    name: Truto Unified ATS API
    tags:
      - ATS
      - Applicant Tracking
      - Recruiting
      - Jobs
      - Candidates
      - Unified API
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truto.one/unified/ats
    humanURL: https://truto.one/docs/api-reference/unified-ats-api
    properties:
      - url: https://truto.one/docs/api-reference/unified-ats-api
        type: Documentation
      - url: https://truto.one/unified-apis/ats/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/openapi/truto-unified-ats-openapi.yml
        type: OpenAPI
    description: 'The Truto Unified ATS API provides a single normalized interface for accessing applicant tracking system data across 27 ATS providers including Greenhouse, Lever, Workable, SmartRecruiters, Ashby, Teamtailor, and more. Offers 17 unified resources covering the full recruiting lifecycle: jobs, candidates, applications, interview stages, interviews, scorecards, offers, EEOC data, departments, offices, reject reasons, activities, attachments, tags, and users. Authentication uses Bearer token with integrated_account_id query parameter.'
  - aid: truto:truto-unified-crm-api
    name: Truto Unified CRM API
    tags:
      - CRM
      - Customer Relationship Management
      - Contacts
      - Opportunities
      - Unified API
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truto.one/unified/crm
    humanURL: https://truto.one/docs/api-reference/unified-crm-api
    properties:
      - url: https://truto.one/docs/api-reference/unified-crm-api
        type: Documentation
      - url: https://truto.one/unified-apis/crm/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/openapi/truto-unified-crm-openapi.yml
        type: OpenAPI
    description: The Truto Unified CRM API provides a single normalized interface for accessing CRM data across 27 CRM providers including Salesforce, HubSpot, Pipedrive, Attio, Outreach, and more. Offers 17 unified resources including accounts, contacts, opportunities, tasks, users, stages, engagements, notes, fields, associations, and more. Data is accessed in real-time via pass-through to underlying CRM APIs. Authentication uses Bearer token with integrated_account_id query parameter.
common:
  - url: https://truto.one/
    name: Truto Website
    type: Website
  - url: https://truto.one/docs/
    name: Developer Documentation
    type: Documentation
  - url: https://truto.one/docs/api-reference/overview/introduction
    name: API Reference Introduction
    type: Documentation
  - url: https://truto.one/docs/getting-started
    name: Getting Started
    type: GettingStarted
  - url: https://truto.one/integrations/
    name: Integration Directory
    type: Integrations
  - url: https://truto.one/unified-apis/
    name: Unified APIs
    type: Documentation
  - url: https://truto.one/blog/
    name: Truto Blog
    type: Blog
  - url: https://github.com/trutohq
    name: Truto on GitHub
    type: GitHub
  - url: https://truto.one/docs/api-reference/overview/introduction
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/rules/truto-rules.yml
    name: Spectral Rules
    type: SpectralRules
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
