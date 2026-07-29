---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Sauce Labs Agentic Access
  operation_count: 18
  slug: sauce-labs-agentic-access
  summary_line: 18 operations · 8 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Retrieve information about Sauce Labs supported automation environments, browser/OS combinations, and overall platform status. Useful for dynamically querying available test configurations.
  name: Sauce Labs Platform API
  slug: platform
- description: Manage Sauce Connect Proxy tunnels programmatically. The Sauce Connect API provides endpoints for listing, creating, and stopping secure tunnels that allow testing of applications on private or intern
  name: Sauce Labs Sauce Connect API
  slug: sauce-connect
- description: Upload and manage application files (APK, IPA, ZIP) and other test artifacts in the Sauce Labs file storage service. Supports uploading apps, listing stored files, and deleting files used in test runs
  name: Sauce Labs Storage API
  slug: storage
- description: The Devices API from Sauce Labs — 2 operation(s) for devices.
  name: Sauce Labs Devices API
  slug: sauce-labs-devices-api
- description: The Job Assets API from Sauce Labs — 1 operation(s) for job assets.
  name: Sauce Labs Job Assets API
  slug: sauce-labs-job-assets-api
- description: The Jobs API from Sauce Labs — 3 operation(s) for jobs.
  name: Sauce Labs Jobs API
  slug: sauce-labs-jobs-api
- description: The Platform API from Sauce Labs — 2 operation(s) for platform.
  name: Sauce Labs Platform API
  slug: sauce-labs-platform-api
- description: The Sessions API from Sauce Labs — 5 operation(s) for sessions.
  name: Sauce Labs Sessions API
  slug: sauce-labs-sessions-api
- description: The Users API from Sauce Labs — 1 operation(s) for users.
  name: Sauce Labs Users API
  slug: sauce-labs-users-api
artifact_total: 28
collections:
- collection_type: postman
  name: Sauce Labs Jobs Devices API
  slug: postman-sauce-labs-devices-api
- collection_type: postman
  name: Sauce Labs Jobs Devices Job Assets API
  slug: postman-sauce-labs-job-assets-api
- collection_type: postman
  name: Sauce Labs Devices Jobs API
  slug: postman-sauce-labs-jobs-api
- collection_type: postman
  name: Sauce Labs Jobs Devices Platform API
  slug: postman-sauce-labs-platform-api
- collection_type: postman
  name: Sauce Labs Jobs Devices Sessions API
  slug: postman-sauce-labs-sessions-api
- collection_type: postman
  name: Sauce Labs Jobs Devices Users API
  slug: postman-sauce-labs-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sauce-labs/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sauce-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sauce-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sauce-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://saucelabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.saucelabs.com/dev/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saucelabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sauce-labs
- group: other
  title: ''
  type: X
  url: https://twitter.com/saucelabs
- group: company
  title: ''
  type: Blog
  url: https://saucelabs.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://saucelabs.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.saucelabs.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.saucelabs.com/en
- group: agent
  title: ''
  type: MCP
  url: https://github.com/saucelabs/sauce-api-mcp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/saucelabs/node-saucelabs
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sauce-labs-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sauce-labs-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/sauce-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sauce-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sauce-labs-finops.yml
created: '2026-06-12'
description: Sauce Labs is a cloud-based cross-browser and mobile app testing platform trusted by over 100,000 customers worldwide. It provides a comprehensive set of REST APIs for managing test jobs, devices, builds, insights, and results across virtual and real device clouds. The platform supports automated testing with frameworks like Appium, Espresso, and XCUITest, and integrates with popular CI/CD pipelines including GitHub Actions. Sauce Labs also offers API testing, contract testing, error reporting, and an MCP server for AI agent integrations.
examples:
- key_count: 3
  name: Sauce Labs Create Session Example
  slug: sauce-labs-create-session-example
- key_count: 2
  name: Sauce Labs Get Platform Status Example
  slug: sauce-labs-get-platform-status-example
finops:
- name: Sauce Labs Finops
  service_category: Developer Tools
  slug: sauce-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sauce-labs.png
json_schemas:
- name: Device
  property_count: 4
  slug: sauce-labs-device
- name: Job
  property_count: 34
  slug: sauce-labs-job
- name: Session
  property_count: 7
  slug: sauce-labs-session
jsonld:
- class_count: 2
  name: Sauce Labs Context
  property_count: 48
  slug: sauce-labs-context
layout: provider
modified: '2026-06-12'
name: Sauce Labs
nav: Providers
network: true
overview: 'Sauce Labs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Job Assets API, Jobs API, and 3 more. Tagged areas include Testing, Cross-Browser Testing, Mobile Testing, Real Devices, and Automation.


  The Sauce Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sauce Labs'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 15 more developer resources.'
plans:
- name: Sauce Labs Plans Pricing
  plan_count: 5
  slug: sauce-labs-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Sauce Labs Rate Limits
  slug: sauce-labs-rate-limits
rules:
- name: Sauce Labs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sauce-labs-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.7
  delta: -3.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.4
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 61.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sauce-labs/refs/heads/main/screenshots/sauce-labs-2026-06-20T193442.png
security:
- kind: authentication
  name: Sauce Labs Authentication
  slug: sauce-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sauce Labs Domain Security
  slug: sauce-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sauce-labs
tags:
- Testing
- Cross-Browser Testing
- Mobile Testing
- Real Devices
- Automation
- CI/CD
- Quality Assurance
website: https://saucelabs.com
---
