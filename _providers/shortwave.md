---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/shortwave-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shortwave-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shortwave-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.shortwave.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/shortwave-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shortwave-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shortwave-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.shortwave.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.shortwave.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.shortwave.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://www.shortwave.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shortwave.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.shortwave.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shortwave.com/policies/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shortwave.com/policies/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shortwave
- group: operate
  title: ''
  type: Support
  url: mailto:support@shortwave.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.shortwave.com/docs/guides/security/
created: '2026-07-17'
description: Shortwave is an AI-native email client that upgrades an existing Gmail or Google Workspace account with a reimagined inbox, built by former members of Google's Inbox team and backed by Lightspeed Venture Partners. Its AI assistant drafts and triages email, its AI-powered search answers natural-language questions across your mailbox, and it connects to external tools as a Model Context Protocol (MCP) client — Shortwave consumes MCP tool calls rather than publishing a public developer REST API. Data is hosted on Google Cloud with AES-256 encryption at rest and TLS 1.2+ in transit, and the product undergoes annual CASA Tier 2 security audits, with SOC 2 Type II and GDPR compliance available on request.
image: https://www.shortwave.com/og-image.png
layout: provider
modified: '2026-07-21'
name: Shortwave
nav: Providers
network: true
overview: 'Shortwave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Email Client, Artificial Intelligence, and AI Assistant.


  Shortwave''s developer surface includes documentation, engineering blog, pricing, signup flow, support, and 13 more developer resources.'
random_paper: 45
score:
  band: emerging
  composite: 26.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 61.1
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 26.5
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Shortwave Domain Security
  slug: shortwave-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Shortwave Vulnerability Disclosure
  slug: shortwave-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Shortwave Trust Center
  slug: shortwave-trust-center
  summary_line: SOC 2, GDPR
slug: shortwave
tags:
- Company
- Email
- Email Client
- Artificial Intelligence
- AI Assistant
- Productivity
- Model Context Protocol
- Gmail
- Google Workspace
- Collaboration
website: https://www.shortwave.com
---
