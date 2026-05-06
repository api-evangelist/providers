---
aid: postmark
name: Postmark
description: Postmark is an email delivery service that helps businesses send and track transactional and broadcast email reliably, replacing SMTP with a scalable service that surfaces detailed delivery analytics, bounce tracking, open and click tracking, and dedicated IP addresses.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/postmark/refs/heads/main/apis.yml
tags:
  - Emails
  - Messaging
  - Transactional Email
  - Deliverability
  - SMTP
created: '2024-04-14'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: postmark:postmark-api
    name: Postmark API
    description: The Postmark API provides programmatic access to send and track transactional and broadcast emails, manage servers, templates, message streams, bounces, suppressions, statistics, webhooks, and inbound message processing.
    humanURL: https://postmarkapp.com/developer
    baseURL: https://api.postmarkapp.com
    tags:
      - Email
      - Messages
      - Templates
      - Servers
      - Bounces
      - Statistics
      - Webhooks
      - Inbound
      - Outbound
    properties:
      - type: Documentation
        url: https://postmarkapp.com/developer
      - type: GettingStarted
        url: https://postmarkapp.com/developer/api/overview
      - type: Authentication
        url: https://postmarkapp.com/developer/api/overview#authentication
      - type: OpenAPI
        url: openapi/postmark-api-openapi.yml
    contact:
      - FN: Postmark Support
        url: https://postmarkapp.com/support
common:
  - type: Website
    url: https://postmarkapp.com
  - type: Documentation
    url: https://postmarkapp.com/developer
  - type: GettingStarted
    url: https://postmarkapp.com/developer/api/overview
  - type: Pricing
    url: https://postmarkapp.com/pricing
  - type: SignUp
    url: https://account.postmarkapp.com/sign_up
  - type: Login
    url: https://account.postmarkapp.com/login
  - type: Blog
    url: https://postmarkapp.com/blog
  - type: Support
    url: https://postmarkapp.com/support
  - type: Status
    url: https://status.postmarkapp.com
  - type: Templates
    url: https://postmarkapp.com/transactional-email-templates
  - type: ChangeLog
    url: https://postmarkapp.com/changelog
  - type: TermsOfService
    url: https://postmarkapp.com/terms-of-service
  - type: PrivacyPolicy
    url: https://wildbit.com/privacy
  - type: GitHub
    url: https://github.com/ActiveCampaign
  - type: Twitter
    url: https://twitter.com/postmarkapp
  - type: LinkedIn
    url: https://www.linkedin.com/company/postmarkapp
  - type: Features
    data:
      - 'Free: 100 emails/month'
      - 'Basic: $15/mo for 10K emails'
      - 'Pro: $16.50/mo for 10K emails with templates and webhooks'
      - 'Platform: $18/mo for 10K emails with multiple servers and dedicated IPs'
      - Email API and SMTP server
      - Templates with versioning (Pro+)
      - Webhooks for delivery, bounce, open, click, spam, subscription events
      - Bounce and spam complaint handling
      - Server tokens for per-environment isolation
      - Send up to 500 emails per batch request
      - Inbound email parsing
      - Message Streams (broadcast vs transactional)
      - OpenTracker beacon for opens/clicks
      - Suppression management
      - Dedicated IPs (Platform)
      - Best-in-class deliverability
    sources:
      - https://postmarkapp.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
