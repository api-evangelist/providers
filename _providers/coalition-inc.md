---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coalition Inc Agentic Access
  operation_count: 7
  slug: coalition-inc-agentic-access
  summary_line: 7 operations
api_count: 2
apis:
- description: Partner-gated REST API that brokers and distribution partners use to rate, quote, bind, generate documents (quote PDF, Coalition Risk Assessment, signature bundle, specimen policy), and manage renewal
  name: Coalition Active Insurance API
  slug: active-insurance-api
- description: The Cve API from Coalition — 7 operation(s) for cve.
  name: Coalition Cve API
  slug: coalition-inc-cve-api
artifact_total: 19
collections:
- collection_type: open
  name: Coalition Exploit Scoring System API
  slug: open-coalition-ess
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coalition-inc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coalition-inc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coalition-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coalitioninc.com
- group: company
  title: ''
  type: About
  url: https://www.coalitioninc.com/about
- group: other
  title: ''
  type: Products
  url: https://www.coalitioninc.com/cyber-insurance
- group: other
  title: ''
  type: Control
  url: https://www.coalitioninc.com/control
- group: auth
  title: ''
  type: Security
  url: https://www.coalitioninc.com/security
- group: other
  title: ''
  type: ExploitScoringSystem
  url: https://ess.coalitioninc.com
- group: other
  title: ''
  type: BrokerIQ
  url: https://www.coalitioninc.com/brokers/broker-iq
- group: other
  title: ''
  type: API
  url: https://www.coalitioninc.com/brokers/api
- group: company
  title: ''
  type: Partners
  url: https://www.coalitioninc.com/serviceproviders
- group: company
  title: ''
  type: Partnership
  url: https://web.coalitioninc.com/partnership.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.coalitioninc.com/newsroom
- group: other
  title: ''
  type: Announcements
  url: https://www.coalitioninc.com/announcements
- group: company
  title: ''
  type: Blog
  url: https://www.coalitioninc.com/blog
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.coalitioninc.com/knowledge-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.coalitioninc.com
- group: company
  title: ''
  type: Careers
  url: https://www.coalitioninc.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.coalitioninc.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coalitioninc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SolveCyberRisk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCoc7ed_HZrl-Ln4ZCnDsuZA
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/coalitioninc
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/coalitioninc
created: '2026-05-25'
description: Coalition is a San Francisco–headquartered cyber insurance and active risk management provider founded in 2017 by Joshua Motta (CEO) and John Hering. Coalition pairs commercial insurance lines — Cyber, Technology Errors & Omissions, Executive Risks (D&O, EPL, Fiduciary, Crime), Miscellaneous Professional Liability, and AI coverage — with a continuous attack-surface monitoring and incident-response platform (Coalition Control, Wirespeed ADR, Coalition Incident Response, Security Awareness Training). The company's underwriting engine is exposed to brokers and distribution partners through the Coalition Active Insurance API, a RESTful surface that supports rate, quote, bind, document generation, renewals, and webhook events across the United States and Canada, with executive risks APIs and additional product lines added over time. Coalition also publishes a public Exploit Scoring System (ESS) API at ess-api.coalitioninc.com that exposes CVE detail, ESS/EPSS/CVSS scoring, exploit
  references (ExploitDB, Metasploit), GitHub repository signals, and Twitter mention timelines for over 200,000 vulnerabilities. Coalition is backed by Allianz X, Valor Equity Partners, Ribbit Capital, Mitsui Sumitomo, Kinetic Partners and other strategic insurers (Allianz, Arch, Ascot, Zurich, Swiss Re, Lloyd's syndicates); it raised a $250M Series F in 2022 at a $5B valuation. The Active Insurance API is partner-gated (no public OpenAPI), but the ESS API is fully public with OpenAPI 3.1, an interactive docs UI, and ReDoc.
examples:
- key_count: 2
  name: Coalition Ess Getcve Example
  slug: coalition-ess-getCve-example
- key_count: 2
  name: Coalition Ess Getesshistory Example
  slug: coalition-ess-getEssHistory-example
- key_count: 2
  name: Coalition Ess Listcves Example
  slug: coalition-ess-listCves-example
- key_count: 2
  name: Coalition Ess Listgithubrepos Example
  slug: coalition-ess-listGithubRepos-example
finops:
- name: Coalition Inc Finops
  service_category: Insurance / Developer API
  slug: coalition-inc-finops
graphqls:
- description: This conceptual GraphQL schema models the Coalition Active Insurance API and Exploit Scoring System (ESS) API as a unified graph. Coalition is a cyber insurance and active risk management provider tha
  name: Coalition GraphQL Schema
  slug: coalition-inc-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coalition-inc.png
json_schemas:
- name: Coalition ESS CVE
  property_count: 13
  slug: coalition-ess-cve
json_structures:
- name: Coalition Ess Cve Structure
  property_count: 0
  slug: coalition-ess-cve-structure
jsonld:
- class_count: 27
  name: Coalition Inc Context
  property_count: 0
  slug: coalition-inc-context
layout: provider
modified: '2026-05-25'
name: Coalition
nav: Providers
network: true
overview: 'Coalition publishes 1 API on the [APIs.io](https://apis.io/) network: Cve API. Tagged areas include Cyber Insurance, Insurance, Insurtech, Risk Management, and Cybersecurity.


  The Coalition catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Coalition''s developer surface includes engineering blog, YouTube channel, and 23 more developer resources.'
plans:
- name: Coalition Inc Plans Pricing
  plan_count: 3
  slug: coalition-inc-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Coalition Inc Rate Limits
  slug: coalition-inc-rate-limits
rules:
- name: Coalition API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 5
  slug: coalition-ess-rules
- name: Coalition API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: coalition-inc-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.3
    developer_ergonomics: 6.5
    discoverability: 59.3
    governance: 47.9
    operational_transparency: 42.1
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coalition-inc/refs/heads/main/screenshots/coalition-inc-2026-06-20T174644.png
security:
- kind: domain-security
  name: Coalition Inc Domain Security
  slug: coalition-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coalition Inc Vulnerability Disclosure
  slug: coalition-inc-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: coalition-inc
tags:
- Cyber Insurance
- Insurance
- Insurtech
- Risk Management
- Cybersecurity
- Vulnerability Management
- CVE
- Exploit Scoring
- Threat Intelligence
- Incident Response
- Attack Surface Management
- Brokers
- MGA
- Executive Risks
- Technology E&O
- Active Insurance
website: https://www.coalitioninc.com
---
