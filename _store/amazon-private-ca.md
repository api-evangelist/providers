---
name: Amazon Private CA
description: AWS Private Certificate Authority (AWS Private CA) is a highly available, fully managed private CA service that helps you easily and securely manage the lifecycle of your private certificates. It allows you to create private CA hierarchies and issue X.509 certificates for your internal resources including TLS certificates for microservices, IoT devices, and user authentication.
url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/apis.yml
type: Index
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Certificate Authority
  - Certificates
  - PKI
  - Security
  - X.509
  - TLS
  - IoT
created: '2026-03-16'
modified: '2026-04-19'
apis:
  - name: AWS Private CA API
    description: The AWS Private CA API provides programmatic access to create and manage private certificate authorities, issue X.509 certificates, manage certificate revocation lists, configure audit reports, and control permissions and policies for private PKI infrastructure.
    humanURL: https://aws.amazon.com/private-ca/
    baseURL: https://acm-pca.amazonaws.com
    tags:
      - Certificates
      - PKI
      - Security
      - Certificate Authority
      - X.509
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/privateca/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-private-ca-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/private-ca/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/private-ca/pricing/
      - type: FAQ
        url: https://aws.amazon.com/private-ca/faqs/
      - type: Authentication
        url: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/privateca/latest/userguide/PcaLimits.html
common:
  - type: Portal
    url: https://aws.amazon.com/private-ca/
  - type: Documentation
    url: https://docs.aws.amazon.com/privateca/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/aws-certificate-manager-private-ca/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/acm-pca/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SpectralRules
    url: rules/amazon-private-ca-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/pki-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-private-ca-vocabulary.yaml
  - type: Features
    data:
      - name: Private CA Hierarchy
        description: Create root and subordinate CA hierarchies for complete control over your PKI infrastructure.
      - name: X.509 Certificate Issuance
        description: Issue end-entity and CA certificates signed by your private CAs for internal resources.
      - name: Certificate Revocation
        description: Revoke compromised or expired certificates with CRL and OCSP support.
      - name: Audit Reports
        description: Generate detailed audit reports of all certificate issuance activity stored in S3.
      - name: Short-Lived Certificates
        description: Issue short-lived certificates to reduce revocation overhead and improve security posture.
      - name: Custom Templates
        description: Use certificate templates to standardize certificate extensions and constraints.
      - name: IAM Integration
        description: Control access to CA operations using fine-grained IAM policies and resource-based policies.
      - name: High Availability
        description: Fully managed, highly available service with automatic failover across AWS Availability Zones.
  - type: UseCases
    data:
      - name: TLS for Internal Services
        description: Issue TLS certificates for microservices, APIs, and internal web applications.
      - name: IoT Device Authentication
        description: Provision unique X.509 certificates to IoT devices for mutual TLS authentication.
      - name: User and Workload Identity
        description: Issue certificates for user authentication and workload identity in zero-trust architectures.
      - name: Code Signing
        description: Sign software artifacts and container images with private CA-issued certificates.
      - name: VPN and Network Security
        description: Issue certificates for VPN clients and network devices for mutual authentication.
  - type: Integrations
    data:
      - name: AWS Certificate Manager
        description: Integrate Private CA with ACM to manage and deploy certificates on AWS services.
      - name: AWS IoT Core
        description: Use Private CA to provision certificates for IoT devices connecting to AWS IoT Core.
      - name: Kubernetes
        description: Integrate with cert-manager for automated certificate provisioning in Kubernetes clusters.
      - name: Amazon EKS
        description: Issue certificates for service mesh and pod-to-pod TLS in EKS clusters.
      - name: AWS Secrets Manager
        description: Store and rotate private keys associated with issued certificates.
  - type: JSON-LD
    url: json-ld/amazon-private-ca-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-private-ca-access-description-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-access-method-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-access-method-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-action-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-api-passthrough-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-asn1subject-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-audit-report-response-format-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-audit-report-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-certificate-authority-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-certificate-authority-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-certificate-authority-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-certificate-authority-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-certificate-authority-usage-mode-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-create-certificate-authority-audit-report-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-create-certificate-authority-audit-report-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-create-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-create-certificate-authority-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-create-permission-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-crl-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-csr-extensions-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-custom-attribute-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-custom-extension-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-delete-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-delete-permission-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-delete-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-describe-certificate-authority-audit-report-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-describe-certificate-authority-audit-report-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-describe-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-describe-certificate-authority-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-edi-party-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-extended-key-usage-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-extended-key-usage-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-extensions-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-failure-reason-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-general-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-certificate-authority-certificate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-certificate-authority-certificate-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-certificate-authority-csr-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-certificate-authority-csr-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-certificate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-certificate-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-get-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-import-certificate-authority-certificate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-issue-certificate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-issue-certificate-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-key-algorithm-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-key-storage-security-standard-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-key-usage-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-list-certificate-authorities-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-list-certificate-authorities-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-list-permissions-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-list-permissions-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-list-tags-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-list-tags-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-ocsp-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-other-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-permission-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-policy-information-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-policy-qualifier-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-policy-qualifier-info-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-put-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-qualifier-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-resource-owner-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-restore-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-revocation-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-revocation-reason-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-revoke-certificate-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-s3object-acl-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-signing-algorithm-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-tag-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-tag-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-untag-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-update-certificate-authority-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-validity-period-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-private-ca-validity-schema.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-access-description-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-access-method-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-access-method-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-action-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-api-passthrough-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-asn1subject-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-audit-report-response-format-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-audit-report-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-certificate-authority-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-certificate-authority-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-certificate-authority-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-certificate-authority-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-certificate-authority-usage-mode-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-create-certificate-authority-audit-report-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-create-certificate-authority-audit-report-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-create-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-create-certificate-authority-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-create-permission-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-crl-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-csr-extensions-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-custom-attribute-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-custom-extension-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-delete-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-delete-permission-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-delete-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-describe-certificate-authority-audit-report-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-describe-certificate-authority-audit-report-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-describe-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-describe-certificate-authority-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-edi-party-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-extended-key-usage-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-extended-key-usage-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-extensions-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-failure-reason-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-general-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-certificate-authority-certificate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-certificate-authority-certificate-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-certificate-authority-csr-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-certificate-authority-csr-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-certificate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-certificate-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-get-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-import-certificate-authority-certificate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-issue-certificate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-issue-certificate-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-key-algorithm-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-key-storage-security-standard-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-key-usage-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-list-certificate-authorities-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-list-certificate-authorities-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-list-permissions-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-list-permissions-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-list-tags-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-list-tags-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-ocsp-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-other-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-permission-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-policy-information-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-policy-qualifier-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-policy-qualifier-info-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-put-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-qualifier-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-resource-owner-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-restore-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-revocation-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-revocation-reason-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-revoke-certificate-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-s3object-acl-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-signing-algorithm-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-tag-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-tag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-untag-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-update-certificate-authority-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-validity-period-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-private-ca-validity-structure.json
  - type: Example
    url: examples/amazon-private-ca-access-description-example.json
  - type: Example
    url: examples/amazon-private-ca-access-method-example.json
  - type: Example
    url: examples/amazon-private-ca-api-passthrough-example.json
  - type: Example
    url: examples/amazon-private-ca-asn1subject-example.json
  - type: Example
    url: examples/amazon-private-ca-certificate-authority-configuration-example.json
  - type: Example
    url: examples/amazon-private-ca-certificate-authority-example.json
  - type: Example
    url: examples/amazon-private-ca-create-certificate-authority-audit-report-request-example.json
  - type: Example
    url: examples/amazon-private-ca-create-certificate-authority-audit-report-response-example.json
  - type: Example
    url: examples/amazon-private-ca-create-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-create-certificate-authority-response-example.json
  - type: Example
    url: examples/amazon-private-ca-create-permission-request-example.json
  - type: Example
    url: examples/amazon-private-ca-crl-configuration-example.json
  - type: Example
    url: examples/amazon-private-ca-csr-extensions-example.json
  - type: Example
    url: examples/amazon-private-ca-custom-attribute-example.json
  - type: Example
    url: examples/amazon-private-ca-custom-extension-example.json
  - type: Example
    url: examples/amazon-private-ca-delete-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-delete-permission-request-example.json
  - type: Example
    url: examples/amazon-private-ca-delete-policy-request-example.json
  - type: Example
    url: examples/amazon-private-ca-describe-certificate-authority-audit-report-request-example.json
  - type: Example
    url: examples/amazon-private-ca-describe-certificate-authority-audit-report-response-example.json
  - type: Example
    url: examples/amazon-private-ca-describe-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-describe-certificate-authority-response-example.json
  - type: Example
    url: examples/amazon-private-ca-edi-party-name-example.json
  - type: Example
    url: examples/amazon-private-ca-extended-key-usage-example.json
  - type: Example
    url: examples/amazon-private-ca-extensions-example.json
  - type: Example
    url: examples/amazon-private-ca-general-name-example.json
  - type: Example
    url: examples/amazon-private-ca-get-certificate-authority-certificate-request-example.json
  - type: Example
    url: examples/amazon-private-ca-get-certificate-authority-certificate-response-example.json
  - type: Example
    url: examples/amazon-private-ca-get-certificate-authority-csr-request-example.json
  - type: Example
    url: examples/amazon-private-ca-get-certificate-authority-csr-response-example.json
  - type: Example
    url: examples/amazon-private-ca-get-certificate-request-example.json
  - type: Example
    url: examples/amazon-private-ca-get-certificate-response-example.json
  - type: Example
    url: examples/amazon-private-ca-get-policy-request-example.json
  - type: Example
    url: examples/amazon-private-ca-get-policy-response-example.json
  - type: Example
    url: examples/amazon-private-ca-import-certificate-authority-certificate-request-example.json
  - type: Example
    url: examples/amazon-private-ca-issue-certificate-request-example.json
  - type: Example
    url: examples/amazon-private-ca-issue-certificate-response-example.json
  - type: Example
    url: examples/amazon-private-ca-key-usage-example.json
  - type: Example
    url: examples/amazon-private-ca-list-certificate-authorities-request-example.json
  - type: Example
    url: examples/amazon-private-ca-list-certificate-authorities-response-example.json
  - type: Example
    url: examples/amazon-private-ca-list-permissions-request-example.json
  - type: Example
    url: examples/amazon-private-ca-list-permissions-response-example.json
  - type: Example
    url: examples/amazon-private-ca-list-tags-request-example.json
  - type: Example
    url: examples/amazon-private-ca-list-tags-response-example.json
  - type: Example
    url: examples/amazon-private-ca-ocsp-configuration-example.json
  - type: Example
    url: examples/amazon-private-ca-other-name-example.json
  - type: Example
    url: examples/amazon-private-ca-permission-example.json
  - type: Example
    url: examples/amazon-private-ca-policy-information-example.json
  - type: Example
    url: examples/amazon-private-ca-policy-qualifier-info-example.json
  - type: Example
    url: examples/amazon-private-ca-put-policy-request-example.json
  - type: Example
    url: examples/amazon-private-ca-qualifier-example.json
  - type: Example
    url: examples/amazon-private-ca-restore-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-revocation-configuration-example.json
  - type: Example
    url: examples/amazon-private-ca-revoke-certificate-request-example.json
  - type: Example
    url: examples/amazon-private-ca-tag-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-tag-example.json
  - type: Example
    url: examples/amazon-private-ca-untag-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-update-certificate-authority-request-example.json
  - type: Example
    url: examples/amazon-private-ca-validity-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-private-ca.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include: []
---
