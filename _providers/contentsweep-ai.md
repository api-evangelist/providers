---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Content Sweep offers an API (MCP endpoint) for scanning and monitoring content.
  name: Content Sweep API
  slug: content-sweep-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/contentsweep-ai/plans/contentsweep-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contentsweep-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/contentsweep-ai/llms/contentsweep-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contentsweep-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/contentsweep-ai/hosts/contentsweep-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentsweep-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/contentsweep-ai/vendors/contentsweep-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentsweep-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://contentsweep.ai/login
- group: auth
  href: https://artifacts.apis.io/contentsweep-ai/security/contentsweep-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentsweep-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contentsweep.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://contentsweep.ai/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://contentsweep.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://contentsweep.ai/signup
- group: operate
  title: ''
  type: Support
  url: https://contentsweep.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contentsweep.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contentsweep.ai/legal/privacy
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was found despite probing common spec locations.
  evidence:
  - status: 404
    url: https://contentsweep.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Adult creator content protection and leaked-content help. Sweep will find leaked content and remove it on your behalf. Content protection for adult creators starts with a private possible-match count and careful review before any DMCA takedown request. The service offers a free scan, ongoing monitoring, unlimited takedown requests, delisting notices, and 24/7 availability. Pricing is a clear $40 per month. The platform includes resources, FAQ, and support for independent creators.
image: https://contentsweep.ai/brand/sweep-social-card.png
layout: provider
modified: '2026-10-29'
name: contentsweep-ai
nav: Providers
network: true
overview: 'contentsweep-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Adult-Content-Protection, DMCA, Content-Monitoring, and Privacy.


  contentsweep-ai''s developer surface includes documentation, pricing, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Contentsweep Ai Plans Pricing
  plan_count: 1
  slug: contentsweep-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Contentsweep Ai Rate Limits
  slug: contentsweep-ai-rate-limits
scopes:
- name: Contentsweep Ai Scopes
  scope_count: 0
  slug: contentsweep-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contentsweep Ai Authentication
  slug: contentsweep-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Contentsweep Ai Domain Security
  slug: contentsweep-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contentsweep-ai
tags:
- Company
- Adult-Content-Protection
- DMCA
- Content-Monitoring
- Privacy
website: https://contentsweep.ai/
---
