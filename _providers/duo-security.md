---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Duo Security Agentic Access
  operation_count: 32
  slug: duo-security-agentic-access
  summary_line: 32 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: Batched operations
  name: Duo Security Bulk API
  slug: duo-security-bulk-api
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: Bypass code generation and listing
  name: Duo Security Bypass Codes API
  slug: duo-security-bypass-codes-api
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: Group management and membership
  name: Duo Security Groups API
  slug: duo-security-groups-api
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: Phone device management
  name: Duo Security Phones API
  slug: duo-security-phones-api
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: Hardware token management
  name: Duo Security Tokens API
  slug: duo-security-tokens-api
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: User account management
  name: Duo Security Users API
  slug: duo-security-users-api
- baseURL: https://api-XXXXXXXX.duosecurity.com
  baseurl_source: declared
  description: WebAuthn credential management
  name: Duo Security WebAuthn API
  slug: duo-security-webauthn-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Duo Admin API
  slug: open-duo-admin-api
- collection_type: open
  name: Duo Admin Bulk API
  slug: open-duo-security-bulk-api
- collection_type: open
  name: Duo Admin Bulk Bypass Codes API
  slug: open-duo-security-bypass-codes-api
- collection_type: open
  name: Duo Admin Bulk Groups API
  slug: open-duo-security-groups-api
- collection_type: open
  name: Duo Admin Bulk Phones API
  slug: open-duo-security-phones-api
- collection_type: open
  name: Duo Admin Bulk Tokens API
  slug: open-duo-security-tokens-api
- collection_type: open
  name: Duo Admin Bulk Users API
  slug: open-duo-security-users-api
- collection_type: open
  name: Duo Admin Bulk WebAuthn API
  slug: open-duo-security-webauthn-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/duo-security-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/duo-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/duo-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duo-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duo-security-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/duosec
- group: company
  title: ''
  type: Website
  url: https://duo.com
- group: docs
  title: ''
  type: Documentation
  url: https://duo.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duosecurity
- group: company
  title: ''
  type: Blog
  url: https://duo.com/feed
created: '2026-03-25'
description: Duo Security is a multi-factor authentication and zero trust security platform from Cisco for securing access to applications and APIs.
finops:
- name: Duo Security Finops
  service_category: API
  slug: duo-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duo-security.png
layout: provider
modified: '2026-08-19'
name: Duo Security
nav: Providers
network: true
overview: 'Duo Security publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Bypass Codes API, Groups API, and 4 more. Tagged areas include Authentication, MFA, Zero Trust, and Identity.


  Duo Security''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Duo Security Plans Pricing
  plan_count: 3
  slug: duo-security-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Duo Security Rate Limits
  slug: duo-security-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/duo-security/refs/heads/main/screenshots/duo-security-2026-06-20T180323.png
security:
- kind: authentication
  name: Duo Security Authentication
  slug: duo-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duo Security Domain Security
  slug: duo-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Duo Security Vulnerability Disclosure
  slug: duo-security-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Duo Security Trust Center
  slug: duo-security-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: duo-security
tags:
- Authentication
- MFA
- Zero Trust
- Identity
website: https://duo.com
---
