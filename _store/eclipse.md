---
aid: eclipse
name: Eclipse Foundation
description: The Eclipse Foundation provides a global community of individuals and organizations with a mature, scalable, and business-friendly environment for open source software collaboration and innovation. This index aggregates the developer-facing APIs and services published by the Eclipse Foundation and its working groups.
type: Index
image: https://www.eclipse.org/eclipse.org-common/themes/solstice/public/images/logo/eclipse-foundation-grey-orange.svg
url: https://raw.githubusercontent.com/api-evangelist/eclipse/refs/heads/main/apis.yml
tags:
  - Eclipse Foundation
  - Foundation
  - Open Source
  - Standards
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: eclipse:marketplace-api
    name: Eclipse Marketplace API
    description: REST API for accessing Eclipse Marketplace data including listings, categories, favorites, and installation statistics for plugins, IDEs, and other extensions.
    image: https://marketplace.eclipse.org/sites/all/themes/solstice/public/images/logo/eclipse-foundation-grey-orange.svg
    humanURL: https://marketplace.eclipse.org/
    baseURL: https://marketplace.eclipse.org/api/p
    tags:
      - Extensions
      - IDE
      - Marketplace
      - Plugins
    properties:
      - type: Documentation
        url: https://wiki.eclipse.org/Marketplace/REST
      - type: Authentication
        url: https://wiki.eclipse.org/Marketplace/REST#Authentication
  - aid: eclipse:foundation-web-api
    name: Eclipse Foundation Web API
    description: Foundation-wide REST APIs for accessing project data, releases, committer paperwork, GeoIP, downloads, mailing lists, profiles, working groups, and other Eclipse Foundation services. Index of available APIs at webdev.eclipse.org/docs/api.
    humanURL: https://api.eclipse.org/
    baseURL: https://api.eclipse.org/
    tags:
      - Foundation
      - Metadata
      - Projects
      - Releases
    properties:
      - type: Documentation
        url: https://webdev.eclipse.org/docs/api/
      - type: Portal
        url: https://api.eclipse.org/
  - aid: eclipse:projects-api
    name: Eclipse Projects API
    description: REST API exposing Eclipse Foundation project metadata, releases, committers, and project lifecycle data.
    humanURL: https://projects.eclipse.org/
    baseURL: https://projects.eclipse.org/api/
    tags:
      - Metadata
      - Projects
      - Releases
    properties:
      - type: Documentation
        url: https://www.eclipse.org/projects/handbook/
  - aid: eclipse:open-vsx-api
    name: Open VSX Registry API
    description: REST API for the Eclipse Open VSX Registry, an open-source alternative to the Visual Studio Marketplace for distributing VS Code-compatible extensions.
    humanURL: https://open-vsx.org/
    baseURL: https://open-vsx.org/api
    tags:
      - Extensions
      - Open Source
      - Registry
      - VS Code
    properties:
      - type: Documentation
        url: https://github.com/eclipse/openvsx/wiki/Publishing-Extensions
      - type: GitHub
        url: https://github.com/eclipse/openvsx
  - aid: eclipse:newsroom-api
    name: Eclipse Newsroom REST API
    description: REST API providing access to news, events, and announcements from the Eclipse Foundation newsroom.
    humanURL: https://newsroom.eclipse.org/
    baseURL: https://newsroom.eclipse.org/api/
    tags:
      - Events
      - News
      - Newsroom
    properties:
      - type: Documentation
        url: https://webdev.eclipse.org/docs/api/
common:
  - type: Portal
    url: https://www.eclipse.org/
  - type: API Documentation Index
    url: https://webdev.eclipse.org/docs/api/
  - type: Blog
    url: https://blogs.eclipse.org/
  - type: News
    url: https://newsroom.eclipse.org/
  - type: GitHub Organization
    url: https://github.com/eclipse
  - type: Terms of Service
    url: https://www.eclipse.org/legal/termsofuse.php
  - type: Privacy Policy
    url: https://www.eclipse.org/legal/privacy.php
  - type: License
    url: https://www.eclipse.org/legal/epl-2.0/
maintainers:
  - FN: Eclipse Foundation
    email: webmaster@eclipse.org
    url: https://www.eclipse.org/org/foundation/contact.php
---
