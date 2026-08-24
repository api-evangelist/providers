---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: REST API for Blackboard Learn, the flagship LMS. Covers users, courses, content, grades, assignments, announcements, terms, system roles, and SIS data integration. SOAP APIs are also available for leg
  name: Blackboard Learn REST API
  slug: learn-rest
- description: REST API for Anthology Ally, the accessibility and learning effectiveness service.
  name: Anthology Ally REST API
  slug: ally-rest
- description: REST API for Anthology Student, the SIS for higher education.
  name: Anthology Student REST API
  slug: student-rest
- description: Legacy SOAP web services for Blackboard Learn integrations.
  name: Blackboard Learn SOAP API (Legacy)
  slug: learn-soap
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/blackboard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blackboard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blackboard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackboard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blackboardlearn
- group: company
  title: ''
  type: Website
  url: https://www.anthology.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.blackboard.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/blackboard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blackboard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blackboard-finops.yml
created: '2026-05-08'
description: Blackboard (now part of Anthology) provides Blackboard Learn LMS plus the Anthology product suite (Ally, Student). The Anthology Developer portal exposes REST APIs for Learn, Ally, and Student, with versions across the 3200, 3900, and 4000 series and ongoing backward compatibility.
finops:
- name: Blackboard Finops
  service_category: Education & Training
  slug: blackboard-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Blackboard (Anthology) Learn LMS REST API. Blackboard Learn exposes its capabilities through a REST API at https://developer.blackboard.com/
  name: Blackboard GraphQL Schema
  slug: blackboard-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blackboard.png
layout: provider
modified: '2026-05-08'
name: Blackboard
nav: Providers
network: true
overview: Blackboard publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EdTech, LMS, and Learning Management.
plans:
- name: Blackboard Plans Pricing
  plan_count: 1
  slug: blackboard-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Blackboard Rate Limits
  slug: blackboard-rate-limits
score:
  band: emerging
  composite: 22.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 43.3
    developer_ergonomics: 0.0
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blackboard/refs/heads/main/screenshots/blackboard-2026-06-20T173333.png
security:
- kind: domain-security
  name: Blackboard Domain Security
  slug: blackboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blackboard Vulnerability Disclosure
  slug: blackboard-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Blackboard Trust Center
  slug: blackboard-trust-center
  summary_line: ISO 27001, FedRAMP
slug: blackboard
tags:
- EdTech
- LMS
- Learning Management
website: https://www.anthology.com/
---
