---
aid: hvault
url: https://raw.githubusercontent.com/api-evangelist/hvault/refs/heads/main/apis.yml
apis:
- name: Vault System Backend API
  description: API for system-level operations including authentication, secrets engines, audit devices, and general Vault configuration.
  image: https://www.vaultproject.io/img/logo-hashicorp.svg
  humanURL: https://www.vaultproject.io/
  baseURL: https://vault.example.com/v1/sys
  tags:
  - Administration
  - Configuration
  - System
  properties:
  - type: Documentation
    url: https://developer.hashicorp.com/vault/api-docs/system
  - type: X-openapi
    url: https://github.com/hashicorp/vault/blob/main/openapi.json
  - type: Authentication
    url: https://developer.hashicorp.com/vault/docs/auth
  - type: OpenAPI
    url: openapi/hvault-system-backend-openapi.yml
  contact:
  - FN: HashiCorp Support
    email: support@hashicorp.com
    X-twitter: HashiCorp
- name: Vault Secrets Engines API
  description: APIs for various secrets engines including Key/Value, AWS, Azure, databases, PKI, SSH, and more.
  image: https://www.vaultproject.io/img/logo-hashicorp.svg
  humanURL: https://developer.hashicorp.com/vault/docs/secrets
  baseURL: https://vault.example.com/v1
  tags:
  - Cloud
  - Databases
  - Kv
  - Secrets
  properties:
  - type: Documentation
    url: https://developer.hashicorp.com/vault/api-docs/secret
  - type: X-kv-docs
    url: https://developer.hashicorp.com/vault/api-docs/secret/kv/kv-v2
  - type: X-aws-docs
    url: https://developer.hashicorp.com/vault/api-docs/secret/aws
  - type: X-database-docs
    url: https://developer.hashicorp.com/vault/api-docs/secret/databases
  - type: OpenAPI
    url: openapi/hvault-secrets-engines-openapi.yml
  contact:
  - FN: HashiCorp Support
    email: support@hashicorp.com
- name: Vault Auth Methods API
  description: APIs for authentication methods including Token, AppRole, Kubernetes, LDAP, JWT/OIDC, GitHub, and more.
  image: https://www.vaultproject.io/img/logo-hashicorp.svg
  humanURL: https://developer.hashicorp.com/vault/docs/auth
  baseURL: https://vault.example.com/v1/auth
  tags:
  - Access Control
  - Authentication
  - Identity
  properties:
  - type: Documentation
    url: https://developer.hashicorp.com/vault/api-docs/auth
  - type: X-token-docs
    url: https://developer.hashicorp.com/vault/api-docs/auth/token
  - type: X-approle-docs
    url: https://developer.hashicorp.com/vault/api-docs/auth/approle
  - type: X-kubernetes-docs
    url: https://developer.hashicorp.com/vault/api-docs/auth/kubernetes
  - type: OpenAPI
    url: openapi/hvault-auth-methods-openapi.yml
  contact:
  - FN: HashiCorp Support
    email: support@hashicorp.com
- name: Vault Identity API
  description: APIs for managing entities, entity aliases, and groups for identity management across authentication methods.
  image: https://www.vaultproject.io/img/logo-hashicorp.svg
  humanURL: https://developer.hashicorp.com/vault/docs/secrets/identity
  baseURL: https://vault.example.com/v1/identity
  tags:
  - Entities
  - Groups
  - Identity
  properties:
  - type: Documentation
    url: https://developer.hashicorp.com/vault/api-docs/secret/identity
  - type: OpenAPI
    url: openapi/hvault-identity-openapi.yml
  contact:
  - FN: HashiCorp Support
    email: support@hashicorp.com
name: HashiCorp Vault
tags:
- Encryption
- Identity
- Infrastructure
- Secrets Management
- Security
type: Contract
image: https://www.vaultproject.io/img/logo-hashicorp.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: HashiCorp Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing. Vault handles leasing, key revocation, key rolling, and auditing. Through a unified API, users can access an encrypted Key/Value store and network encryption-as-a-service, or generate AWS IAM/STS credentials, SQL/NoSQL databases, X.509 certificates, SSH credentials, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

