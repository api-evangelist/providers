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
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-09-21'
api_count: 3
apis:
- description: Playwright provides a cross-browser automation API for end-to-end testing of web applications. It supports Chromium, Firefox, and WebKit with a single API, enabling reliable testing with auto-wait, ne
  name: Playwright API
  slug: playwright-api
- description: Azure Playwright Testing is a managed cloud service for running Playwright tests at scale. It provides browser infrastructure for parallel test execution, reducing test suite run times and enabling CI
  name: Azure Playwright Testing Service API
  slug: testing-service-api
- description: Open-source framework for reliable end-to-end browser testing and web automation supporting Chromium, Firefox, and WebKit. Distributed as a library/CLI; there is no public hosted HTTP API.
  name: Playwright
  slug: playwright
artifact_total: 8
common:
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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-playwright/refs/heads/main/security/microsoft-playwright-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-playwright-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/playwrightweb
- group: start
  title: ''
  type: Portal
  url: https://playwright.dev/
- group: company
  title: ''
  type: Website
  url: https://playwright.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://playwright.dev/docs/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/playwright
- group: start
  title: ''
  type: GettingStarted
  url: https://playwright.dev/docs/intro
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://playwright.dev/docs/support
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/playwright-mcp
created: '2024-01-01'
description: Playwright is an open-source browser automation framework by Microsoft for reliable end-to-end testing of web applications. It supports Chromium, Firefox, and WebKit with a single API across multiple programming languages.
finops:
- name: Microsoft Playwright Finops
  service_category: API
  slug: microsoft-playwright-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-playwright.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Playwright
nav: Providers
network: true
overview: 'Microsoft Playwright publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Browser Automation, End-to-End Testing, Microsoft, and Testing.


  Microsoft Playwright''s developer surface includes release notes, developer portal, documentation, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Microsoft Playwright Plans Pricing
  plan_count: 3
  slug: microsoft-playwright-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Microsoft Playwright Rate Limits
  slug: microsoft-playwright-rate-limits
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 63.0
    operational_transparency: 28.9
  previous_composite: 25.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-playwright/refs/heads/main/screenshots/microsoft-playwright-2026-06-20T185519.png
security:
- kind: domain-security
  name: Microsoft Playwright Domain Security
  slug: microsoft-playwright-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-playwright
tags:
- Browser Automation
- End-to-End Testing
- Microsoft
- Testing
website: https://playwright.dev/
---
