---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: CrewAI is a framework for orchestrating role-playing autonomous AI agents that collaborate on complex tasks.
  name: CrewAI
  slug: crewai
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crewai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crewai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crewAIInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crewai-inc
- group: company
  title: ''
  type: Website
  url: https://www.crewai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.crewai.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.crewai.com/blog
created: '2026-03-27'
description: CrewAI is a framework for orchestrating role-playing autonomous AI agents that collaborate on complex tasks.
finops:
- name: Crewai Finops
  service_category: API
  slug: crewai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crewai.png
layout: provider
modified: '2026-03-27'
name: CrewAI
nav: Providers
network: true
overview: 'CrewAI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents and AI Automation.


  CrewAI''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Crewai Plans Pricing
  plan_count: 3
  slug: crewai-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Crewai Rate Limits
  slug: crewai-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: -1.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crewai/refs/heads/main/screenshots/crewai-2026-06-20T175231.png
security:
- kind: domain-security
  name: Crewai Domain Security
  slug: crewai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crewai Vulnerability Disclosure
  slug: crewai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crewai
tags:
- AI Agents
- AI Automation
website: https://www.crewai.com
---
