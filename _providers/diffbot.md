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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Diffbot Agentic Access
  operation_count: 14
  slug: diffbot-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 1
apis:
- description: The Diffbot DQL API is a powerful tool that allows users to query and retrieve data from the web in a structured format. By using a simple query language, users can access a wealth of information from
  name: Diffbot DQL API
  slug: diffbot-dql-api
- description: Diffbot Enhance API enhances data by providing additional context and insights. By analyzing text and images, the API can identify and extract key information, such as entities, topics, and sentiment,
  name: Diffbot Enhance API
  slug: diffbot-enhance-api
- description: Diffbot Natural Language API allows users to extract and analyze textual content from websites. By utilizing advanced natural language processing algorithms, the API can automatically identify and ext
  name: Diffbot Natural Language API
  slug: diffbot-natural-language-api
- description: Diffbot Extract API is a powerful tool that allows users to automatically extract multiple types of data from web pages. This API is capable of extracting information such as article text, author deta
  name: Diffbot Extract API
  slug: diffbot-extract-api
- description: Diffbot Bulk Extract API is a tool that allows users to extract data at scale from a variety of sources, including websites, documents, and social media platforms. This API utilizes machine learning a
  name: Diffbot Bulk Extract API
  slug: diffbot-bulk-extract-api
- description: Diffbot Crawl API is a powerful tool that automates the process of extracting content and data from websites on a large scale. By using advanced machine learning algorithms, the API can analyze and ex
  name: Diffbot Crawl API
  slug: diffbot-crawl-api
- description: The Diffbot Crawl/Bulk Job API is a powerful tool that allows users to automatically extract and organize large amounts of web data. It enables users to create custom scraping jobs that can gather inf
  name: Diffbot Crawl/Bulk Job API
  slug: diffbot-crawlbulk-job-api
- description: The Crawl API from Diffbot — 2 operation(s) for crawl.
  name: Diffbot Crawl API
  slug: diffbot-crawl-api
- description: The Extract API from Diffbot — 9 operation(s) for extract.
  name: Diffbot Extract API
  slug: diffbot-extract-api
- description: The Knowledge Graph API from Diffbot — 2 operation(s) for knowledge graph.
  name: Diffbot Knowledge Graph API
  slug: diffbot-knowledge-graph-api
- description: The Natural Language API from Diffbot — 1 operation(s) for natural language.
  name: Diffbot Natural Language API
  slug: diffbot-natural-language-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Diffbot Crawl API
  slug: open-diffbot-crawl-api
- collection_type: open
  name: Diffbot Crawl Extract API
  slug: open-diffbot-extract-api
- collection_type: open
  name: Diffbot Crawl Knowledge Graph API
  slug: open-diffbot-knowledge-graph-api
- collection_type: open
  name: Diffbot Crawl Natural Language API
  slug: open-diffbot-natural-language-api
- collection_type: open
  name: Diffbot API
  slug: open-diffbot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/diffbot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diffbot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/diffbot-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diffbot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diffbot
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.diffbot.com/changelog
- group: company
  title: ''
  type: Website
  url: https://www.diffbot.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.diffbot.com/pricing/
- group: other
  title: ''
  type: Customers
  url: https://www.diffbot.com/customer-stories/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.diffbot.com/docs/getting-started-with-diffbot
- group: company
  title: ''
  type: News
  url: https://www.diffbot.com/company/news/
- group: company
  title: ''
  type: Blog
  url: https://blog.diffbot.com/
- group: other
  title: ''
  type: Glossary
  url: https://blog.diffbot.com/knowledge-graph-glossary/
- group: learn
  title: ''
  type: Webinars
  url: https://blog.diffbot.com/webinars/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diffbot.com/company/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diffbot.com/company/privacy/
- group: other
  title: ''
  type: DataLicensing
  url: https://docs.diffbot.com/docs/is-diffbot-compliant-with-gdpr
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.diffbot.com/llms.txt
created: '2024-11-13'
description: Diffbot is a company that provides AI-powered web scraping and data extraction services. Their technology allows businesses to automatically extract and organize data from any website, turning unstructured web content into structured data that can be easily analyzed and used for various purposes. Diffbot's solution is used by companies across industries to gather competitive intelligence, monitor market trends, track online mentions, and more.
finops:
- name: Diffbot Finops
  service_category: API
  slug: diffbot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diffbot.png
layout: provider
modified: '2026-04-28'
name: Diffbot
nav: Providers
network: true
overview: 'Diffbot publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Natural Language API, Extract API, Crawl API, and 4 more. Tagged areas include Extraction, Harvesting, Scraping, and Web.


  Diffbot''s developer surface includes authentication, changelog, pricing, documentation, product news, engineering blog, and 12 more developer resources.'
plans:
- name: Diffbot Plans Pricing
  plan_count: 3
  slug: diffbot-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Diffbot Rate Limits
  slug: diffbot-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/diffbot/refs/heads/main/screenshots/diffbot-2026-06-20T180012.png
security:
- kind: authentication
  name: Diffbot Authentication
  slug: diffbot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Diffbot Domain Security
  slug: diffbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diffbot
tags:
- Extraction
- Harvesting
- Scraping
- Web
website: https://www.diffbot.com/
---
