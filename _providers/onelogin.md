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
- acting_count: 21
  human_in_the_loop: 1
  name: Onelogin Agentic Access
  operation_count: 31
  slug: onelogin-agentic-access
  summary_line: 31 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: Application management
  name: OneLogin Apps API
  slug: onelogin-apps-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: Multi-Factor Authentication
  name: OneLogin MFA API
  slug: onelogin-mfa-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: OAuth 2.0 token generation and revocation
  name: OneLogin OAuth API
  slug: onelogin-oauth-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: Role management
  name: OneLogin Roles API
  slug: onelogin-roles-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: SAML assertion generation
  name: OneLogin SAML API
  slug: onelogin-saml-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: User management
  name: OneLogin Users API
  slug: onelogin-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OneLogin Apps API
  slug: open-onelogin-apps-api
- collection_type: open
  name: OneLogin Apps MFA API
  slug: open-onelogin-mfa-api
- collection_type: open
  name: OneLogin Apps OAuth API
  slug: open-onelogin-oauth-api
- collection_type: open
  name: OneLogin Apps Roles API
  slug: open-onelogin-roles-api
- collection_type: open
  name: OneLogin Apps SAML API
  slug: open-onelogin-saml-api
- collection_type: open
  name: OneLogin Apps Users API
  slug: open-onelogin-users-api
- collection_type: open
  name: OneLogin API
  slug: open-onelogin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onelogin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onelogin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onelogin-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onelogin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onelogin
- group: company
  title: ''
  type: Website
  url: https://www.onelogin.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.onelogin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.onelogin.com
- group: company
  title: ''
  type: Blog
  url: https://www.onelogin.com/blog/feed
created: '2025-01-08'
description: OneLogin is an identity and access management platform providing single sign-on (SSO), multi-factor authentication, user provisioning, and a RESTful API for managing users, roles, applications, MFA, branding, connectors, reports, SAML assertions, smart hooks, and Vigilance AI.
finops:
- name: Onelogin Finops
  service_category: API
  slug: onelogin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onelogin.png
layout: provider
modified: '2026-05-19'
name: OneLogin
nav: Providers
network: true
overview: 'OneLogin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Apps API, MFA API, OAuth API, and 3 more. Tagged areas include Identity, Access Management, Single Sign-On, Multi-Factor Authentication, and SAML.


  OneLogin''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Onelogin Plans Pricing
  plan_count: 3
  slug: onelogin-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Onelogin Rate Limits
  slug: onelogin-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/onelogin/refs/heads/main/screenshots/onelogin-2026-06-20T190716.png
security:
- kind: authentication
  name: Onelogin Authentication
  slug: onelogin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Onelogin Domain Security
  slug: onelogin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onelogin
tags:
- Identity
- Access Management
- Single Sign-On
- Multi-Factor Authentication
- SAML
- Authentication
website: https://www.onelogin.com
---
