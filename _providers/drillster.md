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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Drillster REST API (v2.1.1) lets developers integrate Drillster's adaptive learning and training platform into external applications. It supports user account provisioning, group assignment, progr
  name: Drillster API
  slug: drillster-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drillster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drillster-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drillster
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drillster-bv
- group: company
  title: ''
  type: Website
  url: https://www.drillster.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.drillster.com/info/developers/
- group: agent
  title: ''
  type: LlmsText
  url: https://drillster.com/llms.txt
created: '2025-02-17'
description: Drillster is a digital learning platform that uses adaptive, repetition-based technology to help users acquire and retain knowledge and skills through personalized drills, quizzes, and learning modules.
finops:
- name: Drillster Finops
  service_category: API
  slug: drillster-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drillster.png
layout: provider
modified: '2026-04-28'
name: Drillster
nav: Providers
network: true
overview: 'Drillster publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Assessments, Education, Learning, Quizzes, and Training.


  Drillster''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Drillster Plans Pricing
  plan_count: 3
  slug: drillster-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 5
  name: Drillster Rate Limits
  slug: drillster-rate-limits
score:
  band: emerging
  composite: 11.5
  delta: -1.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drillster/refs/heads/main/screenshots/drillster-2026-06-20T180231.png
security:
- kind: domain-security
  name: Drillster Domain Security
  slug: drillster-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Drillster Vulnerability Disclosure
  slug: drillster-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: drillster
tags:
- Assessments
- Education
- Learning
- Quizzes
- Training
- LMS
website: https://www.drillster.com
---
