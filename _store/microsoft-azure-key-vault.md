---
aid: microsoft-azure-key-vault
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-key-vault/refs/heads/main/apis.yml
apis:
- name: Azure Key Vault API
  description: REST API for managing vaults, keys, secrets, and certificates in Azure Key Vault.
  image: https://azure.microsoft.com/svghandler/key-vault/
  humanUrl: https://azure.microsoft.com/en-us/services/key-vault/
  baseUrl: https://management.azure.com
  tags:
  - Certificates
  - Keys
  - Secrets
  - Vaults
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/azure/key-vault/
  - type: X-openapi
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/resource-manager/Microsoft.KeyVault/stable/2023-02-01/keyvault.json
  - type: X-pricing
    url: https://azure.microsoft.com/en-us/pricing/details/key-vault/
  - type: X-getting-started
    url: https://docs.microsoft.com/en-us/azure/key-vault/general/overview
  - type: X-authentication
    url: https://docs.microsoft.com/en-us/azure/key-vault/general/authentication
  - type: X-best-practices
    url: https://docs.microsoft.com/en-us/azure/key-vault/general/best-practices
  - type: X-security
    url: https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault
  - type: X-rbac-guide
    url: https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide
  contact:
  - type: X-support
    url: https://azure.microsoft.com/en-us/support/
  - type: X-portal
    url: https://portal.azure.com/
- name: Azure Key Vault Data Plane API
  description: API for performing cryptographic operations and managing keys, secrets, and certificates within a specific Key Vault instance.
  image: https://azure.microsoft.com/svghandler/key-vault/
  humanUrl: https://docs.microsoft.com/en-us/rest/api/keyvault/
  baseUrl: https://{vault-name}.vault.azure.net
  tags:
  - Certificate Operations
  - Cryptographic Operations
  - Key Operations
  - Secret Operations
  properties:
  - type: X-documentation
    url: https://docs.microsoft.com/en-us/rest/api/keyvault/
  - type: X-openapi
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/data-plane/Microsoft.KeyVault/stable/7.4/keyvault.json
  - type: X-openapi-local
    url: openapi/azure-key-vault-data-plane-openapi.yml
  - type: X-json-schema
    url: json-schema/azure-key-vault-secret-schema.json
  - type: X-json-ld-context
    url: json-ld/azure-key-vault-context.jsonld
  - type: X-api-reference
    url: https://docs.microsoft.com/en-us/rest/api/keyvault/keys
  - type: X-sdk-dotnet
    url: https://docs.microsoft.com/en-us/dotnet/api/overview/azure/key-vault
  - type: X-sdk-python
    url: https://docs.microsoft.com/en-us/python/api/overview/azure/keyvault-keys-readme
  - type: X-sdk-java
    url: https://docs.microsoft.com/en-us/java/api/overview/azure/security-keyvault-keys-readme
  - type: X-sdk-javascript
    url: https://docs.microsoft.com/en-us/javascript/api/overview/azure/keyvault-keys-readme
  - type: X-authentication
    url: https://learn.microsoft.com/en-us/azure/key-vault/general/authentication-requests-and-responses
- name: Azure Key Vault Keys API
  description: REST API for creating, importing, updating, and performing cryptographic operations with keys in Azure Key Vault. Supports RSA, EC, and symmetric key types with operations including encrypt, decrypt, sign, verify, wrap, and unwrap.
  image: https://azure.microsoft.com/svghandler/key-vault/
  humanUrl: https://learn.microsoft.com/en-us/rest/api/keyvault/keys
  baseUrl: https://{vault-name}.vault.azure.net
  tags:
  - Cryptographic Operations
  - Encryption
  - HSM
  - Keys
  - Signing
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/azure/key-vault/keys/about-keys
  - type: X-openapi
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/data-plane/Microsoft.KeyVault/stable/7.5/keys.json
  - type: X-openapi-local
    url: openapi/azure-key-vault-data-plane-openapi.yml
  - type: X-json-ld-context
    url: json-ld/azure-key-vault-context.jsonld
  - type: X-api-reference
    url: https://learn.microsoft.com/en-us/rest/api/keyvault/keys
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/azure/key-vault/keys/quick-create-net
  - type: X-sdk-dotnet
    url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/security.keyvault.keys-readme
  - type: X-sdk-python
    url: https://learn.microsoft.com/en-us/python/api/overview/azure/keyvault-keys-readme
  - type: X-sdk-java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/security-keyvault-keys-readme
  - type: X-sdk-javascript
    url: https://learn.microsoft.com/en-us/javascript/api/overview/azure/keyvault-keys-readme
  contact:
  - type: X-support
    url: https://azure.microsoft.com/en-us/support/
- name: Azure Key Vault Secrets API
  description: REST API for securely storing and managing secrets such as passwords, connection strings, and API keys in Azure Key Vault. Supports operations including set, get, update, delete, backup, restore, and list secrets.
  image: https://azure.microsoft.com/svghandler/key-vault/
  humanUrl: https://learn.microsoft.com/en-us/rest/api/keyvault/secrets
  baseUrl: https://{vault-name}.vault.azure.net
  tags:
  - Connection Strings
  - Passwords
  - Secrets
  - Secure Storage
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets
  - type: X-openapi
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/data-plane/Microsoft.KeyVault/stable/7.5/secrets.json
  - type: X-openapi-local
    url: openapi/azure-key-vault-data-plane-openapi.yml
  - type: X-json-schema
    url: json-schema/azure-key-vault-secret-schema.json
  - type: X-json-ld-context
    url: json-ld/azure-key-vault-context.jsonld
  - type: X-api-reference
    url: https://learn.microsoft.com/en-us/rest/api/keyvault/secrets
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-net
  - type: X-sdk-dotnet
    url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/security.keyvault.secrets-readme
  - type: X-sdk-python
    url: https://learn.microsoft.com/en-us/python/api/overview/azure/keyvault-secrets-readme
  - type: X-sdk-java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/security-keyvault-secrets-readme
  - type: X-sdk-javascript
    url: https://learn.microsoft.com/en-us/javascript/api/overview/azure/keyvault-secrets-readme
  contact:
  - type: X-support
    url: https://azure.microsoft.com/en-us/support/
- name: Azure Key Vault Certificates API
  description: REST API for creating, importing, managing, and renewing certificates in Azure Key Vault. Supports certificate lifecycle management including issuance, renewal, policy configuration, and integration with certificate authorities.
  image: https://azure.microsoft.com/svghandler/key-vault/
  humanUrl: https://learn.microsoft.com/en-us/rest/api/keyvault/certificates
  baseUrl: https://{vault-name}.vault.azure.net
  tags:
  - Certificate Authorities
  - Certificate Management
  - Certificates
  - SSL
  - TLS
  properties:
  - type: X-documentation
    url: https://learn.microsoft.com/en-us/azure/key-vault/certificates/about-certificates
  - type: X-openapi
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/data-plane/Microsoft.KeyVault/stable/7.5/certificates.json
  - type: X-openapi-local
    url: openapi/azure-key-vault-data-plane-openapi.yml
  - type: X-json-ld-context
    url: json-ld/azure-key-vault-context.jsonld
  - type: X-api-reference
    url: https://learn.microsoft.com/en-us/rest/api/keyvault/certificates
  - type: X-getting-started
    url: https://learn.microsoft.com/en-us/azure/key-vault/certificates/quick-create-net
  - type: X-access-control
    url: https://learn.microsoft.com/en-us/azure/key-vault/certificates/certificate-access-control
  - type: X-sdk-dotnet
    url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/security.keyvault.certificates-readme
  - type: X-sdk-python
    url: https://learn.microsoft.com/en-us/python/api/overview/azure/keyvault-certificates-readme
  - type: X-sdk-java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/security-keyvault-certificates-readme
  - type: X-sdk-javascript
    url: https://learn.microsoft.com/en-us/javascript/api/overview/azure/keyvault-certificates-readme
  contact:
  - type: X-support
    url: https://azure.microsoft.com/en-us/support/
name: Azure Key Vault
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
type: Contract
image: https://azure.microsoft.com/svghandler/key-vault/
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Key Vault is a cloud service for securely storing and accessing secrets, keys, and certificates. It helps safeguard cryptographic keys and secrets used by cloud applications and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

