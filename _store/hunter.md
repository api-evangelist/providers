---
aid: hunter
url: https://raw.githubusercontent.com/api-evangelist/hunter/refs/heads/main/apis.yml
apis:
- name: Hunter Domain Search API
  description: Returns all the email addresses found using a given domain name, with sources.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/domain-search
  baseURL: https://api.hunter.io/v2
  tags:
  - Contact Discovery
  - Domain
  - Email
  - Search
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#domain-search
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Email Finder API
  description: Generates the most likely email address from a domain name, a first name and a last name.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/email-finder
  baseURL: https://api.hunter.io/v2
  tags:
  - Contact Discovery
  - Email
  - Finder
  - Lead Generation
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#email-finder
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Email Verifier API
  description: Verifies the deliverability of a given email address.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/email-verifier
  baseURL: https://api.hunter.io/v2
  tags:
  - Data Quality
  - Email
  - Validation
  - Verification
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#email-verifier
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Email Count API
  description: Returns the number of email addresses found for a given domain.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io
  baseURL: https://api.hunter.io/v2
  tags:
  - Analytics
  - Count
  - Email
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#email-count
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Account API
  description: Returns information about the account associated with the API key.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io
  baseURL: https://api.hunter.io/v2
  tags:
  - Account
  - Management
  - Usage
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#account
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Discover API
  description: Returns companies matching a set of criteria using natural language queries or robust filters to find companies aligned with your ideal customer profile.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/discover
  baseURL: https://api.hunter.io/v2
  tags:
  - Companies
  - Discover
  - Lead Generation
  - Prospecting
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#discover
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Email Enrichment API
  description: Returns comprehensive personal information linked to an email address or LinkedIn profile, providing enriched data points about the person.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/lead-enrichment
  baseURL: https://api.hunter.io/v2
  tags:
  - Data
  - Email
  - Enrichment
  - People
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#email-enrichment
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Company Enrichment API
  description: Returns detailed organizational data associated with a domain name, including company size, industry, location, and other firmographic information.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/company-enrichment
  baseURL: https://api.hunter.io/v2
  tags:
  - Company
  - Data
  - Enrichment
  - Firmographic
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#company-enrichment
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Combined Enrichment API
  description: Merges person and company information for a single email address, returning enriched records combining both datasets.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/combined-enrichment
  baseURL: https://api.hunter.io/v2
  tags:
  - Combined
  - Company
  - Enrichment
  - People
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#combined-enrichment
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Leads API
  description: Allows you to manage the leads stored in Hunter, including listing, creating, updating, upserting, and deleting leads.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/leads
  baseURL: https://api.hunter.io/v2
  tags:
  - Contacts
  - CRM
  - Leads
  - Management
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#leads
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  - type: JSONSchema
    url: json-schema/hunter-lead-schema.json
  - type: JSONLDContext
    url: json-ld/hunter-context.jsonld
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Leads Lists API
  description: Allows you to manage leads lists in Hunter, including listing, creating, updating, and deleting lead collection groups.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/leads
  baseURL: https://api.hunter.io/v2
  tags:
  - Leads
  - Lists
  - Management
  - Organization
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#leads_lists
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  - type: JSONSchema
    url: json-schema/hunter-lead-schema.json
  - type: JSONLDContext
    url: json-ld/hunter-context.jsonld
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Campaigns API
  description: Allows you to manage email sequences including listing campaigns, managing recipients, and starting sequences for automated email outreach.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/campaigns
  baseURL: https://api.hunter.io/v2
  tags:
  - Automation
  - Campaigns
  - Email Outreach
  - Sequences
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#campaigns
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
- name: Hunter Logo API
  description: Retrieves any company logo using a domain name. Free to use with no authentication required, just a backlink from your site to hunter.io.
  image: https://hunter.io/images/hunter-logo.png
  humanURL: https://hunter.io/api/logo
  baseURL: https://logos.hunter.io
  tags:
  - Branding
  - Company
  - Images
  - Logo
  properties:
  - type: Documentation
    url: https://hunter.io/api-documentation/v2#logo
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  contact:
  - FN: Hunter Support
    email: support@hunter.io
    url: https://hunter.io/contact
name: Hunter
tags:
- API
type: Contract
image: https://hunter.io/images/hunter-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Hunter is an email finding and verification service that helps find professional email addresses associated with a domain and verify email deliverability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

