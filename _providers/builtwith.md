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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Builtwith Agentic Access
  operation_count: 20
  slug: builtwith-agentic-access
  summary_line: 20 operations · 1 acting
api_count: 29
apis:
- description: Current and historical website technology information for single or multiple domains with support for JSON, XML, and CSV formats.
  name: BuiltWith Domain API
  slug: builtwith-domain-api
- description: Retrieve lists of websites using specific web technologies in XML, JSON, TXT, CSV, and TSV formats.
  name: BuiltWith Lists API
  slug: builtwith-lists-api
- description: Access technology trend data showing adoption and growth of web technologies over time.
  name: BuiltWith Trends API
  slug: builtwith-trends-api
- description: Track technology additions and removals on websites with business context in JSON format.
  name: BuiltWith Change API
  slug: builtwith-change-api
- description: Website interconnection data revealing domain relationships via shared IPs, analytics, and other attributes.
  name: BuiltWith Relationships API
  slug: builtwith-relationships-api
- description: Free tier API providing technology group counts and last-updated timestamps for website domains.
  name: BuiltWith Free API
  slug: builtwith-free-api
- description: Natural language website lookups returning technology profile data in JSON and CSV formats.
  name: BuiltWith Ask API
  slug: builtwith-ask-api
- description: Real-time WebSocket feed of technology detections as they happen across the web.
  name: BuiltWith Live Feed API
  slug: builtwith-live-feed-api
- description: Resolve company names to their associated domain names in JSON and XML formats.
  name: BuiltWith Company to URL API
  slug: builtwith-company-to-url-api
- description: Retrieve related domains associated with IPs and other website attributes.
  name: BuiltWith Tags API
  slug: builtwith-tags-api
- description: Get technology suggestions based on a website's existing technology profile.
  name: BuiltWith Recommendations API
  slug: builtwith-recommendations-api
- description: Find websites that use specific keywords in their content.
  name: BuiltWith Keywords API
  slug: builtwith-keywords-api
- description: Search websites by keyword content returning results in JSON and CSV formats.
  name: BuiltWith Keyword Search API
  slug: builtwith-keyword-search-api
- description: Text-based technology searches using vector embeddings for semantic similarity matching.
  name: BuiltWith Vector Search API
  slug: builtwith-vector-search-api
- description: Access website redirect chain data to understand domain redirect patterns.
  name: BuiltWith Redirects API
  slug: builtwith-redirects-api
- description: eCommerce product lookup for identifying products and merchants across the web.
  name: BuiltWith Product API
  slug: builtwith-product-api
- description: Website trustworthiness assessment providing reliability and safety scores for domains.
  name: BuiltWith Trust API
  slug: builtwith-trust-api
- description: Access financial data from SEC Edgar and UK Companies House filings for domains, including revenue, assets, and equity data.
  name: BuiltWith Financial API
  slug: builtwith-financial-api
- description: Batch domain processing for high-volume technology lookups across large domain lists.
  name: BuiltWith Bulk Domain API
  slug: builtwith-bulk-domain-api
- description: Model Context Protocol server integration enabling AI assistants to query BuiltWith technology detection data natively.
  name: BuiltWith MCP API
  slug: builtwith-mcp-api
- description: Autonomous credit management API enabling AI agents to manage and replenish API credits programmatically.
  name: BuiltWith Agent Payment API
  slug: builtwith-agent-payment-api
- description: Asynchronous batch domain processing
  name: BuiltWith Bulk Processing API
  slug: builtwith-bulk-processing-api
- description: Single or multi-domain technology detection endpoints
  name: BuiltWith Domain Lookup API
  slug: builtwith-domain-lookup-api
- description: Identify domain interconnections via shared identifiers
  name: BuiltWith Domain Relationships API
  slug: builtwith-domain-relationships-api
- description: Technology count lookups for free tier
  name: BuiltWith Free Lookup API
  slug: builtwith-free-lookup-api
- description: Lookup domains by IP or attribute identifier
  name: BuiltWith Tag Lookup API
  slug: builtwith-tag-lookup-api
- description: Track technology additions and removals on websites
  name: BuiltWith Technology Changes API
  slug: builtwith-technology-changes-api
- description: Retrieve websites using specific technologies
  name: BuiltWith Technology Lists API
  slug: builtwith-technology-lists-api
- description: Technology adoption trends and market share data
  name: BuiltWith Technology Trends API
  slug: builtwith-technology-trends-api
artifact_total: 45
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/builtwith/mcp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/builtwith/mcp/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/builtwith/mcp/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/builtwith-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/builtwith-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/builtwith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/builtwith-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://builtwith.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.builtwith.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/builtwith
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/builtwith
- group: company
  title: ''
  type: Blog
  url: https://blog.builtwith.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://builtwith.com/plans
- group: other
  title: ''
  type: X
  url: https://x.com/builtwith
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.builtwith.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/builtwithcom/builtwith/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/builtwith-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/builtwith-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/builtwith-finops.yml
created: 2026-06-13
description: Technology profiling and lead generation platform with a REST API for detecting technologies used by websites, tracking technology trends, and identifying technology adoption across 491.9 million domains and 115,907 tracked web technologies.
examples:
- key_count: 1
  name: Builtwith Change Example
  slug: builtwith-change-example
- key_count: 1
  name: Builtwith Domain Example
  slug: builtwith-domain-example
- key_count: 2
  name: Builtwith Lists Example
  slug: builtwith-lists-example
- key_count: 1
  name: Builtwith Trends Example
  slug: builtwith-trends-example
finops:
- name: Builtwith Finops
  service_category: ''
  slug: builtwith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/builtwith.png
json_schemas:
- name: BuiltWith Change API Result
  property_count: 1
  slug: builtwith-change
- name: BuiltWith Domain API Result
  property_count: 1
  slug: builtwith-domain
- name: BuiltWith Lists API Result
  property_count: 2
  slug: builtwith-lists
jsonld:
- class_count: 10
  name: Builtwith Context
  property_count: 52
  slug: builtwith-context
layout: provider
modified: 2026-06-13
name: BuiltWith
nav: Providers
network: true
overview: 'BuiltWith publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bulk Processing API, Domain Lookup API, Domain Relationships API, and 5 more. Tagged areas include Technology Profiling, Lead Generation, Web Intelligence, Technology Detection, and Website Analysis.


  The BuiltWith catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuiltWith''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Builtwith Plans Pricing
  plan_count: 6
  slug: builtwith-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Builtwith Rate Limits
  slug: builtwith-rate-limits
rules:
- name: BuiltWith API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: builtwith-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.0
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/builtwith/refs/heads/main/screenshots/builtwith-2026-06-20T173756.png
security:
- kind: authentication
  name: Builtwith Authentication
  slug: builtwith-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Builtwith Domain Security
  slug: builtwith-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Builtwith Vulnerability Disclosure
  slug: builtwith-vulnerability-disclosure
  summary_line: disclosure policy published
slug: builtwith
tags:
- Technology Profiling
- Lead Generation
- Web Intelligence
- Technology Detection
- Website Analysis
- Market Research
website: https://builtwith.com/
---
