---
aid: notary
url: https://raw.githubusercontent.com/api-evangelist/notary/refs/heads/main/apis.yml
apis:
- aid: notary:notary-spec
  name: Notary Project Signing Specification
  description: The Notary Project specification defines the signature envelope format, trust store and trust policy for container image signing and verification. It supports multiple signature formats and integrates with OCI distribution registries for storing signatures alongside container images. The specification enables end-to-end supply chain security from build to deployment.
  humanURL: https://notaryproject.dev/docs/
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://notaryproject.dev/docs/
  - type: Reference
    url: https://github.com/notaryproject/specifications/blob/main/specs/trust-store-trust-policy.md
  - type: GitHubRepository
    url: https://github.com/notaryproject/specifications
  - type: JSONSchema
    url: json-schema/notary-trust-policy-schema.json
  - type: JSONSchema
    url: json-schema/notary-signature-envelope-schema.json
  tags:
  - Signing
  - Specification
  - Verification
- aid: notary:notation-cli
  name: Notation CLI
  description: Notation is the command-line tool that implements the Notary Project specifications for signing and verifying OCI artifacts stored in container registries. It supports signing with certificates stored in trust stores, configuring trust policies for verification, and extends to third-party key management systems via a plugin model.
  humanURL: https://notaryproject.dev/docs/user-guides/installation/cli/
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://notaryproject.dev/docs/user-guides/installation/cli/
  - type: Getting Started
    url: https://notaryproject.dev/docs/user-guides/installation/
  - type: Reference
    url: https://github.com/notaryproject/notation/blob/main/specs/notation-cli.md
  - type: GitHubRepository
    url: https://github.com/notaryproject/notation
  - type: Change Log
    url: https://github.com/notaryproject/notation/releases
  tags:
  - CLI
  - OCI
  - Signing
  - Verification
- aid: notary:notation-go
  name: notation-go Library
  description: notation-go is the official Go library for signing and verifying OCI artifacts using the Notary Project specifications. It provides the programmatic interface used by the Notation CLI and enables Go applications to integrate artifact signing and verification into their own workflows without invoking the CLI directly.
  humanURL: https://github.com/notaryproject/notation-go
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://pkg.go.dev/github.com/notaryproject/notation-go
  - type: GitHubRepository
    url: https://github.com/notaryproject/notation-go
  tags:
  - Client Library
  - Go
  - SDK
  - Signing
- aid: notary:notation-plugin-framework
  name: Notation Plugin Extensibility
  description: The Notation plugin extensibility specification defines the interface that third-party plugins must implement to integrate with Notation for key management, signing, and verification operations. Plugins allow Notation to work with hardware security modules, cloud key management services, and other external credential systems.
  humanURL: https://github.com/notaryproject/specifications/blob/main/specs/plugin-extensibility.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/notaryproject/specifications/blob/main/specs/plugin-extensibility.md
  - type: Reference
    url: https://pkg.go.dev/github.com/notaryproject/notation-plugin-framework-go/plugin
  - type: GitHubRepository
    url: https://github.com/notaryproject/notation-go
  - type: JSONSchema
    url: json-schema/notary-plugin-schema.json
  - type: JSONSchema
    url: json-schema/notary-plugin-protocol-schema.json
  tags:
  - Extensibility
  - Key Management
  - Plugin
  - Signing
name: Notary Project
tags:
- Cloud Native
- Container Security
- Image Signing
- Incubating
- OCI
- Verification
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Notary Project is a CNCF incubating set of specifications and tools for signing and verifying container images and other OCI artifacts. It provides Notation, a CLI and library for signing artifacts stored in OCI-compliant registries. The project defines standards for signature formats, trust policies, and verification workflows to secure software supply chains.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

