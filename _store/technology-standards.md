---
aid: technology-standards
name: Technology Standards
description: Technology Standards covers the landscape of formal technical standards, protocols, and normative specifications developed by international standards bodies including IEEE, IETF, W3C, ISO, OASIS, and the Linux Foundation. These standards define how technology systems interoperate, communicate, and behave. In the API economy, key standards govern data formats (JSON, XML, CSV), communication protocols (HTTP/2, HTTP/3, WebSocket, gRPC), security (OAuth 2.0, OpenID Connect, TLS), identity (SAML, SCIM), and API description (OpenAPI, AsyncAPI). Technology standards ensure interoperability, reduce vendor lock-in, and form the foundation of the modern internet and API ecosystem.
url: https://raw.githubusercontent.com/api-evangelist/technology-standards/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - IEEE
  - IETF
  - ISO
  - Protocols
  - Standards
  - Technology Standards
  - W3C
apis:
  - aid: technology-standards:ietf-standards
    name: IETF Internet Standards
    description: The Internet Engineering Task Force (IETF) produces Internet Standards (STDs) and Best Current Practices (BCPs) covering core internet protocols including HTTP, TLS, OAuth, OpenID Connect, JSON, and many more. IETF RFCs form the normative basis for most web API standards. Key API-related RFCs include RFC 9110 (HTTP Semantics), RFC 6749 (OAuth 2.0), RFC 7519 (JWT), RFC 7946 (GeoJSON), and RFC 8259 (JSON).
    humanURL: https://www.ietf.org/
    baseURL: https://datatracker.ietf.org/api/v1
    tags:
      - HTTP
      - IETF
      - Internet Standards
      - OAuth
      - Protocols
      - RFC
      - TLS
    properties:
      - type: Documentation
        url: https://www.ietf.org/standards/
      - type: Website
        url: https://www.ietf.org/
      - type: API
        url: https://datatracker.ietf.org/api/v1/
  - aid: technology-standards:w3c-standards
    name: W3C Web Standards
    description: The World Wide Web Consortium (W3C) leads the World Wide Web to its full potential by developing open standards for web technologies. W3C standards critical to APIs include CORS (Cross-Origin Resource Sharing), Web Authentication (WebAuthn), Linked Data (RDF, JSON-LD), and the Activity Streams vocabulary. The W3C also maintains standards for semantic web technologies including OWL and SPARQL.
    humanURL: https://www.w3.org/standards/
    baseURL: https://www.w3.org
    tags:
      - CORS
      - Linked Data
      - Semantic Web
      - W3C
      - Web Standards
    properties:
      - type: Documentation
        url: https://www.w3.org/TR/
      - type: Website
        url: https://www.w3.org/
      - type: GitHub
        url: https://github.com/w3c
  - aid: technology-standards:ieee-standards
    name: IEEE Standards
    description: The Institute of Electrical and Electronics Engineers (IEEE) develops standards for electronics, electrical engineering, and computer science. IEEE standards relevant to APIs and technology include IEEE 802 (networking), IEEE P2510 (IoT data trust), and standards around software engineering lifecycle processes.
    humanURL: https://standards.ieee.org/
    baseURL: https://standards.ieee.org
    tags:
      - Computer Science
      - Electrical Engineering
      - IEEE
      - Networking
    properties:
      - type: Documentation
        url: https://standards.ieee.org/
      - type: Website
        url: https://standards.ieee.org/
  - aid: technology-standards:oasis-standards
    name: OASIS Open Standards
    description: OASIS Open is a nonprofit standards development organization that advances the creation, convergence, and adoption of open standards for the global information society. OASIS standards relevant to APIs include SAML (Security Assertion Markup Language), OData (Open Data Protocol), WS-Security, MQTT, AMQP, and OpenDocument.
    humanURL: https://www.oasis-open.org/
    baseURL: https://www.oasis-open.org
    tags:
      - AMQP
      - MQTT
      - OData
      - OASIS
      - SAML
    properties:
      - type: Documentation
        url: https://www.oasis-open.org/standards/
      - type: Website
        url: https://www.oasis-open.org/
      - type: GitHub
        url: https://github.com/oasis-tcs
  - aid: technology-standards:oauth-openid
    name: OAuth and OpenID Connect
    description: OAuth 2.0 (RFC 6749) is the industry-standard protocol for authorization, enabling third-party applications to obtain limited access to web services. OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0 that enables clients to verify the identity of end users and obtain profile information. Together they form the foundation for API security and developer authentication across the modern web.
    humanURL: https://oauth.net/2/
    baseURL: https://oauth.net
    tags:
      - Authentication
      - Authorization
      - Identity
      - OAuth
      - OpenID Connect
      - Security
    properties:
      - type: Documentation
        url: https://oauth.net/2/
      - type: Website
        url: https://oauth.net/
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc6749
common:
  - type: Website
    url: https://www.ietf.org/
  - type: Website
    url: https://www.w3.org/
  - type: Website
    url: https://standards.ieee.org/
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/technology-standards/refs/heads/main/vocabulary/technology-standards-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/technology-standards/refs/heads/main/json-ld/technology-standards-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
