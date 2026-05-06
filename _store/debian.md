---
aid: debian
name: Debian
url: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/apis.yml
type: Index
position: Provider
access: Public
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bug Tracker
  - Debian
  - Linux
  - Open Source
  - Operating System
  - Package Management
  - Source Code
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: opensource
description: Debian is a free operating system distribution maintained by the Debian Project, a community of more than a thousand volunteers worldwide. Debian provides a number of developer-facing services including a source-code browsing API at sources.debian.org, the Bug Tracking System (BTS) at bugs.debian.org, and the Ultimate Debian Database (UDD) - a single Postgres database aggregating package, bug, Lintian, popcon, and reproducibility data for cross-cutting queries.
apis:
  - aid: debian:debian-sources-api
    name: Debian Sources API
    description: The Debian Sources API at sources.debian.org provides programmatic access to source code, package metadata, copyright records, and Debian patches for every source package in the archive.
    humanURL: https://sources.debian.org/doc/api/
    baseURL: https://sources.debian.org/api
    tags:
      - Copyright
      - Packages
      - Patches
      - Source Code
    properties:
      - type: Documentation
        url: https://sources.debian.org/doc/api/
      - type: OpenAPI
        url: openapi/debian-sources-api-openapi.yml
      - type: JSONSchema
        url: json-schema/debian-package.json
      - type: Rules
        url: rules/debian-sources-api-rules.yml
      - type: Capabilities
        url: capabilities/debian-sources-api-capabilities.yml
  - aid: debian:debian-bts-api
    name: Debian Bug Tracking System
    description: The Debian BTS at bugs.debian.org tracks bugs against packages and pseudo-packages. Bug reports are accessible as machine-readable mbox files and structured CGI views, with email serving as the canonical interaction surface.
    humanURL: https://www.debian.org/Bugs/
    baseURL: https://bugs.debian.org
    tags:
      - Bugs
      - Maintainers
      - Severity
    properties:
      - type: Documentation
        url: https://www.debian.org/Bugs/
      - type: OpenAPI
        url: openapi/debian-bts-api-openapi.yml
      - type: JSONSchema
        url: json-schema/debian-bug.json
  - aid: debian:debian-udd
    name: Debian Ultimate Database (UDD)
    description: The Ultimate Debian Database aggregates Debian-wide data into a single Postgres database and exposes web tools for bugs, maintainer dashboards, Lintian results, reproducibility, and more.
    humanURL: https://wiki.debian.org/UltimateDebianDatabase
    baseURL: https://udd.debian.org
    tags:
      - Aggregated Data
      - Lintian
      - Reproducibility
      - SQL
    properties:
      - type: Documentation
        url: https://wiki.debian.org/UltimateDebianDatabase
      - type: OpenAPI
        url: openapi/debian-udd-api-openapi.yml
common:
  - type: Website
    url: https://www.debian.org/
  - type: Wiki
    url: https://wiki.debian.org/
  - type: Documentation
    url: https://www.debian.org/doc/
  - type: GitLab
    url: https://salsa.debian.org/
  - type: Mailing Lists
    url: https://lists.debian.org/
  - type: Privacy Policy
    url: https://www.debian.org/legal/privacy
  - type: License
    url: https://www.debian.org/social_contract
  - type: JSON-LD
    url: json-ld/debian-context.jsonld
  - type: Vocabulary
    url: vocabulary/debian-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
