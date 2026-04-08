---
aid: eclipse
url: https://raw.githubusercontent.com/api-evangelist/eclipse/refs/heads/main/apis.yml
apis:
- name: Eclipse Marketplace API
  description: API for accessing Eclipse Marketplace data including listings, favorites, and installation statistics.
  image: https://marketplace.eclipse.org/sites/all/themes/solstice/public/images/logo/eclipse-foundation-grey-orange.svg
  humanURL: https://marketplace.eclipse.org/
  baseURL: https://marketplace.eclipse.org/api/p
  tags:
  - Extensions
  - Marketplace
  - Plugins
  properties:
  - type: Documentation
    url: https://wiki.eclipse.org/Marketplace/REST
  - type: OpenAPI
    url: https://marketplace.eclipse.org/api-docs
  - type: Authentication
    url: https://wiki.eclipse.org/Marketplace/REST#Authentication
  contact:
  - type: Support
    url: https://www.eclipse.org/org/support/
- name: Eclipse JGit API
  description: Java implementation of the Git version control system API.
  humanURL: https://www.eclipse.org/jgit/
  baseURL: https://download.eclipse.org/jgit/
  tags:
  - Git
  - Java
  - Version-Control
  properties:
  - type: Documentation
    url: https://wiki.eclipse.org/JGit/User_Guide
  - type: GitHub
    url: https://github.com/eclipse-jgit/jgit
  - type: JavaDoc
    url: https://download.eclipse.org/jgit/site/latest/apidocs/
- name: Eclipse IoT API
  description: APIs for IoT protocols and device management including MQTT, CoAP, and LWM2M.
  humanURL: https://iot.eclipse.org/
  baseURL: https://iot.eclipse.org/
  tags:
  - Coap
  - Devices
  - Iot
  - Mqtt
  properties:
  - type: Documentation
    url: https://iot.eclipse.org/getting-started
  - type: GitHub
    url: https://github.com/eclipse
- name: Eclipse Foundation Web API
  description: API for accessing Eclipse Foundation project data, releases, and metadata.
  humanURL: https://api.eclipse.org/
  baseURL: https://api.eclipse.org/
  tags:
  - Metadata
  - Projects
  - Releases
  properties:
  - type: Documentation
    url: https://api.eclipse.org/
  - type: OpenAPI
    url: https://api.eclipse.org/swagger-ui/
name: Eclipse Foundation
tags:
- API
type: Contract
image: https://www.eclipse.org/eclipse.org-common/themes/solstice/public/images/logo/eclipse-foundation-grey-orange.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and services provided by the Eclipse Foundation and its projects.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

