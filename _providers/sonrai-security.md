---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
api_count: 1
apis:
- description: GraphQL API for the Sonrai Cloud Permissions Firewall platform — exempt, protect, quarantine, and disable cloud IAM access. Bearer-token authenticated; reference documentation is gated behind the Auth
  name: Sonrai GraphQL API
  slug: sonrai-graphql-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://sonraisecurity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sonraisecurity.com/cpf-public/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonraisecurity.com/cpf-public/
- group: commercial
  title: ''
  type: Pricing
  url: https://sonraisecurity.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.sonraisecurity.com/SignUp
- group: start
  title: ''
  type: Login
  url: https://app.sonraisecurity.com/Login
- group: company
  title: ''
  type: Blog
  url: https://sonraisecurity.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://sonraisecurity.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sonraisecurity.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sonraisecurity.com/terms-of-service/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonraisecurity
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonrai-security-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sonrai-security-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonrai-security-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sonrai-security-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonrai-security-llms.txt
created: '2026-07-17'
description: Sonrai Security is a cloud identity and access security company whose Cloud Permissions Firewall (CPF) enforces least-privilege access across AWS, Azure, and Google Cloud by quarantining unused IAM identities, protecting sensitive permissions, and disabling unused services and regions without disrupting developers. The platform also ships WALLy, an AI-driven Cloud PAM agent that grants just-in-time privileged access through Slack and Teams, and offers agentic AI security consulting. Sonrai exposes a GraphQL API for the platform (endpoint https://app.sonraisecurity.com/graphql), documented in its CPF developer docs; platform and API access authenticate through an Auth0-backed OpenID Connect identity provider at login.sonraisecurity.com. Sonrai Security is backed by Menlo Ventures.
image: https://sonraisecurity.com/wp-content/uploads/sonrai-logo-sharing.png
layout: provider
modified: '2026-07-21'
name: Sonrai Security
nav: Providers
network: true
overview: 'Sonrai Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, Identity and Access Management, and CIEM.


  Sonrai Security''s developer surface includes documentation, pricing, signup flow, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/sonrai-security/refs/heads/main/screenshots/sonrai-security-2026-09-02T160229.png
security:
- kind: authentication
  name: Sonrai Security Authentication
  slug: sonrai-security-authentication
  summary_line: oauth2/openIdConnect/http · 2 schemes
- kind: domain-security
  name: Sonrai Security Domain Security
  slug: sonrai-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonrai-security
tags:
- Company
- Security
- Cloud Security
- Identity and Access Management
- CIEM
- Cloud Permissions
- Least Privilege
- GraphQL
- IAM
website: https://sonraisecurity.com
---
