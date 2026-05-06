---
aid: absence-io
url: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/apis.yml
name: Absence.io
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Absences
  - Employees
  - Leave Management
  - HR
description: Absence.io is an innovative and efficient leave management software that simplifies the process of tracking and managing employee absences. It provides a centralized platform for both employees and managers to easily request, approve, and track time-off requests. Absence.io helps streamline communication and ensure transparency within an organization by providing real-time updates on employee availability and leave balances. The REST API v2 allows integration with absences, users, allowances, departments, locations, reason types, and timespans using Hawk authentication.
created: '2025-02-17'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: absence-io:absence-io
    name: Absence.io API
    tags:
      - Absences
      - Employees
      - Leave Management
    humanURL: https://www.absence.io/
    properties:
      - type: Documentation
        url: https://docs.absence.io/
      - type: Authentication
        url: https://docs.absence.io/#authentication
      - type: OpenAPI
        url: openapi/absence-io-openapi.yml
      - type: SDK
        url: https://www.npmjs.com/package/absence.io
        title: Node.js SDK
      - type: JSONSchema
        url: json-schema/absence-schema.json
        title: Absence Schema
      - type: JSONSchema
        url: json-schema/user-schema.json
        title: User Schema
      - type: JSONSchema
        url: json-schema/allowance-schema.json
        title: Allowance Schema
    description: Absence.io REST API v2 allows seamless integration of absence management features into software applications. Retrieve, create, update, and delete records for absences, users, allowances, departments, locations, reason types, and timespans. All requests and responses use JSON format with Hawk authentication.
common:
  - type: Pricing
    url: https://www.absence.io/pricing/pricing-packages/
  - type: Authentication
    url: https://docs.absence.io/#authentication
  - type: Blog
    url: https://blog.absence.io/en/
  - type: Partners
    url: https://promo.absence.io/partner-program
  - type: TermsOfService
    url: https://www.absence.io/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.absence.io/privacy-notice/
  - type: Features
    data:
      - name: Absence Management
        description: Create, approve, and track employee vacation, sick leave, and other absence types through a centralized platform.
      - name: Leave Allowances
        description: Configure and track annual leave allowances per employee, including carryover management.
      - name: Approval Workflows
        description: Configurable approval workflows for absence requests with manager notifications and audit trail.
      - name: Organizational Structure
        description: Support for departments, locations, and teams to reflect your organization's hierarchy.
      - name: Reason Types
        description: Customizable absence reason types (vacation, sick leave, parental leave, etc.) with color coding.
      - name: Working Time Configurations
        description: Define timespans with hours per day and days per week for accurate absence calculation.
      - name: REST API v2
        description: Full REST API for integrating absence management with ERP, HRIS, and other business systems using Hawk authentication.
  - type: UseCases
    data:
      - name: ERP Integration
        description: Integrate absence data with ERP systems to automatically reflect employee availability and costs.
      - name: HRIS Sync
        description: Sync employee records between Absence.io and HR information systems to maintain a single source of truth.
      - name: Payroll Processing
        description: Use absence and allowance data to calculate accurate payroll deductions and entitlements.
      - name: Capacity Planning
        description: Query team absence data to plan project staffing and identify scheduling conflicts.
      - name: Absence Reporting
        description: Generate custom reports on absence patterns, allowance usage, and team availability.
      - name: Custom Dashboards
        description: Pull absence and allowance data into custom HR dashboards and analytics tools.
  - type: Integrations
    data:
      - name: Slack
        description: Integration with Slack for absence request notifications and team visibility.
      - name: Atlassian Jira
        description: Integration with Jira for project planning with awareness of team availability.
      - name: SharePoint
        description: Integration with SharePoint for absence calendar sharing and team visibility.
      - name: Google Calendar
        description: Sync absence records to Google Calendar for team scheduling visibility.
      - name: Redmine
        description: Integration with Redmine project management for resource planning.
  - type: SpectralRules
    url: rules/absence-io-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/absence-management.yaml
  - type: NaftikoCapability
    url: capabilities/shared/absence-io.yaml
  - type: Vocabulary
    url: vocabulary/absence-io-vocabulary.yaml
  - type: JSONLD
    url: json-ld/absence-io-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
