---
aid: mailchimp
url: >-

  https://raw.githubusercontent.com/api-search/messaging/main/_apis/mailchimp/apis.md
apis:
  - aid: mailchimp:mailchimp-marketing-api
    name: 'Mailchimp Marketing API '
    tags:
      - Marketing
      - Newsletters
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://mailchimp.com/developer/marketing/
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
    data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Up to 500 contacts, max 1,000 emails/month or 500/day
        elements:
          - name: Easily create email campaigns and learn more about your customers
          - name: Up to 500 contacts
          - name: Max of 1,000/mo or 500/day email sends
          - name: 1 Seat
          - name: 1 Audience
          - name: Email support for first 30 days
          - name: Basic segmentation
          - name: Limited reporting tools
        description: Easily create email campaigns and learn more about your customers
      - id: essentials
        name: Essentials
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 13
            metric: user
            timeFrame: month
            description: Free for 14 days, then starts at $13/month
        elements:
          - name: >-
              Send the right content at the right time with testing and
              scheduling features
          - name: Up to 50,000 contacts with $385/mo tier
          - name: 10X contacts monthly email sends
          - name: 3 Seats
          - name: 3 Audiences
          - name: 24/7 Email & Chat Support
          - name: Up to 4 flow steps for marketing automation
          - name: Basic segmentation
          - name: A/B Testing
          - name: Email scheduling
          - name: SMS add-on available
        description: >-
          Send the right content at the right time with testing and scheduling
          features
      - id: standard
        name: Standard
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 20
            metric: user
            timeFrame: month
            description: Free for 14 days, then starts at $20/month
        elements:
          - name: >-
              Sell even more with personalization, optimization tools, and
              enhanced automations
          - name: Up to 100,000 contacts with $800/mo tier
          - name: 12X contacts monthly email sends
          - name: 5 Seats
          - name: 5 Audiences
          - name: 24/7 Email & Chat Support
          - name: Up to 200 flow steps for marketing automation
          - name: Advanced segmentation
          - name: Custom reports
          - name: Send time optimization
          - name: Dynamic content
          - name: SMS and MMS add-on available
          - name: Generative AI features (no additional cost add-on)
        description: >-
          Sell even more with personalization, optimization tools, and enhanced
          automations
      - id: premium
        name: Premium
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 297.5
            metric: user
            timeFrame: month
            description: $297.50 per month for 12 months, then starts at $350/month
        elements:
          - name: >-
              Scale fast with dedicated onboarding, unlimited contacts, and
              priority support; built for teams
          - name: Unlimited contacts (contact for custom plan)
          - name: 15X contacts monthly email sends
          - name: Unlimited users
          - name: Unlimited audiences
          - name: Phone & Priority Support
          - name: Up to 200 flow steps for marketing automation
          - name: Advanced segmentation
          - name: Multivariate testing
          - name: Comparative reporting
          - name: Predictive segmentation
          - name: Customer lifetime value analytics
          - name: SMS and MMS add-on available
          - name: Generative AI features (no additional cost add-on)
          - name: Premium migration services
          - name: 4 personalized onboarding sessions
        description: >-
          Scale fast with dedicated onboarding, unlimited contacts, and priority
          support; built for teams
    type: Plans
created: 2023/11/23
modified: '2025-09-01'
description: |-

  Mailchimp's developer tools provide everything you need to integrate your data
  with intelligent marketing tools and event-driven transactional email.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---