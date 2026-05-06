---
aid: buttondown
name: Buttondown
description: Buttondown is an independent email newsletter platform for creators and businesses, offering a markdown editor, automations, paid subscriptions, analytics, team collaboration, and a feature-complete REST API for programmatic management of subscribers, emails, newsletters, and related resources.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Automations
  - Email
  - Markdown
  - Newsletters
  - Paid Subscriptions
  - SaaS
  - Subscribers
url: https://raw.githubusercontent.com/api-evangelist/buttondown/refs/heads/main/apis.yml
created: '2026-04-23'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: buttondown:buttondown-api
    name: Buttondown API
    description: The Buttondown API is a RESTful HTTP API that enables programmatic management of newsletters, subscribers, emails, drafts, tags, automations, surveys, and webhooks. Authentication is via API keys issued in the Buttondown dashboard, and the API powers both first-party and third-party tooling on the platform.
    humanURL: https://docs.buttondown.com/api
    baseURL: https://api.buttondown.email/v1
    tags:
      - Email
      - Newsletters
      - REST
      - Subscribers
    properties:
      - type: Documentation
        url: https://docs.buttondown.com/api
      - type: Developer Portal
        url: https://docs.buttondown.com/
      - type: API Keys
        url: https://buttondown.com/requests
      - type: Changelog
        url: https://docs.buttondown.com/changelog
      - type: Status
        url: https://buttondown.statuspage.io/
    x-features:
      - Subscriber management (create, update, list, delete)
      - Email sending and scheduling
      - Draft creation and revision
      - Tag and segmentation management
      - Automations and drip sequences
      - Webhooks for event delivery
      - Survey and poll endpoints
      - Paid subscription support
    x-use-cases:
      - Syncing subscribers from an external CRM or identity system
      - Automated email publishing pipelines
      - Custom signup and preference pages
      - Analytics and reporting integrations
      - Event-driven automations via webhooks
  - aid: buttondown:newsletter-platform
    name: Buttondown Newsletter Platform
    description: The Buttondown hosted newsletter platform provides a markdown-based composition experience, subscriber management, delivery infrastructure, analytics, monetization via paid subscriptions, team collaboration, and integrations with Discord, Memberful, YouTube, and RSS.
    humanURL: https://buttondown.com/
    tags:
      - Analytics
      - Email
      - Markdown
      - Newsletters
      - SaaS
    properties:
      - type: Website
        url: https://buttondown.com/
      - type: Features
        url: https://buttondown.com/features
      - type: Integrations
        url: https://buttondown.com/features/integrations
      - type: Pricing
        url: https://buttondown.com/pricing
    x-features:
      - Markdown editor with personalization
      - Paid subscriptions without platform fees
      - Analytics dashboard
      - Automations and scheduling
      - Team collaboration without per-seat pricing
      - Concierge migration service
      - High deliverability and spam protection
    x-use-cases:
      - Independent creator newsletters
      - Paid subscription newsletters
      - Company and product newsletters
      - Migration from other newsletter platforms
common:
  - type: Website
    url: https://buttondown.com/
  - type: Documentation
    url: https://docs.buttondown.com/
  - type: Pricing
    url: https://buttondown.com/pricing
  - type: Blog
    url: https://buttondown.com/blog
  - type: Status
    url: https://buttondown.statuspage.io/
  - type: Changelog
    url: https://docs.buttondown.com/changelog
  - type: Support
    url: mailto:support@buttondown.email
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
