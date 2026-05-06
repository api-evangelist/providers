---
aid: openssf
name: OpenSSF
description: The Open Source Security Foundation (OpenSSF) is a collaborative initiative under the Linux Foundation dedicated to improving the security of open source software. It brings together industry leaders, developers, and security experts to address vulnerabilities, enhance supply chain security, and develop security tools and best practices. OpenSSF stewards a number of projects with public REST APIs, including the OSV (Open Source Vulnerabilities) database, the Scorecard automated security health-check service, and Sigstore signing infrastructure.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Linux Foundation
  - Open Source
  - Security
  - Supply Chain
  - Vulnerabilities
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openssf:osv-api
    name: OSV (Open Source Vulnerabilities) API
    description: OSV is an OpenSSF-hosted distributed vulnerability database and query infrastructure. The OSV API at api.osv.dev exposes vulnerability records keyed to specific package versions or commits across multiple ecosystems including npm, PyPI, Maven, Go, NuGet, RubyGems, Cargo, Packagist, Hex, OSS-Fuzz, Linux, Android, and GitHub Actions.
    humanURL: https://osv.dev/
    baseURL: https://api.osv.dev
    tags:
      - Vulnerabilities
      - Supply Chain
      - Database
      - Open Source
    properties:
      - type: Documentation
        url: https://google.github.io/osv.dev/api/
      - type: Documentation
        url: https://osv.dev/
      - type: GitHubRepository
        url: https://github.com/google/osv.dev
      - type: GitHubRepository
        url: https://github.com/ossf/osv-schema
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/openapi/openssf-osv-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/json-schema/openssf-osv-vulnerability-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/json-ld/openssf-context.jsonld
  - aid: openssf:scorecard-api
    name: OpenSSF Scorecard API
    description: The OpenSSF Scorecard API returns automated security health metrics for public open source repositories. Scorecard runs a series of checks (e.g., Branch-Protection, Code-Review, Pinned-Dependencies, Signed-Releases, Token-Permissions, Vulnerabilities) and exposes per-check scores plus an aggregate 0-10 score via api.securityscorecards.dev.
    humanURL: https://scorecard.dev/
    baseURL: https://api.securityscorecards.dev
    tags:
      - Security Health
      - Repositories
      - Supply Chain
    properties:
      - type: Documentation
        url: https://github.com/ossf/scorecard
      - type: Documentation
        url: https://scorecard.dev/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/openapi/openssf-scorecard-openapi.yml
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/openssf/refs/heads/main/json-ld/openssf-context.jsonld
  - aid: openssf:sigstore-api
    name: Sigstore Public Good APIs
    description: Sigstore is an OpenSSF-hosted standard and service for signing, verifying, and protecting software. The public-good Sigstore instance exposes Fulcio (code-signing certificate authority) and Rekor (transparency log) APIs that can be queried programmatically to inspect signing certificates and transparency log entries.
    humanURL: https://www.sigstore.dev/
    baseURL: https://rekor.sigstore.dev
    tags:
      - Signing
      - Transparency Log
      - Supply Chain
    properties:
      - type: Documentation
        url: https://docs.sigstore.dev/
      - type: Documentation
        url: https://docs.sigstore.dev/logging/overview/
      - type: GitHubOrganization
        url: https://github.com/sigstore
  - aid: openssf:guac-api
    name: GUAC (Graph for Understanding Artifact Composition)
    description: GUAC aggregates software supply-chain security metadata (SBOMs, attestations, vulnerabilities, signatures) into a queryable graph. GUAC exposes a GraphQL API for supply-chain queries when self-hosted.
    humanURL: https://guac.sh/
    baseURL: https://guac.sh
    tags:
      - SBOM
      - Supply Chain
      - GraphQL
    properties:
      - type: Documentation
        url: https://docs.guac.sh/
      - type: GitHubRepository
        url: https://github.com/guacsec/guac
common:
  - type: Website
    name: OpenSSF
    url: https://openssf.org/
  - type: Documentation
    name: OpenSSF Documentation
    url: https://openssf.org/resources/
  - type: Portal
    name: Projects Directory
    url: https://openssf.org/projects/
  - type: Blog
    name: OpenSSF Blog
    url: https://openssf.org/blog/
  - type: GitHubOrganization
    name: OpenSSF GitHub
    url: https://github.com/ossf
  - type: GitHubRepository
    name: OSV Schema
    url: https://github.com/ossf/osv-schema
  - type: GitHubRepository
    name: Scorecard
    url: https://github.com/ossf/scorecard
  - type: GitHubOrganization
    name: Sigstore GitHub
    url: https://github.com/sigstore
  - type: License
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Community
    name: OpenSSF Community
    url: https://openssf.org/community/
  - type: Slack
    name: OpenSSF Slack
    url: https://slack.openssf.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
