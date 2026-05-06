---
aid: mockito
name: Mockito
description: Mockito is a popular open-source mocking framework for unit tests in Java. It lets developers write clean, readable tests by creating mock objects, stubbing their behavior, verifying interactions, and using simple, fluent APIs to keep test setup minimal and intent obvious.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mockito/refs/heads/main/apis.yml
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Java
  - Mocking
  - Testing
  - Unit Testing
  - Open Source
  - Framework
apis:
  - aid: mockito:mockito-core
    name: Mockito Core
    description: The core Mockito mocking framework for creating mock objects, stubbing methods, verifying invocations, and writing expressive unit tests in Java. Mockito Core is consumed as a Java library (Maven / Gradle artifact) rather than a network REST API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://site.mockito.org
    tags:
      - Java
      - Mocking
      - Testing
      - Library
    properties:
      - type: Documentation
        url: https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html
      - type: User Guide
        url: https://github.com/mockito/mockito/wiki
      - type: GitHub Repository
        url: https://github.com/mockito/mockito
      - type: Maven Central
        url: https://central.sonatype.com/artifact/org.mockito/mockito-core
common:
  - type: Website
    url: https://site.mockito.org
  - type: GitHub Organization
    url: https://github.com/mockito
  - type: Getting Started
    url: https://site.mockito.org/#how
  - type: Release Notes
    url: https://github.com/mockito/mockito/releases
  - type: Contributing Guide
    url: https://github.com/mockito/mockito/blob/main/.github/CONTRIBUTING.md
  - type: License
    url: https://github.com/mockito/mockito/blob/main/LICENSE
  - type: Code of Conduct
    url: https://github.com/mockito/mockito/blob/main/.github/CODE_OF_CONDUCT.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
