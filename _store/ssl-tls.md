---
aid: ssl-tls
name: SSL/TLS
description: SSL/TLS (Secure Sockets Layer / Transport Layer Security) is the cryptographic protocol that secures communications over the internet. TLS 1.3 is the current standard, providing authentication, confidentiality, and integrity for HTTPS, email, VoIP, and other protocols. This covers certificate management, public key infrastructure (PKI), certificate authorities, and TLS configuration APIs from major vendors and open source projects.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SSL/TLS
  - TLS
  - Certificates
  - PKI
  - Cryptography
  - Certificate Authority
  - HTTPS
url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: ssl-tls:lets-encrypt-acme
    name: Let's Encrypt ACME API
    description: Let's Encrypt provides free, automated SSL/TLS certificates via the ACME (Automatic Certificate Management Environment) protocol (RFC 8555). The ACME API enables automated certificate issuance, renewal, and revocation using HTTP-01, DNS-01, and TLS-ALPN-01 challenges to verify domain ownership.
    humanURL: https://letsencrypt.org/
    baseURL: https://acme-v02.api.letsencrypt.org/directory
    tags:
      - SSL/TLS
      - Certificate Authority
      - ACME
      - Let's Encrypt
      - HTTPS
    properties:
      - type: Documentation
        url: https://letsencrypt.org/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/openapi/ssl-tls-certificate-management-openapi.yml
  - aid: ssl-tls:digicert-api
    name: DigiCert Certificate Management API
    description: DigiCert provides enterprise certificate management through a REST API supporting issuance, renewal, revocation, and lifecycle management for OV, EV, DV, and private certificates. Supports CT log integration and ACME protocol.
    humanURL: https://www.digicert.com/
    baseURL: https://www.digicert.com/services/v2
    tags:
      - SSL/TLS
      - Certificate Authority
      - Enterprise PKI
      - DigiCert
    properties:
      - type: Documentation
        url: https://dev.digicert.com/
  - aid: ssl-tls:sectigo-api
    name: Sectigo Certificate Manager API
    description: Sectigo (formerly Comodo CA) provides certificate lifecycle management APIs for enterprise PKI, including S/MIME, code signing, and TLS certificates.
    humanURL: https://sectigo.com/
    baseURL: https://cert-manager.com/api
    tags:
      - SSL/TLS
      - Certificate Authority
      - Enterprise PKI
    properties:
      - type: Documentation
        url: https://sectigo.com/knowledge-base
common:
  - type: Website
    url: https://letsencrypt.org/
  - type: Documentation
    url: https://letsencrypt.org/docs/
  - type: GitHub Organization
    url: https://github.com/letsencrypt
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/openapi/ssl-tls-certificate-management-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/json-schema/ssl-tls-certificate-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/json-structure/ssl-tls-certificate-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/json-ld/ssl-tls-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/rules/ssl-tls-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/capabilities/certificate-lifecycle.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/vocabulary/ssl-tls-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
