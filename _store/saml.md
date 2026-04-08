---
aid: saml
url: https://raw.githubusercontent.com/api-evangelist/saml/refs/heads/main/apis.yml
apis:
- name: SAML 2.0 SSO HTTP Bindings API
  description: API specification for SAML 2.0 Single Sign-On HTTP bindings including the HTTP Redirect Binding and HTTP POST Binding for AuthnRequest and Response exchange, Assertion Consumer Service, Single Logout, and metadata retrieval as defined in the OASIS SAML 2.0 Bindings specification.
  properties:
  - type: x-openapi
    url: openapi/saml-sso-bindings.yml
name: SAML
tags:
- Authentication
- Identity Management
- Security
- SSO
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAML (Security Assertion Markup Language) is an XML-based open standard for exchanging authentication and authorization data between identity providers and service providers. It enables single sign-on (SSO) across different applications and domains, reducing the need for users to manage multiple sets of credentials.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

