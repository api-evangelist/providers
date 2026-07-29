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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Rootly Agentic Access
  operation_count: 30
  slug: rootly-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 7
apis:
- description: The Alerts API from Rootly — 4 operation(s) for alerts.
  name: Rootly Alerts API
  slug: rootly-alerts-api
- description: The Escalation Policies API from Rootly — 1 operation(s) for escalation policies.
  name: Rootly Escalation Policies API
  slug: rootly-escalation-policies-api
- description: The Incidents API from Rootly — 4 operation(s) for incidents.
  name: Rootly Incidents API
  slug: rootly-incidents-api
- description: The Services API from Rootly — 2 operation(s) for services.
  name: Rootly Services API
  slug: rootly-services-api
- description: The Teams API from Rootly — 2 operation(s) for teams.
  name: Rootly Teams API
  slug: rootly-teams-api
- description: The Users API from Rootly — 2 operation(s) for users.
  name: Rootly Users API
  slug: rootly-users-api
- description: The Workflows API from Rootly — 2 operation(s) for workflows.
  name: Rootly Workflows API
  slug: rootly-workflows-api
artifact_total: 17
collections:
- collection_type: open
  name: Rootly API
  slug: open-rootly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rootly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rootly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rootly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rootly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rootly-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://rootly.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rootlyhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rootlyhq
- group: company
  title: ''
  type: Website
  url: https://rootly.com
- group: docs
  title: ''
  type: Documentation
  url: https://rootly.com/docs
created: '2026-03-27'
description: Rootly is an incident management platform that automates incident response workflows and integrates with existing tools.
finops:
- name: Rootly Finops
  service_category: API
  slug: rootly-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Rootly incident management platform. Rootly provides a REST API for automating incident response workflows, managing on-call schedules, co
  name: Rootly GraphQL Schema
  slug: rootly-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rootly.png
layout: provider
modified: '2026-05-19'
name: Rootly
nav: Providers
network: true
overview: 'Rootly publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Escalation Policies API, Incidents API, and 4 more. Tagged areas include AIOps and Incident Management.


  Rootly''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Rootly Plans Pricing
  plan_count: 3
  slug: rootly-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Rootly Rate Limits
  slug: rootly-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 0.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.0
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rootly/refs/heads/main/screenshots/rootly-2026-06-20T193221.png
security:
- kind: authentication
  name: Rootly Authentication
  slug: rootly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rootly Domain Security
  slug: rootly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rootly Vulnerability Disclosure
  slug: rootly-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rootly Trust Center
  slug: rootly-trust-center
  summary_line: SOC 2, GDPR
slug: rootly
tags:
- AIOps
- Incident Management
website: https://rootly.com
---
