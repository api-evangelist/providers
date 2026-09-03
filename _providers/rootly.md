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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Rootly Agentic Access
  operation_count: 30
  slug: rootly-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 7
apis:
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Alerts API from Rootly — 4 operation(s) for alerts.
  name: Rootly Alerts API
  slug: rootly-alerts-api
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Escalation Policies API from Rootly — 1 operation(s) for escalation policies.
  name: Rootly Escalation Policies API
  slug: rootly-escalation-policies-api
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Incidents API from Rootly — 4 operation(s) for incidents.
  name: Rootly Incidents API
  slug: rootly-incidents-api
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Services API from Rootly — 2 operation(s) for services.
  name: Rootly Services API
  slug: rootly-services-api
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Teams API from Rootly — 2 operation(s) for teams.
  name: Rootly Teams API
  slug: rootly-teams-api
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Users API from Rootly — 2 operation(s) for users.
  name: Rootly Users API
  slug: rootly-users-api
- baseURL: https://api.rootly.com/v1
  baseurl_source: spec
  description: The Workflows API from Rootly — 2 operation(s) for workflows.
  name: Rootly Workflows API
  slug: rootly-workflows-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rootly Alerts API
  slug: open-rootly-alerts-api
- collection_type: open
  name: Rootly Alerts Escalation Policies API
  slug: open-rootly-escalation-policies-api
- collection_type: open
  name: Rootly Alerts Incidents API
  slug: open-rootly-incidents-api
- collection_type: open
  name: Rootly Alerts Services API
  slug: open-rootly-services-api
- collection_type: open
  name: Rootly Alerts Teams API
  slug: open-rootly-teams-api
- collection_type: open
  name: Rootly Alerts Users API
  slug: open-rootly-users-api
- collection_type: open
  name: Rootly Alerts Workflows API
  slug: open-rootly-workflows-api
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
random_paper: 9
rate_limits:
- limit_count: 5
  name: Rootly Rate Limits
  slug: rootly-rate-limits
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.7
    developer_ergonomics: 23.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
