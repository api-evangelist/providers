---
aid: red-hat-enterprise-linux-8
name: Red Hat Enterprise Linux 8
description: Red Hat Enterprise Linux 8 (RHEL 8) is an enterprise-grade Linux distribution that provides a stable, secure, and high-performance operating system platform for modern IT environments. RHEL 8 is managed and accessed programmatically through Red Hat's cloud console APIs, subscription management APIs, security data APIs, and system management interfaces including Insights, Image Builder, and Cockpit. These APIs enable automated provisioning, configuration, security scanning, patch management, and compliance reporting for RHEL deployments at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise
  - Linux
  - Operating System
  - Red Hat
  - RHEL
url: https://raw.githubusercontent.com/api-evangelist/red-hat-enterprise-linux-8/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: red-hat-enterprise-linux-8:subscription-management-api
    name: RHEL 8 Subscription Management API
    description: The Red Hat Subscription Management (RHSM) API provides programmatic access to manage Red Hat subscriptions, entitlements, and system registrations. Operators can list, activate, and manage subscriptions, query available SKUs, register and unregister systems, and retrieve entitlement certificates. Authentication uses OAuth 2.0 tokens obtained via the Red Hat SSO service.
    humanURL: https://access.redhat.com/management/api
    baseURL: https://api.access.redhat.com/management/v1
    tags:
      - Entitlements
      - Registration
      - Subscriptions
      - System Management
    properties:
      - type: Documentation
        url: https://access.redhat.com/management/api/rhsm
      - type: OpenAPI
        url: https://api.access.redhat.com/management/v1/openapi.json
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
  - aid: red-hat-enterprise-linux-8:insights-api
    name: RHEL 8 Insights API
    description: Red Hat Insights is a predictive analytics service for RHEL systems that provides API access to vulnerability assessment, compliance reporting, patch management, drift analysis, and advisor recommendations. The Insights API allows automation of security scanning, patch prioritization, and system health monitoring for registered RHEL hosts. Authentication uses OAuth 2.0 tokens via the console.redhat.com identity service.
    humanURL: https://console.redhat.com/docs/api/insights
    baseURL: https://console.redhat.com/api/insights/v1
    tags:
      - Analytics
      - Compliance
      - Monitoring
      - Predictive Analytics
      - Security
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/insights
      - type: OpenAPI
        url: https://console.redhat.com/api/insights/v1/openapi.json
      - type: Console
        url: https://console.redhat.com/insights
  - aid: red-hat-enterprise-linux-8:image-builder-api
    name: RHEL 8 Image Builder API
    description: The Red Hat Image Builder API enables automated creation of custom RHEL system images for cloud, virtual machine, and bare-metal deployments. Users can define image compositions, specify packages and customizations, build images for specific target environments (AWS, Azure, GCP, VMware, ISO), and download completed image artifacts. The API is part of the Red Hat Hybrid Cloud Console.
    humanURL: https://console.redhat.com/docs/api/image-builder
    baseURL: https://console.redhat.com/api/image-builder/v1
    tags:
      - Cloud
      - Deployment
      - Image Builder
      - Infrastructure
      - Provisioning
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/composing_a_customized_rhel_system_image/index
      - type: OpenAPI
        url: https://console.redhat.com/api/image-builder/v1/openapi.json
      - type: Tutorial
        url: https://www.redhat.com/en/blog/using-red-hat-image-builder
  - aid: red-hat-enterprise-linux-8:patch-api
    name: RHEL 8 Patch Management API
    description: The Red Hat Patch Management API (part of Red Hat Insights) provides endpoints for querying available errata, advisories, and CVE patches for registered RHEL systems. It enables operators to list applicable patches per system, filter by severity or type, and trigger patch installations. The API integrates with Satellite for on-premises patch orchestration.
    humanURL: https://console.redhat.com/docs/api/patch
    baseURL: https://console.redhat.com/api/patch/v3
    tags:
      - Errata
      - Packages
      - Patch Management
      - Security
      - Updates
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/patch
      - type: OpenAPI
        url: https://console.redhat.com/api/patch/v3/openapi.json
  - aid: red-hat-enterprise-linux-8:vulnerability-api
    name: RHEL 8 Vulnerability Management API
    description: The Red Hat Vulnerability Management API (part of Insights) provides programmatic access to CVE vulnerability data for registered RHEL systems. Operators can query known CVEs affecting their hosts, retrieve severity scores, filter by system or CVE, and export vulnerability reports for compliance and risk management purposes.
    humanURL: https://console.redhat.com/docs/api/vulnerability
    baseURL: https://console.redhat.com/api/vulnerability/v1
    tags:
      - CVE
      - Risk Management
      - Security
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/vulnerability
      - type: OpenAPI
        url: https://console.redhat.com/api/vulnerability/v1/openapi.json
  - aid: red-hat-enterprise-linux-8:compliance-api
    name: RHEL 8 Compliance API
    description: The Red Hat Compliance API (part of Insights) enables automated compliance scanning and reporting against security profiles such as CIS, DISA STIG, and PCI-DSS for RHEL systems. Operators can list compliance policies, query system compliance scores, retrieve rule results, and download compliance reports in SCAP and PDF formats.
    humanURL: https://console.redhat.com/docs/api/compliance
    baseURL: https://console.redhat.com/api/compliance/v2
    tags:
      - Compliance
      - SCAP
      - Security
      - STIG
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/compliance
      - type: OpenAPI
        url: https://console.redhat.com/api/compliance/v2/openapi.json
  - aid: red-hat-enterprise-linux-8:security-data-api
    name: RHEL 8 Security Data API
    description: The Red Hat Security Data API provides public access to Red Hat's security advisory and CVE data. Operators can query CVEs affecting RHEL products, retrieve CVSS scores, list security advisories (RHSA), bug fix advisories (RHBA), and enhancement advisories (RHEA), and obtain OVAL XML data for vulnerability scanning integration. No authentication is required for public data.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0
    baseURL: https://access.redhat.com/labs/securitydataapi
    tags:
      - Advisories
      - CVE
      - OVAL
      - Public Data
      - Security
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0/html/red_hat_security_data_api/index
      - type: API Endpoint
        url: https://access.redhat.com/labs/securitydataapi/
      - type: Examples
        url: https://access.redhat.com/articles/2915291
      - type: OpenAPI
        url: openapi/red-hat-enterprise-linux-8-security-data-openapi.yml
  - aid: red-hat-enterprise-linux-8:host-inventory-api
    name: RHEL 8 Host Inventory API
    description: The Red Hat Insights Host Inventory API provides programmatic access to the inventory of RHEL systems registered with Red Hat Insights. Operators can query hosts by attributes, retrieve system facts, manage host groups, query system profiles, and track system metadata including OS version, hardware, and installed packages.
    humanURL: https://console.redhat.com/docs/api/inventory
    baseURL: https://console.redhat.com/api/inventory/v1
    tags:
      - Asset Management
      - Inventory
      - System Management
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api/inventory
      - type: OpenAPI
        url: https://console.redhat.com/api/inventory/v1/openapi.json
  - aid: red-hat-enterprise-linux-8:cockpit-api
    name: RHEL 8 Cockpit Web Console API
    description: Cockpit is a web-based system management interface for RHEL that exposes internal D-Bus and system APIs through a WebSocket-based transport. The Cockpit API provides access to system configuration, storage management, network configuration, service management, user accounts, and system logs from a web browser. It operates locally on each managed system at port 9090.
    humanURL: https://cockpit-project.org/guide/latest/api-base1.html
    baseURL: https://localhost:9090/cockpit
    tags:
      - Management
      - System Administration
      - UI
      - Web Console
    properties:
      - type: Documentation
        url: https://cockpit-project.org/guide/latest/api-base1.html
      - type: GitHub
        url: https://github.com/cockpit-project/cockpit
      - type: Guide
        url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_systems_using_the_rhel_8_web_console/index
  - aid: red-hat-enterprise-linux-8:system-roles-api
    name: RHEL 8 System Roles API
    description: RHEL System Roles are a collection of Ansible roles and modules for automating RHEL system configuration tasks including networking, storage, certificate management, SELinux, time sync, and firewall configuration. The roles expose a structured YAML-based API for declarative system state management through Ansible Automation Platform or standalone Ansible.
    humanURL: https://access.redhat.com/articles/3050101
    baseURL: https://console.redhat.com/ansible/automation-hub/
    tags:
      - Ansible
      - Automation
      - Configuration Management
      - System Roles
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/administration_and_configuration_tasks_using_system_roles_in_rhel/index
      - type: GitHub
        url: https://github.com/linux-system-roles
      - type: Ansible Galaxy
        url: https://galaxy.ansible.com/linux-system-roles
common:
  - type: Portal
    url: https://access.redhat.com/
  - type: Customer Portal
    url: https://console.redhat.com/
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/
  - type: Knowledge Base
    url: https://access.redhat.com/knowledgebase/
  - type: Support
    url: https://access.redhat.com/support/
  - type: Downloads
    url: https://access.redhat.com/downloads/
  - type: Blog
    url: https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux
  - type: Release Notes
    url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/8.0_release_notes/index
  - type: Security
    url: https://access.redhat.com/security/
  - type: Training
    url: https://www.redhat.com/en/services/training-and-certification
  - type: GitHub Organization
    url: https://github.com/redhat-developer
  - type: Privacy Policy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Terms of Service
    url: https://www.redhat.com/en/about/agreements
  - type: OpenAPI
    url: openapi/red-hat-enterprise-linux-8-security-data-openapi.yml
  - type: JSONLDContext
    url: json-ld/red-hat-enterprise-linux-8-context.jsonld
  - type: JSONSchema
    url: json-schema/red-hat-enterprise-linux-8-cve-schema.json
  - type: JSONStructure
    url: json-structure/red-hat-enterprise-linux-8-cve-structure.json
  - type: SpectralRuleset
    url: rules/red-hat-enterprise-linux-8-rules.yml
  - type: Vocabulary
    url: vocabulary/red-hat-enterprise-linux-8-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
