---
name: SSO
description: Single Sign-On (SSO) is an authentication technology that allows users to log in once and gain access to multiple related applications and services without re-authenticating. SSO implementations rely on protocols such as SAML 2.0, OpenID Connect (OIDC), and OAuth 2.0. Major identity providers including Okta, Microsoft Entra ID, Google, Ping Identity, Auth0, and Keycloak expose SSO APIs that allow applications to integrate federated authentication, token exchange, assertion validation, and session management.
url: https://github.com/api-evangelist/sso
tags:
  - Authentication
  - Authorization
  - Identity
  - OAuth
  - OIDC
  - SAML
  - Security
  - Single Sign-On
  - SSO
created: '2025-01-01'
modified: '2026-05-02'
apis:
  - aid: sso:saml-authentication
    name: SAML SSO Authentication API
    tags:
      - Authentication
      - Federation
      - Identity
      - SAML
      - Single Sign-On
      - SSO
    baseURL: https://your-idp.example.com
    humanURL: https://www.oasis-open.org/standards#samlv2.0
    description: The SAML 2.0 Single Sign-On API enables service providers and identity providers to exchange authentication assertions via XML-signed messages. It supports HTTP Redirect Binding and HTTP POST Binding for AuthnRequest and Response flows, Assertion Consumer Service (ACS) endpoints, Single Logout (SLO), and IdP metadata retrieval as defined by the OASIS SAML 2.0 specification.
    properties:
      - url: https://www.oasis-open.org/standards#samlv2.0
        type: Documentation
      - url: https://wiki.oasis-open.org/security/FrontPage
        type: Documentation
      - url: openapi/sso-saml-openapi.yml
        type: OpenAPI
  - aid: sso:oidc-authentication
    name: OpenID Connect (OIDC) Authentication API
    tags:
      - Authentication
      - Identity
      - JWT
      - OAuth
      - OIDC
      - Single Sign-On
      - SSO
    baseURL: https://your-idp.example.com
    humanURL: https://openid.net/connect/
    description: The OpenID Connect (OIDC) API is a lightweight identity layer built on top of OAuth 2.0. It enables applications to verify user identity through the Authorization Code Flow, Implicit Flow, and Hybrid Flow. Key endpoints include the Authorization Endpoint, Token Endpoint, UserInfo Endpoint, and JWKS URI for token signature verification. OIDC is supported by all major identity providers.
    properties:
      - url: https://openid.net/connect/
        type: Documentation
      - url: https://openid.net/developers/specs/
        type: Specification
      - url: openapi/sso-oidc-openapi.yml
        type: OpenAPI
common:
  - url: https://www.oasis-open.org/standards#samlv2.0
    type: Specification
  - url: https://openid.net/connect/
    type: Specification
  - url: https://oauth.net/2/
    type: Specification
  - url: https://github.com/api-evangelist/sso
    type: GitHubOrg
  - url: json-ld/sso-context.jsonld
    type: JSON-LD
  - url: json-schema/sso-saml-assertion-schema.json
    type: JSONSchema
  - url: json-schema/sso-oidc-token-schema.json
    type: JSONSchema
  - url: vocabulary/sso-vocabulary.yml
    type: Vocabulary
  - url: rules/sso-rules.yml
    type: SpectralRules
---
