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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Unisys Agentic Access
  operation_count: 7
  slug: unisys-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 4
apis:
- description: Isolate and un-isolate both endpoints and users simultaneously
  name: Unisys Combined Isolation API
  slug: unisys-combined-isolation-api
- description: Isolate and un-isolate endpoints from the Stealth network
  name: Unisys Endpoint Isolation API
  slug: unisys-endpoint-isolation-api
- description: Retrieve Stealth network role configurations
  name: Unisys Roles API
  slug: unisys-roles-api
- description: Isolate and un-isolate users from the Stealth network
  name: Unisys User Isolation API
  slug: unisys-user-isolation-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unisys-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unisys-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unisys-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unisys-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.unisys.com/blog/
created: '2025-02-06'
description: Unisys is a global information technology company that provides specialized solutions integrated with leading-edge security. Unisys delivers digital workplace services, cloud and infrastructure services, and enterprise computing solutions including the ClearPath mainframe platform and the Unisys Stealth zero trust security suite. Unisys serves clients across industries including financial services, government, healthcare, and transportation.
examples:
- key_count: 2
  name: Unisys Stealth Get Roles Example
  slug: unisys-stealth-get-roles-example
- key_count: 2
  name: Unisys Stealth Isolate Endpoint Example
  slug: unisys-stealth-isolate-endpoint-example
- key_count: 2
  name: Unisys Stealth Isolate User Example
  slug: unisys-stealth-isolate-user-example
finops:
- name: Unisys Finops
  service_category: IT Services
  slug: unisys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unisys.png
json_schemas:
- name: ActionResponse
  property_count: 3
  slug: unisys-action-response
- name: IsolationRequest
  property_count: 3
  slug: unisys-isolation-request
- name: StealthRole
  property_count: 4
  slug: unisys-stealth-role
- name: UnisolationRequest
  property_count: 2
  slug: unisys-unisolation-request
json_structures:
- name: Unisys Action Response Structure
  property_count: 0
  slug: unisys-action-response-structure
- name: Unisys Isolation Request Structure
  property_count: 0
  slug: unisys-isolation-request-structure
- name: Unisys Stealth Role Structure
  property_count: 0
  slug: unisys-stealth-role-structure
jsonld:
- class_count: 0
  name: Unisys Context
  property_count: 11
  slug: unisys-context
layout: provider
modified: '2026-05-19'
name: Unisys
nav: Providers
network: true
overview: 'Unisys publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Combined Isolation API, Endpoint Isolation API, Roles API, and 1 more. Tagged areas include Fortune 1000, Security, Zero Trust, Network Security, and IT Services.


  The Unisys catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Unisys'' developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Unisys Plans Pricing
  plan_count: 1
  slug: unisys-plans-pricing
press:
- date: '2026-05-25'
  title: 'New Unisys Report: AI-Powered, Employee-Focused ...'
  url: https://www.prnewswire.com/news-releases/new-unisys-report-ai-powered-employee-focused-digital-workplaces-double-the-odds-of-exceeding-revenue-targets-302636061.html
- date: '2026-05-25'
  title: 'Unisys: Global Technology Solutions – Keep Breaking Through'
  url: https://www.unisys.com/
- date: '2026-05-25'
  title: ISG Names Unisys a Leader in its 2025 Provider Lens ...
  url: https://www.unisys.com/news-release/isg-names-unisys-a-leader-in-its-2025-provider-lens-for-cybersecurity-solutions-and-services/
- date: '2026-05-25'
  title: Investor Relations | Earnings Releases
  url: https://www.unisys.com/investor-relations/
- date: '2026-05-25'
  title: Earnings Releases
  url: https://www.unisys.com/investor-relations/earnings-releases/
random_paper: 67
rate_limits:
- limit_count: 1
  name: Unisys Rate Limits
  slug: unisys-rate-limits
rules:
- name: Unisys API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unisys-jsonschema-spectral-rules
- name: Unisys API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: unisys-spectral-rules
- name: Unisys API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 14
  slug: unisys-stealth-spectral-rules
score:
  band: thin
  composite: 40.2
  delta: -8.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.5
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Unisys Authentication
  slug: unisys-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unisys Domain Security
  slug: unisys-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unisys Vulnerability Disclosure
  slug: unisys-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unisys
tags:
- Fortune 1000
- Security
- Zero Trust
- Network Security
- IT Services
- Cybersecurity
- Enterprise Technology
---
