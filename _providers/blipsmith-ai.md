---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/blipsmith-ai/plans/blipsmith-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blipsmith-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/blipsmith-ai/security/blipsmith-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blipsmith-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/blipsmith-ai/well-known/blipsmith-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blipsmith-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/blipsmith-ai/hosts/blipsmith-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blipsmith-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/blipsmith-ai/vendors/blipsmith-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blipsmith-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blipsmith.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blipsmith.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://blipsmith.ai/login
- group: auth
  href: https://artifacts.apis.io/blipsmith-ai/security/blipsmith-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blipsmith-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blipsmith-ai/security/blipsmith-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blipsmith-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blipsmith.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://blipsmith.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://blipsmith.ai/support
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found at the API host despite probing known paths.
  evidence:
  - status: error
    url: https://api.blipsmith.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Blipsmith provides an AI-powered sound effect generator for game developers, allowing users to describe a desired sound and receive royalty‑free, game‑ready WAV files within seconds. The service offers free first sound, tiered pricing, seamless loops, variations, and a web interface for quick creation, positioning itself as a SaaS solution for rapid audio asset creation in interactive entertainment.
image: https://blipsmith.ai/opengraph-image.png?opengraph-image.0tolzi2hi-d2d.png
layout: provider
modified: '2026-11-02'
name: Blipsmith
nav: Providers
network: true
overview: 'Blipsmith is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sound, Gaming, Generator, and Software-as-a-Service.


  Blipsmith''s developer surface includes pricing, support, and 11 more developer resources.'
plans:
- name: Blipsmith Ai Plans Pricing
  plan_count: 3
  slug: blipsmith-ai-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blipsmith Ai Domain Security
  slug: blipsmith-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blipsmith Ai Vulnerability Disclosure
  slug: blipsmith-ai-vulnerability-disclosure
  summary_line: no policy recorded
slug: blipsmith-ai
tags:
- Artificial Intelligence
- Sound
- Gaming
- Generator
- Software-as-a-Service
website: https://blipsmith.ai/
---
