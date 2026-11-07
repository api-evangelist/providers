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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cavendo AI provides a human‑led AI platform with endpoints described in the website documentation.
  name: Cavendo AI API
  slug: cavendo-ai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cavendo-ai/plans/cavendo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cavendo-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/cavendo-ai/security/cavendo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cavendo-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cavendo-ai/llms/cavendo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cavendo-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/cavendo-ai/hosts/cavendo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cavendo-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cavendo-ai/vendors/cavendo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cavendo-ai-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://cavendo.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://cavendo.ai/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://cavendo.ai/pricing
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation site does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files despite extensive pages.
  evidence:
  - status: unreachable
    url: https://api.cavendo.ai/openapi.json
  - status: 200
    url: https://cavendo.ai/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cavendo AI provides a human‑led AI platform for teams and agencies, enabling them to set up, run, and review AI‑driven workflows across tasks such as monthly reports, content creation, site audits, client updates, proposals, development tasks, support replies, and lead follow‑up. The service integrates with popular models like ChatGPT, Claude, Gemini, and Perplexity, and connects to tools like email, Slack, WordPress, and CRMs, ensuring human oversight before any output is delivered. Pricing starts at $299/mo for teams, with higher tiers for agencies and custom enterprise solutions.
image: https://cavendo.ai/og-image.png
layout: provider
modified: '2026-11-04'
name: Cavendo AI
nav: Providers
network: true
overview: 'Cavendo AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Workflows, Agency, and Platform.


  Cavendo AI''s developer surface includes getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Cavendo Ai Plans Pricing
  plan_count: 5
  slug: cavendo-ai-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cavendo Ai Domain Security
  slug: cavendo-ai-domain-security
  summary_line: TLSv1.3
slug: cavendo-ai
tags:
- Artificial Intelligence
- Automation
- Workflows
- Agency
- Platform
website: https://cavendo.ai/
---
