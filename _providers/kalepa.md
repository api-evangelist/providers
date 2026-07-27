---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://kalepa.com/
- group: company
  title: ''
  type: Blog
  url: https://kalepa.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://kalepa.com/newsroom
- group: company
  title: ''
  type: About
  url: https://kalepa.com/company
- group: other
  title: ''
  type: CaseStudies
  url: https://kalepa.com/case-studies
- group: other
  title: ''
  type: Events
  url: https://kalepa.com/events
- group: company
  title: ''
  type: Careers
  url: https://kalepa.com/careers
- group: other
  title: ''
  type: Sitemap
  url: https://kalepa.com/sitemap.xml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kalepa.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kalepa-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://kalepa.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kalepa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kalepa-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kalepa.com/solutions/for-it-ai-leaders
- group: design
  title: ''
  type: Conformance
  url: conformance/kalepa-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kalepa-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kalepa-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kalepa.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://kalepa.com/book-a-demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kalepa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kalepa
created: '2026-07-25'
description: 'Kalepa is a New York–headquartered insurtech founded in 2018 by Paul Monasterio and Daniel Hillman that builds Copilot, an AI underwriting workbench sold to commercial property and casualty carriers, MGAs, mutuals and brokers in its home market of the United States. Copilot covers the commercial underwriting workflow end to end — submission ingestion out of broker email and document packages (ACORD forms, statements of value, loss runs, supplemental applications), clearance and sanctions screening, triage by bindability and profitability, risk analysis, rating, quote and bind document generation, and portfolio management. Its API posture is partner-gated and there is no public API. Kalepa publishes no developer portal — developer.kalepa.com, developers.kalepa.com and docs.kalepa.com do not resolve, and /developers, /api, /developer, /partners and /integrations on kalepa.com all return 404. A production API host does exist at api.kalepa.com and a "Kalepa API" component is monitored
  on the company status page, but every documentation path on it returns 404 and the application at copilot.kalepa.com redirects to api.kalepa.com/auth/login, so the only integration surface is behind a customer login negotiated in a commercial deal. The only technical posture Kalepa publishes sits on its For IT/AI Leaders page — an "API-first platform" claim, a 4-6 week production deployment, and SOC 2 Type II, the single certification named anywhere on the site. Its open source is real but unrelated to the product API: two PyPI packages (safe-init, marshmallow-fastoneofschema) and 24 Terraform modules in the public HashiCorp registry, all infrastructure tooling rather than client SDKs. ACORD appears only as an ingested document format, not as an implemented data standard — no ACORD XML, AL3, NGDS, IVANS download, Applied Epic or Vertafore integration is documented anywhere on the public site. Kalepa is a clean example of the US insurance seam: no federal regulator, no open-insurance mandate,
  and therefore nothing forcing a vendor in the underwriting layer to expose anything publicly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Kalepa
nav: Providers
network: true
overview: 'Kalepa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Insurtech, Underwriting, and Property and Casualty.


  Kalepa''s developer surface includes engineering blog, signup flow, and 19 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 23.5
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.5
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 56.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kalepa/refs/heads/main/screenshots/kalepa-2026-07-25T223430.png
security:
- kind: domain-security
  name: Kalepa Domain Security
  slug: kalepa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kalepa Vulnerability Disclosure
  slug: kalepa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kalepa
tags:
- Insurance
- United States
- Insurtech
- Underwriting
- Property and Casualty
- Commercial Insurance
- Artificial Intelligence
- ACORD
- Partner Gated
- No Public API
website: https://kalepa.com/
---
