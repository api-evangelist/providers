---
name: Azure Key Vault
description: Azure Key Vault is a cloud service for securely storing and accessing secrets, keys, and certificates. It helps safeguard cryptographic keys and secrets used by cloud applications and services.
image: https://azure.microsoft.com/svghandler/key-vault/
tags:
  - Certificates
  - Cloud Security
  - Cryptography
  - Key Management
  - Secrets Management
  - Security
created: '2024'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/key-vault/
specificationVersion: '0.18'
apis:
  - name: Azure Key Vault API
    description: REST API for managing vaults, keys, secrets, and certificates in Azure Key Vault.
    image: https://azure.microsoft.com/svghandler/key-vault/
    humanURL: https://azure.microsoft.com/en-us/services/key-vault/
    baseURL: https://management.azure.com
    tags:
      - Certificates
      - Keys
      - Secrets
      - Vaults
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/key-vault/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/resource-manager/Microsoft.KeyVault/stable/2023-02-01/keyvault.json
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/key-vault/
      - type: GettingStarted
        url: https://docs.microsoft.com/en-us/azure/key-vault/general/overview
      - type: Authentication
        url: https://docs.microsoft.com/en-us/azure/key-vault/general/authentication
      - type: BestPractices
        url: https://docs.microsoft.com/en-us/azure/key-vault/general/best-practices
      - type: Security
        url: https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: Azure Key Vault Data Plane API
    description: API for performing cryptographic operations and managing keys, secrets, and certificates within a specific Key Vault instance.
    image: https://azure.microsoft.com/svghandler/key-vault/
    humanURL: https://docs.microsoft.com/en-us/rest/api/keyvault/
    baseURL: https://{vault-name}.vault.azure.net
    tags:
      - Certificate Operations
      - Cryptographic Operations
      - Key Operations
      - Secret Operations
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/keyvault/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/keyvault/data-plane/Microsoft.KeyVault/stable/7.4/keyvault.json
      - type: OpenAPI
        url: openapi/azure-key-vault-data-plane-openapi.yml
      - type: APIReference
        url: https://docs.microsoft.com/en-us/rest/api/keyvault/keys
      - type: JSONSchema
        url: json-schema/azure-key-vault-secret-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-bundle-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-create-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-item-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-list-result-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-operation-result-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-operations-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-sign-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-update-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-verify-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-verify-result-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-attributes-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-properties-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-release-policy-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-json-web-key-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-json-web-key-type-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-json-web-key-operation-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-json-web-key-curve-name-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-bundle-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-set-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-update-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-item-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-list-result-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-attributes-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-properties-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-secret-restore-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-backup-secret-result-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-bundle-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-create-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-import-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-update-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-item-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-list-result-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-attributes-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-operation-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-certificate-policy-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-issuer-parameters-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-lifetime-action-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-subject-alternative-names-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-x509-certificate-properties-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-deleted-key-bundle-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-deleted-secret-bundle-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-deleted-certificate-bundle-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-deletion-recovery-level-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-error-schema.json
      - type: JSONSchema
        url: json-schema/azure-key-vault-data-plane-key-vault-error-schema.json
      - type: JSONLD
        url: json-ld/azure-key-vault-context.jsonld
      - type: JSONLD
        url: json-ld/azure-key-vault-data-plane-context.jsonld
      - type: SDK
        url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/security.keyvault.keys-readme
        title: .NET SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/python/api/overview/azure/keyvault-keys-readme
        title: Python SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/java/api/overview/azure/security-keyvault-keys-readme
        title: Java SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/javascript/api/overview/azure/keyvault-keys-readme
        title: JavaScript SDK
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: Azure Key Vault Keys API
    description: REST API for creating, importing, updating, and performing cryptographic operations with keys in Azure Key Vault. Supports RSA, EC, and symmetric key types with operations including encrypt, decrypt, sign, verify, wrap, and unwrap.
    image: https://azure.microsoft.com/svghandler/key-vault/
    humanURL: https://learn.microsoft.com/en-us/rest/api/keyvault/keys
    baseURL: https://{vault-name}.vault.azure.net
    tags:
      - Cryptographic Operations
      - Encryption
      - HSM
      - Keys
      - Signing
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/key-vault/keys/about-keys
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/keyvault/keys
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/key-vault/keys/quick-create-net
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: Azure Key Vault Secrets API
    description: REST API for securely storing and managing secrets such as passwords, connection strings, and API keys in Azure Key Vault.
    image: https://azure.microsoft.com/svghandler/key-vault/
    humanURL: https://learn.microsoft.com/en-us/rest/api/keyvault/secrets
    baseURL: https://{vault-name}.vault.azure.net
    tags:
      - Connection Strings
      - Passwords
      - Secrets
      - Secure Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/keyvault/secrets
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-net
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: Azure Key Vault Certificates API
    description: REST API for creating, importing, managing, and renewing certificates in Azure Key Vault.
    image: https://azure.microsoft.com/svghandler/key-vault/
    humanURL: https://learn.microsoft.com/en-us/rest/api/keyvault/certificates
    baseURL: https://{vault-name}.vault.azure.net
    tags:
      - Certificate Authorities
      - Certificate Management
      - Certificates
      - SSL
      - TLS
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/key-vault/certificates/about-certificates
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/keyvault/certificates
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/key-vault/certificates/quick-create-net
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: StatusPage
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: ChangeLog
    url: https://docs.microsoft.com/en-us/azure/key-vault/general/whats-new
  - type: Portal
    url: https://portal.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/key-vault/
  - type: SpectralRules
    url: rules/azure-key-vault-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/azure-key-vault-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/secrets-and-keys.yaml
  - type: Features
    data:
      - name: Key Management
        description: Create, import, and manage cryptographic keys with support for RSA, EC, and symmetric key types.
      - name: Secrets Management
        description: Securely store and control access to passwords, connection strings, API keys, and other secrets.
      - name: Certificate Lifecycle
        description: Automate certificate creation, renewal, and management with certificate authority integration.
      - name: Cryptographic Operations
        description: Perform encrypt, decrypt, sign, verify, wrap, and unwrap operations using managed keys.
      - name: HSM-Backed Keys
        description: Use hardware security modules for FIPS 140-2 Level 2 validated key protection.
      - name: Soft Delete and Purge Protection
        description: Recover accidentally deleted vaults, keys, secrets, and certificates with configurable retention.
  - type: UseCases
    data:
      - name: Application Secret Management
        description: Centralize and secure application secrets with audited access and automatic rotation.
      - name: Data Encryption
        description: Encrypt data at rest and in transit using customer-managed keys stored in Key Vault.
      - name: TLS Certificate Management
        description: Automate TLS certificate provisioning and renewal for web applications and services.
      - name: Code and Document Signing
        description: Sign code, documents, and artifacts using keys stored securely in Key Vault.
  - type: Integrations
    data:
      - name: Azure App Service
        description: Reference Key Vault secrets and certificates directly from App Service configuration.
      - name: Azure Kubernetes Service
        description: Mount Key Vault secrets as volumes in AKS pods using the Secrets Store CSI Driver.
      - name: Azure DevOps
        description: Use Key Vault secrets in CI/CD pipelines for secure deployment automation.
      - name: Azure Disk Encryption
        description: Encrypt Azure VM disks using customer-managed keys stored in Key Vault.
      - name: Azure SQL Database
        description: Enable Transparent Data Encryption with customer-managed keys from Key Vault.
---
