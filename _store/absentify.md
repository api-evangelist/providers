---
aid: absentify
url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/apis.yml
name: Absentify
description: Absentify is an absence management platform integrated with Microsoft 365 and Microsoft Teams that helps businesses track and manage employee absences, leave requests, approvals, and team schedules. Built by BrainCore Solutions GmbH, it provides a REST API for integrating absence management into custom workflows, HR systems, and business automation tools.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Absence Management
  - HR
  - Leave Management
  - Microsoft Teams
  - Human Resources
type: Contract
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: absentify:absentify
    name: Absentify API
    description: REST API for managing employee absences, leave requests, members, departments, leave types, public holidays, and workspace settings. Requires an API key (x-api-key header) available on the Plus plan. Rate limit of 150 requests per second per IP address.
    humanURL: https://absentify.com/docs/en/api-reference/introduction
    baseURL: https://api.absentify.com/api/v1
    tags:
      - Absence Management
      - Leave Requests
      - Members
      - Departments
      - Leave Types
    properties:
      - type: Documentation
        url: https://absentify.com/docs/en/api-reference/introduction
      - type: OpenAPI
        url: openapi/absentify-openapi.yml
      - type: JSONSchema
        url: json-schema/absentify-member-schema.json
        title: Member Schema
      - type: JSONSchema
        url: json-schema/absentify-department-schema.json
        title: Department Schema
      - type: JSONSchema
        url: json-schema/absentify-leave-type-schema.json
        title: Leave Type Schema
      - type: JSONSchema
        url: json-schema/absentify-request-schema.json
        title: Request Schema
      - type: JSONSchema
        url: json-schema/absentify-absence-schema.json
        title: Absence Schema
      - type: JSONSchema
        url: json-schema/absentify-workspace-schema.json
        title: Workspace Schema
      - type: JSONSchema
        url: json-schema/absentify-public-holiday-calendar-schema.json
        title: Public Holiday Calendar Schema
      - type: JSONStructure
        url: json-structure/absentify-member-structure.json
        title: Member Structure
      - type: JSONStructure
        url: json-structure/absentify-department-structure.json
        title: Department Structure
      - type: JSONStructure
        url: json-structure/absentify-leave-type-structure.json
        title: Leave Type Structure
      - type: JSONStructure
        url: json-structure/absentify-request-structure.json
        title: Request Structure
      - type: JSONStructure
        url: json-structure/absentify-absence-structure.json
        title: Absence Structure
      - type: JSONStructure
        url: json-structure/absentify-workspace-structure.json
        title: Workspace Structure
      - type: JSONStructure
        url: json-structure/absentify-public-holiday-calendar-structure.json
        title: Public Holiday Calendar Structure
      - type: JSON-LD
        url: json-ld/absentify-context.jsonld
      - type: Example
        url: examples/absentify-member-example.json
        title: Member Example
      - type: Example
        url: examples/absentify-department-example.json
        title: Department Example
      - type: Example
        url: examples/absentify-leave-type-example.json
        title: Leave Type Example
      - type: Example
        url: examples/absentify-request-example.json
        title: Request Example
      - type: Example
        url: examples/absentify-absence-example.json
        title: Absence Example
      - type: Example
        url: examples/absentify-workspace-example.json
        title: Workspace Example
common:
  - type: Portal
    url: https://absentify.com/
  - type: Documentation
    url: https://absentify.com/docs/en/
  - type: Pricing
    url: https://absentify.com/pricing
  - type: PrivacyPolicy
    url: https://absentify.com/privacy-policy
  - type: TermsOfService
    url: https://absentify.com/terms-and-conditions
  - type: Blog
    url: https://absentify.com/blog
  - type: StatusPage
    url: https://status.absentify.com
  - type: Security
    url: https://absentify.com/security
  - type: Tools
    url: https://absentify.com/docs/en/mcp-server
    title: MCP Server
  - type: SpectralRules
    url: rules/absentify-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/absence-management-absentify.yaml
  - type: Vocabulary
    url: vocabulary/absentify-vocabulary.yaml
  - type: Features
    data:
      - name: Absence Tracking
        description: Track and manage employee absences, time off, and leave requests across the organization.
      - name: Leave Request Management
        description: Submit, approve, decline, and cancel leave requests with multi-level approval workflows.
      - name: Microsoft 365 Integration
        description: Native integration with Microsoft 365 and Microsoft Teams for seamless absence management in existing workflows.
      - name: Department Management
        description: Organize employees into departments with custom leave type entitlements and approval chains.
      - name: Leave Type Configuration
        description: Define custom leave types with color coding, limits, approval requirements, and accrual policies.
      - name: Public Holiday Calendars
        description: Manage public holiday calendars per region and apply them to members and departments.
      - name: Webhook Support
        description: Receive real-time webhook notifications for request creation and status changes.
      - name: Workspace Management
        description: Configure workspace-wide settings, fiscal year, and default approval workflows.
      - name: Absence Per Day Reporting
        description: Query absences broken down by individual day for reporting and payroll integration.
  - type: UseCases
    data:
      - name: HR System Integration
        description: Integrate absence data into HRIS platforms like SAP, Workday, or BambooHR for unified people management.
      - name: Payroll Processing
        description: Export absence data to payroll systems to automatically calculate pay adjustments for time off.
      - name: Team Scheduling
        description: Sync absence data into scheduling tools to prevent understaffing and manage coverage.
      - name: Compliance Reporting
        description: Generate absence reports for regulatory compliance, labor law adherence, and audit purposes.
      - name: Custom Approval Workflows
        description: Build custom absence request approval workflows integrated with business process automation tools.
      - name: Absence Analytics
        description: Analyze absence trends, patterns, and costs to improve workforce planning and reduce absenteeism.
      - name: Microsoft Teams Automation
        description: Automate absence-related notifications and approvals directly within Microsoft Teams channels.
  - type: Integrations
    data:
      - name: Microsoft Teams
        description: Native Microsoft Teams app for submitting and approving absence requests without leaving Teams.
      - name: Microsoft 365
        description: Deep integration with Microsoft 365 calendar, Active Directory, and identity management.
      - name: Zapier
        description: Connect absentify to thousands of apps via Zapier automation workflows.
      - name: Make (Integromat)
        description: Automate absence management workflows using Make's visual automation platform.
      - name: Custom Webhooks
        description: Send real-time absence event notifications to any system via configurable webhooks.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
