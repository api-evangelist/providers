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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/kusari/llms/kusari-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kusari-llms.txt
- group: other
  href: https://artifacts.apis.io/kusari/hosts/kusari-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kusari-hosts.yml
- group: other
  href: https://artifacts.apis.io/kusari/vendors/kusari-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kusari-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kusari.dev/security/
- group: start
  title: ''
  type: Login
  url: https://www.kusari.dev/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kusari.cloud
- group: auth
  href: https://artifacts.apis.io/kusari/security/kusari-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kusari-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kusari/security/kusari-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kusari-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kusari.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kusari.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kusari.cloud/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kusari.dev/start/
- group: operate
  title: ''
  type: Support
  url: https://www.kusari.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://www.kusari.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kusari.dev/roi-calculator
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kusari.dev/terms
coverage:
  checked: '2026-10-29'
  detail: Documentation site renders via Docusaurus JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.kusari.cloud/reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Kusari provides software supply chain security solutions, offering a verified graph of every dependency shipped, built from source. Their platform enables reachability analysis, blast radius assessment, and automated fixes, integrating with existing CI pipelines and registries. Targeting complex stacks across financial services, insurance, and regulated SaaS, Kusari helps teams detect transitive CVEs, secrets, license issues, and end‑of‑life packages, delivering autonomous security reviews on pull requests.
image: https://www.kusari.dev/images/social/home.png
layout: provider
modified: '2026-10-29'
name: Kusari
nav: Providers
network: true
overview: 'Kusari is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Software Supply Chain, DevOps, and Open Source.


  Kusari''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kusari/kusari-2026-11-03T134602.png
security:
- kind: domain-security
  name: Kusari Domain Security
  slug: kusari-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kusari Vulnerability Disclosure
  slug: kusari-vulnerability-disclosure
  summary_line: no policy recorded
slug: kusari
tags:
- Company
- Security
- Software Supply Chain
- DevOps
- Open Source
website: https://www.kusari.dev/
---
