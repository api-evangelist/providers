---
aid: openjs-foundation
name: OpenJS Foundation
description: The OpenJS Foundation is a Linux Foundation project that supports the growth of JavaScript and web technologies through open governance and collaboration. It hosts critical web ecosystem projects including Node.js, jQuery, Electron, webpack, ESLint, Express, Fastify, LoopBack, Appium, Mocha, Jest, and many more.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - JavaScript
  - Linux Foundation
  - Node.js
  - Web
  - API Frameworks
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openjs-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openjs-foundation:nodejs
    name: Node.js
    description: Node.js is a JavaScript runtime built on Chrome's V8 engine that powers server-side applications and tooling across the JavaScript ecosystem.
    humanURL: https://nodejs.org/
    tags:
      - Runtime
      - JavaScript
      - Server-side
    properties:
      - type: Documentation
        url: https://nodejs.org/en/docs/
      - type: GitHubRepository
        url: https://github.com/nodejs/node
  - aid: openjs-foundation:express
    name: Express
    description: Express is a fast, unopinionated, minimalist web framework for Node.js used for building HTTP APIs and web applications.
    humanURL: https://expressjs.com/
    tags:
      - Web Framework
      - HTTP
      - APIs
    properties:
      - type: Documentation
        url: https://expressjs.com/en/4x/api.html
      - type: GitHubRepository
        url: https://github.com/expressjs/express
  - aid: openjs-foundation:fastify
    name: Fastify
    description: Fastify is a fast, low-overhead web framework for Node.js with a strong plugin architecture and built-in JSON Schema validation.
    humanURL: https://fastify.dev/
    tags:
      - Web Framework
      - JSON Schema
      - APIs
    properties:
      - type: Documentation
        url: https://fastify.dev/docs/latest/
      - type: GitHubRepository
        url: https://github.com/fastify/fastify
  - aid: openjs-foundation:loopback
    name: LoopBack
    description: LoopBack is a highly extensible Node.js and TypeScript framework for building APIs and microservices with built-in OpenAPI support.
    humanURL: https://loopback.io/
    tags:
      - API Framework
      - TypeScript
      - OpenAPI
    properties:
      - type: Documentation
        url: https://loopback.io/doc/
      - type: GitHubRepository
        url: https://github.com/loopbackio/loopback-next
  - aid: openjs-foundation:electron
    name: Electron
    description: Electron is a framework for building cross-platform desktop applications with web technologies (Chromium and Node.js).
    humanURL: https://www.electronjs.org/
    tags:
      - Desktop
      - Cross-platform
    properties:
      - type: Documentation
        url: https://www.electronjs.org/docs/latest
      - type: GitHubRepository
        url: https://github.com/electron/electron
  - aid: openjs-foundation:appium
    name: Appium
    description: Appium is an open source automation framework for native, hybrid, and mobile web applications, exposing a WebDriver-compatible HTTP API.
    humanURL: https://appium.io/
    tags:
      - Test Automation
      - WebDriver
      - Mobile
    properties:
      - type: Documentation
        url: https://appium.io/docs/
      - type: GitHubRepository
        url: https://github.com/appium/appium
common:
  - type: Website
    name: OpenJS Foundation
    url: https://openjsf.org/
  - type: Documentation
    name: OpenJS Projects
    url: https://openjsf.org/projects
  - type: GitHubOrg
    name: OpenJS Foundation GitHub
    url: https://github.com/openjs-foundation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
