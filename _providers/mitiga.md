---
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'The product API behind the Mitiga cloud detection and response platform. The host is live and fronted by a Kong gateway, and it publishes an anonymous RFC 8414 authorization-server metadata document, '
  name: Mitiga Platform API
  slug: mitiga-platform-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mitiga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mitiga.io/
- group: company
  title: ''
  type: Blog
  url: https://www.mitiga.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mitiga.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mitiga
- group: start
  title: ''
  type: Login
  url: https://mitiga.cloud/
- group: operate
  title: ''
  type: Support
  url: https://www.mitiga.io/company
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mitiga.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mitiga.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mitiga.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/mitiga-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mitiga-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mitiga-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mitiga-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mitiga-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mitiga-conformance.yml
created: '2026-08-04'
description: 'Mitiga is a cloud and SaaS security company built around what it calls Zero-Impact Breach Prevention — an AI-native Cloud Detection and Response (CDR) platform that ingests, normalizes and retains activity logs from roughly 100 cloud, SaaS, identity and AI platforms in a Cloud Security Data Lake with 1,000+ days of forensic retention, then detects, investigates and helps contain active attacks. The company was founded by cloud incident responders and sells 24/7 managed cloud detection and response, managed threat hunting, and emergency cloud and SaaS incident response alongside the platform, with Helios AI as its AI SOC analyst layer. Monitoring is agentless and API-based: Mitiga is a heavy consumer of other providers'' APIs rather than a publisher of a public developer program. Its own product API runs at api.mitiga.cloud behind a Kong gateway and an Auth0 OAuth 2.0 authorization server, but no public reference or machine-readable contract is published.'
image: https://cdn.prod.website-files.com/68b741896c644c7106024a46/68e43e28a7c652f90cd2024c_Mitiga-Open-Grpah.png
layout: provider
modified: '2026-08-04'
name: Mitiga
nav: Providers
network: true
overview: 'Mitiga publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, SaaS Security, and Cloud Detection and Response.


  Mitiga''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 5
scopes:
- name: Mitiga Scopes
  scope_count: 14
  slug: mitiga-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 23.7
  delta: -0.7
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mitiga/refs/heads/main/screenshots/mitiga-2026-08-07T183806.png
security:
- kind: authentication
  name: Mitiga Authentication
  slug: mitiga-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Mitiga Domain Security
  slug: mitiga-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mitiga Trust Center
  slug: mitiga-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27001:2022, CSA STAR Level 1, HIPAA, GDPR, CCPA, Microsoft SSPA, AWS Qualified Software
slug: mitiga
tags:
- Company
- Security
- Cloud Security
- SaaS Security
- Cloud Detection and Response
- Incident Response
- Threat Detection
- Identity Security
- Managed Security Services
- Artificial Intelligence
website: https://www.mitiga.io/
---
