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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: RESTful JSON API for CapLinked virtual data rooms, secured by HMAC-SHA256 request signing. Manage organizations, teams, workspaces, folders, files, groups, permissions, uploads, downloads, watermarks,
  name: CapLinked API
  slug: caplinked-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/caplinked-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caplinked-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caplinked.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.caplinked.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.caplinked.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.caplinked.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.caplinked.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.caplinked.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caplinked
- group: company
  title: ''
  type: Blog
  url: https://www.caplinked.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.caplinked.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.caplinked.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.caplinked.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caplinked.com/company/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caplinked.com/company/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.caplinked.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.caplinked.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.caplinked.com/api-changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/caplinked-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/caplinked-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/caplinked-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caplinked-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caplinked-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/caplinked-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/caplinked-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caplinked-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caplinked-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/caplinked-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caplinked-llms.txt
created: '2026-07-17'
description: 'CapLinked is a secure virtual data room (VDR) provider used for M&A, fundraising, due diligence, audits, and other confidential document workflows. The CapLinked API is a RESTful, JSON API secured by HMAC-SHA256 request signing (TLS + signed requests) that lets developers embed CapLinked''s information-security controls into their own applications: protect and encrypt files in secure cloud storage, configure Access Control List (ACL) privileges, apply enterprise Digital Rights Management (DRM) to Microsoft Office and PDF files, generate dynamic watermarks, produce exhaustive activity and audit-trail reports, and run OCR-backed search over stored files. The API models an Organization > Team > Workspace hierarchy containing Folders, Files, Groups, Permissions, Activities, Uploads, Downloads, and Watermarks, and ships official SDKs for Node.js, Ruby, PHP, C#/.NET, and Python. It supports search, pagination, and filtering.'
image: https://www.caplinked.com/wp-content/uploads/2022/03/Caplinked-Logo-299x80-e1541700266853.png
layout: provider
mcp_servers:
- description: ''
  name: caplinked-mcp.yml
  slug: caplinked-mcpyml
modified: '2026-07-18'
name: Caplinked
nav: Providers
network: true
overview: 'Caplinked publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtual Data Room, Document Security, File Sharing, and Due Diligence.


  Caplinked''s developer surface includes documentation, getting-started guide, signup flow, engineering blog, pricing, support, changelog, and 22 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 38.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caplinked/refs/heads/main/screenshots/caplinked-2026-07-25T204422.png
security:
- kind: authentication
  name: Caplinked Authentication
  slug: caplinked-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Caplinked Domain Security
  slug: caplinked-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Caplinked Trust Center
  slug: caplinked-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, HITECH, PCI SAQ-D, FISMA, EU-U.S. Privacy Shield
slug: caplinked
tags:
- Company
- Virtual Data Room
- Document Security
- File Sharing
- Due Diligence
- Mergers and Acquisitions
- Digital Rights Management
- Compliance
- Data Room
- Security
website: https://caplinked.com
---
