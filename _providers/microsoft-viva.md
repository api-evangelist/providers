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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Viva Connections provides a personalized employee experience gateway built on SharePoint. Developers can create custom dashboard cards using Adaptive Card Extensions (ACEs) in the SharePoint Framework
  name: Viva Connections API
  slug: connections-api
- description: The Viva Learning API through Microsoft Graph enables integration of third-party learning content providers with Microsoft Viva Learning. Developers can register learning providers, sync course catalo
  name: Viva Learning API
  slug: learning-api
- description: Viva Insights provides data-driven insights about work patterns and collaboration habits. The API surfaces analytics about meeting time, focus hours, collaboration patterns, and wellbeing metrics to h
  name: Viva Insights API
  slug: insights-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-viva-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-viva
- group: start
  title: ''
  type: Portal
  url: https://www.microsoft365.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-viva
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/viva/
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
created: '2024-01-01'
description: Microsoft Viva is an employee experience platform built on Microsoft 365 and Teams. It provides APIs for Viva Connections, Viva Learning, and Viva Insights to integrate employee experience capabilities into custom applications.
finops:
- name: Microsoft Viva Finops
  service_category: API
  slug: microsoft-viva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-viva.png
layout: provider
modified: '2026-04-28'
name: Microsoft Viva
nav: Providers
network: true
overview: 'Microsoft Viva publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Employee Experience, Insights, Learning, Microsoft, and Microsoft 365.


  Microsoft Viva''s developer surface includes developer portal, documentation, support, and 6 more developer resources.'
plans:
- name: Microsoft Viva Plans Pricing
  plan_count: 3
  slug: microsoft-viva-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 5
  name: Microsoft Viva Rate Limits
  slug: microsoft-viva-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 19.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-viva/refs/heads/main/screenshots/microsoft-viva-2026-06-20T185542.png
security:
- kind: domain-security
  name: Microsoft Viva Domain Security
  slug: microsoft-viva-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: microsoft-viva
tags:
- Employee Experience
- Insights
- Learning
- Microsoft
- Microsoft 365
website: https://www.microsoft.com/en-us/microsoft-viva
---
