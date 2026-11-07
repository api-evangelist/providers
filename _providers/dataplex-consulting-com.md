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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only static catalog of Dataplex healthcare data products with 100-row real samples.
  name: Dataplex Agent API
  slug: dataplex-agent-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/dataplex-consulting-com/rules/dataplex-consulting-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dataplex-consulting-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dataplex-consulting-com/conformance/dataplex-consulting-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataplex-consulting-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/dataplex-consulting-com/plans/dataplex-consulting-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataplex-consulting-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dataplex-consulting-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dataplex-consulting-com/llms/dataplex-consulting-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataplex-consulting-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dataplex-consulting-com/well-known/dataplex-consulting-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataplex-consulting-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataplex-consulting-com/hosts/dataplex-consulting-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataplex-consulting-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataplex-consulting-com/vendors/dataplex-consulting-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataplex-consulting-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dataplex-consulting.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataplex-consulting.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dataplex-consulting.com/readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dataplex-consulting
- group: auth
  href: https://artifacts.apis.io/dataplex-consulting-com/security/dataplex-consulting-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataplex-consulting-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataplex-consulting.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dataplex-consulting.com
- group: company
  title: ''
  type: About
  url: https://www.dataplex-consulting.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dataplex-consulting.com
- group: start
  title: ''
  type: SignUp
  url: https://trial.dataplex-consulting.com
created: '2026-11-05'
description: Dataplex Consulting provides analysis‑ready public healthcare data products delivered on platforms such as Snowflake, Databricks, Google Cloud, and SAP. They transform free government and public data into dependable, ready‑to‑use datasets for enterprises, supporting marketplace channels and data‑driven decision making.
image: https://framerusercontent.com/images/jYw9t6EnfEL4XLn7iQES1F1jz8Y.png
layout: provider
modified: '2026-11-05'
name: Dataplex Consulting
nav: Providers
network: true
overview: 'Dataplex Consulting publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Healthcare, Analytics, and Cloud.


  The Dataplex Consulting catalog on APIs.io includes 1 Spectral governance ruleset.


  Dataplex Consulting''s developer surface includes getting-started guide, documentation, API reference, signup flow, and 14 more developer resources.'
plans:
- name: Dataplex Consulting Com Plans Pricing
  plan_count: 4
  slug: dataplex-consulting-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Dataplex Consulting API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: dataplex-consulting-com-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataplex Consulting Com Domain Security
  slug: dataplex-consulting-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dataplex-consulting-com
tags:
- Company
- Data
- Healthcare
- Analytics
- Cloud
website: https://dataplex-consulting.com/
---
