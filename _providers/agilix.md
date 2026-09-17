---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'The Buzz API is the programmable surface of the Agilix Learning Suite. It is a command-style HTTP API rather than a path-and-method REST API: every one of its 291 documented operations is issued as PO'
  name: Agilix Buzz API (DLAP / xLi)
  slug: buzz-api
artifact_total: 8
asyncapis:
- description: ''
  name: Agilix Datastream Webhooks
  slug: agilix-datastream-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/security/agilix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agilix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/security/agilix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agilix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agilix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.agilixbuzz.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.agilixbuzz.com/docs/entry/Concept/Overview.md
- group: docs
  title: ''
  type: APIReference
  url: https://api.agilixbuzz.com/docs/all.md
- group: start
  title: ''
  type: GettingStarted
  url: https://api.agilixbuzz.com/docs/entry/Concept/Tutorial.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgilixLabs
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/packages/agilix-packages.yml
  title: ''
  type: SDKs
  url: packages/agilix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/packages/agilix-packages.yml
  title: ''
  type: Packages
  url: packages/agilix-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.agilix.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.agilix.com/hc/en-us
- group: operate
  title: ''
  type: ContactUs
  url: https://www.agilix.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.agilix.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agilix.com/privacy
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/plans/agilix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agilix-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/conformance/agilix-conformance.yml
  title: ''
  type: Compliance
  url: conformance/agilix-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/conformance/agilix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agilix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/well-known/agilix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agilix-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/llms/agilix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agilix-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/lifecycle/agilix-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/agilix-lifecycle.yml
- group: other
  title: ''
  type: Accessibility
  url: https://www.agilix.com/accessibility
- group: company
  title: ''
  type: Partners
  url: https://www.agilix.com/partners
- group: company
  title: ''
  type: News
  url: https://www.agilix.com/news-and-press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/security/agilix-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agilix-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/security/agilix-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agilix-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agilix/refs/heads/main/asyncapi/agilix-datastream-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agilix-datastream-webhooks.yml
created: '2026-09-12'
description: Agilix Labs, Inc. is a K-12 education technology company in Orem, Utah that builds the Agilix Learning Suite — a white-label, multi-tenant set of products schools, districts, virtual and online schools and curriculum publishers use to author, deliver and assess online and blended learning. The suite is Buzz (the learning management system), TutorKit (tutoring program management), Publish Anywhere (LTI-based content distribution to any LMS), Dawn (mobile, offline-capable delivery) and BusyBee (an AI teaching assistant built into Buzz). Agilix has built learning technology for more than 25 years and reaches millions of teachers and students in 20+ languages across 200+ countries, running on AWS. Its public developer surface is the Buzz API — also called DLAP or xLi — a command-style HTTP API with 291 documented commands covering domains, users, courses, enrollments, items, questions, submissions, gradebooks, objectives, rights and licensing, plus a configurable Data Stream event
  feed with roughly 70 event types and five delivery targets including HTTPS webhooks. Buzz is a 1EdTech LTI 1.3 / LTI Advantage platform and exchanges SCORM run-time data. Authentication is OAuth 2.0 client credentials with a JWT client assertion (RFC 6749 + RFC 7523) against an Application Identity account. Agilix publishes an llms.txt for both its corporate site and its API documentation, an ai-plugin.json manifest on two API hosts, weekly dated release notes, and seven first-party sample client libraries on GitHub — but no OpenAPI, no MCP server and no agent card.
image: https://cdn.prod.website-files.com/63e3df066454cf5d1a3762bf/63fcec436021ff40163c2ad8_logo.png
layout: provider
modified: '2026-09-12'
name: Agilix
nav: Providers
network: true
overview: 'Agilix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Learning Management System, and K-12.


  The Agilix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agilix''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, product news, and 21 more developer resources.'
plans:
- name: Agilix Plans Pricing
  plan_count: 0
  slug: agilix-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Agilix Rate Limits
  slug: agilix-rate-limits
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 76.3
  previous_composite: 52.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 59.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agilix Authentication
  slug: agilix-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agilix Domain Security
  slug: agilix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agilix Vulnerability Disclosure
  slug: agilix-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Agilix Trust Center
  slug: agilix-trust-center
  summary_line: SOC 2
slug: agilix
tags:
- Company
- Education
- EdTech
- Learning Management System
- K-12
- Online Learning
- Tutoring
- Assessment
- LTI
- SCORM
- Artificial Intelligence
- Event
website: https://www.agilix.com/
---
