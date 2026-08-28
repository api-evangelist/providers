---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Hiver REST API (v1) exposes Shared Inboxes and their conversations, users, tags and internal notes. Twelve operations across two resources let an integration list and read inboxes, enumerate and s
  name: Hiver API
  slug: hiver-api
artifact_total: 8
asyncapis:
- description: ''
  name: Hiver Webhooks
  slug: hiver-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://hiverhq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hiverhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hiverhq.com/hiver-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hiverhq.com/api-runner/hiverhq/hiver-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.hiverhq.com/hiver-api/hiver-api
- group: operate
  title: ''
  type: Support
  url: https://help.hiverhq.com/
- group: company
  title: ''
  type: Blog
  url: https://hiverhq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GrexIt
- group: operate
  title: ''
  type: Roadmap
  url: https://updates.hiverhq.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.hiverhq.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hiverhq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hiverhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hiverhq.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hiverhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hiverhq.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://hiverhq.com/disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.hiverhq.com/
- group: auth
  title: ''
  type: Compliance
  url: https://hiverhq.com/security-center
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hiver-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hiver-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hiver-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hiver-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hiver-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hiver-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hiver-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hiver-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hiver-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hiver-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hiver-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: 'Hiver (Hiver Inc., originally GrexIt) builds an AI-powered customer service platform for teams that run support out of shared email addresses. It ships in two forms: Hiver in Gmail, a Chrome-extension helpdesk that turns shared inboxes like support@ and billing@ into assignable, SLA-tracked queues without leaving Gmail; and Hiver Omni, a standalone omnichannel platform covering email, live chat, Slack, voice, WhatsApp, a help center and a customer portal. Hiver publishes a public REST API for Shared Inboxes, conversations, users, tags and internal notes, documented on a Theneo developer portal with a downloadable OpenAPI 3.0.2 contract, and gates API access to its Pro plan and above.'
image: https://hiverhq.com/wp-content/uploads/2025/05/hiver-dark-logo@2x.png
layout: provider
modified: '2026-08-22'
name: Hiver
nav: Providers
network: true
overview: 'Hiver publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, Help Desk, Shared Inbox, and Email.


  The Hiver catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hiver''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 23 more developer resources.'
plans:
- name: Hiver Plans Pricing
  plan_count: 0
  slug: hiver-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Hiver Rate Limits
  slug: hiver-rate-limits
score:
  band: strong
  composite: 56.5
  delta: 2.3
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 30.3
    contract_quality: 56.5
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 65.8
  previous_composite: 54.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Hiver Authentication
  slug: hiver-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hiver Domain Security
  slug: hiver-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hiver Vulnerability Disclosure
  slug: hiver-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Hiver Trust Center
  slug: hiver-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type II, HIPAA
slug: hiver
tags:
- Company
- Customer Service
- Help Desk
- Shared Inbox
- Email
- Ticketing
- Customer Support
- Collaboration
- Gmail
- Google Workspace
- Omnichannel
- Live Chat
- SaaS
- Artificial Intelligence
website: https://hiverhq.com/
---
