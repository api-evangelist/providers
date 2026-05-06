---
aid: sops
name: SOPS
description: SOPS (Secrets OPerationS) is a CNCF Sandbox encrypted file editor that supports YAML, JSON, ENV, INI, and binary formats. SOPS encrypts file values while leaving keys in cleartext, enabling secure storage of secrets in version control systems. Supports AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, age, and PGP for key management. Originally created at Mozilla and donated to the CNCF in 2023.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Secrets Management
  - Encryption
  - Configuration Management
  - DevOps
  - Security
  - Kubernetes
  - CNCF
created: '2025'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sops/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sops:sops-go-library
    name: SOPS Go Library
    description: The SOPS decrypt Go package provides programmatic access to SOPS-encrypted files from Go applications. It supports decryption of YAML, JSON, ENV, INI, and binary formats using configured key management services.
    humanURL: https://getsops.io/docs/
    baseURL: https://github.com/getsops/sops
    tags:
      - Go
      - Secrets Management
      - Encryption
      - Library
    properties:
      - type: Documentation
        url: https://getsops.io/docs/
      - type: GitHub
        url: https://github.com/getsops/sops
      - type: Releases
        url: https://github.com/getsops/sops/releases
common:
  - type: Website
    url: https://getsops.io/
  - type: Documentation
    url: https://getsops.io/docs/
  - type: GitHub Org
    url: https://github.com/getsops
  - type: GitHub Repository
    url: https://github.com/getsops/sops
  - type: Releases
    url: https://github.com/getsops/sops/releases
  - type: License
    url: https://github.com/getsops/sops/blob/main/LICENSE
  - type: Changelog
    url: https://github.com/getsops/sops/blob/main/CHANGELOG.rst
  - type: CNCF Sandbox
    url: https://www.cncf.io/projects/sops/
  - type: Homebrew
    url: https://formulae.brew.sh/formula/sops
  - type: Flux Integration
    url: https://fluxcd.io/flux/guides/mozilla-sops/
  - type: Blog
    url: https://getsops.io/blog/
  - type: Security
    url: https://github.com/getsops/sops/blob/main/SECURITY.md
features:
  - Encrypts file values while keeping keys in cleartext
  - Supports AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, age, PGP
  - Works with YAML, JSON, ENV, INI, and binary file formats
  - Key groups using Shamir Secret Sharing for multi-factor access control
  - Audit logging via PostgreSQL integration
  - Git integration for transparent decryption in diffs
  - Configuration file (.sops.yaml) for creation and destination rules
  - exec-env and exec-file commands to avoid secret exposure to disk
  - In-place encryption/decryption for workflow integration
integrations:
  - AWS KMS
  - GCP KMS
  - Azure Key Vault
  - HuaweiCloud KMS
  - age encryption
  - PGP/GPG
  - Kubernetes Secrets
  - Flux CD
  - ArgoCD
  - Helm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
