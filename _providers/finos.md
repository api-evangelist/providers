---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 94
  human_in_the_loop: 3
  name: Finos Agentic Access
  operation_count: 172
  slug: finos-agentic-access
  summary_line: 172 operations · 94 acting · 3 human-in-the-loop
api_count: 34
apis:
- description: FDC3 is an open standard for financial desktop interoperability, defining how applications launch, share context, and resolve intents across the financial desktop. The standard includes a Desktop Agen
  name: FDC3
  slug: fdc3
- description: The Common Domain Model (CDM) is a standardized, machine-readable, and machine-executable model that represents financial products, trades in those products, and the lifecycle events of those trades.
  name: Common Domain Model
  slug: common-domain-model
- description: FINOS Common Cloud Controls is an open standard project that describes consistent controls for compliant public cloud deployments in the financial services sector.
  name: Common Cloud Controls
  slug: common-cloud-controls
- description: Morphir is a universal language for business and technology that captures business logic in a portable, technology-agnostic intermediate representation that can be compiled to multiple target language
  name: Morphir
  slug: morphir
- description: The Admin API from FINOS — 3 operation(s) for admin.
  name: FINOS Admin API
  slug: finos-admin-api
- description: The AppEntitlement API from FINOS — 2 operation(s) for appentitlement.
  name: FINOS AppEntitlement API
  slug: finos-appentitlement-api
- description: The Application API from FINOS — 4 operation(s) for application.
  name: FINOS Application API
  slug: finos-application-api
- description: The Attachments API from FINOS — 1 operation(s) for attachments.
  name: FINOS Attachments API
  slug: finos-attachments-api
- description: The AuditTrail API from FINOS — 1 operation(s) for audittrail.
  name: FINOS AuditTrail API
  slug: finos-audittrail-api
- description: The CertificateAuthentication API from FINOS — 2 operation(s) for certificateauthentication.
  name: FINOS CertificateAuthentication API
  slug: finos-certificateauthentication-api
- description: The CertificatePod API from FINOS — 1 operation(s) for certificatepod.
  name: FINOS CertificatePod API
  slug: finos-certificatepod-api
- description: The Connection API from FINOS — 6 operation(s) for connection.
  name: FINOS Connection API
  slug: finos-connection-api
- description: The Datafeed API from FINOS — 3 operation(s) for datafeed.
  name: FINOS Datafeed API
  slug: finos-datafeed-api
- description: The Datahose API from FINOS — 1 operation(s) for datahose.
  name: FINOS Datahose API
  slug: finos-datahose-api
- description: The Disclaimer API from FINOS — 3 operation(s) for disclaimer.
  name: FINOS Disclaimer API
  slug: finos-disclaimer-api
- description: The DLP Policies and Dictionary Management API from FINOS — 14 operation(s) for dlp policies and dictionary management.
  name: FINOS DLP Policies and Dictionary Management API
  slug: finos-dlp-policies-and-dictionary-management-api
- description: The File Ext API from FINOS — 2 operation(s) for file ext.
  name: FINOS File Ext API
  slug: finos-file-ext-api
- description: The InfoBarriers API from FINOS — 5 operation(s) for infobarriers.
  name: FINOS InfoBarriers API
  slug: finos-infobarriers-api
- description: The Message API from FINOS — 1 operation(s) for message.
  name: FINOS Message API
  slug: finos-message-api
- description: The Messages API from FINOS — 7 operation(s) for messages.
  name: FINOS Messages API
  slug: finos-messages-api
- description: The MessageSuppression API from FINOS — 1 operation(s) for messagesuppression.
  name: FINOS MessageSuppression API
  slug: finos-messagesuppression-api
- description: The Pod API from FINOS — 3 operation(s) for pod.
  name: FINOS Pod API
  slug: finos-pod-api
- description: The Presence API from FINOS — 8 operation(s) for presence.
  name: FINOS Presence API
  slug: finos-presence-api
- description: The Room Membership API from FINOS — 8 operation(s) for room membership.
  name: FINOS Room Membership API
  slug: finos-room-membership-api
- description: The Security API from FINOS — 8 operation(s) for security.
  name: FINOS Security API
  slug: finos-security-api
- description: The Session API from FINOS — 1 operation(s) for session.
  name: FINOS Session API
  slug: finos-session-api
- description: The Share API from FINOS — 1 operation(s) for share.
  name: FINOS Share API
  slug: finos-share-api
- description: The Signals API from FINOS — 9 operation(s) for signals.
  name: FINOS Signals API
  slug: finos-signals-api
- description: The Streams API from FINOS — 16 operation(s) for streams.
  name: FINOS Streams API
  slug: finos-streams-api
- description: The System API from FINOS — 7 operation(s) for system.
  name: FINOS System API
  slug: finos-system-api
- description: The User API from FINOS — 24 operation(s) for user.
  name: FINOS User API
  slug: finos-user-api
- description: The Users API from FINOS — 6 operation(s) for users.
  name: FINOS Users API
  slug: finos-users-api
- description: The Util API from FINOS — 1 operation(s) for util.
  name: FINOS Util API
  slug: finos-util-api
- description: The Violations API from FINOS — 7 operation(s) for violations.
  name: FINOS Violations API
  slug: finos-violations-api
artifact_total: 42
collections:
- collection_type: open
  name: Agent API
  slug: open-finos-symphony-agent-api
- collection_type: open
  name: Authenticator API
  slug: open-finos-symphony-authenticator-api
- collection_type: open
  name: Pod API
  slug: open-finos-symphony-pod-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finos-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finosfoundation
- group: company
  title: ''
  type: Website
  url: https://www.finos.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.finos.org/about
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/finos
- group: other
  title: ''
  type: Landscape
  url: https://landscape.finos.org/
- group: operate
  title: ''
  type: Community
  url: https://www.finos.org/community
- group: company
  title: ''
  type: Blog
  url: https://www.finos.org/blog/rss.xml
created: '2026-03-16'
description: The Fintech Open Source Foundation (FINOS) is a Linux Foundation project dedicated to open source innovation in the financial services industry. It fosters collaboration between banks, fintech companies, and technology firms on standards and projects spanning desktop interoperability (FDC3), financial product modeling (Common Domain Model), cloud compliance (Common Cloud Controls), business and technology modeling (Morphir), and messaging APIs (Symphony API Spec), among others.
finops:
- name: Finos Finops
  service_category: Open Source Foundation / Standards Body
  slug: finos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finos.png
layout: provider
modified: '2026-05-19'
name: FINOS
nav: Providers
network: true
overview: 'FINOS publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Admin API, AppEntitlement API, Application API, and 27 more. Tagged areas include Financial Services, Fintech, Linux Foundation, and Open Source.


  FINOS''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Finos Plans Pricing
  plan_count: 5
  slug: finos-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Finos Rate Limits
  slug: finos-rate-limits
score:
  band: thin
  composite: 32.7
  delta: -1.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.6
    developer_ergonomics: 15.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finos/refs/heads/main/screenshots/finos-2026-06-20T181222.png
security:
- kind: domain-security
  name: Finos Domain Security
  slug: finos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finos
tags:
- Financial Services
- Fintech
- Linux Foundation
- Open Source
website: https://www.finos.org/
---
