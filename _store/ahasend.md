---
aid: ahasend
url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/apis.yml
apis:
  - aid: ahasend:ahasend
    name: AhaSend
    tags:
      - Email
      - Transactional Email
      - REST API
      - SMTP
      - Webhooks
    humanURL: https://ahasend.com/docs
    properties:
      - url: https://ahasend.com/docs
        type: Documentation
      - url: https://ahasend.com/docs/api-reference
        type: APIReference
      - url: openapi/ahasend-openapi.yml
        type: OpenAPI
        title: AhaSend Email API v1
      - url: openapi/ahasend-openapi-v2.yaml
        type: OpenAPI
        title: AhaSend API v2
      - url: https://ahasend.com/docs/quickstart
        type: Quickstart
      - url: https://ahasend.com/docs/authentication
        type: Authentication
    description: Send, receive, and track transactional emails with the AhaSend REST API. Supports sending messages, managing domains, webhooks, routes, API keys, suppressions, SMTP credentials, and viewing delivery statistics.
name: AhaSend
tags:
  - Email
  - Transactional Email
  - Developer Tools
  - SMTP
  - Webhooks
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-19'
position: Consumer
description: AhaSend is a developer-focused transactional email platform providing fast, reliable email delivery via REST API and SMTP relay. It offers features including email tracking, webhooks, email routing, suppression management, domain management, SMTP credentials, and detailed delivery statistics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: AhaSend Pricing
    url: https://ahasend.com/pricing
    type: Pricing
    description: Pay-as-you-go email pricing with 1,000 free monthly emails.
  - name: AhaSend Blog
    url: https://ahasend.com/blog
    type: Blog
    description: AhaSend blog with email delivery tips and product updates.
  - name: AhaSend Help Center
    url: https://ahasend.com/help
    type: Support
    description: Help center and support documentation.
  - name: AhaSend Privacy Policy
    url: https://ahasend.com/privacy
    type: PrivacyPolicy
    description: Privacy policy for AhaSend services.
  - name: AhaSend Terms of Service
    url: https://ahasend.com/terms
    type: TermsOfService
    description: Terms and conditions for using AhaSend.
  - name: AhaSend Sign Up
    url: https://dash.ahasend.com/user/register
    type: SignUp
    description: Create a free AhaSend account.
  - name: AhaSend Login
    url: https://dash.ahasend.com/user/login
    type: Login
    description: Log in to the AhaSend dashboard.
  - name: AhaSend GitHub Organization
    url: https://github.com/AhaSend
    type: GitHubOrganization
    description: Official AhaSend GitHub organization with SDKs and CLI tools.
  - name: AhaSend Go SDK
    url: https://github.com/AhaSend/ahasend-go
    type: SDK
    title: Go SDK
    description: Official Go SDK for AhaSend.
  - name: AhaSend CLI
    url: https://github.com/AhaSend/ahasend-cli
    type: CLI
    description: Command-line tool for AhaSend.
  - name: AhaSend WordPress Plugin
    url: https://github.com/AhaSend/wordpress-plugin
    type: Integrations
    description: WordPress plugin for sending emails via AhaSend API.
  - name: AhaSend Java Client
    url: https://github.com/AhaSend/ahasend-java-client
    type: SDK
    title: Java SDK
    description: Java client for AhaSend APIs generated using Swagger Codegen.
  - name: AhaSend Affiliate Program
    url: https://ahasend.com/affiliates
    type: Affiliate
    description: Earn commissions by referring new users to AhaSend.
  - type: Features
    data:
      - name: Transactional Email Delivery
        description: Fast delivery of transactional emails including OTPs and confirmations, targeting sub-2-second delivery to Gmail at 99th percentile.
      - name: Email Tracking
        description: Track email opens and link clicks with real-time analytics.
      - name: Webhook Notifications
        description: Real-time webhook events for delivery, bounces, opens, clicks, and account alerts.
      - name: Email Routing
        description: Route incoming emails to HTTP endpoints with automatic parsing of signatures and quoted replies.
      - name: Suppression Management
        description: Automated handling of bounces, complaints, and unsubscribes with suppression lists.
      - name: Domain Management
        description: Manage sending domains including DNS validation, DKIM rotation, and whitelabeling.
      - name: SMTP Relay
        description: Compatible SMTP relay supporting any programming language or software.
      - name: Dedicated IPs
        description: Free dedicated IPs for high-volume senders exceeding 300k emails per month.
      - name: S3-Compatible Archiving
        description: Archive emails to S3-compatible storage with configurable retention policies.
      - name: SSO with OIDC
        description: Enterprise single sign-on via OpenID Connect with granular API credential scoping.
  - type: UseCases
    data:
      - name: Password Reset Emails
        description: Send secure one-time password and password reset links with guaranteed fast delivery.
      - name: Email Verification
        description: Deliver account verification emails for new user signups.
      - name: Order Confirmation Emails
        description: Transactional order and shipping confirmation emails for e-commerce.
      - name: System Alerts
        description: Programmatic email alerts and notifications from applications and infrastructure.
      - name: Inbound Email Processing
        description: Route and process incoming emails in applications using email routing.
  - type: Integrations
    data:
      - name: Node.js
        description: Native Node.js integration with code examples and SDK support.
      - name: Python
        description: Python integration examples for sending emails via API or SMTP.
      - name: PHP / Symfony
        description: PHP integration including Symfony Mailer transport support.
      - name: Ruby on Rails
        description: Ruby integration with Rails ActionMailer transport.
      - name: Go
        description: Official Go SDK for the AhaSend API.
      - name: WordPress
        description: WordPress plugin for routing site emails through AhaSend.
      - name: Java
        description: Java client generated from OpenAPI spec.
  - name: AhaSend Spectral Rules
    url: rules/ahasend-spectral-rules.yml
    type: SpectralRules
    description: Spectral ruleset enforcing AhaSend API conventions.
  - name: AhaSend Email Operations Capability
    url: capabilities/email-operations.yaml
    type: NaftikoCapability
    description: Naftiko workflow capability for email operations.
  - name: AhaSend Vocabulary
    url: vocabulary/ahasend-vocabulary.yaml
    type: Vocabulary
    description: Taxonomy vocabulary for AhaSend APIs.
---
