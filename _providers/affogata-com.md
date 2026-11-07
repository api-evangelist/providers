---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.affogata.com/
- group: agent
  href: https://artifacts.apis.io/affogata-com/llms/affogata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affogata-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/affogata-com/well-known/affogata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affogata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/affogata-com/hosts/affogata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/affogata-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/affogata
- group: auth
  href: https://artifacts.apis.io/affogata-com/security/affogata-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/affogata-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/affogata-com/security/affogata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affogata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.affogata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.affogata.com/platform
- group: docs
  title: ''
  type: APIReference
  url: https://www.affogata.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.affogata.com/how-to
- group: company
  title: ''
  type: Blog
  url: https://www.affogata.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affogata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affogata.com/privacy-policy
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found after probing common spec URLs on the provider’s API hosts.
  evidence:
  - status: 0
    url: https://api.affogata.com/openapi.json
  - status: 404
    url: https://app.affogata.com/openapi.json
  - status: 301
    url: https://www.affogata.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Affogata provides an insights platform that transforms unstructured data into actionable, real‑time intelligence for research, product, data and AI teams. Their solution offers public benchmarks, AI‑ready data, and a managed API layer that enables enterprises to govern, audit, and integrate noisy data sources across industries, supporting use cases from market research to AI agent training.
image: https://www.affogata.com/wp-content/uploads/2026/10/affogata-og-default.png
layout: provider
modified: '2026-10-31'
name: Affogata
nav: Providers
network: true
overview: 'Affogata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data, Insights, Platform, and Enterprise.


  Affogata''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 20.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Affogata Com Domain Security
  slug: affogata-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Affogata Com Trust Center
  slug: affogata-com-trust-center
  summary_line: ISO 27001, GDPR
slug: affogata-com
tags:
- Artificial Intelligence
- Data
- Insights
- Platform
- Enterprise
- Company
website: https://www.affogata.com/
---
