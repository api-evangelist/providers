---
aid: tuf
url: https://raw.githubusercontent.com/api-evangelist/tuf/refs/heads/main/apis.yml
apis:
- aid: tuf:tuf-spec
  name: TUF Repository Specification
  description: The TUF specification defines the structure of update repositories including the root, targets, snapshot, and timestamp metadata files. Each metadata file has a defined schema with signatures, expiration dates, and delegation rules. Clients follow a defined verification workflow to securely resolve and download updates while protecting against various attack vectors.
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
  - Repository Metadata
  - Specification
  - Verification
- aid: tuf:python-tuf
  name: TUF Python Reference Implementation
  description: The official Python reference implementation of The Update Framework (TUF) specification. Provides a metadata API for reading and writing TUF metadata files, an ngclient API implementing the TUF client update workflow, and a repository library for building TUF-compliant software repositories.
  humanURL: https://theupdateframework.readthedocs.io/en/stable/
  properties:
  - type: Documentation
    url: https://theupdateframework.readthedocs.io/en/stable/
  - type: GitHubRepository
    url: https://github.com/theupdateframework/python-tuf
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
name: The Update Framework (TUF)
tags:
- Cloud Native
- Graduated
- Security
- Software Updates
- Supply Chain
- Verification
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: TUF (The Update Framework) is a CNCF graduated framework for securing software update systems. It provides a specification for how software repositories should be structured and how clients should verify updates to protect against key compromise, rollback attacks, and mix-and-match attacks. TUF is used by many package managers and update systems including PyPI, Sigstore, and various Linux distributions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

