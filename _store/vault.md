---
aid: vault
url: https://raw.githubusercontent.com/api-evangelist/vault/refs/heads/main/apis.yml
apis:
- aid: vault:vault
  name: Vault API
  description: The Vault HTTP API gives you full access to Vault via HTTP. Every aspect of Vault can be controlled via this API.
  humanURL: https://developer.hashicorp.com/vault/api-docs
  baseURL: https://vault.example.com
  tags:
  - Secrets Management
  - Security
  properties:
  - type: Documentation
    url: https://developer.hashicorp.com/vault/api-docs
  - type: OpenAPI
    url: https://github.com/hashicorp/vault/blob/main/openapi.json
  - type: Authentication
    url: https://developer.hashicorp.com/vault/docs/auth
  - type: Getting Started
    url: https://developer.hashicorp.com/vault/docs/get-started
  - type: Change Log
    url: https://github.com/hashicorp/vault/blob/main/CHANGELOG.md
name: HashiCorp Vault
tags:
- Encryption
- Secrets Management
- Security
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

