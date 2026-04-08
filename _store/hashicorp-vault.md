---
aid: hashicorp-vault
url: https://raw.githubusercontent.com/api-evangelist/hashicorp-vault/refs/heads/main/apis.yml
apis:
- aid: hashicorp-vault:vault-http-api
  name: HashiCorp Vault HTTP API
  description: The Vault HTTP API provides full access to Vault via HTTP. Every aspect of Vault can be controlled via this API. The Vault CLI uses the HTTP API to access Vault functionality.
  humanURL: https://developer.hashicorp.com/vault/api-docs
  baseURL: https://127.0.0.1:8200/v1
  tags:
  - Encryption
  - Secrets Management
  - Security
  properties:
  - type: Documentation
    url: https://developer.hashicorp.com/vault/api-docs
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/hashicorp-vault/refs/heads/main/openapi/vault-http-api.yml
  - type: Authentication
    url: https://developer.hashicorp.com/vault/docs/auth
  - type: Getting Started
    url: https://developer.hashicorp.com/vault/tutorials
name: HashiCorp Vault
tags:
- DevOps
- Encryption
- Infrastructure
- Secrets Management
- Security
type: Contract
image: https://www.datocms-assets.com/2885/1620155116-brandhcvaultprimaryattributedcolor.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: HashiCorp Vault is a secrets management tool that provides secure storage, access control, and distribution of tokens, passwords, certificates, and encryption keys. It provides a unified interface to any secret while providing tight access control and recording a detailed audit log.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

