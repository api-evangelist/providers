---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/askwatch-ai/plans/askwatch-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askwatch-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askwatch-ai/llms/askwatch-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askwatch-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/askwatch-ai/well-known/askwatch-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askwatch-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/askwatch-ai/hosts/askwatch-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askwatch-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/askwatch-ai/vendors/askwatch-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askwatch-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/askwatch
- group: start
  title: ''
  type: GettingStarted
  url: https://askwatch.ai/help/getting-started/add-a-website
- group: auth
  href: https://artifacts.apis.io/askwatch-ai/security/askwatch-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askwatch-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askwatch.ai/
- group: company
  title: ''
  type: Blog
  url: https://askwatch.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://askwatch.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askwatch.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askwatch.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://askwatch.ai/help
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: timeout
    url: https://api.askwatch.ai/openapi.json
  - status: 404
    url: https://askwatch.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskWatch provides an AI visibility tracking platform that helps marketers and agencies understand why AI systems recommend certain brands or competitors. Users can check their brand presence, see AI‑generated recommendations, and receive actionable insights to improve visibility. The service offers free tools like AI‑visibility checkers, overview checkers, and integrations with popular AI models. It includes pricing plans for deeper monitoring, a blog with industry insights, and support resources. AskWatch aims to make AI‑driven brand discovery transparent and actionable for businesses.
image: https://askwatch.ai/opengraph-image?e17b7bdd535eddcf
layout: provider
modified: '2026-11-01'
name: AskWatch
nav: Providers
network: true
overview: 'AskWatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Visibility, Marketing, Agencies, Brand Monitoring, and AI engines.


  AskWatch''s developer surface includes getting-started guide, engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Askwatch Ai Plans Pricing
  plan_count: 4
  slug: askwatch-ai-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 22.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askwatch Ai Domain Security
  slug: askwatch-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askwatch-ai
tags:
- AI Visibility
- Marketing
- Agencies
- Brand Monitoring
- AI engines
- Autopilot
website: https://askwatch.ai/
---
