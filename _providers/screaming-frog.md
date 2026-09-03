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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.1
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Screaming Frog SEO Spider is a desktop website crawler for Windows, macOS, and Ubuntu that performs comprehensive technical SEO audits. It crawls websites to find broken links, analyze page titles
  name: Screaming Frog SEO Spider
  slug: seo-spider
- description: The Screaming Frog Log File Analyser is a free desktop tool that allows SEO professionals to upload and analyze server log files to understand how search bots are crawling a website. It identifies whi
  name: Screaming Frog Log File Analyser
  slug: log-file-analyser
artifact_total: 12
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
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.screamingfrog.co.uk/seo-spider/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/screamingfrog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.screamingfrog.co.uk/seo-spider/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.screamingfrog.co.uk/privacy/
- group: start
  title: ''
  type: Login
  url: https://www.screamingfrog.co.uk/login/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/screaming-frog-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/screaming-frog-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/screaming-frog-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/screaming-frog-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/screaming-frog-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/screaming-frog-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/screaming-frog-llms.txt
created: '2026-05-02'
description: Screaming Frog is a UK-based SEO software company and search marketing agency, best known for the SEO Spider website crawler tool used by SEO professionals worldwide to perform technical SEO audits, crawl analysis, and integrations with third-party APIs. The SEO Spider integrates with Google Analytics (GA4), Google Search Console, PageSpeed Insights, Ahrefs, Majestic, Moz, OpenAI, Gemini, Ollama, and Anthropic. Screaming Frog also offers a free Log File Analyser for analyzing server log files to understand search bot behavior. Screaming Frog operates no public web API. Its machine-callable surfaces are the SEO Spider command line interface, which runs the product fully headless, and — since version 24.0, released 19 May 2026 — a first-party Model Context Protocol server built into the desktop application, exposing 29 tools for crawl control, reports, bulk exports, URL inspection, screenshots, embeddings, Node scripting and sandboxed file access. The MCP server is a paid licence
  feature and runs inside the user's own installation over stdio or a loopback HTTP transport; there is no hosted endpoint.
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
mcp_servers:
- description: First-party Model Context Protocol server built into the Screaming Frog SEO Spider desktop application from version 24.0 (19 May 2026). It exposes the crawler's reports, bulk exports, SEO element data
  name: Screaming Frog SEO Spider MCP Server
  slug: screaming-frog-seo-spider-mcp-server
modified: '2026-08-13'
name: Screaming Frog
nav: Providers
network: true
overview: 'Screaming Frog publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Website Crawler, Technical Audit, Marketing, and Analytics.


  The Screaming Frog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Screaming Frog''s developer surface includes engineering blog, pricing, support, changelog, and 15 more developer resources.'
plans:
- name: Screaming Frog Plans Pricing
  plan_count: 4
  slug: screaming-frog-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Screaming Frog Rate Limits
  slug: screaming-frog-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Screaming Frog API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: screaming-frog-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 45.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 25.0
    contract_quality: 25.3
    developer_ergonomics: 44.6
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 18.4
  previous_composite: 42.1
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Website Crawler
- Technical Audit
- Marketing
- Analytics
- MCP
- Agents
- Desktop Software
- Command Line
website: https://www.screamingfrog.co.uk/
---
