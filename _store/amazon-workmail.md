---
aid: amazon-workmail
name: Amazon WorkMail
description: Amazon WorkMail is a secure, managed business email and calendar service with support for existing desktop and mobile email client applications. It provides encrypted mailboxes, corporate calendaring, full Outlook compatibility, and enterprise-grade security controls for business communications. WorkMail integrates with Active Directory, supports IMAP and Exchange ActiveSync for mobile devices, and provides 80 API operations for programmatic management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Business Communication
  - Calendar
  - Email
  - Exchange
  - Enterprise
url: https://raw.githubusercontent.com/api-evangelist/amazon-workmail/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-workmail:amazon-workmail-api
    name: Amazon WorkMail API
    description: The Amazon WorkMail API provides programmatic access to manage organizations, users, groups, aliases, mailboxes, resources, and mobile device access. It enables automation of email infrastructure provisioning and management for enterprise deployments with 80 operations.
    humanURL: https://aws.amazon.com/workmail/
    baseURL: https://workmail.amazonaws.com
    tags:
      - AWS
      - Calendar
      - Email
      - Enterprise
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/workmail/latest/adminguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/workmail/latest/APIReference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/workmail/latest/adminguide/getting_started.html
      - type: Pricing
        url: https://aws.amazon.com/workmail/pricing/
      - type: FAQ
        url: https://aws.amazon.com/workmail/faqs/
      - type: OpenAPI
        url: openapi/amazon-workmail-openapi-original.yaml
      - type: JSONSchema
        url: json-schema/workmail-organization-schema.json
      - type: JSONLD
        url: json-ld/amazon-workmail-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/workmail/
  - type: Documentation
    url: https://docs.aws.amazon.com/workmail/latest/adminguide/
  - type: Console
    url: https://console.aws.amazon.com/workmail/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: rules/amazon-workmail-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-workmail-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/email-management.yaml
  - type: Features
    data:
      - name: Outlook Compatibility
        description: Native support for Microsoft Outlook on Windows and Mac OS X with free/busy scheduling, delegation, and out-of-office replies.
      - name: Enterprise-Grade Security
        description: Automatic encryption at rest using AWS KMS and SSL encryption in transit with spam and virus protection.
      - name: Active Directory Integration
        description: Integration with AWS Directory Service AD Connector and Microsoft Active Directory for seamless enterprise authentication.
      - name: Mobile Device Management
        description: Exchange ActiveSync support with remote device encryption, lock, password reset, and wipe capabilities across iOS, Android, and Windows.
      - name: Exchange Interoperability
        description: Hybrid environments with Microsoft Exchange Server 2010 and 2013 for gradual migration scenarios.
      - name: Administrative SDK
        description: Programmatic API for managing users, groups, resources, and organizational settings at scale.
      - name: Email Flow Rules
        description: Configurable email flow rules for filtering and routing messages based on custom organizational policies.
      - name: Journaling and Archiving
        description: Email journaling capabilities for compliance archiving and e-discovery requirements.
  - type: UseCases
    data:
      - name: Exchange Migration
        description: Migrate from Microsoft Exchange to Amazon WorkMail with minimal disruption using hybrid environment support.
      - name: Enterprise Email Provisioning
        description: Automate user and mailbox provisioning via API for large-scale enterprise deployments.
      - name: Compliance Email Archiving
        description: Use journaling and encryption for HIPAA-compliant and regulatory email archiving programs.
      - name: Mobile Workforce Enablement
        description: Provide secure mobile email access with ActiveSync and mobile device management policies.
      - name: Hybrid Cloud Email
        description: Run WorkMail alongside existing Exchange infrastructure for gradual cloud migration.
  - type: Integrations
    data:
      - name: AWS Directory Service
        description: AD Connector and Simple AD for directory integration and single sign-on capabilities.
      - name: AWS KMS
        description: Key Management Service for managing encryption keys for mailbox data at rest.
      - name: AWS CloudTrail
        description: Audit logging of all WorkMail API calls for compliance and security monitoring.
      - name: AWS Lambda
        description: Lambda integration for email flow rules and custom email processing workflows.
      - name: Microsoft Outlook
        description: Native Outlook MAPI support for Windows and Mac desktops.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
