---
aid: amazon-incident-manager
name: Amazon Incident Manager
description: AWS Systems Manager Incident Manager is an incident management console designed to help users mitigate and recover from incidents affecting their AWS-hosted applications. It enables faster incident resolution by automating response plans and engaging responders across notification channels.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - AWS
  - DevOps
  - Incident Management
  - Operations
url: https://raw.githubusercontent.com/api-evangelist/amazon-incident-manager/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-incident-manager:aws-ssm-incidents-api
    name: AWS Systems Manager Incident Manager API
    description: The AWS Systems Manager Incident Manager API provides programmatic access to create and manage response plans, incidents, timelines, related items, and replication sets for automated incident response.
    humanURL: https://aws.amazon.com/systems-manager/features/#Incident_Manager
    baseURL: https://ssm-incidents.amazonaws.com
    tags:
      - DevOps
      - Incident Management
      - Operations
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-incident-manager-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/incident-manager/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/systems-manager/pricing/
      - type: FAQ
        url: https://aws.amazon.com/systems-manager/faq/
common:
  - type: Portal
    url: https://aws.amazon.com/systems-manager/features/#Incident_Manager
  - type: Website
    url: https://aws.amazon.com/systems-manager/
  - type: Documentation
    url: https://docs.aws.amazon.com/incident-manager/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/tag/aws-systems-manager-incident-manager/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/systems-manager/incidents/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-incident-manager-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/ssm-incidents.yaml
  - type: NaftikoCapability
    url: capabilities/incident-response.yaml
  - type: Vocabulary
    url: vocabulary/amazon-incident-manager-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-incident-manager-context.jsonld
  - type: Features
    data:
      - name: Automated Response Plans
        description: Create response plans that automatically engage responders and execute runbooks when incidents occur.
      - name: Incident Tracking
        description: Track incident status, severity, and timeline in real time from a centralized console.
      - name: Multi-Channel Notifications
        description: Notify responders via SMS, email, voice, and PagerDuty through contact channels.
      - name: Runbook Automation
        description: Automatically run Systems Manager Automation runbooks as part of incident response.
      - name: Post-Incident Analysis
        description: Generate analysis reports with timeline events to identify root causes and improve future response.
      - name: Multi-Region Replication
        description: Replicate incident data across multiple AWS regions for global incident management.
  - type: UseCases
    data:
      - name: On-Call Management
        description: Define escalation policies and on-call schedules to ensure the right responders are engaged.
      - name: Automated Incident Detection
        description: Integrate with CloudWatch alarms and EventBridge to automatically trigger response plans.
      - name: Cross-Team Coordination
        description: Coordinate incident response across multiple teams with shared incident channels.
      - name: Compliance and Audit
        description: Maintain incident timelines and analysis reports for regulatory compliance and audits.
  - type: Integrations
    data:
      - name: Amazon CloudWatch
        description: Trigger incident response plans automatically from CloudWatch alarms.
      - name: AWS Systems Manager Automation
        description: Run automation runbooks as part of incident response workflows.
      - name: PagerDuty
        description: Integrate with PagerDuty for on-call management and notification.
      - name: AWS Chatbot
        description: Receive incident notifications and updates in Slack or Microsoft Teams.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
