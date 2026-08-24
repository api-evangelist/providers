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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Firecrawl Agentic Access
  operation_count: 31
  slug: firecrawl-agentic-access
  summary_line: 31 operations · 17 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The Account API from Firecrawl — 1 operation(s) for account.
  name: Firecrawl Account API
  slug: firecrawl-account-api
- description: The Agent API from Firecrawl — 2 operation(s) for agent.
  name: Firecrawl Agent API
  slug: firecrawl-agent-api
- description: The Billing API from Firecrawl — 4 operation(s) for billing.
  name: Firecrawl Billing API
  slug: firecrawl-billing-api
- description: The Browser API from Firecrawl — 3 operation(s) for browser.
  name: Firecrawl Browser API
  slug: firecrawl-browser-api
- description: The Crawling API from Firecrawl — 5 operation(s) for crawling.
  name: Firecrawl Crawling API
  slug: firecrawl-crawling-api
- description: The Extraction API from Firecrawl — 2 operation(s) for extraction.
  name: Firecrawl Extraction API
  slug: firecrawl-extraction-api
- description: The Mapping API from Firecrawl — 1 operation(s) for mapping.
  name: Firecrawl Mapping API
  slug: firecrawl-mapping-api
- description: The Miscellaneous API from Firecrawl — 1 operation(s) for miscellaneous.
  name: Firecrawl Miscellaneous API
  slug: firecrawl-miscellaneous-api
- description: The Scraping API from Firecrawl — 6 operation(s) for scraping.
  name: Firecrawl Scraping API
  slug: firecrawl-scraping-api
- description: The Search API from Firecrawl — 1 operation(s) for search.
  name: Firecrawl Search API
  slug: firecrawl-search-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Firecrawl Account API
  slug: open-firecrawl-account-api
- collection_type: open
  name: Firecrawl Account Agent API
  slug: open-firecrawl-agent-api
- collection_type: open
  name: Firecrawl Account Billing API
  slug: open-firecrawl-billing-api
- collection_type: open
  name: Firecrawl Account Browser API
  slug: open-firecrawl-browser-api
- collection_type: open
  name: Firecrawl Account Crawling API
  slug: open-firecrawl-crawling-api
- collection_type: open
  name: Firecrawl Account Extraction API
  slug: open-firecrawl-extraction-api
- collection_type: open
  name: Firecrawl Account Mapping API
  slug: open-firecrawl-mapping-api
- collection_type: open
  name: Firecrawl Account Miscellaneous API
  slug: open-firecrawl-miscellaneous-api
- collection_type: open
  name: Firecrawl API
  slug: open-firecrawl-openapi-original
- collection_type: open
  name: Firecrawl Account Scraping API
  slug: open-firecrawl-scraping-api
- collection_type: open
  name: Firecrawl Account Search API
  slug: open-firecrawl-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firecrawl-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/firecrawl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firecrawl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/firecrawl-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firecrawl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firecrawl
- group: company
  title: ''
  type: Website
  url: https://www.firecrawl.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firecrawl.dev/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firecrawl.dev/api-reference/introduction
- group: other
  title: ''
  type: Playground
  url: https://www.firecrawl.dev/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firecrawl.dev/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.firecrawl.dev/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firecrawl.dev/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firecrawl.dev/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://www.firecrawl.dev/blog
- group: other
  title: ''
  type: Affiliate
  url: https://www.firecrawl.dev/affiliate-program
- group: build
  title: ''
  type: SDKs
  url: https://docs.firecrawl.dev/sdks/overview
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.firecrawl.dev/rate-limits
- group: operate
  title: ''
  type: Support
  url: https://firecrawl.dev/support
- group: agent
  title: ''
  type: LLMs
  url: https://docs.firecrawl.dev/llms.txt
created: '2025-02-12'
description: Empower your AI apps with clean data from any website. Featuring advanced scraping, crawling, and data extraction capabilities. Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data. We crawl all accessible subpages and give you clean data for each. No sitemap required.
finops:
- name: Firecrawl Finops
  service_category: API
  slug: firecrawl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firecrawl.png
layout: provider
modified: '2026-05-19'
name: Firecrawl
nav: Providers
network: true
overview: 'Firecrawl publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agent API, Billing API, and 7 more. Tagged areas include Crawling, Data Extraction, Scraping, URLs, and Artificial Intelligence.


  Firecrawl''s developer surface includes authentication, documentation, API reference, pricing, changelog, engineering blog, support, and 13 more developer resources.'
plans:
- name: Firecrawl Plans Pricing
  plan_count: 3
  slug: firecrawl-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Firecrawl Rate Limits
  slug: firecrawl-rate-limits
score:
  band: developing
  composite: 43.5
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.6
    developer_ergonomics: 46.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firecrawl/refs/heads/main/screenshots/firecrawl-2026-06-20T181259.png
security:
- kind: authentication
  name: Firecrawl Authentication
  slug: firecrawl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Firecrawl Domain Security
  slug: firecrawl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Firecrawl Vulnerability Disclosure
  slug: firecrawl-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: firecrawl
tags:
- Crawling
- Data Extraction
- Scraping
- URLs
- Artificial Intelligence
- Markdown
website: https://www.firecrawl.dev
---
