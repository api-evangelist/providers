---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.0
  scored_at: '2026-11-06'
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
artifact_total: 19
common:
- group: commercial
  href: https://artifacts.apis.io/adscrawl/finops/adscrawl-finops.yml
  title: ''
  type: FinOps
  url: finops/adscrawl-finops.yml
- group: build
  href: https://artifacts.apis.io/adscrawl/integrations/adscrawl-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/adscrawl-integration-edges.yml
- group: operate
  title: ''
  type: Support
  url: https://www.adscrawl.net/support/
- group: agent
  href: https://artifacts.apis.io/adscrawl/agentic-access/adscrawl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adscrawl-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/adscrawl/plans/adscrawl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adscrawl-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adscrawl/rules/adscrawl-rules.yml
  title: ''
  type: Spectral
  url: rules/adscrawl-rules.yml
- group: design
  href: https://artifacts.apis.io/adscrawl/json-ld/adscrawl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adscrawl-context.jsonld
- group: design
  href: https://artifacts.apis.io/adscrawl/vocabulary/adscrawl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adscrawl-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adscrawl/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adscrawl/data-model/adscrawl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adscrawl-data-model.yml
- group: design
  href: https://artifacts.apis.io/adscrawl/conventions/adscrawl-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adscrawl-conventions.yml
- group: auth
  href: https://artifacts.apis.io/adscrawl/authentication/adscrawl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adscrawl-authentication.yml
- group: design
  href: https://artifacts.apis.io/adscrawl/errors/adscrawl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adscrawl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adscrawl/conformance/adscrawl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adscrawl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adscrawl/llms/adscrawl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adscrawl-llms.txt
- group: other
  href: https://artifacts.apis.io/adscrawl/a2a/adscrawl-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adscrawl-a2a.yml
- group: agent
  href: https://artifacts.apis.io/adscrawl/well-known/adscrawl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adscrawl-well-known.yml
- group: other
  href: https://artifacts.apis.io/adscrawl/hosts/adscrawl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adscrawl-hosts.yml
- group: other
  href: https://artifacts.apis.io/adscrawl/vendors/adscrawl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adscrawl-vendors.yml
- group: build
  href: https://artifacts.apis.io/adscrawl/packages/adscrawl-packages.yml
  title: ''
  type: SDKs
  url: packages/adscrawl-packages.yml
- group: build
  href: https://artifacts.apis.io/adscrawl/packages/adscrawl-packages.yml
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
  href: https://artifacts.apis.io/adscrawl/security/adscrawl-domain-security.yml
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
description: AdsCrawl offers a comprehensive Browser Automation API enabling developers to run full browsers such as Playwright, Puppeteer, or Chrome DevTools Protocol with residential proxy routing. It supports dynamic page rendering, screenshot capture, HTML extraction, and structured data scraping, catering to e‑commerce monitoring, SEO analysis, content aggregation, and other web‑data use cases. The service emphasizes real‑browser fidelity, scalable proxy infrastructure, and reliable data collection across authenticated sessions and complex sites.
finops:
- has_sources: true
  method: derived
  name: Adscrawl Finops
  primary_unit: seat
  service_category: ''
  slug: adscrawl-finops
  template: false
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
  property_count: 22
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
overview: 'AdsCrawl publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Browser tasks API, Cloud browsers API, and Remote CDP API. Tagged areas include Company, Browser Automation, WebDataExtraction, Playwright, and Puppeteer.


  The AdsCrawl catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AdsCrawl''s developer surface includes support, authentication, pricing, engineering blog, API reference, getting-started guide, documentation, and 26 more developer resources.'
plans:
- name: Adscrawl Plans Pricing
  plan_count: 4
  slug: adscrawl-plans-pricing
- name: Adscrawl Price Estimates
  plan_count: 0
  slug: adscrawl-price-estimates
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 56
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
  composite: 47.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 64.5
    developer_ergonomics: 43.5
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 75.0
      total: 4
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adscrawl/adscrawl-2026-10-11T092842.png
security:
- kind: authentication
  name: Adscrawl Authentication
  slug: adscrawl-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adscrawl Domain Security
  slug: adscrawl-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: adscrawl-create-and-launch-cloud-browser
  slug: adscrawl-create-and-launch-cloud-browser
- name: adscrawl-remote-cdp-session-workflow
  slug: adscrawl-remote-cdp-session-workflow
slug: adscrawl
tags:
- Company
- Browser Automation
- WebDataExtraction
- Playwright
- Puppeteer
- Chrome DevTools Protocol
website: https://www.adscrawl.net/
---
