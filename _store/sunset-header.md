---
aid: sunset-header
name: Sunset Header
description: The Sunset HTTP header field (RFC 8594) is an informational IETF specification that allows servers to communicate to clients that a URI is likely to become unresponsive at a specified future point in time. Published in May 2019, it provides a standardized mechanism for API deprecation signaling, enabling clients to plan migrations before service retirement. The header value is an HTTP-date timestamp following RFC 7231 syntax. A complementary sunset link relation type allows resources to reference documentation covering the sunset policy, migration guidance, and alternatives. RFC 9745 (Deprecation HTTP Header Field) extends this pattern by providing a two-phase deprecation + sunset lifecycle where Deprecation marks the start of deprecation and Sunset marks the end-of-life. These two headers are widely adopted in REST API governance practices and API lifecycle management tooling.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Deprecation
  - HTTP Headers
  - RFC 8594
  - RFC 9745
  - API Lifecycle
  - REST APIs
  - Standards
url: https://raw.githubusercontent.com/api-evangelist/sunset-header/refs/heads/main/apis.yml
created: '2026-03-29'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sunset-header:sunset-header
    name: Sunset Header (RFC 8594)
    description: The Sunset HTTP header field (RFC 8594) communicates the deprecation timeline of API endpoints to consumers. The header value is an HTTP-date timestamp indicating when a URI is expected to become unresponsive. It is accompanied by a sunset link relation type for linking to deprecation documentation and migration guidance.
    humanURL: https://datatracker.ietf.org/doc/html/rfc8594
    tags:
      - HTTP Headers
      - API Deprecation
      - RFC 8594
      - Sunset
      - API Lifecycle
    properties:
      - type: Documentation
        url: https://datatracker.ietf.org/doc/html/rfc8594
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc8594
  - aid: sunset-header:deprecation-header
    name: Deprecation HTTP Header Field (RFC 9745)
    description: RFC 9745 defines the Deprecation HTTP response header field, which signals to clients that a resource has been or will be deprecated. It complements the Sunset header by marking the start of the deprecation lifecycle. The header value is a structured date (Unix timestamp per RFC 9651). The Sunset timestamp, if present, must not be earlier than the Deprecation timestamp.
    humanURL: https://www.rfc-editor.org/rfc/rfc9745.html
    tags:
      - HTTP Headers
      - API Deprecation
      - RFC 9745
      - Deprecation
      - API Lifecycle
    properties:
      - type: Documentation
        url: https://www.rfc-editor.org/rfc/rfc9745.html
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc9745
common:
  - type: Website
    url: https://datatracker.ietf.org/doc/html/rfc8594
  - type: IETF Specification
    url: https://www.rfc-editor.org/rfc/rfc8594
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
