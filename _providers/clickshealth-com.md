---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://clickshealth.com/security
- group: auth
  href: https://artifacts.apis.io/clickshealth-com/authentication/clickshealth-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clickshealth-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/clickshealth-com/llms/clickshealth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickshealth-com-llms.txt
- group: other
  href: https://artifacts.apis.io/clickshealth-com/a2a/clickshealth-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clickshealth-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clickshealth-com/well-known/clickshealth-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickshealth-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clickshealth-com/hosts/clickshealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clickshealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clickshealth-com/vendors/clickshealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clickshealth-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://clickshealth.com/status
- group: auth
  title: ''
  type: Security
  url: https://clickshealth.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://clickshealth.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clickshealth.com/api/introduction
- group: auth
  href: https://artifacts.apis.io/clickshealth-com/security/clickshealth-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clickshealth-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clickshealth-com/security/clickshealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickshealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clickshealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.clickshealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clickshealth.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://clickshealth.com/guides/how-to-choose-your-first-ai-workflow
- group: company
  title: ''
  type: Blog
  url: https://clickshealth.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickshealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickshealth.com/privacy-policy
created: '2026-10-24'
description: Clicks Health provides AI-driven automation for revenue cycle management in healthcare, offering solutions for patient access, prior authorization, claims and denials, and repetitive workflow automation. Their platform integrates with existing EHR and payer systems to streamline processes, reduce manual effort, and improve financial outcomes for providers.
image: https://clickshealth.com/opengraph-image?32c67500ac68fcb9
layout: provider
modified: '2026-10-24'
name: Clicks
nav: Providers
network: true
overview: 'Clicks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Revenue Cycle Management, and Automation.


  Clicks'' developer surface includes authentication, changelog, API reference, documentation, getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 55.4
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clickshealth-com/clickshealth-com-2026-11-03T124419.png
security:
- kind: authentication
  name: Clickshealth Com Authentication
  slug: clickshealth-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clickshealth Com Domain Security
  slug: clickshealth-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Clickshealth Com Trust Center
  slug: clickshealth-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: clickshealth-com
tags:
- Company
- Healthcare
- Artificial Intelligence
- Revenue Cycle Management
- Automation
website: https://clickshealth.com/
---
