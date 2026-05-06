---
aid: hunter
name: Hunter
description: Hunter is an email finding and verification service that helps find professional email addresses associated with a domain and verify email deliverability.
image: https://hunter.io/images/hunter-logo.png
url: https://raw.githubusercontent.com/api-evangelist/hunter/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
tags:
  - Contact Discovery
  - Email
  - Email Verification
  - Lead Generation
  - Prospecting
  - Sales Intelligence
apis:
  - aid: hunter:domain-search
    name: Hunter Domain Search API
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
  - aid: hunter:email-finder
    name: Hunter Email Finder API
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
  - aid: hunter:email-verifier
    name: Hunter Email Verifier API
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
  - aid: hunter:email-count
    name: Hunter Email Count API
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
  - aid: hunter:account
    name: Hunter Account API
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
  - aid: hunter:discover
    name: Hunter Discover API
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
  - aid: hunter:email-enrichment
    name: Hunter Email Enrichment API
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
  - aid: hunter:company-enrichment
    name: Hunter Company Enrichment API
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
  - aid: hunter:combined-enrichment
    name: Hunter Combined Enrichment API
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
  - aid: hunter:leads
    name: Hunter Leads API
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
      - type: JSONLD
        url: json-ld/hunter-context.jsonld
    contact:
      - FN: Hunter Support
        email: support@hunter.io
        url: https://hunter.io/contact
  - aid: hunter:leads-lists
    name: Hunter Leads Lists API
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
      - type: JSONLD
        url: json-ld/hunter-context.jsonld
    contact:
      - FN: Hunter Support
        email: support@hunter.io
        url: https://hunter.io/contact
  - aid: hunter:campaigns
    name: Hunter Campaigns API
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
  - aid: hunter:logo
    name: Hunter Logo API
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
common:
  - type: Portal
    url: https://hunter.io/api
  - type: Documentation
    url: https://hunter.io/api-documentation/v2
  - type: OpenAPI
    url: openapi/hunter-api-openapi.yml
  - type: JSONSchema
    url: json-schema/hunter-lead-schema.json
  - type: JSONLD
    url: json-ld/hunter-context.jsonld
  - type: Authentication
    url: https://hunter.io/api-documentation/v2#authentication
  - type: RateLimits
    url: https://hunter.io/api-documentation/v2#rate-limiting
  - type: Pricing
    url: https://hunter.io/pricing
  - type: TermsOfService
    url: https://hunter.io/terms
  - type: PrivacyPolicy
    url: https://hunter.io/privacy-policy
  - type: StatusPage
    url: https://status.hunter.io
  - type: Blog
    url: https://hunter.io/blog
  - type: Login
    url: https://hunter.io/users/sign_in
  - type: SignUp
    url: https://hunter.io/users/sign_up
  - type: ChangeLog
    url: https://hunter.io/changelog
  - type: Integrations
    url: https://hunter.io/integrations
  - type: GitHubOrganization
    url: https://github.com/hunter-io
  - type: Contact
    url: https://hunter.io/contact
  - type: Support
    url: https://help.hunter.io
  - type: NaftikoCapability
    url: capabilities/shared/hunter-api.yaml
    title: Hunter API Shared Definition
  - type: NaftikoCapability
    url: capabilities/sales-prospecting.yaml
    title: Sales Prospecting Workflow
  - type: Features
    data:
      - name: Domain Search
        description: Find all email addresses associated with a domain name along with confidence scores and sources.
      - name: Email Finder
        description: Generate the most likely email address for a person given their name and company domain.
      - name: Email Verification
        description: Verify the deliverability and validity of email addresses with detailed status reporting.
      - name: Lead Management
        description: Store, organize, and manage prospect leads with lists, tags, and CRM-like contact management.
      - name: Email Campaigns
        description: Create and manage automated email outreach sequences with recipient tracking and scheduling.
      - name: Data Enrichment
        description: Enrich email addresses and domains with personal, company, and firmographic data points.
      - name: Company Discovery
        description: Find companies matching ideal customer profiles using natural language queries and advanced filters.
  - type: UseCases
    data:
      - name: Sales Prospecting
        description: Find and verify email addresses for sales outreach by searching company domains and building prospect lists.
      - name: Lead Qualification
        description: Enrich leads with company and personal data to qualify prospects and prioritize outreach efforts.
      - name: Email List Cleaning
        description: Verify large email lists to reduce bounce rates and improve email deliverability.
      - name: Account-Based Marketing
        description: Discover key contacts at target accounts using domain search and build targeted outreach campaigns.
      - name: Recruitment Outreach
        description: Find professional email addresses for passive candidates at target companies for recruitment campaigns.
  - type: Integrations
    data:
      - name: Salesforce
        description: Push verified leads and enriched contacts directly to Salesforce CRM for pipeline management.
      - name: HubSpot
        description: Sync leads and contact data with HubSpot CRM for unified sales and marketing workflows.
      - name: Pipedrive
        description: Export leads to Pipedrive CRM with enriched contact and company information.
      - name: Zapier
        description: Connect Hunter with thousands of apps through Zapier for automated lead processing workflows.
      - name: Google Sheets
        description: Export domain search results and verified emails directly to Google Sheets for analysis.
      - name: Zoho CRM
        description: Integrate lead data with Zoho CRM for end-to-end sales pipeline management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
