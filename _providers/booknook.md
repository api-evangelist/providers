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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/booknook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.booknook.com/
- group: company
  title: ''
  type: About
  url: https://www.booknook.com/about
- group: operate
  title: ''
  type: Support
  url: https://support.booknook.com/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.booknook.com/knowledge-base/
- group: company
  title: ''
  type: Blog
  url: https://blog.booknook.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.booknook.com/rss.xml
- group: operate
  title: ''
  type: StatusPage
  url: https://booknook.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.booknook.com/product-updates/
- group: start
  title: ''
  type: Login
  url: https://app.booknooklearning.com/student/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.booknook.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.booknook.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BookNook
- group: operate
  title: ''
  type: Contact
  url: https://www.booknook.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.booknook.com/careers
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/booknook-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/booknook-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/booknook-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/booknook-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/booknook-llms.txt
coverage:
  checked: '2026-08-08'
  detail: 'BookNook runs a production API service — api.booknooklearning.com answers 200 with {"success":true,"message":"BookNook API: ..."} and "API" is a named component on its public Statuspage — but it is the tutoring platform''s own backend, not a product: no developer portal, no reference, no OpenAPI/GraphQL/MCP/agent card at any probed path on that host or on www.booknook.com, no SDK on any registry, and the GitHub org''s single public repo is a fork of node-db-migrate; districts integrate through Clever Secure Sync and ClassLink SSO, where BookNook is the consumer of someone else''s API.'
  evidence:
  - status: 200
    url: https://api.booknooklearning.com/
  - status: 404
    url: https://api.booknooklearning.com/openapi.json
  - status: 404
    url: https://api.booknooklearning.com/graphql
  - status: 404
    url: https://www.booknook.com/llms.txt
  - status: 404
    url: https://www.booknook.com/.well-known/agent-card.json
  - status: 200
    url: https://booknook.statuspage.io/api/v2/components.json
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: BookNook is a K-8 high-impact tutoring company that delivers live 1:1 and small-group virtual instruction in reading and math through its own online learning platform. Schools and districts license the platform and either use BookNook's trained tutor corps or run sessions with their own staff; educators work from a district dashboard that reports attendance, session detail, lesson-band progress, and math engagement and understanding scores. Students and staff reach the platform at app.booknooklearning.com and sign in manually or through Clever Instant Login and ClassLink single sign-on, with district rosters provisioned by Clever Secure Sync. BookNook operates a production API service (api.booknooklearning.com, listed as an "API" component on its public status page), but it is the platform's own backend — BookNook publishes no developer portal, no API reference, and no machine-readable contract, and its integration surface is consumed from partner platforms (Clever, ClassLink,
  Ed-Fi) rather than published as its own.
image: https://www.booknook.com/hubfs/booknook-512-icon.png
layout: provider
modified: '2026-08-08'
name: BookNook
nav: Providers
network: true
overview: 'BookNook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Tutoring, and K-12.


  BookNook''s developer surface includes support, engineering blog, changelog, and 17 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 21.7
  delta: -1.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 22.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Booknook Domain Security
  slug: booknook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: booknook
tags:
- Company
- Education
- EdTech
- Tutoring
- K-12
- Learning Platform
- Reading
- Mathematics
- Student Data
- Rostering
website: https://www.booknook.com/
---
