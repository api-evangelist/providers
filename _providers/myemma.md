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
    agent_skills: unknown
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
    mcp_server: false
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
  score: 17.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/myemma/plans/myemma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/myemma-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/myemma/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/myemma/changelog/myemma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/myemma-changelog.yml
- group: auth
  href: https://artifacts.apis.io/myemma/well-known/myemma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/myemma-security.txt
- group: agent
  href: https://artifacts.apis.io/myemma/well-known/myemma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/myemma-well-known.yml
- group: other
  href: https://artifacts.apis.io/myemma/hosts/myemma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/myemma-hosts.yml
- group: other
  href: https://artifacts.apis.io/myemma/vendors/myemma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/myemma-vendors.yml
- group: build
  href: https://artifacts.apis.io/myemma/packages/myemma-packages.yml
  title: ''
  type: SDKs
  url: packages/myemma-packages.yml
- group: build
  href: https://artifacts.apis.io/myemma/packages/myemma-packages.yml
  title: ''
  type: Packages
  url: packages/myemma-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.myemma.com/
- group: auth
  title: ''
  type: Security
  url: https://myemma.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myemma.com/legal/privacy-notice/
- group: commercial
  title: ''
  type: Pricing
  url: https://myemma.com/product/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://myemma.com/customers/newsroom/
- group: start
  title: ''
  type: Login
  url: https://myemma.com/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://myemma.com/customers/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://myemma.com/resources/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.myemma.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myemma
- group: auth
  href: https://artifacts.apis.io/myemma/security/myemma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/myemma-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/myemma/security/myemma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myemma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myemma.com/
coverage:
  checked: '2026-10-27'
  detail: The Emma API documentation is HTML only and provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://api.myemma.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Emma provides an email marketing platform that helps businesses design, personalize, segment, and automate targeted email campaigns. The service focuses on delivering measurable results through advanced analytics, A/B testing, and integration with various CRM and e‑commerce tools. Emma’s platform aims to improve customer engagement and drive revenue growth for marketers of all sizes.
layout: provider
modified: '2026-10-27'
name: Emma
nav: Providers
network: true
overview: 'Emma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Automation, Artificial Intelligence, SMS, and Higher Education.


  Emma''s developer surface includes changelog, pricing, engineering blog, documentation, and 18 more developer resources.'
plans:
- name: Myemma Plans Pricing
  plan_count: 3
  slug: myemma-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 45.5
    operational_transparency: 23.7
  previous_composite: 29.3
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/myemma/myemma-2026-11-03T135936.png
security:
- kind: domain-security
  name: Myemma Domain Security
  slug: myemma-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Myemma Vulnerability Disclosure
  slug: myemma-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: myemma
tags:
- Email Marketing
- Automation
- Artificial Intelligence
- SMS
- Higher Education
- Non-Profit
- Government
- Travel & Hospitality
website: https://myemma.com/
---
