---
aid: hashicorp-vault
name: HashiCorp Vault
description: HashiCorp Vault is a secrets management tool that provides secure storage, access control, and distribution of tokens, passwords, certificates, and encryption keys. It provides a unified interface to any secret while providing tight access control and recording a detailed audit log.
image: https://www.datocms-assets.com/2885/1620155116-brandhcvaultprimaryattributedcolor.svg
url: https://raw.githubusercontent.com/api-evangelist/hashicorp-vault/refs/heads/main/apis.yml
type: Index
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - DevOps
  - Encryption
  - Infrastructure
  - Secrets Management
  - Security
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
        url: https://raw.githubusercontent.com/api-evangelist/hashicorp-vault/refs/heads/main/openapi/hashicorp-vault-openapi.yml
      - type: Authentication
        url: https://developer.hashicorp.com/vault/docs/auth
      - type: Getting Started
        url: https://developer.hashicorp.com/vault/tutorials
common:
  - type: Website
    url: https://www.vaultproject.io/
  - type: Documentation
    url: https://developer.hashicorp.com/vault/docs
  - type: Getting Started
    url: https://developer.hashicorp.com/vault/tutorials
  - type: Support
    url: https://support.hashicorp.com
  - type: Status
    url: https://status.hashicorp.com
  - type: Blog
    url: https://www.hashicorp.com/blog
  - type: Pricing
    url: https://www.hashicorp.com/products/vault/pricing
  - type: Terms of Service
    url: https://www.hashicorp.com/terms-of-service
  - type: Privacy Policy
    url: https://www.hashicorp.com/privacy
  - type: GitHub Organization
    url: https://github.com/hashicorp/vault
  - type: SDKs
    url: https://developer.hashicorp.com/vault/docs/libraries
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
