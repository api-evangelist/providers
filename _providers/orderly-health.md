---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Orderly Health Agentic Access
  operation_count: 1
  slug: orderly-health-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Look Up Practitioners API from Orderly Health — 1 operation(s) for look up practitioners.
  name: Orderly Health Look Up Practitioners API
  slug: orderly-health-look-up-practitioners-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orderly-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orderly-health-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orderly-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orderly-health-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orderly-health-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orderly-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orderly-health-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orderly-health-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orderly-health-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orderly-health-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orderlyapi.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://orderlyapi.readme.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://orderlyapi.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://orderlyapi.readme.io/docs/setting-up-to-use-the-orderly-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://orderlyapi.readme.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://orderlyhealth.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orderlyhealth
- group: start
  title: ''
  type: SignUp
  url: https://app.orderlyhealth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orderlyhealth.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orderlyhealth.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://orderlyhealth.com
created: '2026-07-17'
description: Orderly Health is a Denver, Colorado healthcare data company that keeps provider directories accurate and usable. Founded in 2015, its API-first platform uses machine learning and AI to automatically identify and repair inaccuracies in healthcare provider data for providers, payers, and health-technology companies. Its products include the Orderly Provider Directory (6.4M+ practitioner profiles), a Roster Automation Suite that normalizes and validates rosters in seconds, and Data Updates that deliver traceable, field-level corrections. The public Orderly Provider Directory API lets developers search practitioners by NPI, name, location, specialty, care category, accepted insurance, and DEA number, returning per-field confidence scores and source attribution. Orderly Health was acquired by First Choice Health.
image: https://files.readme.io/e494480-small-Orderly_Logo_4cMrk_NavyText.png
layout: provider
mcp_servers:
- description: ''
  name: orderly-health-mcp.yml
  slug: orderly-health-mcpyml
modified: '2026-07-20'
name: Orderly Health
nav: Providers
network: true
overview: 'Orderly Health publishes 1 API on the [APIs.io](https://apis.io/) network: Look Up Practitioners API. Tagged areas include Company, Healthcare, Provider Data, Provider Directory, and Health Data.


  Orderly Health''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 43.4
  delta: -5.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.8
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Orderly Health Authentication
  slug: orderly-health-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Orderly Health Domain Security
  slug: orderly-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: orderly-health
tags:
- Company
- Healthcare
- Provider Data
- Provider Directory
- Health Data
- Machine Learning
- Data Quality
- Interoperability
website: https://orderlyhealth.com
---
