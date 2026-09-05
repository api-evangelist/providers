---
access_model:
  confidence: medium
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Browserstack Agentic Access
  operation_count: 18
  slug: browserstack-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- description: Give your users a seamless experience by testing on 20,000 real devices.Dont compromise with emulators and simulators.
  name: BrowserStack
  slug: browserstack
- description: The BrowserStack Automate REST API provides access to plan, project, build, and session details for Selenium-based automated testing on real browsers and devices. It enables managing test sessions, re
  name: BrowserStack Automate API
  slug: automate-api
- description: The BrowserStack App Automate REST API enables running mobile automation tests and integrating CI/CD pipelines with BrowserStack. It supports Appium, Espresso, XCUITest, Flutter, Detox, and Maestro fr
  name: BrowserStack App Automate API
  slug: app-automate-api
- description: The BrowserStack Screenshots API enables headless screenshot creation for any URL across 3000+ real browser and OS combinations. It supports generating, managing, and retrieving screenshots via REST e
  name: BrowserStack Screenshots API
  slug: screenshots-api
- description: The BrowserStack App Live REST API supports uploading, viewing, and deleting mobile apps via command line or automation scripts. It enables managing .apk, .aab, and .ipa files for manual testing on re
  name: BrowserStack App Live API
  slug: app-live-api
- description: The BrowserStack Local Testing API helps manage and debug multiple Local Testing connections. It provides endpoints to list active binary instances, retrieve instance details, and disconnect running b
  name: BrowserStack Local Testing API
  slug: local-testing-api
- description: The BrowserStack Automate TurboScale REST API provides access to projects, builds, sessions, grids, and browser information for tests run on BrowserStack TurboScale infrastructure, including self-host
  name: BrowserStack Automate TurboScale API
  slug: automate-turboscale-api
- description: The BrowserStack Test Management API provides REST access to manage test projects, folders, test cases, test runs, test plans, test results, attachments, configurations, and custom fields for organizi
  name: BrowserStack Test Management API
  slug: test-management-api
- description: The BrowserStack Test Reporting and Analytics API provides programmatic access to upload JUnit XML and Allure reports, manage projects and builds, retrieve test executions, and check Quality Gate stat
  name: BrowserStack Test Reporting and Analytics API
  slug: test-reporting-and-analytics-api
- description: The BrowserStack Accessibility Testing API provides REST access to workflow analyzer, assisted tests, website scanner, and automated tests results for identifying and managing accessibility issues acr
  name: BrowserStack Accessibility Testing API
  slug: accessibility-testing-api
- description: The BrowserStack Percy API provides REST access for managing visual testing projects, builds, snapshots, Visual Git synchronization, and Visual Scanner capabilities to detect visual regressions across
  name: BrowserStack Percy API
  slug: percy-api
- description: The BrowserStack App Percy API provides automated visual testing for mobile applications across real iOS and Android devices, enabling teams to detect visual regressions and deploy with confidence.
  name: BrowserStack App Percy API
  slug: app-percy-api
- description: The BrowserStack User Management REST API enables enterprise account management including creating and managing users, teams, service accounts, usage reports, and audit logs. It requires an Enterprise
  name: BrowserStack User Management API
  slug: user-management-api
- description: The BrowserStack JavaScript Testing API provides HTTPS-based access to run JavaScript unit tests across 3000+ real desktop and mobile browsers in the cloud. It supports popular test frameworks includi
  name: BrowserStack JavaScript Testing API
  slug: javascript-testing-api
- description: The BrowserStack App Accessibility REST API enables programmatic access to accessibility data for mobile app projects and builds. It provides endpoints for retrieving accessibility results from automa
  name: BrowserStack App Accessibility Testing API
  slug: app-accessibility-testing-api
- description: The BrowserStack Low Code Automation REST API enables triggering test suite executions and retrieving build statuses for CI/CD pipeline integration. It also supports exporting low-code tests as code i
  name: BrowserStack Low Code Automation API
  slug: low-code-automation-api
- baseURL: https://api.browserstack.com
  baseurl_source: declared
  description: Operations on Automate access keys.
  name: BrowserStack AccessKey API
  slug: browserstack-accesskey-api
- baseURL: https://api.browserstack.com
  baseurl_source: declared
  description: Operations describing supported browsers and devices.
  name: BrowserStack Browsers API
  slug: browserstack-browsers-api
- baseURL: https://api.browserstack.com
  baseurl_source: declared
  description: Operations on Automate builds.
  name: BrowserStack Builds API
  slug: browserstack-builds-api
- baseURL: https://api.browserstack.com
  baseurl_source: declared
  description: Operations describing the current Automate subscription plan and capacity.
  name: BrowserStack Plan API
  slug: browserstack-plan-api
- baseURL: https://api.browserstack.com
  baseurl_source: declared
  description: Operations on Automate projects.
  name: BrowserStack Projects API
  slug: browserstack-projects-api
- baseURL: https://api.browserstack.com
  baseurl_source: declared
  description: Operations on Automate sessions.
  name: BrowserStack Sessions API
  slug: browserstack-sessions-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BrowserStack Automate REST AccessKey API
  slug: open-browserstack-accesskey-api
- collection_type: open
  name: BrowserStack Automate REST AccessKey Browsers API
  slug: open-browserstack-browsers-api
- collection_type: open
  name: BrowserStack Automate REST AccessKey Builds API
  slug: open-browserstack-builds-api
- collection_type: open
  name: BrowserStack Automate REST AccessKey Plan API
  slug: open-browserstack-plan-api
- collection_type: open
  name: BrowserStack Automate REST AccessKey Projects API
  slug: open-browserstack-projects-api
- collection_type: open
  name: BrowserStack Automate REST AccessKey Sessions API
  slug: open-browserstack-sessions-api
- collection_type: open
  name: BrowserStack Automate REST API
  slug: open-browserstack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/browserstack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/browserstack-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/browserstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/browserstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/browserstack
- group: company
  title: ''
  type: Website
  url: https://www.browserstack.com
- group: start
  title: ''
  type: Portal
  url: https://www.browserstack.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.browserstack.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://www.browserstack.com/docs/automate/api-reference/selenium/introduction#authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.browserstack.com
- group: company
  title: ''
  type: Blog
  url: https://www.browserstack.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.browserstack.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.browserstack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.browserstack.com/privacy
- group: start
  title: ''
  type: Signup
  url: https://www.browserstack.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://www.browserstack.com/users/sign_in
- group: operate
  title: ''
  type: Contact
  url: https://www.browserstack.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.browserstack.com/support
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.browserstack.com/release-notes/en
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/browserstack
- group: operate
  title: ''
  type: Community
  url: https://www.browserstack.com/community
- group: auth
  title: ''
  type: Security
  url: https://www.browserstack.com/vulnerability-disclosure-program
- group: build
  title: ''
  type: Developer Tools
  url: https://www.browserstack.com/docs/browserstack-mcp-server/overview
- group: agent
  title: ''
  type: WellKnown
  url: well-known/browserstack-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/browserstack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/browserstack-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/browserstack-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/browserstack-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/browserstack-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/browserstack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/browserstack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/browserstack-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/browserstack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/browserstack-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/browserstack-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/browserstack-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/browserstack-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/browserstack-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/browserstack-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/browserstack-plans-pricing.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.browserstack.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.browserstack.com/docs/automate/api-reference/selenium/introduction
created: '2025-02-17'
description: BrowserStack provides instant access to 3,500+ real desktop browsers and 30,000+ real mobile device units for manual and automated software testing. Its products span cross-browser testing (Live, Automate), mobile app testing (App Live, App Automate), visual regression testing (Percy, App Percy), accessibility testing, test management, test reporting and analytics, and low-code automation. Each product exposes its own REST API on its own host, and BrowserStack ships an official Model Context Protocol server — hosted at mcp.browserstack.com and distributed as an npm package — carrying 44 tools across those products.
finops:
- name: Browserstack Finops
  service_category: API
  slug: browserstack-finops
image: https://www.browserstack.com/images/browserstack-logo.svg
layout: provider
mcp_servers:
- description: BrowserStack's official Model Context Protocol server. It exposes 44 tools covering Test Management, Automate/App Automate SDK setup, Observability, Live and App Live manual sessions, Accessibility sc
  name: BrowserStack MCP Server
  slug: browserstack-mcp-server
modified: '2026-09-04'
name: BrowserStack
nav: Providers
network: true
overview: 'BrowserStack publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AccessKey API, Browsers API, Builds API, and 3 more. Tagged areas include Accessibility, Appium, Application, Automation, and CI/CD.


  BrowserStack''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, pricing, signup flow, support, and 36 more developer resources.'
plans:
- name: Browserstack Plans Pricing
  plan_count: 17
  slug: browserstack-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Browserstack Rate Limits
  slug: browserstack-rate-limits
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 73.2
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/browserstack/refs/heads/main/screenshots/browserstack-2026-06-20T173725.png
security:
- kind: authentication
  name: Browserstack Authentication
  slug: browserstack-authentication
  summary_line: http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Browserstack Domain Security
  slug: browserstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Browserstack Vulnerability Disclosure
  slug: browserstack-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Browserstack Trust Center
  slug: browserstack-trust-center
  summary_line: SOC 2, GDPR
slug: browserstack
tags:
- Accessibility
- Appium
- Application
- Automation
- CI/CD
- Cross-Browser Testing
- Enterprise
- JavaScript
- Low-Code
- Mobile Testing
- QA
- Regression Testing
- Selenium
- Testing
- Unit Testing
- Visual Testing
website: https://www.browserstack.com
---
