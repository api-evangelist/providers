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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aurentia-fr/llms/aurentia-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurentia-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/aurentia-fr/well-known/aurentia-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aurentia-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/aurentia-fr/hosts/aurentia-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurentia-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurentia-fr/vendors/aurentia-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurentia-fr-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.aurentia.fr/legal/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://entrepreneurs.aurentia.fr/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aurentia.fr/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://entrepreneurs.aurentia.fr/privacy
- group: start
  title: ''
  type: Login
  url: https://entrepreneurs.aurentia.fr/login
- group: auth
  href: https://artifacts.apis.io/aurentia-fr/security/aurentia-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurentia-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aurentia.fr/
- group: company
  title: ''
  type: Blog
  url: https://www.aurentia.fr/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aurentia.fr/tarifs/
- group: commercial
  title: ''
  type: Legal
  url: https://www.aurentia.fr/legal/
coverage:
  checked: '2026-11-02'
  detail: Main website renders content via JavaScript, providing no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.aurentia.fr/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Aurentia provides AI-powered tools for entrepreneurs to manage, grow, and develop their businesses. Their platform offers modules for forecasting, action planning, market monitoring, branding, and productivity, integrating AI assistants across finance, sales, marketing, and project management. Users can access free trials, customize pricing plans, and leverage resources such as legal tools, domain registration, and graphic design support.
image: https://www.aurentia.fr/images/og-default.png
layout: provider
modified: '2026-11-02'
name: Aurentia
nav: Providers
network: true
overview: 'Aurentia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Entrepreneurship, Productivity, Tools, and Platform.


  Aurentia''s developer surface includes engineering blog, pricing, legal docs, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 19.0
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
  name: Aurentia Fr Domain Security
  slug: aurentia-fr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aurentia-fr
tags:
- Artificial Intelligence
- Entrepreneurship
- Productivity
- Tools
- Platform
- Business
website: https://aurentia.fr/
---
