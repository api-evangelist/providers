---
name: SAML
description: SAML (Security Assertion Markup Language) is an XML-based open standard for exchanging authentication and authorization data between identity providers and service providers. Ratified as an OASIS Standard in March 2005, SAML 2.0 enables single sign-on (SSO) across different applications and domains, reducing the need for users to manage multiple sets of credentials. It uses XML digital signatures and encryption to secure assertions exchanged between Identity Providers (IdP) and Service Providers (SP).
url: https://www.oasis-open.org/standard/saml/
tags:
  - Authentication
  - Authorization
  - Federation
  - Identity Management
  - Open Standard
  - Security
  - Single Sign-On
  - SSO
  - XML
created: '2025-01-01'
modified: '2026-05-02'
apis:
  - name: SAML 2.0 SSO HTTP Bindings API
    description: API specification for SAML 2.0 Single Sign-On HTTP bindings including the HTTP Redirect Binding and HTTP POST Binding for AuthnRequest and Response exchange, Assertion Consumer Service, Single Logout, and metadata retrieval as defined in the OASIS SAML 2.0 Bindings specification (saml-bindings-2.0-os).
    tags:
      - Authentication
      - Bindings
      - HTTP
      - Identity Provider
      - Service Provider
      - Single Sign-On
      - SSO
    properties:
      - type: OpenAPI
        url: openapi/saml-sso-bindings.yml
      - type: Documentation
        url: https://docs.oasis-open.org/security/saml/v2.0/saml-bindings-2.0-os.pdf
common:
  - type: Documentation
    url: https://www.oasis-open.org/standard/saml/
    title: SAML 2.0 OASIS Standard
  - type: Documentation
    url: https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html
    title: SAML 2.0 Technical Overview
  - type: Documentation
    url: https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf
    title: SAML 2.0 Core Specification
  - type: Documentation
    url: https://docs.oasis-open.org/security/saml/v2.0/saml-bindings-2.0-os.pdf
    title: SAML 2.0 Bindings Specification
  - type: Documentation
    url: https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf
    title: SAML 2.0 Profiles Specification
  - type: JSONSchema
    url: json-schema/saml-entity-descriptor.json
    title: SAML 2.0 EntityDescriptor Metadata
  - type: JSONSchema
    url: json-schema/saml-authn-request.json
    title: SAML 2.0 AuthnRequest
  - type: JSONSchema
    url: json-schema/saml-assertion.json
    title: SAML 2.0 Assertion
  - type: JSONLDContext
    url: json-ld/saml-context.jsonld
    title: SAML 2.0 JSON-LD Context
  - type: JSONStructure
    url: json-structure/saml-assertion-structure.json
    title: SAML 2.0 Assertion Structure
  - type: SpectralRules
    url: rules/saml-rules.yml
    title: SAML API Spectral Rules
  - type: NaftikoCapability
    url: capabilities/single-sign-on.yaml
    title: SAML Single Sign-On Capability
  - type: Example
    url: examples/saml-sso-redirect-example.json
    title: SAML SSO HTTP Redirect Binding Example
  - type: Vocabulary
    url: vocabulary/saml-vocabulary.yml
    title: SAML 2.0 Vocabulary
---
