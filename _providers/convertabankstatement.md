---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/convertabankstatement/refs/heads/main/hosts/convertabankstatement-hosts.yml
  title: ''
  type: Hosts
  url: hosts/convertabankstatement-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/convertabankstatement/refs/heads/main/vendors/convertabankstatement-vendors.yml
  title: ''
  type: Vendors
  url: vendors/convertabankstatement-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/convertabankstatement/refs/heads/main/security/convertabankstatement-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convertabankstatement-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://convertabankstatement.com/
- group: docs
  title: ''
  type: Documentation
  url: https://convertabankstatement.com/docs
- group: company
  title: ''
  type: Blog
  url: https://convertabankstatement.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://convertabankstatement.com/docs#getting-started
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://convertabankstatement.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Convertabankstatement provides a platform that enables users to transform bank statement data into standardized, machine‑readable formats. By offering robust APIs, the service supports automated ingestion, categorization, and reconciliation of financial transactions for fintech applications, accounting software, and personal finance tools. The solution emphasizes security, compliance with banking standards, and scalability to handle high‑volume data streams, helping businesses streamline financial workflows and gain actionable insights.
image: https://mgx-backend-cdn.metadl.com/mgx-backend-1300249583/chats/logo/6047413e81274f1a9367982bc1ca360d.png
layout: provider
modified: '2026-10-16'
name: Convertabankstatement
nav: Providers
network: true
overview: 'Convertabankstatement is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, and DataTransformation.


  Convertabankstatement''s developer surface includes documentation, engineering blog, getting-started guide, and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 39.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Convertabankstatement Domain Security
  slug: convertabankstatement-domain-security
  summary_line: TLSv1.3
slug: convertabankstatement
tags:
- Company
- Fintech
- Banking
- DataTransformation
website: https://convertabankstatement.com/
---
