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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Admin/management REST API for MultiLine, used to connect external applications to a Movius organization. Supports provisioning and managing API users, assigning and reassigning business numbers, confi
  name: MultiLine Management REST API
  slug: multiline-management-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/movius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/movius-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/movius-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/movius-lifecycle.yml
- group: company
  title: ''
  type: Website
  url: https://movius.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.moviuscorp.com/help
- group: docs
  title: ''
  type: Documentation
  url: https://help.moviuscorp.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://help.moviuscorp.com/help/add-api-user
- group: start
  title: ''
  type: GettingStarted
  url: https://help.moviuscorp.com/help/installation
- group: operate
  title: ''
  type: Support
  url: https://help.moviuscorp.com/help
- group: company
  title: ''
  type: Blog
  url: https://movius.ai/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moviuscorp.net/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.moviuscorp.com/help/product-docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://movius.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://movius.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://movius.ai/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://movius.ai/security-compliance/
created: '2026-07-17'
description: Movius is a secure enterprise mobile communications company whose flagship product, MultiLine, gives employees a separate, compliant business identity (voice, SMS, MMS, and social messaging across WhatsApp, WeChat, Line, and Microsoft Teams) on their personal phones. Marketed as SCaaS (Secure Communication as a Service), the platform is built for regulated industries such as financial services, healthcare, and government, capturing and archiving all communications for FINRA, SEC, MiFID II, FCA COBS, HIPAA, and GDPR compliance. Movius exposes an admin/management REST API through its Management Portal that lets external applications provision and manage API users, assign and reassign numbers, configure compliance policies, and pull reports and communication records into cloud archival systems, alongside packaged integrations for Salesforce and Microsoft Teams.
image: https://movius.ai/wp-content/uploads/2021/09/movius-logo.png
layout: provider
modified: '2026-07-20'
name: Movius
nav: Providers
network: true
overview: 'Movius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Messaging, Mobile, and Telecom.


  Movius'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 10 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 32.9
  delta: 1.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 79.6
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 31.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Movius Authentication
  slug: movius-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Movius Domain Security
  slug: movius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Movius Trust Center
  slug: movius-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 9001, HIPAA, HITECH, FedRAMP, GovRAMP, FISMA, PCI DSS, GDPR, FIPS 140-2 Level 3
slug: movius
tags:
- Company
- Communications
- Messaging
- Mobile
- Telecom
- Compliance
- Security
- Voice
- SMS
- Enterprise
website: https://movius.ai/
---
