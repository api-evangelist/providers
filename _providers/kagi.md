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
- acting_count: 2
  human_in_the_loop: 0
  name: Kagi Agentic Access
  operation_count: 3
  slug: kagi-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: The Kagi Search API delivers premium, ad-free web search results powered by the Kagi index, designed for AI agents, research workflows, and applications that demand high-quality results.
  name: Kagi Search API
  slug: search-api
- description: The Kagi Enrichment API provides access to Kagi's Teclis non-commercial web index and TinyGem news index for specialized retrieval and discovery workloads.
  name: Kagi Enrichment API
  slug: enrichment-api
- description: The Universal Summarizer API condenses URLs, documents, audio, and video into structured summaries using Kagi's hosted models.
  name: Kagi Universal Summarizer API
  slug: summarizer-api
- description: FastGPT is Kagi's LLM-powered question answering API that combines a hosted model with live Kagi web search for grounded, cited answers.
  name: Kagi FastGPT API
  slug: fastgpt-api
- baseURL: https://kagi.com/api/v0
  baseurl_source: declared
  description: Extract markdown content from web URLs.
  name: Kagi Extract API
  slug: kagi-extract-api
- baseURL: https://kagi.com/api/v0
  baseurl_source: declared
  description: Perform Kagi web searches.
  name: Kagi Search API
  slug: kagi-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kagi Search Extract API
  slug: open-kagi-extract-api
- collection_type: open
  name: Kagi Extract Search API
  slug: open-kagi-search-api
- collection_type: open
  name: Kagi Search API
  slug: open-kagi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kagi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kagi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kagi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kagi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kagi.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.kagi.com/kagi/api/overview.html
- group: company
  title: ''
  type: Blog
  url: https://blog.kagi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kagisearch
- group: commercial
  title: ''
  type: Pricing
  url: https://help.kagi.com/kagi/api/overview.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kagi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kagi.com/privacy
- group: operate
  title: ''
  type: Discord
  url: https://kagi.com/discord
- group: other
  title: ''
  type: X
  url: https://x.com/kagihq
- group: operate
  title: ''
  type: ChangeLog
  url: https://kagi.com/changelog
created: '2026-05-23'
description: Kagi is a privacy-focused premium search engine that also operates a commercial APIs portfolio for developers. The Kagi APIs Portal exposes Search, Enrichment, Universal Summarizer, and FastGPT endpoints, plus a free Small Web RSS feed for non-commercial use. The portal includes an API Playground, usage dashboard, and API key management with IP allowlists and per-product scopes. Kagi publishes an OpenAPI specification and ships official client libraries in Python, Go, Rust, and TypeScript. Billing is pay-per-use with monthly invoicing and a Discord community for developer support.
finops:
- name: Kagi Finops
  service_category: API
  slug: kagi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kagi.png
layout: provider
modified: '2026-05-23'
name: Kagi
nav: Providers
network: true
overview: 'Kagi publishes 2 APIs on the [APIs.io](https://apis.io/) network: Extract API and Search API. Tagged areas include Search, Premium Search, AI Search, Summarization, and FastGPT.


  Kagi''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 9 more developer resources.'
plans:
- name: Kagi Plans Pricing
  plan_count: 1
  slug: kagi-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Kagi Rate Limits
  slug: kagi-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/kagi/refs/heads/main/screenshots/kagi-2026-06-20T183852.png
security:
- kind: authentication
  name: Kagi Authentication
  slug: kagi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kagi Domain Security
  slug: kagi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kagi Vulnerability Disclosure
  slug: kagi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kagi
tags:
- Search
- Premium Search
- AI Search
- Summarization
- FastGPT
- Enrichment
- OpenAPI
- Pay-Per-Use
- Privacy
- LLMs
- Web Index
website: https://kagi.com
---
