---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Printnode Agentic Access
  operation_count: 31
  slug: printnode-agentic-access
  summary_line: 31 operations · 11 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Account API from PrintNode — 4 operation(s) for account.
  name: PrintNode Account API
  slug: printnode-account-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The API Keys API from PrintNode — 1 operation(s) for api keys.
  name: PrintNode API Keys API
  slug: printnode-api-keys-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Clients API from PrintNode — 1 operation(s) for clients.
  name: PrintNode Clients API
  slug: printnode-clients-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Computers API from PrintNode — 2 operation(s) for computers.
  name: PrintNode Computers API
  slug: printnode-computers-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Printers API from PrintNode — 3 operation(s) for printers.
  name: PrintNode Printers API
  slug: printnode-printers-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Scales API from PrintNode — 3 operation(s) for scales.
  name: PrintNode Scales API
  slug: printnode-scales-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Utility API from PrintNode — 2 operation(s) for utility.
  name: PrintNode Utility API
  slug: printnode-utility-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Webhooks API from PrintNode — 1 operation(s) for webhooks.
  name: PrintNode Webhooks API
  slug: printnode-webhooks-api
- baseURL: https://api.printnode.com
  baseurl_source: declared
  description: The Print Jobs API from PrintNode — 4 operation(s) for print jobs.
  name: PrintNode Print Jobs API
  slug: printnode-print-jobs-api
artifact_total: 26
collections:
- collection_type: open
  name: PrintNode Account API
  slug: open-printnode-account-api
- collection_type: open
  name: PrintNode Account API Keys API
  slug: open-printnode-api-keys-api
- collection_type: open
  name: PrintNode Account Clients API
  slug: open-printnode-clients-api
- collection_type: open
  name: PrintNode Account Computers API
  slug: open-printnode-computers-api
- collection_type: open
  name: PrintNode Account Printers API
  slug: open-printnode-printers-api
- collection_type: open
  name: PrintNode Account PrintJobs API
  slug: open-printnode-printjobs-api
- collection_type: open
  name: PrintNode Account Scales API
  slug: open-printnode-scales-api
- collection_type: open
  name: PrintNode Account Utility API
  slug: open-printnode-utility-api
- collection_type: open
  name: PrintNode Account Webhooks API
  slug: open-printnode-webhooks-api
- collection_type: open
  name: PrintNode API
  slug: open-printnode
common:
- group: other
  href: https://artifacts.apis.io/printnode/capabilities/printnode-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/printnode-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/printnode/agentic-access/printnode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/printnode-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/printnode/security/printnode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/printnode-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/printnode/authentication/printnode-authentication.yml
  title: ''
  type: Authentication
  url: authentication/printnode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrintNode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printnode
- group: company
  title: ''
  type: Website
  url: https://www.printnode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.printnode.com/en/docs/api/curl
- group: commercial
  href: https://artifacts.apis.io/printnode/plans/printnode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/printnode-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/printnode/rate-limits/printnode-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/printnode-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/printnode/finops/printnode-finops.yml
  title: ''
  type: FinOps
  url: finops/printnode-finops.yml
created: '2026-06-25'
description: PrintNode is a cloud and remote printing service that lets web and server applications print to any physical printer through a lightweight client installed on a remote computer. Its REST API at https://api.printnode.com covers accounts, computers, printers, print jobs, scales, child-account/API-key management, and webhooks, using HTTP Basic authentication with an API key.
finops:
- has_sources: true
  method: generated
  name: Printnode Finops
  primary_unit: ''
  service_category: Printing and Output Management
  slug: printnode-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printnode.png
layout: provider
modified: '2026-06-25'
name: PrintNode
nav: Providers
network: true
overview: 'PrintNode publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Clients API, and 6 more. Tagged areas include Printing, Cloud Printing, Remote Printing, Print Jobs, and Hardware.


  The PrintNode catalog on APIs.io includes 1 Spectral governance ruleset.


  PrintNode''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Printnode Plans Pricing
  plan_count: 7
  slug: printnode-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Printnode Rate Limits
  slug: printnode-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: PrintNode API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 2
  slug: printnode-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 47.5
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/printnode/printnode-2026-09-02T152034.png
security:
- kind: authentication
  name: Printnode Authentication
  slug: printnode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Printnode Domain Security
  slug: printnode-domain-security
  summary_line: TLSv1.3 · DMARC
slug: printnode
tags:
- Printing
- Cloud Printing
- Remote Printing
- Print Jobs
- Hardware
website: https://www.printnode.com/
---
