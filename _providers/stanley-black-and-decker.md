---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 2
  human_in_the_loop: 0
  name: Stanley Black And Decker Agentic Access
  operation_count: 12
  slug: stanley-black-and-decker-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 6
apis:
- description: Stanley X is the innovation arm of Stanley Black & Decker that provides IoT connectivity APIs enabling smart factory solutions, equipment management, and digital manufacturing workflows. Partners inte
  name: Stanley X IoT API
  slug: stanley-x-iot-api
- description: Asset inventory and tracking operations
  name: Stanley Black & Decker Assets API
  slug: stanley-black-and-decker-assets-api
- description: Battery tracking and status operations
  name: Stanley Black & Decker Batteries API
  slug: stanley-black-and-decker-batteries-api
- description: Jobsite management operations
  name: Stanley Black & Decker Jobsites API
  slug: stanley-black-and-decker-jobsites-api
- description: Connected tool management operations
  name: Stanley Black & Decker Tools API
  slug: stanley-black-and-decker-tools-api
- description: User and team management operations
  name: Stanley Black & Decker Users API
  slug: stanley-black-and-decker-users-api
artifact_total: 21
collections:
- collection_type: open
  name: Stanley Black & Decker Tool Connect API
  slug: open-stanley-black-and-decker-tool-connect-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stanley-black-and-decker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stanley-black-and-decker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stanley-black-and-decker-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.stanleyblackanddecker.com/
- group: company
  title: ''
  type: Website
  url: https://www.dewalt.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.stanley.com/
- group: start
  title: ''
  type: Portal
  url: https://sitemanager.dewalt.com/
- group: company
  title: ''
  type: Blog
  url: https://www.stanleyblackanddecker.com/news-stories
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stanleyblackanddecker.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stanleyblackanddecker.com/terms-use
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/StanleyInnovation
- group: other
  title: ''
  type: X
  url: https://x.com/SBDinnovates
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stanley-black-and-decker
created: '2024-01-01'
description: Stanley Black & Decker is a global manufacturer and marketer of hand tools, power tools, and related accessories. Through brands like DEWALT, Stanley, Craftsman, and Black+Decker, the company provides connected tool management platforms, IoT solutions, and partner integrations for jobsite productivity.
examples:
- key_count: 2
  name: Stanley Black And Decker List Tools Example
  slug: stanley-black-and-decker-list-tools-example
- key_count: 2
  name: Stanley Black And Decker Register Asset Example
  slug: stanley-black-and-decker-register-asset-example
finops:
- name: Stanley Black And Decker Finops
  service_category: IoT / Connected Hardware
  slug: stanley-black-and-decker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stanley-black-and-decker.png
json_schemas:
- name: DEWALT Battery
  property_count: 12
  slug: stanley-black-and-decker-battery
- name: DEWALT Connected Tool
  property_count: 15
  slug: stanley-black-and-decker-tool
json_structures:
- name: Stanley Black And Decker Tool Structure
  property_count: 0
  slug: stanley-black-and-decker-tool-structure
jsonld:
- class_count: 35
  name: Stanley Black And Decker Context
  property_count: 3
  slug: stanley-black-and-decker-context
layout: provider
modified: '2026-05-19'
name: Stanley Black & Decker
nav: Providers
network: true
overview: 'Stanley Black & Decker publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Batteries API, Jobsites API, and 2 more. Tagged areas include Tools, Hardware, Manufacturing, IoT, and Connected Tools.


  The Stanley Black & Decker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stanley Black & Decker''s developer surface includes authentication, developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Stanley Black And Decker Plans Pricing
  plan_count: 1
  slug: stanley-black-and-decker-plans-pricing
press:
- date: '2026-05-25'
  title: 'Employee Stories: Scott G.'
  url: https://www.stanleyblackanddecker.com/careers/why-work-here/meet-our-employees/scott-g
- date: '2026-05-25'
  title: 'Employee Stories: Amir K.'
  url: https://www.stanleyblackanddecker.com/careers/why-work-here/meet-our-employees/amir-k
- date: '2026-05-25'
  title: Stanley Black & Decker Completes Sale of Consolidated ...
  url: https://www.prnewswire.com/news-releases/stanley-black--decker-completes-sale-of-consolidated-aerospace-manufacturing-business-to-howmet-aerospace-302734667.html
- date: '2026-05-25'
  title: VDE and Stanley Black & Decker launch strategic ...
  url: https://www.vde.com/en/press/press-releases/strategic-cooperation-vde-stanley-black-decker
- date: '2026-05-25'
  title: H2O.ai Empowers Stanley Black & Decker to Develop ...
  url: https://h2o.ai/company/press-media/2018/h2o-ai-empowers-stanley-black-decker-to-develop-innovative-manufacturing-processes/
random_paper: 50
rate_limits:
- limit_count: 1
  name: Stanley Black And Decker Rate Limits
  slug: stanley-black-and-decker-rate-limits
rules:
- name: Stanley Black & Decker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stanley-black-and-decker-jsonschema-spectral-rules
- name: Stanley Black & Decker API Rules
  rule_count: 20
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 12
  slug: stanley-black-and-decker-rules
score:
  band: developing
  composite: 46.9
  delta: -3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.6
    developer_ergonomics: 21.7
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stanley-black-and-decker/refs/heads/main/screenshots/stanley-black-and-decker-2026-06-20T194505.png
security:
- kind: authentication
  name: Stanley Black And Decker Authentication
  slug: stanley-black-and-decker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stanley Black And Decker Domain Security
  slug: stanley-black-and-decker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stanley-black-and-decker
tags:
- Tools
- Hardware
- Manufacturing
- IoT
- Connected Tools
- Fortune 500
website: https://www.stanleyblackanddecker.com/
---
