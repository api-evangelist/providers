---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connectrn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connectrn.com/
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/connectrn_stock/
- group: company
  title: ''
  type: Blog
  url: https://www.connectrn.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.connectrn.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.connectrn.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectrn.com/main-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connectrn.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/connectRN
- group: operate
  title: ''
  type: StatusPage
  url: https://status.connectrn.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/connectrn-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/connectrn-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connectrn-llms.txt
coverage:
  checked: '2026-08-09'
  detail: connectRN ships only end-user products — a clinician mobile app and a facility web app at app.connectrn.com — and its application backend api.connectrn.com answers a plain-text `NotFound` 404 on every anonymously probed path including `/`, `/v1`, `/openapi.json` and `/graphql`; there is no developer portal, no docs host (developer/developers/docs.connectrn.com do not resolve), and no spec anywhere on the site or in the connectRN GitHub organization.
  evidence:
  - status: 404
    url: https://api.connectrn.com/openapi.json
  - status: 404
    url: https://api.connectrn.com/
  - status: 404
    url: https://www.connectrn.com/llms.txt
  - status: 404
    url: https://api.connectrn.com/.well-known/agent-card.json
  - status: 200
    url: https://connectrn.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: connectRN is a Waltham, Massachusetts based per-diem (PRN) healthcare staffing marketplace that connects nurses, CNAs and allied clinicians with open shifts at hospitals, home health and hospice agencies, and skilled nursing facilities across the United States. Clinicians browse and claim shifts through the connectRN mobile app with no minimum commitment, no required weekends or holidays, and same-day pay; facilities post shifts, auto-backfill open coverage and approve timesheets through a web platform at app.connectrn.com. In April 2026 connectRN merged with SnapCare, combining connectRN's PRN clinician community with SnapCare's Booker workforce technology platform. connectRN operates a public status page but publishes no public developer program, API documentation, or machine-readable API contract; its API host api.connectrn.com serves the first-party mobile and web applications only.
image: https://cdn.prod.website-files.com/689ccaaf2d508bcba0f8168a/689cccfba48ff91d2ddeacfc_LogoMark_Registered_Purple.png
layout: provider
modified: '2026-08-09'
name: ConnectRN
nav: Providers
network: true
overview: 'ConnectRN is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Staffing, and Nursing.


  ConnectRN''s developer surface includes engineering blog, signup flow, and 11 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 17.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Connectrn Domain Security
  slug: connectrn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connectrn
tags:
- Company
- Healthcare
- Health IT
- Staffing
- Nursing
- Workforce Management
- Marketplace
- Mobile App
website: https://www.connectrn.com/
---
