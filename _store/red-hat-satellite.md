---
aid: red-hat-satellite
url: https://raw.githubusercontent.com/api-evangelist/red-hat-satellite/refs/heads/main/apis.yml
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
  - type: JSONLDContext
    url: json-ld/red-hat-satellite-context.jsonld
  - type: Authentication
    url: https://access.redhat.com/documentation/en-us/red_hat_satellite/6.14/html/api_guide/chap-api_guide-authentication
  - type: GettingStartedGuide
    url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html/using_the_satellite_rest_api/introduction-to-satellite-api
  - type: APIReferenceLatest
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
  - type: CheatSheet
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
  - type: APIReferenceLatest
    url: https://apidocs.theforeman.org/foreman/latest/apidoc/v2.html
  - type: GitHubOrganization
    url: https://github.com/theforeman
  - type: SourceCode
    url: https://github.com/theforeman/foreman
  - type: APIDocsRepository
    url: https://github.com/theforeman/apidocs
  contact:
  - type: Support
    url: https://access.redhat.com/support
  - type: Community
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
  - type: APIReferenceLatest
    url: https://apidocs.theforeman.org/katello/latest/apidoc/v2.html
  - type: ContentManagementGuide
    url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/managing_content/index
  - type: SourceCode
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
  - type: SourceCode
    url: https://github.com/RedHatSatellite/satellite-ansible-collection
  - type: AutomationHubListing
    url: https://catalog.redhat.com/en/software/collection/redhat/satellite
  - type: CommunityUpstream
    url: https://github.com/theforeman/foreman-ansible-modules
  - type: Blog
    url: https://www.redhat.com/en/blog/automating-red-hat-satellite-with-ansible
  contact:
  - type: Support
    url: https://access.redhat.com/support
  - type: Issues
    url: https://bugzilla.redhat.com
name: Red Hat Satellite
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
type: Contract
image: https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Red Hat Satellite is a systems management product that helps deploy, configure, and maintain systems across physical, virtual, and cloud environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

