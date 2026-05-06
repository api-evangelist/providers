---
aid: npm
name: npm
description: npm is the world's largest software registry, hosting over two million JavaScript packages for the Node.js ecosystem. Their developer platform provides APIs for searching and retrieving package metadata, managing access tokens, subscribing to registry event webhooks, and publishing packages with supply chain provenance verification.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Packages
  - JavaScript
  - Node.js
  - Package Management
  - Registry
  - Security
url: https://raw.githubusercontent.com/api-evangelist/npm/refs/heads/main/apis.yml
created: '2026-03-20'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: npm:registry
    name: npm Registry API
    description: The npm Registry API provides programmatic access to the npm package registry, the largest software registry in the world hosting over two million JavaScript packages. Developers can query package metadata, download tarballs, search for packages, and retrieve version-specific information. The API follows CouchDB-based conventions and serves package manifests in JSON format, enabling tools and services to integrate with the npm ecosystem for dependency resolution, package discovery, and automated workflows.
    humanURL: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md
    baseURL: https://registry.npmjs.org
    tags:
      - Packages
      - JavaScript
      - Registry
      - Package Management
      - Node.js
    properties:
      - type: Documentation
        url: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md
      - type: OpenAPI
        url: openapi/npm-registry-api-openapi.yml
      - type: JSONSchema
        url: json-schema/npm-package-schema.json
  - aid: npm:public
    name: npm Public API
    description: The npm Public API provides authenticated endpoints for managing npm access tokens, configuring trusted publishers, and exchanging OIDC tokens for short-lived registry access. It supports creating, listing, and deleting npm access tokens with customizable permissions, scope restrictions, expiration settings, and CIDR IP range limitations. The API also enables CI/CD providers like GitHub Actions, GitLab CI, and CircleCI to publish packages securely through OIDC token exchange without requiring long-lived npm tokens.
    humanURL: https://api-docs.npmjs.com/
    baseURL: https://npm.pkg.github.com
    tags:
      - Packages
      - Tokens
      - Authentication
      - Security
      - OIDC
      - Access Control
    properties:
      - type: Documentation
        url: https://api-docs.npmjs.com/
      - type: OpenAPI
        url: openapi/npm-public-api-openapi.yml
  - aid: npm:hooks
    name: npm Hooks API
    description: The npm Hooks API allows developers to subscribe to notifications about changes in the npm registry. Hooks send HTTP POST payloads to a configured URI whenever a package is changed, enabling developers to build integrations that respond to registry events in real time. Users can add hooks to follow specific packages, track all activity of given npm users, or monitor all packages within an organization or user scope. The API provides endpoints for creating, listing, updating, and deleting hook subscriptions.
    humanURL: https://blog.npmjs.org/post/145260155635/introducing-hooks-get-notifications-of-npm
    tags:
      - Webhooks
      - Notifications
      - Events
      - Automation
      - Packages
    properties:
      - type: Documentation
        url: https://blog.npmjs.org/post/145260155635/introducing-hooks-get-notifications-of-npm
      - type: OpenAPI
        url: openapi/npm-hooks-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/npm-hooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/npm-hook-event-schema.json
  - aid: npm:cli
    name: npm CLI
    description: The npm CLI is the official command-line interface for the npm package manager, providing developers with tools to install, publish, and manage JavaScript packages and their dependencies. It supports package publishing with provenance attestation via Sigstore, workspace management for monorepos, script execution, semantic versioning, and comprehensive dependency tree management. The CLI is bundled with Node.js and serves as the primary developer interface for interacting with the npm registry.
    humanURL: https://docs.npmjs.com/cli
    tags:
      - Command Line
      - Package Management
      - JavaScript
      - Node.js
      - Developer Tools
    properties:
      - type: Documentation
        url: https://docs.npmjs.com/cli
      - type: SourceCode
        url: https://github.com/npm/cli
  - aid: npm:provenance
    name: npm Provenance
    description: npm Provenance provides supply chain security for JavaScript packages by establishing a verifiable link between a published package and its source code repository and build environment. When a package is published with provenance, it is signed using Sigstore public good servers and the attestation is logged in a public transparency ledger. This allows developers to verify where and how a package was built before downloading it, helping to protect against supply chain attacks and ensuring the integrity of the npm ecosystem.
    humanURL: https://docs.npmjs.com/generating-provenance-statements
    tags:
      - Security
      - Supply Chain
      - Verification
      - Sigstore
      - Transparency
      - CI/CD
    properties:
      - type: Documentation
        url: https://docs.npmjs.com/generating-provenance-statements
      - type: Documentation
        url: https://github.blog/security/supply-chain-security/introducing-npm-package-provenance/
common:
  - url: https://www.npmjs.com/
    name: npm Portal
    type: Portal
  - url: https://docs.npmjs.com/
    name: npm Documentation
    type: Documentation
  - url: https://blog.npmjs.org/
    name: npm Blog
    type: Blog
  - url: https://www.npmjs.com/login
    name: Login
    type: Login
  - url: https://www.npmjs.com/support
    name: Support
    type: Support
  - url: https://docs.npmjs.com/policies/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://docs.npmjs.com/policies/terms
    name: Terms of Service
    type: TermsOfService
  - url: https://www.npmjs.com/
    name: Website
    type: Website
  - url: https://github.com/npm
    name: GitHub Organization
    type: GitHubOrg
  - url: https://status.npmjs.org/
    name: Status
    type: StatusPage
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
