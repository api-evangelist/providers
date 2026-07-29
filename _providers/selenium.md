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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Selenium Agentic Access
  operation_count: 13
  slug: selenium-agentic-access
  summary_line: 13 operations · 9 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: WebDriver is a browser automation framework that accepts commands and sends them to a browser. It is implemented through a browser-specific driver that sends commands to a browser and retrieves result
  name: Selenium WebDriver
  slug: selenium-webdriver
- description: Selenium Grid allows you to run test cases in different machines across different platforms. It enables the execution of test scripts on remote machines by routing commands to remote web browser insta
  name: Selenium Grid
  slug: selenium-grid
- description: Cookie management
  name: Selenium Cookies API
  slug: selenium-cookies-api
- description: Element discovery and interaction
  name: Selenium Elements API
  slug: selenium-elements-api
- description: Page navigation and metadata
  name: Selenium Navigation API
  slug: selenium-navigation-api
- description: Execute JavaScript in the page context
  name: Selenium Script API
  slug: selenium-script-api
- description: Session lifecycle
  name: Selenium Session API
  slug: selenium-session-api
- description: Remote end readiness
  name: Selenium Status API
  slug: selenium-status-api
artifact_total: 14
collections:
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol)
  slug: open-selenium
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/selenium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/selenium-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SeleniumHQ
- group: company
  title: ''
  type: Blog
  url: https://www.selenium.dev/blog/
- group: other
  title: ''
  type: Downloads
  url: https://www.selenium.dev/downloads/
- group: operate
  title: ''
  type: Support
  url: https://www.selenium.dev/support/
- group: other
  title: ''
  type: Ecosystem
  url: https://www.selenium.dev/ecosystem/
- group: other
  title: ''
  type: Sponsor
  url: https://www.selenium.dev/sponsors/
- group: other
  title: ''
  type: History
  url: https://www.selenium.dev/history/
created: '2024-01-01'
description: Selenium is a suite of tools for automating web browsers across many platforms. It provides a way to control browsers programmatically for testing web applications and automating browser-based tasks.
finops:
- name: Selenium Finops
  service_category: API
  slug: selenium-finops
image: https://www.selenium.dev/images/selenium-logo.svg
layout: provider
modified: '2024-01-01'
name: Selenium
nav: Providers
network: true
overview: 'Selenium publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cookies API, Elements API, Navigation API, and 3 more. Tagged areas include Automation, Browsers, End-To-End Testing, Quality Assurance, and Testing.


  Selenium''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Selenium Plans Pricing
  plan_count: 3
  slug: selenium-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Selenium Rate Limits
  slug: selenium-rate-limits
score:
  band: thin
  composite: 31.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 40.7
    developer_ergonomics: 6.5
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/selenium/refs/heads/main/screenshots/selenium-2026-06-20T193639.png
security:
- kind: domain-security
  name: Selenium Domain Security
  slug: selenium-domain-security
  summary_line: TLSv1.3
slug: selenium
tags:
- Automation
- Browsers
- End-To-End Testing
- Quality Assurance
- Testing
- WebDriver
website: https://www.selenium.dev/
---
