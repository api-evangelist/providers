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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Browser Use Agentic Access
  operation_count: 24
  slug: browser-use-agentic-access
  summary_line: 24 operations · 12 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Browser Use is an open-source framework for AI-powered browser automation and web interaction.
  name: Browser Use
  slug: browser-use
- description: The Billing API from Browser Use — 2 operation(s) for billing.
  name: Browser Use Billing API
  slug: browser-use-billing-api
- description: The Browsers API from Browser Use — 3 operation(s) for browsers.
  name: Browser Use Browsers API
  slug: browser-use-browsers-api
- description: The Profiles API from Browser Use — 2 operation(s) for profiles.
  name: Browser Use Profiles API
  slug: browser-use-profiles-api
- description: The Sessions API from Browser Use — 5 operation(s) for sessions.
  name: Browser Use Sessions API
  slug: browser-use-sessions-api
- description: The Workspaces API from Browser Use — 5 operation(s) for workspaces.
  name: Browser Use Workspaces API
  slug: browser-use-workspaces-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Browser Use Cloud Billing API
  slug: open-browser-use-billing-api
- collection_type: open
  name: Browser Use Cloud Billing Browsers API
  slug: open-browser-use-browsers-api
- collection_type: open
  name: Browser Use Cloud Billing Profiles API
  slug: open-browser-use-profiles-api
- collection_type: open
  name: Browser Use Cloud Billing Sessions API
  slug: open-browser-use-sessions-api
- collection_type: open
  name: Browser Use Cloud Billing Workspaces API
  slug: open-browser-use-workspaces-api
- collection_type: open
  name: Browser Use Cloud API
  slug: open-browser-use
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/browser-use-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/browser-use-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/browser-use-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/browser-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/browser-use
- group: company
  title: ''
  type: Website
  url: https://browser-use.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.browser-use.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.browser-use.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://browser-use.com/rss.xml
created: '2026-03-27'
description: Browser Use is an open-source framework for AI-powered browser automation and web interaction.
finops:
- name: Browser Use Finops
  service_category: API
  slug: browser-use-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/browser-use.png
layout: provider
modified: '2026-03-27'
name: Browser Use
nav: Providers
network: true
overview: 'Browser Use publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Browsers API, Profiles API, and 2 more. Tagged areas include AI Automation and Browser Automation.


  Browser Use''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Browser Use Plans Pricing
  plan_count: 3
  slug: browser-use-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Browser Use Rate Limits
  slug: browser-use-rate-limits
score:
  band: thin
  composite: 28.5
  delta: 0.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 23.8
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/screenshots/browser-use-2026-06-20T173722.png
security:
- kind: authentication
  name: Browser Use Authentication
  slug: browser-use-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Browser Use Domain Security
  slug: browser-use-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: browser-use
tags:
- AI Automation
- Browser Automation
website: https://browser-use.com
---
