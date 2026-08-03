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
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: The Screaming Frog SEO Spider is a desktop website crawler for Windows, macOS, and Ubuntu that performs comprehensive technical SEO audits. It crawls websites to find broken links, analyze page titles
  name: Screaming Frog SEO Spider
  slug: seo-spider
- description: The Screaming Frog Log File Analyser is a free desktop tool that allows SEO professionals to upload and analyze server log files to understand how search bots are crawling a website. It identifies whi
  name: Screaming Frog Log File Analyser
  slug: log-file-analyser
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/screaming-frog-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/screaming-frog
- group: company
  title: ''
  type: Website
  url: https://www.screamingfrog.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.screamingfrog.co.uk/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.screamingfrog.co.uk/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.screamingfrog.co.uk/seo-spider/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.screamingfrog.co.uk/seo-spider/faq/
created: '2026-05-02'
description: Screaming Frog is a UK-based SEO software company and search marketing agency, best known for the SEO Spider website crawler tool used by SEO professionals worldwide to perform technical SEO audits, crawl analysis, and integrations with third-party APIs. The SEO Spider integrates with Google Analytics (GA4), Google Search Console, PageSpeed Insights, Ahrefs, Majestic, Moz, OpenAI, Gemini, Ollama, and Anthropic. Screaming Frog also offers a free Log File Analyser for analyzing server log files to understand search bot behavior.
examples:
- key_count: 20
  name: Screaming Frog Crawl Result Example
  slug: screaming-frog-crawl-result-example
finops:
- name: Screaming Frog Finops
  service_category: API
  slug: screaming-frog-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/screaming-frog.png
json_schemas:
- name: Screaming Frog Crawl Result
  property_count: 20
  slug: screaming-frog-crawl-result
json_structures:
- name: Screaming Frog Crawl Result Structure
  property_count: 0
  slug: screaming-frog-crawl-result-structure
jsonld:
- class_count: 20
  name: Screaming Frog Context
  property_count: 0
  slug: screaming-frog-context
layout: provider
modified: '2026-05-02'
name: Screaming Frog
nav: Providers
network: true
overview: 'Screaming Frog publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Search Engine Optimization, Website Crawler, Technical Audit, and Marketing.


  The Screaming Frog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Screaming Frog''s developer surface includes engineering blog, pricing, support, and 4 more developer resources.'
plans:
- name: Screaming Frog Plans Pricing
  plan_count: 3
  slug: screaming-frog-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Screaming Frog Rate Limits
  slug: screaming-frog-rate-limits
rules:
- name: Screaming Frog API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: screaming-frog-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 22.6
    developer_ergonomics: 6.5
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 34.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/screaming-frog/refs/heads/main/screenshots/screaming-frog-2026-06-20T193601.png
security:
- kind: domain-security
  name: Screaming Frog Domain Security
  slug: screaming-frog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: screaming-frog
tags:
- SEO
- Search Engine Optimization
- Website Crawler
- Technical Audit
- Marketing
- Analytics
website: https://www.screamingfrog.co.uk/
---
