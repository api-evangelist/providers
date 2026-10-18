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
api_count: 1
apis:
- description: API for LabArchives electronic lab notebook platform
  name: LabArchives API
  slug: labarchives-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/labarchives/refs/heads/main/plans/labarchives-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/labarchives-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.labarchives.com/security-compliance
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/labarchives/refs/heads/main/llms/labarchives-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/labarchives-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/labarchives/refs/heads/main/hosts/labarchives-hosts.yml
  title: ''
  type: Hosts
  url: hosts/labarchives-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/labarchives/refs/heads/main/vendors/labarchives-vendors.yml
  title: ''
  type: Vendors
  url: vendors/labarchives-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.labarchives.com/terms-of-use
- group: commercial
  title: ''
  type: Pricing
  url: https://www.labarchives.com/pricing
- group: start
  title: ''
  type: Login
  url: https://mynotebook.labarchives.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.labarchives.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/labarchives/refs/heads/main/security/labarchives-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/labarchives-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/labarchives/refs/heads/main/security/labarchives-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/labarchives-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.labarchives.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.labarchives.com/hc/en-us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.labarchives.com/mcp
  - status: 200
    url: https://www.labarchives.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: LabArchives provides a modern electronic lab notebook (ELN) platform that helps researchers record, organize, search, and share scientific data. It offers solutions for research, inventory management, scheduling, government compliance, education, and startups, integrating with tools like SnapGene, GraphPad Prism, Geneious, and Microsoft. The service emphasizes data security, compliance, and collaborative workflows for labs of all sizes.
image: https://cdn.labarchives.com/assets/22.5.0/assets/images/dotmatics/lab-archives/meta/preview-labrchives-dotmatics.png
layout: provider
modified: '2026-10-12'
name: LabArchives
nav: Providers
network: true
overview: 'LabArchives is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ELN, Data Management, Research, and Collaboration.


  LabArchives'' developer surface includes pricing, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Labarchives Plans Pricing
  plan_count: 10
  slug: labarchives-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Labarchives Domain Security
  slug: labarchives-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Labarchives Trust Center
  slug: labarchives-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: labarchives
tags:
- Company
- ELN
- Data Management
- Research
- Collaboration
website: https://www.labarchives.com
---
