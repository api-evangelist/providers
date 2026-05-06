---
aid: backupify
name: Backupify
description: Backupify (by Datto/Kaseya) is a SaaS backup platform providing automated cloud-to-cloud data protection for Google Workspace and Microsoft 365. It offers seat-level backup coverage for users, shared mailboxes, SharePoint sites, team sites, and Microsoft Teams. The SaaS Protection REST API enables MSPs and enterprise IT teams to automate domain administration and seat licensing programmatically.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SaaS Backup
  - Data Protection
  - Cloud Backup
  - Microsoft 365
  - Google Workspace
url: https://raw.githubusercontent.com/api-evangelist/backupify/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: backupify:saas-protection-api
    name: Backupify SaaS Protection API
    description: The Backupify SaaS Protection REST API enables programmatic management of cloud-to-cloud backup for Microsoft 365 and Google Workspace. Covers domain listing, seat enumeration, and bulk seat licensing operations. Authentication uses HTTP Basic auth with API key credentials.
    humanURL: https://www.backupify.com/
    tags:
      - SaaS Backup
      - Data Protection
      - Microsoft 365
      - Google Workspace
    properties:
      - type: Documentation
        url: https://saasprotection.datto.com/help/M365/Content/Other_Administrative_Tasks/using-rest-api-saas-protection.htm
      - type: OpenAPI
        url: openapi/backupify-saas-protection-api.yaml
common:
  - type: Website
    url: https://www.backupify.com
  - type: Documentation
    url: https://saasprotection.datto.com/help/M365/Content/Other_Administrative_Tasks/using-rest-api-saas-protection.htm
  - type: Portal
    url: https://portal.dattobackup.com
  - type: Pricing
    url: https://www.backupify.com/pricing
  - type: Blog
    url: https://www.datto.com/blog/
  - type: Support
    url: https://www.datto.com/support/
  - type: TermsOfService
    url: https://www.datto.com/legal/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.datto.com/legal/privacy-policy/
  - type: GitHubOrganization
    url: https://github.com/backupify
  - type: SpectralRules
    url: rules/backupify-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/backupify-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/saas-backup-management.yaml
  - name: Features
    type: Features
    data:
      - name: Microsoft 365 Backup
        description: Automated cloud-to-cloud backup for Exchange, OneDrive, SharePoint, and Teams.
      - name: Google Workspace Backup
        description: Automated backup for Gmail, Drive, Contacts, and Calendar.
      - name: Seat-Level Control
        description: License, unlicense, or pause backup at the individual user, mailbox, site, or team level.
      - name: Bulk Seat Management
        description: Manage up to 100 seat changes in a single API call.
      - name: MSP Multi-Tenant
        description: Manage backup across multiple customer domains from a single pane of glass.
      - name: Point-in-Time Recovery
        description: Restore data to any point in time with granular item-level recovery.
  - name: UseCases
    type: UseCases
    data:
      - name: SaaS Data Protection
        description: Protect Microsoft 365 and Google Workspace data from accidental deletion, ransomware, and insider threats.
      - name: MSP Backup Management
        description: Automate backup seat provisioning and de-provisioning across multiple customer tenants.
      - name: Compliance and Archival
        description: Maintain immutable backups for compliance, legal hold, and audit requirements.
      - name: Migration Support
        description: Backup source data before and during cloud-to-cloud migrations.
  - name: Integrations
    type: Integrations
    data:
      - name: Microsoft 365
        description: Native integration with Exchange Online, OneDrive, SharePoint, and Microsoft Teams.
      - name: Google Workspace
        description: Native integration with Gmail, Google Drive, Contacts, and Calendar.
      - name: Kaseya VSA
        description: Integration with Kaseya RMM for MSP workflow automation.
      - name: Datto RMM
        description: Integration with Datto RMM for endpoint and SaaS backup orchestration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
