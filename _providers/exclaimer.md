---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Partner and distributor provisioning API for Exclaimer Cloud tenants. Covers creating and managing subscriptions (add, update, activate, deactivate, end, reactivate, migrate, transfer ownership, chang
  name: Exclaimer Cloud API
  slug: exclaimer-cloud-api
artifact_total: 16
collections:
- collection_type: open
  name: Exclaimer Cloud API — End Users
  slug: open-exclaimer-end-users
- collection_type: open
  name: Exclaimer Cloud API — Mailboxes
  slug: open-exclaimer-mailboxes
- collection_type: open
  name: Exclaimer Cloud API — Miscellaneous
  slug: open-exclaimer-miscellaneous
- collection_type: open
  name: Exclaimer Cloud API — MSP
  slug: open-exclaimer-msp
- collection_type: open
  name: Exclaimer Cloud API — Reference Resources
  slug: open-exclaimer-reference-resources
- collection_type: open
  name: Exclaimer Cloud API — Resellers
  slug: open-exclaimer-resellers
- collection_type: open
  name: Exclaimer Cloud API — Subscription Transfers
  slug: open-exclaimer-subscription-transfers
- collection_type: open
  name: Exclaimer Cloud API — Subscription Users
  slug: open-exclaimer-subscription-users
- collection_type: open
  name: Exclaimer Cloud API — Subscriptions
  slug: open-exclaimer-subscriptions
common:
- group: company
  title: ''
  type: Website
  url: https://exclaimer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://exclaimer.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://exclaimer.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://go.exclaimer.com/trial
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.exclaimer.com/hc/en-gb
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exclaimer.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exclaimer.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.exclaimer.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exclaimer-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://exclaimer.com/product/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/exclaimer-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.exclaimer.com/p/Welcome
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exclaimer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/exclaimer-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/exclaimer-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exclaimer-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloudapi.exclaimer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.exclaimer.com/hc/en-gb
- group: docs
  title: ''
  type: APIReference
  url: https://cloudapi.exclaimer.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.exclaimer.com/hc/en-gb/articles/360050643511-Onboarding-Connect-to-Microsoft-365
- group: operate
  title: ''
  type: Support
  url: https://support.exclaimer.com/hc/en-gb
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exclaimerltd
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/exclaimer-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://exclaimer.com/support/discontinued/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exclaimer-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/exclaimer-plans-pricing.yml
created: '2026-07-17'
description: Exclaimer is an email signature management platform used by IT, marketing, and sales teams to centrally create, deploy, and govern corporate email signatures across Microsoft 365, Microsoft Exchange, and Google Workspace. It manages signatures for more than 9 million email accounts, adding campaign banners, meeting-branding backgrounds, click-tracking analytics, directory synchronization with Azure AD and Google Directory, and role-based access control. Exclaimer publishes the Exclaimer Cloud API — a partner/distributor provisioning REST API documented at cloudapi.exclaimer.com with a machine- readable OpenAPI 3.0.1 definition covering subscriptions, MSP subscriptions, subscription users, resellers, end users, mailbox counts, subscription transfers and reference data. It operates a multi-region Exclaimer Cloud with a real-time status page and a strong security and compliance program (SOC 2 Type II, ISO 27001/27018, HIPAA, PCI DSS, CSA STAR, Cyber Essentials).
image: https://exclaimer.com/img/og-image.jpg
layout: provider
modified: '2026-08-13'
name: Exclaimer
nav: Providers
network: true
overview: 'Exclaimer publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud API. Tagged areas include Company, Email, Email Signatures, Email Signature Management, and Microsoft 365.


  Exclaimer''s developer surface includes pricing, engineering blog, signup flow, documentation, API reference, getting-started guide, support, and 19 more developer resources.'
plans:
- name: Exclaimer Plans Pricing
  plan_count: 4
  slug: exclaimer-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Exclaimer Rate Limits
  slug: exclaimer-rate-limits
score:
  band: strong
  composite: 59.0
  delta: 0.5
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 56.1
    developer_ergonomics: 45.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 52.6
  previous_composite: 58.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exclaimer/refs/heads/main/screenshots/exclaimer-2026-07-25T213850.png
security:
- kind: authentication
  name: Exclaimer Authentication
  slug: exclaimer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Exclaimer Domain Security
  slug: exclaimer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Exclaimer Vulnerability Disclosure
  slug: exclaimer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Exclaimer Trust Center
  slug: exclaimer-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27018, PCI DSS, CSA (Cloud Security Alliance), Cyber Essentials, HIPAA, GDPR, CCPA
slug: exclaimer
tags:
- Company
- Email
- Email Signatures
- Email Signature Management
- Microsoft 365
- Google Workspace
- Marketing
- Productivity
- SaaS
- Security
website: https://exclaimer.com/
---
