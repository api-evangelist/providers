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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
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
  description: The PrintJobs API from PrintNode — 4 operation(s) for printjobs.
  name: PrintNode PrintJobs API
  slug: printnode-printjobs-api
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
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/printnode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printnode-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/printnode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/printnode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/printnode-finops.yml
created: '2026-06-25'
description: PrintNode is a cloud and remote printing service that lets web and server applications print to any physical printer through a lightweight client installed on a remote computer. Its REST API at https://api.printnode.com covers accounts, computers, printers, print jobs, scales, child-account/API-key management, and webhooks, using HTTP Basic authentication with an API key.
finops:
- name: Printnode Finops
  service_category: Printing and Output Management
  slug: printnode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printnode.png
layout: provider
modified: '2026-06-25'
name: PrintNode
nav: Providers
network: true
overview: 'PrintNode publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Clients API, and 6 more. Tagged areas include Printing, Cloud Printing, Remote Printing, Print Jobs, and Hardware.


  PrintNode''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Printnode Plans Pricing
  plan_count: 7
  slug: printnode-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Printnode Rate Limits
  slug: printnode-rate-limits
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/printnode/refs/heads/main/screenshots/printnode-2026-09-02T152034.png
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
