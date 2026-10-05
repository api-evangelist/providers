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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: BlockSec provides a Web3 security and compliance API suite covering AML, smart contract auditing, and threat detection.
  name: BlockSec API
  slug: blocksec-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blocksec/refs/heads/main/plans/blocksec-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blocksec-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blocksec/refs/heads/main/llms/blocksec-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blocksec-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blocksec/refs/heads/main/well-known/blocksec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blocksec-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blocksec/refs/heads/main/hosts/blocksec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocksec-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blocksec/refs/heads/main/vendors/blocksec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blocksec-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blocksec.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://blocksec.com/phalcon/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blocksec.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://blocksec.com/aml/pricing-affordable-crypto-aml-compliance-tool-small-vasp
- group: company
  title: ''
  type: Newsroom
  url: https://blocksec.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://app.blocksec.com/phalcon/network/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blocksecteam
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blocksec/refs/heads/main/security/blocksec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocksec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blocksec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blocksec.com
- group: company
  title: ''
  type: Blog
  url: https://blocksec.com/blog
created: '2026-09-29'
description: BlockSec is a Web3 security and compliance platform offering smart contract audits, infrastructure audits, blockchain penetration testing, AML/CFT compliance tools, and real‑time threat detection. Founded to protect decentralized applications and crypto enterprises, BlockSec provides a suite of products including Phalcon Security, Phalcon Compliance, MetaSleuth, and a public intelligence network for illicit fund monitoring.
image: https://assets.blocksec.com/image/1710749481735-4.jpg
layout: provider
modified: '2026-09-29'
name: BlockSec
nav: Providers
network: true
overview: 'BlockSec publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Blockchain, Web3, Compliance, and Auditing.


  BlockSec''s developer surface includes pricing, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Blocksec Plans Pricing
  plan_count: 5
  slug: blocksec-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocksec Domain Security
  slug: blocksec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blocksec
tags:
- Security
- Blockchain
- Web3
- Compliance
- Auditing
website: https://blocksec.com/
---
