---
aid: spin-ai
name: Spin.AI
description: Spin.AI is a SaaS security platform providing data protection, ransomware detection, and compliance management for cloud applications including Google Workspace, Microsoft 365, Salesforce, and Slack. The SpinOne Public API enables programmatic integration for managing backup entity lifecycle across enterprise SaaS environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backup
  - Compliance
  - Data Protection
  - Ransomware
  - SaaS Security
url: https://raw.githubusercontent.com/api-evangelist/spin-ai/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spin-ai:spin-ai-spinone-api
    name: Spin.AI SpinOne API
    description: The SpinOne Public API provides programmatic access to SaaS data protection management. It enables reading, filtering, and updating the backup status of entities (users, groups, shared drives) across Google Workspace, Microsoft 365, Salesforce, and Slack. Authentication uses a custom SPIN_API key scheme combining an App ID and API Key from the SpinOne admin console.
    humanURL: https://spin.ai/help/gworkspace-administration/setting-up-public-api
    tags:
      - Backup
      - Data Protection
      - Entities
      - Google Workspace
      - Microsoft 365
      - SaaS Security
    properties:
      - type: Documentation
        url: https://spin.ai/help/gworkspace-administration/setting-up-public-api
      - type: SwaggerUI
        url: https://apg-1.spin.ai/swagger-ui/
      - type: OpenAPI
        url: openapi/spin-ai-openapi.yml
      - type: SpectralRules
        url: rules/spin-ai-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/saas-data-protection.yaml
common:
  - type: Website
    url: https://www.spin.ai
  - type: Documentation
    url: https://spin.ai/help/
  - type: Portal
    url: https://spin.ai/help/gworkspace-administration/setting-up-public-api
  - type: Integrations
    url: https://spin.ai/integrations/
  - type: Support
    url: https://spin.ai/support/
  - type: TermsOfService
    url: https://spin.ai/terms-of-service/
  - type: PrivacyPolicy
    url: https://spin.ai/privacy-policy/
  - type: Blog
    url: https://spin.ai/blog/
  - type: LinkedIn
    url: https://www.linkedin.com/company/spin-ai/
  - type: OpenAPI
    url: openapi/spin-ai-openapi.yml
  - type: SpectralRules
    url: rules/spin-ai-rules.yml
  - type: Vocabulary
    url: vocabulary/spin-ai-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/saas-data-protection.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
