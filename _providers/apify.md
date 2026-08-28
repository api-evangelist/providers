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
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apify Agentic Access
  operation_count: 13
  slug: apify-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 6
apis:
- description: Monitor and manage Actor run executions.
  name: Apify Actor Runs API
  slug: apify-actor-runs-api
- description: Manage and run Apify Actors.
  name: Apify Actors API
  slug: apify-actors-api
- description: Manage structured data storage from Actor runs.
  name: Apify Datasets API
  slug: apify-datasets-api
- description: Manage persistent key-value storage.
  name: Apify Key-Value Stores API
  slug: apify-key-value-stores-api
- description: Manage URL queues for web crawling.
  name: Apify Request Queues API
  slug: apify-request-queues-api
- description: User and account management.
  name: Apify Users API
  slug: apify-users-api
artifact_total: 60
collections:
- collection_type: postman
  name: Apify Actor Runs API
  slug: postman-apify-actor-runs-api
- collection_type: postman
  name: Apify Actor Runs Actors API
  slug: postman-apify-actors-api
- collection_type: postman
  name: Apify Actor Runs Datasets API
  slug: postman-apify-datasets-api
- collection_type: postman
  name: Apify Actor Runs Key-Value Stores API
  slug: postman-apify-key-value-stores-api
- collection_type: postman
  name: Apify Actor Runs Request Queues API
  slug: postman-apify-request-queues-api
- collection_type: postman
  name: Apify Actor Runs Users API
  slug: postman-apify-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apify Actor Runs API
  slug: open-apify-actor-runs-api
- collection_type: open
  name: Apify Actor Runs Actors API
  slug: open-apify-actors-api
- collection_type: open
  name: Apify Actor Runs Datasets API
  slug: open-apify-datasets-api
- collection_type: open
  name: Apify Actor Runs Key-Value Stores API
  slug: open-apify-key-value-stores-api
- collection_type: open
  name: Apify Actor Runs Request Queues API
  slug: open-apify-request-queues-api
- collection_type: open
  name: Apify Actor Runs Users API
  slug: open-apify-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apify/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apify-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apify-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apify
- group: company
  title: ''
  type: Website
  url: https://apify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apify.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apify.com/api/v2/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://apify.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.apify.com
- group: start
  title: ''
  type: Signup
  url: https://console.apify.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://console.apify.com/sign-in
- group: learn
  title: ''
  type: Academy
  url: https://docs.apify.com/academy
- group: operate
  title: ''
  type: Support
  url: https://help.apify.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apify
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/apify-cli
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/apify/apify-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/apify/agent-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apify.com/llms.txt
created: '2026-03-26'
description: Apify is a full-stack web scraping and browser automation platform that enables developers to build, run, and scale web scrapers, crawlers, and data extraction tools using a cloud-based infrastructure with built-in proxy management, scheduling, and storage. The platform hosts thousands of ready-made Actors for scraping social media, search engines, maps, e-commerce sites, and more.
examples:
- key_count: 5
  name: Apify Actor Example
  slug: apify-actor-example
- key_count: 3
  name: Apify Dataset Example
  slug: apify-dataset-example
- key_count: 2
  name: Apify Key Value Store Example
  slug: apify-key-value-store-example
- key_count: 6
  name: Apify Run Example
  slug: apify-run-example
features:
- description: Store of thousands of pre-built web scrapers and automation tools ready to run with zero configuration.
  name: Actors Marketplace
- description: Run Actors on Apify's scalable cloud infrastructure with built-in proxy rotation, scheduling, and storage.
  name: Cloud Infrastructure
- description: Structured storage for Actor output with multi-format export (JSON, CSV, XML, XLSX, etc.).
  name: Datasets
- description: Persistent key-value storage for arbitrary data including files, screenshots, and configuration.
  name: Key-Value Stores
- description: URL queue management for large-scale distributed web crawling.
  name: Request Queues
- description: Built-in datacenter and residential proxy pools with automatic rotation.
  name: Proxy Management
- description: Schedule Actors to run automatically on cron schedules.
  name: Scheduled Runs
- description: Apify MCP server enabling AI agents to use thousands of web scraping and automation tools.
  name: MCP Server
finops:
- name: Apify Finops
  service_category: API
  slug: apify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apify.png
json_schemas:
- name: Actor
  property_count: 5
  slug: apify-actor
- name: Dataset
  property_count: 3
  slug: apify-dataset
- name: KeyValueStore
  property_count: 2
  slug: apify-key-value-store
- name: Run
  property_count: 6
  slug: apify-run
json_structures:
- name: Apify Actor Structure
  property_count: 5
  slug: apify-actor-structure
- name: Apify Dataset Structure
  property_count: 3
  slug: apify-dataset-structure
- name: Apify Key Value Store Structure
  property_count: 2
  slug: apify-key-value-store-structure
- name: Apify Run Structure
  property_count: 6
  slug: apify-run-structure
jsonld:
- class_count: 7
  name: Apify Context
  property_count: 6
  slug: apify-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Apify
nav: Providers
network: true
overview: 'Apify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Actor Runs API, Actors API, Datasets API, and 3 more. Tagged areas include Actors, Browser Automation, Crawling, Data Aggregation, and Data Extraction.


  The Apify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apify''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, academy / training, and 13 more developer resources.'
plans:
- name: Apify Plans Pricing
  plan_count: 3
  slug: apify-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Apify Rate Limits
  slug: apify-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apify-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Apify API Rules
  rule_count: 20
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 14
  slug: apify-spectral-rules
score:
  band: thin
  composite: 37.8
  delta: 1.4
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 27.0
    developer_ergonomics: 66.7
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apify/refs/heads/main/screenshots/apify-2026-06-20T172249.png
security:
- kind: authentication
  name: Apify Authentication
  slug: apify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apify Domain Security
  slug: apify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apify Vulnerability Disclosure
  slug: apify-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: apify-actor-development
  slug: apify-actor-development
- name: apify-actorization
  slug: apify-actorization
- name: apify-generate-output-schema
  slug: apify-generate-output-schema
- name: apify-sdk-integration
  slug: apify-sdk-integration
- name: apify-ultimate-scraper
  slug: apify-ultimate-scraper
slug: apify
tags:
- Actors
- Browser Automation
- Crawling
- Data Aggregation
- Data Extraction
- Web Automation
- Web Scraping
use_cases:
- description: Extract structured data from websites for LLM training datasets, RAG pipelines, and AI applications.
  name: AI Training Data Collection
- description: Scrape product prices, availability, and reviews from e-commerce websites for competitive intelligence.
  name: E-commerce Price Monitoring
- description: Extract posts, profiles, and engagement data from social media platforms.
  name: Social Media Data Extraction
- description: Scrape search engine results, SERP data, and web listings for SEO and market research.
  name: Search Engine Data
- description: Extract business data from directories, LinkedIn, and other professional platforms.
  name: Lead Generation
website: https://apify.com
---
