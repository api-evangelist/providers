---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Helix Ml Webhooks
  slug: helix-ml-webhooks
common:
- group: other
  href: https://artifacts.apis.io/helix-ml/vendors/helix-ml-vendors.yml
  title: ''
  type: Vendors
  url: vendors/helix-ml-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/helix-ml/plans/helix-ml-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/helix-ml-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/helix-ml/asyncapi/helix-ml-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/helix-ml-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/helix-ml/authentication/helix-ml-authentication.yml
  title: ''
  type: Authentication
  url: authentication/helix-ml-authentication.yml
- group: design
  href: https://artifacts.apis.io/helix-ml/conformance/helix-ml-conformance.yml
  title: ''
  type: Conformance
  url: conformance/helix-ml-conformance.yml
- group: agent
  href: https://artifacts.apis.io/helix-ml/llms/helix-ml-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/helix-ml-llms.txt
- group: agent
  href: https://artifacts.apis.io/helix-ml/well-known/helix-ml-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/helix-ml-well-known.yml
- group: other
  href: https://artifacts.apis.io/helix-ml/hosts/helix-ml-hosts.yml
  title: ''
  type: Hosts
  url: hosts/helix-ml-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://helix.ml/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://helix.ml/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.helixml.tech/favicon.ico
- group: auth
  href: https://artifacts.apis.io/helix-ml/security/helix-ml-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/helix-ml-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://helix.ml/
- group: docs
  title: ''
  type: Documentation
  url: https://helix.ml/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://helix.ml/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://helix.ml/pricing
- group: company
  title: ''
  type: Blog
  url: https://helix.ml/blog
- group: operate
  title: ''
  type: Support
  url: https://helix.ml/contact
created: '2026-10-27'
description: HelixML provides a platform for agent virtualization, enabling software teams to run isolated agent desktops on their own infrastructure. Their offerings include Helix GTM for sales teams, Helix Cyber for penetration testing, and Helix Recruiter to streamline hiring. The platform runs on Helix Cloud, Kubernetes, and Linux/macOS, emphasizing security with SOC 2, ISO 27001 compliance, and support for private AI platforms. It targets enterprises seeking to reduce toil, improve security, and accelerate development through scalable, isolated environments.
layout: provider
modified: '2026-10-27'
name: HelixML
nav: Providers
network: true
overview: 'HelixML is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agent Virtualization, Security, and Cloud.


  The HelixML catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HelixML''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Helix Ml Plans Pricing
  plan_count: 7
  slug: helix-ml-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 31.0
    discoverability: 51.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/helix-ml/helix-ml-2026-11-03T133535.png
security:
- kind: authentication
  name: Helix Ml Authentication
  slug: helix-ml-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Helix Ml Domain Security
  slug: helix-ml-domain-security
  summary_line: TLSv1.3 · DMARC
slug: helix-ml
tags:
- Company
- Artificial Intelligence
- Agent Virtualization
- Security
- Cloud
website: https://helix.ml/
---
