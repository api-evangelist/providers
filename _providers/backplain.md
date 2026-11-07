---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  score: 6.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Backplain provides AI-powered data governance APIs as described in their developer portal.
  name: Backplain API
  slug: backplain-api
artifact_total: 5
common:
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.backplain.com/register
- group: start
  title: ''
  type: GettingStarted
  url: https://support.backplain.com/getting-started
- group: commercial
  href: https://artifacts.apis.io/backplain/plans/backplain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/backplain-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://backplain.com/security
- group: agent
  href: https://artifacts.apis.io/backplain/llms/backplain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backplain-llms.txt
- group: auth
  href: https://artifacts.apis.io/backplain/well-known/backplain-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/backplain-support-security.txt
- group: auth
  href: https://artifacts.apis.io/backplain/well-known/backplain-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/backplain-security.txt
- group: agent
  href: https://artifacts.apis.io/backplain/well-known/backplain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backplain-well-known.yml
- group: other
  href: https://artifacts.apis.io/backplain/hosts/backplain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backplain-hosts.yml
- group: other
  href: https://artifacts.apis.io/backplain/vendors/backplain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backplain-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://backplain.com/status
- group: auth
  title: ''
  type: Security
  url: https://backplain.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://backplain.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://dev.backplain.com/
- group: auth
  href: https://artifacts.apis.io/backplain/security/backplain-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/backplain-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/backplain/security/backplain-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/backplain-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/backplain/security/backplain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backplain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backplain.com/
- group: operate
  title: ''
  type: Support
  url: https://support.backplain.com
- group: company
  title: ''
  type: Blog
  url: https://backplain.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://backplain.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backplain.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backplain.com/privacy
coverage:
  checked: '2026-10-16'
  detail: API endpoints return 403 for OpenAPI files, and no machine‑readable spec is published.
  evidence:
  - status: 403
    url: https://api.backplain.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Backplain provides AI-powered data governance and secure multi‑model AI workspaces for regulated enterprises. Their platform offers a patent‑pending AI Firewall, sovereign compute options, and a unified interface to 47 frontier models, enabling teams to harness powerful language models while ensuring data privacy and compliance. Backplain serves legal, biotech, defense, and other regulated industries with customizable plans, audit logs, and robust security controls.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/c1e74f51-a824-4caf-914f-e5c09ea37c4b/id-preview-c2680e9f--1e1b191c-4f7a-4357-91c6-2b7304cab379.lovable.app-1777697954675.png
layout: provider
modified: '2026-10-16'
name: Backplain
nav: Providers
network: true
overview: 'Backplain is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Governance, Security, and Enterprise.


  Backplain''s developer surface includes signup flow, getting-started guide, documentation, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Backplain Plans Pricing
  plan_count: 1
  slug: backplain-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 65.2
    operational_transparency: 13.2
  previous_composite: 34.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/backplain/backplain-2026-11-03T121514.png
security:
- kind: domain-security
  name: Backplain Domain Security
  slug: backplain-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Backplain Vulnerability Disclosure
  slug: backplain-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Backplain Trust Center
  slug: backplain-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: backplain
tags:
- Company
- Artificial Intelligence
- Data Governance
- Security
- Enterprise
website: https://backplain.com/
---
