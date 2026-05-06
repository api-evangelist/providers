---
aid: spiffe
name: SPIFFE
description: Secure Production Identity Framework for Everyone (SPIFFE) is a set of open-source standards for securely identifying software systems in dynamic and heterogeneous environments through platform-agnostic, cryptographic identities. SPIFFE defines the SPIFFE ID URI format, the X.509 SVID and JWT SVID identity document formats, and the Workload API for issuing and rotating identities without secrets or passwords. SPIFFE is a graduated CNCF project.
url: https://spiffe.io/
tags:
  - Authentication
  - Cloud Native
  - Graduated
  - Identity
  - Security
  - Zero Trust
created: '2025'
modified: '2026-05-02'
specificationVersion: '0.19'
type: Index
apis:
  - aid: spiffe:spiffe-workload-api
    name: SPIFFE Workload API
    description: The SPIFFE Workload API is a gRPC streaming interface through which workloads request and receive SPIFFE Verifiable Identity Documents (SVIDs) including X.509-SVIDs and JWT-SVIDs, as well as trust bundle updates. It enables software to obtain cryptographic identities at runtime without requiring secrets to be embedded in configuration or code.
    humanURL: https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE_Workload_API.md
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
      - type: Reference
        url: https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE_Workload_API.md
      - type: AsyncAPI
        url: asyncapi/spiffe-workload-asyncapi.yml
      - type: GitHubRepository
        url: https://github.com/spiffe/spiffe
    tags:
      - gRPC
      - Identity
      - JWT
      - Workload
      - X.509
  - aid: spiffe:spiffe-x509-svid-api
    name: SPIFFE X.509 SVID
    description: The SPIFFE X.509 SVID (SPIFFE Verifiable Identity Document) is a standard for encoding SPIFFE identities into X.509 certificates. The Subject Alternative Name field carries the SPIFFE ID URI, enabling mutual TLS authentication between workloads using standard X.509 certificate validation libraries.
    humanURL: https://github.com/spiffe/spiffe/blob/main/standards/X509-SVID.md
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/spiffe-about/svid/
      - type: Reference
        url: https://github.com/spiffe/spiffe/blob/main/standards/X509-SVID.md
      - type: GitHubRepository
        url: https://github.com/spiffe/spiffe
    tags:
      - Certificate
      - Identity
      - mTLS
      - Security
      - X.509
  - aid: spiffe:spiffe-jwt-svid-api
    name: SPIFFE JWT SVID
    description: The SPIFFE JWT SVID standard defines a format for encoding SPIFFE identities as JSON Web Tokens. JWT-SVIDs are used in scenarios where X.509 certificates are not practical, such as HTTP header-based authentication between services or for passing identity across trust domain boundaries.
    humanURL: https://github.com/spiffe/spiffe/blob/main/standards/JWT-SVID.md
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/spiffe-about/svid/
      - type: Reference
        url: https://github.com/spiffe/spiffe/blob/main/standards/JWT-SVID.md
      - type: GitHubRepository
        url: https://github.com/spiffe/spiffe
    tags:
      - Authentication
      - Identity
      - JWT
      - Security
  - aid: spiffe:spiffe-federation-api
    name: SPIFFE Federation API
    description: The SPIFFE Federation API defines how SPIFFE trust domains exchange trust bundle information to enable cross-domain workload authentication. It specifies the SPIFFE Trust Domain and Bundle endpoint format, allowing systems in different trust domains to establish mutual trust and authenticate workloads across organizational or infrastructure boundaries.
    humanURL: https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE_Trust_Domain_and_Bundle.md
    properties:
      - type: Documentation
        url: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
      - type: Reference
        url: https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE_Trust_Domain_and_Bundle.md
      - type: OpenAPI
        url: openapi/spiffe-federation-openapi.yml
      - type: GitHubRepository
        url: https://github.com/spiffe/spiffe
      - type: SpectralRules
        url: rules/spiffe-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/workload-identity.yaml
    tags:
      - Cross-Domain
      - Federation
      - Identity
      - Security
      - Trust Domain
common:
  - type: JSONSchema
    url: json-schema/spiffe-svid-schema.json
  - type: JSON-LD
    url: json-ld/spiffe-context.jsonld
  - type: SpectralRules
    url: rules/spiffe-rules.yml
  - type: Vocabulary
    url: vocabulary/spiffe-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/workload-identity.yaml
  - type: Website
    url: https://spiffe.io/
  - type: Documentation
    url: https://spiffe.io/docs/latest/
  - type: GettingStarted
    url: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
  - type: GitHubOrganization
    url: https://github.com/spiffe
  - type: GitHubRepository
    url: https://github.com/spiffe/spiffe
  - type: Community
    url: https://spiffe.io/community/
  - type: Slack
    url: https://slack.spiffe.io
  - type: Blog
    url: https://spiffe.io/blog/
  - type: Security
    url: https://github.com/spiffe/spiffe/blob/main/SECURITY.md
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/spiffe
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
