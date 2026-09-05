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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Open-source framework for reliable end-to-end browser testing and web automation supporting Chromium, Firefox, and WebKit. Distributed as a library/CLI; there is no public hosted HTTP API.
  name: Playwright
  slug: playwright
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playwright-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/playwrightweb
- group: company
  title: ''
  type: Website
  url: https://playwright.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://playwright.dev/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/playwright
- group: operate
  title: ''
  type: Community
  url: https://aka.ms/playwright/discord
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/microsoft/playwright/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/microsoft/playwright/issues
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/playwright-mcp
created: '2026-03-16'
description: Playwright is an open-source framework from Microsoft for web automation and browser testing. It enables reliable end-to-end testing for modern web apps, supporting Chromium, Firefox, and WebKit browsers. Playwright is consumed as a library and CLI rather than a hosted HTTP API.
finops:
- name: Playwright Finops
  service_category: API
  slug: playwright-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/playwright.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Playwright
nav: Providers
network: true
overview: 'Playwright publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Browser Testing, End-to-End, Library, Open-Source, and Test Automation.


  Playwright''s developer surface includes documentation, release notes, and 7 more developer resources.'
plans:
- name: Playwright Plans Pricing
  plan_count: 3
  slug: playwright-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Playwright Rate Limits
  slug: playwright-rate-limits
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/playwright/refs/heads/main/screenshots/playwright-2026-06-20T191808.png
security:
- kind: domain-security
  name: Playwright Domain Security
  slug: playwright-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: playwright
tags:
- Browser Testing
- End-to-End
- Library
- Open-Source
- Test Automation
- Test Framework
- Web Automation
website: https://playwright.dev/
---
