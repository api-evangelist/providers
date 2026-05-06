---
name: Ubuntu
description: Collection of APIs and services provided by Canonical for Ubuntu and related products. Includes the Snap Store API for package management, Launchpad API for project hosting and bug tracking, Ubuntu Security CVE API for vulnerability intelligence, and enterprise services including Ubuntu Pro, MAAS, Juju, and Landscape.
image: https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png
url: https://ubuntu.com
created: '2024-01-15'
modified: '2026-05-03'
apis:
  - name: Launchpad API
    description: REST API for Launchpad, Ubuntu's project hosting and collaboration platform. Provides access to people, projects, bugs, packages, branches, and distributions. Uses OAuth 1.0a authentication and WADL-described resources.
    image: https://launchpad.net/@@/launchpad-logo
    humanURL: https://launchpad.net/
    baseURL: https://api.launchpad.net/1.0
    tags:
      - Bugs
      - Collaboration
      - Distributions
      - Packages
      - Projects
      - Open Source
    properties:
      - type: Documentation
        url: https://launchpad.net/+apidoc/
      - type: Documentation
        url: https://documentation.ubuntu.com/launchpad/user/explanation/launchpad-api/launchpad-web-service/
      - type: Authentication
        url: https://help.launchpad.net/API/Uses
      - type: Wadl
        url: https://api.launchpad.net/devel
      - type: OpenAPI
        url: openapi/ubuntu-launchpad-openapi.yml
    contact:
      - type: Support
        url: https://answers.launchpad.net/launchpad
  - name: Ubuntu Pro API
    description: API for managing Ubuntu Pro subscriptions and entitlements, including security patches, compliance tooling, and extended security maintenance.
    humanURL: https://ubuntu.com/pro
    baseURL: https://contracts.canonical.com/
    tags:
      - Enterprise
      - Security
      - Subscriptions
      - Support
    properties:
      - type: Documentation
        url: https://canonical-ubuntu-pro-client.readthedocs-hosted.com/
      - type: Authentication
        url: https://ubuntu.com/pro/dashboard
    contact:
      - type: Support
        url: https://ubuntu.com/support
  - name: Snap Store API
    description: API for the Snap Store for publishing and managing snap packages. Enables snap search, package info retrieval, refresh operations, category listings, and usage metrics for IoT and desktop deployments.
    humanURL: https://snapcraft.io/
    baseURL: https://api.snapcraft.io
    tags:
      - Applications
      - Distribution
      - Packages
      - Snaps
      - Package Management
    properties:
      - type: Documentation
        url: https://snapcraft.io/docs/snapcraft-store-api
      - type: Documentation
        url: https://api.snapcraft.io/docs/
      - type: Dashboard
        url: https://snapcraft.io/account
      - type: Developer Portal
        url: https://snapcraft.io/docs
      - type: OpenAPI
        url: openapi/ubuntu-snap-store-openapi.yml
      - type: Example
        url: examples/ubuntu-snap-search-example.json
      - type: JSONSchema
        url: json-schema/ubuntu-snap-schema.json
    contact:
      - type: Forum
        url: https://forum.snapcraft.io/
  - name: Ubuntu Archive API
    description: Access to Ubuntu package repositories and archive information via the Launchpad API's Ubuntu distribution endpoint.
    humanURL: https://archive.ubuntu.com/
    baseURL: https://api.launchpad.net/devel/ubuntu
    tags:
      - Archives
      - Packages
      - Releases
      - Repositories
    properties:
      - type: Documentation
        url: https://wiki.ubuntu.com/ArchiveAdministration
      - type: Package Search
        url: https://packages.ubuntu.com/
  - name: Landscape API
    description: Systems management API for Ubuntu servers enabling automated patch management, compliance reporting, and fleet monitoring for Ubuntu deployments.
    humanURL: https://ubuntu.com/landscape
    baseURL: https://landscape.canonical.com/api/
    tags:
      - Automation
      - Management
      - Monitoring
      - Servers
    properties:
      - type: Documentation
        url: https://ubuntu.com/landscape/docs/api
      - type: Authentication
        url: https://ubuntu.com/landscape/docs/api-authentication
    contact:
      - type: Support
        url: https://ubuntu.com/landscape/contact-us
  - name: MAAS API
    description: Metal as a Service API for physical server provisioning, enabling automated bare-metal infrastructure management and cloud-like workflows.
    humanURL: https://maas.io/
    baseURL: https://maas.io/docs/api
    tags:
      - Bare-Metal
      - Cloud
      - Infrastructure
      - Provisioning
    properties:
      - type: Documentation
        url: https://maas.io/docs/api
      - type: GitHub
        url: https://github.com/canonical/maas
    contact:
      - type: Discourse
        url: https://discourse.maas.io/
  - name: Juju API
    description: Application modeling and deployment API supporting automated deployment, scaling, and management of applications across clouds and bare metal.
    humanURL: https://juju.is/
    baseURL: wss://[controller-address]:17070/api
    tags:
      - Automation
      - Deployment
      - Devops
      - Orchestration
    properties:
      - type: Documentation
        url: https://juju.is/docs/juju/api
      - type: GitHub
        url: https://github.com/juju/juju
    contact:
      - type: Discourse
        url: https://discourse.charmhub.io/
  - name: Ubuntu CVE API
    description: API for Ubuntu security notices and CVE vulnerability information, enabling programmatic queries of the Ubuntu CVE database including affected packages and patch status across Ubuntu releases.
    humanURL: https://ubuntu.com/security/cves
    baseURL: https://ubuntu.com/security
    tags:
      - Cve
      - Patches
      - Security
      - Vulnerabilities
    properties:
      - type: Documentation
        url: https://ubuntu.com/security/api
      - type: RSS
        url: https://ubuntu.com/security/notices/rss.xml
      - type: OpenAPI
        url: openapi/ubuntu-cve-openapi.yml
      - type: Example
        url: examples/ubuntu-cve-list-example.json
      - type: JSONSchema
        url: json-schema/ubuntu-cve-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Cloud
  - Containers
  - Devops
  - Enterprise
  - Linux
  - Security
  - Ubuntu
  - Package Management
  - Open Source
properties:
  - url: rules/ubuntu-rules.yml
    type: SpectralRules
  - url: vocabulary/ubuntu-vocabulary.yml
    type: Vocabulary
  - url: json-ld/ubuntu-context.jsonld
    type: JSONLDContext
  - url: capabilities/package-and-security-management.yaml
    type: NaftikoCapabilities
specificationVersion: '0.19'
---
