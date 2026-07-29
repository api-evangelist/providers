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
- description: The dependabot.yml schema, examples, validation rules, and capability catalog for configuring GitHub Dependabot.
  name: Dependabot Configuration
  slug: dependabot-config
artifact_total: 8
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2025-01-01'
description: GitHub Dependabot configuration file defining automated dependency update schedules, package ecosystems to monitor, grouping, cooldown, and review assignment rules.
finops:
- name: Dependabot Yml Finops
  service_category: API
  slug: dependabot-yml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dependabot-yml.png
json_schemas:
- name: Dependabot Configuration
  property_count: 4
  slug: dependabot-config
jsonld:
- class_count: 0
  name: Dependabot Yml Context
  property_count: 0
  slug: dependabot-yml
layout: provider
modified: '2026-04-28'
name: Dependabot.yml
nav: Providers
network: true
overview: 'Dependabot.yml publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, CI/CD, Dependency Management, GitHub, and Security.


  The Dependabot.yml catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dependabot.yml''s developer surface includes documentation and 1 more developer resources.'
plans:
- name: Dependabot Yml Plans Pricing
  plan_count: 3
  slug: dependabot-yml-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Dependabot Yml Rate Limits
  slug: dependabot-yml-rate-limits
rules:
- name: Dependabot.yml API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: dependabot-config-rules
- name: Dependabot.yml API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dependabot-yml-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.2
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 8.7
    discoverability: 40.7
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 26.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/refs/heads/main/screenshots/dependabot-yml-2026-06-20T175926.png
slug: dependabot-yml
tags:
- Automation
- CI/CD
- Dependency Management
- GitHub
- Security
- Open Source
---
