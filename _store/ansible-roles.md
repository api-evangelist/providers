---
name: Ansible Roles
description: A curated collection of APIs and resources for discovering, managing, and consuming Ansible roles — the primary unit of reusable automation content in the Ansible ecosystem. Covers the Galaxy and Automation Hub APIs for role discovery, download, and publishing, as well as the Ansible Collections framework that has extended the role model into full-featured content packages.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.16'
url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/apis.yml
tags:
  - Ansible
  - Automation
  - Collections
  - Configuration Management
  - DevOps
  - Infrastructure As Code
  - Roles
apis:
  - name: Ansible Galaxy Roles API
    description: The Ansible Galaxy v1 and v2 REST API enables searching, discovering, and downloading Ansible roles contributed by the community. Supports searching roles by keyword, author, or tag; retrieving role details and version history; and downloading specific role versions for use in playbooks.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://galaxy.ansible.com
    baseURL: https://galaxy.ansible.com/api/v1/
    tags:
      - Ansible
      - Community
      - Galaxy
      - Roles
    properties:
      - type: Documentation
        url: https://galaxy.ansible.com/docs/
      - type: APIReference
        url: https://galaxy.ansible.com/api/v1/
      - type: GettingStarted
        url: https://docs.ansible.com/ansible/latest/galaxy/user_guide.html
    contact:
      - FN: Ansible Galaxy Team
        url: https://github.com/ansible/galaxy/issues
  - name: Ansible Galaxy Collections API
    description: The Ansible Galaxy v3 API provides enhanced support for Ansible collections — the modern packaging format that bundles roles, modules, plugins, and documentation together. Supports listing, searching, downloading, and versioning of published collections from the community namespace on Galaxy.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://galaxy.ansible.com
    baseURL: https://galaxy.ansible.com/api/v3/
    tags:
      - Ansible
      - Collections
      - Community
      - Galaxy
    properties:
      - type: Documentation
        url: https://galaxy.ansible.com/docs/
      - type: APIReference
        url: https://galaxy.ansible.com/api/v3/
      - type: GettingStarted
        url: https://docs.ansible.com/ansible/latest/collections/index.html
    contact:
      - FN: Ansible Galaxy Team
        url: https://github.com/ansible/galaxy/issues
  - name: Ansible Automation Hub Roles API
    description: The Red Hat Ansible Automation Hub provides certified and partner-validated Ansible collections and roles for enterprise use. The API enables access to Red Hat-certified content with SLA-backed quality, partner-certified content, and community content synced from Galaxy in supported namespaces.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://console.redhat.com/ansible/automation-hub
    baseURL: https://console.redhat.com/api/automation-hub/v3/
    tags:
      - Ansible
      - Certified Content
      - Collections
      - Enterprise
      - Red Hat
      - Roles
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
      - type: APIReference
        url: https://console.redhat.com/api/automation-hub/v3/
      - type: Portal
        url: https://console.redhat.com/ansible/automation-hub
    contact:
      - FN: Red Hat Support
        url: https://access.redhat.com/support
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: GettingStarted
    url: https://docs.ansible.com/ansible/latest/galaxy/user_guide.html
  - type: Authentication
    url: https://galaxy.ansible.com/docs/authentication/
  - type: TermsOfService
    url: https://www.redhat.com/en/about/terms-use
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: GitHubRepository
    url: https://github.com/ansible/galaxy
  - type: GitHubOrganization
    url: https://github.com/ansible
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/json-schema/ansible-roles-role-schema.json
    title: Role Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/json-schema/ansible-roles-collection-schema.json
    title: Collection Schema
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/vocabulary/ansible-roles-vocabulary.yaml
  - type: Features
    data:
      - name: Role Search and Discovery
        description: Search Galaxy for community-contributed roles by keyword, author, namespace, or tag to find reusable automation content.
      - name: Collection Packaging
        description: Bundle roles, modules, plugins, and documentation into distributable collection packages versioned and published via the Galaxy API.
      - name: Version Management
        description: Access specific versions of roles and collections, enabling pinned dependency management in Ansible projects.
      - name: Certified Content
        description: Access Red Hat-certified and partner-validated Ansible collections with enterprise-grade quality assurance via Automation Hub.
      - name: Namespace Management
        description: Manage author namespaces on Galaxy to publish and maintain role and collection content under a consistent identity.
  - type: UseCases
    data:
      - name: Role Reuse Across Projects
        description: Discover and install community roles from Galaxy to avoid reinventing automation logic for common tasks like nginx, MySQL, or Kubernetes setup.
      - name: Certified Enterprise Automation
        description: Use Red Hat-certified collections from Automation Hub in production environments where quality assurance and support are required.
      - name: Private Content Distribution
        description: Publish internal roles and collections to a private Automation Hub instance for controlled distribution within an organization.
      - name: Dependency Management
        description: Pin role and collection versions in requirements.yml files and install them via the Galaxy API in CI/CD pipelines.
  - type: Integrations
    data:
      - name: Ansible Playbooks
        description: Use roles discovered via the Galaxy API directly in Ansible playbooks with the roles directive or include_role task.
      - name: Ansible Automation Platform
        description: Synchronize collections from Galaxy or Automation Hub into Ansible Automation Platform for use in job templates.
      - name: Requirements Files
        description: Define role and collection dependencies in requirements.yml and install them automatically via ansible-galaxy CLI using the API.
---
