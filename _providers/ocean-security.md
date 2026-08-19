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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ocean Security Agentic Access
  operation_count: 20
  slug: ocean-security-agentic-access
  summary_line: 20 operations · 3 acting
api_count: 4
apis:
- description: Security metrics and analytics endpoints
  name: Ocean Security Metrics API
  slug: ocean-security-metrics-api
- description: Manage tenant allow/deny list entries
  name: Ocean Security Settings API
  slug: ocean-security-settings-api
- description: Phishing report (SONAR) management and response analytics
  name: Ocean Security Sonar API
  slug: ocean-security-sonar-api
- description: Operations for retrieving threat information
  name: Ocean Security Threats API
  slug: ocean-security-threats-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ocean Security Metrics API
  slug: open-ocean-security-metrics-api
- collection_type: open
  name: Ocean Security Metrics Settings API
  slug: open-ocean-security-settings-api
- collection_type: open
  name: Ocean Security Metrics Sonar API
  slug: open-ocean-security-sonar-api
- collection_type: open
  name: Ocean Security Metrics Threats API
  slug: open-ocean-security-threats-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ocean-security-investigate-phishing-reports.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ocean-security-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocean-security-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ocean-security-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ocean.security/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ocean.security/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ocean.security/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ocean.security/documentation/getting-started
- group: company
  title: ''
  type: Website
  url: https://ocean.security
- group: company
  title: ''
  type: Blog
  url: https://ocean.security/resources/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ocean.security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ocean.security/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ocean.security/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://ocean.security/demo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocean-security-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocean-security-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocean-security-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ocean-security-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ocean-security-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ocean-security-well-known.yml
created: '2026-07-17'
description: Ocean Security (Ocean) is an AI-native, agentic email security platform that stops targeted, AI-powered email attacks that surface-level detection tools miss. At its core is Ray, an autonomous investigation engine that reviews every inbound email in real time — checking the sender, content, links, technical infrastructure, and business context to decide whether a message can be trusted — enabling enterprises to stop phishing, business email compromise (BEC), impersonation, and financial fraud. The platform pairs deep email investigation with autonomous SOC triage and real-time employee inbox guidance. Ocean's REST API gives security teams programmatic access to detected threats, phishing reports (SONAR), allow/deny list settings, and ROI/security metrics such as hours saved and financial loss prevented. Founded in Israel and backed by Lightspeed Venture Partners, Ocean protects hundreds of thousands of mailboxes across Global Fortune 500 organizations.
image: https://ocean.security/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ocean-security-mcp.yml
  slug: ocean-security-mcpyml
modified: '2026-07-20'
name: Ocean Security
nav: Providers
network: true
overview: 'Ocean Security publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Metrics API, Settings API, Sonar API, and 1 more. Tagged areas include Company, Security, Email Security, Cybersecurity, and Phishing.


  Ocean Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 14 more developer resources.'
random_paper: 110
score:
  band: developing
  composite: 40.5
  delta: -2.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 60.1
    developer_ergonomics: 42.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocean-security/refs/heads/main/screenshots/ocean-security-2026-08-07T185923.png
security:
- kind: authentication
  name: Ocean Security Authentication
  slug: ocean-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ocean Security Domain Security
  slug: ocean-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ocean-security
tags:
- Company
- Security
- Email Security
- Cybersecurity
- Phishing
- Threat Detection
- Email
- Anti-Phishing
- Artificial Intelligence
- Threat Intelligence
website: https://ocean.security
---
