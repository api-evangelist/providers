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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Selenium Agentic Access
  operation_count: 13
  slug: selenium-agentic-access
  summary_line: 13 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: WebDriver is a browser automation framework that accepts commands and sends them to a browser. It is implemented through a browser-specific driver that sends commands to a browser and retrieves result
  name: Selenium WebDriver
  slug: selenium-webdriver
- description: Selenium Grid allows you to run test cases in different machines across different platforms. It enables the execution of test scripts on remote machines by routing commands to remote web browser insta
  name: Selenium Grid
  slug: selenium-grid
- baseURL: http://localhost:4444
  baseurl_source: declared
  description: Cookie management
  name: Selenium Cookies API
  slug: selenium-cookies-api
- baseURL: http://localhost:4444
  baseurl_source: declared
  description: Element discovery and interaction
  name: Selenium Elements API
  slug: selenium-elements-api
- baseURL: http://localhost:4444
  baseurl_source: declared
  description: Page navigation and metadata
  name: Selenium Navigation API
  slug: selenium-navigation-api
- baseURL: http://localhost:4444
  baseurl_source: declared
  description: Execute JavaScript in the page context
  name: Selenium Script API
  slug: selenium-script-api
- baseURL: http://localhost:4444
  baseurl_source: declared
  description: Session lifecycle
  name: Selenium Session API
  slug: selenium-session-api
- baseURL: http://localhost:4444
  baseurl_source: declared
  description: Remote end readiness
  name: Selenium Status API
  slug: selenium-status-api
artifact_total: 23
asyncapis:
- description: ''
  name: Selenium Bidi Events
  slug: selenium-bidi-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol) Cookies API
  slug: open-selenium-cookies-api
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol) Cookies Elements API
  slug: open-selenium-elements-api
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol) Cookies Navigation API
  slug: open-selenium-navigation-api
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol) Cookies Script API
  slug: open-selenium-script-api
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol) Cookies Session API
  slug: open-selenium-session-api
- collection_type: open
  name: Selenium WebDriver (W3C Wire Protocol) Cookies Status API
  slug: open-selenium-status-api
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.selenium.dev/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://www.selenium.dev/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.selenium.dev/selenium/docs/api/java/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.selenium.dev/documentation/webdriver/getting_started/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/selenium-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/selenium-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/selenium-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/selenium-cli.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/selenium-grid.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/selenium-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/selenium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/selenium-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/selenium-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/selenium-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/selenium-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/selenium-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/selenium-changelog.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/selenium-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/selenium-bidi-events.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/selenium-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/selenium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/selenium-rate-limits.yml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/SeleniumHQ/selenium/releases
- group: other
  title: ''
  type: Governance
  url: https://www.selenium.dev/project/governance/
- group: commercial
  title: ''
  type: License
  url: https://www.selenium.dev/documentation/about/copyright/
created: '2024-01-01'
description: 'Selenium is the open-source browser automation project behind the W3C WebDriver and WebDriver BiDi standards. It drives real browsers through a vendor-neutral, standardised HTTP wire protocol that the browser vendors implement themselves, with official language bindings for Java, Python, C#, Ruby and JavaScript, all released in lockstep. The suite covers WebDriver (the browser-control protocol), Selenium Grid (distributed, parallel execution across machines and platforms), Selenium Manager (a Rust CLI that resolves and downloads matching browser drivers automatically) and Selenium IDE (record and playback). Selenium is self-hosted software rather than a service: there is no vendor-operated API host, no account and no pricing — the remote end runs on infrastructure the consumer owns, at a documented default of http://localhost:4444, under Apache-2.0 and the stewardship of the Software Freedom Conservancy.'
finops:
- name: Selenium Finops
  service_category: API
  slug: selenium-finops
image: https://www.selenium.dev/images/selenium-logo.svg
layout: provider
modified: '2026-08-26'
name: Selenium
nav: Providers
network: true
overview: 'Selenium publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cookies API, Elements API, Navigation API, and 3 more. Tagged areas include Automation, Browsers, End-to-End Testing, Quality Assurance, and Testing.


  The Selenium catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Selenium''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, CLI, authentication, and 28 more developer resources.'
plans:
- name: Selenium Plans Pricing
  plan_count: 0
  slug: selenium-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Selenium Rate Limits
  slug: selenium-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 48.2
    developer_ergonomics: 73.2
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/selenium/refs/heads/main/screenshots/selenium-2026-06-20T193639.png
security:
- kind: authentication
  name: Selenium Authentication
  slug: selenium-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Selenium Domain Security
  slug: selenium-domain-security
  summary_line: TLSv1.3
slug: selenium
tags:
- Automation
- Browsers
- End-to-End Testing
- Quality Assurance
- Testing
- WebDriver
website: https://www.selenium.dev/documentation/
---
