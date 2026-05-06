---
name: HashiCorp Vault
description: HashiCorp Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing. Vault handles leasing, key revocation, key rolling, and auditing. Through a unified API, users can access an encrypted Key/Value store and network encryption-as-a-service, or generate AWS IAM/STS credentials, SQL/NoSQL databases, X.509 certificates, SSH credentials, and more.
image: https://www.vaultproject.io/img/logo-hashicorp.svg
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.16'
tags:
  - Encryption
  - Identity
  - Infrastructure
  - Secrets Management
  - Security
url: https://www.vaultproject.io/api-docs
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: X-website
    url: https://www.vaultproject.io/
  - type: X-documentation
    url: https://developer.hashicorp.com/vault/docs
  - type: X-api-documentation
    url: https://developer.hashicorp.com/vault/api-docs
  - type: X-github
    url: https://github.com/hashicorp/vault
  - type: X-tutorials
    url: https://developer.hashicorp.com/vault/tutorials
  - type: X-support
    url: https://support.hashicorp.com/
  - type: X-terms-of-service
    url: https://www.hashicorp.com/terms-of-service
  - type: X-privacy-policy
    url: https://www.hashicorp.com/privacy
  - type: X-pricing
    url: https://www.hashicorp.com/products/vault/pricing
  - type: X-blog
    url: https://www.hashicorp.com/blog
  - type: X-status
    url: https://status.hashicorp.com/
  - type: JSON-LD
    url: json-ld/hvault-context.jsonld
  - type: JSONSchema
    url: json-schema/hvault-secret-schema.json
  - type: JSONSchema
    url: json-schema/hvault-entity-schema.json
  - type: JSONSchema
    url: json-schema/hvault-entity-alias-schema.json
  - type: JSONSchema
    url: json-schema/hvault-token-schema.json
  - type: JSONSchema
    url: json-schema/hvault-policy-schema.json
  - type: JSONSchema
    url: json-schema/hvault-group-schema.json
include:
  - name: Vault Client Libraries
    url: https://developer.hashicorp.com/vault/api-docs/libraries
---
