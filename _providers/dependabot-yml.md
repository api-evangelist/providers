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
api_count: 1
apis:
- description: The dependabot.yml schema, examples, validation rules, and capability catalog for configuring GitHub Dependabot.
  name: Dependabot Configuration
  slug: dependabot-config
artifact_total: 8
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/refs/heads/main/plans/dependabot-yml-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dependabot-yml-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/refs/heads/main/rate-limits/dependabot-yml-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dependabot-yml-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dependabot-yml/refs/heads/main/finops/dependabot-yml-finops.yml
  title: ''
  type: FinOps
  url: finops/dependabot-yml-finops.yml
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
- has_sources: false
  method: generated
  name: Dependabot Yml Finops
  primary_unit: ''
  service_category: API
  slug: dependabot-yml-finops
  template: true
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
overview: 'Dependabot.yml is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, CI/CD, Dependency Management, GitHub, and Security.


  The Dependabot.yml catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dependabot.yml''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Dependabot Yml Plans Pricing
  plan_count: 3
  slug: dependabot-yml-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Dependabot Yml Rate Limits
  slug: dependabot-yml-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
  extends: []
  name: Dependabot.yml — dependabot config rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: dependabot-config-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Dependabot.yml — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dependabot-yml-jsonschema-spectral-rules
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
