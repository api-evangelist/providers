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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Tines Agentic Access
  operation_count: 31
  slug: tines-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 7
apis:
- description: Manage individual actions within stories
  name: Tines Actions API
  slug: tines-actions-api
- description: Retrieve audit log entries for tenant activity
  name: Tines Audit Logs API
  slug: tines-audit-logs-api
- description: Manage stored credentials for integrations
  name: Tines Credentials API
  slug: tines-credentials-api
- description: Organize stories, credentials, and resources into folders
  name: Tines Folders API
  slug: tines-folders-api
- description: Manage stories (automated workflows)
  name: Tines Stories API
  slug: tines-stories-api
- description: Manage tags for organizing resources
  name: Tines Tags API
  slug: tines-tags-api
- description: Manage teams and team membership
  name: Tines Teams API
  slug: tines-teams-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tines-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tines-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tines-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tines-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tines-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tines.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tines.com/api/welcome/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tines
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tines-io
- group: company
  title: ''
  type: Blog
  url: https://www.tines.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tines.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tines.com/
- group: other
  title: ''
  type: X
  url: https://x.com/tines_hq
- group: commercial
  title: ''
  type: Plans
  url: plans/tines-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tines-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tines-finops.yml
created: '2026-06-13'
description: Tines is a no-code intelligent workflow automation platform built for security teams. Its REST API provides programmatic access to manage stories (workflows), actions, agents, credentials, teams, cases, records, folders, dashboards, audit logs, and AI usage. Tenants can also trigger automated workflows via webhooks and integrate with the Tines platform through SCIM for identity provisioning.
examples:
- key_count: 21
  name: Tines Action Example
  slug: tines-action-example
- key_count: 22
  name: Tines Credential Example
  slug: tines-credential-example
- key_count: 17
  name: Tines Story Example
  slug: tines-story-example
finops:
- name: Tines Finops
  service_category: ''
  slug: tines-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tines.png
json_schemas:
- name: Tines Action
  property_count: 21
  slug: tines-action
- name: Tines Credential
  property_count: 20
  slug: tines-credential
- name: Tines Story
  property_count: 17
  slug: tines-story
jsonld:
- class_count: 13
  name: Tines Context
  property_count: 54
  slug: tines-context
layout: provider
modified: '2026-06-13'
name: Tines
nav: Providers
network: true
overview: 'Tines publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Audit Logs API, Credentials API, and 4 more. Tagged areas include Security Automation, No-Code, Workflow Automation, Security Operations, and SOAR.


  The Tines catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tines'' developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Tines Plans Pricing
  plan_count: 3
  slug: tines-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 0
  name: Tines Rate Limits
  slug: tines-rate-limits
rules:
- name: Tines API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tines-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tines/refs/heads/main/screenshots/tines-2026-06-20T195413.png
security:
- kind: authentication
  name: Tines Authentication
  slug: tines-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tines Domain Security
  slug: tines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tines Vulnerability Disclosure
  slug: tines-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tines Trust Center
  slug: tines-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: tines
tags:
- Security Automation
- No-Code
- Workflow Automation
- Security Operations
- SOAR
- Incident Response
- REST API
- Webhooks
website: https://www.tines.com/
---
