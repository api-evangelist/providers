---
aid: cert-manager
name: Cert-Manager
description: cert-manager is a powerful and extensible X.509 certificate controller for Kubernetes and OpenShift workloads. It obtains certificates from a variety of issuers, including Let's Encrypt, HashiCorp Vault, and Venafi, and ensures certificates are valid and up-to-date, attempting to renew them before expiry. It supports certificate issuance for Ingress, Gateway API, and arbitrary workloads via Certificate resources.
url: https://cert-manager.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Certificates
  - Cloud Native
  - Graduated
  - Kubernetes
  - Security
  - TLS
created: '2026-03-16'
modified: '2026-04-23'
specificationVersion: '0.19'
type: Index
apis:
  - aid: cert-manager:cert-manager-api
    name: cert-manager Kubernetes API
    description: The cert-manager API extends the Kubernetes API with custom resources including Certificate, Issuer, ClusterIssuer, CertificateRequest, and Order. These resources allow declarative management of TLS certificates, automatic renewal, and integration with ACME and other certificate authorities directly through kubectl and Kubernetes manifests.
    humanURL: https://cert-manager.io/docs/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://cert-manager.io/docs/
      - type: Reference
        url: https://cert-manager.io/docs/reference/api-docs/
      - type: Getting Started
        url: https://cert-manager.io/docs/getting-started/
      - type: GitHubRepository
        url: https://github.com/cert-manager/cert-manager
      - type: Change Log
        url: https://github.com/cert-manager/cert-manager/releases
      - type: JSONSchema
        url: json-schema/cert-manager-certificate-schema.json
      - type: JSONSchema
        url: json-schema/cert-manager-issuer-schema.json
    tags:
      - Certificates
      - Kubernetes API
      - TLS
  - aid: cert-manager:cmctl-cli
    name: cert-manager CLI (cmctl)
    description: cmctl is the command-line tool for managing cert-manager resources. It provides commands for checking certificate status, manually triggering renewals, approving or denying certificate requests, and converting cert-manager resources between API versions.
    humanURL: https://cert-manager.io/docs/reference/cmctl/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://cert-manager.io/docs/reference/cmctl/
      - type: GitHubRepository
        url: https://github.com/cert-manager/cmctl
      - type: Change Log
        url: https://github.com/cert-manager/cmctl/releases
    tags:
      - Certificate Management
      - CLI
  - aid: cert-manager:trust-manager
    name: trust-manager
    description: trust-manager is a cert-manager companion project for managing TLS trust bundles in Kubernetes and OpenShift clusters. It distributes CA bundles via a Bundle custom resource to namespaces and workloads, ensuring that applications have access to an up-to-date set of trusted CA certificates without manual maintenance.
    humanURL: https://cert-manager.io/docs/trust/trust-manager/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://cert-manager.io/docs/trust/trust-manager/
      - type: Getting Started
        url: https://cert-manager.io/docs/trust/trust-manager/installation/
      - type: GitHubRepository
        url: https://github.com/cert-manager/trust-manager
      - type: Change Log
        url: https://github.com/cert-manager/trust-manager/releases
    tags:
      - Kubernetes
      - TLS
      - Trust Bundles
  - aid: cert-manager:approver-policy
    name: cert-manager approver-policy
    description: approver-policy is a cert-manager policy plugin that automatically approves or denies CertificateRequest resources based on defined CertificateRequestPolicy custom resources. It provides fine-grained control over which certificate requests are permitted, including constraints on allowed DNS names, key usages, and issuers.
    humanURL: https://cert-manager.io/docs/policy/approval/approver-policy/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://cert-manager.io/docs/policy/approval/approver-policy/
      - type: GitHubRepository
        url: https://github.com/cert-manager/approver-policy
      - type: Change Log
        url: https://github.com/cert-manager/approver-policy/releases
    tags:
      - Certificate Approval
      - Policy
      - Security
  - aid: cert-manager:csi-driver
    name: cert-manager csi-driver
    description: csi-driver is a Kubernetes Container Storage Interface plugin that works alongside cert-manager to seamlessly request and mount certificate key pairs as ephemeral volumes directly into pods. It enables workloads to automatically obtain short-lived certificates at pod startup without requiring manual secret management.
    humanURL: https://cert-manager.io/docs/usage/csi-driver/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://cert-manager.io/docs/usage/csi-driver/
    tags:
      - Certificate Management
      - CSI
      - Kubernetes
  - aid: cert-manager:csi-driver-spiffe
    name: cert-manager csi-driver-spiffe
    description: csi-driver-spiffe is a Kubernetes CSI plugin that works alongside cert-manager to transparently deliver SPIFFE SVIDs as X.509 certificate key pairs to mounted pods using ephemeral volumes. It allows all pods running in a Kubernetes cluster to automatically receive SPIFFE identity documents from a configured Trust Domain.
    humanURL: https://cert-manager.io/docs/usage/csi-driver-spiffe/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://cert-manager.io/docs/usage/csi-driver-spiffe/
      - type: Getting Started
        url: https://cert-manager.io/docs/usage/csi-driver-spiffe/installation/
    tags:
      - CSI
      - Identity
      - Kubernetes
      - SPIFFE
common:
  - type: Website
    url: https://cert-manager.io
  - type: Documentation
    url: https://cert-manager.io/docs/
  - type: Getting Started
    url: https://cert-manager.io/docs/getting-started/
  - type: Reference
    url: https://cert-manager.io/docs/reference/
  - type: Community
    url: https://cert-manager.io/docs/contributing/
  - type: GitHubOrganization
    url: https://github.com/cert-manager
  - type: GitHubRepository
    url: https://github.com/cert-manager/cert-manager
  - type: Change Log
    url: https://github.com/cert-manager/cert-manager/releases
  - type: JSONSchema
    url: json-schema/cert-manager-certificate-schema.json
  - type: JSONSchema
    url: json-schema/cert-manager-issuer-schema.json
  - type: JSON-LD
    url: json-ld/cert-manager-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
