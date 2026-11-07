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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Dataimporter provides a Salesforce data migration API documented at the Help Center. No machine‑readable contract was found despite probing known OpenAPI locations.
  name: Dataimporter API
  slug: dataimporter-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dataimporter/plans/dataimporter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataimporter-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dataimporter.io/security
- group: agent
  href: https://artifacts.apis.io/dataimporter/llms/dataimporter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataimporter-llms.txt
- group: agent
  href: https://artifacts.apis.io/dataimporter/well-known/dataimporter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataimporter-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataimporter/hosts/dataimporter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataimporter-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataimporter/vendors/dataimporter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataimporter-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dataimporter.io/security
- group: start
  title: ''
  type: Sandbox
  url: https://app.dataimporter.io/login/sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.dataimporter.io/changelog
- group: auth
  href: https://artifacts.apis.io/dataimporter/security/dataimporter-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dataimporter-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dataimporter/security/dataimporter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataimporter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataimporter.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dataimporter.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.dataimporter.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dataimporter.io/load
- group: operate
  title: ''
  type: Support
  url: https://help.dataimporter.io/
- group: company
  title: ''
  type: Blog
  url: https://www.dataimporter.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dataimporter.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.dataimporter.io/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dataimporter.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataimporter.io/privacy-policy
coverage:
  checked: '2026-10-20'
  detail: Probing standard OpenAPI endpoints on api.dataimporter.io and app.dataimporter.io returned only 404 or 401 responses, and no machine‑readable spec was discovered.
  evidence:
  - status: 404
    url: https://api.dataimporter.io/openapi.json
  - status: 404
    url: https://app.dataimporter.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Dataimporter provides a Salesforce data migration, import, and backup platform that enables users to load data from CSV, Excel, S3, FTP, or databases into Salesforce, automate scheduled jobs, and create flows. It offers tools for consultants, ISVs, and enterprises to streamline data loading, migrations, and backups with versioning, rollback, and security features.
image: https://cdn.prod.website-files.com/6067901f981fe62dc3adc948/613e82c09900f82b8e27afa8_Copy%20of%20dataimporter%20(2)%20(1).png
layout: provider
modified: '2026-10-20'
name: Dataimporter
nav: Providers
network: true
overview: 'Dataimporter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Salesforce, Data Migration, Import, and Backup.


  Dataimporter''s developer surface includes sandbox, changelog, documentation, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Dataimporter Plans Pricing
  plan_count: 4
  slug: dataimporter-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.4
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 13.2
  previous_composite: 38.7
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/dataimporter/dataimporter-2026-11-03T130204.png
security:
- kind: domain-security
  name: Dataimporter Domain Security
  slug: dataimporter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dataimporter Trust Center
  slug: dataimporter-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: dataimporter
tags:
- Company
- Salesforce
- Data Migration
- Import
- Backup
website: https://dataimporter.io/
---
