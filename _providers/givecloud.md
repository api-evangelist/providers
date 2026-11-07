---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer documentation for Givecloud's fundraising platform APIs.
  name: Givecloud API
  slug: givecloud-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/givecloud/plans/givecloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/givecloud-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/givecloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://help.givecloud.com/en/articles/6045181-security
- group: auth
  href: https://artifacts.apis.io/givecloud/authentication/givecloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/givecloud-authentication.yml
- group: agent
  href: https://artifacts.apis.io/givecloud/llms/givecloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/givecloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/givecloud/well-known/givecloud-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/givecloud-help-security.txt
- group: agent
  href: https://artifacts.apis.io/givecloud/well-known/givecloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/givecloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/givecloud/hosts/givecloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/givecloud-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://givecloud.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.givecloud.com
- group: auth
  title: ''
  type: Security
  url: https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w?utm_source=chatgpt.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://givecloud.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.givecloud.com/
- group: company
  title: ''
  type: Blog
  url: https://givecloud.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.givecloud.com/en/articles/11132883-getting-started-with-givecloud
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/givecloud
- group: auth
  href: https://artifacts.apis.io/givecloud/security/givecloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/givecloud-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/givecloud/security/givecloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/givecloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://givecloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://givecloud.com/about/
- group: auth
  title: ''
  type: SecurityCompliance
  url: https://givecloud.com/security-compliance/
- group: operate
  title: ''
  type: Support
  url: https://givecloud.com/support-onboarding/
- group: commercial
  title: ''
  type: Pricing
  url: https://givecloud.com/pricing/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.givecloud.com/
- group: other
  title: ''
  type: Resources
  url: https://givecloud.com/resources/
coverage:
  checked: '2026-10-27'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://developers.givecloud.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Givecloud provides a fundraising platform that helps nonprofits increase donor engagement, streamline operations, and boost recurring giving. Their solution includes donation forms, membership management, sponsorships, online stores, impact‑giving experiences, and integrated tools for email automation, event registration, and virtual point‑of‑sale. Trusted by thousands of organizations, Givecloud aims to make fundraising feel better and work better for both donors and nonprofits.
image: https://givecloud.com/wp-content/uploads/2023/03/Group-15.png
layout: provider
modified: '2026-10-27'
name: Givecloud
nav: Providers
network: true
overview: 'Givecloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Non-Profit, Software-as-a-Service, and Platform.


  Givecloud''s developer surface includes authentication, engineering blog, getting-started guide, documentation, support, pricing, and 19 more developer resources.'
plans:
- name: Givecloud Plans Pricing
  plan_count: 4
  slug: givecloud-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 37.4
    discoverability: 64.3
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/givecloud/givecloud-2026-11-03T132832.png
security:
- kind: authentication
  name: Givecloud Authentication
  slug: givecloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Givecloud Domain Security
  slug: givecloud-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Givecloud Trust Center
  slug: givecloud-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: givecloud
tags:
- Company
- Fundraising
- Non-Profit
- Software-as-a-Service
- Platform
website: https://givecloud.com/
---
