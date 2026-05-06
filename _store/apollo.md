---
aid: apollo
name: Apollo
description: Apollo.io is an AI-powered B2B sales intelligence and engagement platform combining a database of 230M+ verified contacts and 30M+ companies with prospecting, outreach, and deal execution tools. The platform helps sales teams build pipeline, qualify inbound leads, enrich data, and close deals faster with AI-powered workflows and conversation intelligence.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - B2B Sales
  - CRM
  - Data Enrichment
  - Lead Generation
  - Sales Intelligence
  - Sales Platform
url: https://raw.githubusercontent.com/api-evangelist/apollo/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apollo:apollo-rest-api
    name: Apollo REST API
    description: Apollo.io's REST API provides programmatic access to Apollo's B2B data platform with 230M+ verified contacts and 30M+ companies. The API supports people enrichment, organization enrichment, people search, organization search, accounts and contacts management, deals, sequences, tasks, analytics reporting, and calls management. Authentication via API keys (direct access) or OAuth 2.0 (partner integrations).
    humanURL: https://www.apollo.io/
    tags:
      - Analytics
      - CRM
      - Data Enrichment
      - Organization Search
      - People Search
      - REST
      - Sales Intelligence
      - Sequences
    properties:
      - type: Documentation
        url: https://docs.apollo.io/
      - type: GettingStarted
        url: https://docs.apollo.io/docs
      - type: APIReference
        url: https://docs.apollo.io/reference
      - type: Authentication
        url: https://docs.apollo.io/reference/authentication
      - type: RateLimits
        url: https://docs.apollo.io/reference/rate-limits
      - type: Tutorials
        url: https://docs.apollo.io/docs/overview-apollo-api-tutorials
  - aid: apollo:apollo-client
    name: Apollo Client
    description: Apollo Client provides libraries and integrations for connecting to Apollo.io's sales platform from external applications and CRM systems.
    humanURL: https://www.apollo.io/integrations
    tags:
      - CRM
      - Integrations
      - Salesforce
      - SDKs
    properties:
      - type: Documentation
        url: https://www.apollo.io/integrations
common:
  - type: Documentation
    url: https://docs.apollo.io/
  - type: GettingStarted
    url: https://docs.apollo.io/docs
  - type: Pricing
    url: https://www.apollo.io/pricing
  - type: Blog
    url: https://www.apollo.io/blog
  - type: Support
    url: https://www.apollo.io/support
  - type: Training
    url: https://academy.apollo.io/
  - type: PrivacyPolicy
    url: https://www.apollo.io/privacy-policy
  - type: TermsOfService
    url: https://www.apollo.io/terms-of-service
  - type: Compliance
    url: https://www.apollo.io/security
  - type: Features
    data:
      - name: Outbound Prospecting
        description: AI-powered multichannel outbound campaigns with email deliverability guardrails and workflow automations.
      - name: Inbound Lead Qualification
        description: Anonymous visitor identification, real-time form enrichment, instant routing, and automated follow-ups.
      - name: Data Enrichment
        description: Enrich contact and company records with always-fresh data from 230M+ verified contacts and 30M+ companies.
      - name: Deal Execution
        description: Pre-meeting insights, AI call summaries, pipeline boards, and coaching dashboards.
      - name: AI Assistant
        description: AI-powered assistant for automating sales research, writing, and workflow tasks.
      - name: Conversation Intelligence
        description: Call recording, AI call summaries, and conversation analytics for sales coaching.
      - name: Chrome Extension
        description: Browser extension for accessing Apollo data and workflows directly from any website.
      - name: Workflow Automation
        description: No-code workflow automation engine for sales process automation.
      - name: Email Deliverability
        description: Email deliverability guardrails to protect sender reputation and maximize inbox placement.
      - name: Meeting Scheduler
        description: Integrated meeting scheduling functionality linked to sales workflows.
  - type: UseCases
    data:
      - name: Outbound Sales Prospecting
        description: Find and engage ideal prospects at scale using Apollo's contact database and multichannel outreach.
      - name: Inbound Lead Management
        description: Automatically qualify, route, and follow up on inbound leads in real time.
      - name: CRM Data Enrichment
        description: Enrich Salesforce, HubSpot, and other CRM records with verified contact and company data.
      - name: Sales Pipeline Building
        description: Build and manage sales pipeline with AI-assisted prospecting and deal execution tools.
      - name: Partner API Integration
        description: Build third-party integrations using OAuth 2.0 to access Apollo data on behalf of customers.
  - type: Integrations
    data:
      - name: Salesforce
        description: Bi-directional Salesforce CRM integration syncing contacts, accounts, activities, and sequences.
      - name: HubSpot
        description: HubSpot CRM integration for syncing contact data and outreach activity.
      - name: Gmail
        description: Gmail integration for email tracking and outreach directly from inbox.
      - name: Outlook
        description: Microsoft Outlook integration for email tracking and outreach.
      - name: LinkedIn
        description: LinkedIn integration via Chrome extension for prospecting and data enrichment.
      - name: Zapier
        description: Zapier integration for connecting Apollo to hundreds of other applications.
      - name: Slack
        description: Slack integration for deal alerts and notifications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
