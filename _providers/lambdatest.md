---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - '{''url'': ''https://www.lambdatest.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.testmuai.com/ — a different registrable domain (lambdatest.com -> testmuai.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 3
  name: Lambdatest Agentic Access
  operation_count: 52
  slug: lambdatest-agentic-access
  summary_line: 52 operations · 20 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: REST API for managing mobile app test automation on real devices and emulators/simulators. Supports uploading iOS (.ipa) and Android (.apk/.aab) apps, listing devices by region, managing app versions,
  name: LambdaTest App Automation API
  slug: app-automation-api
- description: REST API for the HyperExecute AI-native test orchestration platform. Provides endpoints for triggering distributed test jobs, monitoring job status, fetching artifacts, and retrieving execution analyt
  name: LambdaTest HyperExecute API
  slug: hyperexecute-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Autoheal Command Logs API from LambdaTest — 1 operation(s) for autoheal command logs.
  name: LambdaTest Autoheal Command Logs API
  slug: lambdatest-autoheal-command-logs-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Build API from LambdaTest — 3 operation(s) for build.
  name: LambdaTest Build API
  slug: lambdatest-build-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The extensions API from LambdaTest — 2 operation(s) for extensions.
  name: LambdaTest extensions API
  slug: lambdatest-extensions-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Fetch Build Screenshots API from LambdaTest — 1 operation(s) for fetch build screenshots.
  name: LambdaTest Fetch Build Screenshots API
  slug: lambdatest-fetch-build-screenshots-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Geolocation API from LambdaTest — 1 operation(s) for geolocation.
  name: LambdaTest Geolocation API
  slug: lambdatest-geolocation-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Get Build Status API from LambdaTest — 1 operation(s) for get build status.
  name: LambdaTest Get Build Status API
  slug: lambdatest-get-build-status-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Get Screenshot Status API from LambdaTest — 1 operation(s) for get screenshot status.
  name: LambdaTest Get Screenshot Status API
  slug: lambdatest-get-screenshot-status-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Lighthouse API from LambdaTest — 1 operation(s) for lighthouse.
  name: LambdaTest Lighthouse API
  slug: lambdatest-lighthouse-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Organisation API from LambdaTest — 1 operation(s) for organisation.
  name: LambdaTest Organisation API
  slug: lambdatest-organisation-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The platforms API from LambdaTest — 1 operation(s) for platforms.
  name: LambdaTest platforms API
  slug: lambdatest-platforms-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The prerun API from LambdaTest — 4 operation(s) for prerun.
  name: LambdaTest prerun API
  slug: lambdatest-prerun-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Resolution API from LambdaTest — 1 operation(s) for resolution.
  name: LambdaTest Resolution API
  slug: lambdatest-resolution-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Session API from LambdaTest — 13 operation(s) for session.
  name: LambdaTest Session API
  slug: lambdatest-session-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Session Logs (V2) API from LambdaTest — 6 operation(s) for session logs (v2).
  name: LambdaTest Session Logs (V2) API
  slug: lambdatest-session-logs-v2-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Test API from LambdaTest — 2 operation(s) for test.
  name: LambdaTest Test API
  slug: lambdatest-test-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The tunnel API from LambdaTest — 2 operation(s) for tunnel.
  name: LambdaTest tunnel API
  slug: lambdatest-tunnel-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The Upload Screenshots API from LambdaTest — 1 operation(s) for upload screenshots.
  name: LambdaTest Upload Screenshots API
  slug: lambdatest-upload-screenshots-api
- baseURL: https://api.lambdatest.com
  baseurl_source: declared
  description: The user-files API from LambdaTest — 3 operation(s) for user-files.
  name: LambdaTest user-files API
  slug: lambdatest-user-files-api
artifact_total: 78
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs API
  slug: open-lambdatest-autoheal-command-logs-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Build API
  slug: open-lambdatest-build-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs extensions API
  slug: open-lambdatest-extensions-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Fetch Build Screenshots API
  slug: open-lambdatest-fetch-build-screenshots-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Geolocation API
  slug: open-lambdatest-geolocation-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Get Build Status API
  slug: open-lambdatest-get-build-status-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Get Screenshot Status API
  slug: open-lambdatest-get-screenshot-status-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Lighthouse API
  slug: open-lambdatest-lighthouse-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Organisation API
  slug: open-lambdatest-organisation-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs platforms API
  slug: open-lambdatest-platforms-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs prerun API
  slug: open-lambdatest-prerun-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Resolution API
  slug: open-lambdatest-resolution-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Session API
  slug: open-lambdatest-session-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Session Logs (V2) API
  slug: open-lambdatest-session-logs-v2-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Test API
  slug: open-lambdatest-test-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs tunnel API
  slug: open-lambdatest-tunnel-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs Upload Screenshots API
  slug: open-lambdatest-upload-screenshots-api
- collection_type: open
  name: TestMu AI SmartUI API Documentation Autoheal Command Logs user-files API
  slug: open-lambdatest-user-files-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lambdatest-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lambdatest-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lambdatest-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lambdatest-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/LambdaTest/agent-skills
- group: company
  title: ''
  type: Website
  url: https://www.lambdatest.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.lambdatest.com/support/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LambdaTest
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lambdatest
- group: other
  title: ''
  type: X
  url: https://x.com/lambdatesting
- group: company
  title: ''
  type: Blog
  url: https://www.lambdatest.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lambdatest.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lambdatest.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/lambdatest-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lambdatest-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lambdatest-finops.yml
created: '2026-06-12'
description: LambdaTest (rebranding as TestMu AI) is a cloud-based AI-powered test execution platform that enables developers and QA teams to run Selenium, Cypress, Playwright, and Appium automation tests across 3,000+ browser and OS combinations at scale. The platform provides live interactive cross-browser and real device testing, visual regression testing with SmartUI, and AI-native test orchestration via HyperExecute. LambdaTest exposes a suite of REST APIs for managing test sessions, uploading mobile apps, retrieving test results, and controlling tunnel connections, all secured with HTTP Basic Authentication using a username and access key. The platform serves over 2 million developers and testers across 10,000+ enterprise customers in 130 countries.
examples:
- key_count: 1
  name: Lambdatest Get Session Example
  slug: lambdatest-get-session-example
- key_count: 2
  name: Lambdatest List Builds Example
  slug: lambdatest-list-builds-example
- key_count: 2
  name: Lambdatest Smartui Build Status Example
  slug: lambdatest-smartui-build-status-example
finops:
- name: Lambdatest Finops
  service_category: Developer Tools / Quality Engineering
  slug: lambdatest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lambdatest.png
json_schemas:
- name: LambdaTest Build
  property_count: 11
  slug: lambdatest-build
- name: LambdaTest Session
  property_count: 24
  slug: lambdatest-session
- name: LambdaTest SmartUI Build
  property_count: 10
  slug: lambdatest-smartui-build
jsonld:
- class_count: 5
  name: Lambdatest Context
  property_count: 38
  slug: lambdatest-context
layout: provider
modified: '2026-06-12'
name: LambdaTest
nav: Providers
network: true
overview: 'LambdaTest publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Autoheal Command Logs API, Build API, extensions API, and 15 more. Tagged areas include Testing, Cross-Browser Testing, Selenium, Cypress, and Playwright.


  The LambdaTest catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LambdaTest''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Lambdatest Plans Pricing
  plan_count: 12
  slug: lambdatest-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Lambdatest Rate Limits
  slug: lambdatest-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: LambdaTest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lambdatest-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 58.8
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lambdatest/refs/heads/main/screenshots/lambdatest-2026-06-20T184255.png
security:
- kind: authentication
  name: Lambdatest Authentication
  slug: lambdatest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lambdatest Domain Security
  slug: lambdatest-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Lambdatest Trust Center
  slug: lambdatest-trust-center
  summary_line: SOC 2, GDPR
skill_count: 71
skills:
- name: api-ai-augmented
  slug: api-ai-augmented
- name: api-analyzer
  slug: api-analyzer
- name: api-compliance-checker
  slug: api-compliance-checker
- name: api-designer
  slug: api-designer
- name: api-documentation
  slug: api-documentation
- name: api-fetcher-specific-domains
  slug: api-fetcher-specific-domains
- name: api-graphql-grpc
  slug: api-graphql-grpc
- name: api-health-monitoring
  slug: api-health-monitoring
- name: api-inferrer-from-files
  slug: api-inferrer-from-files
- name: api-integration
  slug: api-integration
- name: api-mock-helper
  slug: api-mock-helper
- name: api-rate-limiting-helper
  slug: api-rate-limiting-helper
- name: api-sdk-generator
  slug: api-sdk-generator
- name: api-security-auth-pattern
  slug: api-security-auth-pattern
- name: api-to-testcase-generator
  slug: api-to-testcase-generator
- name: api-versioning-helper
  slug: api-versioning-helper
- name: appium-skill
  slug: appium-skill
- name: behat-skill
  slug: behat-skill
- name: behave-skill
  slug: behave-skill
- name: capybara-skill
  slug: capybara-skill
- name: cicd-pipeline-skill
  slug: cicd-pipeline-skill
- name: codeception-skill
  slug: codeception-skill
- name: cucumber-skill
  slug: cucumber-skill
- name: cypress-skill
  slug: cypress-skill
slug: lambdatest
tags:
- Testing
- Cross-Browser Testing
- Selenium
- Cypress
- Playwright
- Mobile Testing
- Automation
- QA
- Visual Regression
website: https://www.lambdatest.com
---
