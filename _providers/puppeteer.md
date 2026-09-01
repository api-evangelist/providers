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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Puppeteer is a Node.js library providing a high-level API to control headless Chrome or Chromium browsers for web scraping, testing, and automation.
  name: Puppeteer
  slug: puppeteer
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puppeteer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pptr.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://pptr.dev/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/puppeteer
created: '2026-03-29'
description: Puppeteer is a Node.js library providing a high-level API to control headless Chrome or Chromium browsers for web scraping, testing, and automation.
finops:
- name: Puppeteer Finops
  service_category: API
  slug: puppeteer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/puppeteer.png
layout: provider
modified: '2026-03-29'
name: Puppeteer
nav: Providers
network: true
overview: 'Puppeteer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Browser Automation, Headless Browsers, and Scraping.


  Puppeteer''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Puppeteer Plans Pricing
  plan_count: 3
  slug: puppeteer-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Puppeteer Rate Limits
  slug: puppeteer-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/puppeteer/refs/heads/main/screenshots/puppeteer-2026-06-20T192309.png
security:
- kind: domain-security
  name: Puppeteer Domain Security
  slug: puppeteer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: puppeteer
tags:
- Browser Automation
- Headless Browsers
- Scraping
website: https://pptr.dev/
---
