---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/api-evangelist/gtm-release/issues
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gtm-release-llms.txt
coverage:
  checked: '2026-08-13'
  detail: GTM Release is an API Evangelist first-party network index of 55 go-to-market channels — it ships no product, has no website, developer portal, or base URL of its own, and the only surface it publishes is the apis.yml index in this repository; every API in it belongs to a separately profiled member provider.
  evidence:
  - status: 200
    url: https://raw.githubusercontent.com/api-evangelist/gtm-release/refs/heads/main/apis.yml
  - status: 200
    url: https://apis.io/providers/gtm-release/
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: An API Evangelist network index of the 55 companies, platforms, and events that make up a software go-to-market release surface — press and tech media, developer communities and content platforms, open-source and developer-tool directories, social media, podcasts, business and startup directories, product-launch and SaaS platforms, review platforms, and conferences. GTM Release is not a company and operates no API of its own; each member is a separately profiled provider in the api-evangelist network with its own apis.yml, artifacts, and Kin Score.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gtm-release.png
layout: provider
modified: '2026-08-13'
name: GTM Release
nav: Providers
network: true
overview: GTM Release is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Conferences, Events, Developer Communities, Directories, and GTM.
random_paper: 18
score:
  band: minimal
  composite: 6.1
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 6.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: gtm-release
tags:
- Conferences
- Events
- Developer Communities
- Directories
- GTM
- Marketing
- Press
- Release
- Review Platforms
---
