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
- acting_count: 6
  human_in_the_loop: 0
  name: Liferay Agentic Access
  operation_count: 8
  slug: liferay-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- description: Manage roles and role associations
  name: Liferay Roles API
  slug: liferay-roles-api
artifact_total: 9
collections:
- collection_type: open
  name: Liferay Roles API
  slug: open-liferay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liferay-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liferay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liferay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liferay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liferay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liferay-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.liferay.com/blog
created: '2025-01-08'
description: Liferay DXP is an open-source digital experience platform offering headless REST APIs for managing users, roles, permissions, content, and site configuration. The Roles API lets you list, retrieve, and associate or dissociate regular, site, and organization roles for users.
finops:
- name: Liferay Finops
  service_category: API
  slug: liferay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liferay.png
layout: provider
modified: '2026-05-19'
name: Liferay
nav: Providers
network: true
overview: 'Liferay publishes 1 API on the [APIs.io](https://apis.io/) network: Roles API. Tagged areas include Open Source, Digital Experience, DXP, Roles, and Users.


  Liferay''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Liferay Plans Pricing
  plan_count: 3
  slug: liferay-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Liferay Rate Limits
  slug: liferay-rate-limits
score:
  band: thin
  composite: 32.4
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.9
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liferay/refs/heads/main/screenshots/liferay-2026-06-20T184517.png
security:
- kind: authentication
  name: Liferay Authentication
  slug: liferay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Liferay Domain Security
  slug: liferay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Liferay Vulnerability Disclosure
  slug: liferay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: liferay
tags:
- Open Source
- Digital Experience
- DXP
- Roles
- Users
- Permissions
- Headless
---
