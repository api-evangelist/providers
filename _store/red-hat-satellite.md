---
aid: red-hat-satellite
name: Red Hat Satellite
description: Red Hat Satellite is a systems management product that helps deploy, configure, and maintain systems across physical, virtual, and cloud environments.
type: Index
image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
url: https://raw.githubusercontent.com/api-evangelist/red-hat-satellite/refs/heads/main/apis.yml
tags:
  - Configuration Management
  - Lifecycle Management
  - Patch Management
  - Subscription Management
  - Systems Management
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - name: Red Hat Satellite REST API
    description: The main REST API for Red Hat Satellite 6.x, providing programmatic access to all Satellite functions including host management, content management, provisioning, and configuration.
    image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
    baseURL: https://satellite.example.com/api/v2
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_satellite/
    tags:
      - Automation
      - REST API
      - Systems Management
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/using_the_satellite_rest_api/index
      - type: OpenAPI
        url: https://satellite.example.com/apidoc/v2.json
      - type: OpenAPI
        url: openapi/red-hat-satellite-api.yml
      - type: JSONSchema
        url: json-schema/red-hat-satellite-host-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-host-create-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-host-update-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-host-interface-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-host-interface-create-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-content-view-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-content-view-create-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-content-view-update-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-subscription-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-lifecycle-environment-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-organization-schema.json
      - type: JSONSchema
        url: json-schema/red-hat-satellite-foreman-task-schema.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-host-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-host-create-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-host-update-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-host-interface-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-host-interface-create-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-content-view-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-content-view-create-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-content-view-update-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-subscription-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-lifecycle-environment-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-organization-structure.json
      - type: JSONStructure
        url: json-structure/red-hat-satellite-foreman-task-structure.json
      - type: Example
        url: examples/red-hat-satellite-host-example.json
      - type: Example
        url: examples/red-hat-satellite-host-create-example.json
      - type: Example
        url: examples/red-hat-satellite-host-update-example.json
      - type: Example
        url: examples/red-hat-satellite-host-interface-example.json
      - type: Example
        url: examples/red-hat-satellite-host-interface-create-example.json
      - type: Example
        url: examples/red-hat-satellite-content-view-example.json
      - type: Example
        url: examples/red-hat-satellite-content-view-create-example.json
      - type: Example
        url: examples/red-hat-satellite-content-view-update-example.json
      - type: Example
        url: examples/red-hat-satellite-subscription-example.json
      - type: Example
        url: examples/red-hat-satellite-lifecycle-environment-example.json
      - type: Example
        url: examples/red-hat-satellite-organization-example.json
      - type: Example
        url: examples/red-hat-satellite-foreman-task-example.json
      - type: JSONLD
        url: json-ld/red-hat-satellite-context.jsonld
      - type: Authentication
        url: https://access.redhat.com/documentation/en-us/red_hat_satellite/6.14/html/api_guide/chap-api_guide-authentication
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html/using_the_satellite_rest_api/introduction-to-satellite-api
      - type: APIReference
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html/using_the_satellite_rest_api/index
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Satellite Hammer CLI
    description: Command-line interface tool for Red Hat Satellite that provides scriptable access to Satellite functions including host management, content views, and provisioning.
    image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
    humanURL: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/using_the_hammer_cli_tool/index
    tags:
      - Automation
      - CLI
      - Command Line
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/using_the_hammer_cli_tool/index
      - type: CodeExamples
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/using_the_hammer_cli_tool/hammer-cheat-sheet
      - type: Authentication
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/using_the_hammer_cli_tool/hammer-authentication
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Satellite Foreman API
    description: Core Foreman API integrated into Red Hat Satellite for host lifecycle management, provisioning, and configuration management. This is the upstream project API that powers Satellite's core functionality including the web UI, users, organizations, and security.
    image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
    baseURL: https://satellite.example.com/api
    humanURL: https://theforeman.org/api.html
    tags:
      - Foreman
      - Host Management
      - Provisioning
      - REST API
    properties:
      - type: Documentation
        url: https://apidocs.theforeman.org/
      - type: APIReference
        url: https://apidocs.theforeman.org/foreman/latest/apidoc/v2.html
      - type: GitHubOrganization
        url: https://github.com/theforeman
      - type: GitHubRepository
        url: https://github.com/theforeman/foreman
      - type: GitHubRepository
        url: https://github.com/theforeman/apidocs
        title: API Docs Repository
    contact:
      - type: Support
        url: https://access.redhat.com/support
      - type: Support
        url: https://community.theforeman.org/
  - name: Red Hat Satellite Katello API
    description: Content management API for Red Hat Satellite handling repositories, content views, lifecycle environments, subscriptions, and errata. Katello is the upstream plugin that provides Satellite's content and subscription management capabilities.
    image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
    baseURL: https://satellite.example.com/katello/api
    humanURL: https://theforeman.org/plugins/katello/
    tags:
      - Content Management
      - Lifecycle Environments
      - Repositories
      - REST API
      - Subscriptions
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/using_the_satellite_rest_api/index
      - type: APIReference
        url: https://apidocs.theforeman.org/katello/latest/apidoc/v2.html
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/managing_content/index
        title: Content Management Guide
      - type: GitHubRepository
        url: https://github.com/Katello/katello
      - type: GitHubOrganization
        url: https://github.com/Katello
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Satellite Ansible Collection
    description: The redhat.satellite Ansible collection provides modules, roles, and plugins for automating Red Hat Satellite configuration and management through the Satellite API. Based on the theforeman.foreman community collection.
    image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
    humanURL: https://catalog.redhat.com/en/software/collection/redhat/satellite
    tags:
      - Ansible
      - Automation
      - Configuration Management
      - Infrastructure as Code
    properties:
      - type: Documentation
        url: https://redhatsatellite.github.io/satellite-ansible-collection/develop/README.html
      - type: GitHubRepository
        url: https://github.com/RedHatSatellite/satellite-ansible-collection
      - type: Marketplace
        url: https://catalog.redhat.com/en/software/collection/redhat/satellite
      - type: GitHubRepository
        url: https://github.com/theforeman/foreman-ansible-modules
        title: Community Upstream
      - type: Blog
        url: https://www.redhat.com/en/blog/automating-red-hat-satellite-with-ansible
    contact:
      - type: Support
        url: https://access.redhat.com/support
common:
  - type: Portal
    url: https://access.redhat.com/
  - type: Documentation
    url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16
  - type: Support
    url: https://access.redhat.com/support/
  - type: StatusPage
    url: https://status.redhat.com/
  - type: Blog
    url: https://www.redhat.com/en/blog/channel/red-hat-satellite
  - type: GitHubOrganization
    url: https://github.com/theforeman
  - type: KnowledgeCenter
    url: https://access.redhat.com/solutions/
  - type: Support
    url: https://access.redhat.com/community/
    title: Community
  - type: Support
    url: https://community.theforeman.org/
    title: Foreman Community
  - type: ReleaseNotes
    url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html-single/release_notes/index
  - type: Documentation
    url: https://access.redhat.com/support/policy/updates/satellite
    title: Product Lifecycle
  - type: Documentation
    url: https://access.redhat.com/articles/1365633
    title: Release Dates
  - type: Documentation
    url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/provisioning_hosts/index
    title: Provisioning Guide
  - type: Documentation
    url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/managing_content/index
    title: Managing Hosts Guide
  - type: APIReference
    url: https://apidocs.theforeman.org/
  - type: CLI
    url: https://github.com/theforeman/hammer-cli-foreman
    title: Hammer CLI
  - type: GitHubRepository
    url: https://github.com/theforeman/foreman-ansible-modules
    title: Ansible Modules
  - type: SpectralRules
    url: rules/red-hat-satellite-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/red-hat-satellite-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/satellite-api.yaml
    title: Satellite API Shared Definition
  - type: NaftikoCapability
    url: capabilities/systems-lifecycle-management.yaml
    title: Systems Lifecycle Management Workflow
  - type: Features
    data:
      - name: Host Management
        description: Manage physical, virtual, and cloud hosts across the entire lifecycle from provisioning to decommissioning.
      - name: Content Management
        description: Curate and distribute RPM packages, errata, and container images through content views and lifecycle environments.
      - name: Patch Management
        description: Apply security patches and errata across managed systems with controlled rollouts through lifecycle stages.
      - name: Subscription Management
        description: Track and manage Red Hat subscriptions and entitlements across organizations and hosts.
      - name: Provisioning
        description: Automate bare-metal and virtual machine provisioning with kickstart templates, PXE boot, and compute resources.
      - name: Configuration Management
        description: Enforce desired-state configuration using Puppet classes and Ansible roles across managed hosts.
      - name: Multi-Tenancy
        description: Organize hosts, content, and subscriptions into isolated organizations and locations.
  - type: UseCases
    data:
      - name: Automated Server Provisioning
        description: Provision new servers automatically using compute resources, host groups, and kickstart templates.
      - name: Security Patching at Scale
        description: Identify, test, and deploy security errata across thousands of hosts using content views and promotion workflows.
      - name: Hybrid Cloud Management
        description: Manage hosts across on-premises data centers and cloud providers from a single console.
      - name: Compliance Reporting
        description: Generate compliance reports using OpenSCAP integration to verify hosts meet security baselines.
      - name: Air-Gapped Environment Management
        description: Manage systems in disconnected environments using content synchronization and inter-satellite sync.
  - type: Integrations
    data:
      - name: Ansible
        description: Automate Satellite operations and host configuration using the redhat.satellite Ansible collection.
      - name: Red Hat Insights
        description: Proactive risk analysis and remediation recommendations for managed hosts.
      - name: Puppet
        description: Apply and enforce configuration management policies using Puppet modules and classes.
      - name: OpenSCAP
        description: Security compliance scanning and reporting using SCAP content and policies.
      - name: VMware vSphere
        description: Provision and manage virtual machines on VMware infrastructure as compute resources.
      - name: Red Hat OpenStack
        description: Provision and manage instances on OpenStack as compute resources.
      - name: Amazon EC2
        description: Provision and manage cloud instances on AWS as compute resources.
      - name: Google GCE
        description: Provision and manage cloud instances on Google Cloud as compute resources.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
