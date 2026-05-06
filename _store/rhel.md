---
aid: rhel
name: Red Hat Enterprise Linux
description: Red Hat Enterprise Linux (RHEL) is the world's leading enterprise Linux platform, providing APIs and services for subscription management, security insights, compliance monitoring, vulnerability assessment, patch management, content delivery, and automation. The Red Hat Hybrid Cloud Console exposes a comprehensive suite of REST APIs for managing RHEL systems at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Compliance
  - Enterprise
  - Linux
  - Operating System
  - Red Hat
  - RHEL
  - Security
  - Subscription Management
  - Vulnerability Management
url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rhel:subscription-management-api
    name: Red Hat Subscription Management API
    description: API for managing RHEL subscriptions, entitlements, and system registrations. Enables automation of subscription lifecycle, system registration, and entitlement queries using OAuth 2.0 authentication.
    humanURL: https://access.redhat.com/management/api
    baseURL: https://api.access.redhat.com/management/v1
    tags:
      - Entitlements
      - Systems Management
      - Subscriptions
    properties:
      - type: Documentation
        url: https://access.redhat.com/management/api/docs
      - type: OpenAPI
        url: https://api.access.redhat.com/management/v1/openapi.json
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/openapi/rhel-subscription-management-openapi.yml
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
  - aid: rhel:insights-api
    name: Red Hat Insights API
    description: Predictive analytics and remediation service for RHEL systems. Provides advisor recommendations based on 20+ years of Red Hat support experience, covering security, performance, availability, and stability issues.
    humanURL: https://console.redhat.com/docs/api/insights
    baseURL: https://console.redhat.com/api/insights/v1
    tags:
      - Analytics
      - Monitoring
      - Remediation
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/insights
      - type: OpenAPI
        url: https://cloud.redhat.com/api/insights/v1/openapi.json
  - aid: rhel:security-data-api
    name: Red Hat Security Data API
    description: API for accessing security advisories, CVE data, bug fixes, and enhancement updates for Red Hat products. Enables automated vulnerability assessment and tracking of RHEL-relevant CVEs with severity filtering.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/
    baseURL: https://access.redhat.com/hydra/rest/securitydata
    tags:
      - Advisories
      - CVE
      - Errata
      - Security
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0/
      - type: GithubRepository
        url: https://github.com/RedHatOfficial/rhsecapi
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/openapi/rhel-security-data-openapi.yml
  - aid: rhel:compliance-api
    name: Red Hat Insights Compliance API
    description: API for assessing, monitoring, and reporting on security-policy compliance of RHEL systems. Based on the Security Content Automation Protocol (SCAP), enables creation and management of compliance policies and reports.
    humanURL: https://console.redhat.com/docs/api/compliance
    baseURL: https://console.redhat.com/api/compliance/v2
    tags:
      - Compliance
      - SCAP
      - Security
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/compliance
      - type: OpenAPI
        url: https://console.redhat.com/api/compliance/v2/openapi.json
  - aid: rhel:vulnerability-api
    name: Red Hat Insights Vulnerability API
    description: API for managing vulnerabilities on RHEL systems. Integrates with the Red Hat CVE database to assess outstanding CVEs and provide remediation guidance for registered RHEL hosts.
    humanURL: https://console.redhat.com/docs/api/vulnerability
    baseURL: https://console.redhat.com/api/vulnerability/v1
    tags:
      - CVE
      - Remediation
      - Security
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/vulnerability
      - type: OpenAPI
        url: https://console.redhat.com/api/vulnerability/v1/openapi.json
  - aid: rhel:patch-api
    name: Red Hat Insights Patch API
    description: API for patch management of RHEL systems. Tracks applicable advisories and patches for registered systems, enabling automated patch compliance reporting and remediation workflows.
    humanURL: https://console.redhat.com/docs/api/patch
    baseURL: https://console.redhat.com/api/patch/v3
    tags:
      - Advisories
      - Patch Management
      - Updates
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/patch
      - type: OpenAPI
        url: https://console.redhat.com/api/patch/v3/openapi.json
  - aid: rhel:inventory-api
    name: Red Hat Insights Host Inventory API
    description: API for managing the inventory of RHEL systems registered with Red Hat Insights. Provides host metadata, system profiles, and group management for hybrid cloud environments.
    humanURL: https://console.redhat.com/docs/api/inventory
    baseURL: https://console.redhat.com/api/inventory/v1
    tags:
      - Hosts
      - Inventory
      - Systems Management
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/inventory
      - type: OpenAPI
        url: https://console.redhat.com/api/inventory/v1/openapi.json
  - aid: rhel:remediations-api
    name: Red Hat Insights Remediations API
    description: API for creating and executing Ansible-based remediation playbooks for RHEL systems. Integrates with Insights advisor, vulnerability, and compliance services to automate issue resolution at scale.
    humanURL: https://console.redhat.com/docs/api/remediations
    baseURL: https://console.redhat.com/api/remediations/v1
    tags:
      - Ansible
      - Automation
      - Remediation
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/remediations
      - type: OpenAPI
        url: https://console.redhat.com/api/remediations/v1/openapi.json
common:
  - type: Portal
    url: https://access.redhat.com
  - type: Developer
    url: https://developers.redhat.com/products/rhel
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/
  - type: HybridCloudConsole
    url: https://console.redhat.com
  - type: APIManagement
    url: https://access.redhat.com/management/api
  - type: GithubOrg
    url: https://github.com/RedHatOfficial
  - type: GithubOrg
    url: https://github.com/redhat-cop
  - type: Support
    url: https://access.redhat.com/support
  - type: TermsOfService
    url: https://www.redhat.com/en/about/terms-use
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Website
    url: https://www.redhat.com
  - type: Authentication
    url: https://access.redhat.com/articles/3626371
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/rules/rhel-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/capabilities/vulnerability-management.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/json-schema/rhel-cve-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/json-schema/rhel-system-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/json-ld/rhel-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/vocabulary/rhel-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
