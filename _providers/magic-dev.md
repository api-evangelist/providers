---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/magic-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magic-dev-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magicproduct
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magicailabs
- group: company
  title: ''
  type: Website
  url: https://magic.dev
- group: company
  title: ''
  type: Blog
  url: https://magic.dev/blog
- group: company
  title: ''
  type: Careers
  url: https://magic.dev/careers
- group: other
  title: ''
  type: Safety
  url: https://magic.dev/safety
created: '2026-07-02'
description: Magic (magic.dev) is a San Francisco frontier AI research lab building frontier-scale code models - an "AI coworker" for software engineering, and ultimately a path to safe AGI - rather than a shipping developer product. It has raised roughly $515M from Nat Friedman, Daniel Gross, CapitalG, Elad Gil, Sequoia, Jane Street, and Eric Schmidt, and has published research on ultra-long-context models (LTM-1 at a 5M token context window, and the unreleased LTM-2-mini research prototype claimed to handle up to 100M tokens). As of this review Magic does not publish a public, self-serve developer API, API reference, SDK, or waitlist; its website and careers pages describe mission, research, and open roles only, with no product access model, pricing, or documented endpoints. Its GitHub organization (magicproduct) hosts research tooling (e.g. hash-hop, a long-context evaluation harness) and infrastructure forks, not an API client or SDK.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magic-dev.png
layout: provider
modified: '2026-07-02'
name: Magic
nav: Providers
network: true
overview: 'Magic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, AGI Research, Coding Agent, Long Context, and LLM.


  Magic''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 57
score:
  band: minimal
  composite: 6.1
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magic-dev/refs/heads/main/screenshots/magic-dev-2026-07-25T225842.png
security:
- kind: domain-security
  name: Magic Dev Domain Security
  slug: magic-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Magic Dev Vulnerability Disclosure
  slug: magic-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: magic-dev
tags:
- AI
- AGI Research
- Coding Agent
- Long Context
- LLM
- Frontier Lab
- No Public API
website: https://magic.dev
---
