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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Usefomo Agentic Access
  operation_count: 8
  slug: usefomo-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.fomo.com/api/v1
  baseurl_source: spec
  description: The Applications API from FOMO — 6 operation(s) for applications.
  name: FOMO Applications API
  slug: usefomo-applications-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/usefomo/agentic-access/usefomo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/usefomo-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/usefomo/rules/usefomo-rules.yml
  title: ''
  type: Spectral
  url: rules/usefomo-rules.yml
- group: design
  href: https://artifacts.apis.io/usefomo/errors/usefomo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usefomo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/usefomo/conformance/usefomo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usefomo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usefomo/llms/usefomo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usefomo-llms.txt
- group: other
  href: https://artifacts.apis.io/usefomo/hosts/usefomo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usefomo-hosts.yml
- group: other
  href: https://artifacts.apis.io/usefomo/vendors/usefomo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usefomo-vendors.yml
- group: build
  href: https://artifacts.apis.io/usefomo/packages/usefomo-packages.yml
  title: ''
  type: SDKs
  url: packages/usefomo-packages.yml
- group: build
  href: https://artifacts.apis.io/usefomo/packages/usefomo-packages.yml
  title: ''
  type: Packages
  url: packages/usefomo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usefomo.com/terms
- group: operate
  title: ''
  type: Support
  url: http://help.usefomo.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usefomo.com/
- group: start
  title: ''
  type: SignUp
  url: https://usefomo.com/app/register
- group: commercial
  title: ''
  type: Pricing
  url: https://usefomo.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://usefomo.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://usefomo.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usefomo.com/login?redirect_uri=/reference/welcome-to-fomo
- group: start
  title: ''
  type: GettingStarted
  url: https://help.usefomo.com/category/13-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usefomo.com/
- group: auth
  href: https://artifacts.apis.io/usefomo/security/usefomo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usefomo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usefomo.com/
coverage:
  checked: '2026-10-26'
  detail: Documentation redirects to a JavaScript‑rendered portal with no machine‑readable spec.
  evidence:
  - status: 302
    url: https://usefomo.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Fomo is the world’s first social proof marketing platform, helping brands increase conversions by showcasing real‑time customer activity. The service aggregates user actions such as purchases, sign‑ups, and reviews, and displays them as dynamic notifications on websites. By leveraging social proof, Fomo aims to boost trust, reduce cart abandonment, and drive higher sales for e‑commerce and SaaS businesses. The platform offers customizable widgets, analytics, and integrations with major marketing tools.
image: https://s3.amazonaws.com/fomo-static-assets/og/fomo-social-proof-homepage-og.jpg
layout: provider
modified: '2026-10-26'
name: FOMO
nav: Providers
network: true
overview: 'FOMO publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Applications API. Tagged areas include Company, Social Proof, Marketing, Software-as-a-Service, and E-Commerce.


  The FOMO catalog on APIs.io includes 1 Spectral governance ruleset.


  FOMO''s developer surface includes support, signup flow, pricing, changelog, engineering blog, API reference, getting-started guide, and 14 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: FOMO API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: usefomo-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 25.0
    discoverability: 55.4
    operational_transparency: 15.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/usefomo/usefomo-2026-11-03T145524.png
security:
- kind: domain-security
  name: Usefomo Domain Security
  slug: usefomo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usefomo
tags:
- Company
- Social Proof
- Marketing
- Software-as-a-Service
- E-Commerce
website: https://usefomo.com/
---
