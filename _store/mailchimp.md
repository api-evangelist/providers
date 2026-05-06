---
aid: mailchimp
url: https://raw.githubusercontent.com/api-evangelist/mailchimp/refs/heads/main/apis.yml
apis:
  - aid: mailchimp:mailchimp-marketing-api
    name: Mailchimp Marketing API
    tags:
      - Audiences
      - Automation
      - Campaigns
      - Email Marketing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://server.api.mailchimp.com/3.0
    humanURL: https://mailchimp.com/developer/marketing/
    properties:
      - url: https://mailchimp.com/developer/marketing/docs/fundamentals/
        type: Documentation
      - url: openapi/mailchimp-marketing-api-openapi.yml
        type: OpenAPI
      - url: json-schema/campaign.json
        type: JSONSchema
      - url: json-schema/audience.json
        type: JSONSchema
      - url: json-schema/member.json
        type: JSONSchema
      - url: json-schema/template.json
        type: JSONSchema
      - url: json-ld/context.jsonld
        type: JSONLD
      - url: https://mailchimp.com/developer/marketing/docs/integrations/
        type: Integrations
      - url: https://mailchimp.com/developer/marketing/docs/errors/
        type: Errors
      - url: https://mailchimp.com/developer/marketing/api/
        type: APIReference
      - url: https://mailchimp.com/developer/marketing/guides/quick-start/
        type: GettingStarted
      - url: https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
        type: Authentication
      - url: https://mailchimp.com/developer/marketing/docs/e-commerce/
        type: E-Commerce
      - url: https://mailchimp.com/developer/marketing/docs/methods-parameters/
        type: Methods and Parameters
    description: The Mailchimp Marketing API provides programmatic access to Mailchimp data and functionality, allowing developers to build custom features to sync email activity and campaign analytics with their database, manage audiences and campaigns, and more.
  - aid: mailchimp:mailchimp-transactional-api
    name: Mailchimp Transactional API
    tags:
      - Email Delivery
      - Messaging
      - Transactional Email
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://mandrillapp.com/api/1.0
    humanURL: https://mailchimp.com/developer/transactional/
    overlays: []
    properties:
      - url: https://mailchimp.com/developer/transactional/docs/fundamentals/
        type: Documentation
      - url: openapi/mailchimp-transactional-api-openapi.yml
        type: OpenAPI
      - url: json-ld/context.jsonld
        type: JSONLD
      - url: https://mailchimp.com/developer/transactional/guides/quick-start/
        type: GettingStarted
      - url: https://mailchimp.com/developer/transactional/docs/authentication-delivery/
        type: Authentication
      - url: https://mailchimp.com/developer/transactional/docs/webhooks/
        type: Webhooks
      - url: https://mailchimp.com/developer/transactional/api/
        type: APIReference
      - url: https://mailchimp.com/developer/transactional/guides/send-first-email/
        type: GettingStarted
      - url: https://mailchimp.com/developer/transactional/docs/outbound-email/
        type: Outbound Email
      - url: https://mailchimp.com/developer/transactional/docs/tags-metadata/
        type: Tags and Metadata
    description: Mailchimp Transactional (formerly Mandrill) is a powerful email delivery service that lets you send personalized, one-to-one emails like password resets, order confirmations, and welcome messages.
  - aid: mailchimp:mailchimp-open-commerce
    name: Mailchimp Open Commerce
    tags:
      - E-Commerce
      - GraphQL
      - Headless Commerce
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://mailchimp.com/developer/open-commerce/
    overlays: []
    properties:
      - url: https://mailchimp.com/developer/open-commerce/docs/fundamentals/
        type: Documentation
      - url: https://mailchimp.com/developer/open-commerce/guides/quick-start/
        type: GettingStarted
      - url: https://mailchimp.com/developer/open-commerce/playground/
        type: GraphQL Playground
      - url: https://mailchimp.com/developer/open-commerce/guides/build-api-plugin/
        type: Plugin Development
      - url: https://mailchimp.com/developer/open-commerce/docs/sharing-code-between-plugins/
        type: Sharing Code Between Plugins
      - url: https://github.com/reactioncommerce
        type: GitHubOrganization
      - url: https://mailchimp.com/developer/open-commerce/docs/contribute-open-commerce/
        type: Contributing
    description: An open source, API-first, modular commerce stack built using Node.js, React, and GraphQL. Formerly known as Reaction Commerce, the project has been discontinued but documentation remains available.
name: Mailchimp
tags:
  - Campaigns
  - Email Marketing
  - Marketing Automation
  - Newsletters
  - Transactional Email
image: https://mailchimp.com/release/plums/cxp/images/apple-touch-icon.png
common:
  - url: https://mailchimp.com/features/
    type: Features
    data:
      - 'Free: 250 contacts, ~500 sends/mo, 1 audience'
      - 'Essentials at $13/mo (500 contacts): A/B testing, 4-step automations'
      - 'Standard at $20/mo: 200 automation flows, Generative AI'
      - 'Premium at $350/mo: predictive segmentation, multivariate testing'
      - Marketing API v3 with REST + Batch operations
      - 'Concurrency limit: 10 simultaneous connections per user'
      - 'Batch operations: 1,000 ops/request, 500 open batches'
      - Transactional Email (Mandrill) priced separately
      - OAuth 2.0 and API keys
      - Webhooks for subscribe/unsubscribe/profile/cleaned/upemail/campaign
      - Audiences with tags, segments, custom fields
      - Automations with conditional logic
      - Customer Journey Builder
      - Landing pages, popup forms, signup forms
      - 'Reports: opens, clicks, bounces, conversions'
      - Pricing scales with active contact count
    sources:
      - https://mailchimp.com/pricing/marketing/
    updated: '2026-05-04'
  - url: https://mailchimp.com/solutions/
    type: UseCases
  - url: https://mailchimp.com/integrations/
    type: Integrations
  - url: https://mailchimp.com/developer/tools/
    type: Resources
  - url: https://mailchimp.com/developer/
    type: Portal
  - url: https://mailchimp.com/developer/release-notes/
    type: ChangeLog
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
          - name: Send the right content at the right time with testing and scheduling features
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
        description: Send the right content at the right time with testing and scheduling features
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
          - name: Sell even more with personalization, optimization tools, and enhanced automations
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
        description: Sell even more with personalization, optimization tools, and enhanced automations
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
          - name: Scale fast with dedicated onboarding, unlimited contacts, and priority support; built for teams
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
        description: Scale fast with dedicated onboarding, unlimited contacts, and priority support; built for teams
    type: Pricing
  - url: https://mailchimp.com/developer/marketing/guides/client-libraries-and-sdks/
    type: SDK
  - url: https://status.mailchimp.com/
    type: StatusPage
  - url: https://mailchimp.com/contact/
    type: Support
  - url: https://mailchimp.com/legal/terms/
    type: TermsOfService
  - url: https://mailchimp.com/legal/privacy/
    type: PrivacyPolicy
  - url: https://mailchimp.com/legal/api_use/
    type: API Use Policy
  - url: https://login.mailchimp.com/signup/
    type: SignUp
  - url: https://github.com/mailchimp
    type: GitHubOrganization
  - url: https://login.mailchimp.com/
    type: Login
  - url: https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
    type: Authentication
  - url: https://stackoverflow.com/questions/tagged/mailchimp
    type: StackOverflow
  - url: https://mailchimp.com/developer/marketing/docs/mobile-sdk/
    type: SDK
created: 2023/11/23
modified: '2026-05-04'
description: Mailchimp is an Intuit company providing a marketing automation platform and email marketing service for managing mailing lists, creating email marketing campaigns, and automating marketing workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
