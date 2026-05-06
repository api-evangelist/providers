---
aid: bettercloud
name: BetterCloud
description: BetterCloud is the end-to-end SaaS management platform that enables IT teams to discover, manage, and secure the growing SaaS environment. The platform provides automated workflows, security policies, and management capabilities for SaaS applications in enterprise environments, handling billions of API calls per day across 100+ SaaS application integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Compliance
  - Enterprise
  - IT Operations
  - SaaS Management
  - Security
  - Workflows
  - User Lifecycle
url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: bettercloud:bettercloud-platform-api
    name: BetterCloud Platform API
    description: The BetterCloud Platform API provides REST API access for managing SaaS application operations, automated workflows, user lifecycle management, and security policies. It enables IT and security teams to programmatically automate management workflows and enforce security policies across cloud technology stacks using standard HTTP methods.
    humanURL: https://developer.bettercloud.com/
    baseURL: https://api.bettercloud.com/v1
    tags:
      - Automation
      - REST API
      - SaaS Management
      - Security
      - User Lifecycle
      - Workflows
    properties:
      - type: Documentation
        url: https://developer.bettercloud.com/
      - type: GettingStarted
        url: https://support.bettercloud.com/s/article/BCCINT4000--BetterCloud-API-Overview-bc33451
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/openapi/bettercloud-platform-api.yaml
common:
  - type: Portal
    url: https://developer.bettercloud.com/
  - type: GettingStarted
    url: https://support.bettercloud.com/s/article/BCCINT4000--BetterCloud-API-Overview-bc33451
  - type: Pricing
    url: https://www.bettercloud.com/pricing/
  - type: Blog
    url: https://www.bettercloud.com/monitor/
  - type: Support
    url: https://support.bettercloud.com/s/
  - type: Login
    url: https://support.bettercloud.com/s/login/
  - type: SignUp
    url: https://www.bettercloud.com/monitor/sign-up/
  - type: GitHubOrganization
    url: https://github.com/BetterCloud
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/rules/bettercloud-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/vocabulary/bettercloud-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/capabilities/saas-lifecycle-management.yaml
  - type: Features
    data:
      - name: User Lifecycle Management
        description: Automate user onboarding and offboarding workflows across all connected SaaS applications.
      - name: SaaS Discovery
        description: Automatically discover all SaaS applications in use across the organization.
      - name: Automated Workflows
        description: Build no-code automation workflows triggered by events, schedules, or manual action.
      - name: Security Policy Enforcement
        description: Create and enforce security policies that monitor and remediate violations across SaaS apps.
      - name: Group Management
        description: Manage groups and memberships across Google Workspace, Azure AD, and other directory services.
      - name: Audit Logging
        description: Comprehensive audit trail of all actions taken by users and automated workflows.
      - name: SaaS Integrations
        description: Connect and manage 100+ enterprise SaaS applications including Google Workspace, Slack, Salesforce, and more.
      - name: License Management
        description: Track and optimize SaaS licenses to reduce spend and identify unused seats.
  - type: UseCases
    data:
      - name: Employee Offboarding
        description: Automatically revoke access and deprovision users across all SaaS applications when an employee leaves.
      - name: Employee Onboarding
        description: Automatically provision new employees with appropriate SaaS access based on role and department.
      - name: SaaS Spend Optimization
        description: Identify underutilized licenses and redundant applications to reduce SaaS spend.
      - name: Security Incident Response
        description: Immediately suspend and deprovision compromised accounts across all SaaS platforms.
      - name: Compliance Auditing
        description: Generate audit reports showing who has access to what across all connected SaaS applications.
      - name: Access Reviews
        description: Periodically review and certify user access to ensure least-privilege principles.
  - type: Integrations
    data:
      - name: Google Workspace
        description: Manage Google Workspace users, groups, Drive files, and calendar access.
      - name: Slack
        description: Manage Slack workspace users, channels, and app connections.
      - name: Salesforce
        description: Manage Salesforce user provisioning and deprovisioning.
      - name: Microsoft 365
        description: Manage Microsoft 365 users, licenses, and Azure AD groups.
      - name: Okta
        description: Connect BetterCloud workflows with Okta identity management.
      - name: ServiceNow
        description: Trigger BetterCloud workflows from ServiceNow ITSM tickets.
      - name: Jira
        description: Integrate SaaS management actions with Jira issue workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
