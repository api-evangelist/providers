---
aid: cflow
url: https://raw.githubusercontent.com/api-evangelist/cflow/refs/heads/main/apis.yml
name: Cflow
x-type: company
tags:
  - Automations
  - Business Process Automation
  - Integrations
  - No-Code
  - Platform
  - Protocols
  - Rules
  - Workflows
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-23'
position: Consumer
description: Cflow is a cloud-based workflow automation platform that helps organizations streamline and optimize business processes. It offers a drag-and-drop workflow builder, customizable forms, rule-based routing, approval flows, integrations with popular business applications, and real-time analytics. Cflow exposes a REST API allowing developers to list workflows, submit and manage requests, approve or reject tasks, and manage users and roles programmatically.
apis:
  - aid: cflow:cflow
    name: Cflow Workflow API
    tags:
      - Approvals
      - Automation
      - Integrations
      - Protocols
      - Requests
      - Roles
      - Rules
      - Users
      - Workflows
    humanURL: https://www.cflowapps.com
    baseURL: https://us.cflowapps.com
    properties:
      - url: https://www.cflowapps.com/workflow/workflow-api/
        type: Documentation
      - url: openapi/cflow-openapi.yml
        type: OpenAPI
      - url: json-schema/workflow.json
        type: JSONSchema
      - url: json-schema/stage.json
        type: JSONSchema
      - url: json-schema/request.json
        type: JSONSchema
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/role.json
        type: JSONSchema
      - url: json-ld/cflow-context.jsonld
        type: JSONLD
    description: The Cflow Workflow API provides REST endpoints for retrieving workflows, creating and managing requests, approving or rejecting requests at each stage, creating draft requests, and administering users and roles. All business objects and integration objects are exposed as JSON resources and authentication is handled via API key, user key, and username headers.
common:
  - type: Website
    url: https://www.cflowapps.com
  - type: Documentation
    url: https://www.cflowapps.com/workflow/workflow-api/
  - type: SignUp
    url: https://www.cflowapps.com/sign-up/
  - type: Pricing
    url: https://www.cflowapps.com/pricing/
  - type: Blog
    url: https://www.cflowapps.com/blog/
  - type: Support
    url: https://help.cflowapps.com/
  - type: TermsOfService
    url: https://www.cflowapps.com/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.cflowapps.com/privacy-policy/
  - name: Features
    type: Features
    data:
      - name: Drag-and-Drop Workflow Builder
      - name: Custom Forms
      - name: Conditional Rules
      - name: Multi-Level Approvals
      - name: Role-Based Access Control
      - name: Real-Time Analytics
      - name: Dashboards
      - name: Email Notifications
      - name: Mobile Access
      - name: Audit Trails
      - name: REST API
      - name: Webhooks
      - name: Integrations
      - name: No-Code
      - name: Low-Code
      - name: Parallel Approvals
      - name: Sequential Approvals
      - name: Escalations
      - name: Reminders
      - name: Reports
  - name: UseCases
    type: UseCases
    data:
      - name: Purchase Request Approval
      - name: Employee Onboarding
      - name: Leave Requests
      - name: Expense Approval
      - name: Travel Requests
      - name: Vendor Onboarding
      - name: Invoice Approval
      - name: Capital Expenditure Requests
      - name: Document Approval
      - name: Change Management
      - name: Compliance Workflows
      - name: Help Desk Ticketing
  - name: Integrations
    type: Integrations
    data:
      - name: Zapier
      - name: Microsoft Teams
      - name: Slack
      - name: Google Workspace
      - name: Office 365
      - name: Dropbox
      - name: OneDrive
      - name: SharePoint
      - name: DocuSign
      - name: Salesforce
      - name: QuickBooks
      - name: Webhooks
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
