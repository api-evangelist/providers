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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/drillspark-io/conformance/drillspark-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drillspark-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drillspark-io/llms/drillspark-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drillspark-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/drillspark-io/well-known/drillspark-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drillspark-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/drillspark-io/hosts/drillspark-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drillspark-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/drillspark-io/vendors/drillspark-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drillspark-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drillspark.io/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://drillspark.io/ja/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drillspark.io/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://drillspark.io/ja/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://drillspark.io/en/templates/saas-onboarding
- group: auth
  href: https://artifacts.apis.io/drillspark-io/security/drillspark-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drillspark-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drillspark.io/
coverage:
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://drillspark.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DrillSpark provides an AI-powered platform that visualizes and automates work processes. By simply speaking about tasks, the AI maps the entire workflow, identifies automation opportunities, and eliminates repetitive work, allowing users to focus on what they love. The service is offered for free and aims to increase productivity through intelligent automation.
image: https://drillspark.io/og-image.png
layout: provider
modified: '2026-11-05'
name: DrillSpark
nav: Providers
network: true
overview: 'DrillSpark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Productivity, Workflows, and Company.


  DrillSpark''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 10.5
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drillspark Io Domain Security
  slug: drillspark-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: drillspark-io
tags:
- Artificial Intelligence
- Automation
- Productivity
- Workflows
- Company
website: https://drillspark.io/
---
