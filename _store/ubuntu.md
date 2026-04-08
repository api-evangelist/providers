---
aid: ubuntu
url: https://raw.githubusercontent.com/api-evangelist/ubuntu/refs/heads/main/apis.yml
apis:
- name: Launchpad API
  description: REST API for Launchpad, Ubuntu's project hosting and collaboration platform.
  image: https://launchpad.net/@@/launchpad-logo
  humanURL: https://launchpad.net/
  baseURL: https://api.launchpad.net/
  tags:
  - Bugs
  - Collaboration
  - Distributions
  - Packages
  - Projects
  properties:
  - type: Documentation
    url: https://launchpad.net/+apidoc/
  - type: Authentication
    url: https://help.launchpad.net/API/Uses
  - type: Wadl
    url: https://api.launchpad.net/devel
  contact:
  - type: Support
    url: https://answers.launchpad.net/launchpad
- name: Ubuntu Pro API
  description: API for managing Ubuntu Pro subscriptions and entitlements.
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
  description: API for the Snap Store for publishing and managing snap packages.
  humanURL: https://snapcraft.io/
  baseURL: https://api.snapcraft.io/
  tags:
  - Applications
  - Distribution
  - Packages
  - Snaps
  properties:
  - type: Documentation
    url: https://snapcraft.io/docs/snapcraft-store-api
  - type: Dashboard
    url: https://snapcraft.io/account
  - type: Developer Portal
    url: https://snapcraft.io/docs
  contact:
  - type: Forum
    url: https://forum.snapcraft.io/
- name: Ubuntu Archive API
  description: Access to Ubuntu package repositories and archive information.
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
  description: Systems management API for Ubuntu servers.
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
  description: Metal as a Service API for physical server provisioning.
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
  description: Application modeling and deployment API.
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
  description: API for Ubuntu security notices and CVE information.
  humanURL: https://ubuntu.com/security/cves
  baseURL: https://ubuntu.com/security/cves.json
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
name: Ubuntu
tags:
- Cloud
- Containers
- Devops
- Enterprise
- Linux
- Security
- Ubuntu
type: Contract
image: https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs and services provided by Canonical for Ubuntu and related products.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

