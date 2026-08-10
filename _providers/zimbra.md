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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: SOAP API (XML and JSON encodings) for Zimbra Collaboration — account, mail, and admin operations, POSTed to /service/soap on a Zimbra deployment. Self-hosted, so the base host is per-deployment; the r
  name: Zimbra SOAP API
  slug: zimbra-soap-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.zimbra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zimbra.com/product/zimbra-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://files.zimbra.com/docs/soap_api/
- group: company
  title: ''
  type: Blog
  url: https://blog.zimbra.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zimbra.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zimbra
- group: start
  title: ''
  type: SignUp
  url: https://www.zimbra.com/connect/forms/?form=trial-license
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zimbra.com/product/licenses-and-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://synacor.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/zimbra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zimbra-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zimbra-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zimbra-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zimbra-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zimbra-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zimbra-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zimbra-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zimbra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://wiki.zimbra.com/wiki/Security_Center
created: '2026-07-17'
description: Zimbra is an open-source email and collaboration platform serving more than 200 million users worldwide, offering email, calendar, contacts, tasks, group chat, file storage (Briefcase), and an in-browser office suite. It is deployed self-hosted (on-premises, private cloud, or regional data center) to give organizations full data sovereignty over their communications. Zimbra's programmatic surface is a SOAP API (account, mail, and admin namespaces) wrapped by a first-party GraphQL/JavaScript client (@zimbra/api-client); it also speaks the IMAP, POP3, SMTP, CalDAV, CardDAV, and Exchange ActiveSync standards. There is no public OpenAPI/REST contract. Backed by Redpoint Ventures; added to the API Evangelist network from a VC-portfolio lead and enriched from Zimbra's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zimbra.png
layout: provider
modified: '2026-07-21'
name: Zimbra
nav: Providers
network: true
overview: 'Zimbra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Collaboration, Calendar, Messaging, and Open Source.


  Zimbra''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 65
score:
  band: thin
  composite: 28.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 28.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Zimbra Authentication
  slug: zimbra-authentication
  summary_line: soap-auth-token/preauth/oauth2 · 4 schemes
- kind: domain-security
  name: Zimbra Domain Security
  slug: zimbra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zimbra Vulnerability Disclosure
  slug: zimbra-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zimbra
tags:
- Email
- Collaboration
- Calendar
- Messaging
- Open Source
- SOAP
- GraphQL
- Productivity
website: https://www.zimbra.com/
---
