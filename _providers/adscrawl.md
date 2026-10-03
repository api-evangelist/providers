---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 3
  name: Adscrawl Agentic Access
  operation_count: 15
  slug: adscrawl-agentic-access
  summary_line: 15 operations · 10 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.adscrawl.net
  baseurl_source: declared
  description: Synchronous rendered content, screenshots, and structured extraction.
  name: AdsCrawl Browser tasks API
  slug: adscrawl-browser-tasks-api
- baseURL: https://api.adscrawl.net
  baseurl_source: declared
  description: Persistent profiles and browser lifecycle. Starting requires a paid plan.
  name: AdsCrawl Cloud browsers API
  slug: adscrawl-cloud-browsers-api
- baseURL: https://api.adscrawl.net
  baseurl_source: declared
  description: Temporary browser sessions and scoped connection tokens.
  name: AdsCrawl Remote CDP API
  slug: adscrawl-remote-cdp-api
artifact_total: 15
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/agentic-access/adscrawl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adscrawl-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/plans/adscrawl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adscrawl-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/rules/adscrawl-rules.yml
  title: ''
  type: Spectral
  url: rules/adscrawl-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/json-ld/adscrawl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adscrawl-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/vocabulary/adscrawl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adscrawl-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/data-model/adscrawl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adscrawl-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/conventions/adscrawl-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adscrawl-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/authentication/adscrawl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adscrawl-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/errors/adscrawl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adscrawl-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/conformance/adscrawl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adscrawl-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/llms/adscrawl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adscrawl-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/a2a/adscrawl-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adscrawl-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/well-known/adscrawl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adscrawl-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/hosts/adscrawl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adscrawl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/vendors/adscrawl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adscrawl-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/packages/adscrawl-packages.yml
  title: ''
  type: SDKs
  url: packages/adscrawl-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/packages/adscrawl-packages.yml
  title: ''
  type: Packages
  url: packages/adscrawl-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adscrawl.net/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adscrawl.net/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.adscrawl.net/pricing
- group: start
  title: ''
  type: Login
  url: https://www.adscrawl.net/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdsCrawl
- group: company
  title: ''
  type: Blog
  url: https://blog.adscrawl.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adscrawl.net/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adscrawl.net/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.adscrawl.net`
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adscrawl/refs/heads/main/security/adscrawl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adscrawl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adscrawl.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adscrawl.net
created: '2026-10-02'
description: AdsCrawl provides a Browser Automation API that lets developers run full browsers (Playwright, Puppeteer, or Chrome DevTools Protocol) with residential proxy routing to handle dynamic pages, authenticated sessions, and structured web data extraction. The platform offers endpoints for page rendering, screenshot capture, HTML extraction, and data scraping, targeting use cases like e‑commerce monitoring, SEO analysis, and content aggregation. It emphasizes real‑browser fidelity and scalable proxy infrastructure for reliable web data collection.
image: https://www.adscrawl.net/logo.svg
json_schemas:
- name: BrowserSettings
  property_count: 11
  slug: adscrawl-browser-settings
- name: CloudBrowser
  property_count: 11
  slug: adscrawl-cloud-browser
- name: CloudLaunchRequest
  property_count: 5
  slug: adscrawl-cloud-launch-request
- name: CloudStartRequest
  property_count: 5
  slug: adscrawl-cloud-start-request
- name: ExtractionTemplate
  property_count: 11
  slug: adscrawl-extraction-template
- name: SpaRequest
  property_count: 0
  slug: adscrawl-spa-request
jsonld:
- class_count: 16
  name: Adscrawl Context
  property_count: 87
  slug: adscrawl-context
layout: provider
modified: '2026-10-02'
name: AdsCrawl
nav: Providers
network: true
overview: 'AdsCrawl publishes 3 APIs on the [APIs.io](https://apis.io/) network: Browser tasks API, Cloud browsers API, and Remote CDP API. Tagged areas include Company, Browser Automation, WebDataExtraction, Playwright, and Puppeteer.


  The AdsCrawl catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AdsCrawl''s developer surface includes authentication, pricing, engineering blog, API reference, getting-started guide, documentation, and 24 more developer resources.'
plans:
- name: Adscrawl Plans Pricing
  plan_count: 4
  slug: adscrawl-plans-pricing
random_paper: 13
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: AdsCrawl API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: adscrawl-rules
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Adscrawl Authentication
  slug: adscrawl-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adscrawl Domain Security
  slug: adscrawl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adscrawl
tags:
- Company
- Browser Automation
- WebDataExtraction
- Playwright
- Puppeteer
- CDP
website: https://www.adscrawl.net/
---
