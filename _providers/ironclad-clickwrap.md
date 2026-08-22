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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ironclad Clickwrap Agentic Access
  operation_count: 12
  slug: ironclad-clickwrap-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 5
apis:
- description: Send acceptance, rejection, and view events.
  name: Ironclad Clickwrap Activity API
  slug: ironclad-clickwrap-activity-api
- description: Manage individual contract documents.
  name: Ironclad Clickwrap Contracts API
  slug: ironclad-clickwrap-contracts-api
- description: Manage clickwrap groups (containers of contracts).
  name: Ironclad Clickwrap Groups API
  slug: ironclad-clickwrap-groups-api
- description: Manage end users who accept agreements.
  name: Ironclad Clickwrap Signers API
  slug: ironclad-clickwrap-signers-api
- description: Manage sites that host clickwrap groups.
  name: Ironclad Clickwrap Sites API
  slug: ironclad-clickwrap-sites-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ironclad Clickwrap Activity API
  slug: open-ironclad-clickwrap-activity-api
- collection_type: open
  name: Ironclad Clickwrap Activity Contracts API
  slug: open-ironclad-clickwrap-contracts-api
- collection_type: open
  name: Ironclad Clickwrap Activity Groups API
  slug: open-ironclad-clickwrap-groups-api
- collection_type: open
  name: Ironclad Clickwrap Activity Signers API
  slug: open-ironclad-clickwrap-signers-api
- collection_type: open
  name: Ironclad Clickwrap Activity Sites API
  slug: open-ironclad-clickwrap-sites-api
- collection_type: open
  name: Ironclad Clickwrap API
  slug: open-ironclad-clickwrap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ironclad-clickwrap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ironclad-clickwrap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ironclad-clickwrap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ironclad-clickwrap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pactsafe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ironclad-inc-
- group: start
  title: ''
  type: Portal
  url: https://clickwrap-developer.ironcladapp.com/
- group: company
  title: ''
  type: Website
  url: https://ironcladapp.com/
- group: operate
  title: ''
  type: Support
  url: https://ironcladapp.com/support/
- group: agent
  title: ''
  type: LlmsText
  url: https://clickwrap-developer.ironcladapp.com/llms.txt
created: '2025-02-17'
description: Ironclad Clickwrap is a developer-friendly platform for implementing clickwrap agreements, terms of service, and contract acceptance workflows. The Ironclad Clickwrap API enables developers to programmatically manage clickwrap agreements, record user acceptance, and generate audit trails.
finops:
- name: Ironclad Clickwrap Finops
  service_category: API
  slug: ironclad-clickwrap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ironclad-clickwrap.png
layout: provider
modified: '2026-05-19'
name: Ironclad Clickwrap
nav: Providers
network: true
overview: 'Ironclad Clickwrap publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Contracts API, Groups API, and 2 more. Tagged areas include Agreements, Compliance, Contracts, and Legal.


  The Ironclad Clickwrap catalog on APIs.io includes 1 Spectral governance ruleset.


  Ironclad Clickwrap''s developer surface includes authentication, developer portal, support, and 7 more developer resources.'
plans:
- name: Ironclad Clickwrap Plans Pricing
  plan_count: 3
  slug: ironclad-clickwrap-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Ironclad Clickwrap Rate Limits
  slug: ironclad-clickwrap-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Ironclad Clickwrap API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ironclad-clickwrap-rules
score:
  band: thin
  composite: 30.2
  delta: -2.9
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 21.4
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ironclad-clickwrap/refs/heads/main/screenshots/ironclad-clickwrap-2026-06-20T183613.png
security:
- kind: authentication
  name: Ironclad Clickwrap Authentication
  slug: ironclad-clickwrap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ironclad Clickwrap Domain Security
  slug: ironclad-clickwrap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ironclad Clickwrap Trust Center
  slug: ironclad-clickwrap-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: ironclad-clickwrap
tags:
- Agreements
- Compliance
- Contracts
- Legal
website: https://ironcladapp.com/
---
