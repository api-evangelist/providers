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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 2
  name: Scrapybara Agentic Access
  operation_count: 32
  slug: scrapybara-agentic-access
  summary_line: 32 operations · 22 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Auth States API from Scrapybara — 4 operation(s) for auth states.
  name: Scrapybara Auth States API
  slug: scrapybara-auth-states-api
- description: The Browser API from Scrapybara — 4 operation(s) for browser.
  name: Scrapybara Browser API
  slug: scrapybara-browser-api
- description: The Code Execution API from Scrapybara — 2 operation(s) for code execution.
  name: Scrapybara Code Execution API
  slug: scrapybara-code-execution-api
- description: The Computer Actions API from Scrapybara — 3 operation(s) for computer actions.
  name: Scrapybara Computer Actions API
  slug: scrapybara-computer-actions-api
- description: The Environment API from Scrapybara — 1 operation(s) for environment.
  name: Scrapybara Environment API
  slug: scrapybara-environment-api
- description: The Filesystem API from Scrapybara — 3 operation(s) for filesystem.
  name: Scrapybara Filesystem API
  slug: scrapybara-filesystem-api
- description: The Instances API from Scrapybara — 6 operation(s) for instances.
  name: Scrapybara Instances API
  slug: scrapybara-instances-api
- description: The Notebook API from Scrapybara — 6 operation(s) for notebook.
  name: Scrapybara Notebook API
  slug: scrapybara-notebook-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scrapybara Auth States API
  slug: open-scrapybara-auth-states-api
- collection_type: open
  name: Scrapybara Auth States Browser API
  slug: open-scrapybara-browser-api
- collection_type: open
  name: Scrapybara Auth States Code Execution API
  slug: open-scrapybara-code-execution-api
- collection_type: open
  name: Scrapybara Auth States Computer Actions API
  slug: open-scrapybara-computer-actions-api
- collection_type: open
  name: Scrapybara Auth States Environment API
  slug: open-scrapybara-environment-api
- collection_type: open
  name: Scrapybara Auth States Filesystem API
  slug: open-scrapybara-filesystem-api
- collection_type: open
  name: Scrapybara Auth States Instances API
  slug: open-scrapybara-instances-api
- collection_type: open
  name: Scrapybara Auth States Notebook API
  slug: open-scrapybara-notebook-api
- collection_type: open
  name: Scrapybara API
  slug: open-scrapybara
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scrapybara-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrapybara-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scrapybara-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scrapybara
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scrapybara
- group: company
  title: ''
  type: Website
  url: https://scrapybara.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scrapybara.com
- group: commercial
  title: ''
  type: Plans
  url: plans/scrapybara-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scrapybara-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scrapybara-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://scrapybara.com/blog
created: '2026-07-01'
description: Scrapybara provides virtual desktops for AI agents - remote Ubuntu, browser, and Windows instances that computer-use models can see and control. A single x-api-key REST API starts and manages cloud instances, streams the desktop, runs computer / keyboard / mouse actions, drives Chromium over Playwright CDP, executes bash and code, manages the filesystem and Jupyter notebooks, and saves reusable browser auth states.
finops:
- name: Scrapybara Finops
  service_category: Compute
  slug: scrapybara-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scrapybara.png
layout: provider
modified: '2026-07-01'
name: Scrapybara
nav: Providers
network: true
overview: 'Scrapybara publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth States API, Browser API, Code Execution API, and 5 more. Tagged areas include AI Agents, Virtual Desktops, Computer Use, Browser Automation, and Code Execution.


  Scrapybara''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Scrapybara Plans Pricing
  plan_count: 4
  slug: scrapybara-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Scrapybara Rate Limits
  slug: scrapybara-rate-limits
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
    contract_quality: 50.5
    developer_ergonomics: 31.0
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
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Scrapybara Authentication
  slug: scrapybara-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scrapybara Domain Security
  slug: scrapybara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scrapybara
tags:
- AI Agents
- Virtual Desktops
- Computer Use
- Browser Automation
- Code Execution
website: https://scrapybara.com/
---
