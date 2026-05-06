---
aid: tuf
name: The Update Framework (TUF)
description: TUF (The Update Framework) is a CNCF graduated framework for securing software update systems. It provides a specification for how software repositories should be structured and how clients should verify updates to protect against key compromise, rollback attacks, and mix-and-match attacks. TUF is used by many package managers and update systems including PyPI, Sigstore, and various Linux distributions. The framework defines a four-role metadata structure (root, targets, snapshot, timestamp) with threshold signing and delegation capabilities for scalable trust management.
url: https://theupdateframework.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNCF
  - Cloud Native
  - Graduated
  - Security
  - Software Supply Chain
  - Software Updates
  - Verification
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
apis:
  - aid: tuf:tuf-spec
    name: TUF Repository Specification
    description: The TUF specification defines the structure of update repositories including the root, targets, snapshot, and timestamp metadata files. Each metadata file has a defined schema with signatures, expiration dates, and delegation rules. Clients follow a defined verification workflow to securely resolve and download updates while protecting against various attack vectors including key compromise, rollback attacks, freeze attacks, and mix-and-match attacks. The specification is version 1.0.31.
    humanURL: https://theupdateframework.github.io/specification/latest/
    properties:
      - type: Documentation
        url: https://theupdateframework.github.io/specification/latest/
      - type: GitHubRepository
        url: https://github.com/theupdateframework/specification
      - type: JSONSchema
        url: json-schema/tuf-root-metadata-schema.json
      - type: JSONSchema
        url: json-schema/tuf-targets-metadata-schema.json
      - type: JSONSchema
        url: json-schema/tuf-snapshot-metadata-schema.json
      - type: JSONSchema
        url: json-schema/tuf-timestamp-metadata-schema.json
    tags:
      - Metadata
      - Repository Metadata
      - Specification
      - Verification
  - aid: tuf:python-tuf
    name: TUF Python Reference Implementation
    description: The official Python reference implementation of The Update Framework (TUF) specification. Provides a metadata API for reading and writing TUF metadata files, an ngclient API implementing the TUF client update workflow, and a repository library for building TUF-compliant software repositories. Available on PyPI as the 'tuf' package.
    humanURL: https://theupdateframework.readthedocs.io/en/stable/
    properties:
      - type: Documentation
        url: https://theupdateframework.readthedocs.io/en/stable/
      - type: GitHubRepository
        url: https://github.com/theupdateframework/python-tuf
      - type: PackageRegistry
        url: https://pypi.org/project/tuf/
    tags:
      - Client Library
      - Python
      - Security
      - Software Updates
      - Supply Chain
  - aid: tuf:go-tuf
    name: TUF Go Implementation
    description: A Go implementation of The Update Framework (TUF), heavily influenced by python-tuf's design. Provides metadata, TrustedMetadata, and Updater packages implementing the TUF client workflow and specification-compliant metadata handling, as well as multi-repository support via TAP 4.
    humanURL: https://github.com/theupdateframework/go-tuf
    properties:
      - type: Documentation
        url: https://github.com/theupdateframework/go-tuf
      - type: GitHubRepository
        url: https://github.com/theupdateframework/go-tuf
    tags:
      - Client Library
      - Go
      - Security
      - Software Updates
      - Supply Chain
  - aid: tuf:rust-tuf
    name: TUF Rust Implementation
    description: A Rust implementation of The Update Framework (TUF) specification providing a strongly-typed API for working with TUF metadata, verifying signatures, and implementing the TUF client update workflow.
    humanURL: https://github.com/theupdateframework/rust-tuf
    properties:
      - type: GitHubRepository
        url: https://github.com/theupdateframework/rust-tuf
    tags:
      - Client Library
      - Rust
      - Security
      - Software Updates
  - aid: tuf:tuf-js
    name: TUF JavaScript Implementation
    description: A JavaScript/TypeScript implementation of The Update Framework (TUF) for use in Node.js environments and browser-based update systems. Enables TUF-compliant software update verification in the JavaScript ecosystem.
    humanURL: https://github.com/theupdateframework/tuf-js
    properties:
      - type: GitHubRepository
        url: https://github.com/theupdateframework/tuf-js
    tags:
      - Client Library
      - JavaScript
      - Security
      - Software Updates
      - TypeScript
  - aid: tuf:tuf-on-ci
    name: TUF on CI
    description: A TUF repository management and signing tool designed for use in CI/CD pipelines. Enables teams to maintain a TUF repository using GitHub Actions and other CI systems for automated, policy-driven key management and metadata signing workflows.
    humanURL: https://github.com/theupdateframework/tuf-on-ci
    properties:
      - type: GitHubRepository
        url: https://github.com/theupdateframework/tuf-on-ci
    tags:
      - CI/CD
      - Key Management
      - Repository Management
      - Security
  - aid: tuf:tuf-conformance
    name: TUF Conformance Test Suite
    description: The official TUF client conformance test suite for verifying that TUF client implementations correctly implement the TUF specification, including proper handling of all attack vectors and edge cases.
    humanURL: https://github.com/theupdateframework/tuf-conformance
    properties:
      - type: GitHubRepository
        url: https://github.com/theupdateframework/tuf-conformance
    tags:
      - Compliance
      - Conformance Testing
      - Security
      - Testing
common:
  - type: Website
    url: https://theupdateframework.io/
  - type: Documentation
    url: https://theupdateframework.io/docs/
  - type: GettingStarted
    url: https://theupdateframework.io/docs/getting-started/
  - type: GitHub Organization
    url: https://github.com/theupdateframework
  - type: GitHubRepository
    url: https://github.com/theupdateframework/python-tuf
  - type: Specification
    url: https://theupdateframework.github.io/specification/latest/
  - type: Blog
    url: https://theupdateframework.io/resources/news/
  - type: CNCF
    url: https://www.cncf.io/projects/the-update-framework-tuf/
  - type: Community
    url: https://github.com/theupdateframework/community
  - type: JSON-LD
    url: json-ld/tuf-context.jsonld
  - type: JSONSchema
    url: json-schema/tuf-root-metadata-schema.json
  - type: JSONSchema
    url: json-schema/tuf-targets-metadata-schema.json
  - type: JSONSchema
    url: json-schema/tuf-snapshot-metadata-schema.json
  - type: JSONSchema
    url: json-schema/tuf-timestamp-metadata-schema.json
  - type: Vocabulary
    url: vocabulary/tuf-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
