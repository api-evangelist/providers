---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Bastion Agentic Access
  operation_count: 7
  slug: microsoft-azure-bastion-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Bastion Hosts operations
  name: Azure Bastion Bastion Hosts API
  slug: microsoft-azure-bastion-bastion-hosts-api
- description: Operations operations
  name: Azure Bastion Operations API
  slug: microsoft-azure-bastion-operations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Bastion REST API
  slug: open-microsoft-azure-bastion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-bastion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-bastion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-bastion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-bastion-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
created: '2026-03-13'
description: Learn more about [Virtual Networks Bastion Hosts Operations]. How to [Create Or Update,Delete,Get,List,List By Resource Group,Update Tags].
finops:
- name: Microsoft Azure Bastion Finops
  service_category: API
  slug: microsoft-azure-bastion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-bastion.png
layout: provider
modified: '2026-05-19'
name: Azure Bastion
nav: Providers
network: true
overview: 'Azure Bastion publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bastion Hosts API and Operations API. Tagged areas include Bastion, RDP, Remote Access, Secure Access, and SSH.


  Azure Bastion''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Bastion Plans Pricing
  plan_count: 3
  slug: microsoft-azure-bastion-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Microsoft Azure Bastion Rate Limits
  slug: microsoft-azure-bastion-rate-limits
scopes:
- name: Microsoft Azure Bastion Scopes
  scope_count: 1
  slug: microsoft-azure-bastion-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 45.5
  delta: 3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.1
    developer_ergonomics: 26.1
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-bastion/refs/heads/main/screenshots/microsoft-azure-bastion-2026-06-20T185400.png
security:
- kind: authentication
  name: Microsoft Azure Bastion Authentication
  slug: microsoft-azure-bastion-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Bastion Domain Security
  slug: microsoft-azure-bastion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-bastion
tags:
- Bastion
- RDP
- Remote Access
- Secure Access
- SSH
website: https://portal.azure.com/
---
