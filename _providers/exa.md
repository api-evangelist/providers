---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Exa Agentic Access
  operation_count: 4
  slug: exa-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: The Exa Search API provides neural web search, contents retrieval, find similar, and grounded answers for AI agents. Multiple speed modes range from fast 250ms searches to deep research lasting tens o
  name: Exa Search API
  slug: search-api
- baseURL: https://api.exa.ai
  baseurl_source: declared
  description: The Answer API from Exa — 1 operation(s) for answer.
  name: Exa Answer API
  slug: exa-answer-api
- baseURL: https://api.exa.ai
  baseurl_source: declared
  description: The Contents API from Exa — 1 operation(s) for contents.
  name: Exa Contents API
  slug: exa-contents-api
- baseURL: https://api.exa.ai
  baseurl_source: declared
  description: The Search API from Exa — 2 operation(s) for search.
  name: Exa Search API
  slug: exa-search-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Exa Search Answer API
  slug: open-exa-answer-api
- collection_type: open
  name: Exa Search Answer Contents API
  slug: open-exa-contents-api
- collection_type: open
  name: Exa Answer Search API
  slug: open-exa-search-api
- collection_type: open
  name: Exa Search API
  slug: open-exa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://exa.ai
- group: docs
  title: ''
  type: Documentation
  url: https://exa.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://exa.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exa-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://exa.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exa.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exa.ai/privacy-policy
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/HCShtBqbfV
- group: other
  title: ''
  type: X
  url: https://x.com/exaailabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exa-ai
created: '2026-05-23'
description: Exa is a neural web search API designed for AI agents and applications. It combines a purpose-built web index with embedding-based retrieval to deliver highly relevant results across categories such as full web, news, companies, research, people, and financials. Exa exposes search, contents, find similar, and answer endpoints, with multiple search modes ranging from fast sub-second responses to deeper multi-step research. It also returns token-efficient highlights and summaries that reduce LLM input costs and supports structured output extraction across more than 70 million indexed companies. Exa is SOC 2 Type II certified, offers Zero Data Retention, and ships Python and JavaScript SDKs.
finops:
- name: Exa Finops
  service_category: API
  slug: exa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exa.png
layout: provider
modified: '2026-05-23'
name: Exa
nav: Providers
network: true
overview: 'Exa publishes 3 APIs on the [APIs.io](https://apis.io/) network: Answer API, Contents API, and Search API. Tagged areas include Search, Neural Search, AI Agents, LLMs, and Web Index.


  Exa''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Exa Plans Pricing
  plan_count: 1
  slug: exa-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Exa Rate Limits
  slug: exa-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/exa/refs/heads/main/screenshots/exa-2026-06-20T180946.png
security:
- kind: authentication
  name: Exa Authentication
  slug: exa-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Exa Domain Security
  slug: exa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exa Vulnerability Disclosure
  slug: exa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: exa
tags:
- Search
- Neural Search
- AI Agents
- LLMs
- Web Index
- Retrieval
- Answers
- Contents
- Find Similar
- Research
- SOC 2
- MCP
website: https://exa.ai
---
