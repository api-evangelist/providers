---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Microsoft Azure Key Vault Agentic Access
  operation_count: 29
  slug: microsoft-azure-key-vault-agentic-access
  summary_line: 29 operations · 20 acting
api_count: 6
apis:
- description: 'REST API for creating, importing, updating, and performing cryptographic operations with keys in Azure Key Vault. Supports RSA, EC, and symmetric key types with operations including encrypt, decrypt, '
  name: Azure Key Vault Keys API
  slug: azure-key-vault-keys-api
- description: REST API for securely storing and managing secrets such as passwords, connection strings, and API keys in Azure Key Vault.
  name: Azure Key Vault Secrets API
  slug: azure-key-vault-secrets-api
- description: REST API for creating, importing, managing, and renewing certificates in Azure Key Vault.
  name: Azure Key Vault Certificates API
  slug: azure-key-vault-certificates-api
- description: Operations for creating, importing, managing, and renewing certificates including lifecycle management and certificate authority integration.
  name: Azure Key Vault Certificates API
  slug: microsoft-azure-key-vault-certificates-api
- description: Operations for creating, importing, managing, and performing cryptographic operations with keys.
  name: Azure Key Vault Keys API
  slug: microsoft-azure-key-vault-keys-api
- description: Operations for securely storing and managing secrets such as passwords, connection strings, and API keys.
  name: Azure Key Vault Secrets API
  slug: microsoft-azure-key-vault-secrets-api
artifact_total: 222
collections:
- collection_type: postman
  name: Azure Key Vault Data Plane Certificates API
  slug: postman-microsoft-azure-key-vault-certificates-api
- collection_type: postman
  name: Azure Key Vault Data Plane Certificates Keys API
  slug: postman-microsoft-azure-key-vault-keys-api
- collection_type: postman
  name: Azure Key Vault Data Plane Certificates Secrets API
  slug: postman-microsoft-azure-key-vault-secrets-api
- collection_type: open
  name: Azure Key Vault Data Plane API
  slug: open-azure-key-vault-data-plane
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-key-vault/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-key-vault-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-key-vault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-key-vault-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-key-vault-scopes.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.microsoft.com/en-us/azure/key-vault/general/whats-new
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/key-vault/
- group: design
  title: ''
  type: SpectralRules
  url: rules/azure-key-vault-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/azure-key-vault-vocabulary.yaml
created: '2024'
description: Azure Key Vault is a cloud service for securely storing and accessing secrets, keys, and certificates. It helps safeguard cryptographic keys and secrets used by cloud applications and services.
examples:
- key_count: 1
  name: Azure Key Vault Data Plane Backup Secret Result Example
  slug: azure-key-vault-data-plane-backup-secret-result-example
- key_count: 6
  name: Azure Key Vault Data Plane Certificate Attributes Example
  slug: azure-key-vault-data-plane-certificate-attributes-example
- key_count: 7
  name: Azure Key Vault Data Plane Certificate Bundle Example
  slug: azure-key-vault-data-plane-certificate-bundle-example
- key_count: 1
  name: Azure Key Vault Data Plane Certificate Create Parameters Example
  slug: azure-key-vault-data-plane-certificate-create-parameters-example
- key_count: 3
  name: Azure Key Vault Data Plane Certificate Import Parameters Example
  slug: azure-key-vault-data-plane-certificate-import-parameters-example
- key_count: 4
  name: Azure Key Vault Data Plane Certificate Item Example
  slug: azure-key-vault-data-plane-certificate-item-example
- key_count: 2
  name: Azure Key Vault Data Plane Certificate List Result Example
  slug: azure-key-vault-data-plane-certificate-list-result-example
- key_count: 7
  name: Azure Key Vault Data Plane Certificate Operation Example
  slug: azure-key-vault-data-plane-certificate-operation-example
- key_count: 2
  name: Azure Key Vault Data Plane Certificate Policy Example
  slug: azure-key-vault-data-plane-certificate-policy-example
- key_count: 1
  name: Azure Key Vault Data Plane Certificate Update Parameters Example
  slug: azure-key-vault-data-plane-certificate-update-parameters-example
- key_count: 3
  name: Azure Key Vault Data Plane Deleted Certificate Bundle Example
  slug: azure-key-vault-data-plane-deleted-certificate-bundle-example
- key_count: 3
  name: Azure Key Vault Data Plane Deleted Key Bundle Example
  slug: azure-key-vault-data-plane-deleted-key-bundle-example
- key_count: 3
  name: Azure Key Vault Data Plane Deleted Secret Bundle Example
  slug: azure-key-vault-data-plane-deleted-secret-bundle-example
- key_count: 0
  name: Azure Key Vault Data Plane Deletion Recovery Level Example
  slug: azure-key-vault-data-plane-deletion-recovery-level-example
- key_count: 2
  name: Azure Key Vault Data Plane Error Example
  slug: azure-key-vault-data-plane-error-example
- key_count: 3
  name: Azure Key Vault Data Plane Issuer Parameters Example
  slug: azure-key-vault-data-plane-issuer-parameters-example
- key_count: 0
  name: Azure Key Vault Data Plane Json Web Key Curve Name Example
  slug: azure-key-vault-data-plane-json-web-key-curve-name-example
- key_count: 14
  name: Azure Key Vault Data Plane Json Web Key Example
  slug: azure-key-vault-data-plane-json-web-key-example
- key_count: 0
  name: Azure Key Vault Data Plane Json Web Key Operation Example
  slug: azure-key-vault-data-plane-json-web-key-operation-example
- key_count: 0
  name: Azure Key Vault Data Plane Json Web Key Type Example
  slug: azure-key-vault-data-plane-json-web-key-type-example
- key_count: 8
  name: Azure Key Vault Data Plane Key Attributes Example
  slug: azure-key-vault-data-plane-key-attributes-example
- key_count: 2
  name: Azure Key Vault Data Plane Key Bundle Example
  slug: azure-key-vault-data-plane-key-bundle-example
- key_count: 4
  name: Azure Key Vault Data Plane Key Create Parameters Example
  slug: azure-key-vault-data-plane-key-create-parameters-example
- key_count: 3
  name: Azure Key Vault Data Plane Key Item Example
  slug: azure-key-vault-data-plane-key-item-example
- key_count: 2
  name: Azure Key Vault Data Plane Key List Result Example
  slug: azure-key-vault-data-plane-key-list-result-example
- key_count: 5
  name: Azure Key Vault Data Plane Key Operation Result Example
  slug: azure-key-vault-data-plane-key-operation-result-example
- key_count: 5
  name: Azure Key Vault Data Plane Key Operations Parameters Example
  slug: azure-key-vault-data-plane-key-operations-parameters-example
- key_count: 3
  name: Azure Key Vault Data Plane Key Properties Example
  slug: azure-key-vault-data-plane-key-properties-example
- key_count: 3
  name: Azure Key Vault Data Plane Key Release Policy Example
  slug: azure-key-vault-data-plane-key-release-policy-example
- key_count: 2
  name: Azure Key Vault Data Plane Key Sign Parameters Example
  slug: azure-key-vault-data-plane-key-sign-parameters-example
- key_count: 2
  name: Azure Key Vault Data Plane Key Update Parameters Example
  slug: azure-key-vault-data-plane-key-update-parameters-example
- key_count: 0
  name: Azure Key Vault Data Plane Key Vault Error Example
  slug: azure-key-vault-data-plane-key-vault-error-example
- key_count: 3
  name: Azure Key Vault Data Plane Key Verify Parameters Example
  slug: azure-key-vault-data-plane-key-verify-parameters-example
- key_count: 1
  name: Azure Key Vault Data Plane Key Verify Result Example
  slug: azure-key-vault-data-plane-key-verify-result-example
- key_count: 2
  name: Azure Key Vault Data Plane Lifetime Action Example
  slug: azure-key-vault-data-plane-lifetime-action-example
- key_count: 6
  name: Azure Key Vault Data Plane Secret Attributes Example
  slug: azure-key-vault-data-plane-secret-attributes-example
- key_count: 6
  name: Azure Key Vault Data Plane Secret Bundle Example
  slug: azure-key-vault-data-plane-secret-bundle-example
- key_count: 4
  name: Azure Key Vault Data Plane Secret Item Example
  slug: azure-key-vault-data-plane-secret-item-example
- key_count: 2
  name: Azure Key Vault Data Plane Secret List Result Example
  slug: azure-key-vault-data-plane-secret-list-result-example
- key_count: 1
  name: Azure Key Vault Data Plane Secret Properties Example
  slug: azure-key-vault-data-plane-secret-properties-example
- key_count: 1
  name: Azure Key Vault Data Plane Secret Restore Parameters Example
  slug: azure-key-vault-data-plane-secret-restore-parameters-example
- key_count: 3
  name: Azure Key Vault Data Plane Secret Set Parameters Example
  slug: azure-key-vault-data-plane-secret-set-parameters-example
- key_count: 2
  name: Azure Key Vault Data Plane Secret Update Parameters Example
  slug: azure-key-vault-data-plane-secret-update-parameters-example
- key_count: 5
  name: Azure Key Vault Data Plane Subject Alternative Names Example
  slug: azure-key-vault-data-plane-subject-alternative-names-example
- key_count: 4
  name: Azure Key Vault Data Plane X509 Certificate Properties Example
  slug: azure-key-vault-data-plane-x509-certificate-properties-example
features:
- description: Create, import, and manage cryptographic keys with support for RSA, EC, and symmetric key types.
  name: Key Management
- description: Securely store and control access to passwords, connection strings, API keys, and other secrets.
  name: Secrets Management
- description: Automate certificate creation, renewal, and management with certificate authority integration.
  name: Certificate Lifecycle
- description: Perform encrypt, decrypt, sign, verify, wrap, and unwrap operations using managed keys.
  name: Cryptographic Operations
- description: Use hardware security modules for FIPS 140-2 Level 2 validated key protection.
  name: HSM-Backed Keys
- description: Recover accidentally deleted vaults, keys, secrets, and certificates with configurable retention.
  name: Soft Delete and Purge Protection
finops:
- name: Azure Key Vault Finops
  service_category: Security
  slug: azure-key-vault-finops
- name: Microsoft Azure Key Vault Finops
  service_category: Security / Key Management
  slug: microsoft-azure-key-vault-finops
image: https://azure.microsoft.com/svghandler/key-vault/
integrations:
- description: Reference Key Vault secrets and certificates directly from App Service configuration.
  name: Azure App Service
- description: Mount Key Vault secrets as volumes in AKS pods using the Secrets Store CSI Driver.
  name: Azure Kubernetes Service
- description: Use Key Vault secrets in CI/CD pipelines for secure deployment automation.
  name: Azure DevOps
- description: Encrypt Azure VM disks using customer-managed keys stored in Key Vault.
  name: Azure Disk Encryption
- description: Enable Transparent Data Encryption with customer-managed keys from Key Vault.
  name: Azure SQL Database
json_schemas:
- name: BackupSecretResult
  property_count: 1
  slug: azure-key-vault-data-plane-backup-secret-result
- name: CertificateAttributes
  property_count: 6
  slug: azure-key-vault-data-plane-certificate-attributes
- name: CertificateBundle
  property_count: 7
  slug: azure-key-vault-data-plane-certificate-bundle
- name: CertificateCreateParameters
  property_count: 1
  slug: azure-key-vault-data-plane-certificate-create-parameters
- name: CertificateImportParameters
  property_count: 3
  slug: azure-key-vault-data-plane-certificate-import-parameters
- name: CertificateItem
  property_count: 4
  slug: azure-key-vault-data-plane-certificate-item
- name: CertificateListResult
  property_count: 2
  slug: azure-key-vault-data-plane-certificate-list-result
- name: CertificateOperation
  property_count: 7
  slug: azure-key-vault-data-plane-certificate-operation
- name: CertificatePolicy
  property_count: 2
  slug: azure-key-vault-data-plane-certificate-policy
- name: CertificateUpdateParameters
  property_count: 1
  slug: azure-key-vault-data-plane-certificate-update-parameters
- name: DeletedCertificateBundle
  property_count: 3
  slug: azure-key-vault-data-plane-deleted-certificate-bundle
- name: DeletedKeyBundle
  property_count: 3
  slug: azure-key-vault-data-plane-deleted-key-bundle
- name: DeletedSecretBundle
  property_count: 3
  slug: azure-key-vault-data-plane-deleted-secret-bundle
- name: DeletionRecoveryLevel
  property_count: 0
  slug: azure-key-vault-data-plane-deletion-recovery-level
- name: Error
  property_count: 2
  slug: azure-key-vault-data-plane-error
- name: IssuerParameters
  property_count: 3
  slug: azure-key-vault-data-plane-issuer-parameters
- name: JsonWebKeyCurveName
  property_count: 0
  slug: azure-key-vault-data-plane-json-web-key-curve-name
- name: JsonWebKeyOperation
  property_count: 0
  slug: azure-key-vault-data-plane-json-web-key-operation
- name: JsonWebKey
  property_count: 14
  slug: azure-key-vault-data-plane-json-web-key
- name: JsonWebKeyType
  property_count: 0
  slug: azure-key-vault-data-plane-json-web-key-type
- name: KeyAttributes
  property_count: 8
  slug: azure-key-vault-data-plane-key-attributes
- name: KeyBundle
  property_count: 2
  slug: azure-key-vault-data-plane-key-bundle
- name: KeyCreateParameters
  property_count: 4
  slug: azure-key-vault-data-plane-key-create-parameters
- name: KeyItem
  property_count: 3
  slug: azure-key-vault-data-plane-key-item
- name: KeyListResult
  property_count: 2
  slug: azure-key-vault-data-plane-key-list-result
- name: KeyOperationResult
  property_count: 5
  slug: azure-key-vault-data-plane-key-operation-result
- name: KeyOperationsParameters
  property_count: 5
  slug: azure-key-vault-data-plane-key-operations-parameters
- name: KeyProperties
  property_count: 3
  slug: azure-key-vault-data-plane-key-properties
- name: KeyReleasePolicy
  property_count: 3
  slug: azure-key-vault-data-plane-key-release-policy
- name: KeySignParameters
  property_count: 2
  slug: azure-key-vault-data-plane-key-sign-parameters
- name: KeyUpdateParameters
  property_count: 2
  slug: azure-key-vault-data-plane-key-update-parameters
- name: KeyVaultError
  property_count: 0
  slug: azure-key-vault-data-plane-key-vault-error
- name: KeyVerifyParameters
  property_count: 3
  slug: azure-key-vault-data-plane-key-verify-parameters
- name: KeyVerifyResult
  property_count: 1
  slug: azure-key-vault-data-plane-key-verify-result
- name: LifetimeAction
  property_count: 2
  slug: azure-key-vault-data-plane-lifetime-action
- name: SecretAttributes
  property_count: 6
  slug: azure-key-vault-data-plane-secret-attributes
- name: SecretBundle
  property_count: 6
  slug: azure-key-vault-data-plane-secret-bundle
- name: SecretItem
  property_count: 4
  slug: azure-key-vault-data-plane-secret-item
- name: SecretListResult
  property_count: 2
  slug: azure-key-vault-data-plane-secret-list-result
- name: SecretProperties
  property_count: 1
  slug: azure-key-vault-data-plane-secret-properties
- name: SecretRestoreParameters
  property_count: 1
  slug: azure-key-vault-data-plane-secret-restore-parameters
- name: SecretSetParameters
  property_count: 3
  slug: azure-key-vault-data-plane-secret-set-parameters
- name: SecretUpdateParameters
  property_count: 2
  slug: azure-key-vault-data-plane-secret-update-parameters
- name: SubjectAlternativeNames
  property_count: 5
  slug: azure-key-vault-data-plane-subject-alternative-names
- name: X509CertificateProperties
  property_count: 4
  slug: azure-key-vault-data-plane-x509-certificate-properties
- name: Azure Key Vault Secret Bundle
  property_count: 7
  slug: azure-key-vault-secret
- name: BackupSecretResult
  property_count: 1
  slug: microsoft-azure-key-vault-backupsecretresult
- name: CertificateAttributes
  property_count: 7
  slug: microsoft-azure-key-vault-certificateattributes
- name: CertificateBundle
  property_count: 9
  slug: microsoft-azure-key-vault-certificatebundle
- name: CertificateCreateParameters
  property_count: 3
  slug: microsoft-azure-key-vault-certificatecreateparameters
- name: CertificateImportParameters
  property_count: 5
  slug: microsoft-azure-key-vault-certificateimportparameters
- name: CertificateItem
  property_count: 5
  slug: microsoft-azure-key-vault-certificateitem
- name: CertificateListResult
  property_count: 2
  slug: microsoft-azure-key-vault-certificatelistresult
- name: CertificateOperation
  property_count: 9
  slug: microsoft-azure-key-vault-certificateoperation
- name: CertificatePolicy
  property_count: 7
  slug: microsoft-azure-key-vault-certificatepolicy
- name: CertificateUpdateParameters
  property_count: 3
  slug: microsoft-azure-key-vault-certificateupdateparameters
- name: DeletedCertificateBundle
  property_count: 3
  slug: microsoft-azure-key-vault-deletedcertificatebundle
- name: DeletedKeyBundle
  property_count: 3
  slug: microsoft-azure-key-vault-deletedkeybundle
- name: DeletedSecretBundle
  property_count: 3
  slug: microsoft-azure-key-vault-deletedsecretbundle
- name: DeletionRecoveryLevel
  property_count: 0
  slug: microsoft-azure-key-vault-deletionrecoverylevel
- name: Error
  property_count: 3
  slug: microsoft-azure-key-vault-error
- name: IssuerParameters
  property_count: 3
  slug: microsoft-azure-key-vault-issuerparameters
- name: JsonWebKey
  property_count: 16
  slug: microsoft-azure-key-vault-jsonwebkey
- name: JsonWebKeyCurveName
  property_count: 0
  slug: microsoft-azure-key-vault-jsonwebkeycurvename
- name: JsonWebKeyOperation
  property_count: 0
  slug: microsoft-azure-key-vault-jsonwebkeyoperation
- name: JsonWebKeyType
  property_count: 0
  slug: microsoft-azure-key-vault-jsonwebkeytype
- name: KeyAttributes
  property_count: 9
  slug: microsoft-azure-key-vault-keyattributes
- name: KeyBundle
  property_count: 5
  slug: microsoft-azure-key-vault-keybundle
- name: KeyCreateParameters
  property_count: 8
  slug: microsoft-azure-key-vault-keycreateparameters
- name: KeyItem
  property_count: 4
  slug: microsoft-azure-key-vault-keyitem
- name: KeyListResult
  property_count: 2
  slug: microsoft-azure-key-vault-keylistresult
- name: KeyOperationResult
  property_count: 5
  slug: microsoft-azure-key-vault-keyoperationresult
- name: KeyOperationsParameters
  property_count: 5
  slug: microsoft-azure-key-vault-keyoperationsparameters
- name: KeyProperties
  property_count: 5
  slug: microsoft-azure-key-vault-keyproperties
- name: KeyReleasePolicy
  property_count: 3
  slug: microsoft-azure-key-vault-keyreleasepolicy
- name: KeySignParameters
  property_count: 2
  slug: microsoft-azure-key-vault-keysignparameters
- name: KeyUpdateParameters
  property_count: 4
  slug: microsoft-azure-key-vault-keyupdateparameters
- name: KeyVaultError
  property_count: 1
  slug: microsoft-azure-key-vault-keyvaulterror
- name: KeyVerifyParameters
  property_count: 3
  slug: microsoft-azure-key-vault-keyverifyparameters
- name: KeyVerifyResult
  property_count: 1
  slug: microsoft-azure-key-vault-keyverifyresult
- name: LifetimeAction
  property_count: 2
  slug: microsoft-azure-key-vault-lifetimeaction
- name: SecretAttributes
  property_count: 7
  slug: microsoft-azure-key-vault-secretattributes
- name: SecretBundle
  property_count: 7
  slug: microsoft-azure-key-vault-secretbundle
- name: SecretItem
  property_count: 5
  slug: microsoft-azure-key-vault-secretitem
- name: SecretListResult
  property_count: 2
  slug: microsoft-azure-key-vault-secretlistresult
- name: SecretProperties
  property_count: 1
  slug: microsoft-azure-key-vault-secretproperties
- name: SecretRestoreParameters
  property_count: 1
  slug: microsoft-azure-key-vault-secretrestoreparameters
- name: SecretSetParameters
  property_count: 4
  slug: microsoft-azure-key-vault-secretsetparameters
- name: SecretUpdateParameters
  property_count: 3
  slug: microsoft-azure-key-vault-secretupdateparameters
- name: SubjectAlternativeNames
  property_count: 5
  slug: microsoft-azure-key-vault-subjectalternativenames
- name: X509CertificateProperties
  property_count: 5
  slug: microsoft-azure-key-vault-x509certificateproperties
json_structures:
- name: Azure Key Vault Data Plane Backup Secret Result Structure
  property_count: 1
  slug: azure-key-vault-data-plane-backup-secret-result-structure
- name: Azure Key Vault Data Plane Certificate Attributes Structure
  property_count: 6
  slug: azure-key-vault-data-plane-certificate-attributes-structure
- name: Azure Key Vault Data Plane Certificate Bundle Structure
  property_count: 7
  slug: azure-key-vault-data-plane-certificate-bundle-structure
- name: Azure Key Vault Data Plane Certificate Create Parameters Structure
  property_count: 1
  slug: azure-key-vault-data-plane-certificate-create-parameters-structure
- name: Azure Key Vault Data Plane Certificate Import Parameters Structure
  property_count: 3
  slug: azure-key-vault-data-plane-certificate-import-parameters-structure
- name: Azure Key Vault Data Plane Certificate Item Structure
  property_count: 4
  slug: azure-key-vault-data-plane-certificate-item-structure
- name: Azure Key Vault Data Plane Certificate List Result Structure
  property_count: 2
  slug: azure-key-vault-data-plane-certificate-list-result-structure
- name: Azure Key Vault Data Plane Certificate Operation Structure
  property_count: 7
  slug: azure-key-vault-data-plane-certificate-operation-structure
- name: Azure Key Vault Data Plane Certificate Policy Structure
  property_count: 2
  slug: azure-key-vault-data-plane-certificate-policy-structure
- name: Azure Key Vault Data Plane Certificate Update Parameters Structure
  property_count: 1
  slug: azure-key-vault-data-plane-certificate-update-parameters-structure
- name: Azure Key Vault Data Plane Deleted Certificate Bundle Structure
  property_count: 3
  slug: azure-key-vault-data-plane-deleted-certificate-bundle-structure
- name: Azure Key Vault Data Plane Deleted Key Bundle Structure
  property_count: 3
  slug: azure-key-vault-data-plane-deleted-key-bundle-structure
- name: Azure Key Vault Data Plane Deleted Secret Bundle Structure
  property_count: 3
  slug: azure-key-vault-data-plane-deleted-secret-bundle-structure
- name: Azure Key Vault Data Plane Deletion Recovery Level Structure
  property_count: 0
  slug: azure-key-vault-data-plane-deletion-recovery-level-structure
- name: Azure Key Vault Data Plane Error Structure
  property_count: 2
  slug: azure-key-vault-data-plane-error-structure
- name: Azure Key Vault Data Plane Issuer Parameters Structure
  property_count: 3
  slug: azure-key-vault-data-plane-issuer-parameters-structure
- name: Azure Key Vault Data Plane Json Web Key Curve Name Structure
  property_count: 0
  slug: azure-key-vault-data-plane-json-web-key-curve-name-structure
- name: Azure Key Vault Data Plane Json Web Key Operation Structure
  property_count: 0
  slug: azure-key-vault-data-plane-json-web-key-operation-structure
- name: Azure Key Vault Data Plane Json Web Key Structure
  property_count: 14
  slug: azure-key-vault-data-plane-json-web-key-structure
- name: Azure Key Vault Data Plane Json Web Key Type Structure
  property_count: 0
  slug: azure-key-vault-data-plane-json-web-key-type-structure
- name: Azure Key Vault Data Plane Key Attributes Structure
  property_count: 8
  slug: azure-key-vault-data-plane-key-attributes-structure
- name: Azure Key Vault Data Plane Key Bundle Structure
  property_count: 2
  slug: azure-key-vault-data-plane-key-bundle-structure
- name: Azure Key Vault Data Plane Key Create Parameters Structure
  property_count: 4
  slug: azure-key-vault-data-plane-key-create-parameters-structure
- name: Azure Key Vault Data Plane Key Item Structure
  property_count: 3
  slug: azure-key-vault-data-plane-key-item-structure
- name: Azure Key Vault Data Plane Key List Result Structure
  property_count: 2
  slug: azure-key-vault-data-plane-key-list-result-structure
- name: Azure Key Vault Data Plane Key Operation Result Structure
  property_count: 5
  slug: azure-key-vault-data-plane-key-operation-result-structure
- name: Azure Key Vault Data Plane Key Operations Parameters Structure
  property_count: 5
  slug: azure-key-vault-data-plane-key-operations-parameters-structure
- name: Azure Key Vault Data Plane Key Properties Structure
  property_count: 3
  slug: azure-key-vault-data-plane-key-properties-structure
- name: Azure Key Vault Data Plane Key Release Policy Structure
  property_count: 3
  slug: azure-key-vault-data-plane-key-release-policy-structure
- name: Azure Key Vault Data Plane Key Sign Parameters Structure
  property_count: 2
  slug: azure-key-vault-data-plane-key-sign-parameters-structure
- name: Azure Key Vault Data Plane Key Update Parameters Structure
  property_count: 2
  slug: azure-key-vault-data-plane-key-update-parameters-structure
- name: Azure Key Vault Data Plane Key Vault Error Structure
  property_count: 0
  slug: azure-key-vault-data-plane-key-vault-error-structure
- name: Azure Key Vault Data Plane Key Verify Parameters Structure
  property_count: 3
  slug: azure-key-vault-data-plane-key-verify-parameters-structure
- name: Azure Key Vault Data Plane Key Verify Result Structure
  property_count: 1
  slug: azure-key-vault-data-plane-key-verify-result-structure
- name: Azure Key Vault Data Plane Lifetime Action Structure
  property_count: 2
  slug: azure-key-vault-data-plane-lifetime-action-structure
- name: Azure Key Vault Data Plane Secret Attributes Structure
  property_count: 6
  slug: azure-key-vault-data-plane-secret-attributes-structure
- name: Azure Key Vault Data Plane Secret Bundle Structure
  property_count: 6
  slug: azure-key-vault-data-plane-secret-bundle-structure
- name: Azure Key Vault Data Plane Secret Item Structure
  property_count: 4
  slug: azure-key-vault-data-plane-secret-item-structure
- name: Azure Key Vault Data Plane Secret List Result Structure
  property_count: 2
  slug: azure-key-vault-data-plane-secret-list-result-structure
- name: Azure Key Vault Data Plane Secret Properties Structure
  property_count: 1
  slug: azure-key-vault-data-plane-secret-properties-structure
- name: Azure Key Vault Data Plane Secret Restore Parameters Structure
  property_count: 1
  slug: azure-key-vault-data-plane-secret-restore-parameters-structure
- name: Azure Key Vault Data Plane Secret Set Parameters Structure
  property_count: 3
  slug: azure-key-vault-data-plane-secret-set-parameters-structure
- name: Azure Key Vault Data Plane Secret Update Parameters Structure
  property_count: 2
  slug: azure-key-vault-data-plane-secret-update-parameters-structure
- name: Azure Key Vault Data Plane Subject Alternative Names Structure
  property_count: 5
  slug: azure-key-vault-data-plane-subject-alternative-names-structure
- name: Azure Key Vault Data Plane X509 Certificate Properties Structure
  property_count: 4
  slug: azure-key-vault-data-plane-x509-certificate-properties-structure
- name: Microsoft Azure Key Vault Structure
  property_count: 0
  slug: microsoft-azure-key-vault-structure
jsonld:
- class_count: 0
  name: Azure Key Vault Context
  property_count: 57
  slug: azure-key-vault-context
- class_count: 0
  name: Azure Key Vault Data Plane Context
  property_count: 0
  slug: azure-key-vault-data-plane-context
layout: provider
modified: '2026-05-19'
name: Azure Key Vault
nav: Providers
network: true
overview: 'Azure Key Vault publishes 3 APIs on the [APIs.io](https://apis.io/) network: Certificates API, Keys API, and Secrets API. Tagged areas include Certificates, Cloud Security, Cryptography, Key Management, and Secrets Management.


  The Azure Key Vault catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Azure Key Vault''s developer surface includes authentication, engineering blog, changelog, developer portal, support, pricing, and 9 more developer resources.'
plans:
- name: Azure Key Vault Plans Pricing
  plan_count: 3
  slug: azure-key-vault-plans-pricing
- name: Microsoft Azure Key Vault Plans Pricing
  plan_count: 3
  slug: microsoft-azure-key-vault-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 13
  name: Azure Key Vault Rate Limits
  slug: azure-key-vault-rate-limits
- limit_count: 7
  name: Microsoft Azure Key Vault Rate Limits
  slug: microsoft-azure-key-vault-rate-limits
rules:
- name: Azure Key Vault API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-key-vault-spectral-rules
- name: Azure Key Vault API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-key-vault-jsonschema-spectral-rules
- name: Azure Key Vault API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: microsoft-azure-key-vault-spectral-rules
scopes:
- name: Microsoft Azure Key Vault Scopes
  scope_count: 1
  slug: microsoft-azure-key-vault-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.2
  delta: -8.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.1
    developer_ergonomics: 30.4
    discoverability: 72.2
    governance: 31.3
    operational_transparency: 39.5
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-key-vault/refs/heads/main/screenshots/microsoft-azure-key-vault-2026-06-20T185418.png
security:
- kind: authentication
  name: Microsoft Azure Key Vault Authentication
  slug: microsoft-azure-key-vault-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Key Vault Domain Security
  slug: microsoft-azure-key-vault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-key-vault
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
use_cases:
- description: Centralize and secure application secrets with audited access and automatic rotation.
  name: Application Secret Management
- description: Encrypt data at rest and in transit using customer-managed keys stored in Key Vault.
  name: Data Encryption
- description: Automate TLS certificate provisioning and renewal for web applications and services.
  name: TLS Certificate Management
- description: Sign code, documents, and artifacts using keys stored securely in Key Vault.
  name: Code and Document Signing
website: https://portal.azure.com/
---
