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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Mixmax Agentic Access
  operation_count: 24
  slug: mixmax-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 6
apis:
- description: Contact groups you own or that are shared with you — deprecated
  name: Mixmax Contact Groups API
  slug: mixmax-contact-groups-api
- description: Mixmax Contacts (people you've emailed) — deprecated resource group
  name: Mixmax Contacts API
  slug: mixmax-contacts-api
- description: File requests you've sent out
  name: Mixmax File Requests API
  slug: mixmax-file-requests-api
- description: Meeting Copilot summaries and transcripts (requires mixmaxApi feature)
  name: Mixmax Meetings API
  slug: mixmax-meetings-api
- description: Sequences you have access to, and their recipients
  name: Mixmax Sequences API
  slug: mixmax-sequences-api
- description: Snippet tag management
  name: Mixmax Snippet Tags API
  slug: mixmax-snippet-tags-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mixmax-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mixmax-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mixmax-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mixmax-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mixmax.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mixmax-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/mixmax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mixmax-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mixmax.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mixmax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mixmax.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mixmax.com/reference/getting-started-with-the-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mixmax.com/reference/getting-started-with-the-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mixmaxhq
- group: operate
  title: ''
  type: Support
  url: https://success.mixmax.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mixmax.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mixmax.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mixmax.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mixmax.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mixmax.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mixmax.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.mixmax.com/
created: '2026-07-17'
description: Mixmax is an AI-native sales engagement and execution platform that lives inside Gmail and Outlook, helping sales, customer success, recruiting, and other relationship-driven teams run their entire customer journey without context-switching. It combines email tracking and templates, multi-channel sequences, one-click scheduling, CRM automation, engagement signals, and Meeting Copilot summaries and transcripts. Mixmax exposes a public REST API (api.mixmax.com/v1) for lightweight real-time access to contacts, contact groups, sequences and recipients, file requests, meeting summaries and transcripts, and snippet tags, authenticated with an API token, plus message integrations and Sidebar/Widget SDKs for extending the product surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mixmax.png
layout: provider
mcp_servers:
- description: ''
  name: mixmax-mcp.yml
  slug: mixmax-mcpyml
modified: '2026-07-20'
name: Mixmax
nav: Providers
network: true
overview: 'Mixmax publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contact Groups API, Contacts API, File Requests API, and 3 more. Tagged areas include Company, Saas, Sales Engagement, Email, and Sales.


  Mixmax''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 80
rate_limits:
- limit_count: 1
  name: Mixmax Rate Limits
  slug: mixmax-rate-limits
score:
  band: developing
  composite: 52.5
  delta: -1.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.4
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mixmax/refs/heads/main/screenshots/mixmax-2026-08-07T183824.png
security:
- kind: authentication
  name: Mixmax Authentication
  slug: mixmax-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mixmax Domain Security
  slug: mixmax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mixmax Trust Center
  slug: mixmax-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: mixmax
tags:
- Company
- Saas
- Sales Engagement
- Email
- Sales
- CRM
- Productivity
- Meetings
- Sequences
website: https://www.mixmax.com/
---
