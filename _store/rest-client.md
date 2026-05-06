---
aid: rest-client
name: REST Client
description: REST Client is a Visual Studio Code extension developed by Huachao Mao that enables developers to send HTTP requests and view responses directly within the VS Code editor. It supports RFC 2616 HTTP request format using .http and .rest files, GraphQL queries, cURL commands, multiple authentication schemes (Basic, Digest, SSL Client Certificates, Azure AD, AWS Signature v4, AWS Cognito), environment and file variables, request chaining, cookie management, code generation to multiple languages, and response saving. The extension is installed via the VS Code Marketplace under the identifier humao.rest-client and is widely used as a lightweight alternative to dedicated API clients like Postman and Insomnia.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Clients
  - HTTP Client
  - IDE Extension
  - VS Code
  - API Testing
url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rest-client:rest-client
    name: REST Client
    description: REST Client is a Visual Studio Code extension for sending HTTP requests and viewing responses directly within the editor. It supports .http and .rest file formats, GraphQL, cURL, multiple auth schemes, environment variables, request chaining, and code generation.
    humanURL: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
    tags:
      - Clients
      - HTTP Client
      - IDE Extension
      - VS Code
      - API Testing
      - GraphQL
      - cURL
    properties:
      - type: Documentation
        url: https://github.com/Huachao/vscode-restclient#readme
      - type: Getting Started
        url: https://github.com/Huachao/vscode-restclient#usage
      - type: GitHub Repository
        url: https://github.com/Huachao/vscode-restclient
      - type: VS Code Marketplace
        url: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
      - type: Changelog
        url: https://github.com/Huachao/vscode-restclient/blob/master/CHANGELOG.md
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/json-schema/rest-client-request-schema.json
      - type: JSON Structure
        url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/json-structure/rest-client-request-structure.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/examples/rest-client-get-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/examples/rest-client-request-chaining-example.json
common:
  - type: Website
    url: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
  - type: Documentation
    url: https://github.com/Huachao/vscode-restclient#readme
  - type: GitHub Organization
    url: https://github.com/Huachao/vscode-restclient
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/vocabulary/rest-client-vocabulary.yml
  - type: JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/json-ld/rest-client-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
