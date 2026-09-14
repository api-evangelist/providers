---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the True & Co Shopify storefront: a hosted Universal Commerce Protocol (UCP) MCP endpoint for catalog search, cart, and checkout, backed by Shopify Customer Account O'
  name: True & Co UCP Agent Commerce
  slug: true-co-ucp-agent-commerce
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.trueandco.com/
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/true-and-co-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/true-and-co-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/true-and-co-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/true-and-co-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/true-and-co-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/true-and-co-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-and-co-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trueandco.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trueandco.com/policies/privacy-policy
created: '2026-07-17'
description: 'True & Co is a direct-to-consumer women''s intimates and lingerie brand, originally venture-backed (Cowboy Ventures, Uncork Capital) and now operating under PVH Corp. It sells bras, underwear, and loungewear online through a Shopify-hosted storefront at trueandco.com. The store exposes no traditional developer API, but it does expose a modern agent-commerce surface: a hosted Universal Commerce Protocol (UCP) MCP endpoint for catalog, cart, and checkout, Shopify Customer Account OAuth 2.0 / OIDC for buyer identity, a public read-only storefront JSON surface, and an agent-facing llms.txt / agents.md.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/true-and-co.png
layout: provider
modified: '2026-07-21'
name: True & Co
nav: Providers
network: true
overview: 'True & Co publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Apparel.


  True & Co''s developer surface includes authentication and 9 more developer resources.'
random_paper: 5
scopes:
- name: True And Co Scopes
  scope_count: 0
  slug: true-and-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/true-and-co/refs/heads/main/screenshots/true-and-co-2026-09-02T164331.png
security:
- kind: authentication
  name: True And Co Authentication
  slug: true-and-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: True And Co Domain Security
  slug: true-and-co-domain-security
  summary_line: no transport/DNS hardening detected
slug: true-and-co
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Apparel
- Intimates
- Agentic Commerce
- Shopify
- MCP
website: https://www.trueandco.com/
---
