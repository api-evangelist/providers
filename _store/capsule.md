---
aid: capsule
url: https://raw.githubusercontent.com/api-evangelist/capsule/refs/heads/main/apis.yml
name: Capsule
description: Capsule is a CRM and project-management platform for small and mid-sized businesses that unifies contacts, sales pipelines, tasks, cases, and projects. The Capsule REST API exposes parties (contacts and companies), opportunities, projects, tasks, cases, entries, tracks, and settings such as tags, pipelines, milestones, stages, and custom fields, with REST Hooks webhooks for event-driven integration.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Contact Management
  - CRM
  - Custom Fields
  - Opportunities
  - Pipelines
  - Project Management
  - REST
  - Sales
  - Tasks
  - Webhooks
created: '2025-01-01'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: capsule:capsule-rest-api
    name: Capsule REST API
    description: The Capsule REST API provides CRUD access to Capsule CRM resources including parties (contacts and companies), opportunities, projects, tasks, cases, entries (activity log), and tracks. Settings resources let integrators manage tags, custom fields, pipelines, milestones, boards, stages, and activity types. REST Hooks webhooks notify subscribers of changes and avoid polling.
    humanURL: https://developer.capsulecrm.com/
    tags:
      - Contact Management
      - CRM
      - REST
      - Sales
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.capsulecrm.com/
      - type: Authentication
        url: https://developer.capsulecrm.com/v2/overview/authentication
      - type: Webhooks
        url: https://developer.capsulecrm.com/v2/resources/rest-hooks
      - type: OpenAPI
        url: https://developer.capsulecrm.com/
    x-features:
      - Parties (contacts and companies) with list, search, CRUD
      - Opportunities with pipeline, milestone, and value tracking
      - Projects with assigned parties and status tracking
      - Tasks and activities with assignees and due dates
      - Cases for issue and support-style tracking
      - Entries for activity notes and file attachments
      - Tracks for repeatable activity sequences
      - Configurable tags, custom fields, and activity types
      - Pipelines, milestones, stages, and board configuration
      - REST Hooks webhooks for subscribe/unsubscribe event delivery
      - Team and user management
      - OAuth 2.0 authentication
    x-use-cases:
      - Syncing contacts between Capsule and marketing tools
      - Pushing new leads into the sales pipeline from web forms
      - Automating follow-up tasks based on opportunity milestones
      - Event-driven integration with accounting or support systems
      - Reporting and analytics on pipeline, projects, and activities
      - Embedding Capsule data in custom internal dashboards
common:
  - type: Website
    url: https://capsulecrm.com
  - type: Documentation
    url: https://developer.capsulecrm.com/
  - type: Pricing
    url: https://capsulecrm.com/pricing
  - type: Support
    url: https://capsulecrm.com/support
  - type: Blog
    url: https://capsulecrm.com/blog
  - type: Privacy Policy
    url: https://capsulecrm.com/privacy-policy
  - type: Terms of Service
    url: https://capsulecrm.com/terms-of-service
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
