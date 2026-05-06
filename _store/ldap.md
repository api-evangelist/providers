---
aid: ldap
name: LDAP
description: LDAP (Lightweight Directory Access Protocol) is an industry-standard application protocol for accessing and maintaining distributed directory information services over an IP network, formally specified in RFC 4511. It plays a critical role in protecting organizational assets and maintaining a strong security posture through centralized authentication, authorization, and identity management. LDAP underlies directory services such as Microsoft Active Directory, OpenLDAP, and 389 Directory Server, and is widely used for single sign-on, enterprise address books, and application identity stores.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Directory Services
  - Identity Management
  - LDAP
  - Protocol
  - Single Sign-On
  - Standard
url: https://raw.githubusercontent.com/api-evangelist/ldap/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ldap:ldap
    name: LDAP
    description: Lightweight Directory Access Protocol for accessing and maintaining distributed directory information services over an IP network. The protocol defines bind, search, compare, add, delete, modify, and modifyDN operations carried over a connection-oriented transport.
    humanURL: https://ldap.com/
    tags:
      - Authentication
      - Directory Services
      - Identity Management
      - Protocol
    properties:
      - type: Documentation
        url: https://ldap.com/
      - type: Specification
        url: https://datatracker.ietf.org/doc/html/rfc4511
      - type: Wikipedia
        url: https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol
common:
  - type: Website
    url: https://ldap.com/
  - type: Documentation
    url: https://ldap.com/
  - type: Specification
    url: https://datatracker.ietf.org/doc/html/rfc4511
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
