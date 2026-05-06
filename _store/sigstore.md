---
aid: sigstore
name: Sigstore
description: Sigstore is a set of free-to-use open source tools for signing, verifying, and protecting software supply chain artifacts. It provides a transparent and auditable signing infrastructure that eliminates the need for managing signing keys, making software supply chain security more accessible. The Sigstore ecosystem includes Cosign for artifact signing, Fulcio as the certificate authority, and Rekor as the cryptographically secure transparency log.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Certificate Authority
  - Code Signing
  - Containers
  - Cryptography
  - Open Source
  - PKI
  - Security
  - Software Supply Chain
  - Transparency Log
url: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sigstore:rekor
    name: Rekor Transparency Log API
    description: Rekor is a cryptographically secure, immutable transparency log for signed software releases. The Rekor API enables searching the transparency log, retrieving log entries, checking proofs, and querying the log's public key. The public-good instance runs at rekor.sigstore.dev.
    humanURL: https://docs.sigstore.dev/logging/overview/
    baseURL: https://rekor.sigstore.dev
    tags:
      - Cryptography
      - Security
      - Software Supply Chain
      - Transparency Log
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/logging/overview/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/openapi/rekor-openapi.yaml
      - type: GitHub Repository
        url: https://github.com/sigstore/rekor
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/rules/sigstore-rules.yml
  - aid: sigstore:fulcio
    name: Fulcio Certificate Authority API
    description: Fulcio is Sigstore's free Root Certificate Authority for code signing certificates. It issues short-lived signing certificates to software producers based on OIDC authentication. The API provides endpoints for obtaining signing certificates, retrieving trust bundles, and querying CA configuration. The public instance runs at fulcio.sigstore.dev.
    humanURL: https://docs.sigstore.dev/certificate_authority/overview/
    baseURL: https://fulcio.sigstore.dev
    tags:
      - Certificate Authority
      - Code Signing
      - Cryptography
      - OIDC
      - PKI
      - Security
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/certificate_authority/overview/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/openapi/fulcio-openapi.json
      - type: GitHub Repository
        url: https://github.com/sigstore/fulcio
  - aid: sigstore:cosign
    name: Cosign
    description: Cosign is the Sigstore tool for signing and verifying container images and other OCI artifacts. It enables keyless signing using OIDC identity, hardware token signing, and policy enforcement for container supply chain security.
    humanURL: https://docs.sigstore.dev/cosign/signing/overview/
    tags:
      - Code Signing
      - Containers
      - OCI
      - Security
      - Software Supply Chain
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/cosign/signing/overview/
      - type: GitHub Repository
        url: https://github.com/sigstore/cosign
common:
  - type: Website
    url: https://www.sigstore.dev/
  - type: Documentation
    url: https://docs.sigstore.dev/
  - type: Getting Started
    url: https://docs.sigstore.dev/quickstart/quickstart-cosign/
  - type: GitHub Organization
    url: https://github.com/sigstore
  - type: Blog
    url: https://blog.sigstore.dev/
  - type: Community
    url: https://sigstore.dev/community/
  - type: Policy Controller
    url: https://docs.sigstore.dev/policy-controller/overview/
  - type: Security
    url: https://docs.sigstore.dev/about/security/
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/sigstore/refs/heads/main/vocabulary/sigstore-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
