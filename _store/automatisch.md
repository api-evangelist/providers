---
aid: automatisch
name: Automatisch
description: Automatisch is an open source business automation tool and self-hosted alternative to Zapier that connects different services to automate workflows without programming knowledge. Built with JavaScript/Node.js, it supports 100+ integrations including Slack, GitHub, Gmail, PostgreSQL, and AI services. Licensed under AGPL-3.0 for the community edition, with an enterprise edition for commercial deployments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Workflow Automation
  - Self-Hosted
  - Open Source
  - Zapier Alternative
  - No-Code
  - JavaScript
  - Node.js
  - AGPL
url: https://raw.githubusercontent.com/api-evangelist/automatisch/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: automatisch:automatisch-rest-api
    name: Automatisch REST API
    description: Automatisch exposes a REST API used by its web application for managing flows (automated workflows), connections (service credentials), users, and integrations. The API supports webhook trigger endpoints for receiving events from external services and provides the backend for the Automatisch UI. The API follows standard REST conventions with JSON request and response bodies.
    humanURL: https://github.com/automatisch/automatisch
    tags:
      - Workflow Automation
      - Flows
      - Connections
      - Webhooks
      - REST
    properties:
      - type: Documentation
        url: https://automatisch.io/docs
      - type: GettingStarted
        url: https://automatisch.io/docs/installation/docker
      - type: GitHubRepository
        url: https://github.com/automatisch/automatisch
common:
  - type: Website
    url: https://automatisch.io
  - type: Documentation
    url: https://automatisch.io/docs
  - type: GitHubOrganization
    url: https://github.com/automatisch
  - type: GitHubRepository
    url: https://github.com/automatisch/automatisch
  - type: GettingStarted
    url: https://automatisch.io/docs/installation/docker
  - type: ReleaseNotes
    url: https://github.com/automatisch/automatisch/releases
  - type: Features
    data:
      - name: 100+ Built-In Integrations
        description: Automatisch ships with over 100 pre-built connectors for popular services including Slack, Discord, GitHub, GitLab, Gmail, Google Sheets, Airtable, Notion, Trello, OpenAI, Anthropic, PostgreSQL, and many more.
      - name: Self-Hosted Deployment
        description: Deploy Automatisch on your own infrastructure using Docker Compose, keeping all workflow data and credentials under your control with no data sent to third-party cloud services.
      - name: Webhook Triggers
        description: Built-in webhook trigger support allows external services to trigger Automatisch flows via HTTP POST, enabling event-driven automation from any service that supports outbound webhooks.
      - name: No-Code Workflow Builder
        description: A visual drag-and-drop interface for building multi-step automation workflows connecting triggers from one service to actions in another without writing code.
      - name: AGPL-3.0 Open Source
        description: The community edition is licensed under AGPL-3.0, allowing free use, modification, and distribution. An enterprise edition with additional features is available for commercial deployments.
      - name: Custom App Development
        description: Extend Automatisch by developing custom app integrations using the JavaScript SDK. Custom apps follow the same trigger/action pattern as built-in integrations.
  - type: UseCases
    data:
      - name: Business Process Automation
        description: Automate repetitive business processes such as lead routing, support ticket triage, and data synchronization between SaaS tools without relying on cloud automation vendors.
      - name: Data Privacy Compliance
        description: Self-host workflow automation to keep sensitive business data on-premises or in private cloud infrastructure, meeting GDPR and data residency requirements.
      - name: Developer Workflow Automation
        description: Automate developer workflows including GitHub issue-to-Slack notifications, CI/CD status updates, and pull request review reminders.
      - name: CRM and Marketing Automation
        description: Connect CRM tools with marketing platforms to automate lead nurturing, email sequences, and customer data synchronization across tools.
  - type: Integrations
    data:
      - name: Slack
        description: Send messages, create channels, and respond to Slack events in automated flows.
      - name: GitHub
        description: Trigger flows from GitHub events and create issues, PRs, and comments programmatically.
      - name: Gmail
        description: Send emails and trigger flows from incoming Gmail messages.
      - name: Google Sheets
        description: Read and write rows in Google Sheets as steps in automated workflows.
      - name: OpenAI
        description: Call OpenAI APIs (GPT, DALL-E, Whisper) as steps within Automatisch automation flows.
      - name: PostgreSQL
        description: Query and write to PostgreSQL databases as steps in automation flows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
