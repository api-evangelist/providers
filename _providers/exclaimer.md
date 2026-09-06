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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-05'
api_count: 10
apis:
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The End Users API from Exclaimer — 1 operation(s) for end users.
  name: Exclaimer End Users API
  slug: exclaimer-end-users-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Mailboxes API from Exclaimer — 1 operation(s) for mailboxes.
  name: Exclaimer Mailboxes API
  slug: exclaimer-mailboxes-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Miscellaneous API from Exclaimer — 2 operation(s) for miscellaneous.
  name: Exclaimer Miscellaneous API
  slug: exclaimer-miscellaneous-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The MSP API from Exclaimer — 4 operation(s) for msp.
  name: Exclaimer MSP API
  slug: exclaimer-msp-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Reference Resources API from Exclaimer — 3 operation(s) for reference resources.
  name: Exclaimer Reference Resources API
  slug: exclaimer-reference-resources-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Resellers API from Exclaimer — 1 operation(s) for resellers.
  name: Exclaimer Resellers API
  slug: exclaimer-resellers-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Subscription Transfers API from Exclaimer — 3 operation(s) for subscription transfers.
  name: Exclaimer Subscription Transfers API
  slug: exclaimer-subscription-transfers-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Subscription Users API from Exclaimer — 4 operation(s) for subscription users.
  name: Exclaimer Subscription Users API
  slug: exclaimer-subscription-users-api
- baseURL: https://cloudapi.exclaimer.com/exclaimerapi
  baseurl_source: declared
  description: The Subscriptions API from Exclaimer — 13 operation(s) for subscriptions.
  name: Exclaimer Subscriptions API
  slug: exclaimer-subscriptions-api
artifact_total: 24
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
- group: other
  title: ''
  type: Overlay
  url: overlays/exclaimer-cloud-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
overview: 'Exclaimer publishes 9 APIs on the [APIs.io](https://apis.io/) network, including End Users API, Mailboxes API, Miscellaneous API, and 6 more. Tagged areas include Company, Email, Email Signatures, Email Signature Management, and Microsoft-365.


  Exclaimer''s developer surface includes pricing, engineering blog, signup flow, documentation, API reference, getting-started guide, support, and 21 more developer resources.'
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
  composite: 60.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 60.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Microsoft-365
- Google Workspace
- Marketing
- Productivity
- Software-as-a-Service
- Security
website: https://exclaimer.com/
---
