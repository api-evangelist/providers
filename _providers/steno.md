---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The private, organization-scoped HTTP API behind Steno's first-party case-management integrations. The Steno-Litify Salesforce managed package is configured with a Steno API URL and an API Key that St
  name: Steno Integration API
  slug: integration-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://steno.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.steno.com/steno-litify-integration
- group: operate
  title: ''
  type: Support
  url: https://help.steno.com/
- group: company
  title: ''
  type: Blog
  url: https://brief.steno.com/
- group: start
  title: ''
  type: Login
  url: https://steno.com/account/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://steno.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://steno.com/privacy
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://steno.com/dpa
- group: operate
  title: ''
  type: StatusPage
  url: https://status.steno.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.steno.com/
- group: auth
  title: ''
  type: Compliance
  url: https://brief.steno.com/soc2-hipaa-compliance
- group: auth
  title: ''
  type: Authentication
  url: authentication/steno-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/steno-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/steno-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/steno-packages.yml
- group: design
  title: ''
  type: Components
  url: components/steno-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/steno-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Steno's API exists and is named on its own status page as "Core API services for Steno platform", but the only way to reach it is a Salesforce AppExchange managed package or a Clio App Directory listing whose key Steno issues per Salesforce Organization ID on request — there is no developer.steno.com or docs.steno.com host at all (both NXDOMAIN) and api.steno.com answers AWS API Gateway {"message":"Forbidden"} on every anonymous spec path.
  evidence:
  - status: 403
    url: https://api.steno.com/openapi.json
  - status: 403
    url: https://api.steno.com/v1/openapi.json
  - status: 200
    url: https://status.steno.com/
  - status: 200
    url: https://help.steno.com/steno-litify-integration
  - status: 404
    url: https://steno.com/llms.txt
  reason: marketplace-only
  state: gated
created: '2026-08-05'
description: 'Steno is a Los Angeles-based legal technology and litigation services company serving more than 1,200 US law firms with court reporting, remote and hybrid depositions, legal videography, interpreting, and record retrieval. Its software products are Steno Connect for Zoom (a videoconferencing and exhibit-handling app purpose-built for remote depositions, hearings, and bench trials), Firm Dashboard (scheduling, job management, file access, invoicing, SAML SSO, MFA, and role-based access control), Transcript Genius (AI-assisted transcript search, summarization, and video clip cutting), and DelayPay deferred-payment financing for plaintiff firms. Steno does not operate a public developer program: its integration surface is distributed through host platforms as a Salesforce AppExchange managed package for Litify, a Clio App Directory listing for Clio Manage, and a Zoom Marketplace app, each authenticated with an organization-scoped API key that Steno issues on request. Steno Connect,
  Firm Dashboard, and Ops are audited SOC 2 Type II and HIPAA by Linford & Company LLP, with posture published at a Vanta-hosted trust center.'
image: https://5816813.fs1.hubspotusercontent-na1.net/hubfs/5816813/Steno_Logo_Square_600x600.png
layout: provider
modified: '2026-08-05'
name: Steno
nav: Providers
network: true
overview: 'Steno publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Technology, Court Reporting, and Depositions.


  Steno''s developer surface includes documentation, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 25.5
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Steno Authentication
  slug: steno-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Steno Domain Security
  slug: steno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Steno Trust Center
  slug: steno-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: steno
tags:
- Company
- Legal
- Legal Technology
- Court Reporting
- Depositions
- Litigation Support
- Transcription
- Video
- Artificial Intelligence
- Salesforce
website: https://steno.com/
---
