---
aid: wildapricot
name: WildApricot
description: WildApricot is a cloud-based membership management software platform designed for associations, nonprofits, and clubs. It provides tools for managing members, events, email communications, online payments, and websites. The WildApricot Admin API provides programmatic access to all platform features including contacts, events, event registrations, membership levels, invoices, payments, donations, email campaigns, and store orders via a REST API secured with OAuth2.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Membership Management
  - Associations
  - Nonprofit
  - Events
  - Payments
created: '2025-02-17'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wildapricot/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wildapricot:wildapricot-admin-api
    name: WildApricot Admin API
    description: The WildApricot Admin API provides programmatic access to membership management features including contacts, events, event registrations, membership levels, invoices, payments, donations, email campaigns, and store orders. Secured with OAuth2 client credentials or authorization code flow.
    humanURL: https://app.wildapricot.com/interfaces/api
    baseURL: https://api.wildapricot.org/v2.2
    tags:
      - Membership Management
      - Associations
      - Nonprofit
      - Contacts
      - Events
      - Payments
    properties:
      - type: Documentation
        url: https://app.wildapricot.com/interfaces/api
      - type: APIReference
        url: https://app.swaggerhub.com/apis/WildApricot/wild-apricot_public_api/7.24.0
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wildapricot/refs/heads/main/openapi/wildapricot-admin-api-openapi.yml
      - type: Authentication
        url: https://gethelp.wildapricot.com/en/articles/484
      - type: SDK
        url: https://github.com/WildApricot/ApiSamples
        title: API Samples (.NET)
      - type: SDK
        url: https://github.com/douglasdeodato/wildapricot-python-api
        title: Python SDK (Community)
common:
  - type: Website
    url: https://www.wildapricot.com/
  - type: Portal
    url: https://app.wildapricot.com/interfaces/api
  - type: Documentation
    url: https://gethelp.wildapricot.com/en/articles/182
  - type: GettingStarted
    url: https://gethelp.wildapricot.com/en/articles/484
  - type: Authentication
    url: https://gethelp.wildapricot.com/en/articles/484
  - type: RateLimits
    url: https://gethelp.wildapricot.com/en/articles/182
  - type: Pricing
    url: https://www.wildapricot.com/pricing
  - type: TermsOfService
    url: https://www.wildapricot.com/terms-of-use
  - type: PrivacyPolicy
    url: https://www.wildapricot.com/privacy-policy
  - type: Support
    url: https://gethelp.wildapricot.com/
  - type: Blog
    url: https://www.wildapricot.com/blog
  - type: GitHubOrganization
    url: https://github.com/WildApricot
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/wildapricot/refs/heads/main/rules/wildapricot-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/wildapricot/refs/heads/main/vocabulary/wildapricot-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/wildapricot/refs/heads/main/capabilities/membership-management.yaml
  - type: Features
    data:
      - name: Contact Management
        description: Comprehensive member and contact database with custom fields, saved searches, and OData filtering.
      - name: Event Management
        description: Full event lifecycle management including registration types, waitlists, check-in, and capacity management.
      - name: Membership Levels
        description: Configurable membership tiers with pricing, renewal periods, access restrictions, and bundle support.
      - name: Online Payments
        description: Integrated payment processing for membership fees, event registrations, donations, and store orders.
      - name: Email Campaigns
        description: Built-in email campaign tool with draft management, recipient targeting, scheduling, and delivery tracking.
      - name: Donation Management
        description: Track and manage charitable donations with custom fields and donor contact linking.
      - name: Member Portal
        description: Self-service member portal for profile management, event registration, and membership renewals.
      - name: Store
        description: Simple online store for merchandise and product sales with order management.
  - type: UseCases
    data:
      - name: Member Onboarding Automation
        description: Automate new member welcome workflows by monitoring contact creation events and sending personalized onboarding sequences.
      - name: Event Registration Sync
        description: Sync WildApricot event registrations to CRM or marketing platforms for post-event follow-up campaigns.
      - name: Membership Renewal Reminders
        description: Query lapsed and soon-to-expire members to trigger renewal reminder emails or SMS notifications.
      - name: Financial Reporting
        description: Extract invoice, payment, and donation data to build financial dashboards and audit reports.
      - name: Badge and Check-In Systems
        description: Use the event check-in API to power custom badge printing or door access control at events.
      - name: Directory Integrations
        description: Push member data to external directories, websites, or LDAP systems using the contacts API.
  - type: Integrations
    data:
      - name: QuickBooks
        description: WildApricot has a native QuickBooks integration for financial data sync and accounting workflows.
      - name: Zapier
        description: WildApricot integrates with Zapier enabling no-code workflows connecting to 5000+ apps.
      - name: Stripe
        description: Payments can be processed through Stripe as a payment gateway for online transactions.
      - name: PayPal
        description: WildApricot supports PayPal as a payment gateway for member and event payments.
      - name: WordPress
        description: WildApricot offers a WordPress integration for embedding member login and event lists.
      - name: Mailchimp
        description: Member contact lists can be synced to Mailchimp for external email marketing campaigns.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
