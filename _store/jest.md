---
aid: jest
name: Jest
description: Jest is a delightful JavaScript testing framework with a focus on simplicity. It works with projects using Babel, TypeScript, Node, React, Angular, Vue and more. Jest provides snapshot testing, parallel execution, built-in mocking, and code coverage out of the box.
type: Index
image: https://jestjs.io/img/jest.png
tags:
  - JavaScript
  - Mocking
  - Snapshot Testing
  - Testing
  - Unit Testing
url: https://raw.githubusercontent.com/api-evangelist/jest/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - aid: jest:jest-core-api
    name: Jest Core API
    description: Core testing framework API for writing and running tests, including globals, expect assertions, mock functions, and configuration options.
    humanURL: https://jestjs.io/docs/api
    tags:
      - Assertions
      - Mocking
      - Testing
    properties:
      - type: Documentation
        url: https://jestjs.io/docs/getting-started
      - type: Reference
        url: https://jestjs.io/docs/api
  - aid: jest:jest-cli
    name: Jest CLI
    description: Command-line interface for running Jest tests with various options.
    humanURL: https://jestjs.io/docs/cli
    tags:
      - CLI
      - Command Line
    properties:
      - type: Documentation
        url: https://jestjs.io/docs/cli
  - aid: jest:jest-configuration
    name: Jest Configuration API
    description: Programmatic configuration options for customizing Jest behavior.
    humanURL: https://jestjs.io/docs/configuration
    tags:
      - Configuration
      - Setup
    properties:
      - type: Documentation
        url: https://jestjs.io/docs/configuration
common:
  - type: Website
    url: https://jestjs.io
  - type: Documentation
    url: https://jestjs.io/docs/getting-started
  - type: Blog
    url: https://jestjs.io/blog
  - type: GitHub Organization
    url: https://github.com/jestjs
  - type: Community
    url: https://discord.gg/j6FKKQQrW9
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
