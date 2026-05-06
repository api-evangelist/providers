---
aid: cosign
name: Cosign
x-type: opensource
description: Cosign is the command-line client of the Sigstore project for signing, verifying, and storing container images, OCI artifacts, blobs, and in-toto attestations. Cosign supports keyless signing using OpenID Connect identity providers (Google, GitHub, Microsoft) by obtaining short-lived certificates from the Fulcio certificate authority and recording signing events in the Rekor transparency log. Signatures and attestations are stored alongside the signed artifact in any OCI-compliant registry, and cosign integrates with policy controllers, KMS providers, hardware tokens, and SBOM workflows for software supply chain security.
url: https://raw.githubusercontent.com/api-evangelist/cosign/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Public
position: Provider
tags:
  - Apache 2.0
  - Attestations
  - CLI
  - Code Signing
  - Containers
  - Fulcio
  - Go
  - Keyless
  - OCI
  - OIDC
  - Open Source
  - Rekor
  - Sigstore
  - Supply Chain
  - Transparency Log
  - Verification
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: cosign:cosign-cli
    name: Cosign CLI
    description: Cosign is a command-line tool for signing, verifying, and storing container images and OCI artifacts. It supports keyless signing, hardware-backed keys, KMS providers, in-toto and SLSA attestations, and transparency log inclusion. The CLI is the primary user interface and does not expose its own HTTP API.
    humanURL: https://docs.sigstore.dev/cosign/
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/cosign/
      - type: GettingStarted
        url: https://docs.sigstore.dev/quickstart/quickstart-cosign/
      - type: Installation
        url: https://docs.sigstore.dev/cosign/system_config/installation/
      - type: GitHubRepository
        url: https://github.com/sigstore/cosign
      - type: Reference
        url: https://docs.sigstore.dev/cosign/reference/cosign/
    tags:
      - CLI
      - Containers
      - Keyless
      - OCI
      - Signing
  - aid: cosign:rekor-api
    name: Sigstore Rekor API (consumed)
    description: Rekor is the Sigstore transparency log that cosign writes to and reads from when recording and verifying signing events. The public Rekor service exposes a REST API at rekor.sigstore.dev with operations for creating log entries, retrieving entries by index or UUID, fetching log info and proofs, and searching the index.
    humanURL: https://docs.sigstore.dev/logging/overview/
    baseURL: https://rekor.sigstore.dev
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/logging/overview/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/sigstore/rekor/main/openapi.yaml
      - type: GitHubRepository
        url: https://github.com/sigstore/rekor
    tags:
      - Rekor
      - REST
      - Sigstore
      - Transparency Log
  - aid: cosign:fulcio-api
    name: Sigstore Fulcio API (consumed)
    description: Fulcio is the Sigstore certificate authority that issues short-lived X.509 code-signing certificates bound to OIDC identities. Cosign calls the Fulcio public CA at fulcio.sigstore.dev during keyless signing to obtain a certificate for a verified identity.
    humanURL: https://docs.sigstore.dev/certificate_authority/overview/
    baseURL: https://fulcio.sigstore.dev
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/certificate_authority/overview/
      - type: GitHubRepository
        url: https://github.com/sigstore/fulcio
    tags:
      - CA
      - Certificates
      - Fulcio
      - OIDC
      - Sigstore
common:
  - type: Website
    url: https://www.sigstore.dev/
  - type: Documentation
    url: https://docs.sigstore.dev/cosign/
  - type: GettingStarted
    url: https://docs.sigstore.dev/quickstart/quickstart-cosign/
  - type: Installation
    url: https://docs.sigstore.dev/cosign/system_config/installation/
  - type: GitHubOrganization
    url: https://github.com/sigstore
  - type: GitHubRepository
    url: https://github.com/sigstore/cosign
  - type: Releases
    url: https://github.com/sigstore/cosign/releases
  - type: Blog
    url: https://blog.sigstore.dev/
  - type: Community
    url: https://docs.sigstore.dev/about/community/
  - type: Slack
    url: https://sigstore.slack.com/
  - type: License
    url: https://github.com/sigstore/cosign/blob/main/LICENSE
  - type: Security
    url: https://github.com/sigstore/cosign/security
  - type: Roadmap
    url: https://github.com/sigstore/cosign/blob/main/ROADMAP.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
