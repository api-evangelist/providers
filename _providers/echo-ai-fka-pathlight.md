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
  band: human-only
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/echo-ai-fka-pathlight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.echoai.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pathlight
- group: build
  title: ''
  type: Packages
  url: packages/echo-ai-fka-pathlight-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/echo-ai-fka-pathlight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/echo-ai-fka-pathlight-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: Echo AI was acquired by Calabrio on 2024-12-11 and wound down its own web presence — echoai.com now answers HTTP 404 with a Framer "Site Not Found" shell on every path including /openapi.json and /.well-known/*, and pathlight.com has no A record at all.
  evidence:
  - status: 404
    url: https://echoai.com/
  - status: 404
    url: https://echoai.com/openapi.json
  - status: 404
    url: https://echoai.com/.well-known/agent-card.json
  - status: 0
    url: https://www.pathlight.com/
  - status: 200
    url: https://www.calabrio.com/press/calabrio-continues-to-accelerate-ai-innovation-with-acquisition-of-echo-ai/
  reason: defunct
  state: none
created: '2026-07-17'
description: Echo AI (formerly Pathlight) was an AI-driven customer conversation intelligence platform used by customer-experience and support teams to analyze support conversations, surface hidden insights, and coach agents. Founded as Pathlight and backed by Kleiner Perkins, Insight Partners and Quiet Capital, it rebranded to Echo AI in January 2024 and was acquired by contact-center workforce-engagement vendor Calabrio on 2024-12-11; the technology now ships inside Calabrio ONE, and calabrio.com itself now redirects to verint.com. The company publishes no discoverable public developer surface of its own — no API documentation, OpenAPI, GraphQL, MCP server, agent card or first-party SDK — and both brand domains are dark — pathlight.com no longer resolves and echoai.com returns a removed Framer site (HTTP 404). The Wayback index for both domains contains no /api, /docs/api or /developer path at any point in their history, only legal pages. The only verified live public asset is the Pathlight
  GitHub organization, whose 62 public repositories are third-party forks plus first-party Singer.io taps that INGEST other vendors' APIs (Zendesk, Gorgias, Gladly, Dialpad, Five9, Kustomer) rather than any first-party client library. This profile is retained as an identity record; no fabricated API artifacts were added, and the npm/PyPI packages that share the Pathlight and Echo AI names were verified to belong to unrelated publishers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/echo-ai-fka-pathlight.png
layout: provider
modified: '2026-08-14'
name: Echo AI (fka Pathlight)
nav: Providers
network: true
overview: Echo AI (fka Pathlight) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversation Intelligence, Customer Experience, Customer-Support, and Artificial Intelligence.
plans:
- name: Echo Ai Fka Pathlight Plans Pricing
  plan_count: 0
  slug: echo-ai-fka-pathlight-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Echo Ai Fka Pathlight Rate Limits
  slug: echo-ai-fka-pathlight-rate-limits
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Echo Ai Fka Pathlight Domain Security
  slug: echo-ai-fka-pathlight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: echo-ai-fka-pathlight
tags:
- Company
- Conversation Intelligence
- Customer Experience
- Customer-Support
- Artificial Intelligence
- Analytics
website: https://www.echoai.com/
---
