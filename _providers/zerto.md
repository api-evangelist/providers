---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST API exposed by the Zerto Virtual Manager / Zerto Cloud Appliance for programmatic disaster-recovery management — VPGs, failover, checkpoints, VRAs, peer sites, alerts, events, tasks, and long-ter
  name: Zerto ZVM REST API
  slug: zerto-zvm-rest-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.zerto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.zerto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zerto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/saackerman/ZertoSwaggerAPI
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/ZertoPublic/zerto-api-quickstart
- group: auth
  href: https://artifacts.apis.io/zerto/authentication/zerto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zerto-authentication.yml
- group: design
  href: https://artifacts.apis.io/zerto/conventions/zerto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zerto-conventions.yml
- group: operate
  href: https://artifacts.apis.io/zerto/changelog/zerto-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zerto-changelog.yml
- group: design
  href: https://artifacts.apis.io/zerto/lifecycle/zerto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zerto-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/zerto/data-model/zerto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zerto-data-model.yml
- group: agent
  href: https://artifacts.apis.io/zerto/mcp/zerto-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zerto-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zerto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/zerto/llms/zerto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zerto-llms.txt
- group: build
  href: https://artifacts.apis.io/zerto/packages/zerto-packages.yml
  title: ''
  type: Packages
  url: packages/zerto-packages.yml
- group: build
  href: https://artifacts.apis.io/zerto/packages/zerto-packages.yml
  title: ''
  type: SDKs
  url: packages/zerto-packages.yml
- group: auth
  href: https://artifacts.apis.io/zerto/security/zerto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zerto-domain-security.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/ZertoPublic/PostmanCollections
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZertoPublic
- group: operate
  title: ''
  type: Support
  url: https://www.zerto.com/support-and-services/support/
- group: operate
  title: ''
  type: Community
  url: https://www.zerto.com/myzerto/forums/
- group: company
  title: ''
  type: Blog
  url: https://www.zerto.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zerto.com/try-or-buy/pricing-and-licensing/
- group: start
  title: ''
  type: SignUp
  url: https://www.zerto.com/try-or-buy/try-zerto-free/
created: '2026-07-17'
description: Zerto, a Hewlett Packard Enterprise company, provides continuous data protection (CDP), disaster recovery, ransomware resilience, and multi-cloud data mobility for on-premises and cloud workloads. Its ZVM (Zerto Virtual Manager), ZCA (Zerto Cloud Appliance), and ZIC (Zerto In-Cloud) appliances expose a REST API under /v1, authenticated through an embedded Keycloak OAuth2 identity provider. The API lets teams manage Virtual Protection Groups (VPGs), orchestrate non-disruptive failover tests and live failover/failback, browse recovery checkpoints, run file- and VM-level restores, manage long-term retention repositories, and consume alerts and events — everything the Zerto UI does, driven programmatically. Zerto publishes an official PowerShell SDK, plus Python, Ansible, Terraform, and Postman examples via its ZertoPublic GitHub organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zerto.png
layout: provider
modified: '2026-07-21'
name: Zerto
nav: Providers
network: true
overview: 'Zerto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Disaster Recovery, Data Protection, Backup, and Ransomware Resilience.


  Zerto''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 16 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 29.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zerto/zerto-2026-09-02T171653.png
security:
- kind: authentication
  name: Zerto Authentication
  slug: zerto-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Zerto Domain Security
  slug: zerto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Authenticate to the Zerto API
  slug: zerto-authenticate
- name: Run a non-disruptive failover test
  slug: zerto-run-failover-test
- name: Triage and dismiss alerts
  slug: zerto-triage-alerts
- name: Report every VPG and its RPO
  slug: zerto-vpg-rpo-report
slug: zerto
tags:
- Company
- Disaster Recovery
- Data Protection
- Backup
- Ransomware Resilience
- Business Continuity
- Cloud Migration
- Replication
- Infrastructure
website: https://www.zerto.com/
---
