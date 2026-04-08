---
aid: red-hat-enterprise-linux-8
url: https://raw.githubusercontent.com/api-evangelist/red-hat-enterprise-linux-8/refs/heads/main/apis.yml
apis:
- name: RHEL 8 Subscription Management API
  description: API for managing Red Hat subscriptions, entitlements, and system registration.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/subscription-icon.png
  humanURL: https://access.redhat.com/management/api
  baseURL: https://api.access.redhat.com/management/v1
  tags:
  - Entitlements
  - Subscriptions
  - System Management
  properties:
  - type: Documentation
    url: https://access.redhat.com/management/api/rhsm
  - type: OpenAPI
    url: https://api.access.redhat.com/management/v1/openapi.json
  - type: Authentication
    url: https://access.redhat.com/articles/3626371
- name: RHEL 8 Insights API
  description: Red Hat Insights API for predictive analytics, security vulnerabilities, and system health monitoring.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/insights-icon.png
  humanURL: https://console.redhat.com/docs/api/insights
  baseURL: https://console.redhat.com/api/insights/v1
  tags:
  - Analytics
  - Monitoring
  - Security
  - Vulnerabilities
  properties:
  - type: Documentation
    url: https://console.redhat.com/docs/api/insights
  - type: OpenAPI
    url: https://console.redhat.com/api/insights/v1/openapi.json
  - type: Console
    url: https://console.redhat.com/insights
- name: RHEL 8 Image Builder API
  description: API for creating custom RHEL system images for cloud, virtual, and physical deployments.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/image-builder-icon.png
  humanURL: https://console.redhat.com/docs/api/image-builder
  baseURL: https://console.redhat.com/api/image-builder/v1
  tags:
  - Cloud
  - Deployment
  - Image Builder
  - Provisioning
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/composing_a_customized_rhel_system_image/index
  - type: OpenAPI
    url: https://console.redhat.com/api/image-builder/v1/openapi.json
  - type: Tutorial
    url: https://www.redhat.com/en/blog/using-red-hat-image-builder
- name: RHEL 8 Package Management API
  description: API for querying and managing RPM packages, repositories, and updates.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/package-icon.png
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_software_with_the_dnf_tool/index
  baseURL: https://access.redhat.com/labs/
  tags:
  - DNF
  - Packages
  - RPM
  - Updates
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_software_with_the_dnf_tool/index
  - type: Command Reference
    url: https://dnf.readthedocs.io/en/latest/api.html
  - type: Labs
    url: https://access.redhat.com/labs/
- name: RHEL 8 Content Access API
  description: API for accessing RHEL content, errata, CVEs, and security advisories.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/security-icon.png
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0
  baseURL: https://access.redhat.com/labs/securitydataapi
  tags:
  - Advisories
  - CVE
  - Errata
  - Security
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0/html/red_hat_security_data_api/index
  - type: API Endpoint
    url: https://access.redhat.com/labs/securitydataapi/
  - type: Examples
    url: https://access.redhat.com/articles/2915291
- name: RHEL 8 Cockpit API
  description: Web-based management interface API for system administration tasks.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/cockpit-icon.png
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
- name: RHEL 8 System Roles API
  description: Ansible-based system configuration API for automating RHEL deployments.
  image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/ansible-icon.png
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
name: Red Hat Enterprise Linux 8
tags:
- Enterprise
- Linux
- Operating System
- Red Hat
- RHEL
type: Contract
image: https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/Logo-Red_Hat-Enterprise_Linux_8-B-Standard-RGB.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Red Hat Enterprise Linux 8 provides a stable, proven foundation for modern IT environments with enhanced security, performance, and management capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

