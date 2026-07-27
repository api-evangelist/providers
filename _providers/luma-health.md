---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 160
  human_in_the_loop: 0
  name: Luma Health Agentic Access
  operation_count: 276
  slug: luma-health-agentic-access
  summary_line: 276 operations · 160 acting
api_count: 12
apis:
- description: Self-service scheduling, appointment lifecycle, appointment types, provider availabilities, schedulers, offers, recalls, and waitlist management.
  name: Luma Health Scheduling & Appointments API
  slug: luma-health-scheduling-api
- description: Patient demographics and records, patient forms and form templates, and patient stored credit cards.
  name: Luma Health Patients API
  slug: luma-health-patients-api
- description: Providers, provider scheduling groups, facilities, specialties, groups, and platform users.
  name: Luma Health Providers & Facilities API
  slug: luma-health-providers-facilities-api
- description: Two-way patient messaging, engagements and engagement events/settings, appointment reminders, and patient message templates.
  name: Luma Health Messaging & Engagement API
  slug: luma-health-messaging-api
- description: Broadcast events, broadcast flows and templates, and outreach campaigns for population-level patient messaging.
  name: Luma Health Broadcast & Campaigns API
  slug: luma-health-broadcast-api
- description: Digital intake via checklists and checklist templates, patient forms and form templates, and file uploads.
  name: Luma Health Intake & Forms API
  slug: luma-health-intake-forms-api
- description: Billing charges and copays, cost estimates, and patient credit-card payment instruments.
  name: Luma Health Billing & Payments API
  slug: luma-health-billing-payments-api
- description: Insurance records with real-time eligibility verification and the insurance payors directory.
  name: Luma Health Eligibility & Insurance API
  slug: luma-health-eligibility-insurance-api
- description: Inbound and outbound referral management across the care network.
  name: Luma Health Referrals API
  slug: luma-health-referrals-api
- description: Conversational AI assistant surfaces - assistant instances and actions, lumabot flows and templates, knowledge-base question/answers, chat activities, and queue-manager routing.
  name: Luma Health Conversational AI Assistant API
  slug: luma-health-assistant-api
- description: Operational reports plus system and chat audit trails.
  name: Luma Health Reporting & Audits API
  slug: luma-health-reporting-api
- description: OAuth2 client-credentials authentication - generate and rotate client id/secret and exchange them for JWT access tokens (including subaccount tokens).
  name: Luma Health Authentication API
  slug: luma-health-authentication-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/luma-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luma-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/luma-health-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/luma-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lumahealth.io/security-and-trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/luma-health-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/luma-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/luma-health-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/luma-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/luma-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/luma-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/luma-health-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/luma-health-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.lumahealth.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.lumahealth.io
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.lumahealth.io
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.lumahealth.io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/luma-health-openapi.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.lumahealth.io/blog
- group: learn
  title: ''
  type: Learn
  url: https://www.lumahealth.io/learn
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lumahealth.io
- group: auth
  title: ''
  type: Security
  url: https://www.lumahealth.io/security
- group: start
  title: ''
  type: Login
  url: https://next.lumahealth.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumahealth.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumahealth.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumahealthhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/luma-health
created: '2026-07-24'
description: Luma Health is a United States patient-engagement (Patient Success) platform for healthcare provider organizations, headquartered in San Francisco, California. Its operational AI platform automates the patient journey - self-service scheduling and appointment management, referral and waitlist management, intake and digital forms, omnichannel two-way messaging and broadcast, appointment reminders and recalls, insurance eligibility verification, payments and billing, and a conversational AI assistant (Navigator / lumabot) - and integrates bidirectionally with the major EHRs (Epic, Oracle Health/Cerner, MEDITECH, eClinicalWorks, athenahealth, NextGen, Greenway, Nextech). Luma exposes a documented public REST API (Rest-Service v2.0.0, OpenAPI 3.0.0) at https://api.lumahealth.io/api/v2, secured with OAuth2 client-credentials that issue JWT bearer tokens. The developer-facing surface is a REST API rather than an HL7 FHIR server; FHIR/HL7 interoperability with EHRs happens inside Luma's
  integration layer, not as a public FHIR endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: luma-health-mcp.yml
  slug: luma-health-mcpyml
modified: '2026-07-24'
name: Luma Health
nav: Providers
network: true
overview: 'Luma Health publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Scheduling & Appointments API, Patients API, Providers & Facilities API, and 9 more. Tagged areas include Healthcare, United States, Patient Engagement, Scheduling, and Referrals.


  Luma Health''s developer surface includes authentication, documentation, API reference, engineering blog, and 24 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 26.5
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luma-health/refs/heads/main/screenshots/luma-health-2026-07-25T225704.png
security:
- kind: authentication
  name: Luma Health Authentication
  slug: luma-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Luma Health Domain Security
  slug: luma-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Luma Health Trust Center
  slug: luma-health-trust-center
  summary_line: HITRUST CSF r2, SOC 2 Type II, ISO/IEC 27001:2022, HIPAA, TX-RAMP Level 2
slug: luma-health
tags:
- Healthcare
- United States
- Patient Engagement
- Scheduling
- Referrals
- Intake
- Messaging
- Eligibility
- EHR
- Interoperability
- Clinical AI
website: https://www.lumahealth.io
---
