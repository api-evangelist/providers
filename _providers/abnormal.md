---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API for managing the security threats, cases and posture that Abnormal AI detects for an organization. Covers threats and threat actions, Abnormal cases and case analysis, message detail and atta
  name: Abnormal Security Client API
  slug: client-api
artifact_total: 6
asyncapis:
- description: ''
  name: Abnormal Webhooks
  slug: abnormal-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/abnormal-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abnormal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abnormal.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.abnormalsecurity.com/home/settings/integrations
- group: docs
  title: ''
  type: Documentation
  url: https://app.swaggerhub.com/apis-docs/abnormal-security/abx/1.4.3
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis-docs/abnormal-security/abx/1.4.3
- group: start
  title: ''
  type: GettingStarted
  url: https://abnormalsecurity.my.site.com/knowledgebase/s/article/Abnormal-REST-API-Integration
- group: operate
  title: ''
  type: Support
  url: https://abnormal.ai/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://abnormalsecurity.my.site.com/knowledgebase/s/
- group: company
  title: ''
  type: Blog
  url: https://abnormal.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abnormal-ai
- group: start
  title: ''
  type: SignUp
  url: https://portal.abnormalsecurity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abnormal.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abnormal.ai/legal/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://abnormal.ai/legal/subprocessors
- group: other
  title: ''
  type: Patents
  url: https://abnormal.ai/legal/patents
- group: auth
  title: ''
  type: Authentication
  url: authentication/abnormal-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/abnormal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://abnormal.ai/legal/disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://security.abnormal.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/abnormal-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abnormal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abnormal-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abnormal-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abnormal-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.abnormalsecurity.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/abnormal-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/abnormal-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/abnormal-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/abnormal-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abnormal-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abnormal-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/abnormal-client-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Abnormal AI (formerly Abnormal Security) is a San Francisco based cloud email and human-behavior security company whose behavioral AI platform protects Microsoft 365 and Google Workspace against phishing, business email compromise, vendor fraud, account takeover and misdirected email. The platform is API-first: it integrates with Microsoft and Google over their APIs rather than by rewriting MX records, and every capability in the Abnormal Portal — threats, cases, AI Security Mailbox, employee and vendor insights, audit logs, RBAC roles and users, security posture management and dashboard aggregations — is also reachable through the Abnormal Security Client API, a bearer-token REST API published as OpenAPI 3.0.3 on SwaggerHub with separate US and EU production hosts. Abnormal also streams the same event data to SIEM and SOAR platforms over near-real-time webhooks.'
image: https://www.abnormal.ai/og/home.png
layout: provider
modified: '2026-08-02'
name: Abnormal AI
nav: Providers
network: true
overview: 'Abnormal AI publishes 1 API on the [APIs.io](https://apis.io/) network: Abnormal Security Client API. Tagged areas include Company, Security, Email Security, Cybersecurity, and Threat Intelligence.


  The Abnormal AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Abnormal AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
random_paper: 84
score:
  band: developing
  composite: 55.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.7
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 55.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Abnormal Authentication
  slug: abnormal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abnormal Domain Security
  slug: abnormal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Abnormal Vulnerability Disclosure
  slug: abnormal-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Abnormal Trust Center
  slug: abnormal-trust-center
  summary_line: SOC 2, ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001:2023, CSA STAR, FedRAMP Moderate, GovRAMP, TX-RAMP, CMMC, Cyber Essentials Plus, CJIS, ITAR, VPAT
slug: abnormal
tags:
- Company
- Security
- Email Security
- Cybersecurity
- Threat Intelligence
- Artificial Intelligence
- SOAR
- Identity
- Compliance
website: https://abnormal.ai/
---
