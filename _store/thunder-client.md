---
aid: thunder-client
name: Thunder Client
description: Thunder Client is a lightweight REST API client extension for Visual Studio Code created by Ranga Vadhineni, providing a clean interface for sending HTTP requests, managing collections, and testing APIs without leaving the editor. With nearly 7 million installs, it pioneered GUI-based API testing in VS Code with 100% local storage, scriptless testing, Git Sync for team collaboration, GraphQL support, and an advanced CLI for CI/CD integration. Thunder Client supports importing collections from Postman, Insomnia, Hoppscotch, and OpenAPI 3.0, and offers pre/post-request scripting and environment variables.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Client
  - API Testing
  - CI/CD
  - CLI
  - Collections
  - GraphQL
  - REST Client
  - VS Code
url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: thunder-client:thunder-client
    name: Thunder Client
    description: Thunder Client is the flagship VS Code REST API client extension offering a lightweight GUI for sending HTTP requests, managing collections with environment variables, and running scriptless tests. Features include Git Sync for team collaboration, GraphQL support, pre/post request scripting, collection import from Postman/Insomnia/Hoppscotch/OpenAPI, and an advanced CLI supporting CI/CD pipelines.
    humanURL: https://www.thunderclient.com
    baseURL: https://www.thunderclient.com
    tags:
      - API Client
      - API Testing
      - Collections
      - GraphQL
      - REST Client
      - VS Code
    properties:
      - type: Documentation
        url: https://docs.thunderclient.com/
      - type: Getting Started
        url: https://docs.thunderclient.com/get-started
      - type: GitHub
        url: https://github.com/thunderclient/thunder-client-support
      - type: VS Code Marketplace
        url: https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
      - type: Pricing
        url: https://www.thunderclient.com/pricing
      - type: CLI Documentation
        url: https://docs.thunderclient.com/cli
      - type: Scripting API Reference
        url: https://docs.thunderclient.com/scripting/api
      - type: Changelog
        url: https://github.com/thunderclient/thunder-client-support/releases
      - type: npm
        url: https://www.npmjs.com/package/@thunderclient/cli
    contact:
      - FN: Thunder Client Support
        url: https://github.com/thunderclient/thunder-client-support
    version: 2.40.10
  - aid: thunder-client:thunder-client-cli
    name: Thunder Client CLI
    description: The Thunder Client CLI (@thunderclient/cli) is a Node.js command-line tool for running Thunder Client requests, collections, and cURL commands from the terminal. It supports CI/CD integration, parallel execution, and multiple report formats (CLI, CSV, HTML, JSON, XML, NUnit). Installed globally via npm (npm i -g @thunderclient/cli).
    humanURL: https://docs.thunderclient.com/cli
    baseURL: https://docs.thunderclient.com/cli
    tags:
      - API Testing
      - CI/CD
      - CLI
      - Collections
      - Node.js
    properties:
      - type: Documentation
        url: https://docs.thunderclient.com/cli
      - type: CLI Install
        url: https://docs.thunderclient.com/cli/install
      - type: Run Requests
        url: https://docs.thunderclient.com/cli/run-requests
      - type: Run Collection
        url: https://docs.thunderclient.com/cli/run-collection
      - type: cURL Commands
        url: https://docs.thunderclient.com/cli/curl
      - type: CI/CD Integration
        url: https://docs.thunderclient.com/cli/ci-cd
      - type: List Command
        url: https://docs.thunderclient.com/cli/list
      - type: npm
        url: https://www.npmjs.com/package/@thunderclient/cli
common:
  - type: Website
    url: https://www.thunderclient.com
  - type: Documentation
    url: https://docs.thunderclient.com/
  - type: GitHub
    url: https://github.com/thunderclient/thunder-client-support
  - type: VS Code Marketplace
    url: https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
  - type: Pricing
    url: https://www.thunderclient.com/pricing
  - type: npm
    url: https://www.npmjs.com/package/@thunderclient/cli
  - type: Changelog
    url: https://github.com/thunderclient/thunder-client-support/releases
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-schema/thunder-client-collection-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-schema/thunder-client-environment-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-structure/thunder-client-collection-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-ld/thunder-client-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/vocabulary/thunder-client-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
