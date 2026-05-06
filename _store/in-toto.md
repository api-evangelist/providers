---
aid: in-toto
name: In-Toto
description: in-toto is a CNCF graduated framework for securing the integrity of software supply chains. It provides a specification for generating and verifying metadata about each step in a software supply chain, from source code to deployment. in-toto ensures that each step is performed by the authorized party and that materials and products are not tampered with between steps.
url: https://in-toto.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Graduated
  - Security
  - Software Integrity
  - Supply Chain Security
  - Verification
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: in-toto:in-toto-spec
    name: in-toto Attestation Specification
    description: The in-toto specification defines the metadata format for recording software supply chain steps. It includes layout metadata that defines the expected steps and their authorized functionaries, and link metadata that records what actually happened at each step including materials consumed and products produced. Verification compares layouts against links to detect tampering.
    humanURL: https://in-toto.io/docs/specs/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://in-toto.io/docs/specs/
      - type: Reference
        url: https://github.com/in-toto/docs/blob/master/in-toto-spec.md
      - type: JSONSchema
        url: json-schema/in-toto-layout-schema.json
      - type: JSONSchema
        url: json-schema/in-toto-link-schema.json
      - type: JSONSchema
        url: json-schema/in-toto-attestation-schema.json
      - type: JSON-LD
        url: json-ld/in-toto-context.jsonld
    tags:
      - Attestation
      - Specification
      - Supply Chain
  - aid: in-toto:in-toto-attestation-framework
    name: in-toto Attestation Framework
    description: The in-toto Attestation Framework provides a specification for generating verifiable claims about any aspect of how a piece of software is produced. It defines a fixed lightweight Statement structure with a subject and predicate, and a set of standard predicate types covering common use cases such as SLSA provenance. A future version of the in-toto specification will incorporate this framework as the primary mechanism to express supply chain claims.
    humanURL: https://github.com/in-toto/attestation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://github.com/in-toto/attestation/blob/main/README.md
      - type: Reference
        url: https://github.com/in-toto/attestation/tree/main/spec/v1
      - type: GitHubRepository
        url: https://github.com/in-toto/attestation
      - type: JSONSchema
        url: json-schema/in-toto-attestation-schema.json
      - type: JSON-LD
        url: json-ld/in-toto-context.jsonld
    tags:
      - Attestation
      - SLSA
      - Specification
      - Supply Chain
  - aid: in-toto:in-toto-python
    name: in-toto Python Reference Implementation
    description: The Python reference implementation of in-toto provides tools and libraries for creating and verifying in-toto metadata. It includes the in-toto-run command for wrapping supply chain steps, in-toto-record for multi-command steps, and in-toto-verify for checking the full supply chain layout. This implementation serves as the canonical reference for the specification.
    humanURL: https://github.com/in-toto/in-toto
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://in-toto.readthedocs.io/
      - type: Getting Started
        url: https://in-toto.io/docs/getting-started/
      - type: GitHubRepository
        url: https://github.com/in-toto/in-toto
    tags:
      - Python
      - Reference Implementation
      - SDK
      - Supply Chain
  - aid: in-toto:in-toto-golang
    name: in-toto Go Implementation
    description: A Go implementation of the in-toto specification that enables supply chain integrity verification in Go-based build and deployment pipelines. It provides the same core functionality as the Python reference implementation including generating link metadata, creating layouts, and verifying supply chains. It supports ITE-7 for X.509-based signing via SPIFFE/SPIRE integration.
    humanURL: https://github.com/in-toto/in-toto-golang
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://pkg.go.dev/github.com/in-toto/in-toto-golang
      - type: GitHubRepository
        url: https://github.com/in-toto/in-toto-golang
    tags:
      - Go
      - Implementation
      - SDK
      - Supply Chain
common:
  - type: Website
    url: https://in-toto.io
  - type: Documentation
    url: https://in-toto.io/docs/
  - type: Getting Started
    url: https://in-toto.io/docs/getting-started/
  - type: Blog
    url: https://in-toto.io/blog/
  - type: Community
    url: https://in-toto.io/community/
  - type: FAQ
    url: https://in-toto.io/docs/faq/
  - type: GitHubOrganization
    url: https://github.com/in-toto
  - type: JSONSchema
    url: json-schema/in-toto-layout-schema.json
  - type: JSONSchema
    url: json-schema/in-toto-link-schema.json
  - type: JSONSchema
    url: json-schema/in-toto-attestation-schema.json
  - type: JSON-LD
    url: json-ld/in-toto-context.jsonld
  - type: Rules
    url: rules/in-toto-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
