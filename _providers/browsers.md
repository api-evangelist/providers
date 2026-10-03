---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering programmable browsers, headless browser engines, and browser-automation APIs. The Browsers topic focuses on the browser execution surface — the runtime where pages are loaded, JavaScript is evaluated, and interactions are scripted — including local libraries like Puppeteer, Playwright, and Selenium, as well as managed browser-as-a-service platforms used for automation, data extraction, agentic web tasks, and cross-browser testing. This collection is distinct from web scraping and pure test-runner topics; it emphasizes the browser instance, session, and navigation surface that other automation, scraping, and AI-agent capabilities build on top of.
examples:
- key_count: 12
  name: Browsers Browser Session Example
  slug: browsers-browser-session-example
- key_count: 8
  name: Browsers Navigation Action Example
  slug: browsers-navigation-action-example
features:
- description: Programmable browser runtimes like Chromium, WebKit, and Gecko driven without a visible UI for automated navigation, rendering, and DOM interaction.
  name: Headless Browser Execution
- description: Client libraries like Puppeteer, Playwright, and Selenium that expose a high-level API for controlling browser sessions, pages, frames, and inputs.
  name: Browser Automation Libraries
- description: Managed cloud platforms that provision pre-warmed browser instances over WebSocket, CDP, or HTTP so consumers do not have to host their own browser fleet.
  name: Browser-as-a-Service
- description: APIs for creating, persisting, and reusing browser sessions, cookies, localStorage, fingerprints, and authenticated profiles across runs.
  name: Session and Profile Management
- description: A consistent surface for navigating to URLs, waiting for selectors, clicking, typing, scrolling, evaluating JavaScript, and capturing rendered DOM state.
  name: Navigation and DOM Interaction
- description: Proxy routing, header and user-agent customization, request interception, and anti-bot evasion controls layered on top of the browser instance.
  name: Network and Stealth Controls
- description: Endpoints for screenshots, full-page PDFs, HAR network logs, video recordings, and trace files generated from automated browser sessions.
  name: Capture and Artifact APIs
- description: AI-agent oriented interfaces, including Model Context Protocol servers and natural-language navigation, that expose a browser as a tool for LLMs.
  name: Agent-Ready Browser Surfaces
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Open-source browser automation library from Microsoft that drives Chromium, Firefox, and WebKit through a unified API.
  name: Playwright
- description: Node.js library from the Chrome team that controls headless Chromium via the Chrome DevTools Protocol.
  name: Puppeteer
- description: Long-standing browser automation suite built around WebDriver, used heavily for cross-browser end-to-end testing.
  name: Selenium
- description: Cloud browser and device platform providing real browsers and devices for automated and live cross-browser testing.
  name: BrowserStack
- description: Managed remote browser endpoint with built-in proxies and anti-bot infrastructure for large-scale automation.
  name: Bright Data Scraping Browser
- description: Web automation platform whose Actors run Puppeteer and Playwright workloads at scale on managed infrastructure.
  name: Apify
- description: AI-agent oriented library that gives LLMs a controllable browser as a tool surface for autonomous web tasks.
  name: Browser Use
- description: Synthetic monitoring platform that runs Playwright scripts on a schedule to validate production user journeys.
  name: Checkly
json_schemas:
- name: BrowserSession
  property_count: 12
  slug: browsers-browser-session
- name: NavigationAction
  property_count: 10
  slug: browsers-navigation-action
json_structures:
- name: Browsers Browser Session Structure
  property_count: 12
  slug: browsers-browser-session-structure
- name: Browsers Navigation Action Structure
  property_count: 10
  slug: browsers-navigation-action-structure
jsonld:
- class_count: 8
  name: Browsers Context
  property_count: 20
  slug: browsers-context
layout: provider
modified: '2026-05-19'
name: Browsers
nav: Providers
network: true
overview: 'Browsers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Headless Browser, Browser Automation, Web Automation, Browser-as-a-Service, and WebDriver.


  The Browsers catalog on APIs.io includes 1 JSON-LD context.


  Browsers'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: browsers
tags:
- Headless Browser
- Browser Automation
- Web Automation
- Browser-as-a-Service
- WebDriver
- Browser Testing
use_cases:
- description: Drive a real browser to render JavaScript-heavy pages and extract structured data that static HTTP scraping cannot reach.
  name: Automated Web Data Extraction
- description: Run application tests against Chromium, Firefox, and WebKit on real or virtualized devices to validate behavior before release.
  name: Cross-Browser End-to-End Testing
- description: Schedule scripted browser flows to continuously verify that critical user journeys remain functional in production.
  name: Synthetic Monitoring and Uptime Checks
- description: Provide AI agents with a controlled browser session so they can complete multi-step tasks like form filling, booking, and research.
  name: Agentic Web Task Execution
- description: Render web content to high-fidelity screenshots, social-share images, or PDF reports on demand via a managed browser API.
  name: Visual and PDF Generation
- description: Maintain logged-in browser profiles so automation can perform actions inside customer-account areas across runs.
  name: Authenticated Session Automation
- description: Execute Lighthouse, axe, and similar audits inside a real browser to track accessibility and performance regressions over time.
  name: Accessibility and Performance Audits
- description: Use browser automation as a UI-layer integration mechanism for systems that lack a usable API.
  name: Legacy Application Robotics
website: https://apievangelist.com
---
