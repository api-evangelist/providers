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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Datachain Webhooks
  slug: datachain-webhooks
common:
- group: design
  href: https://artifacts.apis.io/datachain/asyncapi/datachain-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/datachain-webhooks.yml
- group: other
  href: https://artifacts.apis.io/datachain/hosts/datachain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datachain-hosts.yml
- group: other
  href: https://artifacts.apis.io/datachain/vendors/datachain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datachain-vendors.yml
- group: build
  href: https://artifacts.apis.io/datachain/packages/datachain-packages.yml
  title: ''
  type: SDKs
  url: packages/datachain-packages.yml
- group: build
  href: https://artifacts.apis.io/datachain/packages/datachain-packages.yml
  title: ''
  type: Packages
  url: packages/datachain-packages.yml
- group: start
  title: ''
  type: Login
  url: https://studio.datachain.ai/auth/sign-in
- group: other
  title: ''
  type: Leadership
  url: https://www.datachain.ai/team
- group: auth
  href: https://artifacts.apis.io/datachain/security/datachain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datachain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datachain.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.datachain.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.datachain.ai/docs/getting-started/agents
- group: company
  title: ''
  type: Blog
  url: https://www.datachain.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datachain.ai/contact-sales
- group: operate
  title: ''
  type: Support
  url: https://www.datachain.ai/security-and-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datachain.ai/privacy-policy
coverage:
  checked: '2026-10-24'
  detail: Documentation site renders via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.datachain.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: DataChain provides a platform to curate, enrich, and version AI datasets. It enables developers to ingest massive video and sensor data, apply AI agents for labeling, curate datasets, and stream them into training pipelines. Trusted by startups and Fortune 500 companies, DataChain offers tools for dataset versioning, quality assurance, and collaborative data management across the AI lifecycle.
image: https://www.datachain.ai/social-image?title=Your+coding+agent+can+now+work+with+massive+video+and+sensor+data&variant=main
layout: provider
modified: '2026-10-24'
name: DataChain
nav: Providers
network: true
overview: 'DataChain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Management, Platform, Machine Learning, and Datasets.


  The DataChain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DataChain''s developer surface includes documentation, getting-started guide, engineering blog, pricing, support, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 21.4
    discoverability: 49.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/datachain/datachain-2026-11-03T130237.png
security:
- kind: domain-security
  name: Datachain Domain Security
  slug: datachain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datachain
tags:
- Artificial Intelligence
- Data Management
- Platform
- Machine Learning
- Datasets
- Company
website: https://datachain.ai
---
