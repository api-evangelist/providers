---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'REST/XML API for managing the full Vulnerability Management Detection and Response lifecycle including asset inventory, scans, vulnerability findings, prioritization, and reports. Base URL varies per '
  name: Qualys VMDR API
  slug: vmdr-api
- description: Authentication endpoint that issues JSON Web Tokens (JWT) used as Bearer credentials for newer Qualys APIs (VMDR OT, CSAM, TotalCloud). Clients post username and password to /auth and pass the returne
  name: Qualys Authentication API
  slug: authentication-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qualys-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qualys
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qualys
- group: company
  title: ''
  type: Website
  url: https://www.qualys.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qualys.com
- group: other
  title: ''
  type: API Framework
  url: https://docs.qualys.com/en/vmdr-mobile/api/get_started/qualys_api_framework.htm
- group: start
  title: ''
  type: Free Trial
  url: https://www.qualys.com/free-trial/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qualys.com/forms/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://success.qualys.com/discussions/s/
- group: operate
  title: ''
  type: Support
  url: https://www.qualys.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qualys.com
- group: company
  title: ''
  type: Blog
  url: https://blog.qualys.com/feed
created: '2026-05-11'
description: Qualys is a cloud-based security and compliance platform offering Vulnerability Management Detection and Response (VMDR), Policy Compliance, Web Application Scanning, Container Security, EDR, and Cloud Security Posture Management. The Qualys API framework exposes XML and JSON REST endpoints across platform pods (qualysapi.qualys.com, qualysapi.qg2.apps.qualys.com, etc.) for managing scans, assets, vulnerabilities, reports, and findings. Authentication supports HTTP Basic auth and JWT bearer tokens via the Qualys Authentication API.
graphqls:
- description: 'This conceptual GraphQL schema models the Qualys cloud security platform, covering its major product areas: Vulnerability Management Detection and Response (VMDR), Policy Compliance, Web Application S'
  name: Qualys GraphQL Schema
  slug: qualys-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qualys.png
layout: provider
modified: '2026-05-11'
name: Qualys
nav: Providers
network: true
overview: 'Qualys publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Vulnerability Management, Compliance, VMDR, and Cloud Security.


  Qualys'' developer surface includes documentation, pricing, support, engineering blog, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 21.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qualys/refs/heads/main/screenshots/qualys-2026-06-20T192405.png
security:
- kind: domain-security
  name: Qualys Domain Security
  slug: qualys-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qualys
tags:
- Security
- Vulnerability Management
- Compliance
- VMDR
- Cloud Security
- Web Application Scanning
website: https://www.qualys.com
---
