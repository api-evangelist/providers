---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Lightweight Directory Access Protocol for accessing and maintaining distributed directory information services over an IP network. The protocol defines bind, search, compare, add, delete, modify, and '
  name: LDAP
  slug: ldap
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ldap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ldap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ldap.com/
- group: docs
  title: ''
  type: Specification
  url: https://datatracker.ietf.org/doc/html/rfc4511
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol
- group: company
  title: ''
  type: Blog
  url: https://ldap.com/feed/
created: '2025-01-01'
description: LDAP (Lightweight Directory Access Protocol) is an industry-standard application protocol for accessing and maintaining distributed directory information services over an IP network, formally specified in RFC 4511. It plays a critical role in protecting organizational assets and maintaining a strong security posture through centralized authentication, authorization, and identity management. LDAP underlies directory services such as Microsoft Active Directory, OpenLDAP, and 389 Directory Server, and is widely used for single sign-on, enterprise address books, and application identity stores.
finops:
- name: Ldap Finops
  service_category: API
  slug: ldap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ldap.png
layout: provider
modified: '2026-04-28'
name: LDAP
nav: Providers
network: true
overview: 'LDAP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Authorization, Directory Services, Identity Management, and LDAP.


  LDAP''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Ldap Plans Pricing
  plan_count: 3
  slug: ldap-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Ldap Rate Limits
  slug: ldap-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/ldap/refs/heads/main/screenshots/ldap-2026-06-20T184344.png
security:
- kind: domain-security
  name: Ldap Domain Security
  slug: ldap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ldap
tags:
- Authentication
- Authorization
- Directory Services
- Identity Management
- LDAP
- Protocol
- Single Sign-On
- Standard
website: https://ldap.com/
---
