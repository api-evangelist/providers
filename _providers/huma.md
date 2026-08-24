---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 527
  human_in_the_loop: 6
  name: Huma Agentic Access
  operation_count: 984
  slug: huma-agentic-access
  summary_line: 984 operations · 527 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: Huma's backend Integration API for embedding Huma platform functionality into first-party applications. Authentication uses a Workspace-issued huma-config.json (client-credentials style) consumed by t
  name: Huma Integration API
  slug: huma-integration-api
- description: Huma's software development kits for building or enhancing applications with out-of-the-box Huma functionality across iOS, Android, and Angular, covering authentication/authorization, connected Device
  name: Huma Mobile & Web SDK
  slug: huma-mobile-sdk
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huma-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/huma-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/huma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://huma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.huma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.huma.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.huma.com/quick-start/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/huma-engineering
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huma.com/
- group: start
  title: ''
  type: SignUp
  url: https://workspace.huma.com/
- group: auth
  title: ''
  type: Security
  url: https://docs.huma.com/trust-security/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.huma.com/trust-security/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/huma-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/huma-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/huma-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/huma-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/huma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/huma-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/huma-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://workspace-gcp-uk.api.huma.com/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://huma.com/legal/website-privacy-policy
created: '2026-07-24'
description: Huma (Huma Therapeutics Limited) is a United Kingdom-headquartered digital health and remote patient monitoring company that provides a regulated, configurable platform for building and running healthcare and life-sciences applications. Its Huma Workspace lets clinical teams assemble no-code apps, connected-device data capture, ePRO questionnaires, algorithm-based assessments, and a clinician portal for telemedicine and remote monitoring, while its developer surface exposes a backend Integration API and native iOS, Android, and Angular SDKs for embedding Huma functionality into first-party applications. Huma operates as CE-marked / MDR Class IIb medical-device software and is ISO 13485 and ISO 27001 certified, positioning it as clinical-grade infrastructure used by health systems (including the NHS in its UK home market), pharma, and clinical-trials programs. The developer platform documents a backend Integration API and mobile SDKs; API access is gated behind a Huma Workspace
  account. A full Huma Platform OpenAPI (3.0.3, 984 operations across 76 tags) is served, unlinked, from the ReDoc reference at workspace-gcp-uk.api.huma.com/specs/; authentication is JWT bearer and Hawk MAC (no OAuth2 scheme). No public HL7 FHIR CapabilityStatement is published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Huma MCP Server
  slug: huma-mcp-server
modified: '2026-07-24'
name: Huma
nav: Providers
network: true
overview: 'Huma publishes 1 API on the [APIs.io](https://apis.io/) network: Integration API. Tagged areas include Healthcare, United Kingdom, Remote Patient Monitoring, Telehealth, and Digital Health.


  Huma''s developer surface includes authentication, documentation, getting-started guide, signup flow, API reference, and 17 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 30.3
    contract_quality: 40.9
    developer_ergonomics: 58.9
    discoverability: 66.7
    governance: 30.3
    operational_transparency: 13.2
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huma/refs/heads/main/screenshots/huma-2026-07-25T221642.png
security:
- kind: authentication
  name: Huma Authentication
  slug: huma-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Huma Domain Security
  slug: huma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Huma Trust Center
  slug: huma-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 13485
slug: huma
tags:
- Healthcare
- United Kingdom
- Remote Patient Monitoring
- Telehealth
- Digital Health
- Clinical Trials
- SDK
- Medical Device Software
- Population Health
website: https://huma.com/
---
