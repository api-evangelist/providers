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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: 'Repolinter is an open source linting tool for repositories that validates compliance with open source best practices. It checks repositories for standard files like LICENSE, README, CONTRIBUTING, and '
  name: Repolinter
  slug: repolinter
- description: A GitHub Action that runs Repolinter on repositories as part of CI/CD workflows. Validates repositories against configurable rulesets to enforce open source compliance policies. Supports outputting re
  name: Repolinter Action
  slug: repolinter-action
- description: 'An interactive landscape mapping the Open Source Program Office ecosystem, including OSPO adopter organizations and tools supporting OSPO operations. Data is maintained in landscape.yml and browsable '
  name: OSPO Landscape
  slug: ospo-landscape
- description: A comprehensive collection of 23+ practitioner guides covering all aspects of running Open Source Program Offices. Topics include creating an OSPO, setting open source strategy, measuring program succ
  name: OSPO Guides
  slug: ospo-guides
- description: The OSPOlogy program provides monthly community webinars, working group meetings, and collaborative sessions focused on OSPO practices and challenges. It serves as the primary community engagement pla
  name: OSPOlogy
  slug: ospology
artifact_total: 29
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/todogroup/repolinter/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/todo-group-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/todo-group
- group: company
  title: ''
  type: Website
  url: https://todogroup.org/
- group: docs
  title: ''
  type: Documentation
  url: https://todogroup.org/guides/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/todogroup
- group: operate
  title: ''
  type: Slack
  url: https://slack.todogroup.org/
- group: company
  title: ''
  type: Newsletter
  url: https://todogroup.org/community/newsletter/
- group: design
  title: ''
  type: SpectralRules
  url: rules/todo-group-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/todo-group-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://todogroup.org/blog/
- group: company
  title: ''
  type: Careers
  url: https://github.com/todogroup/ospo-career-path
created: '2026-03-16'
description: The TODO Group is an open community of practitioners under the Linux Foundation who collaborate on best practices, tools, and guidance for running successful Open Source Program Offices (OSPOs). It provides open source tooling including Repolinter for repository linting, the OSPO Landscape mapping OSPO adopters and tools, comprehensive OSPO guides and case studies, and OSPOlogy community programs. The TODO Group serves organizations managing enterprise open source strategies across 120+ member organizations.
features:
- description: Command-line tool for linting open source repositories against configurable compliance rulesets.
  name: Repolinter CLI
- description: Programmatic Node.js API for integrating repository linting into custom workflows and tools.
  name: Repolinter JavaScript API
- description: CI/CD integration for automated repository compliance checks in GitHub workflows.
  name: Repolinter GitHub Action
- description: Interactive ecosystem map of OSPO adopter organizations and supporting tools worldwide.
  name: OSPO Landscape
- description: Comprehensive practitioner guides covering all aspects of running an Open Source Program Office.
  name: OSPO Guides
- description: Monthly community webinars and working group sessions for OSPO practitioners.
  name: OSPOlogy Webinars
- description: Structured career framework defining roles, skills, and progression paths for OSPO professionals.
  name: OSPO Career Path
- description: Curated list of tools and resources for open source program management.
  name: Awesome OSPO
finops:
- name: Todo Group Finops
  service_category: API
  slug: todo-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/todo-group.png
integrations:
- description: Repolinter Action integrates repository linting into GitHub CI/CD workflows.
  name: GitHub Actions
- description: TODO Group operates under the Linux Foundation governance and community infrastructure.
  name: Linux Foundation
- description: OSPO Landscape follows the CNCF landscape pattern for ecosystem visualization.
  name: CNCF Landscape
- description: Repolinter is distributed as an npm package and supports Node.js 12+ runtime.
  name: Node.js / npm
- description: Collaboration with Open Source Security Foundation on best practices for open source security and compliance.
  name: OpenSSF
layout: provider
modified: '2026-07-25'
name: TODO Group
nav: Providers
network: true
overview: 'TODO Group publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Community, Linux Foundation, Open-Source, and OSPO.


  The TODO Group catalog on APIs.io includes 1 Spectral governance ruleset.


  TODO Group''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Todo Group Plans Pricing
  plan_count: 3
  slug: todo-group-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Todo Group Rate Limits
  slug: todo-group-rate-limits
rules:
- effective_rule_count: 29
  extends: []
  name: TODO Group API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 16
  slug: todo-group-spectral-rules
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 69.7
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.6
    governance: 69.7
    operational_transparency: 13.2
  previous_composite: 22.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/todo-group/refs/heads/main/screenshots/todo-group-2026-06-20T195427.png
security:
- kind: domain-security
  name: Todo Group Domain Security
  slug: todo-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: todo-group
tags:
- Community
- Linux Foundation
- Open-Source
- OSPO
use_cases:
- description: Use Repolinter and Repolinter Action to automate checks that all repos have required open source files and follow organizational policies.
  name: Repository Compliance Automation
- description: Use TODO Group guides and case studies to establish and launch a new Open Source Program Office within an organization.
  name: OSPO Program Launch
- description: Reference the OSPO Landscape to discover tools, peer organizations, and adopters in the OSPO ecosystem.
  name: OSPO Ecosystem Mapping
- description: Apply the OSPO Career Path framework to define roles and progression for open source professionals.
  name: Developer Career Development
- description: Leverage TODO Group best practice guides to define and implement an enterprise open source strategy.
  name: Open Source Strategy Development
- description: Participate in OSPOlogy webinars and TODO Group working groups to learn from and contribute to the OSPO community.
  name: Community Building
website: https://todogroup.org/
---
