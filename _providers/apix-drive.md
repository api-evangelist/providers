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
    event_surface_described: unknown
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
  score: 3.9
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/apix-drive/plans/apix-drive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apix-drive-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apix-drive/conformance/apix-drive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apix-drive-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apix-drive/llms/apix-drive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apix-drive-llms.txt
- group: other
  href: https://artifacts.apis.io/apix-drive/hosts/apix-drive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apix-drive-hosts.yml
- group: other
  href: https://artifacts.apis.io/apix-drive/vendors/apix-drive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apix-drive-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://apix-drive.com/en/integrations/slack/webhook
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.apix-drive.com/
- group: auth
  href: https://artifacts.apis.io/apix-drive/security/apix-drive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apix-drive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apix-drive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apix-drive.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apix-drive.com/en/docs/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apix-drive.com/en/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apix-drive.com/en/docs/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://apix-drive.com/en/rates
- group: company
  title: ''
  type: Blog
  url: https://apix-drive.com/en/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://apix-drive.com/en/help
- group: start
  title: ''
  type: SignUp
  url: https://apix-drive.com/en/signup
coverage:
  checked: '2026-10-20'
  detail: OpenAPI endpoint https://apix-drive.com/api/openapi.json returns unauthorized error, indicating authentication required.
  evidence:
  - status: 200
    url: https://apix-drive.com/api/openapi.json
  reason: sales-gate
  state: gated
created: '2026-10-20'
description: ApiX-Drive is a no‑code integration platform enabling businesses to automate workflows across over 600 pre‑built connectors, serving more than 120,000 users worldwide. The cloud‑based service offers a visual builder, multi‑language support, a free trial, and a marketplace featuring integrations like Google Sheets, Slack, Mailchimp, and OpenAI. It focuses on rapid deployment, ease of use, and reducing manual effort, positioning itself as a SaaS solution for marketing, CRM, and productivity automation.
image: https://apix-drive.com/landing/images/apix_drive_info.jpg
layout: provider
modified: '2026-10-20'
name: ApiX-Drive
nav: Providers
network: true
overview: 'ApiX-Drive publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, No-Code, Automation, and Marketing.


  ApiX-Drive''s developer surface includes documentation, API reference, pricing, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Apix Drive Plans Pricing
  plan_count: 9
  slug: apix-drive-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 3.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/apix-drive/apix-drive-2026-11-03T121015.png
security:
- kind: domain-security
  name: Apix Drive Domain Security
  slug: apix-drive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: apix-drive
tags:
- Company
- Integration
- No-Code
- Automation
- Marketing
website: https://apix-drive.com/
---
