---
aid: slack
url: >-
  https://raw.githubusercontent.com/api-search/messaging/main/_apis/slack/apis.md
apis:
  - aid: slack:slack-web-api
    name: Slack Web API
    tags:
      - Messaging
      - Chat
      - Bots
      - Productivity
    contact:
      - FN: Support
        url: https://api.slack.com/support
    humanURL: https://api.slack.com/web
    properties:
      - url: https://api.slack.com/web
        type: Documentation
      - url: openapi/slack-web-openapi-original.yml
        type: OpenAPI
    description: >-
      The Slack Web API is an interface for querying information from and
      enacting change in a Slack workspace. Use it for individual queries, or as
      part of a more complex tapestry of platform features in a Slack app.
name: Slack
tags:
  - Messaging
  - Chat
  - Bots
  - Productivity
  - T1
type: Contract
access: 3rd-Party
common:
  - url: https://slack-status.com/
    name: Status
    type: Status
  - url: https://api.slack.com/
    name: Unlock your productivity potential with Slack Platform | Slack
    type: Portal
    description: 'null'
  - url: https://api.slack.com/automation/quickstart
    name: Quickstart guide for developing automations | Slack
    type: GettingStarted
    description: 'null'
  - url: https://api.slack.com/samples
    name: Samples and templates | Slack
    type: Templates
    description: 'null'
  - url: https://api.slack.com/docs/developer-sandbox
    name: Developer sandboxes | Slack
    type: Sandbox
    description: 'null'
  - url: https://api.slack.com/authentication
    name: Authentication | Slack
    type: Authentication
    description: 'null'
  - url: https://api.slack.com/tutorials
    name: Guided tutorials | Slack
    type: Tutorials
    description: 'null'
  - url: https://api.slack.com/developer-policy
    name: Slack App Developer Policy | Slack
    type: TermsOfService
    description: 'null'
  - url: >-
      https://slack.com/intl/en-gb/terms-of-service/api-updated?_gl=1*1yvqubm*_gcl_au*ODQ0OTgxOTg3LjE3MzU5NDg2ODY.*_ga*MTk4NzA1NTA3Ny4xNzM1OTQ4Njg3*_ga_QTJQME5M5D*MTczNTk0ODY4NS4xLjEuMTczNTk0ODk4My41LjAuMA..
    name: Slack API Terms of Service | Legal | Slack
    type: TermsOfService
    description: 'null'
  - url: https://slack.com/intl/en-gb/blog
    name: Slack blog | Slack
    type: Blog
    description: 'null'
  - url: https://slack.com/pricing
    data:
      url: https://slack.com/pricing
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
              description: Usage based pricing.
          elements:
            - name: 90 days of message history
            - name: Up to 10 apps
            - name: 1:1 meetings
            - name: 1:1 external messages
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: 10 Integrations with other apps
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: 1 Year Data retention policies
            - name: 1 Workspaces
            - name: Manage channel posting permissions
          description: A simpler way to chat and collaborate.
        - id: pro
          name: Pro
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: $4.38
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: Unlimited message history
            - name: Unlimited app integrations
            - name: Group meetings
            - name: Group external messages
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: Lists
            - name: Customizable sections
            - name: Templates
            - name: Thread and channel summaries
            - name: Huddles notes
            - name: AI assistant apps
            - name: Integrations with other apps
            - name: Workflow Builder
            - name: Custom workflow steps
            - name: Deploy apps to Slack infrastructure
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: Access logs
            - name: Single sign-on (SSO)
            - name: OAuth with Google
            - name: Data retention policies
            - name: 1 Workspace
            - name: Manage channel posting permissions
            - name: Admin analytics dashboards
            - name: 24/7 Customer support
          description: Drive productivity in one place.
        - id: business
          name: Business
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: $9.00
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: Unlimited message history
            - name: Unlimited app integrations
            - name: Group meetings
            - name: Group external messages
            - name: AI conversation summaries
            - name: AI workflow generation
            - name: AI search
            - name: AI daily recaps
            - name: AI file summaries
            - name: SAML-based single sign-on
            - name: SCIM user management
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: Lists
            - name: Customizable sections
            - name: Templates
            - name: Slack Atlas
            - name: Thread and channel summaries
            - name: Huddles notes
            - name: AI assistant apps
            - name: Daily recaps
            - name: File summaries
            - name: AI language translations
            - name: AI workflow generation
            - name: AI steps in Workflow Builder
            - name: AI search
            - name: Integrations with other apps
            - name: Workflow Builder
            - name: Custom workflow steps
            - name: Deploy apps to Slack infrastructure
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: Access logs
            - name: Single sign-on (SSO)
            - name: OAuth with Google
            - name: SAML-based
            - name: Supports Multi-SAML
            - name: Data retention policies
            - name: Data residency
            - name: Workspaces
            - name: Manage channel posting permissions
            - name: Admin analytics dashboards
            - name: SCIM user management
            - name: Supports guests
            - name: Admin analytics API
            - name: Message activity analytics
            - name: Custom user groups
            - name: Manually manage
          description: Scale with AI-powered work.
        - id: enterprise
          name: Enterprise
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: Contact Sales
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: Unlimited message history
            - name: Unlimited app integrations
            - name: Group meetings
            - name: Group external messages
            - name: AI conversation summaries
            - name: AI workflow generation
            - name: AI search
            - name: AI daily recaps
            - name: AI file summaries
            - name: SAML-based single sign-on
            - name: SCIM user management
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: Lists
            - name: Customizable sections
            - name: Templates
            - name: Slack Atlas
            - name: Thread and channel summaries
            - name: Huddles notes
            - name: AI assistant apps
            - name: Daily recaps
            - name: File summaries
            - name: AI language translations
            - name: AI workflow generation
            - name: AI steps in Workflow Builder
            - name: AI search
            - name: Enterprise search
            - name: Integrations with other apps
            - name: Workflow Builder
            - name: Custom workflow steps
            - name: Deploy apps to Slack infrastructure
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: Access logs
            - name: Single sign-on (SSO)
            - name: OAuth with Google
            - name: SAML-based
            - name: Supports Multi-SAML
            - name: Slack Enterprise Key Management
            - name: Add-on
            - name: Integration with Enterprise Mobility Management
            - name: Anomaly Event Response
            - name: Data retention policies
            - name: Data residency
            - name: Data exports for all messages
            - name: Data exports for all messages from a single user
            - name: Native data loss prevention
            - name: Information barriers
            - name: Legal holds
            - name: Discovery API
            - name: Audit logs
            - name: Support for HIPAA compliance
            - name: Workspaces
            - name: Manage channel posting permissions
            - name: Admin analytics dashboards
            - name: SCIM user management
            - name: Supports guests
            - name: Admin analytics API
            - name: Message activity analytics
            - name: Custom user groups
            - name: "Manually manage\tSync via identity provider"
            - name: Domain claiming
            - name: Custom terms of service
            - name: Granular roles
            - name: Manage flagged content
            - name: Access to customer support
          description: Scale with AI-powered work.
      name: Plans
      type: Plans
    name: Plans
    type: Plans
created: 2024/04/14
modified: '2025-09-05'
position: Consuming
description: >-
  Slack is a cloud-based freemium cross-platform instant messaging service
  created by Slack Technologies and currently owned by Salesforce. While
  initially developed for professional and organizational communications, it has
  also been adopted as a community platform.
maintainers:
  - FN: API Evangelist
    url: https://apievangelisgt.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---