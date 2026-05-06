---
aid: amazon-health-dashboard
name: Amazon Health Dashboard
description: AWS Health Dashboard provides ongoing visibility into the status of your AWS services, and alerts and remediation guidance when AWS is experiencing events that may affect your operations. It delivers personalized information about events that might affect your specific AWS resources and accounts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Health Monitoring
  - Notifications
  - Operations
  - Service Status
url: https://raw.githubusercontent.com/api-evangelist/amazon-health-dashboard/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-health-dashboard:aws-health-api
    name: AWS Health API
    description: The AWS Health API provides programmatic access to AWS Health information about events that can affect your AWS infrastructure, including service outages, planned maintenance, and account-specific notifications.
    humanURL: https://aws.amazon.com/health/
    baseURL: https://health.us-east-1.amazonaws.com
    tags:
      - Health Monitoring
      - Notifications
      - Operations
      - Service Status
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-health-dashboard-openapi.yaml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/health/latest/ug/getting-started-api.html
      - type: Pricing
        url: https://aws.amazon.com/premiumsupport/
      - type: APIReference
        url: https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: JSONSchema
        url: json-schema/health-event-schema.json
      - type: JSONLD
        url: json-ld/amazon-health-dashboard-context.jsonld
common:
  - type: Portal
    url: https://health.aws.amazon.com/health/home
  - type: Documentation
    url: https://docs.aws.amazon.com/health/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/health/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-health-dashboard-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-health-dashboard-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-health-dashboard-operations-monitoring.yaml
  - type: Features
    data:
      - name: Personalized Health Notifications
        description: Receive alerts specifically tailored to the AWS services and resources you use in your accounts.
      - name: Proactive Event Notifications
        description: Get advance notice of AWS planned maintenance, deprecations, and service changes before they occur.
      - name: Remediation Guidance
        description: Each health event includes specific guidance on what actions to take to minimize impact.
      - name: Organization-Wide Visibility
        description: View health events across all accounts in an AWS Organization from a single management account.
      - name: Affected Resource Identification
        description: Identify exactly which of your specific EC2 instances, RDS databases, or other resources are impacted.
      - name: Event History
        description: Access up to 90 days of event history for your account.
  - type: UseCases
    data:
      - name: Operations Monitoring
        description: Monitor AWS service health in real-time to detect and respond to events affecting workloads.
      - name: Automated Incident Response
        description: Trigger automated runbooks when health events affect specific resources using EventBridge.
      - name: Change Management
        description: Track planned maintenance and scheduled changes to coordinate deployments.
      - name: Compliance Reporting
        description: Maintain records of AWS service events for compliance and audit purposes.
  - type: Integrations
    data:
      - name: Amazon EventBridge
        description: Receive health events as EventBridge events and trigger automated Lambda responses.
      - name: AWS Organizations
        description: View health events across all member accounts in an organization.
      - name: AWS Support
        description: Health events link directly to AWS Support cases for faster resolution.
      - name: Amazon CloudWatch
        description: Create CloudWatch alarms based on health event metrics.
      - name: AWS Chatbot
        description: Receive health notifications in Slack or Chime via AWS Chatbot.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
