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
  band: human-only
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/supafax-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supafax-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supafax-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://supafax.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://supafax.com/security
- group: company
  title: ''
  type: Website
  url: https://supafax.com
- group: commercial
  title: ''
  type: Pricing
  url: https://supafax.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.supafax.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.supafax.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supafax.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supafax.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:rohan@supafax.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supafax-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/supafax-security.txt
created: '2026-07-17'
description: Supafax is an AI email assistant and autonomous inbox agent from Veriad, Inc. (Y Combinator Winter 2026) that lives inside Gmail and Outlook to proactively manage email and calendar. It drafts context-aware replies in your writing style, auto-labels and prioritizes messages, schedules and books meetings through back-and-forth coordination, answers inbox queries, and runs custom automation rules defined in plain English. Founded in 2025 in San Francisco by Rohan Mahendraker and Anton Muratov, Supafax sells a Professional plan and an Enterprise tier with SSO/SCIM, custom integrations, and dedicated support. It is a consumer/B2B productivity product with no public developer API at this time; its security posture (security.txt, CASA Tier 2, ICO registration, GDPR) is its most developer-relevant public surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supafax.png
layout: provider
modified: '2026-07-21'
name: Supafax
nav: Providers
network: true
overview: 'Supafax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Calendar, AI Assistant, and AI Agent.


  Supafax''s developer surface includes pricing, signup flow, support, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.1
  delta: -1.2
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Supafax Domain Security
  slug: supafax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Supafax Vulnerability Disclosure
  slug: supafax-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Supafax Trust Center
  slug: supafax-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: supafax
tags:
- Company
- Email
- Calendar
- AI Assistant
- AI Agent
- Email Automation
- Productivity
- Y Combinator
website: https://supafax.com
---
