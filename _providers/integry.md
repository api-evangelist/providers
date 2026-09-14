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
- acting_count: 6
  human_in_the_loop: 0
  name: Integry Agentic Access
  operation_count: 6
  slug: integry-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.integry.io
  baseurl_source: declared
  description: The Apps API from Integry — 2 operation(s) for apps.
  name: Integry Apps API
  slug: integry-apps-api
- baseURL: https://api.integry.io
  baseurl_source: declared
  description: The Functions API from Integry — 4 operation(s) for functions.
  name: Integry Functions API
  slug: integry-functions-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Integry Apps API
  slug: open-integry-apps-api
- collection_type: open
  name: Integry Apps Functions API
  slug: open-integry-functions-api
- collection_type: open
  name: Integry API
  slug: open-integry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/integry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/integry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integryio
- group: company
  title: ''
  type: Website
  url: https://integry.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.integry.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IntegryHQ
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.integry.ai/llms.txt
created: '2026-03-27'
description: Integry is an embedded integration platform that lets SaaS companies offer native integrations to their users.
finops:
- name: Integry Finops
  service_category: API
  slug: integry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/integry.png
layout: provider
modified: '2026-05-19'
name: Integry
nav: Providers
network: true
overview: 'Integry publishes 2 APIs on the [APIs.io](https://apis.io/) network: Apps API and Functions API. Tagged areas include Embedded iPaaS, Integration, and Native Integrations.


  Integry''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Integry Plans Pricing
  plan_count: 3
  slug: integry-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Integry Rate Limits
  slug: integry-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/integry/refs/heads/main/screenshots/integry-2026-06-20T183535.png
security:
- kind: authentication
  name: Integry Authentication
  slug: integry-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Integry Domain Security
  slug: integry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: integry
tags:
- Embedded iPaaS
- Integration
- Native Integrations
website: https://integry.io
---
