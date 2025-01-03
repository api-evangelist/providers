---
aid: mailchimp
url: >-

  https://raw.githubusercontent.com/api-search/messaging/main/_apis/mailchimp/apis.md
apis:
  - aid: mailchimp:mailchimp-marketing-api
    name: 'Mailchimp Marketing API '
    tags:
      - Root
      - Activity
      - Feed
      - Chatter
      - Accounts
      - Exports
      - Account Export
      - Authorized
      - Applications
      - Authorized Apps
      - Automations
      - Actions
      - Pause
      - Emails
      - Archive
      - Queues
      - Removed
      - Subscribers
      - Batches
      - Batch
      - Webhooks
      - Batch Webhooks
      - Template
      - Folders
      - Template Folders
      - Campaigns
      - Campaign Folders
      - Cancels
      - Send
      - Replicate
      - Schedules
      - Tests
      - Resume
      - Resend
      - Content
      - Feedback
      - Checklist
      - Connected
      - Connected Sites
      - Connected_site_id
      - Verify
      - Scripts
      - Installation
      - Conversations
      - Messages
      - Customers
      - Journeys
      - Steps
      - Trigger
      - Files
      - Managers
      - File Manager
      - Lists
      - List_id
      - Abuse
      - Reports
      - Clients
      - Growth
      - History
      - Month
      - Interest
      - Categories
      - Interests
      - Segments
      - Members
      - Tags
      - Search
      - Events
      - Goals
      - Notes
      - Merge
      - Fields
      - Signup
      - Forms
      - Locations
      - Surveys
      - Publish
      - Email
      - Landing
      - Pages
      - Landing Pages
      - Advice
      - Click
      - Open
      - Domains
      - Performance
      - Eepurl
      - Sent
      - Unsubscribed
      - Ecommerce
      - Product
      - Templates
      - Default
      - Orders
      - Stores
      - Carts
      - Lines
      - Promo
      - Rules
      - Promo_code_id
      - Products
      - Variants
      - Images
      - Pings
      - Facebook
      - Facebook Ads
      - Outreach_id
      - Reporting
      - Questions
      - Answers
      - Response_id
      - Verified
      - Verified Domains
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://mailchimp.com/developer/marketing/
    overlays:
      - url: >-

          overlays/https://api.mailchimp.com/schema/3.0/Swagger.json?expand-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://mailchimp.com/developer/marketing/docs/fundamentals/
        type: Documentation
      - url: properties/mailchimp-marketing-api-openapi.yml
        type: OpenAPI
      - url: https://mailchimp.com/developer/marketing/docs/integrations/
        type: Integrations
      - url: https://mailchimp.com/developer/marketing/docs/errors/
        type: Errors
    description: |-

      The Mailchimp Marketing API provides programmatic access to Mailchimp data
      and functionality, allowing developers to build custom features to do
      things like sync email activity and campaign analytics with their
      database, manage audiences and campaigns, and more.
  - aid: mailchimp:mailchimp-transactional-api
    name: Mailchimp Transactional API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://mailchimp.com/developer/transactional/
    overlays: []
    properties:
      - url: https://mailchimp.com/developer/transactional/docs/fundamentals/
        type: Documentation
      - url: https://mailchimp.com/developer/transactional/guides/quick-start/
        type: Guide
      - url: >-

          https://mailchimp.com/developer/transactional/docs/authentication-delivery/
        type: Authentication
      - url: https://mailchimp.com/developer/transactional/docs/webhooks/
        type: Webhooks
    description: >-
      Mailchimp Transactional is a powerful email delivery service that lets you
      send personalized, one-to-one emails like password resets, order
      confirmations, and welcome messages. 
  - aid: mailchimp:mailchimp-open-commerce
    name: MailChimp Open Commerce
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://mailchimp.com/developer/open-commerce/
    overlays: []
    properties:
      - url: https://mailchimp.com/developer/open-commerce/docs/fundamentals/
        type: Documentation
      - url: https://mailchimp.com/developer/open-commerce/guides/quick-start/
        type: Guides
      - url: https://mailchimp.com/developer/open-commerce/playground/
        type: GraphQL Playground
    description: |-
      An open source, API-first, modular commerce stack made for technical,
      growth-minded retailers. Use our open source platform to build the
      e-commerce solution that fits your business, on your own servers or in the
      cloud.
name: Mailchimp
tags:
  - Email
  - Newsletters
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://mailchimp.com/developer/tools/
    type: Tools
  - url: https://mailchimp.com/developer/
    type: Portal
  - url: https://mailchimp.com/developer/release-notes/
    type: Change Log
  - url: https://mailchimp.com/developer/blog/
    type: Blog
  - url: https://mailchimp.com/pricing/marketing/
    type: Plans
created: 2023/11/23
modified: '2025-01-01'
description: |-

  Mailchimp's developer tools provide everything you need to integrate your data
  with intelligent marketing tools and event-driven transactional email.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---